#  WordPress插件AdvancedCustomFields:Extended曝高危漏洞  
 SecHub网络安全社区   2026-01-21 10:03  
  
****  
****  
****  
**点击蓝字 关注我们**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwuh8LP87lPQLxMwiceAsv3TurmE7zZOulOhMELnQ2OulwFIJkbmB3bRg/640?wx_fmt=png "")  
  
  
**免责声明**  
  
本文发布的工具和脚本，仅用作测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。  
  
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关内容。  
  
文中所涉及的技术、思路及工具等相关知识仅供安全为目的的学习使用，任何人不得将其应用于非法用途及盈利等目的，间接使用文章中的任何工具、思路及技术，我方对于由此引起的法律后果概不负责。  
## 🌟简介                            
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZr6C5lkme9p4hvkkc1PtAzd3mNrM66Kqwn1ibXNQyXrU1ibzZz03YncO6a9KNoymtiaVmwx9TveAo3Lg/640?wx_fmt=png&from=appmsg "")  
  
      
  
    WordPress 的 Advanced Custom Fields: Extended 插件特定范围版本中存在权限提升漏洞，漏洞编号为 CVE-2025-14533，CVSS 基础评分：9.8。这是由于'insert_user'函数没有限制用户注册时可使用的角色。这使得未经身份验证的攻击者可以在注册时提供'administrator'角色，并获得对网站的管理员访问权限。  
  
     
  
 注意：目前已有相关验证POC，当前互联网上有约10万台WordPress网站面临被接管隐患。  
  
影响版本  
# 所有<=0.9.2.1的版本   
  
# 详情ACF Erweitert 通过添加额外的字段类型和“帮助”功能扩展了 ACF，这些功能涵盖了前端表单的处理。其中一项功能允许从前端提交用户创建流程。安全漏洞使得未经身份验证的请求能够在某些插件版本中触发“插入用户”操作，而无需进行适当的权限检查或 Nonce 验证。简而言之：未经身份验证的 HTTP 请求可以创建具有更高权限的新用户。获得提升权限的攻击者的后果：创建具有持久访问权限的管理员账户。安装恶意软件、后门或恶意插件/主题。数据盗窃或破坏（文章、客户信息）。使用可重用凭据将数据迁移到其他系统。SEO 垃圾邮件、钓鱼网站或利用该网站作为其他攻击的跳板。由于攻击向量是无认证的并且可以自动化，因此广泛的扫描和自动化利用是现实的风险。因此，即使在计划插件更新维护窗口之前，也需要快速缓解。注意：只有当'role'映射到自定义字段时，该漏洞才能被利用处置措施1.更新插件：立即将 ACF Extended 更新到 0.9.2.2 或更高版本，在每个网站上。这是唯一的长久解决方案。如果您使用托管部署管道或预发布网站，请在下一个维护窗口期间优先进行生产升级——但在此期间请应用缓解措施。2.如果您无法立即更新：请应用临时缓解措施（虚拟补丁）。如果您已启用 ACF Extended 中的前端用户创建功能，请禁用它（删除或禁用创建用户的表单）。限制对 AJAX 端点的访问（如果可能），仅限于已知来源、已登录用户，或拒绝具有可疑组合的请求（参见检测和 WAF 指南）。  
  
  
  
  
欢迎关注SecHub网络安全社区，SecHub网络安全社区目前邀请式注册，邀请码获取见公众号菜单【邀请码】  
  
**#**  
  
  
**企业简介**  
  
  
**赛克艾威 - 网络安全解决方案提供商**  
  
****  
       北京赛克艾威科技有限公司（简称：赛克艾威），成立于2016年9月，提供全面的安全解决方案和专业的技术服务，帮助客户保护数字资产和网络环境的安全。  
  
  
安全评估|渗透测试|漏洞扫描|安全巡检  
  
代码审计|钓鱼演练|应急响应|安全运维  
  
重大时刻安保|企业安全培训  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwuh8LP87lPQLxMwiceAsv3TurmE7zZOulOhMELnQ2OulwFIJkbmB3bRg/640?wx_fmt=png "")  
  
  
**联系方式**  
  
电话｜010-86460828   
  
官网｜https://sechub.com.cn  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FW5uwU0BZtn2lmMrLPwpibCeCVbtBFDRkbFb7n7ibhPRxg20spUo9mUIiakmRYABB88Idl81IpGuXfw/640?wx_fmt=gif "")  
  
**关注我们**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SUZ43ICubr4mWJcUARDKYbQooQjbjbmqZTerAIXqDX9CaVxXbB7pyWwnMRklrCJias9r59PhnJAxZ4e3gYjyqVQ/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SUZ43ICubr4mWJcUARDKYbQooQjbjbmqZTerAIXqDX9CaVxXbB7pyWwnMRklrCJias9r59PhnJAxZ4e3gYjyqVQ/640?wx_fmt=png "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwyhlWCYDVqK38BA5dbjKkH7icWmAew7SYRA7ao1bFibialrMvmQ9ib0TBvw/640?wx_fmt=jpeg "")  
  
  
**公众号：**  
sechub安全  
  
**哔哩号：**  
SecHub官方账号  
  
  
