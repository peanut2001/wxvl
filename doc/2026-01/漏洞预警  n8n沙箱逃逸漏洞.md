#  漏洞预警 | n8n沙箱逃逸漏洞  
浅安
                    浅安  浅安安全   2026-01-23 00:01  
  
**0x00 漏洞编号**  
- # CVE-2026-0863  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
n8n是一个开源的工作流自动化工具，旨在帮助用户通过图形化界面设计和自动化各种任务。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SXegCZMibyIR1YelBVxaA603bUnpUvAtyaDAs19UkmMRXjPEWib9mWjTJuZDWkd5UzaDWBkOpG3iczcw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
  
**0x03 漏洞详情**  
  
**CVE-2026-0863**  
  
**漏洞类型：**  
沙箱  
逃逸  
  
**影响：**  
任意代码执行  
  
**简述：**  
n8n中Python任务执行器存在沙箱逃逸漏洞，攻击者可利用字符串格式化与异常处理机制，绕过n8n对Python代码块所实施的沙箱限制，进而执行不受限制的任意Python代码。该漏洞可被具备基础权限的已认证用户触发，通过Code节点在“Internal”执行模式下直接在宿主系统上实现任意代码执行，最终可能导致n8n实例被完全接管。  
  
**0x04 影响版本**  
- n8n < 1.123.14  
  
- 2.0.0 <= n8n < 2.3.5  
  
- 2.4.0 <= n8n < 2.4.2  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://n8n.io/  
  
  
  
