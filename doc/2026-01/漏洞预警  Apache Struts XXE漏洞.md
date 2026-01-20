#  漏洞预警 | Apache Struts XXE漏洞  
浅安
                    浅安  浅安安全   2026-01-20 00:00  
  
**0x00 漏洞编号**  
- # CVE-2025-68493  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
Apache Struts是一个基于Java的开源Web应用开发框架，采用MVC架构模式，主要用于构建企业级Web应用。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SVDY1k1EV3mQPDLmTdI33eb3QzvmIVC7HcvvMgtdtYQj6TomcOd5MjaKeicrJy7GZibiaPmACibOZvxdg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2025-68493**  
  
**漏洞类型：**  
XXE****  
  
**影响：**  
获取敏感信息  
  
**简述：**  
Apache Struts框架的XWork组件存在XXE漏洞，由于其在解析XML配置文件时，未对XML外部实体进行充分校验与限制，导致攻击者可通过构造恶意XML内容触发外部实体解析。成功利用后，可能造成敏感数据泄露、拒绝服务以及服务器端请求伪造等安全影响。  
  
**0x04 影响版本**  
- 2.0.0 <= Apache Struts <= 2.3.37  
  
- 2.5.0 <= Apache Struts <= 2.5.33  
  
- 6.0.0 <= Apache Struts <= 6.1.0  
  
**0x05 POC状态**  
- 未公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://struts.apache.org/  
  
  
  
