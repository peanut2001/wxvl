#  Agent时代的Web项目0day代码审计思考与实践  
原创 guchangan1
                    guchangan1  L0una   2026-03-05 08:48  
  
   
  
## 0. 前言  
  
最近都在搞各类的AI渗透、代审，也研究一阵子，给大家分享一下。这套方案目前可能并不是最优解，但在可复现性、证据完整性、工程可落地性上，已经优于大多数"提示词包装型"AI 审计工具。  
  
实际上我们**用AI以及Agent的一些概念性功能，都是为了解决现有的审计痛点**  
，而不是单纯贴一些新概念的标签博眼球（某些产品依然是提示词+前端UI）。单纯对于我个人审计来说，在目前自己的审计思路流程的基础上，主要解决的就是需要人工去参与的部分（需要花费时间去执行的步骤）。  
- • **反编译伪源码，还原代码结构**  
  
- • **审计鉴权及业务逻辑漏洞**  
  
- • **漏洞sink点追溯，sink->source还原利用链**  
  
- • **漏洞验证、报告出具**  
  
那我们可以想，这其实正好不是Agent功能的**天然分工**  
嘛？  
- • 审计逻辑漏洞、代码结构理解、调用链推理这些"**需要语义理解**  
"的事，交给**大模型**  
；  
  
- • 反编译、流程编排、报告模板、交付门禁这些"**需要稳定执行**  
"的事，交给 **Skill**  
 固化。  
  
因此就有了核心方案：**Semgrep 扛覆盖，SubAgent 扛深度，Skill 扛稳定性；在不牺牲准确性的前提下，换取更高的审计吞吐和交付稳定性。**  
  
在上年的后半年skill概念出现后就一直这么用，在今年结合了subagent，加了并发回溯增加了效率。  
  
在介绍方案之前，依然讲一下历史的一些实践。从传统 SAST，到纯 AI 审计，再到 Skill 化审计，最后落到我当前可实战的方案。  
  
**大家也可以跳到第四节直接看当前方案**  
。  
## 1. 传统 SAST  
### 1.1 能解决什么问题  
  
首先承认啊，传统 SAST 实际上没那么拉的，不是说 AI 出来了传统就完全没啥用，过时了，实际上依然适用于以下情况  
- • **企业自查/SDL/DevSecOps 场景**  
：PR 扫描、合并前扫描，高危问题能很快揪出来，起码爆出来的漏洞都能解决吧。  
  
- • **红队代审场景**  
：对于伪源码，反编译后，一般红队都会快速的SAST（比如codevulnscan、sinkfinder这种）扫一下sink点，然后自己手动跟一下，效率也还可以。  
  
只要规则配置不离谱、人工研判不偷懒，SAST 抓中高危还是能打的。  
  
这是之前写的纯正则匹配工具，虽然误报多，但覆盖面够全（实际上semgrep、codeql比纯正则好的多，起码有语义理解了，只是当时写这个的时候不知道有这俩玩意）。  
  
https://github.com/guchangan1/CodeVulnScan  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqwtMWUzXxT60tC74SkQuL1k5y06Zok3JG7QXLhJ19QJ2mE4ZbdLDlWQNR4niaaia8KOkakVGPk262AibjyVKdjzGGV5WGicyicuGtzKCxnJsMYo/640?wx_fmt=png&from=appmsg "null")  
### 1.2 核心弊端  
  
但这种方式对于内部项目长期审计的话，可能有些吃力了，主要是以下几点。  
#### 1. 数据流覆盖不全  
  
框架、组件、写法太多了，规则库永远追着跑。Source/Sink 一旦没覆盖，漏报就是必然。**人工补规则吃经验**  
，谁熟谁强，不熟就漏，而且不同人的结论可能的都不一样。本质还是"**把研究员经验硬编码**  
"，维护成本也会越来越重。  
#### 2. 极高的误报率  
- • **缺乏语义理解**  
：工具往往无法理解代码的真实运行逻辑。例如，一个漏洞 Sink  
点虽然未经过滤，但在后续逻辑中并未被用于危险操作，工具仍可能将其标记为漏洞。  
  
- • 如果你用普通的 正则 "eval(" 去搜索：  
  
- • "eval(user_input)" 能找到  
  
- • "safe_eval(user_input)" 能找到，误报（其实不是 eval）  
  
- • **漏报与误报之间的冲突**  
：为了降低漏报，默认规则往往设置得非常严格，导致大量无关紧要的告警淹没了真正的风险，安全人员不得不花费大量时间进行人工筛选。  
  
#### 3. 上下文理解能力缺失  
- • **跨服务/跨框架盲区**  
：跨服务、跨模块、依赖注入一复杂，静态链路很容易断。  
  
- • **业务逻辑盲区**  
：更根本的局限在于，**污点分析只能发现那些能被抽象为「source 到 sink 的数据流」的漏洞**  
。业务逻辑漏洞往往不涉及危险数据流，而是合法操作在错误的上下文中被执行。这些漏洞往往没有固定的代码特征，而是依附于特定的业务场景。  
  
## 2. 纯 AI 审计  
### 2.1 一些实践与检验  
  
这半年看到公众号有不少所谓"xx AI 代码审计工具"，本质上就是个**套壳GUI+提示词**  
。共同套路很简单，就是一下几步  
- • **先用 AI 搭个前端/客户端**  
；（实际上就是用AI写一个GUI（javagui的、python的）、web，你写你也能用AI在半小时内写完）  
  
- • **后端做切片 + 模型调用**  
；  
  
- • **提示词里塞满"你是资深安全专家"**  
；  
  
- • **最后吐一份看着很像回事的报告**  
。  
  
这里就不截图了，大家可自行搜索标榜AI代码审计工具的内容，体验一下就知道了。  
### 2.2 局限性与风险  
  
这类工具不亚于把代码全部丢给豆包，代码片段或者小项目里偶尔能给线索；但项目一大（模块多、依赖多、链路深）就一堆问题。  
#### 1. 幻觉问题  
- • **无中生有**  
：一本正经编漏洞链，甚至给你虚假 PoC。  
  
- • **修复建议翻车**  
：修复代码不兼容业务，甚至引入新风险。  
  
#### 2. 上下文窗口与算力限制  
- • 仓库大了只能切片喂，切完就容易丢全局。  
  
- • 全仓深读太贵，很多时候还不如"SAST 先筛 + 重点研判"。  
  
#### 3. 可复现性与性价比问题  
- • 同一份代码，不同轮次输出不一致。  
  
- • 纯 AI 全仓"通读+搜索"经常退化成昂贵 grep。  
  
#### 4. 另外最重要的伪源码问题  
  
现实里大量目标是 jar/war、反编译产物。直接丢给AI，它是不会结构还原、不会反编译联动的，审计压根覆盖不到。  
## 3. Agent + Skill  
  
Skill 火起来之后，确实解决了不少日常重复工作，这点倒是没啥争议。  
  
但代码审计场景里，现在发布的很多 Skill 还是"漏洞清单驱动"那套老路：把 SQL 注入、XSS、上传这些 Top10 拆模块，然后让 AI 按清单扫。  
  
这套做法看起来很完整，问题也很明显：  
- • 和 **SAST的能力高度重叠**  
，看过调用过程的话，应该知道，本质上都是去grep，但成本更高、稳定性更差；人家扫描工具一秒就提完了，按照你skill里写还搁那不断的重复提取。没啥必要交给AI。  
  
- • 比如一个上传漏洞，这次grep的是upload，下次grep的是fileupload，每次结果都不一样，然后你又得在提示词里把这些全部写进去。  
  
- ![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqwtMWUzXxRibObPVMUC7szibXqTgz7a5H50nTHCqPjgGn6zTuSq9zAERicp3Y0hlSOsRibXHLWZ0flQxeVKLVygbupxbic0ibJOBxW1LdhpibAPU8/640?wx_fmt=png&from=appmsg "null")  
  
所以 Skill 真正要做的，不是"多写几条提示词"，而是把流程和门禁做硬。  
## 4. semgrep快扫sink + SubAgent 并行结构化研判 +Skill完善流程  
> 原则：**AI 必须放在稳定可复现的框架里，才能持续产出价值。**  
  
  
既然纯 SAST 和纯 AI 都有硬伤，那就别二选一，直接做组合：  
- • **SAST（Semgrep）**  
：负责广覆盖、低成本起盘；  
  
- • **Agent**  
：负责研判、补链、定可利用性；  
  
- • **Skill**  
：负责流程资产化和交付标准化。  
  
### 4.1 Skill到底用在哪？  
  
**Skill 的本质是把审计动作产品化，不是把提示词写长。**  
  
真正的问题从来不是"LLM 认不认识 SQL 注入/XSS"。这些它本来就知道。 而是：**它不知道怎么像一个老安服那样，系统地把一次审计做完。**  
  
就拿正常的安服来讲，拿到项目一般来说都是这么个流程，先还原架构（一些jar需要反编译），架构分析、路由分析，再扫sink，然后根据个人经验追调用链，判可利用性，写POC，验证，出报告。 所以怎么写 Skill ，实际上就是把安服的审计方法和思路装载进去。  
  
没有 Skill，LLM 只是"懂很多"的工具；有 Skill，它才是"能稳定交付"的工程节点。  
- • **输入约束**  
：明确项目类型、语言和目录边界；  
  
- • **流程固化**  
：先做什么、后做什么。比如我这里固定的是 reconstruct → classify → scan → trace → deliver  
；  
  
- • **分配资源**  
：哪一步交给 Semgrep，哪一步交给 chain 子代理并行；  
  
- • **设置护栏**  
：什么情况必须追到底，什么情况不允许用 needs-review  
糊弄过去；  
  
- • **证据化输出**  
：证据链、POC、影响面、结论字段统一，便于复核与复盘。  
  
- • **持续迭代**  
：规则集、提示词、适配层滚动增强。  
  
### 4.2 AI/Agent到底要发挥什么作用？  
  
让 Agent 通读全仓是最容易把上下文干爆的反模式。Agent 擅长做以下的高价值动作：  
1. 1. **结构化理解**  
：识别路由/入口、鉴权位置、关键业务模块边界（把"项目地图"画出来）。  
  
1. 2. **误报/漏报确认**  
：SAST命中点并不等于可利用漏洞，通过AI解决可达性/鉴权/业务前置条件。  
  
1. 3. **链路追踪与研判**  
：以 Sink  
为起点反向追溯 Source  
，构造"可验证的调用链与证据点"。  
  
1. 4. **解决跨模块/跨服务链路**  
：真实漏洞往往在"组合调用链"里，仅靠规则很难复原，通过AI解决复杂性漏洞审计。  
  
1. 5. **告警去重与排序**  
：将大量候选命中聚类、按可利用性/影响面/鉴权要求排序。  
  
1. 6. **交付物生成**  
：将证据点固化为报告、待确认清单、API 资产、以及可复现的请求模板（例如 Burp raw 包）。  
  
### 4.3 Semgrep 在方案中的定位  
  
**1. 为什么要用Semgrep？**  
- • 审计里最该"确定性"的步骤就是基线扫描。 **基线如果交给模型随机性，后面的链路研判再强也只是补锅。**  
  
- • 用 Semgrep  
：**成熟规则直接跑，补少量自定义 sink**  
，通常不到 1 分钟就能出完整候选集。  
  
- • 用 AI实际上就是去 grep  
：先猜关键词，再扫，再开文件确认，再改关键词重扫，一圈下来半天就没了。  
  
- • 把审计规则写在 skill 里也不等于稳：模型会漏执行、执行偏、或者上下文漂移后忘了约束。  
  
- • 也考虑过codeql，都能把链路分析的事干了，但是伪源码反编译出的还原再编译可能有困难，codeql的分析也就不会很准确，这一点还在探究。  
  
2. Semgrep 在我这套方案里只干一件事：**快速、稳定产出 sink 候选点**  
。  
- • **快速覆盖已知漏洞类型**  
：对 SQLi/命令执行/反序列化/SSRF/文件上传等常见模式进行批量筛查。  
  
- • **基线产物固定化**  
：在我现有实现里，扫描会立即落地 semgrep_scan_report.md  
，只保存客观命中数据，不混入 AI 结论。  
  
- • **职责边界明确**  
：Semgrep 只负责"找到可疑点"，不负责"证明漏洞成立"。  
  
- • **后续可追溯**  
：每个候选点都会进入后续子代理分析队列，确保"从命中到结论"链路可复盘。  
  
- • **官方规则与知识库托底**  
：起点质量更高，减少低级误报。  
  
- • **新漏洞快速补齐**  
：出现新型漏洞后，能很快转成规则并回扫全仓，不靠人工逐仓重查。实际上最重要的一步是使用AI尽可能的搜罗sink点，用AI去编写规则，可以看一下目前我的规则基本涵盖了Java 的RCE漏洞类型。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqwtMWUzXxQjR3twQ1UONwZhGJMP62L6OgvmVCoFwArhqysDGynAlk77Cia0D3NOaNFoPTesvDjyMRq4M2pH6Gg2kf5b6tA63CsOT5qbI0Cs/640?wx_fmt=png&from=appmsg "")  
- • **Agent 做规则外补位**  
：跨模块链路、鉴权缺失、业务逻辑等问题由 SubAgent 研判，不把能力全压在 Semgrep 上。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HqwtMWUzXxRuPLAK0GdcrRf5icwjUfP7JtLw2sj6h6rH1ibuvTiccxSxVBlxVVP2RmsXWCFhavoKZee3F0LV7iasyPsmXgFAkohLnfTrnfkkia80/640?wx_fmt=png&from=appmsg "null")  
### 4.3 当前的 Skill 形态及审计流程  
#### Phase 1：结构还原 + 架构理解 + Semgrep 扫描  
  
**Step 1: 代码结构修复（按语言）**  
- • 这一步彻底解决伪源码的问题。以某报表为例，源码是jar包，或者jar中有jar，这里用AI的能力去识别哪些是跟业务相关的jar，然后再调用工具去反编译。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqwtMWUzXxT4iafhznp5vzla6DJI2FRHUVSBZbvExESJlcQyPuB24j6lfsVoJB6wyPnAbYTO0NAtVxILRpGggJsoSdOz2PD5r6LCOwXAt41U/640?wx_fmt=png&from=appmsg "null")  
  
**Step 2: 项目架构理解与映射**  
- • 识别技术栈与核心框架、梳理 API 路由与端点映射  
  
- • 分析认证授权机制、识别用户输入点与关键数据出口  
  
后面哪些需要鉴权、哪些不鉴权，哪些能绕过鉴权，基本上都解决了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HqwtMWUzXxTgewueAMPjK0tsYSibCAWTgqQ7JibP6iaKxNiaUojNQIjiaaQu8nBpZhws0xa10bZqFTQff13q2OsfHNNNSFXsWV96ulyvDm51mELo/640?wx_fmt=png&from=appmsg "null")  
  
**Step 3: semgrep扫描**  
- • semgrep扫描获取完整的扫描结果，扫描结果依然使用AI去做分析处理，得出完美报告，便于之后的派发。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HqwtMWUzXxTIibKRoTYSibfpZ8QAW3DeUj05ls0gT9nLyS4Zwibq3kNNoSvBRudzoOBsv5JZ7ssXN2mrS6licLnN4GibOIwyXqd6GX3YxuOw2pjk/640?wx_fmt=png&from=appmsg "null")  
#### Phase 2：主Agent按漏洞类型并行派发 subagent  
- • sec-audit-main  
（主协调器）：  
  
- • 负责 Phase 1~3 编排，执行预处理、扫描、并行派发、聚合与质量门禁。  
  
- • 主协调器只管调度和验收，避免细节把主上下文拖死。  
  
- • 子代理采用"写文件 + 单行摘要回传"，避免主上下文被结果文本淹没。  
  
- • chain-analyzer  
（链路研判）：  
  
- • 将主协调器对于semgrep扫描的结果按漏洞类型/专项域拆分后，排分给多个chain-analyzer  
并行扫描，吞吐和精度更稳定；  
  
- • 这里实际上是因为单 Agent 在大项目下很快会上下文退化，后面越审越飘；  
  
- • 以 Sink→Source  
为主线，优先用 LSP（incomingCalls/goToDefinition/goToImplementation  
），grep 仅兜底。  
  
- • auth-auditor  
（鉴权专项）：  
  
- • 负责认证、授权、对象级访问控制、过滤器绕过向量。  
  
- • 支持系统性模型缺陷识别（例如大面积端点缺失对象级校验）。  
  
- • business-logic-auditor  
（业务逻辑专项）：  
  
- • 覆盖状态机绕过、竞态、金额篡改、配额绕过等"非典型 Source→Sink"问题。  
  
- • config-secrets-auditor  
（配置与密钥专项）：  
  
- • 硬编码凭据、调试暴露、危险配置、组件版本风险提取。  
  
我当前这套实现的关键不是"多开几个 Agent"，而是解决覆盖度问题。并行是为了全，解决受限于一个上下文窗口。****  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HqwtMWUzXxTyp6K9MXR7BWKia3tV3LaHI2f7a7t1SS0fLj9bXrjmzlaZRkjeohanq6HsKvLWDrQfG7w1aGjCKg5bOQkv4f3dV8K8vhmmnD4E/640?wx_fmt=png&from=appmsg "null")  
- • 在chain审计完出完POC之后，Agent会自动拉取docker，将项目运行在docker中，进行漏洞POC验证。实际上非常简单，你都没必要刻意写任何过程，告诉他这么干就行了。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HqwtMWUzXxQykUBjgVsgwd7dj5biaibaQy5mzdtI6JibrrA2aXoS8R8fyiaQkBsdzfOFjA8jUJTE8AydZ4WxkJW9y3CK8bTjbbQheQ38pw0azFM/640?wx_fmt=png&from=appmsg "null")  
#### Phase 3：主Agent聚合结果，清零待定项  
  
当然了，为避免还没审完提前结束，也有控制措施，会穷尽 Pending 清零  
- • 收集所有 needs-review  
状态发现，重新派发 chain-analyzer with force_decision=true  
  
- • 验收标准：audit_pending.md  
中 needs-review  
条目数 = 0  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HqwtMWUzXxT6Z8g9Rjxib1E6lDGQiaHAHFGzibqdfk4a9Z8LTric9wXgeYqN9E8EiaIVvibm89RwRx7Kf93qENwbNTVTQ7dfJLQQSykmRgiaKH7USA/640?wx_fmt=png&from=appmsg "null")  
  
  
漏洞详情就不放了，基本上都是所谓的"0day"，包含具体的漏洞分析步骤以及POC。  
#### Phase4：质量保证与验证  
- • 从原始 Semgrep 结果中提取所有 severity: CRITICAL  
的命中（按 check_id  
列出）  
  
- • 逐条核查：每个 CRITICAL check_id 必须在 audit_final.md  
（confirmed  
）或 audit_pending.md  
（dismissed  
/likely-fp  
）中有对应记录  
  
- • **任何 CRITICAL 命中若无对应处置记录，则禁止输出"审计完成"**  
；必须重新派发 chain-analyzer 追踪缺失项后才能收尾  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HqwtMWUzXxScLXj6ZGMRgVqqfRQHrwnqXkdxypicrniawhU8zUB2a4ribM86SU7ThFL1EbBPL0k9koaXTHz6enbibzYhEbiaKOJuyfwia6cIpCeRQ/640?wx_fmt=png&from=appmsg "null")  
  
### 4.4 当前的局限性  
  
不是说，这一套方案就很完美了，实话说，还是有以下这些问题待解决。  
  
1. **上下文与 Token 上限**  
1. • 项目大、漏洞多、链路深时，AI也会偷懒，直接不给你跑了  
；如下是我最开始在没有设置门禁的时候，AI就会偷懒直接干后面的活了。Ps：目前通过上下文压缩解决了Token上限的问题，代价是可能会丢失准度，但编排好的话应该问题不大。或许还有更好的方案解决这个问题。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/HqwtMWUzXxQQXInTg90GicXqdvFooOgOTvLj3N7uqqjbanBFwsffgqpolw8ymYA7IV3M9KiaUWs07U6eRn1RdAskibLroFzzQbOu4r8Rb8Eqv8/640?wx_fmt=png&from=appmsg "null")  
  
2. **多代理并行带来治理成本**  
1. • 子代理多了，去重、归因、排序难度直线上升；  
  
• 调度不严，结果就会"看起来很忙，价值不集中"。  
  
3. **LSP/反编译质量会直接影响结论置信度**  
1. • 索引不全、反编译可读性差、依赖缺失时，链路质量会下滑；  
  
• 虽然能用 grep 兜底，但精度和效率都会损失。  
  
4. **流程纪律决定最终质量**  
1. • 这套方法吃流程执行力：落盘、门禁、复核缺一步都可能翻车；  
  
• 如果执行打折扣，输出稳定性就会明显下降。  
  
## 5. 总结与展望  
  
但现在的成果，即便是一个零代码基础的小白，用这套方案，只需要把代码丢进去，就能出0day，大大降低了代码审计的核心门槛：懂代码。你不懂代码没关系，AI懂啊。  
  
噢对，token问题的话，我这里用的订阅，合下来一个中型报表或者cms项目，大概1刀的样子。  
  
但当前方案不是终局，最多算一次工程化初探，不是未来最优形态。我相信目前已经有团队实现了更好的审计方案，本方案仅供参考，需完善的点也可以互相交流。  
  
如果未来模型能力显著增强，或者上下文问题被真正解决（长上下文稳定 + 外部记忆可靠 + 多轮推理不退化），那我现在这套方案，在未来可能会是个笑话，所以只能算是当前阶段的一个**权宜之计**  
？  
  
注：因为内容大部分手写，文笔也不是很好，  
文章里可能有很多细节可能没有怎么提到，欢迎评论进行交流。后续有时间的话单独拆分每一步的细节逻辑。  
  
   
  
