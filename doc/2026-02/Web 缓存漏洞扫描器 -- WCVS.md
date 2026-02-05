#  Web 缓存漏洞扫描器 -- WCVS  
原创 wolfse
                    wolfse  风铃Sec   2026-02-05 10:18  
  
声明：仅用于授权测试，用户滥用造成的一切后果和作者无关 请遵守法律法规！【无需回复关键字，文中第二部分0x02获取工具】  
  
**0x01 工具简介**  
  
Web 缓存漏洞扫描器（WCVS）是一款快速且多功能的 CLI 扫描工具，用于  
防范网页缓存中毒  
和网络缓存欺骗，该扫描器支持多种网页缓存中毒和欺骗技术，包含爬虫以识别更多需要测试的网址，并可适应特定网页缓存以实现更高效的测试。它高度可定制，可以轻松集成到现有的 CI/CD 流水线中。WCVS支持10种网页缓存中毒技术：  
- 无钥匙头部中毒  
  
- 无键参数中毒  
  
-  参数隐形  
  
- Fat GET   
  
- HTTP 响应拆分  
  
- HTTP 请求走私  
  
- HTTP 超大头部（HHO）  
  
- HTTP 元字符（HMC）  
  
- HTTP 方法覆盖（HMO）  
  
- 参数污染  
  
支持多种网页缓存欺骗技术：  
- 路径参数欺骗  
  
- 路径遍历  
  
- 附加特殊字符（包括编码和未编码）  
  
**0x02 工具获取**  
  
夸克「WebCacheVulnerabilityScanner」  
  
链接：https://pan.quark.cn/s/dbf620171fe4  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0Hm7ibaoLiafuq1RnGugO0brgia1n6dv1zkP1n3PzvcKuDVwSNtG8vQaSxBlB7MrrNJWGVuUGibicSfQnog/640?wx_fmt=png&from=appmsg "")  
  
**0x03 工具使用**  
###### WCVS唯一需要强制提供的的参数是 -u/--url，用于提供目标 URL，并应检测网页缓存中毒或欺骗。  
  
WCVS唯一需要强制提供的的参数是 -u/--url  
，用于提供目标 URL，并应检测网页缓存中毒或欺骗。  
```
wcvs -u 127.0.0.1wcvs -u http://127.0.0.1wcvs -u https://example.comwcvs -u file:path/to/url_list     #指定保存有要扫描的多个url的文件wcvs -u https://example.com -hw "file:/home/user/Documents/wordlist-header.txt"wcvs -u https://example.com -pw "file:/home/user/Documents/wordlist-parameter.txt"wcvs -u https://example.com -hw "file:/home/user/Documents/wordlist-header.txt" -pw "file:/home/user/Documents/wordlist-parameter.txt"
```  
  
--headerwordlist/-hw  
：一个带头部名的词表  
  
--parameterwordlist/-pw  
：一个带参数名的词表  
  
--generatereport/-gr  
 标志，每次扫描 URL 后都会生成并更新json报告  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0Hm7ibaoLiafuq1RnGugO0brgiafI9dpJ2uSC5hFAMYzgqtQ1uWaPRXZ3uib42HW7gWuaobNzkvxXXzDicA/640?wx_fmt=png&from=appmsg "")  
  
0x04 每日资源分享【综合漏洞自检工具-持续更新  
】  
  
夸克网盘「综合漏洞自检测工具」  
  
  
链接：  
https://pan.quark.cn/s/302256a9ecf6  
  
新增：next.js CVE-2025-55182 浏览器扩展 + 漏洞利用脚本  
  
新增：next.js CVE-2025-55182  
（  
WAF绕过工具  
）  
  
新增：  
MongoDB Bleed -  
CVE-2025-14847  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HnvemUvKPcNicmrhKC7857NtMuGru0ibEtMiaUs6lEkf6aibVdZnrZuPmKn1MApBfHcocujPYl9aiafvlw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=6 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HnvemUvKPcNicmrhKC7857NtRZRKKPlXaichMVYK0YYcKTH2gxrQ01mURiarrrctkQChx4yIMqy8TB3Q/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=7 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HnvemUvKPcNicmrhKC7857NtQaialPju2RecAS2Kc0vjiaMEQE4IxaaTl4Y4mNpeDq4Uib43HWPJSlwicQ/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=8 "")  
  
  
