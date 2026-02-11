#  xss_scanner_mix：一款自动化深度XSS漏洞扫描工具  
原创 网安武器库
                    网安武器库  网安武器库   2026-02-11 05:31  
  
**更多干货  点击蓝字 关注我们**  
  
  
  
**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**  
  
**往期回顾**  
  
  
  
  
  
  
·  
[Metasploit Pro：可视化的metasploit渗透测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486276&idx=1&sn=44e00b0ee13437083417bd8c16f15f0c&scene=21#wechat_redirect)  
  
  
  
  
  
  
·  
[Coda：实现Windows/Linux入侵痕迹抹除](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486251&idx=1&sn=c2c9dc8f482b43d9c5c0384d37eeb8a6&scene=21#wechat_redirect)  
  
  
  
  
  
  
·  
[OSV-Scanner：一款专门于发现开源软件漏洞的扫描器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486240&idx=1&sn=69241fc574c182a305e1c17747377ae6&scene=21#wechat_redirect)  
  
  
  
  
  
  
·  
[LingOps（灵控）：AWD/AWDP 竞赛自动化平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486227&idx=1&sn=c7183a4926281db23003d3e02010fd8f&scene=21#wechat_redirect)  
  
  
  
  
  
  
·  
[融合AI引擎的日志应急响应溯源工具SSLogs--详细配置教程与使用方法](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486211&idx=1&sn=b6893a457752881cbef64eb8f685e0fb&scene=21#wechat_redirect)  
  
  
  
  
  
  
·  
[AWD-H1M：AWD攻防竞赛自动化工具箱](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486193&idx=1&sn=0d299367f73c1a711d810af55196a275&scene=21#wechat_redirect)  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**介绍**  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJAF0czzKpOFTrfJSrRSN4fEW1zRDicakXzmYiaibU8UMz2krs4JUaJsn9Qj0Gn164esBfTsB8Zf6p9LBH0EdhzpYuyz8nAorTPV4/640?wx_fmt=png&from=appmsg "")  
  
      
深度XSS漏洞扫描器是一款专业级、智能化的跨站脚本（XSS）漏洞检测平台。它不仅仅是一个简单的漏洞扫描工具，而是一个完整的Web应用安全评估系统，能够模拟真实黑客攻击手法，深入挖掘传统工具难以发现的反射型、存储型、DOM型XSS漏洞。  
  
     
 该工具  
专注于检测XSS（跨站脚本）漏洞，同时也能够发现其他类型的Web安全漏洞。该工具支持多种扫描模式、不同级别的有效载荷和详细的漏洞报告。  
  
    核心价值定位：  
  
1.深度挖掘：超越表面检测，深入应用逻辑层  
  
2.智能绕过：自动识别并绕过WAF防护机制  
  
3.持续监控：7×24小时漏洞监控与预警  
  
4.企业级支持：支持大规模分布式扫描  
  
    对于XSS  
（反射型、存储型、DOM型）  
 CSRF  
（跨站请求伪造）  
 SQL注入 LFI  
（本地文件包含）  
 RFI  
（本地文件包含）  
 SSRF  
（服务器端请求伪造）  
 XXE  
（XML外部实体注入）  
多种漏洞都可检测。  
  
    具有全面的扫描能力：  
  
1.网站爬虫功能，自动发现可测试的URL  
  
2.表单和参数自动检测  
  
3.支持DOM分析  
  
4.支持不同测试级别（快速、标准、深度）  
  
5.支持多线程扫描  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**安装介绍**  
  
  
  
      
访问下述网址，即为StegoScan工具的源文件地址：  
```
https://github.com/achenc1013/xss_scanner_mix
```  
  
      
在目标文件夹中打开终端后，在网址中复制克隆地址：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJ29dXASdkur2UUE9nvjVibMTtPVb9mp8Z0Nr2Rqz1x9uja2JZ5iaibw8YQ78eGFdzuS7M0j0UcichdP1xY8PSFnNhlB51xWPHeLoI/640?wx_fmt=png&from=appmsg "")  
  
      
在终端中输入：  
```
git clone https://github.com/achenc1013/XSS_Scanner.git
cd XSS_Scanner
```  
  
    即可克隆项目并进入到项目文件夹中。  
  
    检测克隆完成：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIibhUGDaKIuUxuncysPEJhUUgrcnzgH8VJB1SN2iciaxfPgZwia6NjdCA2Ae38MKFcr1pMVqJzVP8h768Mgic4sPvgicTbBE6iaoicNiaA/640?wx_fmt=png&from=appmsg "")  
  
    安装依赖：  
```
pip install -r requirements.txt
```  
  
      
安装ChromeDriver（如需浏览器测试）：  
```
pip install webdriver-manager
```  
  
    然后就可以使用了。  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**功能介绍**  
  
  
  
    基本用法：  
```
python xss_scanner.py -u https://example.com
```  
  
**扫描单个URL**  
：  
```
python xss_scanner.py -u https://example.com
```  
  
     
 **扫描多个URL**  
：  
```
python xss_scanner.py -f targets.txt
```  
  
    **深度扫描**  
：  
```
python xss_scanner.py -u https://example.com --scan-level 
```  
  
    **只****扫描XSS漏洞**  
：  
```
python xss_scanner.py -u https://example.com --scan-type xss
```  
  
      
使用浏览器进行DOM XSS检测：  
```
python xss_scanner.py -u https://example.com --browser
```  
  
     
 **利用发现的漏洞**  
：  
```
python xss_scanner.py -u https://example.com --exploit
```  
  
   
     
生成HTML报告：  
```
python xss_scanner.py -u https://example.com -o report.html --format html
```  
  
      
使用代理：  
```
python xss_scanner.py -u https://example.com --proxy http://127.0.0.1:8080
```  
  
      
  
    XSS漏洞  
案例，  
扫描器能够检测以下XSS攻击场景  
：  
```
1.网页留言板获取cookie：检测表单提交中的XSS漏洞，可能导致cookie泄露
2.CMS管理后台伪造钓鱼网站：检测URL参数中的XSS漏洞，可能用于伪造管理界面
3.图片处XSS攻击：检测图片参数和属性中的XSS漏洞
4.SVG-XSS：检测SVG文件中的XML注入和XSS漏洞
5.PDF-XSS：检测PDF参数中的XSS漏洞
6.浏览器翻译-XSS：检测浏览器翻译功能中的XSS漏洞
7.Flash-XSS：检测Flash参数中的XSS漏洞
8.XSS配合MSf钓鱼：检测可能用于钓鱼的XSS漏洞
9.XSS漏洞配合CSRF漏洞：检测可能与CSRF组合的XSS漏洞
10.XSS漏洞配合越权漏洞：检测可能导致权限提升的XSS漏洞
11.前端框架XSS：检测React、Vue、Angular等前端框架中的XSS漏洞
12.模板注入XSS：检测模板引擎中的XSS漏洞，包括Jinja2、Twig、Handlebars等
13.JSON-XSS：检测JSON数据中的XSS漏洞，包括JSON.parse和eval使用不当
14.WebSocket-XSS：检测WebSocket通信中的XSS漏洞
15.PostMessage-XSS：检测跨域消息传递中的XSS漏洞
```  
  
      
  
      
XSS检测技术，  
扫描器使用多种技术来检测XSS漏洞  
：  
```
1.反射型XSS检测：检测服务器响应中直接反射的用户输入
2.DOM型XSS检测：使用真实浏览器分析DOM操作和事件处理
3.存储型XSS检测：测试在一个页面提交的数据是否在另一个页面中触发XSS
4.上下文感知检测：根据XSS注入点的上下文选择合适的有效载荷
5.WAF绕过技术：使用多种编码和混淆技术绕过WAF防护
```  
  
  
    我们使用以上内容进行模拟。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLb6tYSSxVUyQV1ElbxhqwZYIytHGaFaF4CPZx8s53MHr4nh8qncDgQzAdpSAV2ib87WP9cxBmn8D50Ol4CgS4Fmmajzia2cibaXs/640?wx_fmt=png&from=appmsg "")  
  
    可以看到，对指定网站进行了漏洞扫描。因为是特殊网站没有检测到漏洞。  
  
    我们可以使用一个存在漏洞的靶场进行检测  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJcRRiaBRr5AP7cveQC7NfosZJ9jnVg08VX0wLCEJ82iax4msTs5gibKnh8Hiaeg5lMo0EzgeNNfuJo1DqEu3rgGe7SA4WANvFMjPA/640?wx_fmt=png&from=appmsg "")  
  
      
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
