#  Fortinet 修复可导致未认证代码执行的严重 SQLi 漏洞  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-02-10 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**Fortinet****公司发布安全更新，修复了影响 FortiClientEMS 的一个严重漏洞CVE-2026-21643（CVSS评分9.1），可导致攻击者在可疑系统上执行任意代码。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
Fortinet 公司在一份安全公告中提到，“FortiClientEMS 中的一个SQL 注入漏洞可导致未认证攻击者通过特殊构造的HTTP请求执行未授权代码或命令。”该漏洞对各版本的影响如下：  
  
- FortiClientEMS 7.1（不受影响）  
  
- FortiClientEMS 7.4.4（升级至7.4.5或后续版本）  
  
- FortiClient 8.0（不受影响）  
  
  
  
该漏洞由Fortinet 安全团队成员Gwendal Guégniaud发现并报送。虽然Fortinet 公司并未说明该漏洞是否已遭在野利用，但用户应尽快应用修复方案。  
  
前不久，Fortinet 公司修复了位于 FortiOS、FortiManager、FortiAnalyzer、FortiProxy、FortiWeb 中的另外一个严重漏洞（CVE-2026-24858，CVSS评分9.4），它可导致拥有一个 FortiCloud 账号和一台注册设备的攻击者登录到其它用户注册的设备，前提是这些设备上启用了 FortiCloud SSO 认证机制。  
  
Fortinet 公司证实称该漏洞已被恶意用于创建本地管理员账号以实现持久性、更改配置以使账号拥有VPN访问权限以及盗取防火墙配置。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[Fortinet 修复已遭利用的严重 FortiOS 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524999&idx=2&sn=ff036e0f85b25e6ee0f685062e7a537f&scene=21#wechat_redirect)  
  
  
[Fortinet：5年前的FortiOS SSL VPN 2FA绕过漏洞正遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524747&idx=1&sn=4048d2d12b0a64ce62d92a0b79a83100&scene=21#wechat_redirect)  
  
  
[Fortinet 提醒注意严重的 FortiCloud SSO 登录认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524622&idx=1&sn=c4730e9500580e409534b376a56f70db&scene=21#wechat_redirect)  
  
  
[Fortinet：注意这个严重的 FortiSIEM 预认证 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523808&idx=1&sn=ef2a5d044fa1a9c53dc3920c5ce650d5&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://thehackernews.com/2026/02/fortinet-patches-critical-sqli-flaw.html  
  
  
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
  
