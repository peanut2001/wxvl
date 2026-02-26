#  SolarWinds Serv-U 多个严重漏洞可用于提供服务器root权限  
Sergiu Gatlan
                    Sergiu Gatlan  代码卫士   2026-02-26 11:57  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**SolarWinds****公司修复了位于 Serv-U 中四个严重的代码执行漏洞，可导致攻击者获得未修复服务器的 root 访问权限。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
Serv-U 是 SolarWinds 公司的自托管 Windows 和 Linux 文件传输软件，同时具有 MFT 和 FTP 服务器能力，可使组织机构通过 FTP、FTPS、SFTP和HTTP/S 以安全的方式传输文件。  
  
在这四个漏洞中，最严重的是CVE-2025-40538，可导致具有高权限的攻击者在易受攻击服务器上获得 root 或者管理员权限。SolarWinds 公司在周二的安全公告中提到，“Serv-U 中存在访问控制失败漏洞，如遭利用可导致攻击者创建一个系统管理员用户，并通过域管理员或分组管理员权限执行任意代码。”该公司还修复了两个类型混淆漏洞和一个不安全的直接对象引用漏洞，它们可被通过 root 权限获得代码执行能力。  
  
幸运的是，所有这四个漏洞都要求攻击者已经在目标服务器上具有较高权限，从而限制潜在的利用尝试：攻击者可组合利用多个提权漏洞或者使用此前被盗的管理员凭据。  
  
Shodan 目前追踪到超过1.2万台暴露在互联网的 Serv-U 服务器，而 Shadowserver 预计少于1200台。SolarWinds Serv-U 这类文件传输软件常遭攻击，因为它们可用于轻松访问可能含有敏感的企业和客户数据的文档。此前Serv-U 中的漏洞就曾用于数据盗取等攻击中。目前，CISA 正在追踪已遭或正遭在野活跃利用的九个 SolarWinds 漏洞。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[SolarWinds 修复四个严重漏洞，可导致未认证RCE和认证绕过](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525028&idx=3&sn=70181900e6f00cf38ce9655f395495d9&scene=21#wechat_redirect)  
  
  
[SolarWinds 第三次修复 Web Help Desk RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524063&idx=1&sn=bbbe6b07384696379e2020d8ea0e3c24&scene=21#wechat_redirect)  
  
  
[SolarWinds 修复 Web Help Desk 中的硬编码凭据漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520566&idx=2&sn=2201f2665ef471e47e5dc87762920af5&scene=21#wechat_redirect)  
  
  
[SolarWinds Web Help Desk是 0day时或已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520517&idx=1&sn=33f6242a7bd079eb73527d2099be7fc1&scene=21#wechat_redirect)  
  
  
[SolarWinds 修复访问权限审计软件中的8个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520104&idx=1&sn=b5831c292df944c1998d2c0e89a80188&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.bleepingcomputer.com/news/security/critical-solarwinds-serv-u-flaws-offer-root-access-to-servers/  
  
  
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
  
