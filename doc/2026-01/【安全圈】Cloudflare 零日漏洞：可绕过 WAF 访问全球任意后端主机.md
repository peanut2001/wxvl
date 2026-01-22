#  【安全圈】Cloudflare 零日漏洞：可绕过 WAF 访问全球任意后端主机  
 安全圈   2026-01-22 11:00  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
0day漏洞  
  
  
Cloudflare 已修复其 ACME 验证逻辑中的一项漏洞，该漏洞可能允许攻击者绕过安全检查并访问受保护的源站服务器。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljPKJSHxrpuQomtHf35Q0cAUlr36h2myjoXJkZXlFg0gCRCQLYnyTd1FAbZDGhebl2oJeoDnj2Elw/640?wx_fmt=png&from=appmsg "")  
  
Cloudflare 表示，**其 ACME HTTP-01 验证流程中存在缺陷，问题出在Cloudflare 边缘节点对 /.well-known/acme-challenge/ 路径请求的处理方式上**  
。该公司称，未发现该漏洞被恶意利用的迹象。  
  
ACME 是一种用于让证书颁发机构验证域名所有权的协议。在 HTTP-01 验证方式下，CA 会访问一个包含一次性令牌的特定 URL；如果返回内容匹配，即可签发证书。按设计，该过程只应允许访问这一精确路径，而不能访问其他任何资源。  
### 漏洞是如何被发现的  
  
研究人员在测试部署在 Cloudflare 之后、且 WAF 仅允许特定来源访问的应用时发现，对/.well-known/acme-challenge/{token}  
的请求绕过了 WAF，并直接到达源站服务器。  
  
在演示主机上的测试证实了这一行为：  
- 对普通路径的访问会返回 Cloudflare 的拦截页面；  
  
- 而对 ACME 路径的访问，即使没有真实的令牌，也会返回由源站生成的响应。  
  
研究人员通过自定义主机名创建了一个稳定、处于待验证状态的 HTTP-01 令牌，从而能够在全球范围内可靠地测试 WAF 的行为。  
### 潜在风险与影响  
  
当 Cloudflare 的 WAF 允许 /.well-known/acme-challenge/...  
 路径绕过防护时，信任边界从 WAF 转移到了源站。演示应用显示了由此带来的多种风险，包括：  
- Spring / Tomcat 端点泄露敏感的环境变量  
  
- Next.js SSR 页面暴露运行和运维细节  
  
- PHP 路由因本地文件包含漏洞暴露文件  
  
此外，账户级 WAF 规则在该路径上被忽略，使基于请求头的攻击成为可能，例如 SSRF、SQL 注入和缓存投毒。  
  
Cloudflare 已于 2025 年 10 月 27 日 修复该问题，恢复了对该路径的一致性 WAF 防护。  
### 研究人员的警告  
  
安全研究机构 FearsOff 在报告中指出：  
> “当用于检查请求头的 WAF 规则被跳过时，许多漏洞类型就重新获得了通往源站的通道：例如遗留代码中基于请求头的 SQL 拼接、通过 X-Forwarded-Host  
 或 X-Original-URL  
 实现的 SSRF 和主机混淆、当缓存因请求头变化而产生的缓存键投毒、利用 X-HTTP-Method-Override  
 的方法覆盖技巧，以及通过自定义请求头触发的调试开关。显而易见的问题是——还有多少应用对请求头的信任程度超出应有范围？又有多少应用依赖 WAF 来充当这种信任与互联网之间的防线？”  
  
### AI 时代下的 WAF 绕过风险  
  
报告还强调，随着 AI 驱动攻击的发展，这类 WAF 绕过漏洞的危险性正在上升。AI 能够迅速发现并利用暴露的路径，将多个小漏洞串联成大规模攻击。与此同时，防御方也在使用 AI 进行攻击模拟和防御部署，使强健、全面的 WAF 防护变得愈发关键。  
  
报告总结称：  
> “在 AI 驱动攻击不断演进的背景下，这类 WAF 绕过漏洞显得尤为紧迫。由机器学习驱动的自动化工具可以快速枚举并利用诸如 /.well-known/acme-challenge/  
 这样的暴露路径，在大规模环境中探测特定框架的弱点或配置错误。”  
  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】苹果 App Store、Apple TV 和 iTunes 商店出现服务中断，照片应用也受影响](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073823&idx=1&sn=3ae9380aed826d5162cb8dc5e38f4710&scene=21#wechat_redirect)  
  
  
  
[【安全圈】麦当劳被勒索软件攻击，861GB 敏感数据失窃](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073823&idx=2&sn=c3af708cbe2c9cbf1f1cc812beea988a&scene=21#wechat_redirect)  
  
  
  
[【安全圈】WordPress 插件漏洞导致 10 万余个网站面临权限提升攻击风险](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073823&idx=3&sn=c3951d395ab247469235b1bedcd3f029&scene=21#wechat_redirect)  
  
  
  
[【安全圈】网络工程师李某以技术手段窃取赌博网站184万余名中国公民个人信息，警方已扣押其180余个比特币](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073800&idx=1&sn=2243bc4e8751be2209553741800e555d&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
  
  
