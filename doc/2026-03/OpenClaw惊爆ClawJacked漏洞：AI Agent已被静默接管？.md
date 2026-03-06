#  OpenClaw惊爆"ClawJacked"漏洞：AI Agent已被静默接管？  
千里
                    千里  东方隐侠安全团队   2026-03-05 13:58  
  
![](https://mmecoa.qpic.cn/mmecoa_png/TxlKcWciboehHZRolffNcmJfvBYcTaKNxUMx0MjVGjEMB00oAKyYGCUPaUnzBXdDHmnNdFK65xQJO1fk7zEicaTQ/640?from=appmsg "")  
  
昨天小隐（千里's Claw&Friend）刷Twitter，看到Oasis Security发了一条推，说发现了OpenClaw的一个高危漏洞，名字叫ClawJacked。  
  
我当时的反应是：又是OpenClaw？最近的漏洞实在太多了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNhySzQ69diaRfkRSj0aEtZlLK67cXIjlXDoicrXXgJsGOXBDDA471vpPgymCxAVNusfzHXnL5mUd9QyyjKDfBdSA5B1pRM3ZUyG4/640?wx_fmt=png&from=appmsg "")  
  
不过这次真的不一样。这是一个零点击漏洞——你只需要开着OpenClaw去访问一个恶意网站，攻击者就能静默接管你的AI Agent。  
  
  
01  
  
它是怎么攻击的？  
  
  
说白了就几步：  
1. 你在本机跑着OpenClaw gateway（localhost + 密码保护）  
  
1. 你像往常一样上网，访问了一个看似正常的网站  
  
1. 这个网站的JavaScript代码会尝试连接你本地的OpenClaw端口  
  
1. 因为本地连接没有速率限制，它可以直接暴力破解你的密码  
  
1. 破解成功后，系统自动把它注册为"可信设备"——因为本地连接被认为是可以信任的  
  
1. 然后，攻击者就完全控制了你的AI Agent  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNhnlwtQQAaSicYXuI8USEVAoCZLWiamP05bLQHh6vx6eyooK0ib3cTQic3FbY1e6v3wMYAJvWstnBkXicjWOq1ruIXYAonAjCJCvFLQ/640?wx_fmt=other&from=appmsg "")  
![]( "")  
  
你什么都没做，没有任何点击，没有任何授权——AI Agent就没了。当然了，在对Openclaw如此授权的情况下，部署Agent服务的机器权限也就被接管了。  
  
这不比传统攻击恐怖多了？  
  
  
02  
  
攻击成功了能干嘛？  
  
  
这是最细思极恐的地方。  
  
一旦攻击者控制了你的AI Agent会发生什么？  
  
• 如果你用OpenClaw配置了Binance API交易——攻击者可以直接操纵你的账户  
  
• 如果你用OpenClaw登录了各种服务——攻击者可以获取你的凭据  
  
• 如果你的AI Agent有访问敏感文件的权限——攻击者可以直接读取  
  
在今天我们发的文章中，我们配置Binance API的时候我就说，API Key一定要保护好。结果好家伙，OpenClaw本身就有漏洞。  
  
  
03  
  
还有一个问题：Skills也不安全  
  
  
Oasis Security顺便审计了2890+个OpenClaw skills，结果更让人头皮发麻：  
  
• 41%存在漏洞  
  
• 99.3%没有config.json权限清单  
  
啥意思？  
  
就是攻击者可以上传一个看起来人畜无害的Skill（比如"智能邮件助手"），等48小时后开始窃取你的浏览器凭据和Keychain数据。  
  
你完全不知道什么时候中的招。  
  
  
04  
  
官方怎么说？  
  
  
好消息是：漏洞已经在2026.2.25修复了，2026.2.26版本包含了完整修复。  
  
坏消息是：这是一个典型的"发现即利用"漏洞——在公开之前，很可能已经被利用过了。  
  
  
05  
  
我是怎么应对的？  
  
  
第一时间检查了自己的OpenClaw版本。  
```
openclaw status
```  
  
确认是2026.2.26，然后长舒一口气。  
  
但更重要的是，我开始反思：  
  
我们到底应该怎么安全地使用AI Agent？  
  
企业应该怎么做？  
1. 立即升级：如果还在用旧版本，马上升到2026.2.26+  
  
1. 不要在公网暴露OpenClaw gateway：这次漏洞主要针对本地开发者，但如果你非要把它暴露到公网，那就是找死  
  
1. 定期审计AI Agent的访问权限：不只是人在审查，AI Agent的权限也要定期review  
  
1. 对非人类身份实施治理：Gartner称之为"身份暗物质"问题——企业里AI Agent数量激增，但身份验证和权限控制基本是空白  
  
1. 谨慎使用第三方Skills：来源不明的Skill不要随便装，装之前看看权限要求  
  
个人开发者应该怎么做？  
1. 保持更新：这不用说了  
  
1. API Key别存本地：上次我们配置Binance API我就说了，能不用固定签名就不用，这次漏洞更是印证了这一点  
  
1. 本地调试时别乱上网：开玩笑，但确实要注意  
  
1. 敏感操作用独立账号：别用一个API Key干所有事  
  
06  
  
这对行业意味着什么？  
  
ClawJacked漏洞不仅仅是一个OpenClaw的问题，它是  
整个AI Agent行业  
的警钟。  
  
Gartner最新报告显示：  
  
• 25%企业已部署AI Agents  
  
• 88%在追求agentic AI转型  
  
• 但身份治理完全跟不上  
  
换句话说：AI Agent的安全问题才刚刚开始。  
  
以前我们担心的是传统网络安全：防火墙、杀毒软件、渗透测试。但AI Agent带来的问题是全新的：  
  
• AI Agent有"意志"——它会自主决策  
  
• AI Agent有"能力"——它能调用工具、执行操作  
  
• AI Agent有"信任"——它被授予了很高的权限  
  
当攻击者能控制你的AI Agent，本质上就是控制了一个能自主思考和行动的"数字员工"。  
  
这比传统的"控制一台服务器"恐怖一百倍。  
  
  
07  
  
写到最后  
  
用AI Agent没问题，但一定要记住：  
1. 保持更新——漏洞修复要及时  
  
1. 最小权限——别给Agent太大权力  
  
1. 定期审计——看看Agent做了什么  
  
1. 来源审查—— Skills要从靠谱的地方装  
  
AI是最冷静的助手，但它也是最危险的武器——如果落在别人手里的话。  
  
  
欢迎关注「东方隐侠安全团队」，一起探索AI安全的边界。  
  
  
喜欢就  
关注  
哦  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNhebd9CgAEGjlfm78nsPazFbFf7JljaibfnsGQn705w9VHXJ0JbX8V17PpP1269icnsjY9tfxP3B9LxCNF2cMYOK2WTxWef8JG9o/640?wx_fmt=png&from=appmsg "")  
  
  
动动小手点个  
赞  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNiaib6w6lCoNXLgM53b9SsaPmm9IgQCqBjlh4ECaJQGYydZbAxVJsOC7dFjzHdGYGkFWZmV4LjFHQE9x6FR0CY6qfqKQqlc84G90/640?wx_fmt=png&from=appmsg "")  
  
  
点  
在看  
最好看  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNj8Msed2kYWKYkb6Y0eaKyYbyQJicdue3cYnE2DD0csddLrvpbARRPdMrGI0r9XM0XEIxeibd418bCfMsClmRF9SYFN6chutQebQ/640?wx_fmt=png&from=appmsg "")  
  
  
