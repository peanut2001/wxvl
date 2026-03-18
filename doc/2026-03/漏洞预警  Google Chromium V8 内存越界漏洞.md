#  漏洞预警 | Google Chromium V8 内存越界漏洞  
浅安
                    浅安  浅安安全   2026-03-18 00:02  
  
**0x00 漏洞编号**  
- # CVE-2026-3910  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
Chromium是由Google主导开发的开源Web浏览器项目，其核心组件包括Blink渲染引擎和V8 JavaScript引擎。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/7stTqD182SXxjX8p8WklXuc23v1DKPW7yY83Sic75o0z0rlPgZHmmCPxBNvutPR92HthYPDsg7ia0ODDgsgQYjBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=gigpt6px&tp=webp#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-3910**  
  
**漏洞类型：**  
内存越界  
  
**影响：**  
执行  
任意代码  
  
**简述：**  
Google Chromium V8存在内存越界漏洞，由于其在处理内存缓冲区相关操作时未能正确限制访问边界，导致可能发生越界读写等异常内存访问行为。当用户访问攻击者构造的恶意HTML页面或执行特制的JavaScript代码时，可能触发该漏洞并在浏览器沙箱环境中执行任意代码。  
  
**0x04 影响版本**  
- Chrome Windows/Mac < 146.0.7680.75/76  
  
- Chrome Linux < 146.0.7680.75  
  
**0x05****POC状态**  
- 未公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.google.com/intl/zh-CN/chrome/  
  
  
  
