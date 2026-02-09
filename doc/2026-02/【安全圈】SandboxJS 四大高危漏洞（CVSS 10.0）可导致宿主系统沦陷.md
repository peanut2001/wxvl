#  【安全圈】SandboxJS 四大高危漏洞（CVSS 10.0）可导致宿主系统沦陷  
 安全圈   2026-02-09 11:02  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
漏洞  
  
  
![banner](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyF4KNSVgM8f2nEtMHyN1ZbTeFzo3bgWSYITicLzjXll49Q1GQZ3CGm4FoJ2KIXhrJPOiaqzfZEenHWbJicUK5ZQicnuyL2nMOR09f8/640?wx_fmt=jpeg&from=appmsg "")  
  
专为隔离和保护 JavaScript 执行而设计的 SandboxJS 库近期曝出四个高危漏洞（CVE-2026-25520、CVE-2026-25586、CVE-2026-25587 和 CVE-2026-25641），这些漏洞均获得 CVSS 10.0 的最高风险评分，攻击者可借此完全突破沙箱限制，在宿主系统上执行任意代码。  
  
对于依赖 SandboxJS 安全运行非受信代码的开发者而言，这些发现无异于"红色警报"。该库的安全承诺已被多种绕过核心防护的攻击途径彻底瓦解。  
## 漏洞技术细节  
  
**函数返回值处理缺陷（CVE-2026-25520）**  
  
该漏洞利用库函数处理返回值时的逻辑缺陷。正常情况下，沙箱会对对象进行封装以防止其与外部环境交互，但此漏洞允许攻击者通过方法调用链访问宿主的 Function 构造函数。安全公告指出："函数返回值未被正确封装"，攻击者可通过 Object.values 或 Object.entries 获取包含宿主构造函数的数组，从而获得引擎控制权。  
  
**Map对象安全机制失效（CVE-2026-25587）**  
  
该漏洞针对通常被视为安全的 Map 对象，问题源于库的 let 实现存在缺陷，允许攻击者覆写 Map.prototype.has 方法。公告强调："由于 Map 被列入 SAFE_PROTOYPES，其原型可通过 Map.prototype 获取"，通过覆写这一核心方法，攻击者可操纵沙箱内部逻辑实现逃逸。  
  
**宿主原型污染漏洞（CVE-2026-25586）**  
  
这是该漏洞组中最危险的漏洞，利用 SandboxJS 使用 hasOwnProperty 进行属性检查的机制。攻击者可对沙箱化对象的 hasOwnProperty 进行"影子替换"或覆写。公告警告："当返回值为真时，白名单检查将被跳过"，这一简单技巧即可绕过对 **proto**  
 等敏感原型的访问限制，使攻击者能自由污染宿主环境。  
  
**检查时与使用时差漏洞（CVE-2026-25641）**  
  
这是典型的"检查时与使用时差"（TOCTOU）漏洞，源于库在验证属性键与实际使用之间存在时间差。公告解释："攻击者可传入恶意对象，这些对象在使用时会强制转换为不同的字符串值"，使得安全检查时看似无害的键在实际访问时转变为恶意载荷。  
  
  
   END    
  
  
阅读推荐  
  
  
[【安全圈】突发！BT面板Nginx服务器遭批量攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074052&idx=1&sn=ea5ed1b06b333909c33ceead3b19b8a1&scene=21#wechat_redirect)  
  
  
  
[【安全圈】紧急预警！n8n 曝严重漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074052&idx=2&sn=8e912398d2bf5ec8260e938a07b552b0&scene=21#wechat_redirect)  
  
  
  
[【安全圈】突发！韩国Bithumb交易所误空投2000比特币](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074052&idx=3&sn=0a26f104b944aac1d7e5206201352bcf&scene=21#wechat_redirect)  
  
  
  
[【安全圈】阿里30亿红包分发首日，千问App“崩了”](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074041&idx=1&sn=ead70ffd5a7c58f34ac096e34ec29ba1&scene=21#wechat_redirect)  
  
  
  
[【安全圈】微软Azure突发10小时全球宕机！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074041&idx=2&sn=e9b040f68282d54490efb0d48044e63e&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
