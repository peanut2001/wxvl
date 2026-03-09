#  OpenClaw 近期安全漏洞、风险问题汇总  
 蚁景网安   2026-03-09 09:00  
  
<table><thead><tr style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);outline: 0px;background-color: rgb(255, 255, 255);border-top: 1px solid rgba(209, 217, 224, 0.7);"></tr></thead></table>  
0x00 前言  
  
这篇文章是针对OpenClaw近期曝出的安全漏洞、风险问题以及修复建议做的一个简单  
总结  
汇总  
，仅供参考！  
  
**0x01 OpenClaw 简介**  
  
OpenClaw（曾用名 Clawdbot、Moltbot）是一款在2026年初迅速走红的  
开源、可本地部署的AI智能体（Agent）框架  
。其核心定位是成为一个能理解自然语言并实际执行操作的AI助手，而不仅仅是进行对话。  
  
  
主要作用包括：  
- 任务自动化：  
管理邮件、日历，处理航班值机等日常事务。  
  
- 系统交互与控制：  
执行终端命令、运行脚本、浏览网页、操作文件。  
  
- 多平台集成：  
可通过 WhatsApp、Telegram、Slack、Discord 等常用通讯工具进行控制。  
  
- 能力扩展：  
拥有官方插件市场   
ClawHub  
，用户可安装各种   
Skill   
来扩展其功能，例如连接数据库、进行加密货币交易等。  
  
核心特点：  
强调数据本地处理，保护用户隐私。因其强大的“动手”能力和开源属性，曾创下一周内GitHub星标破18万的纪录。  
  
****  
**0x02 主要缺陷与不足**  
  
OpenClaw 暴露出的安全问题并非偶然，其根源在于一系列  
根本性的设计缺陷和治理不足  
：  
  
  
1. 默认配置不安全：  
- 问题：  
早期版本默认将控制界面（Control UI）绑定到 0.0.0.0（所有网络接口），而非 127.0.0.1（仅本地），导致大量实例无意间暴露于公网。  
  
- 后果：  
直接造成数万个实例可被互联网任意扫描和访问。  
  
2. 脆弱的本地信任模型：  
- 问题：  
错误地假设“来自本地的连接就是可信的”。这导致对 localhost 发起的连接缺乏必要的安全验证（如密码暴力破解防护、新设备强制确认）。  
  
- 后果：  
催生了   
ClawJacked  
 等“零点击”漏洞，恶意网站可通过用户浏览器轻松劫持本地AI助手。  
  
3. 权限边界模糊且过于宽泛：  
- 问题：  
作为高权限Agent，其设计未能严格遵循“最小权限原则”。核心组件（如Gateway）和第三方Skill往往被授予过高的系统访问权限。  
  
- 后果：  
一旦某个环节被攻破（如一个Skill），攻击者就能轻易获得系统级控制权，导致数据窃取、命令随意执行等严重后果。  
  
4. 供应链生态审核缺失：  
- 问题：  
官方技能市场   
ClawHub  
 初期缺乏有效的安全审核机制，允许任何人自由上传Skill。  
  
- 后果：  
引发   
ClawHavoc  
 大规模供应链投毒事件，大量恶意Skill伪装成有用工具，直接分发木马、窃取凭证。  
  
5. 安全治理严重滞后于功能发展：  
- 问题：  
项目在追求功能快速迭代和生态扩张的同时，忽视了同步构建安全架构和流程。  
  
- 后果：  
漏洞集中爆发，包括核心框架、MCP协议、第三方集成等多个层面均发现大量高危漏洞，形成“漏洞风暴”。  
  
6. 对新型AI攻击防护不足：  
- 问题：  
对   
提示词注入  
（尤其是间接注入）攻击缺乏有效防御。AI会信任并执行来自邮件正文、网页内容、日志文件等外部输入中的隐藏指令。  
  
- 后果：  
攻击者可通过污染信息源，间接操控AI行为，实现数据外泄或持久化后门植入。  
  
**0x03 近期安全漏洞、风险问题**  
#### 主要安全事件与漏洞  
<table><thead><tr><th style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">类别</span></span></section></th><th style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">关键漏洞/事件</span></span></section></th><th style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">核心风险</span></span></section></th><th style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">修复版本</span></span></section></th></tr></thead><tbody><tr><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">核心框架漏洞</span></span></strong></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">CVE-2026-25253（一键RCE）</span></span></strong></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">点击恶意链接即被完全控制，令牌窃取。</span></span><p><span x-noteelement="excluded" aria-describedby=":r30:"></span></p></section></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">2026.1.30</span></span></section></td></tr><tr><td style="text-align: left;"><section><span leaf=""><br/></span></section></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">ClawJacked（零点击劫持）</span></span></strong><p><span x-noteelement="excluded" aria-describedby=":r32:"></span></p></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">访问恶意网站即被静默接管，WebSocket无验证。</span></span><p><span x-noteelement="excluded" aria-describedby=":r34:"></span></p></section></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">2026.2.25</span></span></section></td></tr><tr><td style="text-align: left;"><section><span leaf=""><br/></span></section></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">日志投毒</span></span></strong></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">通过污染日志文件实现间接提示词注入。</span></span><p><span x-noteelement="excluded" aria-describedby=":r36:"></span></p></section></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">2026.2.14</span></span></section></td></tr><tr><td style="text-align: left;"><section><span leaf=""><br/></span></section></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">Endor Labs审计6漏洞</span></span></strong><p><span x-noteelement="excluded" aria-describedby=":r38:"></span></p></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">路径遍历、SSRF、命令注入等，可组合利用。</span></span><p><span x-noteelement="excluded" aria-describedby=":r3a:"></span></p></section></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">相应版本</span></span></section></td></tr><tr><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">生态与供应链</span></span></strong></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">ClawHavoc（供应链投毒）</span></span></strong><p><span x-noteelement="excluded" aria-describedby=":r3c:"></span></p></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">ClawHub中大量Skill为恶意软件，窃取数据。</span></span><p><span x-noteelement="excluded" aria-describedby=":r3e:"></span></p></section></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">平台持续清理</span></span></section></td></tr><tr><td style="text-align: left;"><section><span leaf=""><br/></span></section></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">MCP协议30+漏洞</span></span></strong><p><span x-noteelement="excluded" aria-describedby=":r3g:"></span></p></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">核心交互协议存在大量RCE等漏洞。</span></span><p><span x-noteelement="excluded" aria-describedby=":r3i:"></span></p></section></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">持续更新</span></span></section></td></tr><tr><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">部署与配置</span></span></strong></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">公网暴露（超3万实例）</span></span></strong><p><span x-noteelement="excluded" aria-describedby=":r3k:"></span></p></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">实例暴露于公网，无需认证即可访问。</span></span><p><span x-noteelement="excluded" aria-describedby=":r3m:"></span></p></section></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">需用户自行配置</span></span></strong></td></tr><tr><td style="text-align: left;"><section><span leaf=""><br/></span></section></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">企业Shadow AI风险</span></span></strong><p><span x-noteelement="excluded" aria-describedby=":r3o:"></span></p></td><td style="text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 14px;">员工私自安装，导致企业内网和数据风险。</span></span></section></td><td style="text-align: left;"><strong><span leaf=""><span textstyle="" style="font-size: 14px;">需企业策略管理</span></span></strong></td></tr></tbody></table>  
  
**0x04 综合修复与安全加固建议**  
  
✅  
 紧急措施（所有用户必须执行）：****  
1. 立即升级：  
更新至   
2026.2.25 或更高  
 的安全版本。  
  
1. 网络隔离：严禁  
绑定到 0.0.0.0。只允许本地 (127.0.0.1) 访问。远程访问必须通过   
VPN  
 或   
SSH  
 隧道。  
  
1. 审查插件：  
全面检查并卸载来源不明、可疑的   
Skill  
，只信任官方验证（Verified）项目。  
  
1. 强化认证：  
为网关设置  
高强度密码  
，并启用多因素认证（如支持）。  
  
1. 管理密钥：  
API密钥、令牌等敏感信息使用  
环境变量  
或  
密钥管理服务  
存储，禁止硬编码。  
  
🛡️  
 进阶防御（针对企业及高安全要求用户）：  
1. 沙箱隔离：  
在   
Docker  
容器 或使用   
Firejail（Linux）/ sandbox-exec（macOS）  
 中运行，严格限制其资源访问。  
  
1. 最小权限：  
创建  
专用、低权限  
的系统账户来运行OpenClaw，杜绝使用root或管理员账户。  
  
1. 纵深监控：  
部署日志审计、入侵检测（IDS/IPS）和终端防护（EDR），重点监控其网络连接和异常命令执行。  
  
1. 企业治理：  
制定明确的   
AI Agent 管理政策  
，对“非人类身份”进行审批、权限管理和生命周期监控。  
  
❌ 绝对禁止的行为：  
- 点击任何声称与OpenClaw相关的  
不明链接  
。  
  
- 在对话或Prompt中输入  
密码、私钥、API令牌  
等敏感信息。  
  
- 安装  
未经审核、来源可疑  
的Skill。  
  
- 在  
企业环境  
中未经IT部门批准私自安装和使用。  
  
  
  
**0x05 总结与思维导图**  
  
**OpenClaw 是AI Agent能力演进的一个标志性产品，但其早期版本将“功能强大”置于“安全可控”之上，导致了系统性风险。用户必须摒弃“默认即安全”的幻想，采取****主动、纵深**  
的防御策略，才能在享受自动化便利的同时，有效管控安全风险。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tNyBeBKReNImlGJl0UJk6oxak2xp9dg5B5Od0kxaXAJiawtpLeW1pyG5UhVHCWbvCqtNvMXXHxOhNFngWmAVNhPtibBbibzqmzovibNhaj2DRsE/640?wx_fmt=png&from=appmsg "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=64 "")  
  
学  
习  
网安实战课程  
，戳  
“阅读原文”  
  
