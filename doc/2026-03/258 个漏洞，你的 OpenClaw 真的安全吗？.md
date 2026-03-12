#  258 个漏洞，你的 OpenClaw 真的安全吗？  
 安全客   2026-03-12 03:53  
  
“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg "")  
  
  
2026 年开年现象级开源 AI Agent OpenClaw，官方披露并修复 258 个安全漏洞，多个版本受影响！360 漏洞研究院独家深度拆解：全球超 17 万公网暴露实例面临风险，其中严重漏洞可实现无交互远程代码执行。本文将完整梳理漏洞风险、影响范围与可落地的全场景防护方案，帮你避开 AI 助手变 “黑客后门” 的致命陷阱。  
  
  
**01**  
  
**什么是OpenClaw？**  
  
OpenClaw（曾用名 ClawdBot/Moltbot，国内俗称"龙虾"）是一款开源自主 AI Agent 框架，支持通过聊天界面控制，具备执行 Shell 命令、文件操作、浏览器控制、对接第三方服务的全权限能力，支持本地私有化部署。其核心架构遵循"本地优先"原则，由持续运行的后台网关（Gateway）作为控制枢纽，通过节点（Nodes）在终端设备上执行本地动作，并深度集成 WhatsApp、Telegram 和 Slack 等主流平台。  
  
OpenClaw 的爆发式增长令人瞩目——GitHub 星标数约 3 周突破 20 万（目前已达 30.2 万），创下开源项目增长纪录。国内云厂商纷纷上线一键部署服务，个人开发者、电商运营、企业办公自动化、运维管理、金融投研等场景中，大量用户跟风部署。然而，功能越强大，权限越开放，安全风险也越致命。  
  
  
**02**  
  
**OpenClaw 核心安全风险**  
  
  
默认配置信任边界模糊、权限模型过于开放、敏感信息存储无加密、技能扩展机制无安全校验，天生具备 “易被攻击、易被接管” 的属性。  
  
**早在 2026 年 2 月，360 漏洞研究院就已发布《当你在电脑中放入"赛博龙虾": Openclaw (原Clawdbot)安全风险分析》，率先预警了其架构层面的 RCE 漏洞、凭证泄露、供应链投毒等核心安全风险，而本次官方披露的 258 个漏洞，正是这些底层设计缺陷的集中爆发。**  
  
  
**03**  
  
**258 个漏洞概况**  
  
  
在对 OpenClaw 历史暴露 **258**  
 个安全记录的深度溯源中，我们发现该项目在演进过程中经历了一系列复杂的安全挑战。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz9aR7bicr0HsHlXfwIt8cjJa58WNnP2GHRS9LUMhTH2q8zdxmfH1EbEjicy1JODRJI8RvdnFLoDVKw1sib1icJVicypSoxTgAsnklH0/640?wx_fmt=png&from=appmsg "")  
  
图1：每周漏洞数量统计  
  
OpenClaw 产品漏洞覆盖从早期版本至 2026.3.8 之前的几乎所有发行版本。其中包含**严重漏洞3 个**  
，**高危漏洞 72 个，中低危漏洞 183个**  
。这些漏洞并非单一的技术缺陷，而是呈现出多维度并发的态势，涵盖了多种杀伤力巨大的类型，形成了对 OpenClaw 架构体系的立体化威胁。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzz9xnltILAwavVW2QVrUOIktTVSR1lddrhdluciakEP7kZDhZHFcBdlQzkCvkwRX0uxgY9onLRsMRtnoAkbIbEUuuicFNGpziapGMc/640?wx_fmt=png&from=appmsg "")  
  
图2：OpenClaw 漏洞等级分布  
  
OpenClaw 累计记录的漏洞类型分布广泛，其中**注入攻击**  
以 53 个案例位居榜首，紧随其后的是涉及 52 个案例的**访问控制****漏洞**  
。这两类漏洞的高频出现，反映出项目早期在底层架构的输入处理与用户权限隔离机制上存在明显的薄弱环节。此外，**路径遍历与文件操作**  
（46个）以及**认证漏洞**  
（29个）也占据了相当大的比重。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzzicZ7CQib2TibhBGl5ST4L8JlR42rMgEvnUvfaI1Pz6TYaJdolZYUvLy62cfd0rTrqvYvYVASstOJKvicvRXb7Bnqibz6icwiank5OHco/640?wx_fmt=png&from=appmsg "")  
  
图3：OpenClaw 漏洞类型分布  
  
据安全监测数据显示，截至 2026 年 3 月，全球公网暴露的 OpenClaw 实例已超 17 **万个**  
，其中国内暴露实例超过 7 **万个**  
，官方技能市场 ClawHub 已发现**1,184 个恶意技能包**  
（如 ClawHavoc 攻击事件），另有 **824 个恶意技能**  
 伪装成加密货币工具、YouTube 工具等，通过供应链投毒方式窃取 API 密钥、凭证及浏览器数据。结合 Bing AI 搜索结果篡改、恶意 npm 包（如 GhostClaw）等社会工程学攻击，OpenClaw 生态面临严峻的供应链安全威胁。  
  
  
**04**  
  
**OpenClaw 严重漏洞拆解**  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞名称</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">网关节点调用审批绕过导致的远程代码执行</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞编号</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">CVE-2026-28466</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">公开时间</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">2026-02-14</span></p></section></td><td data-colwidth="25.0000%" width="25.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span style="color: rgb(0, 0, 0);box-sizing: border-box;"><span leaf="">漏洞类型</span></span></strong></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">输入验证</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">影响版本</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">&lt; 2026.2.14</span></p></section></td><td data-colwidth="25.0000%" width="25.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">修复版本</span></strong></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">&gt;=2026.2.14</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">危害等级</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""> 严重级</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞描述</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">OpenClaw 在网关将指令转发给节点主机时，节点侧本应对高权限操作（如执行系统命令）进行审批校验，但网关未对用户传入的参数做任何过滤，导致攻击者只需在请求参数中加入特定的&#34;已审批&#34;字段，即可直接骗过节点主机的审批机制。持有合法网关凭据的攻击者无需任何额外条件，即可在任意已连接节点上执行任意系统命令。</span></p></section></td></tr></tbody></table>  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞名称</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">语音通话扩展入站允许列表策略绕过</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞编号</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">CVE-2026-28446</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">公开时间</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">2026-02-15</span></p></section></td><td data-colwidth="25.0000%" width="25.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span style="color: rgb(0, 0, 0);box-sizing: border-box;"><span leaf="">漏洞类型</span></span></strong></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">认证漏洞</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">影响版本</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">&lt;= 2026.2.1</span></p></section></td><td data-colwidth="25.0000%" width="25.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">修复版本</span></strong></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">&gt;=2026.2.2</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">危害等级</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""> 严重级</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞描述</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">该漏洞存在于语音通话扩展的入站白名单校验逻辑中，共有两处缺陷。其一，当来电号码为空（如匿名来电）时，系统错误地将空号码视为合法，允许无号码来电直接接通；其二，白名单比对采用的是号码后缀匹配而非精确匹配，攻击者只需使用任意一个结尾数字与白名单号码相同的号码拨打，即可通过验证。两种方式均无需任何权限，可直接绕过访问控制。</span></p></section></td></tr></tbody></table>  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞名称</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">插件安装路径遍历漏洞</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞编号</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">CVE-2026-28447</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">公开时间</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">2026-02-15</span></p></section></td><td data-colwidth="25.0000%" width="25.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span style="color: rgb(0, 0, 0);box-sizing: border-box;"><span leaf="">漏洞类型</span></span></strong></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">路径遍历</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">影响版本</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="word-break: break-all;white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">&gt;=2026.1.29-beta.1,</span><span style="box-sizing: border-box;"><span leaf="">&lt; 2026.2.1</span></span></p></section></td><td data-colwidth="25.0000%" width="25.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">修复版本</span></strong></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">&gt;=2026.2.1</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">危害等级</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""> 严重级</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞描述</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">OpenClaw 在安装第三方插件时，会直接使用插件包描述文件中的名称字段来拼接安装目录路径，但未对该字段做任何安全过滤。攻击者只需发布一个名称中包含路径跳转字符的恶意插件，当用户执行安装命令时，安装路径就会逃逸出预设目录，将文件写入系统任意位置，从而覆盖关键配置或植入持久化后门。</span></p></section></td></tr></tbody></table>  
  
  
**05**  
  
**高危漏洞核心风险提炼**  
  
  
在对近期披露的 72 个高危漏洞进行分类统计后发现，攻击面主要集中在输入处理与逻辑权限两大领域。其中，注入类攻击以 15 个漏洞位居榜首，紧随其后的是路径遍历与文件操作类漏洞（13个）以及访问控制类漏洞（11个）。这三类漏洞构成了 OpenClaw 的主要威胁源。从技术实现上看，注入漏洞多发生于后端对系统命令调用时的转义不彻底，而路径遍历则反映了系统在处理静态资源请求与日志检索时，缺乏统一的文件系统隔离（Sandboxing）机制。此外，认证类漏洞（10个）的密集出现，揭示了系统在多组件通信过程中，对于 Token 验证逻辑的实现存在显著的一致性缺陷。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzzib8tVubKu4IuiaMaTJgGAVSUY4GqlLOgibUSELU4zoaynI79ms16rf6BAkmn1YwJRkmDY72m9A9VjnaoicaRx09MyJs4wDvM0B75o/640?wx_fmt=png&from=appmsg "")  
  
图4：OpenClaw 高危漏洞类型分布  
  
我们对这些高危漏洞进行分析后发现，高危漏洞分布并非随机，而是高度集中在以下三个核心模块：  
  
● **Gateway (网关模块)**  
: 作为系统的流量入口，该模块在处理认证中间件（Middleware）时存在多处逻辑漏洞，是身份绕过类漏洞的重灾区。  
  
● **Dashboard / Control UI (管理后台)**  
: 前端展示层存在较多信息泄露风险。由于该模块需要持久化登录状态，其对 localStorage 的不当使用增加了攻击面。  
  
● **Desktop Clients (桌面客户端)**  
: 特别是 macOS 端的集成流程，在处理本地 API 调用和 URL Scheme 时，缺乏对源（Origin）的严格验证。  
  
  
**06**  
  
**防护方案**  
  
  
**一、个人用户通用防护**  
  
1. 升级版本：保持更新，升级至官方最新安全版本。  
  
1. 封堵公网暴露：确认网关绑定地址为 127.0.0.1，禁止绑定 0.0.0.0 或公网 IP，关闭非必要端口转发。  
  
1. 开启强身份认证：启用认证模块，设置强密码，禁止使用默认配置或空密码，禁止关闭设备认证选项。  
  
1. 限制 Agent 的操作能力：在配置中明确限定 Agent 只能执行低风险操作，只允许执行白名单中的系统命令、修改系统文件，防止 Agent 被恶意指令利用后对本机造成实质性破坏。  
  
1. 谨慎安装第三方技能：仅通过官方 ClawHub 渠道安装已审核技能，禁止导入来源不明的技能文件和提示词模板。  
  
  
  
**二、企业用户专项防护**  
1. 资产排查：对内外网所有 OpenClaw 实例进行全面摸底，升级或下线高危版本。  
  
1. 网络隔离：禁止实例直接暴露公网，远程访问须经 VPN 或零信任网关，配合 IP 白名单与多因素认证接入。  
  
1. 最小权限：禁止以管理员或最高权限运行，限制对核心数据库、代码仓库及云服务凭证的访问，使用专用机器人账号运行。  
  
1. 持续监控：重点监控异常命令执行、非预期外连及敏感目录访问行为，设置告警阈值，发现异常及时响应。  
  
1. 建章立制：明确 AI Agent 部署须经审批，禁止在办公网和生产网环境中未经隔离地运行，防止影子 AI 成为内网渗透突破口。  
  
1. 企业数据备份：为 AI Agent 可访问的业务系统和数据库建立独立、离线或不可篡改的数据备份机制，确保在发生数据污染或勒索事件时可快速恢复。  
  
  
  
  
**07**  
  
**行业思考与总结**  
  
  
- OpenClaw 的 258 个漏洞，不是孤立的代码缺陷，而是 AI Agent 时代安全挑战的集中爆发 —— 当前多数 AI Agent 框架都存在 “重功能、轻安全” 的问题，默认配置不安全、权限模型过于开放、信任边界模糊，给攻击者留下了巨大攻击面。  
  
- 我们将持续关注 AI Agent 领域的安全威胁，深入挖掘底层安全缺陷，及时发布风险预警与防护方案，守护个人与政企用户的数字安全。  
  
- AI Agent 是提升效率的强大工具，但前提是做好安全防护，切勿盲目跟风部署，让 AI 助手变成窃取数据、接管系统的 “内鬼”。  
  
  
  
  
参考来源：  
  
**Remote Code Execution via Node Invoke Approval Bypass in Gateway**  
  
https://github.com/openclaw/openclaw/security/advisories/GHSA-gv46-4xfq-jv58  
  
**Inbound allowlist policy bypass in voice-call extension (empty caller ID + suffix matching)**  
  
https://github.com/openclaw/openclaw/security/advisories/GHSA-4rj2-gpmh-qq5x  
  
**Path Traversal in Plugin Installation**  
  
https://github.com/openclaw/openclaw/security/advisories/GHSA-qrq5-wjgg-rvqw  
  
**openclaw Security Policy**  
  
https://github.com/openclaw/openclaw/security   
  
**ClawHavoc: 341 Malicious Clawed Skills Found by the Bot They Were Targeting**  
  
https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting  
  
**OpenClaw Malware Campaign Compromises 1,184 Software Packages and Steals SSH Keys**  
  
https://coesecurity.com/openclaw-malware-campaign-compromises-1184-software-packages-and-steals-ssh-keys/  
  
  
  
**安全KER**  
  
  
安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb55r2rFMWkRjmibsbQXdE5srqplubuqeOXIMflUfyZSgNBaXglDiasYF9PNtzHy4e1Pic2c8rW8I0ic1Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb55r2rFMWkRjmibsbQXdE5srjrTDwKKYkTK4dnBuqDa2qRdZSrgHnsErtVXpGvfwqaEch5rDHCWTpg/640?wx_fmt=png&from=appmsg "")  
  
**注册安全KER社区**  
  
**链接最新“圈子”动态**  
  
