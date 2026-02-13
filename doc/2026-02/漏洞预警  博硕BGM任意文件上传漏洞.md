#  漏洞预警 | 博硕BGM任意文件上传漏洞  
浅安
                    浅安  浅安安全   2026-02-13 00:02  
  
**0x00 漏洞编号**  
- # 暂无  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
博硕BGM是山东博硕自动化技术有限公司开发的混凝土搅拌站信息管理系统，它通过整合多种系统，实现了商品混凝土生产企业业务流程的规范化、信息化、自动化和智能化。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SXTPtMzj3nbNuGrcoE07yfBrAz1rNyQr3RProaZTuWYHBWicMr2MHhPPCEbSUUfIA1rZATibiaIr1VTA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
**0x03 漏洞详情**  
  
漏洞类型：  
任意文件上传  
  
**影响：**  
上传恶意脚本****  
  
**简述：**  
博硕BGM的/WebUpload/server/Upload.ashx接口存在任意文件上传漏洞，未经身份验证的攻击者可以通过该漏洞上传恶意脚本文件，从而控制目标服务器。  
  
**0x04 影响版本**  
- 博硕BGM  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.bosure.cn/  
  
  
  
