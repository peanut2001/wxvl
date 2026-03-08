#  漏洞复现 | JeeWMS iconController.do 任意文件上传漏洞  
 实战安全研究   2026-03-08 01:31  
  
**免责声明**  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"><td valign="top" style="-webkit-tap-highlight-color: transparent;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><span style="color: rgb(255, 0, 0);letter-spacing: 0.544px;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);outline: 0px;visibility: visible;font-size: 14px;"><span leaf="">本文仅用于技术学习和安全研究，请勿使用本文所提供的内容及相关技术从事非法活动，由于传播和利用此文所提供的内容或工具而造成任何直接或间接的损失后果，均由使用者本人承担，所产生一切不良后果与文章作者及本账号无关。如内容有争议或侵权，请私信我们！我们会立即删除并致歉。谢谢！</span></span></td></tr></tbody></table>  
1  
  
**漏洞描述**  
  
  
  
JeeWMS 是基于Java全栈技术打造的智能仓储中枢系统，具备多形态仓储场景深度适配能力（兼容3PL第三方物流与厂内物流双模式）。JeeWMS iconController.do 接口存在文件上传漏洞，未经身份攻击者可通过该漏洞在服务器端任意执行代码，写入后门，获取服务器权限，进而控制整个 web 服务器。  
  
2  
  
**影响版本**  
  
  
  
JeeWMS  
  
3  
  
**测绘语法**  
  
  
  
fofa语法  
```
body="url:userController.do?userOrgSelect&userId=" && "loginController.do?changeDefaultOrg"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtoo0TTUCOj3a2qCNwkdsLiajltgtar8QSNLPBNxrubv2EGbDFJkGaoicibrGw2ibaVXPDZTQK8I1ELcdEIe2Gg7UbECPngGTSUkFBvI/640?wx_fmt=png&from=appmsg "")  
  
  
4  
  
**漏洞复现**  
  
  
  
上传文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtopgq9pqCL3r5onIbiceT7ic83hUNeHeQxECD0uibpr7DCazzarnbRFUjYI2ONNibTuqwicu6QQZYMrR3z6Xerd7aoOCuP66SndX2suo/640?wx_fmt=png&from=appmsg "")  
  
访问文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtorvpdmgCxv4ZwlmjPlpsSdmYDEmhrvFGCL0sZvj0icic2gkz8ZzrZBrYJeSUWa9WEicKeRVybBj88mF8RmXhd8OW10KTPXY6MOzZg/640?wx_fmt=png&from=appmsg "")  
  
  
5  
  
**检测POC**  
  
  
  
nuclei  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtorcIvgcNVeLK328WaMtwRIiaQG5OFPWxd169putKefxXYFPt1vPNPBOPVx8ibZRkNl0v3ibfG1pkFHbjlNyCECRCqHTBQOUbic1BmY/640?wx_fmt=png&from=appmsg "")  
  
afrog  
  
![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtop5jeXmL7epWxtJoFqphHgE0P2ypxnvBNsEqNhrSosJT6p9fsCC4xqP76khUR25iboZ8640eQzP7ichCaXZvPuNOygerAsJ5kX7U/640?wx_fmt=png&from=appmsg "")  
  
  
6  
  
**漏洞修复**  
  
  
1、建议联系厂商打补丁或升级版本。  
  
2、增加Web应用防火墙防护。  
  
3、关闭互联网暴露面或接口设置访问权限。  
  
7  
  
**内部圈子**  
  
  
**现在已更新POC数量 2000+（中危以上）**  
  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yIciaKAicYtooL3oOAfnj1KG92gciaoiaeqwdFicCOu4pMnj70Y1vF4wEGUYpZchnjDueyEJOBHsibVJNATO134wHJKNwlDGD2jOMqlM9xEPiczh94/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
