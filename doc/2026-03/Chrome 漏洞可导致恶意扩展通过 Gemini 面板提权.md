#  Chrome 漏洞可导致恶意扩展通过 Gemini 面板提权  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-03-03 10:21  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**网络安全研究人员披露了谷歌 Chrome 浏览器中一个现已修复的安全漏洞 (CVE-2026-0628) 细节，可导致攻击者提权并访问系统上的本地文件。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVAFlnayokqrhmYmpiaEDDbUeiaibiab7Ibuc4YsfEbc7QNP6rnOVHabWsDiaMHgs01gb8XZWGUILVhobVIcBPgSzhaUSp1o0cicRgLQ/640?wx_fmt=gif&from=appmsg "")  
  
**由WebView 标签中策略执行不足引发**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVk1wQVqPaeVvAoU9icNcGByJxQa0Gzg6GrPHtnkyVAdkUJul91ZEHJTdNFgKZgWJeicmI0xz3FXSrd7pzvG8JUoyqZcQuDOtVeA/640?wx_fmt=gif&from=appmsg "")  
  
  
  
该漏洞因WebView 标签中策略执行不足导致。谷歌于 2026 年 1 月初在适用于 Windows/Mac 平台的 143.0.7499.192/.193 版本和 Linux 平台的 143.0.7499.192 版本中予以修复。美国国家标准与技术研究院国家漏洞数据库提到，"在 143.0.7499.192 版本之前的 Google Chrome 浏览器中，WebView 标签策略执行不足，导致攻击者可通过说服用户安装恶意扩展，从而借助特殊构造的 Chrome 扩展程序向特权页面注入脚本或 HTML。"  
  
该漏洞由 Palo Alto Networks 公司 Unit 42 团队的研究员 Gal Weizman在 2025 年 11 月 23 日发现并报告。他表示，该漏洞可能导致拥有基本权限的恶意扩展程序夺取 Chrome 浏览器中新推出的 Gemini Live 面板的控制权。可通过点击浏览器窗口顶部的 Gemini 图标启动该面板。谷歌于 2025 年 9 月将 Gemini 集成到 Chrome 浏览器中。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXPHR4pA3zu86QugnhlrUzRDt5xd47czuOLya20jJgVicTMoNBU8hBPicLJLZtSPByX3rpKMGWsTgbpibhQicDibbIDibKkHuIMfq5wg/640?wx_fmt=gif&from=appmsg "")  
  
**AI功能成双刃剑**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVAQOaNickK5urM9ptVFicG7waibibyqWxhU0cxsCdFRicQWPqxvyYvIPZQJFUMbKa5HEADPRYTBNCdeERvjjVokoia76xVtDBEepAug/640?wx_fmt=gif&from=appmsg "")  
  
  
  
这种攻击可能被用于提权，从而能够在未经受害者许可的情况下访问其摄像头和麦克风，截取任意网站的屏幕截图，并访问本地文件。这些发现揭示了源于将人工智能（AI）和智能体能力直接集成到网页浏览器中的新型攻击向量，可实现实时内容摘要、翻译和自动化任务执行等功能，而同样的能力也可能被滥用来执行特权操作。该问题的核心在于，为了执行多步骤操作，需要授予这些AI智能体对浏览器环境的特权访问权限，这使其成为一把双刃剑：当攻击者在恶意网页中植入隐藏提示，并通过社会工程或其他手段诱骗受害者访问时，智能体便可能被利用。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXrvgImCzCia50mIaURAMC9LEqbsf9tXjneq3YZBv8KzwyoHWOo3ibrGLqaTZ1SSbScI1P2DiaicTxMQN3iarOmlPibAibVun9MlpX9KM/640?wx_fmt=gif&from=appmsg "")  
  
**AI浏览器新时代的旧问题**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUV3U6VEocSoaoTUHFgweJpmiaDkwoPm85NnLsoNWnQVqufNCRjBPeMHYalGDNlFibyPZibDRjc4tAMKJiaEYeIHgqHL5iaZIbAg8Q8/640?wx_fmt=gif&from=appmsg "")  
  
  
  
这类提示能够要求AI助手执行本会被浏览器阻止的操作，从而导致数据泄露或代码执行。更糟糕的是，网页还可能操纵智能体将指令存储在内存中，使其能够在不同会话之间持续存在。Unit 42 的研究人员指出，除了攻击面扩大之外，智能体浏览器中集成AI侧边面板也带来了常见的浏览器安全风险。  
  
Weizman 表示，通过将这个新组件置于浏览器的高权限上下文中，开发者可能会无意中引入新的逻辑缺陷和实现弱点，如与跨站脚本、权限提升和侧信道攻击相关的漏洞，而权限较低的网站或浏览器扩展可以利用这些漏洞。  
  
虽然浏览器扩展基于一套明确的权限集运行，但对 CVE-2026-0628 的成功利用会破坏浏览器的安全模型，并允许攻击者通过浏览器面板在 “gemini.google[.]com/app” 上运行任意代码，进而访问敏感数据。  
  
Weizman 补充道：“通过 declarativeNetRequest API 获得基本权限集的扩展，其所获的权限可能使攻击者能够向新的 Gemini 面板注入 JavaScript 代码。当 Gemini 应用在这个新面板组件中加载时，Chrome 会将其与强大的功能接口相连接，使其能够访问这些功能。”  
  
值得注意的是，declarativeNetRequest API 允许扩展拦截和修改 HTTPS 网络请求与响应的属性。广告拦截扩展正是利用此 API 来阻止网页加载广告的请求。  
  
换句话说，攻击者只需诱骗毫无戒心的用户安装一个特殊构造的扩展，就能向 Gemini 侧边面板注入任意 JavaScript 代码，进而与文件系统交互、截取屏幕截图、访问摄像头、开启麦克风——这些都是 AI 助手执行任务所必需的功能。Unit 42 团队的研究人员指出：“Gemini 应用由何种类型的组件加载的区别正是设计行为与安全漏洞之间的分界线。”扩展能够影响网站是预期之内的行为。然而，扩展能够影响浏览器内置的组件，则是一个严重的安全风险。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[谷歌紧急修复 Chrome 中的两个高危内存损坏漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524683&idx=3&sn=ccf1081df758629e4af0ca28f97b0972&scene=21#wechat_redirect)  
  
  
[谷歌紧急修复已遭利用的Chrome V8 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524445&idx=1&sn=9145b7009a002f9da12dbec7be2ae727&scene=21#wechat_redirect)  
  
  
[AI 编程助手 Cline CLI 2.3.0遭篡改，悄悄安装 OpenClaw](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525250&idx=2&sn=0896fff8eb0f9f9e2369a299930ff6c4&scene=21#wechat_redirect)  
  
  
[Chrome紧急修复 WebGPU 和 V8引擎中的三个高危漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524343&idx=1&sn=bafd6d107e51fa5d67f552a22dd26211&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://thehackernews.com/2026/02/thousands-of-public-google-cloud-api.html  
  
  
题图：Pixa  
bay Licens  
e  
  
  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg "")  
  
**奇安信代码卫士 (codesafe)**  
  
国内首个专注于软件开发安全的产品线。  
  
   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif "")  
  
   
觉得不错，就点个 “  
在看  
” 或 "  
赞  
” 吧~  
  
