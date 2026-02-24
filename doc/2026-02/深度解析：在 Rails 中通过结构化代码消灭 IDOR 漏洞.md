#  深度解析：在 Rails 中通过结构化代码消灭 IDOR 漏洞  
原创 Pwn1
                        Pwn1  漏洞集萃   2026-02-24 01:19  
  
   
  
> **免责声明**  
  
本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。  
  
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
1.    
  
1.    
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
来源:  
  
https://pentesterlab.com/blog/killing-idors-in-rail  
  
在 Ruby on Rails  
 里，有一个经常被人提到的优点，就是它把很多日常开发流程都做得非常顺手、非常省事。在我们编写业务代码时，很多常见操作都被简化到了几乎“顺手一写就能跑”的程度。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/jow1el0IZibzlbwoTiaRf3zJa3H0cxKqfvMHXicjeE958xhBFqalGEmuJahWjSIdWdcVpnjWwqxhHCjOXjbIdpJMfdIzkMXmBHWpgmv8OAf2gE/640?wx_fmt=png&from=appmsg "")  
  
  
例如，如果你想取出一条记录，通常只需要一行代码：  
```
@project = Project.find(params[:id])
```  
  
如果你想加一个授权检查，接着在下面补一行代码即可。这种写法的可读性不错，结构清晰，在代码审查（Code Review）时也容易通过。  
### 简洁背后的隐患  
  
正是因为这种“太顺手”的风格，一些技术实力强、节奏快的团队，反而容易在不经意间发布带有 **IDOR**  
 问题的系统。问题不在于开发者不知道要做授权检查，而在于这种**“先获取对象，再做检查”**的模式本质上在依赖**  
人脑记忆**。  
  
只要在写新端点、重构或写脚本时漏掉那一行检查，后果往往非常严重。因此，彻底消灭 **IDOR**  
 的核心不在于多写检查语句，而在于**从结构上改变代码组织方式**  
，让写出不安全代码变得困难。  
## 1. 永不腐朽的授权模式  
  
在传统的 Rails  
 项目中，常见的写法如下：  
```
@project = Project.find(params[:id])authorize! @project
```  
  
这种结构非常脆弱。当项目演进，有人新增 Controller Action  
 忘记写 authorize!  
，或者在导出接口中复用了查询逻辑，漏洞就会产生。  
### 从“布尔值检查”转向“数据集边界”  
  
更稳妥的做法是：不要先加载记录再问“能不能看”，而是直接向数据库询问**“该用户能看的记录集合是什么”**。  
- **普通关联查询：**  
  
```
@project = current_user.projects.find(params[:id])
```  
- **多租户应用：**  
  
```
@invoice = current_account.invoices.find(params[:id])
```  
  
**这种方式的优势：**  
1. **自动处理异常：**  
 如果用户无权访问，Rails  
 会直接抛出 ActiveRecord::RecordNotFound  
，流程立即终止。  
  
1. **防止元数据泄露：**  
 记录压根不会进入内存，避免了在日志或模板渲染中意外泄露对象信息。  
  
1. **安全性内建：**  
 授权规则不再是易忘的插件，而是查询语句本身的一部分。  
  
## 2. 默认作用域带来的“超能力”错觉  
  
当开发者习惯了作用域，往往会倾向于使用 default_scope  
 来实现自动过滤。例如**软删除（Soft Delete）**  
：  
```
class Product < ApplicationRecord  default_scope { where(deleted_at: nil) }end
```  
  
此时执行 Product.all  
，生成的 SQL  
 会自动包含约束：  
```
SELECT "products".* FROM "products" WHERE "products"."deleted_at" IS NULL
```  
  
这种行为虽然省心，但它是“悄悄”叠加的。当逻辑变得复杂（如叠加了租户隔离），问题就会随之而来。  
## 3. 危险的旁路：unscoped  
  
Rails  
 提供了 unscoped  
 工具用来移除默认作用域。但它的行为非常激进——**它会一次性清空所有默认作用域**  
。  
  
假设一个多租户系统叠加了软删除：  
```
class Product < ApplicationRecord  default_scope { where(account_id: Current.account.id) }  default_scope { where(deleted_at: nil) }end
```  
  
如果你只想在管理页面查看“包含已删除的产品”，错误地使用了 unscoped  
：  
```
# 危险操作：会移除所有约束Product.unscoped.to_sql
```  
  
生成的 SQL  
 将变成：  
```
SELECT "products".* FROM "products"
```  
  
**陷阱：**  
 原本只想去掉软删除限制，结果连 account_id  
 租户边界也一起消失了。这可能导致管理员甚至普通请求越权访问到其他租户的数据。  
## 4. 更精细的工具：unscope(where: ...)  
  
你应该使用 unscope  
 这把“手术刀”，而不是 unscoped  
 这把“大锤”。它允许你移除特定条件，同时保留其他作用域。  
```
# 精确移除软删除限制，保留租户隔离Product.unscope(where: :deleted_at).to_sql
```  
  
生成的 SQL  
 才是预期的：  
```
SELECT "products".* FROM "products" WHERE "products"."account_id" = 42
```  
### 容易漏审的变体  
  
以下写法看起来安全，实则不然：  
```
Account.first.products.unscoped
```  
  
即便前面有 Account  
 关联，最后的 unscoped  
 依然会移除 Product  
 模型上的**所有**  
默认约束。如果租户隔离依赖于模型级的 default_scope  
，此处依然会产生越权风险。  
## 5. 最佳实践：给安全路径起名字  
  
为了提高可读性并减少重复，建议将精确的绕过逻辑封装为**命名作用域（Named Scope）**  
：  
```
class Product < ApplicationRecord  default_scope { where(account_id: Current.account.id) }  default_scope { where(deleted_at: nil) }  # 显式定义的绕过路径  scope :with_deleted, -> { unscope(where: :deleted_at) }end
```  
  
调用 Product.with_deleted  
 时，意图一目了然，且 SQL  
 逻辑受控。  
## 总结：让安全成为最省力的路径  
  
IDOR 的本质是访问控制的碎片化。通过以下方式可以显著降低风险：  
1. **作用域查询：**  
 坚持使用 current_user.projects.find(...)  
。  
  
1. **弃用 unscoped：**  
 在代码审查中标记所有 unscoped  
 调用，强制改用精确的 unscope(where: ...)  
。  
  
1. **封装命名作用域：**  
 如 with_deleted  
，确保逻辑收敛。  
  
### 额外收益：引导 AI 编写安全代码  
  
如果你在使用 AI 助手（如 Claude  
 或 Copilot  
），可以在项目约定（如 AGENTS.md  
）中加入以下规则：  
> 优先使用current_user.projects.find(params[:id])，将授权融入查询。禁止使用unscoped；必须使用 unscope(where: :column) 绕过特定作用域。使用命名作用域 处理常见绕过场景（如 with_deleted）。  
  
  
通过这些结构化的约束，不仅人类开发者，连 AI 也会倾向于生成更安全的代码。  
  
  
  
   
  
觉得本文内容对您有启发或帮助？  
  
点个**关注➕**  
，获取更多深度分析与前沿资讯！  
  
  
👉 往期精选  
  
[注册功能漏洞检查清单](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484879&idx=1&sn=16cbb0a02931f172a8b7aea7877debe0&scene=21#wechat_redirect)  
  
  
[一种利用 HTTP 重定向循环的新型 SSRF 技术](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484872&idx=1&sn=085b9ed569eefc9a96122fd164da9707&scene=21#wechat_redirect)  
  
  
[API 渗透实战：从 JSON 响应倒推隐藏的高危路由](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484828&idx=1&sn=376a99fecd6210283cc43c2a79633b26&scene=21#wechat_redirect)  
  
  
[使用 Frida 在运行时拦截 OkHttp - 实用指南](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484910&idx=1&sn=9c0e1ee6b39d754de6da5b30355a4ca0&scene=21#wechat_redirect)  
  
  
[一种利用 HTTP 重定向循环的新型 SSRF 技术](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484872&idx=1&sn=085b9ed569eefc9a96122fd164da9707&scene=21#wechat_redirect)  
  
  
  
