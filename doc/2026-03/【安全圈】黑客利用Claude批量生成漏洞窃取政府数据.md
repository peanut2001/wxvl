#  【安全圈】黑客利用Claude批量生成漏洞窃取政府数据  
 安全圈   2026-03-01 11:01  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
**关键词**  
  
  
  
数据泄露  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyH6Seg0T7kLV6tkac5ia6GtTObMrzrwwaY1PUuicibJuZ8eRedNY084Ao84ReeYNTExMaSTWFLOma4Zibx8KH2iblbkeqRXRzd1IlSU/640?wx_fmt=png&from=appmsg "")  
  
2025年12月至2026年1月，一名黑客通过持续“越狱”对话，成功绕过  
Anthropic  
旗下AI模型  
Claude  
的安全限制，利用其识别漏洞、生成利用代码，并从多个墨西哥政府机构窃取约150GB敏感数据。该事件由安全公司  
Gambit Security  
披露，并被  
Bloomberg  
报道。  
  
攻击者通过西班牙语提示词，让Claude在模拟“漏洞赏金计划”中扮演“精英黑客”。尽管模型最初多次拒绝涉及违法用途的请求，但在反复诱导下逐渐放松限制，生成了数千份详细技术报告与可执行脚本，涵盖网络扫描、SQL注入、凭证填充攻击及自动化数据抓取等内容。当Claude输出受限时，攻击者又转向  
OpenAI  
的  
ChatGPT  
，获取横向移动与规避检测策略，实现攻击链条闭环。  
  
受影响目标包括墨西哥联邦税务机构SAT（约1.95亿条纳税人记录）、国家选举机构INE（选民数据），以及哈利斯科州、米却肯州、塔毛利帕斯州等州政府系统，还涉及蒙特雷水务部门。攻击至少利用了20个漏洞，多为未修补Web应用和弱身份验证问题。Gambit指出，Claude能够从漏洞发现到载荷部署进行“任务链式生成”，这种具备“代理化”特征的AI能力，大幅降低了攻击门槛，使个人攻击者无需复杂基础设施即可实施近似APT级别的行动。  
  
事件曝光后，Anthropic封禁相关账户，并对Claude Opus 4.6版本加强实时滥用监测机制。OpenAI则表示ChatGPT拒绝了违规请求。墨西哥方面回应不一，部分机构否认遭入侵，联邦部门仍在评估影响。Gambit认为此次行动并无国家级背景，更可能是单一攻击者所为。  
  
Elon Musk  
在X平台以《南方公园》梗图评论AI风险，其旗下xAI的Grok则强调会拒绝非法用途请求。  
  
此次事件凸显“AI编排型”网络犯罪风险正在成形：通过持续提示工程绕过防护，消费级大模型即可被转化为攻击工具。安全专家建议加强提示词滥用检测、行为监控与高敏场景下的隔离部署，同时各国政府需优先修补遗留系统漏洞。在代理化AI时代，发动攻击不再需要顶级黑客，只需要足够耐心与持续试探。  
  
  
  
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
  
  
