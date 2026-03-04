#  Chrome Gemini漏洞可致攻击者远程访问用户摄像头和麦克风  
 华盟信安   2026-03-04 02:37  
  
![](https://mmbiz.qpic.cn/mmbiz_png/E08BHTj0T121ibQ2lOZrPtHOIiacgyfn6keic0ogjSfHHTcdH2sGPvB7OwHAwVNibxXRkPUFaMXfQrSqsc5SarUic3j01kjEjcJUIibt3FoSBbI94/640?wx_fmt=png&from=appmsg "")  
  
**Part01**  
## 高危漏洞曝光  
  
  
谷歌Chrome浏览器内置的Gemini AI助手被发现存在一个高危安全漏洞（CVE-2026-0628），攻击者无需用户任何额外操作，仅需用户启动浏览器内置的AI面板，即可实现未经授权的摄像头和麦克风访问、本地文件窃取以及钓鱼攻击。  
  
  
该漏洞由Palo Alto Networks旗下Unit 42的研究人员发现，并于2025年10月23日向谷歌报告。谷歌确认问题后于2026年1月5日发布补丁。  
  
  
**Part02**  
## 特权架构扩大攻击面  
  
  
Chrome中的Gemini Live功能属于"AI浏览器"这一新兴类别，这类浏览器将AI助手直接嵌入浏览环境。这些AI助手（包括Edge中的Microsoft Copilot以及Atlas和Comet等独立产品）作为特权侧边栏运行，能够实现实时网页摘要、任务自动化和上下文浏览辅助。  
  
  
由于这些AI面板需要"多模态"视图才能有效运行，Chrome授予Gemini面板提升的权限，包括访问摄像头、麦克风、本地文件和屏幕截图能力。这种特权架构虽然实现了强大功能，但也显著扩大了浏览器的攻击面。  
  
  
**Part03**  
## 漏洞技术细节  
  
  
漏洞存在于Chrome处理declarativeNetRequest API的方式中，这是一个标准的浏览器扩展权限，允许扩展拦截和修改HTTPS网络请求和响应。该API广泛用于广告拦截等合法用途。  
  
  
研究人员发现，Chrome处理hxxps[:]//gemini.google[.]com/app请求时存在关键差异：当该URL在普通浏览器标签页中加载时，扩展可以拦截并向其注入JavaScript，但这不会授予任何特殊权限；而当同一URL在Gemini浏览器面板中加载时，Chrome会以提升的浏览器级权限处理它。  
  
  
利用这种不一致性，仅具有基本权限的恶意扩展即可向特权Gemini面板注入任意JavaScript代码，从而劫持受信任的浏览器组件并继承其所有提升的访问权限。  
  
  
**Part04**  
## 攻击能力与影响  
  
  
攻击者通过此技术控制Gemini面板后，仅需受害者点击Gemini按钮即可执行以下操作，无需任何其他用户交互：  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2iapY2xn60NhOgCgXEbPz94Czgeej9muciaRibqmfFUFfxeD3Cvq9BUN98RYN2Y1yUAibfdyvQVzOzqkYQok5Vj7a4SLMUGWjPFU4/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2 "")  
  
  
钓鱼攻击风险尤为危险，因为Gemini面板是受信任的浏览器集成组件。其中显示的恶意内容具有独立钓鱼页面所缺乏的固有可信度。  
  
  
**Part05**  
## 企业安全风险加剧  
  
  
在企业环境中，被入侵的扩展获取员工摄像头、麦克风和本地文件访问权限会带来严重的组织安全风险，可能导致企业间谍活动和数据外泄。  
  
  
谷歌已于2026年1月5日发布修复补丁。运行最新版Chrome的用户已受到保护。各组织应立即确保所有终端上的Chrome浏览器完成更新。  
  
  
**参考来源：**  
  
Chrome Gemini Vulnerability Lets Attackers Access Victims’ Camera and Microphone Remotely  
  
https://cybersecuritynews.com/chrome-gemini-vulnerability/  
  
文章来源：freebuf  
  
