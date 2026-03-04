#  谷歌安卓更新修复已遭利用的高通 0day 漏洞  
Ionut Arghire
                    Ionut Arghire  代码卫士   2026-03-04 10:30  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**本周一，谷歌宣布推出新的安卓安全更新，包含近130个漏洞的补丁，其中一个漏洞已遭利用。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
这个已遭利用的漏洞编号是CVE-2026-21385（CVSS评分7.8），影响200多个高通芯片集的图形组件，是整数上溢或回绕问题，当使用内存分配的字节对齐时会导致内存损坏。  
  
据Jamf公司的高级企业战略经理 Adam Boynton称，成功利用该漏洞可能使攻击者“绕过安全控制，获得对系统的未授权控制权限”。高通在安全公告中提到，该漏洞在2025年12月18日通过谷歌安卓安全团队报送，谷歌在2月2日将漏洞告知客户并在周一披露。  
  
谷歌在安全公告中提到，“有线索表明CVE-2026-21385可能遭到有限的针对性利用。”虽然该公司并未详述相关攻击详情，但此类漏洞经常遭商业监控软件厂商利用。  
  
该漏洞的修复方案已包含在本月安全更新的第二部（2026-03-05安全补丁级别）。该补丁级别修复了位于内核、Arm、Imagination Technologies、联发科、Unisoc 和高通组件中的60多个漏洞。该更新的第一部分（2026-03-01安全补丁级别）包含50多个漏洞，它们位于 Framework 和 System 组件中，其中一些严重漏洞可导致任意代码执行和拒绝服务后果。谷歌提到，“其中最严重的漏洞位于系统组件中，无需其它执行权限即可导致远程代码执行后果。利用该漏洞无需用户交互。”  
  
运行2026-03-05或更高安全级别的设备中包含所有漏洞的补丁。  
  
本周一，谷歌还宣布发布两个 Wear OS 漏洞的修复方案，这些漏洞影响该平台的 Framework 和 System 组件。该更新中还包括安卓2026年3月份安全通告中所说明的所有漏洞的补丁。  
  
谷歌表示，本月安卓Automotive OS 和 Android XR 更新中并不包含针对特定平台的补丁。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[谷歌修复107个安卓漏洞，其中2个已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524571&idx=1&sn=877a0981b4dec19068dff6f479fce3b9&scene=21#wechat_redirect)  
  
  
[谷歌：速修复系统组件中的这个安卓零点击RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524330&idx=1&sn=5a3facd9ebc276e8428c3c0ea811bbd2&scene=21#wechat_redirect)  
  
  
[谷歌修复安卓遭活跃利用的 FreeType 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522938&idx=2&sn=d6e089276d9d14177da8b1d1e1d32736&scene=21#wechat_redirect)  
  
  
[谷歌修复已遭利用的安卓0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522418&idx=1&sn=6414a084ddce5639ed66ee1cdf5970cb&scene=21#wechat_redirect)  
  
  
[安卓间谍软件 NoviSpy 利用高通6个0day感染设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521826&idx=2&sn=2e115cf641ac90636ca05cde8df5fa09&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.securityweek.com/android-update-patches-exploited-qualcomm-zero-day/  
  
  
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
  
