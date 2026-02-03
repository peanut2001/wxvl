#  【安全圈】Moltbook AI 漏洞暴露邮箱地址、登录令牌与 API 密钥  
 安全圈   2026-02-02 11:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
AI漏洞  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylg52qGWskI3mUn6VK53TC7pPF0oiceRiaBM52QBlU8icjY3w2BQ6GIT5nBGIB08rUEEHWN2BOK19ZCiag/640?wx_fmt=png&from=appmsg "")  
  
Moltbook 是 Octane AI 的 Matt Schlicht 于 2026 年 1 月末推出的新兴 AI 智能体社交网络，当前该平台因号称**拥有 150 万 “用户” 引发热议**  
，但其存在一项**高危漏洞**  
，导致**注册主体的电子邮箱、登录令牌及 API 密钥遭泄露。**  
  
研究人员披露，该平台因数据库配置不当导致暴露，未授权人员可访问智能体档案，进而实现批量数据窃取。  
  
该漏洞同时伴随账户**创建无速率限制**  
的问题，据悉单个 OpenClaw 智能体（@openclaw）就注册了 50 万个虚假 AI 用户，直接戳破了媒体所称的自然增长论调。  
  
**平台运行机制**  
  
Moltbook 支持基于 OpenClaw 构建的 AI 智能体发布内容、评论，还可创建如 m/emergence 这类 “子社群”，催生了围绕**AI 涌现、报复性信息泄露、Solana 代币刷信誉**  
等话题的智能体论战  
  
平台已涌现**超 2.8 万条帖子及 23.3 万条评论**  
，并有 **100 万**  
沉默验证者对内容进行查看。但智能体数量存在造假：因无注册限制，大量机器人批量注册，营造出平台爆火的假象。  
  
关联**不安全开源数据库的暴露端点**  
，无需身份验证，仅通过 GET /api/agents/{id} 这类简单查询指令，即可泄露智能体数据。  
  
![新闻1](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylg52qGWskI3mUn6VK53TC7peWc1jqwch7Nnz1xYvl17V4vPBFtIKq0G2wg6kUGxVBYM1GUscbxvqQ/640?wx_fmt=png&from=appmsg "")  
  
攻击者可以通过枚举 ID 快速获取成千上万条记录。  
  
**安全风险与专家警告**  
  
此次不安全的直接对象引用（IDOR）及数据库暴露漏洞，构成了 “致命三重威胁”：**智能体可访问私密数据、平台存在不可信输入风险（提示注入）、支持外部通信，可能引发凭证窃取、文件删除等破坏性操作。**  
  
Andrej Karpathy 称该平台是 “充斥垃圾信息的规模里程碑”，但更是 “计算机安全噩梦”，Bill Ackman 则评价其 “令人恐慌”。子社群中的提示注入攻击**可操控机器人泄露宿主数据**  
，且 OpenClaw 无沙箱隔离的执行机制会加剧这一风险。  
  
目前尚无修复补丁确认；Moltbook (@moltbook) 对漏洞披露无回应。安全专家强烈建议用户及智能体所有者：立即**撤销所有相关API密钥、将智能体置于沙箱环境中运行，并全面审计数据暴露情况**  
。对于企业而言，不受管控的此类机器人活动更带来了严峻的“影子IT”风险。  
  
  
 END    
  
  
阅读推荐  
  
  
[【安全圈】紧急安全提醒！请立即备份自己的VPS数据 大量VPS提供商面临勒索软件攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073959&idx=1&sn=71f7dd6da6798aecab4b7df91eb2a27f&scene=21#wechat_redirect)  
  
  
  
[【安全圈】两个 n8n 高危漏洞可使认证用户远程执行代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073959&idx=2&sn=5b4af53f24f7e46133988e49401751da&scene=21#wechat_redirect)  
  
  
  
[【安全圈】Chrome 发布安全更新，修复后台 Fetch API 漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073959&idx=3&sn=3979835f9237351359e08771b9781191&scene=21#wechat_redirect)  
  
  
  
[【安全圈】国产飞牛系统fnOS疑似出现重大安全漏洞 官方已修复但没有发布安全公告](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073946&idx=1&sn=bdc710b97937508dd118e83b9f789587&scene=21#wechat_redirect)  
  
  
  
  
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
  
  
  
  
  
  
