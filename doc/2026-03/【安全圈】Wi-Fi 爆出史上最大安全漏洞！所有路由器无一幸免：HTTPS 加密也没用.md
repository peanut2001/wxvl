#  【安全圈】Wi-Fi 爆出史上最大安全漏洞！所有路由器无一幸免：HTTPS 加密也没用  
 安全圈   2026-03-06 11:02  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
漏洞  
  
  
据报道，安全研究人员近日披露一种名为 AirSnitch 的新型攻击手法，该漏洞存在于所有 Wi-Fi 路由器中，可完全绕过当前 Wi-Fi 加密标准，即便连接 HTTPS 加密网站，黑客仍能截取所有经路由器传送的流量。  
  
与 2017 年 WPA2 被破解后升级为 WPA3 的情况不同，AirSnitch 并非破解现有加密，而是利用了网络层（第 1 层与第 2 层）的核心特性，通过修改第 1 层映射实施攻击。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGwicNhxAn0OpzW2vvJoW4IibwcoiayaGjKjBLgxse5ZxpspFbhyh0B5dbz75GySJ3FRO2b45T05NqnKJ9na6piahppdIpKFPXvibsc/640?wx_fmt=jpeg&from=appmsg "")  
  
这种映射本应负责将网络连接端口与受害者的 MAC 地址安全关联，但攻击者利用该漏洞，可以在数据到达预期接收者之前进行拦截、查看甚至修改。  
  
这种完全双向的中间人攻击（MitM）意味着攻击者可以神不知鬼不觉地切入用户的通信链条中，掌控所有经由路由器传输的数据流量。  
  
而且 AirSnitch 攻击实施门槛极低，黑客仅需获取 Wi-Fi 密码并连接网络，无论位于相同 SSID、不同 SSID，或同一接入点的不同网段，均可拦截所有链路层流量。  
  
公共 Wi-Fi 环境下风险更是呈指数级上升，黑客甚至无需任何密码，连接即可发动攻击，未加密数据可被轻易查看篡改，并窃取身份验证 cookie、密码、支付信息等敏感资料。  
  
即便采用 HTTPS 加密，攻击者仍能拦截域名查询流量、查看外部 IP 地址并关联特定 URL，通过破坏 DNS 缓存表最终骗取机密数据。  
  
根据美国加州大学的研究报告，AirSnitch 攻击导致全球 Wi-Fi 用户的客户端隔离机制几乎在一夜之间被彻底瓦解，且目前尚无有效的技术补救措施。  
  
好消息是，在私人 Wi-Fi 环境下，攻击者仍需首先知道密码才能发动攻击，因此对于普通用户，首要防御是确保私人 Wi-Fi 密码不外泄；公共 Wi-Fi 密码通常是公开的，这种场景下使用代理可能较为安全。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFm62M8PFaH0Ue0eabDuqIiakcPWvVFCDIMIm9wzH85gIdGRH0t8LRqhhicFkl5tv0gDVoLVxyPSHO6oGTl2H96eibJhbJJbd0Aq8/640?wx_fmt=jpeg&from=appmsg "")  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】官方提醒：警惕发票陷阱！境外黑客借邮箱植入木马](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074304&idx=1&sn=2c7824b0a8dcd55a514e9b40c95632ea&scene=21#wechat_redirect)  
  
  
  
[【安全圈】Telegram日益成为访问权限、恶意软件和窃取日志的交易平台](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074304&idx=2&sn=765538d7af216b7a02dff36f502b43f0&scene=21#wechat_redirect)  
  
  
  
[【安全圈】汽车胎压传感器或成隐私泄露隐患，可悄无声息追踪车主行程](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074304&idx=3&sn=0c569d6fc257cd7be213ab562bb3620c&scene=21#wechat_redirect)  
  
  
  
[【安全圈】思科修复最高危 Secure FMC 漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074304&idx=4&sn=c541beb5d36c901fe3af1636fafc01a0&scene=21#wechat_redirect)  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png "")  
  
**安全圈**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif "")  
  
  
←扫码关注我们  
  
**网罗圈内热点 专注网络安全**  
  
**实时资讯一手掌握！**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
**好看你就分享 有用就点个赞**  
  
**支持「****安全圈」就点个三连吧！**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif "")  
  
  
