#  漏洞预警 | GNU InetUtils telnetd远程身份认证绕过漏洞  
浅安
                    浅安  浅安安全   2026-01-30 00:02  
  
**0x00 漏洞编号**  
- CVE-  
2026-24061  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
GNU InetUtils telnetd是GNU InetUtils套件中的远程登录服务守护进程，为客户端提供基于Telnet协议的明文终端接入能力。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SW4gkeJaWyibvWC23ytRjjMbueKmPsibnx75TjkXXmo63RN9CDPMOOmnHJ5SnkYY2zdkoib5EUiaOZtgA/640?wx_fmt=png&from=appmsg "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-24061**  
  
**漏洞类型：**  
身份认证绕过  
  
**影响：**  
获取权限  
  
**简述：**  
GNU InetUtils telnetd存在远程身份认证绕过漏洞，telnetd在调用系统/usr/bin/login程序时，未对从客户端USER环境变量传入的用户名做过滤，直接拼接到login命令行。未经授权的远程攻击者可利用该缺陷，在无需任何口令的情况下直接获取目标主机的root shell，造成完全控制权泄露、敏感信息被窃取或进一步横向移动。  
  
**0x04 影响版本**  
- 1.9.3 <= GNU InetUtils <= 2.7  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
******目前官方已发布漏洞修复版本，建议用户升级到安全版本****：******  
  
https://www.gnu.org/software/inetutils/  
  
  
  
