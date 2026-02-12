#  漏洞预警 | 天地伟业Easy7综合管理平台文件读取漏洞  
浅安
                    浅安  浅安安全   2026-02-12 00:00  
  
**0x00 漏洞编号**  
- # 暂无  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
天地伟业Easy7综合管理平台采用分布式架构，融合模数混合切换显示、用户权限控制、数据存储点播等功能，具备智能检索、视频诊断等特色应用，能为各行业提供高效可靠的安防综合管理方案。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SWaLw2vQgZuyUrIFYzJaw7Wq8JT3p6gtDdlQkjnCfQTfZgUJ0NFdz1icCuk7DcAviaMZGvrmxkTGVhQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**漏洞类型：**  
任意文件读取  
  
**影响：**  
获取敏感信息  
  
  
  
  
**简述：**  
天地伟业Easy7的/Easy7/rest/gis/exportGisObj和/Easy7/rest/gisCore/exportGisObj接口存在任意文件读取漏洞，攻击者通过构造恶意路径参数可读取服务器上的任意文件，从而导致敏感信息泄露。  
  
**0x04 影响版本**  
- 天地伟业Easy7综合管理平台  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.tiandy.com/  
  
  
  
