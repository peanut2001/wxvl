#  漏洞预警 | Windows记事本远程代码执行漏洞  
浅安
                    浅安  浅安安全   2026-03-02 00:01  
  
**0x00 漏洞编号**  
- # CVE-2026-20841  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
Windows记事本是微软Windows操作系统内置的一款轻量级纯文本编辑器。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SVleaDeU1ibPickZJzpKIF4Mcm9iaHXXSDJfzdooHoG4ZA4iaHupxCYLp8HtE2qPLEqYibUd5u3E3Nmiczw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
**0x03 漏洞详情**  
  
**CVE-2026-20841**  
  
**漏洞类型：**  
远程代码执行  
  
**影响：**  
执行任意代码  
  
**简述：**  
Windows记事本存在远程代码执行漏洞，由于其在处理Markdown文件中的超链接时，未能对特殊协议或命令元素进行充分的中和与验证，攻击者可利用该漏洞构造特制的恶意Markdown文件，诱骗用户打开文件并点击其中的恶意链接，进而在受害者设备上执行任意恶意代码。  
  
**0x04 影响版本**  
- Windows记事本 < 11.2510  
   
  
**0x05****POC状态**  
- 已公开  
  
****  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://msrc.microsoft.com/update-guide/zh-cn/vulnerability/  
CVE-  
2026-20841  
  
  
  
