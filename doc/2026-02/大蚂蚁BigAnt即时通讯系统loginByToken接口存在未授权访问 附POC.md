#  大蚂蚁BigAnt即时通讯系统loginByToken接口存在未授权访问 附POC  
2026-2-10更新
                    2026-2-10更新  南风漏洞复现文库   2026-02-10 15:31  
  
   
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. 大蚂蚁BigAnt即时通讯系统简介  
  
微信公众号搜索：南风漏洞复现文库  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
大蚂蚁BigAnt即时通讯系统  
## 2.漏洞描述  
  
大蚂蚁BigAnt即时通讯系统loginByToken接口存在未授权访问  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
大蚂蚁BigAnt即时通讯系统  
![大蚂蚁BigAnt即时通讯系统loginByToken接口存在未授权访问](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6xcYH7XmselKxTEqMBgwc0x0zUG9NFDUPNUPkU0NDhEO0Vf4IBv3ibtMYCJnwMiacKMmZU3AyD8IhpMJL0HnrlqAwdee6hrcF5iaI/640?wx_fmt=png&from=appmsg "null")  
  
大蚂蚁BigAnt即时通讯系统loginByToken接口存在未授权访问  
## 4.fofa查询语句  
  
(body="/Public/static/admin/admin_common.js" && body="/Public/lang/zh-cn.js.js")||title="即时通讯 系统登录"&& body="/Public/static/ukey/Syunew3.js"  
## 5.漏洞复现  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wlAj7lfdns4kKLicZWKY2S49Q2RYgmPpiaDVKdepsEFxwibib2qI6U0956E22KhibFiaZJhbvaPiat80F7NFtQqtHK3jALwyVWIic6aBM/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b9KQYsB8q6yxASEffoogHicZTA2d4RdHQLvRicQgRVNoHoicXFZ6KJvxql9KJD5uPcmpCgIZ3b5BrZFQGecia0nlf3PahHaqa7Q9Alv6h6rQabo/640?wx_fmt=png&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
2: 免登录，免费fofa查询。  
3: 更新其他实用网络安全工具项目。  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xEsEkhdb7aPOlLW4xYIMVn4MgoScddZMVfYOcviaIc2yX2VzX59UJFmC7DrVc1xIIxBK30R7icib67vHcJeu7sAhKZAiaUsMa5jOA/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wVbbpgkVOhwTeFmIbz3JtEz8P2SXLGxkTQ71MGBzpVyicbE8ib5hXhYZmlOYe4GUXYOehdHbsb5EoSzn2F0fQA5tS9JOJicf7l14/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yC1MqBVtdJE2kZrhvYQfWSOPBB7fzgrsJ8RKMr4BBH2xHDzcqoY5Xf6LSwXfVBgzAMTLyTszDgs3tVeJt5GrA7K9fnBQGjFWQ/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xdP6lKwImrS4jRodnSH1kU1PYRIGvLicRs3QGGmM0aZONAuOk96ztib9rUsswrbbWEbrsskh6tDndzfZVk6IQJLvZRNkVbkHU14/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wdRpTib5dLoHNHO8HcEib5dX16VpW8hZchiczbbKUAJIBqn1qFOYc17e93urib3ffRr9ofjZ13JAWpBLlLFHDoq5yeAt8iaqhict7rE/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
  
