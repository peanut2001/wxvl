#  严重的FortiSIEM漏洞已遭利用  
Sergiu Gatlan
                    Sergiu Gatlan  代码卫士   2026-01-19 10:43  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**已存在公开 PoC 利用代码的Fortinet FortiSIEM严重漏洞CVE-2025-64155正在遭攻击。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
报送该漏洞的渗透测试公司Horizon3.ai的研究员Zach Hanley透露称，该漏洞由两个问题造成，可导致攻击者以管理员权限进行任意写入，并提权至root访问权限。  
  
Fortinet公司发布安全更新时解释称："FortiSIEM中存在操作系统命令中使用的特殊元素（OS命令注入）未能正确中和的漏洞[CWE-78]，可能导致未经身份验证的攻击者通过精心构造的TCP请求执行未经授权的代码或命令。"  
  
研究人员提到，该漏洞的根本原因是phMonitor服务暴露了数十个命令处理器，这些处理器可以被远程调用且无需身份验证。利用代码可通过参数注入漏洞覆盖/opt/charting/redishb.sh文件，从而获得root权限的代码执行能力。  
  
该漏洞影响FortiSIEM 6.7至7.5版本。用户可通过升级至FortiSIEM 7.4.1或更高版本、7.3.5或更高版本、7.2.7或更高版本，以及7.1.9或更高版本修复该漏洞。建议使用FortiSIEM 7.0.0至7.0.4版本以及6.7.0至6.7.10版本的客户迁移至已修复版本。  
  
上周二，Fortinet还为无法立即安装安全更新的管理员提供了一个临时解决方案，要求他们限制对phMonitor端口（7900）的访问。两天后，威胁情报公司Defused报告称，威胁行为者正在野外积极利用该漏洞。Defused警告道："在我们部署的蜜罐中，发现Fortinet FortiSIEM漏洞CVE-2025-64155正遭受主动的、有针对性的利用。"  
  
Horizon3.ai还提供了入侵指标，帮助防御者识别已遭入侵的系统。正如研究人员所解释的，管理员可以通过检查位于 /opt/phoenix/log/phoenix.logs 的phMonitor消息日志，在包含PHL_ERROR条目的行中查找有效负载URL，从而发现恶意利用的证据。  
  
Fortinet公司尚未更新其安全公告，也未将此漏洞标记为已在攻击中被利用。去年11月，Fortinet曾警告攻击者正在利用一个FortiWeb 0day漏洞（CVE-2025-58034）。一周后，它又确认已悄然修补了第二个同样成为广泛攻击目标的FortiWeb 0day 漏洞（CVE-2025-64446）。2025年2月，Fortinet还披露，两个FortiOS漏洞（编号为CVE-2023-27997和CVE-2022-42475）遭利用。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[Fortinet：注意这个严重的 FortiSIEM 预认证 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523808&idx=1&sn=ef2a5d044fa1a9c53dc3920c5ce650d5&scene=21#wechat_redirect)  
  
  
[Fortinet 提醒注意严重的FortiSIEM命令注入漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518159&idx=1&sn=44370db9677abd274914bebd182e5446&scene=21#wechat_redirect)  
  
  
[Fortinet：5年前的FortiOS SSL VPN 2FA绕过漏洞正遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524747&idx=1&sn=4048d2d12b0a64ce62d92a0b79a83100&scene=21#wechat_redirect)  
  
  
[Fortinet 提醒注意严重的 FortiCloud SSO 登录认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524622&idx=1&sn=c4730e9500580e409534b376a56f70db&scene=21#wechat_redirect)  
  
  
[Fortinet 修复FortiWeb 中的严重SQL注入漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523530&idx=2&sn=e19607b9a1bbf6bc70c902e40f0de1d3&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.bleepingcomputer.com/news/security/hackers-now-exploiting-critical-fortinet-fortisiem-vulnerability-in-attacks/  
  
  
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
  
