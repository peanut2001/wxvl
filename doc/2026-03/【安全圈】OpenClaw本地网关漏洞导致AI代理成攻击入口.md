#  【安全圈】OpenClaw本地网关漏洞导致AI代理成攻击入口  
 安全圈   2026-03-01 11:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
安全漏洞  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyHlu8kibkXZqcoNUrxntahAHuia0uYRKOKbynicBL4FxLjAcEeXRTA4u7nAZVtvj0XWcxfcKZTmyLzJhYKweQ8x8OdJeo2E8cghJI/640?wx_fmt=png&from=appmsg "")  
  
开源AI代理框架OpenClaw近日被披露存在一项“零点击”高危漏洞，研究人员指出，攻击者只需诱导开发者访问一个恶意网站，即可在无插件、无扩展、无交互的情况下，直接劫持其本地运行的AI代理，实现接近整机控制级别的权限获取。该漏洞由  
Oasis Security  
发现，影响范围随着OpenClaw在开发者群体中的快速普及而被进一步放大。  
  
OpenClaw是一款自托管AI代理工具，运行在开发者本地电脑上，可连接Slack、日历、开发工具及本地文件系统，并根据指令执行自动化操作。其核心通过绑定在localhost上的WebSocket网关进行调度，不同“节点”设备可注册到该网关，获得执行系统命令、读取文件、访问通讯录等能力。问题恰恰出在这一“默认信任本地连接”的设计假设上。  
  
攻击链的触发条件极其简单：开发者在浏览器中访问攻击者控制的网站。页面中的JavaScript脚本即可向本地OpenClaw网关发起WebSocket连接。由于现代浏览器并不会阻止跨源脚本访问回环地址，攻击脚本得以直接与本地服务通信。更严重的是，OpenClaw对来自localhost的连接未实施有效限速与失败计数，攻击者可以每秒数百次暴力猜测网关密码而不会被锁定或记录。一旦密码被破解，脚本即可自动注册为“受信设备”，系统默认批准来自本地的配对请求，无需用户确认。  
  
完成认证后，攻击者获得管理员级控制权限，可向AI代理下达指令，例如搜索Slack历史记录中的API密钥、读取私密消息、提取本地文件，甚至执行任意Shell命令。研究人员的概念验证显示，整个过程对受害者完全无感知，仅需一个浏览器标签页即可完成完整接管。  
  
漏洞根源在于三项错误假设的叠加：认为localhost天然安全、认为浏览器无法访问本地服务、认为回环地址无需限速控制。在现代Web环境下，这些前提均已不成立。研究团队完成负责任披露后，OpenClaw项目方在24小时内发布修复版本，将该问题列为高危漏洞。  
  
官方建议所有用户立即升级至2026.2.25或更高版本，并全面盘点组织内开发者终端上的OpenClaw实例，包括未纳入IT管理视野的“影子部署”。同时，应撤销不必要的API密钥与节点权限，将AI代理视为具备独立身份与高权限的系统实体，纳入统一身份与访问管理框架之中。  
  
此次事件再次表明，随着AI代理逐步具备跨应用、跨系统的自动执行能力，其安全边界已远超传统插件或脚本工具。一旦设计中的信任模型出现偏差，风险规模将迅速放大。对企业而言，AI代理不再只是效率工具，而是必须纳入核心安全治理体系的高权限数字身份。  
  
  
 END   
  
  
阅读推荐  
  
  
[【安全圈】ClawJacked 漏洞曝光：网站可远程劫持 OpenClaw AI 代理，开发者需立即升级](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074234&idx=1&sn=2f8e4442c9c605c764d28286413dffa2&scene=21#wechat_redirect)  
  
  
  
[【安全圈】“Vibe Coding”翻车：AI 社交网络 Moltbook 泄露 475 万条数据](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074234&idx=2&sn=5180d19efcb21fb235721580938c11df&scene=21#wechat_redirect)  
  
  
  
[【安全圈】恶意npm包“ambar-src”投毒Windows、Linux与macOS](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074234&idx=3&sn=6bf80090c0a276c836edd13d9b3b63e4&scene=21#wechat_redirect)  
  
  
  
[【安全圈】不用浏览器也能中招：Windows资源管理器成隐秘后门](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074234&idx=4&sn=2a4acaa0943a8a81ed7eda038d8f1330&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
