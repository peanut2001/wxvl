#  【安全圈】ClawJacked 漏洞曝光：网站可远程劫持 OpenClaw AI 代理，开发者需立即升级  
 安全圈   2026-02-28 11:02  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
安全漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyFibNT95xkqu3UhuyplaNaA7xqKomAibXR2Nrv9wiaOkA4Ir3IGFWiaQBQn1oA1fnKCVs7WKFbP5p2icmdia6Yj865x4mo3Sl5Dyj4Lc/640?wx_fmt=png&from=appmsg "")  
  
近期爆红的开发者 AI 工具 OpenClaw 因严重安全漏洞引发关注。由 Oasis Security 披露的 ClawJacked（CVE-2026-25253）漏洞链显示，攻击者只需诱导用户访问恶意网站，即可通过 WebSocket 机制悄无声息地接管本地运行的 AI 代理。问题核心在于 OpenClaw 默认信任来自 localhost 的连接，未对本地请求进行严格校验，导致恶意网页脚本可直接与后台 AI 工具通信。  
  
研究人员演示的 PoC 表明，攻击者可以在用户毫无察觉的情况下暴力猜测密码。由于系统未限制本地连接的尝试次数，脚本每秒可尝试数百次密码组合，成功后即可获得管理员权限，读取 Slack 私信、窃取 API Key，甚至指挥 AI 搜索并外传本地文件。  
  
所幸，OpenClaw 团队在接到通报后 24 小时内发布修复版本，官方建议用户立即升级至 2026.2.25 或更高版本。值得注意的是，此前其社区市场还曾出现超过 1000 个恶意技能，显示攻击者已将 AI 代理生态作为重点目标。  
  
多位安全专家指出，这一事件暴露出“本地即安全”的错误信任模型。AI 代理具备与用户等同甚至更高的权限，应被视为高权限身份主体纳入零信任架构与身份安全体系管理。随着 AI 代理深度嵌入开发与办公流程，安全设计必须与功能扩张同步推进，否则一次劫持便可能造成全面数据泄露。  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】Python 热门 ORM 爆出 9.8 分致命漏洞，数据库或被完全读取](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074218&idx=1&sn=dbc3ef3759a7705b77b093a33c6f0804&scene=21#wechat_redirect)  
  
  
  
[【安全圈】罗马尼亚黑客被引渡至美国，承认入侵俄勒冈州政府网络并实施身份盗窃](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074218&idx=2&sn=712cffe01a041c791e30e33ff4125456&scene=21#wechat_redirect)  
  
  
  
[【安全圈】微软披露新型木马攻击：伪装游戏工具植入RAT，远程窃取数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074218&idx=3&sn=3a065b05b92288570c00874b27a084fb&scene=21#wechat_redirect)  
  
  
  
[【安全圈】新型安卓RAT“Oblivion”曝光：$300即可买断，自动绕过权限与隐藏远程控制](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074218&idx=4&sn=ec2b1e90e791d26d0e824829d9784551&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
