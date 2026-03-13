#  思科修复多个高危 IOS XR 漏洞  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-03-13 10:29  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**本周三，思科发布半年度 IOS XR 软件安全公告，其中三个公告详述了四个高危漏洞。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXYQed1jfo93UmcKHB0GH7QggkxunZXwnd6uIltibiaahYTse8iagfsHuZWoBicZMugeYZhfYNLkaicbZuFkrN4nlKGND2eu1kAlz7k/640?wx_fmt=gif&from=appmsg "")  
  
  
其中最严重的漏洞是CVE-2026-20040和CVE-2026-20046（CVSS评分8.8），它们可被用于以 root 权限执行任意命令或者获得设备的管理员控制权限。CVE-2026-20040存在的原因在于传递给具体 CLI 命令的用户参数未被充分验证，导致低权限攻击者可在提示词级别输入构造命令。思科在安全公告中提到，“成功利用可导致攻击者提权至 root 并在底层操作系统上执行任意命令。”  
  
CVE-2026-20046 影响特定 CLI 命令的任务组分配，是因为在源代码中该命令被错误地映射到任务组而导致的。该漏洞可导致低权限攻击者通过 CLI 命令绕过基于任务组的检查，在无需授权检查的情况下将权限提升至管理员并执行各种操作。  
  
周三，思科还宣布修复位于 IOS XR IS-IS 多实例路由特性中的漏洞CVE-2026-20074（CVSS评分7.4），可被用于重启 IS-IS 流程。对入口 IS-IS 数据包的输入验证不充分可导致未经身份验证的邻近攻击者向易受攻击的设备发送特殊构造的数据包，导致 IS-IS 进程重启，从而导致拒绝服务条件。  
  
第四个高危漏洞CVE-2026-20118（CVSS评分6.8）影响出口数据包网络接口 (EPNI) 对齐器中断的处理。在重载传输流量期间触发 EPNI 对齐器中断时造成的数据包损坏，可能导致攻击者通过向易受攻击的设备持续发送特殊构造的数据包流，导致持续性的严重丢包和拒绝服务状况。  
  
这些漏洞的修复方案已发布，思科表示并未发现这些漏洞遭在野利用的证据。本周三，思科还修复了位于 Packaged CCE、Unified CCE、Unified CCX 和 Unified Intelligence Center 中的两个中危漏洞，它们可被远程未认证攻击者用于 XSS 攻击。  
  
  
****  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[思科：注意已遭利用的两个 Catalyst SD-WAN 管理器 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525349&idx=2&sn=d24d6683fb3bc04d5b47bb36bf521194&scene=21#wechat_redirect)  
  
  
[思科提醒注意满分 Secure FMC 漏洞可用于获取 root 权限](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525317&idx=1&sn=400b0183f75f78413cb8fd0ab335e576&scene=21#wechat_redirect)  
  
  
[思科修复已遭利用的 Unified CM RCE 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524955&idx=2&sn=922edf69046bb2a552b3f58f4f21f882&scene=21#wechat_redirect)  
  
  
[思科：速修复已出现 exp 的身份服务引擎漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524828&idx=1&sn=d0696191628f6b13a09be6edecbbec4d&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.securityweek.com/cisco-patches-high-severity-ios-xr-vulnerabilities-2/  
  
  
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
  
