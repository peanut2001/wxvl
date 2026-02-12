#  漏洞复现 | 深信服运维安全管理系统 getHis 远程代码执行漏洞  
 实战安全研究   2026-02-12 01:00  
  
**免责声明**  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"><td valign="top" style="-webkit-tap-highlight-color: transparent;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><span style="color: rgb(255, 0, 0);letter-spacing: 0.544px;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);outline: 0px;visibility: visible;font-size: 14px;"><span leaf="">本文仅用于技术学习和安全研究，请勿使用本文所提供的内容及相关技术从事非法活动，由于传播和利用此文所提供的内容或工具而造成任何直接或间接的损失后果，均由使用者本人承担，所产生一切不良后果与文章作者及本账号无关。如内容有争议或侵权，请私信我们！我们会立即删除并致歉。谢谢！</span></span></td></tr></tbody></table>  
1  
  
**漏洞描述**  
  
  
  
深信服运维安全管理系统 getHis 远程代码执行漏洞，未经身份攻击者可通过该漏洞在服务器端任意执行代码，写入后门，获取服务器权限，进而控制整个 web 服务器。  
  
2  
  
**影响版本**  
  
  
  
深信服运维安全管理系统  
  
3  
  
**fofa语法**  
  
  
  
fofa语法  
```
body="/fort/login" || header="FORTSESSIONID"
```  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0jh7ibfMcx8rBxdSicicjXy6dBmxxgw2LxK6FNvV8T8DjVmGRwUzREfROXmcdsjvu7RlibDlavJicHnow/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
  
4  
  
**漏洞复现**  
  
  
  
写入文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtorcy05c4w634NWOxPo7t3w6DfP03ibz3SPYQGdDjfPl7eBH8oEe0LAUXdeP0UgFaT193cdCsjs8HC6yXhnMJgia2ayrN03MiaX68I/640?wx_fmt=png&from=appmsg "")  
  
访问文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtoofofuZIwGxP3SBISY8BGzZIrZzlzb4jKrm4YdMGvdSwG5BmbicITyZ01o0laCRHX1bCjguK8mIub2ytptlv1Yr9h2fRzhypMDk/640?wx_fmt=png&from=appmsg "")  
  
  
5  
  
**检测POC**  
  
  
  
nuclei  
  
![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtop7NUuKxiaxVkxbf3wa7TG9J04CWEyR0icTiaYkj7bWyEfjkoINzZJicvR8NjCKUibdib1YhJkrI6ibaFQJHuOonTad3xWK6V9tF5yuzA/640?wx_fmt=png&from=appmsg "")  
  
afrog  
  
![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtorkIkIibdYCXIobQd0lA55t4JXM7w54VxNSUDGQLT8cSdwXflhGCN0ZlTLeEBg1CTcbupRqkb1sB3fHywaHX4Dicc9icTh137Xur0/640?wx_fmt=png&from=appmsg "")  
  
  
6  
  
**漏洞修复**  
  
  
1、建议联系厂商打补丁或升级版本。  
  
2、增加Web应用防火墙防护。  
  
3、关闭互联网暴露面或接口设置访问权限。  
  
7  
  
**内部圈子**  
  
  
**现在已更新POC数量 1900+（中危以上）**  
  
  
🔥 **1day/Nday 漏洞实战圈上线**  
 🔥  
  
还在到处找公开漏洞 POC？  
  
这里专注整合全网1day/Nday漏洞POC和复现，一站式解决你的痛点！  
  
🔍   
圈子福利  
  
✅ 整合全网 1day/Nday 漏洞POC，附带复现步骤，新手也能快速上手  
  
✅ 每周更新 10-15 个POC测试脚本，经过实测验证，到手就能用  
  
✅ 完美适配 Nuclei/Afrog 扫描工具，脚本无需额外修改，即拿即用  
  
✅ 重磅福利：免登录免费 FOFA 查询，无需账号也能高效资产测绘  
  
✅ 专属权益：提供指纹识别库，指纹库持续更新  
  
💡   
适合对象  
  
渗透测试🔹攻防演练🔹安全运维🔹企业自查  
🔹SRC漏洞挖掘  
  
⚠️   
重要提醒  
  
仅限授权范围内的合法安全测试，严禁用于未授权攻击行为！  
  
本服务为虚拟资源服务，一经购买概不退款，请按需谨慎购买！  
  
现在加入圈子价格是59.9元（  
交个朋友啦  
），后面将调整涨价啦。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yIciaKAicYtorKrs1ictBAia3TWKqziaYwAPtvKM8VwcDPGickCjIq12MKEqia1h3lKyribDzicPXa0zR4QZJUbCMicLNDknsT80mtwW5AnTHaV7jf1Y8/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
