#  大海捞针：用 LLM 进行漏洞研究  
devansh
                    devansh  securitainment   2026-03-13 02:36  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://devansh.bearblog.dev/needle-in-the-haystack/</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">devansh</span></section></td></tr></tbody></table>  
**注意:**  
最初我打算用一篇文章涵盖完整方法论及所有技术细节，包括 AI 驱动的差分 fuzzing 与基于语法的 fuzzing、自动化 harness 生成及相关工作流。但后来我意识到，把所有内容塞进一篇文章会显得过于密集且难以跟读。  
  
因此，本文作为系列的第一篇，提供方法论的高层概述和该方法背后的核心思路。后续文章将深入探讨各组件的技术细节与实现方式。  
  
本文所有内容仅供教育和研究用途。任何利用本文信息进行的滥用或恶意行为，责任完全由行为人自行承担。  
  
---  
## 前情提要  
  
过去几周，我报告了一批安全问题。其中一小部分漏洞已修复并以安全公告的形式公开披露。这些漏洞全部通过 LLM 发现，没有进行任何手动源代码审计。涉及的项目都相当知名且被广泛使用，包括 Parse Server、HonoJS、ElysiaJS、Harden Runner 等十余个知名项目。  
  
我认为这足以证明，像 OpenAI Codex 这样的 agentic CLI 和 TUI 工具完全有能力帮你发现严重漏洞。但问题是：我们究竟该如何使用这些工具来发现那些隐蔽的漏洞？在发送了成千上万条 prompt 之后，我得出了一些结论。这些结论可能不够理论严谨，但却是我在实践中总结出的最务实的经验。  
  
我发现，最容易遗漏重要漏洞的几种做法是：  
1. 通过链式 prompt 对安全审计进行过度编排  
  
1. 臃肿的 AGENT.md/SKILLS.md 文件  
  
1. 以文档形式提供过多上下文，或预先规划流程的每一步  
  
1. 试图编排过多的环节  
  
但这听起来有悖直觉，不是吗？正常人都会觉得引导越多结果越好，对吧？然而长上下文系统存在一个经过充分研究的真实问题：当你往上下文窗口中塞入越来越多的 token 时，模型准确提取关键细节的能力会下降。近期研究将这一现象明确称为 **上下文腐烂 (context rot)**  
——即使新增的内容在技术上确实相关，随着上下文长度增长，模型性能也会变得越来越不稳定。安全审计恰恰是这个问题的最坏场景：那根 "针" 往往只是一个微妙的不变量违反，隐藏在数千行正常代码之中。根据我的测试，模型在很多情况下表现出首因/近因效应——当关键的 "针" 靠近上下文的开头或结尾时表现较好，埋在中间时则明显变差。这就是 needle-in-the-haystack 问题最纯粹的体现。  
  
那么我们该怎么办？是不是应该删掉 AGENTS.md，让 LLM 在没有任何引导的情况下自由发挥？那样会带来更多问题，不过那是另一个话题。就目前而言，基于我在多个流行开源项目中发现十余个 CVE 的测试和经验，我总结出的要点是：最小化的持久引导框架、最大化的定向探索与验证，以及一个让模型注意力始终锚定在关键问题上的工作流。  
  
---  
## 为什么 "找出所有漏洞" 行不通  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSia3eDlhGtDUxI8ExiaHyAicthpicn3t1HOtKu70oicqic8y7x4Fuib5UOyS9H5OdMeKSzwia2GuRJu9iaT8wgA6tUxnNo9eUalCusza6O8/640?wx_fmt=png&from=appmsg "")  
  
  
假设你有一个包含大量单体源代码的文件夹，或者你刚从 GitHub 克隆了一个仓库，现在想从中找出安全漏洞。你打开 Codex，输入一句 "找出这个代码库中的所有漏洞"。这条 prompt 会因为两个可预见的原因而失败。  
- 你在提交 prompt 时没有指定任何威胁模型。这导致 LLM 对影响程度毫无概念。它确实可以自行推导出某种威胁模型，但根据我的实验，它通常不会这样做，或者做得非常粗糙。没有合理的威胁模型、信任边界、攻击者能力和前置条件，你得到的结果只会是一长串泛泛的类 CWE 可能性列表，毫无优先级可言。你根本无法从这堆噪声中筛选出真正有价值的发现。  
  
- 第二个原因是，这条 prompt 会将模型推入广度优先的幻觉模式。宽泛的 prompt 必然招来宽泛的回答。模型会通过模式匹配去寻找常见的 bug 类别，哪怕这些 bug 在你的代码上下文中根本不可能存在。最终你会发现自己在审查一堆理论上的漏洞，而这些漏洞所在的代码路径根本没有攻击者能够触及。  
  
---  
## 真正有效的最小引导框架  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgB2KRZvE5SibQfEian5cCd44fXXaq71gmoL427ZEIQZu8moe8ay1BdZeYfBADAZU2ep3nnYh8297Y249NJQNYaEibEWhBd2Sgiahs/640?wx_fmt=png&from=appmsg "")  
  
  
看过模糊 prompt 带来的问题后，我们来试试正确的做法。在让 LLM 审计代码寻找漏洞之前，先做人类安全团队会做的事——建立威胁模型。这同样可以借助 LLM 来完成。  
  
我通常的做法是，先查找该项目此前已披露的 CVE，然后将这些 CVE 的描述喂给 LLM，让它基于这些历史记录为合理的 bug 类别生成一个威胁模型。  
  
举个例子，如果之前披露的 CVE 涉及堆溢出、栈溢出、整数溢出和内存破坏，LLM 就会针对这些类型的漏洞来构建威胁模型——因为这些漏洞此前已被项目方认定为有效的安全问题。  
  
接下来，把你刚生成的威胁模型文档喂给 Codex，让 LLM 查找其中的不变量，或者去寻找修复这些漏洞的 commit 并尝试发现绕过方式。相比模糊的 prompt，这种方式更有可能为你带来真正的漏洞。  
  
在这个过程中，你做的唯一引导工作就是创建了一个威胁模型。我们没有制作任何 skills.md 或 agents.md 文件，也没有试图编排大量流程。你只是创建了一个威胁模型并交给 LLM，然后它就会在代码库中进行深入研究，尝试找到符合该威胁模型的漏洞。  
  
在完成与已披露 CVE 同类漏洞的搜索之后，接着可以识别入口点——例如 HTTP 路由、RPC handler、消息消费者、CLI 入口点和定时任务。识别信任边界——例如浏览器到服务器、服务到服务、插件到宿主、沙箱到特权。识别高风险操作——例如反序列化、模板渲染、原生绑定、授权检查和不受信任输入的解析。并明确声明攻击者-受害者模型，例如你想要发现可由远程未认证用户、远程已认证低权限用户或跨租户用户触发的漏洞。  
  
这就是那种在不膨胀上下文窗口的情况下提升信号质量的小型结构。威胁建模是安全审计的终极压缩算法。  
  
最重要的——或者说唯一重要的——是先构建系统上下文，然后创建一个可编辑的威胁模型。随着安全审计的推进，不断扩展和完善它，持续添加新发现，最后利用这个威胁模型来确定发现的优先级并进行验证。  
  
---  
## 案例研究：Claude Opus 4.6 与 Firefox  
  
Anthropic 2026 年 3 月 6 日的文章描述了与 Mozilla 的一次合作：Claude Opus 4.6 在大约两周内发现了 22 个漏洞，Mozilla 评估其中 14 个为高危。Mozilla 自己的文章确认了这一结果，并强调了它在实践中之所以有效的原因——报告附带了最小测试用例，使复现和修复得以快速推进，团队随后将这项技术从 JS 引擎扩展到了浏览器的其他部分。  
### Anthropic 实际做了什么  
  
Anthropic 的做法并不是 "写了一个巨型 prompt"，而更接近于以下描述。他们从代码库的一个聚焦切片——JavaScript 引擎——入手，因为它是核心组件且可以独立分析。他们进行了快速迭代：Claude 在大约 20 分钟的探索后发现了一个 use-after-free，由人类完成验证后提交了一份带有候选补丁的 Bugzilla 报告。在工作流证明有效后，他们进行了规模化扩展，最终扫描了约 6,000 个 C++ 文件并提交了 112 份独立报告，大部分修复收录于 Firefox 148.0 (2026 年 2 月 24 日发布)。  
  
这种方法一定正确吗？也许是，也许不是。事实上，Anthropic 发现的许多漏洞必然有无效的。他们需要报告可利用的漏洞，而要找到可利用的攻击向量，就必须从潜在漏洞出发，经过验证，再确认其可利用性。这条链路的成本非常高——Anthropic 为此花费了大约 $4,000 的 API 额度。我们在审计代码时能花这么多钱吗？大概不能。但我们面对的代码规模有 Firefox 那么大吗？同样没有。  
  
Anthropic 几乎没有使用任何引导框架就完成了这项工作。但我想倡导的是进行最小化的引导——先创建威胁模型、描述信任边界。而且以上讨论仅限于漏洞发现环节，我并未涉及漏洞评估和误报消除。这些方面也有相应的方法和途径，但那可能是另一篇文章的话题。就目前而言，如果创建威胁模型后 LLM 发现了一些漏洞，你可以指示 Codex 编译源代码后运行本地实例，或者编写测试来证明漏洞的存在。大多数情况下这种方式是有效的。  
  
---  
## 我的方法论  
  
最小化引导框架已经足够有效，它能帮我们发现远比模糊 prompt 更多的漏洞，甚至包括一些陷阱行为和边缘情况。我想通过自己最近的工作来说明这一点——在大约两个月内，我在多个不同项目中发现了超过 30 个漏洞。  
  
---  
### 审计方法  
  
每次审计的起点都一样：选择一个狭窄的切片，在让 LLM 查找漏洞之前先理解它的信任模型。  
#### Parse Server  
  
详细分析：Parse Server 中的四个漏洞  
  
Parse Server 是一个开源后端框架，提供 REST API、实时查询、推送通知和云函数。它支持多种认证机制，包括一个 readOnlyMasterKey  
，文档承诺它将授予 master 级别的读取权限但拒绝所有写入操作。  
  
在让 LLM 寻找任何问题之前，我先调取了 Parse Server 此前已披露的 CVE。过往的安全公告显示了一个反复出现的模式——授权执行失败：权限检查存在但不完整，或在各个路由 handler 间的应用不一致。我将这些 CVE 描述喂给 LLM，要求它基于这些历史记录为合理的 bug 类别生成威胁模型。模型将授权边界执行确定为主要风险类别，考虑到 Parse Server 具有多种不同权限级别 key 类型的架构，这是合理的。  
  
该威胁模型将 readOnlyMasterKey  
标记为一个值得关注的信任边界。其声明很简单：一种 key 类型应该比另一种严格具有更少的权限。我将 LLM 的注意力指向这个边界，让它探索不同 key 类型如何与授权层交互、代码对权限分离做了哪些假设，以及这些假设可能在哪里被打破。  
  
LLM 返回了一份攻击面地图，突显了一个模式：多个路由 handler 通过 isMaster  
来控制访问，但从未检查 isReadOnly  
。这就是信号。我随后用一个更窄的 prompt 跟进，要求它枚举所有展现此模式的 handler，并追踪只读凭证是否可以通过其中任何一个触及写入或状态变更操作。  
  
四个漏洞中的三个 (CVE-2026-29182、CVE-2026-30228、CVE-2026-30229) 都源于同一根因。确认这些后，我打开了一个新的切片，针对社交认证适配器采用类似的引导方法。我将 LLM 指向认证适配器层，让它探索 token 验证流程——检查了哪些 claim、配置部分缺失时会发生什么、以及验证可能在哪里静默降级。LLM 将 JWT audience 验证路径标记为薄弱点，后续 prompt 确认了第四个发现——CVE-2026-30863，一个独立的 JWT audience 验证绕过，当配置不完整时适配器会静默跳过 aud  
claim 检查。不同的切片，相同的方法。  
  
---  
#### HonoJS  
  
详细分析：HonoJS JWT/JWKS 算法混淆  
  
HonoJS 是一个轻量级、高性能的 JavaScript 和 TypeScript Web 框架，可在多种运行时上运行，包括 Cloudflare Workers、Deno、Bun 和 Node.js。它内置了 JWT 和 JWKS 认证中间件。  
  
我先审查了 Hono 过往的安全公告以及其认证中间件中此前已披露的问题。CVE 历史记录 (尽管已披露的 CVE 非常少) 加上整个生态系统中 (其他项目中) JWT 实现错误的普遍模式，在我要求 LLM 构建威胁模型时，将其引向了算法处理这一高风险领域。模型将算法混淆和默认回退行为标记为最可能的 bug 类别，这给了我一个明确的切片——JWT 和 JWKS 验证路径。  
  
有了这个威胁模型，我引导 LLM 探索 JWT 中间件中的算法选择逻辑。我没有询问某个具体缺陷，而是让它走查当开发者没有完美配置时会发生什么——哪些默认值会生效、存在哪些回退路径、中间件如何决定信任哪个算法。目标是让 LLM 梳理出算法选择的决策树，并标记出中间件可能做出不安全假设的分支。  
  
LLM 在分析中发现了两个令人担忧的模式。第一，当没有显式指定算法时会回退到 HS256。第二，当 JWK key 对象缺少 alg  
字段时，JWKS 中间件会转而采用 token 中 header.alg  
的值。我对每个发现分别进行了定向 prompt 跟进，要求 LLM 追踪攻击者可以在哪些确切条件下利用这些回退行为。  
  
两个算法混淆问题随之浮出水面。CVE-2026-22817 是 JWT 中间件在未指定算法时默认使用 HS256，允许攻击者将公钥作为 HMAC 密钥来签名 token。CVE-2026-22818 是 JWKS 中间件在 JWK 缺少 alg  
字段时回退到不受信任的 header.alg  
值，让攻击者可以决定服务器用于验证的算法。  
  
---  
#### ElysiaJS  
  
详细分析：ElysiaJS Cookie 签名验证绕过  
  
ElysiaJS 是一个为 Bun 构建的 TypeScript Web 框架，注重类型安全和开发者体验。它内置了 cookie 处理功能，支持基于签名的完整性验证和密钥轮换。  
  
威胁模型生成遵循了同样的模式。我查阅了 ElysiaJS 的文档。当我将相关上下文喂给 LLM 并要求它识别可能的 bug 类别时，它将签名验证逻辑标记为高风险领域，尤其是密钥轮换路径——在该路径中多个签名密钥可能同时有效，验证逻辑必须正确拒绝与所有密钥都不匹配的 cookie。  
  
这给了我一个窄切片。我将 LLM 指向 cookie 签名和验证层，让它推理验证过程中的状态管理——代码如何跟踪签名是否已成功验证、当遍历多个轮换密钥但没有一个匹配时会发生什么、是否存在初始化假设可能导致逻辑静默接受无效签名。  
  
LLM 将 decoded  
状态变量标记为可疑，并指出了它的初始化方式。我基于这个信号进行跟进，让它追踪当没有任何密钥能产生匹配签名时的控制流。这确认了这个 bug：一个布尔值初始化错误——let decoded = true  
而不是 let decoded = false  
——意味着在使用密钥轮换时签名验证检查永远不会失败。CVE 尚在处理中。  
  
---  
#### harden-runner  
  
详细分析：绕过 harden-runner 的出站连接检测  
  
harden-runner 是 StepSecurity 开发的 GitHub Actions 安全工具，通过对 syscall 进行插桩来监控 CI/CD runner 的出站网络连接，以检测未经授权的出口流量。它有两种运行模式：审计模式记录连接，阻断模式则主动阻止连接。  
  
我审查了 harden-runner 此前的安全公告及其文档中描述的安全模型。该工具的全部价值在于对出站网络活动的完整可见性，因此我要求 LLM 生成的威胁模型围绕一个核心问题展开："在 GitHub Actions runner 上拥有代码执行能力的攻击者，能否绕过出口控制将数据外泄？" LLM 将 syscall 覆盖范围的缺口确定为最可能的绕过方式，理由是该工具通过 hook 特定的系统调用来工作，而任何不在监控范围内的调用都将是不可见的。  
  
基于这个威胁模型，我将 LLM 指向 syscall 监控层，让它探索覆盖面。哪些类型的 syscall 被 hook 了？一个进程在 Linux 上可以通过哪些不同方式通过网络发送数据？这两者之间是否存在缺口？目的是让 LLM 枚举完整的网络相关 syscall 集合，然后与 harden-runner 实际插桩的部分进行比较。  
  
LLM 返回了一份缺口分析，将 UDP send 系列 syscall 标记为可能未被监控。我进一步追问，让它验证 sendto  
、sendmsg  
和 sendmmsg  
中具体哪些被覆盖了。绕过方式恰恰如威胁模型所预测的那样：这些 syscall 在审计模式下不在监控范围内 (CVE-2026-25598)。  
  
---  
#### BullFrog  
  
详细分析：绕过 BullFrog GitHub Action 的出口过滤、BullFrog GitHub Action 中的 sudo 限制绕过、利用共享 IP 绕过 BullFrog 的出口过滤  
  
BullFrog 是另一个用于 GitHub Actions 的安全工具，它通过 DNS 感知规则应用防火墙级别的出口过滤。与 harden-runner 的 syscall 插桩方式不同，BullFrog 在网络层运行，将域名解析为 IP 地址并基于这些解析结果应用防火墙规则。  
  
我遵循了同样的流程。审查了 BullFrog 的文档和安全模型，然后要求 LLM 基于其架构方式生成威胁模型。核心问题与 harden-runner 相同——"在 GitHub Actions runner 上拥有代码执行能力的攻击者，能否绕过出口控制将数据外泄？"——但由于 BullFrog 的执行机制根本不同，LLM 识别出了一组不同的可能绕过类别。威胁模型将 DNS 解析的边缘情况、IP 与域名的绑定逻辑以及权限提升标记为三个最可能的攻击面。  
  
我将审计分成三个独立的切片，每个都有各自的引导探索。对于 DNS 切片，我将 LLM 指向 DNS 解析层，让它探索 agent 在协议层面如何处理 DNS 流量、它对消息边界做了哪些假设、以及在多路复用或流水线消息等边缘情况下会发生什么。对于 IP 切片，我让 LLM 探索 DNS 解析后防火墙规则是如何构建的、域名与其解析 IP 之间的绑定关系是否被跟踪、以及当多个域名解析到同一地址时会发生什么。对于权限切片，我让 LLM 查看该工具如何限制 runner 上的权限提升，以及除了它显式阻止的路径外是否存在其他获取提升权限的途径。  
  
LLM 为每个切片都发现了具体的攻击面：DNS 解析器只检查 TCP 段中的第一条消息、防火墙在白名单中添加 IP 时未将其与触发域名绑定、Docker 组成员资格在 sudoers 被移除后仍然保留。对每个发现的后续 prompt 确认了这三个不同的绕过方式。  
  
---  
#### Better-Hub  
  
详细分析：入侵 Better-Hub  
  
Better-Hub 是一个 GitHub 替代前端，它在自己的源中镜像 GitHub 内容，将 Markdown 渲染为 HTML，并持有用于认证功能的 GitHub OAuth token。  
  
这里的威胁模型更多来源于架构本身而非过往 CVE (因为没有任何先例)。当我向 LLM 描述 Better-Hub 的设计——具体来说，用户控制的 GitHub 内容在 Better-Hub 自己的源中渲染，而 OAuth token 在同一上下文中可用——威胁模型几乎是不言自明的："当用户控制的内容在拥有存储凭证访问权限的上下文中被不安全地渲染时，会发生什么？" LLM 确定了三个高风险领域：Markdown 渲染管线、缓存和授权层、以及 OAuth token 处理逻辑。  
  
我将每个领域作为独立切片进行审计，采用引导探索而非特定漏洞搜索的方式。对于渲染切片，我将 LLM 指向 Markdown 处理管线，让它探索数据流——来自 GitHub 仓库的原始内容在到达浏览器之前经过了怎样的转换、存在哪些清洗步骤、以及不受信任的输入可能在管线的哪个环节存活下来。对于缓存切片，我让 LLM 检查响应是如何被缓存和服务的、缓存层是否感知认证上下文、以及当另一个用户请求来自私有仓库的缓存响应时会发生什么。对于 OAuth 切片，我让它探索 token 的存储和作用域机制、它们是否可从客户端上下文访问、以及 token 的生命周期是怎样的。  
  
每个切片都产生了与 LLM 所识别的攻击面清晰对应的发现。渲染管线产出了六个 XSS 变体，全部源于同一个未经清洗的 Markdown 渲染路径。缓存切片揭示了两个基于缓存的授权绕过——私有仓库内容泄露给了未认证用户。其余发现包括一个私有 prompt 数据泄露、一个客户端 OAuth token 暴露和一个开放重定向。三个切片总共发现了 11 个漏洞。  
### 发现的漏洞  
  
注意：以下仅为我使用本文所述方法发现的漏洞中的一小部分，许多漏洞仍在等待修复/披露  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">目标</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">漏洞数</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">严重性范围</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">关键 CVE</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Parse Server</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">4</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Critical - Moderate</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">CVE-2026-29182, CVE-2026-30228, CVE-2026-30229, CVE-2026-30863</span></section></td></tr><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">HonoJS</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">2</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">High</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">CVE-2026-22817, CVE-2026-22818</span></section></td></tr><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">ElysiaJS</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">1</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">High</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Pending (cookie signature bypass)</span></section></td></tr><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">harden-runner</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">1</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Moderate</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">CVE-2026-25598</span></section></td></tr><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">BullFrog</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">3</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">High</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">DNS pipelining, sudo bypass, shared-IP bypass</span></section></td></tr><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: rgb(248, 248, 248);margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Better-Hub</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">11</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Critical - Low</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">XSS chain, cache deception, OAuth leak</span></section></td></tr></tbody></table>### 为什么这种方法有效  
  
这些审计没有一个使用了巨大的清单、20 页的 prompt 引导框架或全面的安全框架。每一个都从一个简短的威胁模型开始——通常一句话就能表达——以及一个直接对应信任边界或安全关键操作的代码库聚焦切片。引导框架是最小化的，但它是 正确的  
引导框架。它引导 LLM 精确地知道要测试什么不变量、在哪里查找。  
  
---  
## 最佳平衡点  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjnOxMtHqcGvicm2plMlfYFXz78pFAX1n0WDEtWlVcPESYqOKaLvUDgptsPm7rpgoBuWdsqBr7K82Rd9QcAR1MJNocbLHSk1eUg/640?wx_fmt=png&from=appmsg "")  
  
  
好的引导框架是一页威胁模型、一份简短的核心功能清单、以及一小组不变量，如 "只有管理员可以调用 X" 和 "JWT 签发者必须是 Y"。坏的引导框架是一份 20 页的 Agent.md (包含每条策略和风格指南)、一个庞大的 Skill.md 库 (预加载了每份安全检查清单)、以及每轮对话中重复的模板化指令。如果你的引导框架本身变成了干草堆，漏洞就成了那根针——而关于长上下文性能的研究表明，干草堆越大，针越容易被遗漏。  
  
将审计拆分为与真实攻击面匹配的薄切片。选择一个切片，如认证、会话管理、请求解析、文件上传、反序列化、沙箱边界或插件边界。让模型将该切片的入口点映射到敏感的 sink。要求提供证据——确切的调用链、守卫条件、不变量以及哪些输入是攻击者可控的。  
  
不要依赖 "模型说它有漏洞"。使用任务验证器，如单元测试和集成测试、sanitizer 构建和崩溃复现 harness (针对原生代码)、fuzzer (即使是轻量级的)、静态分析和基于 grep 的不变量检查、以及策略检查如 "授权必须保护这些端点"。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgbSAbJEWdD93pR8haJbRHleI0aPibcVrl3A8U4r2sA4MI5xB7IhLpI40iauQicwnvXfruoFERO15ZXvB7QoXGZiaGTcquxic2t7Tqs/640?wx_fmt=png&from=appmsg "")  
  
  
把 token 花在覆盖率和验证上，而不是 prompt 官僚主义上。一个实用的经验法则是：不超过 10% 的 token 预算用于稳定的引导框架 (威胁模型和不变量)，60-80% 用于聚焦上下文中的切片审计，20-30% 用于验证循环——证明、复现、精简和修补。  
  
---  
## Prompt 注入  
  
找到正确的切片并构建威胁模型可以让你进入正确的范围。但一旦到了那里，你向 LLM 表述 prompt 的方式对于最终得到的是一份泛泛的观察列表还是一个真正可利用的发现有着巨大的影响。在数十次审计中发送了数千条 prompt 之后，我发现某些 prompt 模式始终优于其他模式。我称这些为 "prompt 注入"，因为你正在向模型的推理过程中注入一个框架、一种偏向或一个约束，从而将其行为引向有用的方向。以下是我认为最有效的技巧。  
  
**断言漏洞存在。**  
这是我发现的最有效的单一技巧。当我告诉 LLM "这个函数肯定有漏洞，至少有 2 到 3 个安全问题" 时，其分析质量相比询问 "这个函数有漏洞吗？" 有了显著提升。原因很直接：LLM 有很强的默认趋向于附和和肯定。当你问 "这有漏洞吗？"，模型阻力最小的路径是回答 "这看起来总体安全，有一些小问题"，然后给你一份理论问题列表。当你断言漏洞存在时，你翻转了模型的优化目标。它不再是在评估 bug 是否存在，而是在搜索它被告知存在的 bug。它会更仔细地阅读代码，考虑它原本会跳过的边缘情况，并产出具有真正针对性的发现。本质上，你绕过了模型充当令人安心的代码审查者的倾向，迫使它进入一个知道 bug 就在那里、只需要找到它的人的心态。即使你事先没有理由认为该函数确实有漏洞，这种技巧也依然有效。  
  
**要求漏洞利用，而非评估。**  
与其问 "这个输入验证是否足够？"，不如要求 "写一个绕过这个输入验证的概念验证请求"。这迫使模型产出具体的、可测试的输出，而非用定性评估来推诿。当模型必须实际构造一个恶意 payload 时，它不得不逐步推理代码如何处理该输入、检查在哪里、以及如何绕过。如果验证确实是健全的，模型将难以产出有效的 payload，并且经常在生成过程中意识到它正在尝试的绕过行不通——这本身就是有用的信号。如果验证是有缺陷的，你得到的是一个可用的 PoC，而非一段说 "这可能不够充分" 的话。  
  
**将模型定位为对手，而非审计员。**  
框架的选择比大多数人预期的更重要。"你是一名安全审计员，正在审查这段代码" 和 "你是一名红队操作员，你被雇来攻破这个应用，你需要找到真实的、可利用的 bug 来证明你的参与价值" 会产生根本不同的输出分布。审计员框架使模型偏向完整性和全面性——这听起来不错，但实际上会产出大量低信号的观察列表。红队框架使模型偏向影响力和可利用性。它开始思考攻击者实际上能获得什么、需要什么前置条件、以及一个发现是真实的还是理论上的。对抗性框架还使模型更愿意探索令人不安的结论，比如 "这个认证机制从根本上就是坏的"，而不是将发现软化为 "这里可以改进"。  
  
**使用虚假锚定来制造搜索压力。**  
这是断言技巧的变体。告诉 LLM "我已经在这个模块中找到了一个漏洞，但还有其他我没找到的。它们是什么？" 这创造了一种微妙的社会证明压力。模型会推断，如果你——一个人类——已经找到了一个 bug，那么这段代码确实有问题，它应该更努力地寻找。这也改变了模型的先验假设：不再从 "这段代码可能没问题" 开始，而是从 "这段代码有已确认的 bug，因此存在更多 bug 的概率更高" 开始。我发现这在你确实已经找到一个 bug 并想看看同一模块是否有更多时特别有效。在这种情况下锚点是真实的，但即使锚点是虚构的，这种技巧也依然有效。  
  
**反转问题。**  
与其问 "这段代码安全吗？"，不如问 "你会如何攻破它？" 这种反转看似微不足道，但从根本上改变了模型的任务。"这安全吗？" 是一个是/否分类问题，模型的默认倾向是 "是"。"你会如何攻破它？" 是一个没有简单默认答案的生成问题。模型必须产出攻击策略，这要求它从攻击者的角度思考代码。我发现反转 prompt 比非反转等价物多产出 2-3 倍的可操作发现，因为模型无法通过说 "这看起来没问题" 来满足 prompt，它必须真正去尝试。  
  
**分解为不变量然后违反它们。**  
要求 LLM 先列出一个函数为正确运行所依赖的每一个不变量、假设或前置条件，然后让它检查每一个是否真正成立。例如："列出这个认证函数对其输入、环境和调用者所做的每一个假设。现在，对于每个假设，告诉我攻击者是否可以违反它。" 这种两步分解之所以有效，是因为它将枚举任务与评估任务分开了。当列出假设是模型的唯一任务时，它做得很好。当每次只需要考虑一个假设是否成立时，它的推理也很好。将两者合并到一个 prompt 中通常会产出肤浅的结果，因为模型试图同时做所有事情并且会过早满足。  
  
**假设开发者犯了错。**  
将你的 prompt 构造为 "假设开发者在这个函数中引入了一个 bug，它是什么？" 这与断言漏洞存在不同。断言技巧告诉模型 bug 就在那里，而这个技巧告诉模型假设开发过程不完美，从而转变了它对代码质量的先验假设。LLM 有一种将代码合理化为正确的倾向——当它们看到一个模式时，通常会假设它是有意为之的，并基于这个假设向前推理。告诉模型假设犯了错可以打断这种合理化过程。它开始寻找不合理的地方，而非解释为什么一切都说得通。ElysiaJS 的 let decoded = true  
bug 就是一个完美的例子。一个合理化代码的模型可能会说 "开发者初始化为 true 是有原因的"；而一个寻找错误的模型则会立即将其标记为错误的初始值。  
  
**使用对比 prompt 与已知安全模式进行比较。**  
让 LLM 回答 "这个实现与该模式的标准安全实现有何不同？" 这利用了模型的训练数据，其中包含了数千个常见模式 (如 JWT 验证、会话管理、CSRF 防护等) 的正确和错误实现示例。通过让模型比较代码实际做的和安全版本应该做的之间的差异，你让模型进行结构化比较而非开放式审查。这对加密和认证代码特别有效，因为通常只有一种正确方式但有许多错误方式。当你明确要求模型寻找偏差时，它非常擅长发现与规范实现的差异。  
  
**用 "还有呢？" 进行迭代升级。**  
在 LLM 给出第一轮发现后，不要认为它已经完整。用 "那些是显而易见的。有哪些更微妙的、容易遗漏的问题？" 或 "把与 [已发现的 bug 类别] 相关的一切放在一边。这里还存在哪些其他类别的漏洞？" 来推进。这之所以有效，是因为 LLM 会优先输出最高概率的补全内容。你首先得到的发现是模型最有信心的那些，通常也是最显而易见的。微妙的 bug——那些需要更深层推理或不寻常攻击模型的——是较低概率的补全，模型不会生成它们，除非你明确推动它超越表面层。每一次 "还有呢？" 都将模型推向其分布的尾部，而有趣的发现往往就在那里。我通常会进行 2-3 轮，之后信号开始衰减。  
  
**明确约束攻击者模型。**  
与其笼统地说 "找漏洞"，不如指定确切的攻击者模型："你是一名远程未认证攻击者，只能向公开 API 发送 HTTP 请求。你无法访问文件系统、数据库或任何内部服务。找出你仅通过公开 API 就能提升权限或造成危害的所有方式。" 这个约束有两个重要作用。第一，它消除了一整类误报——模型不会报告 "拥有数据库访问权的攻击者可以修改这个表"，因为你已经明确排除了这种情况。第二，它迫使模型在约束内进行创造性思考。当攻击者模型宽泛时，模型会走最简单的路径，报告最强大的攻击向量。当攻击者模型狭窄时，模型必须更加努力地寻找可行的攻击路径，而那些更难发现的路径恰恰是现实中攻击者会利用的——因为它们正是防御者所忽略的。  
  
---  
## 参考资料  
- Anthropic: 与 Mozilla 合作提升 Firefox 的安全性  
  
- Mozilla: 通过 Anthropic 红队加固 Firefox  
  
- OpenAI: Codex Security: 现已进入研究预览  
  
- Mozilla: Firefox 148 中修复的安全漏洞, MFSA-2026-13  
  
- Chroma Research: 上下文腐烂: 增加输入 Token 如何影响 LLM 性能  
  
- arXiv: 迷失在中间: 语言模型如何使用长上下文  
  
- Devansh: Parse Server 中的四个漏洞  
  
- Devansh: HonoJS JWT/JWKS 算法混淆  
  
- Devansh: ElysiaJS Cookie 签名验证绕过  
  
- Devansh: 绕过 harden-runner 的出站连接检测  
  
- Devansh: 绕过 BullFrog GitHub Action 的出口过滤  
  
- Devansh: BullFrog GitHub Action 中的 sudo 限制绕过  
  
- Devansh: 利用共享 IP 绕过 BullFrog 的出口过滤  
  
- Devansh: 入侵 Better-Hub  
  
---  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
