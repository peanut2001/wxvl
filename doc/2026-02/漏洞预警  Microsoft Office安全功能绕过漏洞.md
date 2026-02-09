#  漏洞预警 | Microsoft Office安全功能绕过漏洞  
浅安
                    浅安  浅安安全   2026-02-08 23:50  
  
**0x00 漏洞编号**  
- # CVE-2026-21509  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
Microsoft Office是微软公司开发的一套基于Windows操作系统的办公软件套装。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SXwCq1ryjzf7MMcj7GbibrGsAibUv1nGbUImGKn8UCEeZBgrXK9loZWhjFHmrOo01eqP1Inq1uicCupQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
**0x03 漏洞详情**  
### CVE-2026-21509  
  
**漏洞类型：**  
安全功能绕过  
  
**影响：**  
执行任意代码  
  
**简述：**  
Microsoft Office存在安全功能绕过漏洞，由于其在进行安全决策时依赖了不可信的输入数据，攻击者可以通过构造恶意Office文档绕过用于保护用户免受脆弱COM/OLE控件侵害的安全机制。  
  
**0x04 影响版本**  
- Microsoft Office 2016  
  
- Microsoft Office 2019  
  
- Microsoft Office LTSC 2021  
  
- Microsoft Office LTSC 2024  
  
- Microsoft 365 Apps for Enterprise  
  
**0x05****POC状态**  
- 未公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://msrc.microsoft.com/update-guide/zh-cn/vulnerability/  
CVE-2026-21509  
  
  
  
