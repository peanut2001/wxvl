#  漏洞预警 | Advantech SQL注入漏洞  
浅安
                    浅安  浅安安全   2026-02-03 00:02  
  
**0x00 漏洞编号**  
- # CVE-2025-52694  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
Advantech是中国研华公司的一个智能电动客车管理系统  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SUKVqQTX1FUsjvfXSibEZNOC1bXBibHLHmw8fH2rwYsZ4lAW1tuzKrbMyQ2zTVT0CbpR7YjE27ria2mA/640?wx_fmt=png&from=appmsg "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2025-52694**  
  
**漏洞类型：**  
SQL注入  
  
**影响：**  
窃取敏感信息  
  
**简述：**  
Advantech的/displays/{filename}.json?org_id=接口存在SQL注入漏洞，未经身份验证的攻击者可以通过该漏洞执行任意SQL语句，从而获取数据库敏感信息。  
  
**0x04 影响版本**  
- IoTSuite SaaSComposer prior < 3.4.15  
  
- IoTSuite Growth Linux docker prior < V2.0.2  
  
- IoTSuite Starter Linux docker prior < V2.0.2  
  
- IoT Edge Linux docker prior < V2.0.2  
  
- IoT Edge Windows prior < V2.0.2  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.advantech.com.cn/  
  
  
  
