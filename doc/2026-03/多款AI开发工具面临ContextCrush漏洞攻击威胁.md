#  多款AI开发工具面临ContextCrush漏洞攻击威胁  
 SecHub网络安全社区   2026-03-09 03:07  
  
****  
****  
****  
**点击蓝字 关注我们**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwuh8LP87lPQLxMwiceAsv3TurmE7zZOulOhMELnQ2OulwFIJkbmB3bRg/640?wx_fmt=png "")  
  
  
**免责声明**  
  
本文发布的工具和脚本，仅用作测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。  
  
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关内容。  
  
文中所涉及的技术、思路及工具等相关知识仅供安全为目的的学习使用，任何人不得将其应用于非法用途及盈利等目的，间接使用文章中的任何工具、思路及技术，我方对于由此引起的法律后果概不负责。  
## 🌟简介                            
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/KZCmibwhia3VVJDQbhRzBuuKoibmFC9aSLhNThVdpI1xzfOTic83dibPyo1IwSW5ycA6X76xdC0n1JHfnOvBSic1Qr821kcMibXkxhj3gbzdl0LMg4/640?wx_fmt=png&from=appmsg "")  
  
    一个影响 Context7 MCP 服务器的关键漏洞已被安全研究人员披露，该服务器是广泛用于向 AI 编程助手提供文档的工具。  
  
    该漏洞被称为 ContextCrush，可能允许攻击者通过受信任的文档渠道向 AI 开发工具注入恶意指令。  
  
    该漏洞由 Noma Labs 研究人员在由 Upstash 运营的 Context7 平台上发现。Context7 被开发者用于在集成开发环境中直接为 Cursor、Claude Code 和 Windsuf 等 AI 助手提供最新的库文档。  
# 详情    漏洞源于平台的 Custom Rules（自定义规则） 功能，库维护者可通过该功能向 AI 提供专用指令，帮助助手更好地解析文档。研究人员发现，这些指令会原样下发给 AI，不经过任何过滤或净化。    由于指令通过受信任的 MCP 服务器传输，AI 会将其视为合法指引，并以开发者电脑的权限执行。    这意味着攻击者可在文档注册库中植入恶意规则，并借助 Context7 的基础设施分发给开发者的 AI 工具，且无需与受害者系统直接交互。  
####  研究人员概述了一种典型的攻击链：  
  
·     使用 GitHub 账号在 Context7 注册新库  
  
·     在 Custom Rules 中插入恶意指令  
  
·     等待开发者通过 AI 编程助手查询该库  
  
·     触发后，AI 会利用现有系统权限执行有害操作  
  
****  
**Noma Labs 还强调，GitHub 声誉、热度排名、信任评分等指标均可被操纵，恶意库可轻易伪装成可信库**  
。  
  
  
    测试中，研究人员成功演示了被投毒的库条目如何攻陷开发环境。  
  
AI 助手被指令搜索敏感 .env 文件、将内容传到攻击者控制的仓库，并以 “清理任务” 为名删除本地文件。由于指令与合法文档一同下发，AI 无法可靠区分。  
  
  
    在 2 月 18 日漏洞披露后，Upstash 次日开始修复，并于 2 月 23 日正式发布补丁，加入规则净化与额外安全防护。目前无证据表明该漏洞已被实际利用。  
  
  
  
  
  
欢迎关注SecHub网络安全社区，SecHub网络安全社区目前邀请式注册，邀请码获取见公众号菜单【邀请码】  
  
**#**  
  
  
**企业简介**  
  
  
**赛克艾威 - 网络安全解决方案提供商**  
  
****  
       北京赛克艾威科技有限公司（简称：赛克艾威），成立于2016年9月，提供全面的安全解决方案和专业的技术服务，帮助客户保护数字资产和网络环境的安全。  
  
  
安全评估|渗透测试|漏洞扫描|安全巡检  
  
代码审计|钓鱼演练|应急响应|安全运维  
  
重大时刻安保|企业安全培训  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwuh8LP87lPQLxMwiceAsv3TurmE7zZOulOhMELnQ2OulwFIJkbmB3bRg/640?wx_fmt=png "")  
  
  
**联系方式**  
  
电话｜010-86460828   
  
官网｜https://sechub.com.cn  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0FW5uwU0BZtn2lmMrLPwpibCeCVbtBFDRkbFb7n7ibhPRxg20spUo9mUIiakmRYABB88Idl81IpGuXfw/640?wx_fmt=gif "")  
  
**关注我们**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SUZ43ICubr4mWJcUARDKYbQooQjbjbmqZTerAIXqDX9CaVxXbB7pyWwnMRklrCJias9r59PhnJAxZ4e3gYjyqVQ/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/SUZ43ICubr4mWJcUARDKYbQooQjbjbmqZTerAIXqDX9CaVxXbB7pyWwnMRklrCJias9r59PhnJAxZ4e3gYjyqVQ/640?wx_fmt=png "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/8icWLyUKibZZrPdaxnm18Zscp6Xcu0OiaMwyhlWCYDVqK38BA5dbjKkH7icWmAew7SYRA7ao1bFibialrMvmQ9ib0TBvw/640?wx_fmt=jpeg "")  
  
  
**公众号：**  
sechub安全  
  
**哔哩号：**  
SecHub官方账号  
  
  
  
