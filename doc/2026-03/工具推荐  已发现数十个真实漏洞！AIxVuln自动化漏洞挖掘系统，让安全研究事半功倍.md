#  工具推荐 | 已发现数十个真实漏洞！AIxVuln自动化漏洞挖掘系统，让安全研究事半功倍  
星夜AI安全
                    星夜AI安全  星夜AI安全   2026-03-02 00:26  
  
📌各位可以将公众号设为星标⭐  
  
📌这样就不会错过每期的推荐内容啦~  
  
📌这对我真的很重要！  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")  
  
📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。  
  
📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。  
  
📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。  
  
**背景介绍**  
  
AIxVuln 是一个集成了大语言模型（LLM）、工具调用（Function Calling）与 Docker 沙箱的**自动化漏洞挖掘与验证系统**  
。  
  
该系统通过 Web UI 或桌面客户端来管理“项目”，为每个项目自动组织多名**数字人**  
 协作完成任务，包括环境搭建、代码审计、漏洞验证和报告生成。所有操作均在隔离的 Docker 环境中进行，涵盖依赖安装、服务启动、PoC 验证以及证据采集，最终生成可供下载的漏洞报告。  
  
目前，该系统已在真实开源项目中成功挖掘出数十个漏洞。  
## 工具特性  
- **首次启动引导**  
 — 初次运行时，系统会自动进入初始化向导，引导创建管理员账户并一键构建所需的 Docker 镜像，实现开箱即用。  
  
- 单二进制部署 — 所有资源，包括 Dockerfile 和前端 UI，均已嵌入可执行文件中，无需额外文件即可运行。  
  
- 项目化管理 — 支持通过 Git 仓库、压缩包上传或压缩包 URL 三种方式创建项目，可一键启动或取消任务，并实时查看漏洞列表、容器状态、事件日志与报告。  
  
- 数字人协作 — 每个数字人都具备独立的个性设定（姓名、性别、年龄、性格、头像及自定义提示词），并绑定特定的 Agent 能力类型。它们以持久化实例运行，可在不同任务间复用记忆。  
  
- 决策大脑（DecisionBrain） — 作为全局调度中枢，它维护状态面板与记忆体，自动编排数字人工作，汇聚碎片化的利用点（exploitIdea）并组装成完整的攻击链（exploitChain）。  
  
- 团队聊天（Team Chat） — 用户可通过 @数字人名  
 或 @全体  
 与任意数字人或决策大脑实时对话。数字人之间也可以通过 TeamMessage 机制广播消息。  
  
- Docker 沙箱与多语言环境 — 内置 aisandbox  
 攻击沙箱，支持 PHP、Java、Node.js、Python、Go 等多种运行环境，以及 MySQL、Redis 等中间件。  
  
- 双 API 模式 — 支持 OpenAI Chat Completions API 和 Responses API，并可按 Agent 类型独立配置。  
  
- SQLite 配置管理 — 配置信息存储在 data/AIxVuln.db  
 中，首次启动时自动生成默认值。可通过 Web UI 进行可视化编辑，并支持按 Agent 类型独立覆盖配置。  
  
- 报告模板自定义 — 报告模板存放于 data/.reportTemplate/  
 目录下，支持直接在 Web UI 中编辑。  
  
- 桌面客户端 — 基于 Wails 框架构建了跨平台桌面应用（位于 wailsapp/  
 目录），其中内嵌了前端 UI。  
  
## 界面预览  
### 首页 — 项目管理与创建  
  
支持通过 Git 仓库、压缩包上传或压缩包 URL 三种方式创建项目，并可一键启动漏洞挖掘任务。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaGmk0xg3yz0vBk41xuCsqFxax34Mybns3nu5iawTIQJnobhLfOscmQxssib73trXKw0GGh48LRm4uGjtdEt23txNAgoR3iaiaiavib5c/640?wx_fmt=png&from=appmsg "")  
### 项目详情 — 实时状态总览  
  
运行中的项目详情页。左侧展示数字人工作状态与容器列表，右侧显示环境信息（如登录凭证、数据库信息、路由示例等）。所有信息均实时更新。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHZdjqKcY9bC5jnUt50TAm1jEnP4C2bMbCy4wk2eHrQGUTnpoYLBXtrCLh0FDeicc26TNY0micRdhX2qmib9NeoAdkJzxZkVp4myU/640?wx_fmt=png&from=appmsg "")  
### 数字人管理  
  
用于管理 Agent 数字人角色。每个数字人都有独立的个性设定（姓名、性别、年龄、性格、头像）和自定义提示词，并绑定特定的 Agent 能力类型。支持对数字人进行增删改操作，修改后需要重启项目才能生效。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaE9L2PersPRyO00w2aXBUguqYTzxOkf5mN5tSSD3bxBWsEicH7d2pVRCYBgKBocN6rJ0ib2ArncqUkvwXtkHmBU6HXyibFJP8jPiaA/640?wx_fmt=png&from=appmsg "")  
### 严格审核机制 — 防止 AI 幻觉  
  
ExploitIdea 会经历“审核失败 → 正在整改”等多轮状态流转。决策大脑对每个候选漏洞进行严格审核，以防范因 AI 幻觉导致的误报。ExploitChain 组装完成后，同样需要经过验证流程。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaElKoWQKUznFcuQT65so6JGm5PA583crpZUWT9s5c6y0nf5afHTopIOsjrZumv4aOUQ6TZ62jOVZbYVz4xKaMSqZ9OHVaXfPfg/640?wx_fmt=png&from=appmsg "")  
### 高效的团队沟通机制  
  
数字人之间、数字人与决策大脑之间通过 Team Chat 实现实时协作。以下展示了一次真实项目中的多轮沟通过程：  
  
**环境搭建阶段**  
 — Ops 数字人汇报编译问题，决策大脑给出修复指令，数字人自主执行修复：![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaFYW2bAdkLWgnStL3O3lgEUqIheWKgjfJgJhDHBUu6MnYjpdSV8BgbIa9btMaUNfbsiaOv4D2ol6JSsgLJRbeLPNYAHUsyK3p94/640?wx_fmt=png&from=appmsg "")  
  
  
**用户实时介入**  
 — 用户通过 @数字人名 直接下达指令（绿色气泡），决策大脑同步协调其他数字人处理环境问题：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaG0u6PurZbeSUtuqbM8vMafx7Yibc0FFQSIs76NicZXfKjicJwJGsaxXebzKzWzlNib6ULW1yibPsfqrHq3xLTyM3Hdbe5YNodFJAwU/640?wx_fmt=png&from=appmsg "")  
  
**决策大脑指导**  
 — 决策大脑针对 MySQL 连接问题提供详细的排查步骤和重建方案，数字人据此自主执行：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaGbaCKcAUCbOHgrEDVetDjcRYkvbc0SO7aicZHh2mqn05RbcS91Qa3318RibeSuVX7tHn4oN9I4w00PhlZn2GFugg0uHamX69abk/640?wx_fmt=png&from=appmsg "")  
  
**多线并行**  
 — Analyze 数字人广播发现的漏洞线索（@all），Ops 数字人同步处理 Maven 依赖问题，Verifier 数字人则在环境就绪后立即开始验证：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHQuLzX8N7WxWZZKRGBXficTXtqI0vXQwxBxOVQibwSSBMa6Ribn4k4stfVSIIsgUBVfwibibHUWKRMM87rkrvPwXvNIcmjn7ibF2HYU/640?wx_fmt=png&from=appmsg "")  
  
**自主协作**  
 — 多个数字人同时汇报进展、分配剩余配额，用户可随时 @任意数字人 进行干预：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHrx0qNM1dxXT9Aiat50MtDTYbibLuUiaseFHq76q8uIU9RKCL52ic4Sd8YcHKGV6kibLnllMic6HDl7jvOiasAvNCF6ohVPleHEicIJlM/640?wx_fmt=png&from=appmsg "")  
### 漏洞报告示例  
  
系统自动生成结构化的漏洞报告，包含完整的利用链分析、攻击流程图和验证证据：  
  
**完整利用链分析**  
 — 自动绘制从攻击入口到最终危害的完整调用链路图：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaG0OzGb6VFS5o6WnKkbwRn3sDP7J13OGmdBVGWGbkv8Tn0WSbLgiccV4gSrEgdQKkwF25SGRE6DyDe2P8Y0padQrrawS35Khco4/640?wx_fmt=png&from=appmsg "")  
  
**验证证据与 PoC**  
 — 包含时间盲注验证、UNION SELECT 探测等详细测试流程和关键证据（HTTP 请求/响应）：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaFJbgCDlymKHouawJCaMPXdE173zl1mial6FFJC9rZSmiaFR3XzvKfTjgt99GqUF0UAwUg6nWXcuoG5AdC9MicyArcPDyRyqfX4F4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12 "")  
  
关注微信公众号后台回复“**20260302**  
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
  
- 一键Kill 火绒 defender 工具 **HDKiller**  
（包含源码）  
  
- win11 一键kill 360工具 **InjectKill**  
（包含源码）  
  
- win11 一键kill defender工具**win11_df-killer**  
（包含源码）  
  
- 免杀火绒6.0内存防护加载器**BypassMemLoader**  
  
后续将不断更新到内部圈子中 欢迎加入圈子 ![image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2nhghttp9mQhic3LJWsCj8Jb4QWibnjmRqic7M9W746srJZlLKQg6mmV7cKrwhWCOauLlJPzLzry0iaRQ/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=7 "image")  
  
  
