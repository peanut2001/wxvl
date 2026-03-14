#  漏洞复现 | 用友NC OAUserAuthenticationServlet 反序列化代码执行RCE漏洞  
 实战安全研究   2026-03-14 01:01  
  
**免责声明**  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"><td valign="top" style="-webkit-tap-highlight-color: transparent;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><span style="color: rgb(255, 0, 0);letter-spacing: 0.544px;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);outline: 0px;visibility: visible;font-size: 14px;"><span leaf="">本文仅用于技术学习和安全研究，请勿使用本文所提供的内容及相关技术从事非法活动，由于传播和利用此文所提供的内容或工具而造成任何直接或间接的损失后果，均由使用者本人承担，所产生一切不良后果与文章作者及本账号无关。如内容有争议或侵权，请私信我们！我们会立即删除并致歉。谢谢！</span></span></td></tr></tbody></table>  
1  
  
**漏洞描述**  
  
  
  
用友NC的OAUserAuthenticationServlet组件存在反序列化漏洞。该Servlet在处理用户请求时，可能对接收到的序列化数据（如Java的ObjectInputStream）未进行安全检查，直接进行反序列化操作。攻击者可以构造恶意的序列化对象，其中包含可执行的代码，当OAUserAuthenticationServlet反序列化该恶意对象时，就会触发代码执行。该漏洞可能允许攻击者在服务器上执行任意代码，从而完全控制服务器，窃取敏感数据，篡改系统配置，或进行其他恶意活动，对企业的业务系统和数据安全构成严重威胁。  
  
2  
  
**影响版本**  
  
  
  
用友NC  
  
3  
  
**测绘语法**  
  
  
  
fofa语法  
```
app="用友-UFIDA-NC"
```  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtoqaxiaR6EWqFTZQCLBQygVuq823gJzI2xgeMUmmrMMI3WxdvTvge1rCqMjs6AaYEa2pPKMobcgS8nTLKxibgHe7ozpJQXrYeZg2c/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
  
4  
  
**漏洞复现**  
  
  
  
执行命令  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtopOS6YADkfrhhnvn6MnmDlFhsVhrQASqaofDtjp8LZ26rCvXvKRrudjx5LG2QbMsVh57A7DTTWb2m0JsxGPWBicJuOK4hq2buos/640?wx_fmt=png&from=appmsg "")  
  
  
5  
  
**检测POC**  
  
  
  
nuclei  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/yIciaKAicYtorn7NamcNTTJUxh2Oj7g55YtibsicWw7qOcKxicUeMNZH6vHpBcpkfFexCH7KnItwAwlRdsl2xQvXIRfXMzLO3IQ6o7nU8INLt53E/640?wx_fmt=png&from=appmsg "")  
  
afrog  
  
![](https://mmbiz.qpic.cn/mmbiz_png/yIciaKAicYtopJfmNO3M5jb8nVRv9TgicCMltoIbC3h1ewianXuB28VlDm8bY4iaeInjdWIYZYN06erG2icxOmA8qbPKVTpCx5Vk6TH1Tia3PqiceCQ/640?wx_fmt=png&from=appmsg "")  
  
  
6  
  
**漏洞修复**  
  
  
1、建议联系厂商打补丁或升级版本。  
  
2、增加Web应用防火墙防护。  
  
3、关闭互联网暴露面或接口设置访问权限。  
  
7  
  
**内部圈子**  
  
  
**现在已更新POC数量 2050+（中危以上）**  
  
  
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
  
目前圈子已满100人，价格由59.9调整为64.9元（  
交个朋友啦  
），后面将调整涨价啦。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yIciaKAicYtooYRnOUdibemlylV5BQ0cvDRgic8Kdiaxfwxab3cwPibic6tHaYGlkfYxupNCfo6DJMUQmfuMwkIDic2Iibo1MrlprqdViclvDLLBRKoWI/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
