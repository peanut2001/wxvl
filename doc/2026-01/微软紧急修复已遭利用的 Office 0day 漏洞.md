#  微软紧急修复已遭利用的 Office 0day 漏洞  
Sergiu Gatlan
                    Sergiu Gatlan  代码卫士   2026-01-27 09:48  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**微软发布带外更新，紧急修补一个已遭利用的高危Microsoft Office安全特性绕过 0day漏洞 CVE-2026-21509。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
该漏洞影响多个Office版本，包括Microsoft Office 2016、Microsoft Office 2019、Microsoft Office LTSC 2021、Microsoft Office LTSC 2024以及Microsoft 365企业应用版（微软基于云的订阅服务）。不过，微软在公告中提到，针对Microsoft Office 2016和2019版本的安全更新尚未发布，将尽快推出。  
  
虽然预览窗格并非攻击途径，但未经身份验证的本地攻击者仍能通过要求用户交互的低复杂度攻击成功利用该漏洞。微软对此解释称：“Microsoft Office安全决策机制中对不可信输入的依赖，使得未经授权的攻击者能够在本地绕过安全功能。攻击者需向用户发送恶意Office文件并诱使其打开。本次更新修复了一个可绕过Microsoft 365及Microsoft Office中OLE防护机制的漏洞，该机制原本用于保护用户免受存在漏洞的COM/OLE控件威胁。Office 2021及后续版本的用户将通过服务端变更自动获得防护，但需重启Office应用程序才能使保护生效。”  
  
尽管Office 2016和2019版本未能立即获得攻击防护补丁，微软仍提供了一套可能“降低漏洞利用危害程度”的缓解措施，但其说明存在易混淆之处。文章提到，已尝试通过以下指引进行澄清：  
  
1、关闭所有Microsoft Office应用程序。  
  
2、创建Windows注册表备份（错误编辑注册表可能导致系统故障）。  
  
3、通过开始菜单搜索“regedit”打开Windows注册表编辑器（出现搜索结果时按Enter键启动）。  
  
4、打开注册表编辑器后，使用顶部地址栏检查是否存在以下任一注册表项：  
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\16.0\Common\COM Compatibility\ (for 64-bit Office, or 32-bit Office on 32-bit Windows)
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Office\16.0\Common\COM Compatibility\ (for 32-bit Office on 64-bit Windows)
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\ClickToRun\REGISTRY\MACHINE\Software\Microsoft\Office\16.0\Common\COM Compatibility\
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\ClickToRun\REGISTRY\MACHINE\Software\WOW6432Node\Microsoft\Office\16.0\Common\COM Compatibility\
```  
  
  
若上述注册表路径中不存在对应项，需在当前路径下右键点击“Common”项，选择“新建→项”，创建名为“COM Compatibility”的新项。  
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Office\16.0\Common\
```  
  
5、 随后右键单击已存在或新建的“COM Compatibility”项，选择“新建→项”，将其命名为“{EAB22AC3-30C1-11CF-A7EB-0000C05BAE0B}”。  
  
6、 新建该子项后，右键单击该项并选择“新建→DWORD (32位) 值”，将新建的值命名为“Compatibility Flags”。  
  
7、 创建该数值后，双击打开“Compatibility Flags”，确保基数选项设置为“十六进制”，在数值数据字段中输入“400”。  
  
完成上述步骤后，重启Office应用程序即可启用漏洞缓解措施。  
  
微软尚未透露该漏洞的发现者信息，也未公布任何关于漏洞利用方式的具体细节。微软发言人尚未就此置评。本月微软发布补丁星期二已修复114个安全漏洞，其中包含1个已遭活跃利用的漏洞和2个已公开披露的0day漏洞。本月修复的另一个被活跃利用的0day漏洞是位于桌面窗口管理器中的信息泄露漏洞。微软将其标记为“重要”级别，可导致攻击者读取与远程ALPC端口相关的内存地址。  
  
上周，微软还发布了多轮带外Windows更新，用于修复由1月补丁星期二更新引发的系统关机故障和云电脑异常问题，同时另发布了一组紧急更新以解决导致经典版Outlook邮件客户端冻结或无响应的问题。  
  
****  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[微软2026年1月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524868&idx=1&sn=511dcdb0c6fcd3cd07ef7783b225bcf4&scene=21#wechat_redirect)  
  
  
[微软将影响在线服务的第三方漏洞纳入奖励计划](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524650&idx=3&sn=b7863ac8099dfd54d53e02832cf2eb2f&scene=21#wechat_redirect)  
  
  
[微软12月补丁星期二值得关注的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524622&idx=2&sn=ba8c3120218ed455901938344a91aa4f&scene=21#wechat_redirect)  
  
  
[微软悄悄修复多年前就已遭利用的 LNK 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524584&idx=1&sn=c3b264a905dace804ae6937303f8f391&scene=21#wechat_redirect)  
  
  
[微软Azure Bastion 严重漏洞可导致攻击者绕过认证和实现提权](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524481&idx=2&sn=46622d694aa60bc2d314867e3e424ec1&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-actively-exploited-office-zero-day-vulnerability/  
  
  
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
  
