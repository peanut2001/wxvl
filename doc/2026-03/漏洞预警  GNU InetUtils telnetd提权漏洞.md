#  漏洞预警 | GNU InetUtils telnetd提权漏洞  
浅安
                    浅安  浅安安全   2026-03-05 00:00  
  
**0x00 漏洞编号**  
- CVE-  
2026-  
28372  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
GNU InetUtils telnetd是GNU InetUtils套件中的远程登录服务守护进程，为客户端提供基于Telnet协议的明文终端接入能力。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SW4gkeJaWyibvWC23ytRjjMbueKmPsibnx75TjkXXmo63RN9CDPMOOmnHJ5SnkYY2zdkoib5EUiaOZtgA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-28372**  
  
**漏洞类型：**  
提权  
  
**影响：**  
权限提升  
  
**简述：**  
GNU Inetutils中telnetd组件存在提权漏洞，由于其对客户端可控环境变量过滤不严格，攻击者可通过设置CREDENTIALS_DIRECTORY，并在对应目录中创建包含特定内容的login.noauth文件，诱使以root权限执行的/bin/login跳过正常身份认证流程，最终获取root权限。  
  
**0x04 影响版本**  
- GNU Inetutils <= 2.7  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
******目前官方已发布漏洞修复版本，建议用户升级到安全版本****：******  
  
https://www.gnu.org/software/inetutils/  
  
  
  
