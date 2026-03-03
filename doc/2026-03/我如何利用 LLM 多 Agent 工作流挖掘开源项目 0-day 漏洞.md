#  我如何利用 LLM 多 Agent 工作流挖掘开源项目 0-day 漏洞  
Hyunseo Shin
                    Hyunseo Shin  securitainment   2026-03-03 05:38  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://blog.cykor.kr/2026/02/How-I-Found-Open-Source-0-days-with-an-LLM-Multi-Agent-Workflow</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Hyunseo Shin</span></section></td></tr></tbody></table>## 创建 LLM Agent 工作流的动机  
  
此前，我在大学的网络安全学习主要围绕 wargame 和 CTF 展开。在受控环境中挖掘漏洞并成功利用固然有趣，但我始终有一个愿望——在"真实世界"中发现漏洞。  
  
加入 BoB (Best of the Best，韩国网络安全培训项目) 第 14 期漏洞分析方向后，我深刻意识到安全行业的范式正在发生转变。导师们指出，AI 的攻击能力正在飞速提升，未来将接管安全领域的大量工作，并强调高效运用 AI 将成为黑客不可或缺的核心技能。AI Cyber Challenge (AIxCC) 的出现更让我确信，"AI for Security" 即将成为主流趋势。随着 AI 从简单的 Web UI 聊天机器人进化到 Claude Code、Codex 等 CLI 工具，MCP 的问世，以及 AI 模型在漏洞赏金平台上拔得头筹，这一信念愈发坚定。  
## 目标选择  
  
起初，我考虑过内存损坏漏洞和黑盒服务器漏洞赏金这两个方向，但出于现实考量最终转向了其他目标。  
- **内存漏洞：**  
我为内存损坏类漏洞搭建了专门的工作流，确实发现了一些 OOB (越界) 和栈溢出崩溃。然而，像 Google OSS VRP 这类项目很少接受单纯的崩溃报告——它们要求提供能够完全破坏完整性或机密性的利用链。受限于安全策略与合规要求，用 AI 自动化这一过程目前仍十分困难。加上我的技术背景偏向 Web 安全而非二进制利用 (pwn)，因此在这个方向上并不具备竞争优势。  
  
- **黑盒服务器漏洞赏金：**  
我暂时搁置了这个方向，原因是 AI 在执行漏洞扫描时可能不够安全——发送激进的 payload 有导致服务器崩溃或瘫痪的风险。(像 Theori 旗下的 Xint  
或美国的 xbow  
这类公司可能掌握了安全操作的方法，但我目前还达不到那个水平。)  
  
最终，我将目标锁定在我最熟悉的大型 Web 开源项目上，如 Nextcloud、Matomo 和 Grafana。这些项目的源码完全公开透明，可以通过 Docker 轻松在本地搭建复现环境，而且我相信 LLM 的上下文理解能力在发现人类容易忽略的复杂业务逻辑漏洞方面能够大显身手。  
## 架构  
  
我尝试了多种工作流方案，但目前主要使用的两套工作流具有相同的核心结构："漏洞发现"与"误报验证"两个阶段被严格分离。其核心思路并非在整个流程中使用昂贵的模型，而是在每个阶段将数据高效地路由到合适的模型。![AIxCC.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nShIN4pH8uWzPDULFaGsAWzW6BjTZPFVLAGxcnruDykQWTWkSWYN82KSibu0YDZNpJcAAAjnMFqIFzoekbibOzfPuFiafxicBdYU2ib8/640?wx_fmt=jpeg&from=appmsg "")  
这一架构的灵感来源于 Theori 在 AIxCC 中展示的 'RoboDuck' 方案。尽管 RoboDuck 采用了 fuzzing (会消耗更多 token)，但看到其每小时成本可能超过 1000 美元后，我意识到：要想实现可持续运行，不能对所有环节都使用最顶级的模型，而需要根据实际需求灵活搭配。  
  
在对比各种低成本 LLM 的基准测试时，我在 GeekNews 上偶然发现了一篇关于 GLM 模型的文章，其性价比似乎非常出色。在 GLM 系列中，新发布的 GLM-5 性能比 GLM-4.7 高出约 20%，但 token 消耗量是后者的三倍。由于 Web 漏洞往往需要检测 IDOR 之类的逻辑缺陷，而非高度复杂的推理，我判断提高廉价模型的调用频率比使用略优但昂贵的模型更为高效。因此，我选择性价比突出的 GLM-4.7 作为主力模型。![AIbench.png](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjpv5eoG6lLhTiczrWx0J8fWsibAVV58GAjibd0XTiclogO4woicwx7nXVAPuxhRos9OmxH2Vbzickj4fibOfuztVzsnc2EW91FITMaqw/640?wx_fmt=png&from=appmsg "")  
各模型的 Coding Index 基准测试  
- **Finding (GLM-4.7)：**  
搜索漏洞候选项。我通过调整此发现阶段的 prompt 创建了多个工作流变体。  
  
- **Semi-Triage (GLM-5)：**  
使用性能优于 GLM-4.7 的 GLM-5，从第一步产生的候选项中过滤掉明显的误报。  
  
- **Triage (Codex 5.3)：**  
经过前两轮筛选存活下来的候选项，交由顶级模型 Codex 5.3 进行最终验证。  
  
通过 Triage 阶段验证的漏洞会通过 Discord 发送告警通知，并将漏洞报告上传至 Notion。  
  
在审阅上传的报告后，我始终会在提交之前亲自手动复现并验证每个漏洞。由于即便经过 Codex 的验证仍可能残留误报，最终报告严格基于我的手动复现结果撰写。  
## Prompt 工程  
  
工作流运行初期，误报数量相当多，为此我反复实验和优化了各种 prompt 来解决这一问题。  
  
大多数误报的产生是因为以下三个要素中的某一个被评估有误。因此，我必须强制 AI 在验证阶段逐一审查这三个因素：  
1. **攻击者条件：**  
攻击者需要处于什么网络位置 (内部/外部)，需要具备什么权限 (Unauth/Admin/Guest)，以及需要注入哪些特定输入才能使攻击成功。  
  
1. **服务器条件：**  
服务器端的前置条件，例如是否需要启用特定插件、默认配置如何，或者该漏洞是否仅在特定操作系统/环境下才会触发。  
  
1. **安全影响：**  
不能仅笼统地说"存在危险"，而要基于 CIA 三元组具体说明——是否会导致数据窃取、引发拒绝服务 (DoS)，还是仅仅造成简单的信息泄露。  
  
许多人试图通过在 prompt 中"请求" AI 来解决这个问题，比如 "请在分析时考虑攻击者的权限"  
或 "请注意服务器配置。"  
然而，LLM 本质上是"懒惰"的。像"考虑""注意"这类模糊指令，在推理过程中很容易被跳过或草草带过。而通过强制 AI 在输出中显式列出这三个要素，它就不得不对每个要素进行系统性分析，从而大幅减少了由此类因素导致的误报。  
  
解决了上述三个问题后，一种新的误报类型又浮出水面：在源代码层面看似漏洞，但实际上是特定开源项目安全模型下的预期行为或不在评估范围内的 bug。为此，我更新了 prompt，要求 AI 搜索该项目的官方安全文档和安全策略，以判断其究竟是真正的漏洞还是设计如此。  
  
经过这一系列优化，工作流能够清晰区分 bug  
与 _漏洞_，漏洞分析工作流的误报率显著降低。  
## 发现的漏洞  
  
这个项目带给我的一个切身体会是：AI 在发现 IDOR 和业务逻辑漏洞方面的能力令人惊叹。传统扫描器只能追踪数据流，而 AI 能够理解"上下文"——即 API 的设计意图以及其应当遵循的安全模型。  
  
如果由人类来手动执行这类分析，需要将数万行 API 路由代码与权限引擎的复杂交互逐一交叉比对。这不仅极为耗时，而且当人类审阅数千个参数时，注意力不可避免地会逐渐衰退，极易遗漏关键的缺失检查。相比之下，AI 永远不会疲倦，它能系统性地将每个 API 定义与安全模型进行交叉验证，在捕捉人类容易忽略的微妙逻辑漏洞方面展现出压倒性的优势。  
  
最具代表性的案例是我借助此 LLM 工作流在 Grafana 仪表盘权限管理 API 中发现的权限提升漏洞 (CVE-2026-21721)。![grafana\_cve.png](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSianN7ARKIIm4PpiawrPkjAysgEibxTwiaz9uCgicONTa4hXiaLu7cJdq2VT8PiaSU42HQUib5LdNNgeBIdKDA05o0MvGB3NUbt5Y5Vvxo/640?wx_fmt=png&from=appmsg "")  
  
### 描述  
  
Grafana 允许为每个仪表盘单独设置权限 (Read/Write/Admin)。在正常的安全模型下，用户应当仅能对自己被指定为"权限管理员"的特定仪表盘调用权限控制 API。  
  
然而，AI 发现的漏洞在于：Grafana 的仪表盘权限 API (GET/POST /api/dashboards/uid/<uid>/permissions  
) 未对目标仪表盘的 Scope 进行校验。  
- **根因：**  
在调用内部权限验证逻辑 ac.EvalPermission  
时，未将目标仪表盘的 UID scope 作为参数传入，而仅检查了用户是否拥有 dashboards.permissions:read/write  
操作权限。这意味着，只要用户对系统中 任意一个  
仪表盘拥有 Admin 权限，便可获得执行 dashboards.permissions:write  
操作的有效权限。由于服务器不校验该权限所指向的 _具体仪表盘_，攻击者便能读取或篡改其原本无权访问的所有其他仪表盘的权限数据。  
  
### 影响  
  
这是一个严重的权限提升漏洞：拥有某一特定仪表盘管理员权限的用户，可以任意劫持组织内其他敏感仪表盘的控制权。通过将自己设为其他仪表盘的 Admin，攻击者能够完全访问此前无法触及的数据。  
  
最终，该漏洞被分配编号 CVE-2026-21721 (CVSS 8.1)。在审计大型代码库的全部权限时，追问 "为什么这里没有将 UID scope 作为验证参数传入？"  
这种细节，人类安全工程师很可能会不经意间忽略，而 AI 却精准地捕捉到了安全引擎中的这一逻辑不一致。  
### 其他 0-day 漏洞  
  
**Bug Bounty 与 CVE**  
- CVE-2025-66514, CVSS 5.4 / **nextcloud mail**  
中的 XSS 漏洞, (已获赏金)  
  
- CVE-2025-66558, CVSS 3.1 / **nextcloud twofactor_webauthn**  
中的认证缺陷, (已获赏金)  
  
- CVE-2026-0994, CVSS 8.2 / **protobuf**  
中的 DoS 漏洞  
  
- CVE-2026-21721, CVSS 8.1 / **grafana**  
中的权限提升漏洞, (已获赏金)  
  
- CVE-2026-22922, CVSS 6.5 / **airflow**  
中的特权 API 误用, (已获赏金)  
  
- 待分配的 CVE…  
**Bug Bounty (未分配 CVE)**  
- **Nextcloud Contacts**  
(预发布版), CVSS 6.5 / nextcloud contacts 中的 IDOR 漏洞, (已获赏金)  
  
- **Matomo**  
, 通过 HackerOne 报告的安全问题, (已获赏金)  
  
- **Matomo Official plugins**  
, 通过 HackerOne 报告的安全问题, (已获赏金)  
  
- **Matomo Official plugins**  
, 通过 HackerOne 报告的安全问题, (已获赏金)  
  
- **Matomo Official plugins**  
, 通过 HackerOne 报告的安全问题, (已获赏金)  
  
- **Grafana**  
, 通过 Intigriti 报告的安全问题, (已获赏金)  
  
- **Owncloud**  
, 通过 YesWeHack 报告的安全问题, (已获赏金, CVE 待分配)  
  
- **Discourse**  
, 通过 HackerOne 报告的安全问题, (已获 8 笔赏金, CVE 待分配)  
  
新发现的 0-day 漏洞将在我的 博客 About Me  
部分持续更新。  
## 未来展望  
  
在亲自使用 AI 工作流挖掘漏洞的过程中，一个更深层的问题在我脑海中逐渐成形："如果 AI 已经如此强大，未来还有我的容身之处吗？"  
距离我正式步入职场还有三年多，届时这个世界大概率已遍布远超当下水平的 AI。  
  
虽然我对安全行业尚未有全面了解，但我个人的判断是：红队中简单的漏洞发现工作将大幅减少。主流趋势可能转向 AI 在开发流程中实时执行安全诊断以预防性地拦截漏洞，同时由 AI 漏洞分析 Agent 主动出击寻找 bug。红队不会完全消失，但我相信 AI 将接管他们目前承担的大量手工任务。  
  
然而，我并不认为人类的角色会完全消亡。为发现的漏洞制定修复策略使其贴合业务场景，或者建立和运营企业独有的安全体系，这些领域无论 AI 多么先进，都离不开人类的讨论和决策。  
  
因此，我计划将未来的学习聚焦于两个主要方向：  
- **AI for Security：**  
学习设计和构建类似本项目的漏洞猎取 AI 工作流。  
  
- **Blue Team 与安全架构：**  
超越纯粹的攻击 (红队) 技能，深入理解现实企业的安全策略与基础设施。  
  
当然，以上仅仅是一名安全专业学生的个人推测，而非行业资深人士的判断。但比起抵抗扑面而来的 AI 浪潮，我相信最先学会高效驾驭这一工具的黑客，将拥有显著的优势。  
  
---  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
