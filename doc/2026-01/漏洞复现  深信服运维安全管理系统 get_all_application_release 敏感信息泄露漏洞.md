#  漏洞复现 | 深信服运维安全管理系统 get_all_application_release 敏感信息泄露漏洞  
 实战安全研究   2026-01-23 01:03  
  
**免责声明**  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"><td valign="top" style="-webkit-tap-highlight-color: transparent;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><span style="color: rgb(255, 0, 0);letter-spacing: 0.544px;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);outline: 0px;visibility: visible;font-size: 14px;"><span leaf="">本文仅用于技术学习和安全研究，请勿使用本文所提供的内容及相关技术从事非法活动，由于传播和利用此文所提供的内容或工具而造成任何直接或间接的损失后果，均由使用者本人承担，所产生一切不良后果与文章作者及本账号无关。如内容有争议或侵权，请私信我们！我们会立即删除并致歉。谢谢！</span></span></td></tr></tbody></table>  
1  
  
**漏洞描述**  
  
  
  
深信服运维安全管理系统 get_all_application_release敏感信息泄露接口在未进行充分身份验证或权限校验的情况下，返回了包含敏感信息的响应，导致攻击者可能通过该接口获取到系统内部的敏感数据。  
  
2  
  
**影响版本**  
  
  
  
深信服运维安全管理系统  
  
3  
  
**fofa语法**  
  
  
  
fofa语法  
```
body="/fort/login" || header="FORTSESSIONID"
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0jh7ibfMcx8rBxdSicicjXy6drxyuJbia7ajzSBQFR8l8GYpRbliaFEAmeoqiaaMBiaobV8Uqdk0wEPSv1g/640?wx_fmt=png&from=appmsg "")  
  
  
4  
  
**漏洞复现**  
  
  
  
获取账号密码信息  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0jh7ibfMcx8rBxdSicicjXy6dQ5djk5ZGDbovOAZKLN1SiaQOnBxmMMVshYMs4Bkwk4U5GsJPTEU4d7w/640?wx_fmt=png&from=appmsg "")  
  
  
5  
  
**检测POC**  
  
  
  
nuclei  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0jh7ibfMcx8rBxdSicicjXy6dFrqnDgRxDQUZAyBicp1eEEo1MrpxfDL6vuz6hdfCWhQOkFFuWZqlNkQ/640?wx_fmt=png&from=appmsg "")  
  
afrog  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF0jh7ibfMcx8rBxdSicicjXy6dgfAwlnxiaOmvqWjpOglEeK4neXjjpT5iaF2QWVNFeAxEjbENHdibET0icA/640?wx_fmt=png&from=appmsg "")  
  
  
6  
  
**漏洞修复**  
  
  
1、建议联系厂商打补丁或升级版本。  
  
2、增加Web应用防火墙防护。  
  
3、关闭互联网暴露面或接口设置访问权限。  
  
7  
  
**内部圈子**  
  
  
**现在已更新POC数量 1700+（中危以上）**  
  
  
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
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF0WahagBSLib4DOPBsv4ic1O9D9nzrANOgwluaGYaL3m85kOUOUzkvMKfFX9144deoHicd5OOGoU825g/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
