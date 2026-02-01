#  【安全圈】两个 n8n 高危漏洞可使认证用户远程执行代码  
 安全圈   2026-02-01 05:24  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
漏洞  
  
  
网络安全研究人员披露了在 n8n 工作流自动化平台两个新的安全漏洞，其中一个为可导致远程代码执行的高危漏洞。  
  
  
这两个由 JFrog 安全研究团队发现的漏洞详情如下：  
- **CVE-2026-1470（CVSS 评分：9.9）**  
：一个 eval 注入漏洞。经过身份验证的用户可通过传入特制的 JavaScript 代码，绕过平台的表达式沙箱机制，从而在 n8n 主节点上实现完整的远程代码执行。  
  
- **CVE-2026-0863（CVSS 评分：8.5）**  
：一个 eval 注入漏洞。经过身份验证的用户可借此绕过 n8n 的 python-task-executor 沙箱限制，在底层操作系统上运行任意 Python 代码。  
  
  
成功利用这些漏洞可使攻击者劫持整个 n8n 实例，即便该实例运行在 “内部” 执行模式下也不例外。n8n 在其文档中指出，**在生产环境中使用内部模式可能带来安全风险，并建议用户切换至外部模式**  
，以确保 n8n 与任务运行进程之间有适当的隔离。  
  
  
“n8n 为自动化 AI 工作流而遍布企业全流程，因此它掌控着、基础设施的核心工具、功能和数据密钥，包括大语言模型（LLM）API、销售数据和内部身份与访问管理（IAM）系统等，”JFrog 在与 The Hacker News 分享的声明中表示。“一旦发生沙箱逃逸，就相当于为黑客提供了通往整个公司的有效‘万能钥匙’。”  
  
  
为修复这些漏洞，**建议用户升级至以下版本**  
：  
- **CVE-2026-1470**  
：请升级至 1.123.17、2.4.5 或 2.5.1 版本。  
  
- **CVE-2026-0863**  
：请升级至 1.123.14、2.3.5 或 2.4.2 版本。  
  
此次披露距离 Cyera Research Labs 详细说明 n8n 中一个最高危漏洞（CVE-2026-21858，又名 Ni8mare）仅过去数周，该漏洞允许未经认证的远程攻击者完全控制易受攻击的实例。  
  
  
“这些漏洞凸显了安全地沙箱化 JavaScript 和 Python 这类动态高级语言的难度之大，”研究员 Nathan Nehorai 表示。“**即便部署了多层验证、拒绝列表和基于抽象语法树（AST）的控制措施**  
，攻击者仍可利用微妙的语言特性和运行时行为来突破安全设计的预设。”  
  
  
“在此案例中，一些已被弃用或鲜少使用的语法结构，结合解释器的变更与异常处理行为，便足以突破原本限制严格的沙箱，最终实现远程代码执行。”  
  
  
  END    
  
  
阅读推荐  
  
  
[【安全圈】国产飞牛系统fnOS疑似出现重大安全漏洞 官方已修复但没有发布安全公告](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073946&idx=1&sn=bdc710b97937508dd118e83b9f789587&scene=21#wechat_redirect)  
  
  
  
[【安全圈】Metasploit 发布 7 个新漏洞利用模块 覆盖 FreePBX、Cacti 和 SmarterMail](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073946&idx=2&sn=9b93e65f9ea42f56a293adcf299febd6&scene=21#wechat_redirect)  
  
  
  
[【安全圈】AI 助手 Clawdbot 现象级爆火背后：全网 8000+ 资产暴露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073946&idx=3&sn=a37c28361316ce30cb7d7c1124e1fbc7&scene=21#wechat_redirect)  
  
  
  
[【安全圈】TrustBastion 恶意安卓 App 曝光，瞄准你的支付宝与微信钱包](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073929&idx=1&sn=b57ffb86f56d66a8ea12c5455a3dfdbf&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
  
  
  
  
