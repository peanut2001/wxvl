#  谷歌急于发布关键的Chrome更新，以修复严重的PDFium和V8漏洞  
 网安百色   2026-02-23 10:38  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnvl9y5PNhSDia2at44QRv3nWuKAbLo8nAicDzJ9OanbaQ0A5ov8AXL35rQ1zD7tnQ7Q0B1SXxicAhry8eywTQyYkQYyBMymrTviaicc/640?wx_fmt=jpeg&from=appmsg "")  
  
Google  
 已紧急发布一项关键的 Chrome 安全补丁，修复了三个可能使攻击者在用户设备上运行恶意代码的漏洞。  
  
稳定版（Stable Channel）更新将 Windows 和 Mac 版本提升至 145.0.7632.109/.110，Linux 版本提升至 144.0.7559.109。  
  
本次修复的重点包括 PDFium（Chrome 中处理 PDF 文件的引擎）和 V8（高性能 JavaScript 处理引擎）中的高危问题。  
  
这些漏洞可能源自被植入恶意代码的网站或文档，从而将浏览器变为黑客入侵的入口。  
  
PDFium 漏洞通常在打开被篡改的 PDF 文件时触发，可能导致内存溢出，使应用崩溃，甚至更严重的是远程执行任意代码。  
  
V8 错误（如整数溢出）会干扰 Web 脚本中的数值处理，可能绕过 Chrome 的安全防护并实现隐蔽攻击。  
  
第三个问题涉及媒体播放功能，这也是常见的攻击利用向量。由于具有现实被滥用的潜在可能性，Google 将其中两个漏洞评定为高风险，并在补丁广泛部署前暂不公开详细漏洞信息。  
  
CVE-2026-2648（CWE-122）在 PDF 解析过程中触发，由于边界校验无效，攻击者可远程覆盖堆内存，可能进一步链式利用实现沙箱逃逸及任意代码执行（ACE）。  
  
CVE-2026-2649 利用 V8 在 JavaScript 整数处理方面的缺陷，引发整数溢出并破坏堆结构。  
  
攻击者可构造恶意 HTML 页面实现零点击的堆内存操控，从而在渲染进程中触发任意代码执行风险。V8 的广泛应用使其对各类 Web 应用的影响被进一步放大。  
  
CVE-2026-2650 影响媒体缓冲区，在处理畸形内容时可通过网页视频或嵌入内容造成堆内存破坏。  
  
尽管该漏洞评级为中危，但在 CVSS 评分中达到 8.8，主要由于其对机密性、完整性和可用性的高影响，且利用过程仅需用户进行播放等交互。  
  
CVE ID	Severity	Description  
  
CVE-2026-2648	High	PDFium 中的堆缓冲区溢出  
  
CVE-2026-2649	High	V8 中的整数溢出  
  
CVE-2026-2650	Medium	媒体模块中的堆缓冲区溢出  
  
根据 Google 的安全公告，按照其限制漏洞利用风险的政策，这些漏洞的细节将在大多数用户完成更新之前保持受限状态。媒体相关漏洞由 Google 内部团队通过 libFuzzer 和 AddressSanitizer 等模糊测试工具发现。  
  
Chrome 的多进程沙箱机制和站点隔离在一定程度上可缓解多种攻击，但此类零日级别漏洞仍会对其防护边界构成挑战。目前尚未确认存在在野利用情况，但高危浏览器漏洞常被勒索软件及数据窃取攻击活动所利用。  
  
更新方法：打开 Chrome，进入“帮助（Help）> 关于 Google Chrome（About Google Chrome）”，浏览器会自动检查并安装更新，并在提示时重启。企业环境可通过组策略（Group Policy）或 MDM 工具统一推送更新；关闭自动更新将显著增加安全风险。  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1 "")  
  
