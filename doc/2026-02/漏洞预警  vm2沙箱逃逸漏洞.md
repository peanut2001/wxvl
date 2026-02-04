#  漏洞预警 | vm2沙箱逃逸漏洞  
浅安
                    浅安  浅安安全   2026-02-04 00:02  
  
**0x00 漏洞编号**  
- # CVE-2026-22709  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
vm2是一个可以运行不可信代码的Node.js沙箱，可以防止不可信代码访问系统资源或外部数据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SVickEOS1ibCOQNvUth1poEja9ZKWXgia5e4XxQzNIuoGRY6iblr3jXx4ao4bKcsAdGtqgic7K19gdibPQA/640?wx_fmt=png&from=appmsg "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-22709**  
  
**漏洞类型：**  
沙箱逃逸  
  
**影响：**  
执行任意代码  
  
**简述：**  
vm2存在沙箱逃逸漏洞，由于Promise.prototype.then和Promise.prototype.catch的回调函数未能有效地对传入的数据进行适当的过滤和隔离，导致攻击者能够绕过沙箱的限制，执行任意代码。  
。  
  
**0x04 影响版本**  
- vm2 <= 3.10.0  
  
**0x05 POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://github.com/patriksimek/vm2  
  
  
  
