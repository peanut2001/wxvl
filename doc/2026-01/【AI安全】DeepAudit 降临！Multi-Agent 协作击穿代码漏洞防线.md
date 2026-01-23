#  【AI安全】DeepAudit 降临！Multi-Agent 协作击穿代码漏洞防线  
原创 Oxo Security
                    Oxo Security  Oxo Security   2026-01-23 11:36  
  
# 一、 代码审计的“黑暗森林”：为什么你的扫描器总是在“人工智障”？🕵️‍♂️  
##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！  
  
知识星球 72 小时无理由退款，零成本入局，速看！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg "")  
  
在网络安全的世界里，代码审计一直是一门“玄学”。老牌的 SAST（静态代码分析）工具虽然名气大，但在实际战斗中，往往让安全工程师们叫苦连天。😭 想象一下，你打开一个扫描报告，里面密密麻麻躺着几千个“高危漏洞”，结果你花了一整周去人工核实，发现 99% 都是误报。这种被“噪音”淹没的恐惧，就是传统安全工具的现状。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c8dams0DpAChI5QMN0jg31Kc2S7lhKtDqp3kk67BG13Y7pjoiaNk9FoZvQ8h209kyOryXkPO8kv4bQ/640?wx_fmt=png&from=appmsg "")  
## 1.1 传统审计工具的“三座大山” ⛰️  
  
传统工具（如某些闭源的商业扫描器）之所以难用，核心原因在于它们缺乏**语义理解能力**  
。  
- • **误报率高到离谱：**  
 传统工具大多基于正则匹配或简单的抽象语法树（AST）匹配。只要代码里出现了 dangerouslySetInnerHTML  
 或者 exec()  
，它就疯狂报警。🚨 但它根本不知道这些函数在业务逻辑里是否被严格过滤了。  
  
- • **业务逻辑盲点：**  
 现在的项目动辄几十万行代码，跨文件调用、中间件拦截、复杂的权限校验逻辑，传统工具根本“看不懂”。它只能看到一个个孤立的点，却连不成线。🕸️  
  
- • **缺乏验证手段：**  
 扫出来的漏洞到底是真是假？能不能真的拿到 Shell？传统工具只会告诉你“这里可能有问题”，然后甩手掌柜一样让你自己去写 PoC（漏洞验证脚本）。这种“只管挖不管埋”的做法，极大地浪费了人力。  
  
### 1.2 DeepAudit 的横空出世：从“复读机”到“福尔摩斯” 🕵️  
  
这时候，**DeepAudit**  
 带着 **Multi-Agent（多智能体）**  
 架构降临了。它不是一个死板的扫描器，而是一个由 AI 组成的“审计战队”。🦸‍♂️  
  
DeepAudit 的核心逻辑是：**模拟安全专家的思维模式**  
。它不再是机械地对比规则库，而是像黑客一样去思考：  
1. 1. “这个项目的入口在哪？”  
  
1. 2. “数据流是怎么从前端传到数据库的？”  
  
1. 3. “中间有没有过滤函数？能不能绕过？”  
  
1. 4. “既然我觉得这里有注入，那我能不能写一段代码真的注入进去试试？”  
  
这种思维模式的转变，让 DeepAudit 彻底甩开了传统工具。它能理解上下文，能做逻辑推演，甚至能在 **Docker 沙箱**  
 里跑代码验证漏洞！💥  
### 1.3 战绩说话：48 个 CVE 的含金量 🏆  
  
别看它叫开源项目，DeepAudit 的实战能力简直恐怖。目前，DeepAudit 团队成员已经利用该平台在 **Zentao PMS、Dataease、Xxl-job、PowerJob**  
 等知名开源项目中累计斩获了 **48 个 CVE 编号**  
！  
  
以下是部分令人战栗的战果展示（仅为部分摘录）：  
<table><thead><tr><th style="padding: 12px 15px;text-align: left;font-weight: 600;color: #1d1d1f;border-bottom: 1.5px solid rgba(0,0,0,0.1);background: #fbfbfd;"><section><span leaf="">CVE 编号</span></section></th><th style="padding: 12px 15px;text-align: left;font-weight: 600;color: #1d1d1f;border-bottom: 1.5px solid rgba(0,0,0,0.1);background: #fbfbfd;"><section><span leaf="">受影响项目</span></section></th><th style="padding: 12px 15px;text-align: left;font-weight: 600;color: #1d1d1f;border-bottom: 1.5px solid rgba(0,0,0,0.1);background: #fbfbfd;"><section><span leaf="">漏洞类型</span></section></th><th style="padding: 12px 15px;text-align: left;font-weight: 600;color: #1d1d1f;border-bottom: 1.5px solid rgba(0,0,0,0.1);background: #fbfbfd;"><section><span leaf="">CVSS 评分</span></section></th><th style="padding: 12px 15px;text-align: left;font-weight: 600;color: #1d1d1f;border-bottom: 1.5px solid rgba(0,0,0,0.1);background: #fbfbfd;"><section><span leaf="">危险程度</span></section></th></tr></thead><tbody><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">CVE-2025-64428</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">Dataease</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">JNDI Injection</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">9.8</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">☢️ 严重</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">CVE-2025-13787</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">Zentao PMS</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">Privilege Escalation</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">9.1</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">🔴 高危</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">CVE-2025-10771</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">Jimureport</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">Deserialization</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">9.8</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">☢️ 严重</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">CVE-2025-11581</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">PowerJob</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">Privilege Escalation</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">7.5</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">🟠 中危</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">CVE-2025-9602</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">RockOA</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">Database Backdoor</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">6.5</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">🟠 中危</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">CVE-2025-13246</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">Modulithshop</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">SQL Injection</span></section></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">6.3</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">🟠 中危</span></section></td></tr></tbody></table>  
这些数字背后，代表的是 DeepAudit 对代码深层缺陷的极致压榨。它不仅仅是发现了一些“代码风格不规范”，而是直接掏出了能让系统瘫痪的“致命杀招”。💀  
# 二、 拆解 DeepAudit 的“大脑”：Multi-Agent 协作架构与五维检测矩阵 🧠  
  
DeepAudit 为什么这么强？因为它不是一个人在战斗，而是一个分工明确的**智能体集群**  
。这种架构设计参考了最前沿的 AI Agent 研究，让复杂的代码审计任务变得像流水线一样高效。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c8dams0DpAChI5QMN0jg31Ksf820QxBwJNGz0jV7r9AZLwdZOs7enD4ia7LsczvfKtrpaicDTtXNBLg/640?wx_fmt=png&from=appmsg "")  
### 2.1 四大核心 Agent 的“职场分工” 👩‍💼👨‍💻  
  
在 DeepAudit 的后端系统中，驻扎着四个各司其职的 Agent，它们通过 **FastAPI**  
 和 **WebSocket**  
 实时通信，完成一场华丽的协作。  
1. 1. **Orchestrator（总指挥/编排者）：**  
 它是战队的大脑。负责接收用户的审计任务，分析项目的技术栈（是 Java 还是 Go？是 Spring 还是 Django？），然后制定审计计划。它会把任务拆解，下发给下面的“小弟”，并汇总最终报告。  
  
1. 2. **Recon Agent（侦察兵）：**  
 负责资产识别。它会疯狂扫描项目结构，寻找所有的入口点（Entry Points），比如 API 路由、Controller、公共接口等。它会告诉团队：“兄弟们，这里有 50 个暴露的接口，咱们盯着这几个参数看！”接口多、资产乱？在它眼里都不是事。🔍  
  
1. 3. **Analysis Agent（分析师）：**  
 它是团队里的“技术大牛”。它结合了 **RAG（检索增强生成）**  
 技术，一边翻阅最新的 CWE 漏洞库，一边分析代码逻辑。它不仅仅看 AST，还会结合代码语义分析变量的生命周期。它会说：“这一段 SQL 拼接虽然看起来有过滤，但在特殊编码下其实能绕过！”  
  
1. 4. **Verification Agent（验证者/特种兵）：**  
 这是 DeepAudit 的**杀手锏**  
！它不相信空谈。当 Analysis 发现可疑点时，Verification 会在后台偷偷启一个 **Docker 安全沙箱**  
，现场编写攻击脚本（PoC），直接对代码发起攻击。只有攻击成功的漏洞，才会被列入“确认有效”的名单。这种“实战化审计”直接消灭了误报！🔥  
  
### 2.2 五维检测矩阵：全方位的代码体检 📊  
  
DeepAudit 不仅仅关注安全漏洞，它提供的是一种**全量审计**  
体验。它会对代码进行五个维度的深度扫描：  
- • **🛡️ 安全性 (Security)：**  
 挖掘 SQL 注入、XSS、SSRF、JNDI 注入等致命漏洞。  
  
- • **🐛 Bug 检测 (Bug)：**  
 发现逻辑错误、空指针异常、内存泄漏等导致系统不稳定的因素。  
  
- • **⚡ 性能优化 (Performance)：**  
 识别慢查询、冗余循环、资源未关闭等性能瓶颈。  
  
- • **🎨 代码风格 (Style)：**  
 确保代码符合行业规范，让协作更顺滑。  
  
- • **🛠️ 可维护性 (Maintainability)：**  
 识别“屎山”代码，提供重构建议。  
  
### 2.3 智能化工作流：从导入到报告的一键体验 ⚡  
  
DeepAudit 的操作流程被简化到了极致，哪怕你不是安全专家，也能轻松上手：  
1. 1. **多源导入：**  
 支持 GitHub、GitLab、Gitea 仓库一键导入，或者直接上传本地 ZIP 包，甚至粘贴一段代码片段。  
  
1. 2. **实时审计流：**  
 你可以在界面上看到 Agent 们的“对话”和思考过程。看着 AI 在那讨论“我觉得这个变量可能有问题，你去写个 PoC 试试”，这种上帝视角简直不要太爽！👀  
  
1. 3. **智能仪表盘：**  
 通过可视化图表展现项目的安全态势，漏洞分布、风险等级一目了然。  
  
1. 4. **专业报告导出：**  
 审计结束后，一键生成 PDF、Markdown 或 JSON 格式的专业报告。报告里不仅有漏洞详情，还有具体的**修复建议（How-to-fix）**  
。  
  
# 三、 硬核实测！揭秘 48 个 CVE 是如何被 DeepAudit “暴力”挖掘并自动验证的 💥  
  
🎯 **【AI 漏洞挖掘与自动化审计】**  
  
想知道 AI 是如何通过深度语义分析识破伪装的 SQL 注入的吗？当 AI 具备了自动化编写 PoC 并进行沙箱验证的能力，安全审计的门槛将发生怎样的巨变？  
  
本章节的完整技术实测、RAG 知识库增强逻辑以及针对垂域大模型的攻击理解，已完整收录于 **Oxo AI Security 知识星球**  
。加入星球，即可获取本部分的全部核心干货，助你掌握 AI 驱动的自动化审计精髓！  
  
此外，星球内部还沉淀了大量…  
- • 📚 **AI 文献解读**  
：最前沿的 LLM 安全论文深度剖析。  
  
- • 🐛 **AI 漏洞情报**  
：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。  
  
- • 🛡 **AI 安全体系**  
：从红队攻击到蓝队防御的全方位知识图谱。  
  
- • 🛠 **AI 攻防工具**  
：红队专属的自动化测试与扫描工具箱。  
  
🚀 立即加入 Oxo AI Security 知识星球，掌握AI安全攻防核心能力！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
