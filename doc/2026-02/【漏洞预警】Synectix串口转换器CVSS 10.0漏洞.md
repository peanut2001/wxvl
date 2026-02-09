#  【漏洞预警】Synectix串口转换器CVSS 10.0漏洞  
 博智非攻研究院   2026-02-09 09:50  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/ibQxG9cezyUYOCE1WKtTJZjTlHOhu42yCbr2tZ6du8qfF7H6ekFKuuO0a0rRUAILMzGTq8yT8UQj4ERZct4Gib9Q/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
  
01  
  
  
**概 述**  
  
近日，美国网络安全和基础设施安全局 (CISA) 已针对 Synectix LAN 232 TRIO（一款传统的串口转以太网适配器）发布了最高级别、CVSS 评分为 10.0的安全警报，该漏洞编号为 CVE-2026-1633。  
  
02  
  
  
**验 证**  
  
根据公告该缺陷既简单又致命：攻击者无需凭据即可直接访问该设备的Web管理界面，可以直接进入，因此设备完全无法保护其管理界面，攻击者只需访问设备的 IP 地址即可完全控制该设备。  
  
基于网络空间测绘，发现确实有一部分在线设备，可被直接访问：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Q5UWTjoRgIVCJNb4fwh5Iywh8Hl7YmgV0KDYtDGzTy7riaZCic3WyqiceHZu5RtEy0BAfRIkZOlPPZogtMV7SrDkqhpP6b8Z9KRd6TP2a5fmKA/640?wx_fmt=png&from=appmsg "")  
  
  
  
因此，漏洞可能导致未经身份验证的攻击者修改关键设备设置或将设备恢复出厂设置。  
CISA公告警告说：“受影响的产品应视为已停止生产，因为 Synectix 已停止运营，因此将无法提供固件修复、缓解措施和更新。”  
  
  
03  
  
  
**参 考**  
  
1.https://www.cisa.gov/news-events/ics-advisories/icsa-26-034-04  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Q5UWTjoRgIWdbBUCYOicPxHZG3qKicyMjHbcKbkB1HOLWjJAwAMr7VCexX8o03UX1PdTH0ruK74S6Xbn17QcpPfU4E4e1DapbZwqrDvPfXFRk/640?wx_fmt=png&from=appmsg "")  
  
  
