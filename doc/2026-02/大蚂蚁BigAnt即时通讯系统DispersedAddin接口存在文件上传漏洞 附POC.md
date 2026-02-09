#  大蚂蚁BigAnt即时通讯系统DispersedAddin接口存在文件上传漏洞 附POC  
2026-2-9更新
                    2026-2-9更新  南风漏洞复现文库   2026-02-09 15:43  
  
   
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 大蚂蚁BigAnt即时通讯系统简介  
  
微信公众号搜索：南风漏洞复现文库  
  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
大蚂蚁BigAnt即时通讯系统  
## 2.漏洞描述  
  
大蚂蚁BigAnt即时通讯系统DispersedAddin接口存在文件上传漏洞  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
大蚂蚁BigAnt即时通讯系统  
  
![大蚂蚁BigAnt即时通讯系统DispersedAddin接口存在文件上传漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6zenLCQ0tuibVoWhngXWu214HfRMUDnC8ibFcvluGJQ3wcH6dWI3RCu2Cq3Q3Fkfr2gUZJaR6zT57AlnNryUicySIL71icvKiaiboUpU/640?wx_fmt=png&from=appmsg "null")  
  
大蚂蚁BigAnt即时通讯系统DispersedAddin接口存在文件上传漏洞  
## 4.fofa查询语句  
  
(body="/Public/static/admin/admin_common.js" && body="/Public/lang/zh-cn.js.js")||title="即时通讯 系统登录"&& body="/Public/static/ukey/Syunew3.js"  
## 5.漏洞复现  
  
漏洞链接：http://xx.xx.xx.xx/?m=Api&c=DispersedAddin&a=upload_file  
  
漏洞数据包：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zqzxp0LLXjueZuctd9Gl9t6oAeSBkPd0rPgAd5c5Q4BuKd1OIUfR0O2OZugwSC8my9Dv23sk4UL1yKkMQDum1TIUPQAjgzkPE/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6x2PORC02VKb1zbIRnFPjqlLjsJDs7vsqeCVuKia1JfaSgmkqTibtiafYojibbDXLl0xAeibpzYwonIpIFewfozJkNKwk6DLn7fvoKs/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
  
  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
  
  
2: 免登录，免费fofa查询。  
  
  
3: 更新其他实用网络安全工具项目。  
  
  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6ygBbq6criaCRvhzM3CuN9IS4g3mIwxYU7e3JesxtC3mjTw8xhhYSHLnSBhXhxXazoxicEELrhLOiaK0ueSNeaAFib2Gcia17g0ndsQ/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wQXSskdFTjzicnYMOicgIMpiav0YEYibL3kfrp0ib8yiab4DMibt0tDjMFCEVFC96YWPs15rACteVo6FuZ7Nqy9qvLfUOvtNw5jBia2TU/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zAYGics2tk2xUCuiaR66tr0glAFicvXR9wJoQ6F0q1OHdq9kVQn87cDonxmRfwbx3I3sVCr5zueQKsTSH6XvKeicLqvsVUgJf0oqQ/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wIwcRjpdzwulFdWBbxw2udHGxdAOBBZJCyf9ejJic6OkkRWeiaFUhhZ564vfpckHGibHaUmrQMKo8vWxk7ZlWgRvrO6t6nhic1nW0/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6yxibzslhNAy6iaqspnZovciahNjlzFwQzKXzmNlNT7yO0CwYD4WWfVF1rgQ3K8C4Wk08uK0Ft2XfMaHaOtO74B8Qm9v3YTHPrNAE/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
  
