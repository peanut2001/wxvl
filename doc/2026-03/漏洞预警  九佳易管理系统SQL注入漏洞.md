#  漏洞预警 | 九佳易管理系统SQL注入漏洞  
浅安
                    浅安  浅安安全   2026-03-04 00:01  
  
**0x00 漏洞编号**  
- # 暂无  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
九佳易管理系统是一款线上购物交互平台。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/NQlfTO30MhyZrRzo06V1GaLibicIh6ZRMwyQ1BM0kuftDIQw2eVy7Gp0MRodkXCstETtibdDCG1mT5RVprErdywrhGxrQxIibClsTJ3Issy1BtY/640?wx_fmt=png&from=appmsg "")  
  
**0x03 漏洞详情**  
###   
  
**漏洞类型：**  
SQL注入  
  
**影响：**  
获取敏感信息  
  
**简述：**  
九佳易管理系统的/HuiYuan/HuiYuanDangAn/picHY.aspx和/Service/Ajax_XT.ashx接口存在SQL注入漏洞，未经身份验证的攻击者可以通过该漏洞获取数据库敏感信息。  
  
**0x04 影响版本**  
- 东胜物流软件  
   
  
**0x05****POC状态**  
- 已公开  
  
****  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
http://www.dongshengsoft.com/  
  
  
  
