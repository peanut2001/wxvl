#  谷歌紧急发布关键Chrome更新，以修复PDFium和V8的严重漏洞  
原创 网络安全9527
                    网络安全9527  安全圈的那点事儿   2026-02-21 00:17  
  
谷歌紧急发布了 Chrome 浏览器的重要安全补丁，修复了三个可能让攻击者在用户设备上运行恶意代码的漏洞。  
  
稳定版更新将 Windows 和 Mac 的版本提升至 145.0.7632.109/.110，将 Linux 的版本提升至 144.0.7559.109。  
  
修复的重点是 PDFium （Chrome 中处理 PDF 文件的引擎）和 V8（快速 JavaScript 处理器）中的严重问题。  
  
这些可能源于被植入陷阱的网站或文档，它们会将浏览器变成黑客的入口。  
  
PDFium 的缺陷通常发生在打开受污染的 PDF 文件时，导致内存溢出，从而使应用程序崩溃，或者更糟糕的是，远程执行任意代码。  
  
V8 错误（例如整数溢出）可能会干扰 Web 脚本中的数字处理，从而可能绕过 Chrome 的防御并实施隐蔽攻击。  
  
第三个问题针对媒体播放，这是另一个常见的攻击途径。谷歌将其中两个问题评为高风险，因为它们可能被实际滥用，因此在补丁广泛发布之前，谷歌不会透露漏洞详情。  
  
CVE-2026-2648 (CWE-122) 在 PDF 解析期间触发，无效边界允许攻击者远程覆盖堆内存，可能链接到沙箱逃逸和任意代码执行 (ACE)。  
  
CVE-2026-2649 利用 JavaScript 中 V8 的整数处理缺陷，导致溢出并破坏堆结构。  
  
攻击者精心构造 HTML 页面，实现零点击堆操作，从而在渲染过程中冒着被 ACE 攻击的风险。V8 的广泛应用加剧了这种影响在 Web 应用中的普遍性。  
  
CVE-2026-2650 会攻击格式错误的媒体缓冲区，从而导致 Web 视频或嵌入内容的堆损坏。  
  
虽然评级为中等，但在 CVSS 评分标准中，其保密性/完整性/可用性效果高达 8.8 分，并且具有回放等用户交互功能。  
  
<table><thead style="box-sizing: border-box;border-bottom-width: 3px;border-bottom-style: solid;border-bottom-color: currentcolor;"><tr style="box-sizing: border-box;"><th class="has-text-align-left" data-align="left" style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">CVE ID</font></font></th><th class="has-text-align-left" data-align="left" style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">严重程度</font></font></th><th class="has-text-align-left" data-align="left" style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">描述</font></font></th></tr></thead><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">CVE-2026-2648</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">高的</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">PDFium 中的堆缓冲区溢出</font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">CVE-2026-2649</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">高的</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">V8 中的整数溢出</font></font></td></tr><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">CVE-2026-2650</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">中等的</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">媒体中的堆缓冲区溢出</font></font></td></tr></tbody></table>  
根据谷歌的公告，这些漏洞仍将受到限制，直到大多数用户更新系统为止，这是谷歌限制漏洞利用的政策。谷歌内部团队使用 libFuzzer 和 AddressSanitizer 等模糊测试工具发现了媒体报道中提到的那个漏洞。  
  
Chrome 的多进程沙箱和站点隔离机制可以有效抵御许多攻击，但像这样的零日漏洞却考验着这些机制的极限。目前尚未确认任何活跃的攻击，但高危浏览器漏洞往往会助长勒索软件和数据窃取活动。  
  
