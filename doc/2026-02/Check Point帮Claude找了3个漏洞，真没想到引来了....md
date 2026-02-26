#  Check Point帮Claude找了3个漏洞，真没想到引来了...  
原创 泽钧
                    泽钧  数世咨询   2026-02-26 08:03  
  
上周，Anthropic 公司给旗下AI编码助手 Claude Code，新增了一个Security Scan（代码安全扫描）功能，并率先向企业和团队客户开放Beta测试版，号称在其生产环境（开源代码库）中发现了超过 500 个漏洞，直接把全球网络安全板块的股价吓崩了。仿佛AI不仅会写代码，现在还能当救火队长。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lYWDmickZ2mw8ia3icnehT43fCrc9EAJibIaIUzYB6N7mAJDgVpwicto8n8hr4sGNnJMFB2e3EPgjBTfYicU5qzZ3K9oOf7yJceRiaMzibdd7uxgT8Y/640?wx_fmt=png&from=appmsg "")  
  
Claude Code 为何急匆匆推出安全扫描功能？难道是之前**Check Point**  
 给他们找了3个漏洞，来了一场“高手过招”？我们来看看之前的3个漏洞是咋回事。  
  
**0****1**  
  
**AI加持的开发流程，带来了全新的攻击面**  
  
随着人工智能工具能够自主执行命令、初始化外部集成和发起网络通信，配置文件实际上已成为执行层的一部分。曾经被视为操作上下文的因素，现在直接影响着系统行为。Claude Code是一款命令行编码工具，正在成为程序员桌面上的“标配”。开发者可以使用它生成和编辑代码、修复错误、运行 shell 命令以及自动化代码测试等任务，效率提升肉眼可见，许多组织已经开始使用这类工具来加速软件开发。  
  
这也是为何GitHub Copilot、Amazon CodeWhisperer 和 OpenAI 的 Codex等同类产品发展迅猛。  
  
然而，Check Point的安全研究员 Aviv Donenfeld 和 Oded Vanunu 在他们的博客文章中一针见血地指出：  
  
“曾经作为被动数据的配置文件，如今成了主动执行路径的控制器。”  
  
简单说，传统开发模式里，你打开一个项目文件夹，顶多是看看静态的代码。但将人工智能集成到开发工作流程中，虽然带来了巨大的生产力提升，但也引入了传统工具中不存在的新攻击面，因为它们可以直接访问源代码和本地文件，有时甚至需要生产环境中的凭据。此外，这些工具本身也存在其他风险，例如可能产生幻觉以及生成不安全且易受攻击的代码。你“打开项目”这个动作本身，就可能触发一系列自动化操作。  
  
你引入了一个强大的自动化“副驾驶”，也无意中为自己打开了一扇危险的“后门”。  
  
**02**  
  
**工程师自曝：只需打开一个仓库，你的电脑就“裸奔”了**  
  
去年，Check Point就向Anthropic报告了Claude Code存在的三个严重安全漏洞，开发者只需打开一个项目存储库，就可能面临机器完全被接管，远程代码执行和API凭证被盗的风险。  
  
Check Point 的研究员指出：**这些漏洞利用了各种配置机制，**  
包括 Hooks、模型上下文协议 (MCP) 服务器和环境变量，**当用户克隆和打开不受信任的存储库时，攻击者便能执行任意 shell 命令，并窃取****API****密钥。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lYWDmickZ2mwQfwPE9wgaAnJJc0rEVUibr12rrpRy9Dfoo0y7tzsOGZBtDMHzNGatNYdhtrTiah2pFmq2TMib37WzBHJWHEs9CFSs72CDakKBrA/640?wx_fmt=png&from=appmsg "")  
  
是的，你没看错。仅仅只是“打开”一个被精心设计的项目，你的机器就门户大开。  
  
Claude Code 中的这些漏洞凸显了现代开发工具面临的一个关键挑战：如何在强大的自动化功能和安全性之间取得平衡。通过代码库控制的配置文件执行任意命令的能力造成了严重的供应链风险，一次恶意提交就可能危及任何使用受影响代码库的开发人员的安全。  
  
以下是这三个已被官方修复的漏洞详情：  
- **CVE-2025-59356：****Hooks****授权绕过（****CVSS****评分：8.7）**  
  
—该漏洞涉及 Claude Code 的 Hooks 功能。研究人员发现，攻击者在项目仓库的 Claude Code 配置文件中植入恶意 Hook 命令，利用工具在初始化时“先加载配置、后弹出授权”的逻辑缺陷，当开发者随后打开包含恶意 Hook 命令的项目时，导致通过 .claude/settings.json 中定义的不受信任的项目钩子执行任意代码，而无需额外确认。  
（已在 2025 年 9 月发布的 1.0.87 版本中修复）  
- **CVE-2025-59536：****MCP****（模型上下文协议）配置执行漏洞 （****CVSS****评分：8.7）**  
  
—与 Claude Code 的模型上下文协议(MCP) 设置有关，攻击者通过在受控仓库中配置恶意的 MCP 服务器，将编码平台与外部服务和工具连接起来，当用户在不受信任的目录中启动Claude Code时，可在工具启动初期、用户确认信任目录之前自动执行执行 Shell 命令。  
（已在2025年10月发布的1.0.111版本中修复）  
- **CVE-2026-21852：****API****凭据泄露漏洞（****CVSS****评分：5.3）**  
  
—存在于项目加载流程中信息泄露漏洞，攻击者通过API 通信地址劫持的漏洞，恶意配置重定向 API 通信基准地址，以便拦截 Claude Code 和 Anthropic 服务器之间的 API 相关通信，当开发者运行命令时，Claude Code 会将包含 API Key 的请求发送到攻击者伪造的后端地址， Claude Code 会在显示信任提示之前发出 API 请求，导致凭据泄露。  
（已在2026年1月发布的2.0.65版本中修复）  
  
换句话说，只需打开一个精心构造的代码仓库，就足以窃取开发者的有效 API 密钥，将经过身份验证的 API 流量重定向到外部基础设施，并捕获凭据。这反过来又可能使攻击者能够更深入地渗透到受害者的 AI 基础设施中。  
  
在人工智能驱动的开发浪潮中，供应链攻击的风险也不再仅仅是“引用了恶意的第三方库”。  
  
**如今，风险已经前置到了你“打开项目”的那一刻。**  
  
**03**  
  
**敲响警钟：如何守护你的AI开发环境？**  
  
Anthropic公司在收到报告后，已迅速修复了这些问题，这或许为上线代码安全扫描功能注入强心针。但Check Point的警告言犹在耳：  
> “这从根本上改变了威胁模型。风险不再局限于运行不受信任的代码，而是扩展到打开不受信任的项目。在人工智能驱动的开发环境中，供应链不仅始于源代码，还始于围绕源代码的自动化层。”  
  
  
这无疑给所有开发团队和使用了AI编码工具的同学提了个醒：  
1. **升级！升级！升级！**  
 务必使用工具的最新版本。  
  
1. **信任清单制**  
：对于来源不明、非自己创建的仓库，极度谨慎。  
  
1. **最小权限原则**  
：为开发环境和AI工具配置最小必要权限。  
  
1. **审查AI配置**  
：在将AI工具集成到开发流之前，务必审查其配置机制的安全性。  
  
生产力的提升，不应以牺牲基本安全防线为代价。  
> 欢迎在评论区和我们聊聊，你对AI编码助手当安全“救火队长”这件事怎么看？  
  
  
  
* 本文为泽钧编译，原文地址：https://thehackernews.com  
  
注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。  
  
— 【 THE END 】—  
  
🎉 大家期盼很久的#  
**数字安全交流群**  
来了！快来加入我们的粉丝群吧！  
  
🎁**多种报告，产业趋势、技术趋势**  
  
这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！  
  
👉   
扫码立即加入，精彩不容错过！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
😄  
嘻嘻，我们群里见！  
  
更多推荐  
****  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp8QpgS12GKDZmM3wbia28fgrBsUKCFUU3a6Tf9jsVWJcD2l6ic183HdhE2nqia7uMYO2NRQRylficZ5Q/640?wx_fmt=png&from=appmsg "")  
![]( "")  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539099&idx=1&sn=8820d80fdc92ac1f321b5e0a3ff0653e&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539436&idx=1&sn=676908ed11008cd016b253d1d8e6ba8a&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540181&idx=1&sn=e0cd678638b098f969f257b408062b91&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247540845&idx=1&sn=ec923893881e69010ad830ec852b0abb&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539573&idx=1&sn=a721e2933ad640a3a4b3c72f74d76685&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514185&idx=1&sn=8015c07a68a5e2b6074efd2c77f20085&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247539380&idx=1&sn=da5e8afa28247b4212a544750ece924d&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514336&idx=1&sn=e69b1126e86ab2c59c8ca8e315637031&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247530968&idx=1&sn=3d712e23b322ad37cee46d27adb08ed0&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538943&idx=1&sn=7f95d33eb069aab1cba23c41d68c9759&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247515942&idx=1&sn=bc9ba104b8eb1c0e914d90c8c9a34542&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247532302&idx=1&sn=2c6afc5d39c89c86f79020099ea44baa&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247512372&idx=1&sn=5d06a830f00953a0ab75157fc023ae56&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538487&idx=1&sn=c4a1ad3501ff0eea9eeb56f514f6e445&scene=21#wechat_redirect)  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247541747&idx=1&sn=b92b3db38dbbc9af3b19d8bf65bf0bea&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247537068&idx=1&sn=3a3e7c08d93638c1a6018c7862b13bcd&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247538269&idx=1&sn=848c657fc234aff8840d16d3f06b34ea&scene=21#wechat_redirect)  
  
  
  
