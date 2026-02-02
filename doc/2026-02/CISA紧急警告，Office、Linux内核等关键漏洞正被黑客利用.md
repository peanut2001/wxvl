#  CISA紧急警告，Office、Linux内核等关键漏洞正被黑客利用  
 FreeBuf   2026-02-02 10:31  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibvic9mib2trd1W0JGAJEHlF8NibibBv9dSb6VOpCF8sk5YmUgZD3Dz69l2BttH9ZYMJcibxucicEKw8wqg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
美国网络安全和基础设施安全局（CISA）已将Microsoft Office、GNU InetUtils、SmarterTools SmarterMail及Linux内核相关漏洞纳入其已知可利用漏洞（KEV）目录。以下是新增漏洞清单：  
  
- （CVE-2018-14634）Linux内核整数溢出漏洞  
  
- （CVE-2025-52691）SmarterTools SmarterMail危险类型文件无限制上传漏洞  
  
- （CVE-2026-21509）Microsoft Office安全功能绕过漏洞  
  
- （CVE-2026-23760）SmarterTools SmarterMail通过替代路径或通道的身份验证绕过漏洞  
  
- （CVE-2026-24061）GNU InetUtils参数注入漏洞  
  
**Part01**  
## Linux内核高危漏洞分析  
  
  
2018年9月，安全研究人员在Linux内核中发现被标记为（CVE-2018-14634）的整数溢出漏洞（代号"Mutagen Astronomy"），影响Red Hat、CentOS和Debian发行版。普通用户可利用该漏洞获取目标系统的超级用户权限。  
  
  
该漏洞由Qualys安全公司研究人员发现，其公开了包含PoC利用代码（Exploit 1、Exploit 2）在内的技术细节。影响范围涵盖2007年7月至2017年7月期间发布的2.6.x、3.10.x和4.14.x内核版本，但Red Hat Enterprise Linux 5的内核版本不受影响。  
  
  
漏洞存在于内核管理内存表的create_elf_tables()函数中。与其他本地提权漏洞类似，攻击者需先获得目标系统访问权限，再执行触发缓冲区溢出的利用代码，最终实现任意代码执行并完全控制受感染主机。  
  
  
**Part02**  
## Microsoft Office零日漏洞紧急修复  
  
  
目录中新增的（CVE-2026-21509）漏洞促使微软本周发布带外安全更新。该安全功能绕过漏洞影响Office 2016/2019、LTSC 2021/2024及Microsoft 365企业版。  
  
  
微软公告确认："Office安全决策中依赖不可信输入，导致攻击者可本地绕过安全功能。攻击者需诱使用户打开恶意Office文件。"该漏洞会绕过OLE安全防护机制，但预览窗格不受影响。微软未披露具体攻击技术细节。  
  
  
**Part03**  
## GNU InetUtils潜伏11年的致命缺陷  
  
  
被标记为（CVE-2026-24061）（CVSS 9.8分）的关键漏洞影响GNU InetUtils 1.9.3至2.7版本的telnet守护进程（telnetd），可导致攻击者获取root权限。该漏洞源于2015年3月的代码提交，潜伏近11年才被发现。  
  
  
**Part04**  
## SmarterMail邮件服务器高危漏洞  
  
  
新加坡网络安全局（CSA）早在2025年12月就预警过（CVE-2025-52691）（CVSS 10.0分）漏洞，允许未经认证的攻击者通过任意文件上传实现远程代码执行。受影响版本为Build 9406及更早，建议立即升级至Build 9413。  
  
  
根据第22-01号约束性操作指令（BOD），联邦机构须在2026年2月16日前修复这些漏洞。安全专家同时建议私营机构自查基础设施中的相关漏洞。  
  
  
**参考来源：**  
  
U.S. CISA adds Microsoft Office, GNU InetUtils, SmarterTools SmarterMail, and Linux Kernel flaws to its Known Exploited Vulnerabilities catalog  
  
https://securityaffairs.com/187375/security/u-s-cisa-adds-microsoft-office-gnu-inetutils-smartertools-smartermail-and-linux-kernel-flaws-to-its-known-exploited-vulnerabilities-catalog.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334591&idx=1&sn=7a53f598d945f86ed376200b93146133&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
