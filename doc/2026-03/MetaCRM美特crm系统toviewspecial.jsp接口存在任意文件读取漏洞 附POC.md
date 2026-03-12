#  MetaCRM美特crm系统toviewspecial.jsp接口存在任意文件读取漏洞 附POC  
2026-3-12更新
                    2026-3-12更新  南风漏洞复现文库   2026-03-12 15:10  
  
   
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
## 1. MetaCRM美特crm系简介  
  
微信公众号搜索：南风漏洞复现文库  
该文章 南风漏洞复现文库 公众号首发  
  
本人只有 南风漏洞复现文库 和 南风网络安全  
 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。  
  
MetaCRM美特crm  
## 2.漏洞描述  
  
MetaCRM美特crm系统toviewspecial.jsp接口存在任意文件读取漏洞  
  
CVE编号:  
  
CNNVD编号:  
  
CNVD编号:  
## 3.影响版本  
  
MetaCRM美特crm  
![MetaCRM美特crm系统toviewspecial.jsp接口存在任意文件读取漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6yS4jvvswcvKgZk73KkMHL6fC2sWOhzjQ3CTaicdzibPUpFfYDUKnlDrZDJh3z3aEyKMTfzUdoNUIPvuS2M6SqfnJgm30ne8TyQY/640?wx_fmt=png&from=appmsg "null")  
  
MetaCRM美特crm系统toviewspecial.jsp接口存在任意文件读取漏洞  
## 4.fofa查询语句  
  
body="/common/scripts/basic.js" && body="  
www.metacrm.com.cn  
"  
## 5.漏洞复现  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zqkfoddaF75KVnVzhnDh0Nbk2fpvqmzdpbvGDl9NY3uCW6iafqPwUgIEImLENHGEBBEoZ6WxDHjayOWXqQYP7txqGqXOHicFM90/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 6.POC&EXP  
  
本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全  
1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。  
2: 免登录，免费fofa查询。  
3: 更新其他实用网络安全工具项目。  
4: 免费指纹识别，持续更新指纹库。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6z1ZK5KaEZ5GzJCoEwg0YBMKQKRia9G0icT29gsCzcB1nA0ictyMyCLiaGo5Kk3X7z4dznUtfnb0qOumHBoI0jdUl20DWQ6XTzVc6w/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6yiaJRn2OGEkHktAd5Fc3Vn3X7GnuAeX1MeAAn3MOmnNmyPyUd65S29QK9lBiapoWfaxt6PEn7rXr3kXqDicficoVl8mSOC0icXztwY/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6y6DZnruXyliatibLTZOahG4f8s4RHExiam49JD7pMjErZdgsUswYyJwrvjmNoboUNRicB8MfYp7DialHFdiaTbTW5NwEmBHvxuf7dXw/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yX7YZvN8wlozGpax6x8SlsIto0ib3K0AGztD6On6kZpHwFNuNChZcUe1PXDCNytHvS23QE5YEjRW23sW2sIETibiaiaic4XR1V0B00/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6ydOkib1leaCcalsdKamq4erD8GXuONw34nf1VnqC09fwfoK80nVetLHEkVcSIOiciafyATgsTmNd17icku4icfVapOdwN78fHfetEE/640?wx_fmt=jpeg&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6yWickXbNSvvSmibMwudWBfv1xmnNHvibCYHVCwhkbukFdHJt1g8rtMXmlicIxUjF4iabMYqb4DRIwO6vS4FbYrBFbQkTqxNDP5Zm0s/640?wx_fmt=jpeg&from=appmsg "null")  
  
## 7.整改意见  
  
打补丁  
## 8.往期回顾  
  
  
   
  
  
[天地伟业Easy7 loadAllUserBeans接口存在敏感信息泄露 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490111&idx=1&sn=2be97564465358c3b7b6a05fc38c16b8&scene=21#wechat_redirect)  
[东胜物流软件GetData接口存在SQL注⼊漏洞 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490084&idx=1&sn=d1ed303c0b88a477a1e972200c56f301&scene=21#wechat_redirect)  
  
  
