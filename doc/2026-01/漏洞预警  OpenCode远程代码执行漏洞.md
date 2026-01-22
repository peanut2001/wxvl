#  漏洞预警 | OpenCode远程代码执行漏洞  
浅安
                    浅安  浅安安全   2026-01-22 00:01  
  
**0x00 漏洞编号**  
- # CVE-2026-22812  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
OpenCode是一个开源的AI编码代理工具，支持在终端、IDE或桌面应用中使用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SUO78e1eNb7w6qVvWYBJWrPLiaDqWfdIIsfSs9jEAG16WxvOvH9coQCWyqibb3aUGWhtKw8QPTNHAlQ/640?wx_fmt=png&from=appmsg "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-22812**  
  
**漏洞类型：**  
远程代码执行  
  
**影响：**  
执行任意命令  
  
  
  
**简述：**  
OpenCode存在远程代码执行漏洞，由于其默认启动未经身份验证的HTTP服务器，允许未经授权的远程攻击者通过本地进程或宽松的CORS策略的网站以用户的权限执行任意shell命令。  
  
**0x04 影响版本**  
- Opencode < 1.0.216  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://github.com/anomalyco/opencode/  
  
  
  
