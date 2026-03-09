#  漏洞预警 | XWiki跨站脚本漏洞  
浅安
                    浅安  浅安安全   2026-03-08 23:50  
  
**0x00 漏洞编号**  
- CVE-  
2026-24128  
  
**0x01 危险等级**  
- 中危  
  
**0x02 漏洞概述**  
  
XWiki Platform是一款基于Java的企业级开源Wiki与知识管理平台，支持结构化数据、脚本编写、权限管理，并可作为协作门户或文档中心运行。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SXY1SUib7zvhIc861biaWCm7mvRWuFVKhwMTebF8X0IOqNnQBtibQRniagiaJ8XkfBKc8M3uXyzVF1BCuA/640?wx_fmt=png&from=appmsg&randomid=7s9qrka5&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-24128**  
  
**漏洞类型：**  
跨站脚本  
  
**影响：**  
泄露敏感信息  
  
**简述：**  
XWiki Platform存在反射型跨站脚本漏洞，攻击者可以构造恶意URL诱导受害者访问，进而以该权限执行特权操作。  
  
**0x04 影响版本**  
- 7.0-milestone-2 < XWiki Platform < 16.10.11  
  
- 17.5.0-rc-1 < XWiki Platform < 17.7.0  
  
- 17.0.0-rc-1 < XWiki Platform < 17.4.4  
  
**0x05****POC状态**  
- 未公开  
  
**0x06****修复建议**  
  
******目前官方已发布漏洞修复版本，建议用户升级到安全版本****：******  
  
https://www.xwiki.org/  
  
  
  
