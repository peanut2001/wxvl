#  AIxVuln：安研人的漏洞挖掘数字人团队  
ss0t@m4x
                    ss0t@m4x  ss0t 战队   2026-02-13 05:33  
  
# AIxVuln：安研人的漏洞挖掘数字人团队  
## 这是什么？  
  
AIxVuln 是一个基于大模型驱动的**自动化环境搭建、漏洞挖掘与验证系统**  
，多Agent同时运行并保持高效的沟通。  
  
你只需要提交一个项目的源码（Git 仓库 / 压缩包 / URL），系统就会自动组建一支**数字人团队**  
，协作完成环境搭建、代码审计、漏洞验证与报告生成——全程无需人工干预，当然你也可以随时介入指导。  
  
目前已通过该项目在真实开源项目中发现数十个漏洞。  
  
**项目地址：**  
https://github.com/m4xxxxx/AIxVuln  
## 它能做什么？  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dAwscsrrbUsksgENOmXvTTpNCHrNdVYUz38xx8jPA1rUTk4zYrKP8hGOEUGLpER9O39IjMruXXfmWfHbaDuQSykfpibtlCklTQBx33D3r84s/640?wx_fmt=png&from=appmsg "")  
  
首页  
- **一键启动**  
 — 提交源码，系统自动组建数字人团队开始工作  
  
- **全自动流程**  
 — 环境搭建 → 代码审计 → 漏洞验证 → 报告生成，端到端自动化  
  
- **单二进制部署**  
 — 所有资源（Dockerfile、前端 UI）嵌入一个可执行文件，下载即用  
  
- **多语言支持**  
 — PHP / Java / Node.js / Python / Go，自动识别技术栈并搭建环境  
  
- **实时可观测**  
 — 通过 Web UI 实时查看数字人工作状态、漏洞列表、容器信息和事件日志  
  
## 核心设计：数字人协作  
  
与传统的"单 Agent 扫描器"不同，AIxVuln 模拟的是一个**安全研究团队**  
的工作模式。  
### 什么是数字人？  
  
每个数字人拥有独立的**人格**  
（姓名、性别、年龄、性格、头像）和**能力**  
（绑定的 Agent 类型），以持久化实例运行，跨任务复用记忆。  
  
系统默认创建 9 个数字人，覆盖运维、审计、验证、报告四大职能。  
> 名字是 AI 起的，不涉及真人。用户可在「数字人管理」中自由增删改。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dAwscsrrbUu7qGUMbQrJ0e0GymGhBU3wOnDtX0FEyGn1iaMSJXsXibmzl22PqG8yIrPx2NCDnCLLDYkKpiaGlOW4QKm22c6PBgBICosicvcf40k/640?wx_fmt=png&from=appmsg "")  
  
数字人管理  
### 决策大脑（DecisionBrain）  
  
数字人团队的"项目经理"。它不直接写代码，而是：  
- **全局调度**  
 — 根据当前进度决定派谁去做什么  
  
- **状态维护**  
 — 维护环境信息、容器列表、漏洞候选列表等全局状态  
  
- **攻击链组装**  
 — 将多个碎片化的漏洞利用点（exploitIdea）组装为完整攻击链（exploitChain）  
  
- **质量把控**  
 — 对每个候选漏洞进行严格审核，防止 AI 幻觉导致的误报  
  
### 团队聊天（Team Chat）  
  
数字人之间、数字人与决策大脑之间通过 Team Chat 实时协作。用户也可以随时介入：  
- @数字人名  
 — 给指定数字人下达指令  
  
- @全体  
 — 广播给所有数字人 + 决策大脑  
  
- 直接发消息 — 与决策大脑对话  
  
以下是一次真实项目中的团队协作过程：  
  
**环境搭建阶段**  
 — Ops 数字人汇报编译问题，决策大脑给出修复指令，数字人自主执行修复：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dAwscsrrbUsIJo5a7fa7XPg8deW4fvAbuicpX2D7NJIl22acjhT8xGlRMFYQ2xdytjticfIXOxdUl1faiaDF9kWtKj8p0x76ZfJXRJL5tbsECQ/640?wx_fmt=png&from=appmsg "")  
  
团队沟通-环境搭建  
  
**用户实时介入**  
 — 用户通过 @数字人名 直接下达指令（绿色气泡），决策大脑同步协调其他数字人处理环境问题：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dAwscsrrbUvlQbjrp9JfYn4H3Gh2aEn0thibHv2qJibysiaGy4odIAGuIlmV4kQQiclaDcHoQiaoIxDgfxPM3UqBjztibhUGY7qNgSb9Ttic0icYsa8/640?wx_fmt=png&from=appmsg "")  
  
团队沟通-用户介入  
  
**决策大脑指导**  
 — 决策大脑针对 MySQL 连接问题给出详细排查步骤和重建方案，数字人据此自主执行：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAwscsrrbUtERPWy15wqEAGdU52LBGxswAwKUhTv3s2IN7rMU93Ho1HrbnjmjY6FG9BCHKZVImpejcLTvTR07u2HB9tIScWbvQveNV4Pt1U/640?wx_fmt=png&from=appmsg "")  
  
团队沟通-决策指导  
  
**多线并行**  
 — Analyze 数字人广播发现的漏洞线索，Ops 数字人同步处理依赖问题，Verifier 数字人等待环境就绪后立即开始验证：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAwscsrrbUtYl0XNJlrDBOlZTotseUYum8mFfuozaMvZpoOVbUr38CgmarEdVibVTnaSRQVibQSEPjNoyZKql8TCWfgzcUw0RXJbsZ3uxV1Xk/640?wx_fmt=png&from=appmsg "")  
  
团队沟通-多线并行  
  
**自主协作**  
 — 多个数字人同时汇报进展、分配剩余配额，用户可随时 @任意数字人 进行干预：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dAwscsrrbUscdgEjzbHcfiabXgftycBBYk0akD8uvundDCJW9Wgrol7ibeYicpnzG5ZHCQ3GoEmwOwBE3avtsQkERXkDTATt9SibyNjZkvYBdVQ/640?wx_fmt=png&from=appmsg "")  
  
团队沟通-自主协作  
## 碎片化利用点策略  
  
与传统扫描器"发现即报告"不同，AIxVuln 将漏洞挖掘拆解为**可组合的碎片化利用点**  
（exploitIdea），再逐步推进为攻击链：  
1. **Analyze 数字人**  
并行审计代码，产出多个候选 exploitIdea  
  
1. **决策大脑**  
审核每个 exploitIdea，驳回不合格的，要求整改  
  
1. 审核通过的 exploitIdea 被组装为 **exploitChain**  
（攻击链）  
  
1. **Verifier 数字人**  
在真实 Docker 环境中验证攻击链，采集证据  
  
1. 验证通过后，**Report 数字人**  
生成结构化漏洞报告  
  
### 严格审核机制 — 防止 AI 幻觉  
  
ExploitIdea 经过"审核失败 → 正在整改"等多轮状态流转，决策大脑对每个候选漏洞进行严格审核，防止 AI 幻觉导致的误报。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAwscsrrbUt0ibic0Q8trXEdwsQA3sYADyoiaL4kFcprE9spEh7Qvv3uXib4fOoqbyWicJj2W4uTUWL3B2xh2iaSzib0UFzC5K5saVJVS1UKlm4zho/640?wx_fmt=png&from=appmsg "")  
  
严格审核机制  
## 漏洞报告示例  
  
系统自动生成结构化漏洞报告，包含完整利用链分析、攻击流程图和验证证据：  
  
**完整利用链分析**  
 ：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dAwscsrrbUtoerfVu2mzwRCrdoYjG071IjajwmgvVyESMSYMJWwewCsSUVsLiaffO7jhugghrLx7vb3kj7zLTXjxYbRmPMqabJEJDMWENLmg/640?wx_fmt=png&from=appmsg "")  
  
报告-利用链分析  
  
**验证证据与 PoC**  
 — 包含时间盲注验证、UNION SELECT 探测等详细测试过程和关键证据：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dAwscsrrbUtPdn69qa3Kf8SvTajmz7uSpu0X3GfAZeStHVZry3zxuyiarNsk97bMg3HRXtjWC5iaGOic0VficTGpjNfOhbAWHgQppwrQ1BFfibq8/640?wx_fmt=png&from=appmsg "")  
  
报告-验证证据  
> 完整报告示例：AUTHBYPASS + SQLI-0.md （  
https://github.com/m4xxxxx/AIxVuln/blob/main/docs/Report-Example/AUTHBYPASS%20%2B%20SQLI-0.md  
）  
  
## 项目详情页  
  
运行中的项目详情页，左侧展示数字人工作状态与容器列表，右侧展示环境信息（登录凭证、数据库信息、路由示例等），所有信息实时更新。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dAwscsrrbUtedOlSTtClZwcDdKeB88SuyBQCnr9Y8ibeZwoU9JLDFnlZgIF8DnVSevbRoGvlfXLttacwZ1KPhmQjpIKa1DSpcXle5ic3OXsfI/640?wx_fmt=png&from=appmsg "")  
  
项目详情  
## 快速开始  
### 1. 下载  
  
从 GitHub Releases 下载对应平台的可执行文件：  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="text-align: left;background-color: #f0f0f0;border: 1px solid #e2e8f0;padding: 10px 14px;font-size: 15px;line-height: 1.6;background: #f0fdf4;color: #065f46;font-weight: 600;letter-spacing: 0.3px;min-width: 100px;"><section><span leaf="">版本</span></section></th><th style="text-align: left;background-color: #f0f0f0;border: 1px solid #e2e8f0;padding: 10px 14px;font-size: 15px;line-height: 1.6;background: #f0fdf4;color: #065f46;font-weight: 600;letter-spacing: 0.3px;min-width: 100px;"><section><span leaf="">说明</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="text-align: left;border: 1px solid #e2e8f0;padding: 10px 14px;font-size: 15px;color: #334155;line-height: 1.6;min-width: 100px;"><code><span leaf="">AIxVulnGUI-*</span></code></td><td style="text-align: left;border: 1px solid #e2e8f0;padding: 10px 14px;font-size: 15px;color: #334155;line-height: 1.6;min-width: 100px;"><section><span leaf="">桌面客户端（Wails GUI），macOS 为 </span><code><span leaf="">.app</span></code></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #f8fafc;"><td style="text-align: left;border: 1px solid #e2e8f0;padding: 10px 14px;font-size: 15px;color: #334155;line-height: 1.6;min-width: 100px;"><code><span leaf="">AIxVulnWeb-*</span></code></td><td style="text-align: left;border: 1px solid #e2e8f0;padding: 10px 14px;font-size: 15px;color: #334155;line-height: 1.6;min-width: 100px;"><section><span leaf="">Web-only 版本，适合服务器部署</span></section></td></tr></tbody></table>  
### 2. 运行  
```
chmod +x AIxVulnWeb-linux-amd64./AIxVulnWeb-linux-amd64 --mode web --port 9999
```  
### 3. 首次启动  
1. 浏览器访问 http://IP:9999  
（桌面版自动打开）  
  
1. 初始化向导 → 创建管理员账户  
  
1. 一键构建 Docker 镜像（Dockerfile 已嵌入二进制，无需额外文件）  
  
1. 在「设置」中填写 BASE_URL  
、OPENAI_API_KEY  
、MODEL  
  
1. 创建项目，开始漏洞挖掘  
  
### API 兼容说明  
  
系统支持所有兼容 OpenAI API 格式的模型服务，包括但不限于：**GPT**  
、**GLM（智谱）**  
、**Qwen（通义千问）**  
、**DeepSeek**  
 等。  
  
如需使用其他类型的模型（如 Claude、Gemini 等非 OpenAI 兼容 API），建议配合 CLI Proxy 等工具转换为 OpenAI 格式后接入。  
### LLM 配置建议  
  
系统支持按 Agent 类型独立配置不同的模型，推荐采用**分层配置**  
策略：  
- **main_setting（全局默认）**  
 — 使用 Coding 套餐模型（如 GLM-Coder、Kimi-Coder、、Qwen-Coder 等），性价比高，适合代码审计、环境搭建、报告生成等高频任务  
  
- **decision（决策大脑）**  
 — 使用更擅长决策与指导的模型（如 GPT、Codex 等），决策大脑负责全局调度与攻击链组装，对推理能力要求更高  
  
未单独配置的 Agent 类型会自动 fallback 到 main_setting  
，因此只需额外配置 decision  
 段即可实现分层。  
## 注意事项  
- 本项目会启动并控制 Docker 容器，请在隔离环境中使用  
  
- 敏感信息（API Key 等）存储于本地 SQLite 数据库，不会上传  
  
- 数字人的名字是 AI 生成的，不涉及任何真人  
  
**GitHub：**  
https://github.com/m4xxxxx/AIxVuln  
  
