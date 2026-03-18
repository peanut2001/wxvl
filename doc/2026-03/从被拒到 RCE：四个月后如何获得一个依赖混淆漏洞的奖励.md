#  从被拒到 RCE：四个月后如何获得一个依赖混淆漏洞的奖励  
haidragon
                    haidragon  安全狗的自我修养   2026-03-18 04:27  
  
# 官网：http://securitytech.cc  
  
  
这个故事从一份被拒的报告开始。  
## 被拒的报告：  
  
在这次发现最终获得奖励的四个月前，它被拒绝了。  
  
当时，这感觉像是一个典型的漏洞赏金故事。你发现了有趣的东西，提交报告，但因为无法证明影响而被关闭。这正是当时发生的事情。  
  
在对我们称之为 **redacted.com**  
  
 的网站进行侦察时，我分析了其仪表盘应用加载的 JavaScript 文件。像很多猎人一样，我在侦察阶段依赖 **Burp Suite**  
。一个在 JavaScript 分析中非常有用的扩展是 **JS Miner**  
，它可以从 JavaScript 打包文件中提取端点、密钥和依赖引用。  
  
在解析仪表盘资源时，JS Miner 显示了一些异常。在依赖项中出现了一个看起来不像公共库的包名：  
  
recovery-npm-package  
  
Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvXv43TzqIu3TJ32J16BKfRRT6IqEGpEstkUckRK684or02G5pUXhU5ib1G7uwMNoKZjiaK5BGrWTSqGuQEzOjPiaUx6C1oqRqbIQ/640?wx_fmt=png&from=appmsg "")  
  
我发现了 3 个类似的未被认领的包。  
  
这些 JavaScript 片段是通过仪表盘使用的 CDN 端点提供的：  
[https://dashboard-production-f.redacted-cdn.com](https://dashboard-production-f.redacted-cdn.com/)  
  
自然的下一步是检查 npm。  
  
该包不存在。  
  
那时，我怀疑可能存在 **依赖混淆（dependency confusion）**  
 的情况。应用似乎引用了一个未公开注册的内部依赖。如果构建过程从公共 npm 注册表解析依赖项，攻击者可能注册同名包并将恶意代码注入构建管道。  
  
这是我 **第一次尝试依赖混淆攻击**  
，经验不足显而易见。  
  
我声称了该包名，并发布了一个基础版本。有效载荷很简单，仅用于检测安装事件。我等待回调。  
  
没有任何响应。  
  
没有执行证明，报告纯粹是理论性的。安全团队回应说，该发现缺乏可证明的影响力，因此关闭了报告。  
  
当时我接受了这一点并继续前行，但我从未完全忘记它。  
  
Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuS8icLtQXxeRiaS2wJaeiabmkIVovYsib3bzuourfqJpxIfVvnNSSnVuxtcCTTv6NYAhricV6DU2yk9sdJtwvwfhO2MaUU9t6qnZZE/640?wx_fmt=png&from=appmsg "")  
## 四个月后  
  
四个月后，我深夜翻阅旧笔记时，再次遇到了这份被拒的报告。  
  
这件事让我一直耿耿于怀。  
  
问题不在于发现，而在于利用。  
  
那时，我只对依赖混淆攻击的表面有所了解。我虽然声称了包，但没有正确配置它来证明执行，这样的证据很容易被忽略。  
  
于是，我决定再试一次。  
## 重新审视目标  
  
我回到 npm，再次检查该包名：  
  
recovery-npm-package  
  
它仍然未被认领。  
  
这次，我正确注册了它，并准备了一个更受控的有效载荷，以捕获清晰的执行证据。  
  
包中包含两个文件：一个简单的 index.js  
 和一个包含 **preinstall 钩子**  
 的 package.json  
。  
  
package.json  
 内容如下：  
```
```  
  
思路很简单：  
  
如果任何系统安装这个包，**preinstall 脚本会自动执行**  
，并将 /etc/passwd  
 内容连同执行安装的主机名发送到我的 **Burp Collaborator 服务器**  
。  
  
这是依赖混淆研究中常用的标准技术，因为它可以安全地演示命令执行，而不会造成破坏。  
  
包发布后，我等待回调。  
## 回调开始  
  
几分钟内，我的 Burp Collaborator 仪表盘开始接收到交互请求。起初只是一个请求，随后又一个，然后是更多请求。  
  
Press enter or click to view image in full size  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnupqnJeib17X0eppV9BLT6cPV0YfHEcIcLGQ2QktwPfuQHsXTakBicw7b0URLJiauuMOEeoASriakyEBIMoZbACH3v2L4NTB5Hh04A/640?wx_fmt=png&from=appmsg "")  
  
每个交互都包含 HTTP 请求，内含 /etc/passwd  
 内容，以及执行系统的主机名和元数据。多个 IP 地址访问我的 Collaborator 域。有效载荷已成功执行，这确认了恶意包已在某处安装，preinstall 钩子在安装过程中执行。  
  
从技术角度来看，这证明了 **依赖安装过程中远程命令执行（RCE）**  
 的存在。  
## 再次提交报告  
  
这次我有了真正的证据。  
  
新报告包括：  
- 引用该依赖的 JavaScript 文件  
  
- 未被认领的 npm 包名  
  
- 发布到 npm 的恶意包  
  
- Burp Collaborator 交互日志  
  
- 外泄的 /etc/passwd  
 数据  
  
- 执行有效载荷的系统 IP 地址  
  
两天后，安全团队回复了我。  
  
他们写道：  
> “感谢信息。我们认为该问题可能是误报。你提供的 IP 列表对应中国的服务器提供商，没有映射到我们的内部系统。此外，我们确认项目中存在 YarnLock 文件，所以即便你发布了同名包，内部系统也不会受到影响。为了真正利用该漏洞，/etc/passwd 文件需要被攻破，要么在开发者笔记本上，要么在构建系统上。  
> 我们目前的理论是，这可能是某些第三方扫描器或行为者，在你发布恶意包时安装了它们。  
> 你用于 PoC 的包未在内部完全发布，我们会清理它。因为这是清理工作，我将把其风险等级降低到 P3。”  
  
  
读到这段话，我感到心情复杂。  
  
一方面，他们承认了问题并计划清理依赖；另一方面，他们认为回调是来自第三方扫描器，而不是内部基础设施。  
  
我感到既 **高兴又不高兴**  
。  
  
高兴的是，该发现得到了认可；  
  
不高兴的是，我观察到的实际影响似乎比他们认为的更强。  
## 理解发生了什么  
  
依赖混淆攻击依赖于包管理器的一个简单行为。  
  
当包管理器解析依赖时，它会检查配置的注册表。如果内部包名未正确作用域或注册表配置不严格，解析器可能从 **公共注册表而非私有注册表**  
 获取包。  
  
如果攻击者控制了公共注册表中同名的包，恶意代码会在安装时执行。  
  
**preinstall 脚本**  
尤其强大，因为它在安装过程中自动执行，甚至在包完全安装之前。  
  
在此案例中，攻击链如下：  
1. 应用引用了内部依赖  
  
1. 包名未被公开认领  
  
1. 攻击者在 npm 注册该包  
  
1. 某系统安装了该依赖  
  
1. preinstall 脚本执行  
  
1. 数据被外泄到攻击者的 Collaborator 服务器  
  
即便回调来自自动扫描器或监控 npm 包的第三方行为者，核心问题仍然存在：  
  
**内部依赖名在公共注册表可被认领**  
## 收获的教训  
### 被拒的报告并非总是错误  
  
有时报告被拒是因为 **影响未被充分证明**  
。重新审视旧发现，在积累经验后可能会有突破。  
### 工具很重要  
  
像 **JS Miner**  
 这样的 Burp Suite 扩展能大大提高 JavaScript 侦察效率。现代应用通常包含巨量代码，自动提取工具可以快速发现隐藏依赖。  
### 依赖混淆仍然相关  
  
即便多年后，这种攻击依然有效，许多组织仍通过客户端资产或构建流程暴露内部包名。  
## 最终感想  
  
这个漏洞在我的笔记里放了四个月。  
  
最初，它只是一个被拒的报告。但通过对依赖混淆的深入理解，它最终变成了一个被验证的漏洞，并最终获得了赏金。  
  
漏洞赏金狩猎往往奖励 **坚持不懈**  
。  
  
有时，被拒报告与成功报告的区别，不在于发现本身，而在于 **是否能有说服力地证明影响**  
。  
  
有时，最好的发现是那些几乎被你遗忘的。  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntCrmVkJ0XcSlU4e07kmnBu06aibBXd8jyYsnX1fN09KAFYneY2b9Rd4wPmmJexSb4FCeuIUQv2xoNqAF4YoYN3rOyicpdUERByE/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1 "")  
  
##   
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnulibq1QLlNIctj1PB1q0diaVQkX6EpwtKia2TUwRjBJPZricM2ScWBGibe7dC99kD0qwb9icHLLA2QEoqxiaib0yxs9vc14IMps8lOWmY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7 "")  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
