#  【安全圈】爆火 AI 智能体 OpenClaw 被发现严重漏洞，可传播 / 植入 macOS 病毒  
 安全圈   2026-02-04 11:02  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
AI、恶意软件  
  
  
密码管理工具 1Password 于 2 月 2 日发布博文，其安全团队发现有攻击者利用爆火 AI 智能体 OpenClaw（原名 Clawdbot 和 Moltbot），向 macOS 用户散播和植入恶意软件。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHpJgk3TAht66KCusicWt9kwJXdgMNou0qhvxw1gTYquHNqKTRgJpV4TtgXTRQ26IicBsJHzOJiaxEUKFwibGZwjE6aCuC6je0Xiazc/640?wx_fmt=jpeg&from=appmsg "")  
  
注：OpenClaw 是一个近期爆火的 AI 智能体，核心竞争力在于其 " 主动自动化 " 能力。该 AI 智能体无需用户发出指令，即可自主清理收件箱、预订服务、管理日历及处理其他事务。同时，它具备强大的记忆功能，能够保存所有对话历史，并从过往的对话片段中精准回调用户的偏好设置。  
  
攻击者利用了 OpenClaw 的 " 技能 "（Skills）文件，这些通常为 Markdown 格式的文件本用于指导 AI 学习新任务，**却被黑客伪装成合法的集成教程。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljRMAYtDftYGPEJRsxwCSat6sOUga3IRib8xSK0ib37sibRLqazpZd19QvVIYlZfvibExicCOXzGx8TiaIw/640?wx_fmt=jpeg&from=appmsg "")  
  
在看似常规的设置过程中，文档会诱导用户复制并运行一段 Shell 命令。该命令会在后台解码隐藏载荷、下载后续脚本，并修改系统设置以移除 " 文件隔离（Quarantine）" 标记，从而成功躲避 macOS 内置的安全检查。  
  
植入系统的有效载荷被确认为 " 信息窃取类（Infostealer）" 恶意软件。与传统破坏系统的病毒不同，该恶意软件专注于静默窃取高价值数据，包括浏览器 Cookie、活跃登录会话、自动填充密码、SSH 密钥以及开发者 API 令牌。对于开发人员而言，这意味着攻击者可能借此渗透至源代码库、云基础设施及企业 CI / CD 系统，造成连锁式的数据泄露。  
  
尽管部分开发者寄希望于 " 模型上下文协议（MCP）" 来限制 AI 权限，但事实证明该协议在面对此类攻击时形同虚设。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHzoncl5Yh6onursqaddbkSmtWvHT5uw8uvJ8la6sQARjfYPYHptqlick5WAAJUd1cHwYVAq0Gib84iay3XicYqbUT8zaAND0k58iaA/640?wx_fmt=jpeg&from=appmsg "")  
  
由于攻击本质上是利用文档进行社会工程学欺诈，而非直接调用工具接口，因此可以轻易绕过协议边界。同时，此次攻击显示黑客对 macOS 的防御体系极为熟悉，单纯依赖苹果系统的环境隔离已无法有效阻断此类威胁。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGIibMDYic3nOE3HCLrmlFA1ueiaFssM3Toj0UxUYJIGp8YkMnliafoUEhB8zCuv7MDIlF8VDIlmRiatTNh2IRzmPa0jxibiaZFd8yF5c/640?wx_fmt=jpeg&from=appmsg "")  
  
  
 END    
  
  
阅读推荐  
  
  
[【安全圈】黑客放出新变种病毒针对fnOS升级！官方紧急通告](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073982&idx=1&sn=105dd0887a04a2973f0cb2a46fe6e35a&scene=21#wechat_redirect)  
  
  
  
[【安全圈】海康威视修复DS-3WAP无线接入点命令注入漏洞（CVE-2026-0709）](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073982&idx=2&sn=de21d8160a6914ed983588d94ca30082&scene=21#wechat_redirect)  
  
  
  
[【安全圈】违法违规收集使用个人信息问题，72 款移动应用被通报](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073982&idx=3&sn=6d05f640425c249524534221f7f14569&scene=21#wechat_redirect)  
  
  
  
[【安全圈】元宝崩了！腾讯回应来了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073971&idx=1&sn=29226d82814e3d9a9807b3bff55702f3&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
  
  
  
  
