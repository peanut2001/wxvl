#  思科修复了攻击中利用的统一通信远程代码执行 0 day 漏洞  
Rhinoer
                    Rhinoer  犀牛安全   2026-02-13 16:00  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlibkAjaR8rHFBibnQTUkSKXUPnFqHDXM5q05F50pGZRpwT2G2ACPMREseteLXHLfhRWbrYaJzJwicGg/640?wx_fmt=png&from=appmsg "")  
  
思科已修复了 Unified Communications 和 Webex Calling 的一个严重远程代码执行漏洞（编号为 CVE-2026-20045），该漏洞已被积极利用为零日攻击。  
  
该漏洞编号为 CVE-2026-20045，影响 Cisco Unified Communications Manager (Unified CM)、Unified CM Session Management Edition (SME)、Unified CM IM & Presence、Cisco Unity Connection 和 Webex Calling Dedicated Instance。  
  
思科在其安全公告中警告说：“此漏洞是由于对 HTTP 请求中用户提供的输入验证不当造成的。攻击者可以通过向受影响设备的基于 Web 的管理界面发送一系列精心构造的 HTTP 请求来利用此漏洞。 ”  
  
“成功利用漏洞可能使攻击者获得底层操作系统的用户级访问权限，然后提升权限至 root。”  
  
虽然该漏洞的 CVSS 评分为 8.2，但思科将其评为严重级别，因为利用该漏洞可获得服务器上的 root 权限。  
  
思科已发布以下软件更新和补丁文件以解决该漏洞：  
  
Cisco Unified CM、Unified CM IM&P、Unified CM SME 和 Webex Calling  
 专用实例版本发布：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlibkAjaR8rHFBibnQTUkSKXUc7AIibC56cZoZzmR7SA0sJ5ktvrO3WfNM0Tf1G0vribpDWw4Jotyl2tw/640?wx_fmt=png&from=appmsg "")  
  
Cisco Unity Connection 版本：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlibkAjaR8rHFBibnQTUkSKXUdQUwpXibBgskjqqSXXJibN2VwKoeticerDNVx2JA84jvopbcmBf4LAHow/640?wx_fmt=png&from=appmsg "")  
  
该公司表示，这些补丁是针对特定版本的，因此在应用补丁之前应该先查看 README 文件。  
  
思科产品安全事件响应团队 (PSIRT) 已确认，有人试图利用该漏洞，并敦促客户尽快升级到最新软件。  
  
该公司还表示，除了安装更新之外，没有其他方法可以缓解该缺陷。  
  
美国网络安全和基础设施安全局 (CISA) 已将 CVE-2026-20045 添加到其已知利用漏洞 (KEV) 目录中，并要求联邦机构在 2026 年 2 月 11 日之前部署更新。  
  
本月初，思科修复了身份服务引擎 (ISE) 的一个漏洞，该漏洞包含公开的概念验证利用代码，以及自 11 月以来一直被利用的 AsyncOS 零日漏洞。  
  
  
信息来源：BleepingComputer  
  
