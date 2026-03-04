#  Chrome Gemini 漏洞可被远程利用 访问受害者摄像头和麦克风  
 网安百色   2026-03-04 10:37  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnts72MhdonDnEuy3mH47U4Fz1GbvUQhiapdibKRZsIVwOkWcIpibjwwJVCiazs23MkCsW3sp84ejFLygFkGoEoEpDG4zvoOS2Qrxow/640?wx_fmt=jpeg&from=appmsg "")  
  
近日发现的 Google Chrome 中 Gemini Live 集成功能存在一个高危漏洞，编号为 CVE-2026-0628，使用户面临严重的隐私与安全风险。  
  
研究人员发现，该漏洞可能允许恶意浏览器扩展劫持 Gemini 侧边栏，从而在未经授权的情况下访问用户的摄像头、麦克风以及本地文件。  
  
将 AI 助手集成进网页浏览器、打造所谓的“代理型浏览器（agentic browsers）”，从根本上改变了浏览器的安全格局。  
  
Chrome 中的 Gemini Live 等功能，需要对浏览环境拥有深度且高权限的访问能力，以实现实时内容摘要和自动执行等任务。  
  
CVE 编号 | 严重程度 | 受影响组件 | 利用方式 | 影响 | 状态  
  
CVE-2026-0628 | 高危 | Google Chrome Gemini Live 面板 | 通过 declarativeNetRequests API 注入 JavaScript | 未授权访问摄像头、麦克风、文件及截图 | 已修复（2026 年 1 月）  
  
这种“多模态视角”（即 AI 能看到用户所看到的内容）扩大了攻击面。  
  
由于这些 AI 组件本身具有特权属性，其内部漏洞可能绕过传统的浏览器安全模型。  
  
Gemini 面板漏洞利用方式  
  
来自 Palo Alto Networks Unit 42 的研究人员发现，CVE-2026-0628 的核心问题在于：当 Chrome 在新的侧边栏中加载 Gemini Web 应用（hxxps[:]//gemini.google[.]com/app）时，其处理方式与在普通标签页中加载该应用存在差异。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnstluczKRoqMYmHaicibsJhF5TXZuZ3461Ostxm6CrsE3kNjvOXNrdkmYeHAjdic6FpfvsYIYFC6DaaxHpQHUDEUHMRfCsXNLtYus/640?wx_fmt=png&from=appmsg "")  
  
  
根据设计，使用 declarativeNetRequests API 的浏览器扩展可以拦截并修改 HTTPS 请求，这一功能通常被广告拦截器使用。  
  
在普通标签页中向 Gemini 应用注入 JavaScript 并不会获得特殊权限，但当该应用在 Gemini 面板中加载时，情况则极为危险。  
  
Chrome 会为该面板授予更高的能力，例如读取本地文件和访问媒体设备，以支持复杂的 AI 功能。  
  
攻击者如果在该面板中拦截应用请求，就可能劫持这些提升后的权限。  
  
潜在影响与缓解措施  
  
成功利用该漏洞后，攻击者可在 Gemini 面板的特权上下文中执行任意代码，可能导致严重后果，包括：  
- 在未经用户同意的情况下启动摄像头和麦克风。  
  
- 访问操作系统中的本地文件和目录。  
  
- 对任意 HTTPS 网站进行截图。  
  
- 利用受信任的 Gemini 面板界面发起高级钓鱼攻击。  
  
上述行为几乎不需要用户额外交互，仅需用户打开 Gemini 面板即可实施。  
  
Unit 42 于 2025 年 10 月向 Google 负责任地披露了该漏洞，Google 已于 2026 年 1 月初发布补丁进行修复。  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1 "")  
  
