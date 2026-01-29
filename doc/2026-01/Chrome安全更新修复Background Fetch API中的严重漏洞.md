#  Chrome安全更新修复Background Fetch API中的严重漏洞  
 网安百色   2026-01-29 11:38  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo4WjiaVIiaZzbfVrabwUp1jlia1gGNzaKw7FcCYfSNdWFstEjoQNfPHBUh6EVzOhmt7ibTBC8DevDM76g/640?wx_fmt=jpeg&from=appmsg "")  
  
Google已为桌面平台发布新的Chrome Stable Channel更新，修复了Background Fetch API中的一个高严重性漏洞，该漏洞可能使用户面临安全风险。  
  
最新Chrome版本144.0.7559.109/.110（Windows和macOS）和144.0.7559.109（Linux）现正向用户推送，并将在未来数天和数周内逐步可用。  
  
Google目前尚未公布该漏洞的完整技术细节，因为漏洞信息在大多数用户收到修复补丁前将暂时受限。  
<table><thead><tr style="-webkit-font-smoothing: antialiased;"><th style="-webkit-font-smoothing: antialiased;"><span data-spm-anchor-id="5176.28103460.0.i16.96a075512aKH4s" style="-webkit-font-smoothing: antialiased;"><span leaf="">CVE ID</span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">Severity</span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">Component</span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">Type</span></span></th><th style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">Reporter</span></span></th></tr></thead><tbody><tr style="-webkit-font-smoothing: antialiased;"><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">CVE-2026-1504</span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">High</span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">Background Fetch API</span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">Inappropriate implementation</span></span></td><td style="-webkit-font-smoothing: antialiased;"><span style="-webkit-font-smoothing: antialiased;"><span leaf="">Luan Herrera (@lbherrera_)</span></span></td></tr></tbody></table>  
该已修复的漏洞被追踪为CVE-2026-1504，被描述为Background Fetch API中的"不当实现"，严重性评级为"高"。  
  
该问题由安全研究员Luan Herrera (@lbherrera_)于2026年1月9日报告，Google为此发现授予了3,000美元的漏洞奖励。  
  
Background Fetch API允许网站在后台下载大文件，即使浏览器标签已关闭。  
  
此组件中的实现缺陷可能被滥用，以绕过安全边界、错误处理权限或以不安全方式处理后台请求。  
  
虽然Google尚未披露利用细节，但"高"评级表明成功利用可能影响用户安全或隐私。  
  
按照标准做法，Google在大多数Chrome用户完成更新前，将暂缓完整的漏洞报告和利用细节，以降低威胁行为者进行主动利用的风险。  
  
如果该漏洞也存在于第三方库中，相关限制可能会保持更长时间，以便其他项目有时间进行修复。  
  
强烈建议用户尽快通过浏览器内置的更新机制更新Chrome，以确保免受CVE-2026-1504及其他底层安全漏洞的影响。  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1 "")  
  
