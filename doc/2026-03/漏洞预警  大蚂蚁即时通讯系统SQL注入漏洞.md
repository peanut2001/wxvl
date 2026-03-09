#  漏洞预警 | 大蚂蚁即时通讯系统SQL注入漏洞  
浅安
                    浅安  浅安安全   2026-03-08 23:50  
  
**0x00 漏洞编号**  
- # 暂无  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
杭州九麒科技大蚂蚁即时通讯系统是一款企业级IM通信管理系统，提供多种功能支持。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NQlfTO30MhxMEz4o0bVV8lLONETG6JM1dDvGIAFs4OHuhAkKjZV96gUxdEBf1ZNKOLClibtDxc3mqicicRu2rrIsuZMk97KLpaYuXRr624IVKQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**漏洞类型：**  
SQL注入  
  
**影响：**  
获取敏感信息  
  
**简述：**  
大蚂蚁即时通讯系统的  
/api/dept/moveDept接口存在SQL注入漏洞，未经身份验证的攻击者可以通过/api/oauth/create_authen接口获取authen，从而利用SQL注入获取数据库敏感信息。  
  
**0x04 影响版本**  
- BigAnt >= 5.5.x  
  
**0x05****POC状态**  
- 已公开  
  
****  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.bigant.cn/  
  
  
  
