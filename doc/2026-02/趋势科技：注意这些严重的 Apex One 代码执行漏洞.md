#  趋势科技：注意这些严重的 Apex One 代码执行漏洞  
Sergiu Gatlan
                    Sergiu Gatlan  代码卫士   2026-02-27 10:16  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**趋势科技公司修复了两个严重的 Apex One 漏洞，它们可导致攻击者在易受攻击的 Windows 系统上执行远程代码。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
Apex One 是一款检测和响应安全威胁如恶意软件、间谍软件、恶意工具和漏洞的端点安全平台。第一个漏洞CVE-2025-71210是因趋势科技 Apex One 管理控制台中的路径遍历弱点引发的，可导致无权限攻击者在未修复系统上执行恶意代码。第二个漏洞CVE-2025-71211也是位于同一产品中的路径遍历漏洞，影响范围也类似但影响的是不同的可执行文件。  
  
趋势科技公司在本周二发布安全公告提到，成功利用漏洞需要攻击者“拥有趋势科技 Apex One 管理控制台的访问权限，因此控制台IP地址被暴露到外部的客户如未打补丁，则需考虑缓解源限制等因素。尽管利用需要满足多个特定条件，但趋势科技强烈建议客户尽快更新至最新版本。”  
  
趋势科技已在 SaaS Apex One 版本中修复了这些漏洞并发布“重要补丁 Build 14136”，修复了位于 Windows 智能体中的另外两个高危提权漏洞和四个影响 macOS 智能体的漏洞。  
  
虽然趋势科技公司并未将这些漏洞标记为遭在野利用，但在过去几年中，威胁人员曾滥用其它 Apex One。例如，2025年8月，趋势科技公司提醒客户修复已遭活跃利用的 Apex One RCE 漏洞CVE-2025-54948；2022年9月和2023年9月，修复了影响遭在野利用的其它两个 Apex One 0day漏洞CVE-2022-40139和CVE-2023-41179。  
  
美国网络安全和基础设施安全局 (CISA) 目前发现10个趋势科技 Apex 漏洞已遭或正遭在野利用。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[趋势科技：速修复这个严重的 Apex Central RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524853&idx=1&sn=c4cd6fbd85899f9051551aad7c427db0&scene=21#wechat_redirect)  
  
  
[趋势科技证实本地系统中的两个严重 Apex One 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523757&idx=2&sn=a7158cc27029a29dc4b1bc6553c14569&scene=21#wechat_redirect)  
  
  
[趋势科技修复已遭利用的Apex One 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517701&idx=1&sn=242a34391add46cf11121fbb52e0558b&scene=21#wechat_redirect)  
  
  
[趋势科技修复又一个已遭利用的Apex One漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513971&idx=2&sn=e4ccf27e2628af5d0016b4b5f9385131&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-critical-apex-one-rce-vulnerabilities/  
  
  
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
  
