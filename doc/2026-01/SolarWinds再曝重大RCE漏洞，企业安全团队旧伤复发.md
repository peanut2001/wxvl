#  SolarWinds再曝重大RCE漏洞，企业安全团队旧伤复发  
 FreeBuf   2026-01-29 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF87cf3iaicWjxpYIa8dtzQW2OHDxPg73ZY1ImM4f64uBCDcP4KwBkVJFcQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
SolarWinds再次曝出旗下广受欢迎产品的安全漏洞。该公司已发布更新补丁，修复其IT服务管理软件Web Help Desk（WHD）中六个关键的身份验证绕过和远程代码执行（RCE）漏洞。  
  
  
这些漏洞可能允许攻击者绕过身份验证、执行远程代码并访问本应受限的功能。六个漏洞中有四个被评为"严重"（CVE严重性评分9.8/10），其余两个为"高危"（评分7.5和8.1）。  
  
  
鉴于WHD产品历史上曾遭实际攻击，管理员应立即升级至Web Help Desk 2026.1版本修补漏洞。"我们已经见识过入侵SolarWinds的后果，"Beauceron Security的David Shipley警告道，"存在巨大的连锁风险，必须尽快完成补丁更新。"  
  
  
**Part01**  
## RCE：安全主管最不愿听到的三个字母  
  
  
SolarWinds声称其全球客户超过30万，包括大量《财富》500强企业及政府国防机构。此次漏洞由watchTowr和Horizon3.ai的研究人员发现，具体包括：  
  
- 远程代码执行与数据反序列化漏洞（CVE-2025-40551和CVE-2025-40553，均为严重级）  
  
- 身份验证绕过漏洞（CVE-2025-40552、CVE-2025-40554为严重级，CVE-2025-40536、CVE-2025-40537为高危级）  
  
CVE-2025-40551和CVE-2025-40553使WHD易受不可信数据反序列化攻击，攻击者无需认证即可在主机执行命令。另两个严重漏洞（CVE-2025-40552和CVE-2025-40554）则可能让攻击者调用本应受认证保护的功能。  
  
  
"数据反序列化可能泄露企业机密，RCE是最糟糕的情况，"Shipley强调。Rapid7研究员Ryan Emmons指出，这些反序列化和认证逻辑缺陷使漏洞利用成功率极高，攻击者可使用标准化恶意载荷控制软件并获取全部存储信息。  
  
  
**Part02**  
## 企业应对措施  
  
  
SolarWinds已提供升级至WHD 2026.1的详细指南。分析师强调安全团队必须立即行动，Emmons建议紧急升级版本并检查服务器异常活动："这些漏洞很快就会出现武器化利用，时间至关重要。"  
  
  
**Part03**  
## SolarWinds的安全困局  
  
  
这已是WHD产品近年第三次曝出重大漏洞。2024年9月，该公司刚修补了CISA通报的另一个RCE漏洞（CVE-2025-26399）。"就像历史重演，"Shipley表示，五年前重大入侵事件的阴影仍困扰着IT管理者。  
  
  
虽然此次事件与过往漏洞不同，且SolarWinds在RCE漏洞方面表现优于思科和Fortinet，但Shipley指出厂商仅修补漏洞而不解决编程逻辑根源问题的做法不可持续。"我们即将迎来代码系统的'卡特里娜时刻'，"他警告道，强调美国当前网络安全监管出现"彻底转向"，改善代码质量才是唯一出路。  
  
  
**参考来源：**  
  
SolarWinds, again: Critical RCE bugs reopen old wounds for enterprise security teams  
  
https://www.csoonline.com/article/4124030/solarwinds-again-critical-rce-bugs-reopen-old-wounds-for-enterprise-security-teams.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334591&idx=1&sn=7a53f598d945f86ed376200b93146133&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
