#  网安靶场实战指南（第4期）：OWASP Juice Shop入门——前后端分离架构下的漏洞挖掘  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-01-29 02:07  
  
搞定DVWA全难度后，我们正式进入Web进阶靶场阶段！这一期的主角是OWASP Juice Shop——当下最火的现代Web应用靶场，基于React前后端分离架构，模拟真实电商场景，漏洞类型贴合当下Web开发趋势，是从“基础漏洞”过渡到“实战场景”的核心练习载体。  
  
和DVWA的“纯技术漏洞”不同，OWASP Juice Shop不仅包含XSS、SQL注入等传统漏洞，更侧重业务逻辑漏洞（如支付篡改、权限越权），完美还原真实电商平台的安全场景。这一期我们先搞定“环境搭建+功能拆解+核心漏洞入门”，帮你快速适配前后端分离架构的漏洞挖掘思路。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaLzURuoralYLyC1oCXATWa90WEyEpNnTFnJ4blYUdnSK5OIpGz8dBux22uXPttehLU8qbnqj7Bn6c0cznUUXrQ/640?wx_fmt=jpeg "")  
## 一、OWASP Juice Shop环境搭建：3种方案，适配不同需求  
  
OWASP Juice Shop支持本地部署、Docker部署和在线体验，推荐新手优先选Docker或在线方案，避免踩环境配置坑。  
### 方案1：Docker一键部署（推荐，5分钟搞定）  
#### 核心优势：无需配置Node.js依赖，一键启动，跨平台兼容  
#### 操作步骤：  
1. 确保已安装Docker（Windows/Mac用Docker Desktop，Linux直接安装Docker）；  
  
1. 拉取镜像：命令行执行 docker pull bkimminich/juice-shop  
；  
  
1. 启动容器：执行 docker run -d -p 3000:3000 bkimminich/juice-shop  
（-p 3000:3000映射本地3000端口）；  
  
1. 验证访问：浏览器输入 http://localhost:3000  
，能看到Juice Shop电商首页即部署成功。  
  
### 方案2：本地手动部署（适合想理解架构的学习者）  
#### 依赖要求：Node.js 14-16版本（过高版本不兼容）、npm 6+  
#### 操作步骤：  
1. 下载源码：GitHub克隆 git clone https://github.com/juice-shop/juice-shop.git  
，或直接下载压缩包；  
  
1. 安装依赖：进入源码目录，执行 npm install  
（若报错可尝试 npm install --legacy-peer-deps  
）；  
  
1. 启动应用：执行 npm start  
，启动成功后访问 http://localhost:3000  
；  
  
1. 初始化：首次访问会自动初始化数据库，无需额外配置。  
  
### 方案3：在线体验（零配置，适合快速试玩）  
  
直接访问官方在线靶场：https://juice-shop.herokuapp.com/，无需部署即可体验所有功能（注意：在线版可能有访问延迟，部分漏洞利用受环境限制）。  
### 常见问题排坑  
- Node.js版本不兼容：用nvm切换到14版本（nvm install 14 && nvm use 14  
）；  
  
- 端口被占用：Docker启动时改端口（如 docker run -d -p 8080:3000  
），访问用 http://localhost:8080  
；  
  
- npm依赖安装失败：更换淘宝镜像（npm config set registry https://registry.npm.taobao.org  
）后重新安装。  
  
## 二、OWASP Juice Shop核心功能拆解：找准漏洞挖掘靶点  
  
Juice Shop模拟了完整的电商流程，漏洞隐藏在各个业务功能中，先拆解核心功能模块，再针对性挖掘：  
<table><thead><tr><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">功能模块</span></section></th><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">核心场景</span></section></th><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">潜在漏洞方向</span></section></th></tr></thead><tbody><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">用户系统</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">注册、登录、密码重置、个人中心</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">弱口令、SQL注入、权限越权、敏感数据泄露</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">商品模块</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">商品浏览、搜索、评价</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">XSS（存储型/反射型）、SQL注入、目录遍历</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">购物流程</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">加入购物车、结算、支付</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">支付金额篡改、订单逻辑漏洞、优惠券滥用</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">其他功能</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">反馈留言、隐私政策、关于我们</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">存储型XSS、文件读取、敏感信息泄露</span></section></td></tr></tbody></table>### 关键提示：开启“漏洞提示”功能  
  
登录后点击右上角头像→Settings→勾选“Show Hints”，每个漏洞场景会显示简短提示（新手必备）；进阶者可关闭提示，自主挖掘。  
## 三、核心漏洞实战：前后端分离架构的特殊利用  
  
前后端分离架构（React前端+Node.js后端）的漏洞，和传统PHP应用有明显区别——前端只做数据渲染，所有请求通过API接口与后端交互，漏洞多隐藏在API参数中。  
### 1. 业务逻辑漏洞：支付金额篡改（高价值漏洞）  
#### 漏洞场景：购物车结算时，后端未校验前端传入的金额，仅依赖前端计算结果  
#### 利用步骤：  
1. 前端操作：选择任意商品加入购物车，进入结算页面（Checkout），输入收货地址后点击“Place Order”；  
  
1. 抓包分析：用Burp Suite抓包，找到结算接口（POST /api/Orders  
），请求体中包含 totalPrice  
 参数（如 {"totalPrice":99.99,"items":[]...}  
）；  
  
1. 篡改参数：将 totalPrice  
 改为0.01或0，发送请求；  
  
1. 验证结果：页面显示“Order Placed Successfully”，订单金额被成功篡改，实现“低价购买”。  
  
#### 漏洞本质：后端未重新计算商品总价，盲目信任前端传入的参数——这是真实电商平台最常见的高价值漏洞之一。  
### 2. 存储型XSS：商品评价功能（前后端分离特殊绕过）  
#### 漏洞场景：商品评价提交后，所有用户可见，前端渲染评价内容时未做过滤  
#### 利用步骤：  
1. 前端操作：进入任意商品详情页，点击“Write a Review”，输入评价内容；  
  
1. 构造Payload：由于是React前端，直接输入 <script>alert(1)</script>  
 会被React转义，需用SVG标签绕过：  
```
<svg onload="alert(document.domain)"></svg>
```  
  
1. 提交评价：点击“Submit Review”，评价成功提交；  
  
1. 触发漏洞：刷新商品详情页，或其他用户访问该商品时，SVG标签的onload  
事件触发弹窗，XSS漏洞生效。  
  
#### 关键区别：传统PHP应用的XSS可直接用script标签，前后端分离架构下需针对性选择前端未过滤的标签/事件。  
### 3. 权限越权：访问他人订单信息  
#### 漏洞场景：订单查询接口未校验用户身份，仅通过订单ID即可查询任意订单  
#### 利用步骤：  
1. 正常操作：登录账号，完成一笔订单，进入“Order History”，查看自己的订单（如订单ID为1）；  
  
1. 抓包分析：找到订单查询接口（GET /api/Orders/1  
），请求头包含用户Token（Authorization: Bearer xxx  
）；  
  
1. 篡改参数：将订单ID改为2、3等其他数值，发送请求；  
  
1. 验证结果：若后端返回其他用户的订单信息（收货地址、联系方式、购买商品），则说明存在越权漏洞。  
  
#### 漏洞本质：后端仅校验了用户是否登录（Token有效），未校验该订单是否属于当前用户。  
### 4. 敏感数据泄露：API接口未脱敏  
#### 漏洞场景：用户注册接口返回信息过多，包含敏感字段  
#### 利用步骤：  
1. 前端操作：进入注册页面，输入合法的用户名、邮箱、密码，点击“Register”；  
  
1. 抓包分析：找到注册接口（POST /api/Users  
），查看响应体；  
  
1. 漏洞发现：响应体中包含用户的明文密码、API密钥等敏感信息（如 {"id":1,"email":"test@xxx.com","password":"123456","apiKey":"xxx"...}  
）；  
  
1. 危害：攻击者可通过注册账号，获取自己的敏感信息，推测其他用户数据也未脱敏，进而批量获取。  
  
## 四、前后端分离架构的漏洞挖掘技巧  
1. 聚焦API接口：所有交互都通过API进行，用Burp Suite抓取所有接口，分析参数是否可篡改、是否有未授权访问；  
  
1. 绕过前端校验：前端的表单验证（如金额范围、密码强度）可直接绕过，通过抓包修改参数测试后端是否校验；  
  
1. 关注数据渲染：React前端对特殊标签的过滤规则与传统应用不同，优先尝试SVG、body等不常用标签触发XSS；  
  
1. 测试敏感接口：重点测试 /api/Users  
（用户）、/api/Orders  
（订单）、/api/Payment  
（支付）等核心接口，容易发现高价值漏洞。  
  
## 五、漏洞修复建议  
1. 业务逻辑漏洞：后端重新校验关键参数（如支付金额需根据商品单价×数量重新计算），不依赖前端数据；  
  
1. XSS漏洞：后端对用户输入进行HTML实体编码，前端使用React的内置渲染函数（如{}  
包裹内容），自动转义特殊字符；  
  
1. 权限越权：每个接口都添加“身份校验”（如查询订单时，校验订单的用户ID与当前登录用户ID一致）；  
  
1. 敏感数据泄露：接口响应仅返回必要字段，密码等敏感信息需加密存储，返回时脱敏（如只显示后4位）。  
  
## 六、互动与下期预告  
  
OWASP Juice Shop的漏洞更贴近真实电商场景，尤其是业务逻辑漏洞，比传统技术漏洞更有实战价值。你在挖掘时遇到了哪些有趣的漏洞？比如优惠券滥用、密码重置绕过？评论区分享你的发现~  
  
下一期我们继续深挖OWASP Juice Shop的进阶漏洞，包括SQL注入（API接口型）、文件读取漏洞、第三方组件漏洞（npm依赖），同时讲解“多漏洞组合利用”（如越权+XSS获取管理员权限），关注不迷路！  
  
点击文末  
阅读原文  
领取200节攻防教程  
  
  
