#  谷歌警告WinRAR必须更新！漏洞正被黑客疯狂利用：已有大量用户中招  
 信安在线资讯   2026-01-30 01:08  
  
日前谷歌威胁情报小组（GTIG）发布全球性安全预警，  
**指出去年发现的WinRAR高风险漏洞（CVE-2025-8088）正在被黑客大规模利用，且目前已出现大量中招案例。**  
  
虽然官方已在7.13版本中修复了该问题，但仍有大量用户因未及时更新而面临系统被全面控制的风险。  
  
![谷歌警告WinRAR必须更新！漏洞正被黑客疯狂利用：已有大量用户中招](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaWwR1QrX8pvJM6qE2XiaLJK8JeibAKmwKsvJ0I5ptG6BqRRZZR19LX8aUoxMyYlHr0kRfkzKKNEjKA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1 "")  
  
据谷歌介绍，WinRAR 7.12及更早版本存在严重漏洞，攻击者可利用该漏洞在解压时错误地将文件写入系统目录，最终实现恶意代码执行并获取系统控制权，该漏洞在CVSS中的得分为 8.4/10，属于高风险等级。  
  
攻击的核心机制是利用Windows系统的“备用数据流”（ADS）特性进行路径遍历攻击，通常情况下，黑客会将恶意文件隐藏在压缩包内诱饵文件的ADS中。  
  
**当用户查看诱饵文件时，WinRAR会在后台通过目录遍历，将恶意负载（如LNK、HTA、BAT或脚本文件）解压并释放到任意位置。**  
  
黑客最常选择的目标是Windows的 “启动（Startup）”文件夹，从而确保恶意软件在用户下次登录时自动执行，实现长期潜伏。  
  
谷歌指出，目前包括UNC4895（RomCom）、APT44以及Turla在内的多个知名黑客组织正积极利用该漏洞。  
  
攻击者主要通过鱼叉式网络钓鱼，将恶意RAR附件伪装成“求职简历”或“发票”，投放包括Snipbot、Mythic Agent在内的各类后门木马，受害者涵盖金融、制造、国防及物流等多个重要领域。  
  
**由于WinRAR没有自动更新功能，许多用户可能仍在使用易受攻击的旧版本，建议手动将版本升级至WinRAR 7.13或更高版本。**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/P4iaXc3dZWwXkz0dKnumYtbFQsEtKZbAU4L5zic1eyuakhianrZ5x7mRpA5AaP7EWUSbibyscQTBdebsR7WAfLicQyg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
原文来源：安全圈  
  
  
**end**  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/P4iaXc3dZWwUh6aAJKHdg03U8MjI2BEHkyyjjNjRoqoG8lLIcwFpiczlibBXqXloia8NEd73sa6nyawS8ic3gtO2exQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=gt07df4r&tp=webp#imgIndex=1 "")  
  
  
