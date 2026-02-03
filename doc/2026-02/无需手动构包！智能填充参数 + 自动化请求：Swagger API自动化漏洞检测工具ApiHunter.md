#  无需手动构包！智能填充参数 + 自动化请求：Swagger API自动化漏洞检测工具|ApiHunter  
星夜AI安全
                    星夜AI安全  星夜AI安全   2026-02-03 00:16  
  
📌各位可以将公众号设为星标⭐  
  
📌这样就不会错过每期的推荐内容啦~  
  
📌这对我真的很重要！  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")  
  
📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。  
  
📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。  
  
📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。  
# 0x01 工具介绍  
  
Swagger 文档的未授权访问是 API 渗透测试中一个常见且高效的突破口。然而，通过人工方式手动构造请求包、逐一填充参数不仅耗费大量时间与精力，还很容易遗漏关键的接口。今天要为大家推荐的是由星球成员 @11firefly11 精心开发的开源利器——ApiHunter！这款工具正是为了解决上述痛点而设计，它支持一键解析 Swagger 2.0/3.0 文档，无需手动抓包或构建请求包，就能自动提取出所有接口的端点、请求方法以及参数定义。工具内置了超过 100 条敏感信息检测规则，能够快速捕获密钥、Token、数据库连接字符串等泄露的数据。结合其交互式重发功能，可以显著提升未授权 API 的测试效率。目前该工具已在 GitHub 上开源，旨在高效、稳定地推进数据抓取与 API 测试工作！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OQlrGt1Ax62pRX5ibbiajUkz5Quqkw9iaMX1BUx0Y5nO2hC0fGTichGAibjQ/640?wx_fmt=png&from=appmsg "")  
# 0x02 功能简介  
  
✨ 主要特性  
  
**多类型文档一键解析**  
：支持将 Swagger 2.0/3.0 JSON 文档、ASP.NET Web API Help Page 网页一键导入，自动解析所有接口端点、请求方法及参数定义，省去了手动抓包或构包的繁琐步骤，覆盖了现代前后端分离架构以及传统的 .NET 应用场景。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OmwqKZeElXENWD1JyQW1JPqWLLb0yq2AH9iaicfxADfZaXISy59jSL9og/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OftzEJ0tMyTuXicmibtYjfNW1HiaW7bgIZvNLGFj6rPzuRIRYRAcdHNbrg/640?wx_fmt=png&from=appmsg "")  
  
**智能参数填充与多格式测试**  
：针对 POST/PUT 请求，工具能自动识别 id、email 等参数并填充测试值，同时生成 URL 参数、JSON Body、Form Body 三种格式的数据包进行测试，确保对参数传递方式的全覆盖，避免漏洞遗漏；也支持用户自定义参数值，以适应个性化的测试需求。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OeQ6CAhgrknXfIjHbiazrxo2KcChRNzfzeVDibyhm30krfbpTLwicBv8bg/640?wx_fmt=png&from=appmsg "")  
  
**自动化漏洞检测能力**  
：能够智能识别 upload/file 等上传接口，自动构造 multipart/form-data 请求并上传 XSS 测试文件、普通文本文件以验证上传漏洞；内置 SQL 注入探测引擎，可以识别多种数据库的报错指纹，实现对高频漏洞的自动化检测。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OnKFyCrgziaVpBOibkkHRzFBm0AsW4w7qbnmSqicZF8gw3GwLKQzQNrydw/640?wx_fmt=png&from=appmsg "")  
  
**敏感信息深度扫描**  
：内置超过 100 条高精度检测规则，覆盖云服务密钥、各类 Token、数据库连接串、手机号/身份证等隐私信息，支持自定义规则，发现的敏感信息会在响应结果中以红色高亮展示，便于快速定位。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OC6KCV8cia5FdgZicYhjmDxhw2b9dHzGMAU1ib3qhHVicQibSHFV5zsicuYdg/640?wx_fmt=png&from=appmsg "")  
  
**智能结果去重与过滤**  
：基于“状态码 + 响应长度”的指纹进行去重，过滤掉 404/500 等重复无效的响应；支持自定义状态码过滤，可以屏蔽无价值的测试结果，从而聚焦于存在差异化的高危信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OQlrGt1Ax62pRX5ibbiajUkz5Quqkw9iaMX1BUx0Y5nO2hC0fGTichGAibjQ/640?wx_fmt=png&from=appmsg "")  
  
**安全防护与灵活适配**  
：提供“安全模式”，能够自动拦截 DELETE/PUT 等高危方法、过滤包含高危关键词的接口，防止误删数据；支持配置 HTTP/HTTPS/SOCKS5 代理，可自定义请求头（如 Cookie/Authorization），以适应鉴权场景与流量转发的需求。  
  
**交互式操作与报告导出**  
：双击测试结果即可查看标准 HTTP 格式的数据包，支持编辑请求头/请求体并即时重发；响应内容会自动格式化并高亮显示，测试结果可以导出为 Excel 格式，其中包含完整的请求与响应信息，便于生成报告或进行二次验证。  
###   
# 0x03 更新说明  
```
1. 增加 WSDL、WADL 接口文档提取以及测试功能。2. 优化 Swagger 接口提取功能。3. 优化变异测试功能。
```  
# 0x04 使用介绍  
  
📦 使用指南  
1. **启动程序**  
  
1. 双击 ApiHunter.exe  
 即可启动，开箱即用。  
  
**开始任务**  
- **方式一（单目标）**  
：输入 URL 和接口路径，点击测试。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4O7onoEVIgN9ItHpQo5gEnS9TWNs6BgNaxEGNTWOFB7jXDIbuH0vLYrg/640?wx_fmt=png&from=appmsg "")  
  
**方式二**  
：切换到“接口文档”区域，输入 Swagger/ASP.NET 地址，点击 **[导入]**  
，然后点击 **[swagger]**  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7R1Ple9xaH4dico0xLOxO4OQUhNBvKJC4bX7ancdCjlz30qlT4GDdXBYCpvZNiaBvWLrciagMwXibTRA/640?wx_fmt=png&from=appmsg "")  
1. **查看结果**  
  
1. 扫描结果会实时显示，敏感信息会以红色高亮。  
  
1. 双击某一行可以查看详情，右键点击可以进行导出或复制操作。  
  
关注微信公众号后台回复“**20260203**  
”，即可获取项目下载地址  
  
关注微信公众号后台回复**入群**  
 即可加入星夜AI安全交流群  
## 圈子介绍  
  
现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。  
  
已产出的安全工具及成果包括：  
- 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护，无感知运行，突破多引擎联合检测）  
  
- XXByPassBehinder v1.1 冰蝎免杀生成器（定制化冰蝎免杀工具，绕过主流终端防护与EDR动态检测，支持自定义载荷）  
  
- 哥斯拉二开免杀定制版（二开优化，深度免杀，突破终端防护与EDR检测，适配多场景植入）  
  
- NeoCS4.9终极版（高级免杀加载工具，强化载荷注入与进程劫持，适配多系统版本，无兼容问题）  
  
- WinDump_免杀版（浏览器凭证窃取工具，支持Chrome/Edge/Firefox等主流浏览器，一键提取敏感数据，免杀过防护）_  
  
- _DumpBrowser_V1_免杀版（浏览器凭证窃取工具，专攻浏览器密码、Cookie、历史记录提取，免杀性能拉满）  
  
- fscan二开版（二开优化内网扫描工具，增强指纹精度、弱口令爆破与结果标准化输出，适配复杂内网）  
  
- RingQ加载器二开版（二开优化免杀加载器，支持Shellcode内存执行，绕过各类终端防护与EDR检测）  
  
- 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护，适配不同Web场景）  
  
- 免杀360专属加载器（支持Shellcode内存执行，针对性绕过360全系防护检测，无感知运行）  
  
- 一键Kill 火绒 defender  
  
后续将不断更新到内部圈子中 欢迎加入圈子   
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2lEbGjW7qOx0vmIYqSQK74fiafqxfVf57bREkU77D0JbZtZHElvpCHNibbNOYeeIYCnygHbHyVuFPYA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kTp5BpCMb901r34Qsxiar69aBRExZP9U4yAnhfoP9wABkmc0DCYs7NTyicvYcBaqLxVxfAJoicMyWGQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "image")  
  
  
