#  大海捞针：Openclaw如何革新漏洞挖掘新范式  
原创 骨哥说事
                    骨哥说事  骨哥说事   2026-03-11 08:17  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf="">声明：</span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf="">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></h1></td></tr></tbody></table>#   
  
#   
  
****# 防走失：https://gugesay.com/archives/5408  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg "")  
  
## 引言  
  
我在过去几周报告了一系列安全问题。其中一小部分漏洞现已修复并以安全公告形式披露。所有这些漏洞都是**100%使用LLMs（大语言模型）**  
 发现的，没有进行任何手动源代码审查。我发现这些漏洞的项目相当知名并被广泛使用。其中一些项目包括像 Parse Server、HonoJS、ElysiaJS、Harden Runner 这样的大名，以及其他十几个知名项目。  
  
我认为这证明了基于AI的CLI/TUI（如OpenAI Codex）无疑可以帮助你发现严重的漏洞。但我们究竟如何利用这些工具来发现隐蔽的漏洞？基于我的测试，以及为了发现这些漏洞发送了成千上万条提示后，我得出了一些结论。这些结论可能在理论上不够精确，但这是基于实践得出的一些最具实用性的结论。  
  
我发现，以下一些做法会让你最快地错过重要漏洞：  
1. 通过链式提示过度搭建安全审计的脚手架。  
  
1. 冗长臃肿的 AGENT.md  
/SKILLS.md  
 文件。  
  
1. 以文档形式给予过多上下文，或预先规划好每一步流程。  
  
1. 试图进行过度的编排。  
  
但这听起来违反直觉，不是吗？任何理智的人都会认为指导应该意味着更好的结果，对吧？但长上下文系统存在一个非常真实且经过充分研究的问题。当你向上下文窗口塞入更多Token时，模型提取正确细节的可靠性会下降。最近的研究明确将此描述为**上下文腐化**  
，即使添加的内容在技术上是相关的，随着上下文长度的增加，性能也变得越来越不可靠。安全审计是这种情况的最糟糕环境。那个“针”往往是一个违反不变性假设的微妙之处，埋藏在数千行合法代码之中。根据我的测试，我发现，在许多情况下，模型表现出首因效应/近因效应，当相关的“针”位于上下文开头或结尾附近时表现更好，当它埋在中间时表现更差。这就是最纯粹的大海捞针问题。  
  
那我们该怎么办？我们应该抛弃我们的 AGENTS.md  
 文件，让LLM在没有脚手架的情况下随意运行吗？这会导致一些更大的问题，但这是另一个话题了。目前，根据我在广受欢迎的开源项目中发现的十多个CVE所积累的测试/经验，我所确定的是：窍门在于**最小化的持久脚手架、最大化的针对性探索与验证**  
，以及一个能**将模型注意力锚定在关键之处的工作流**  
。  
## 为什么“找所有漏洞”行不通  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZg1GkREmVwWeV5of6TIr65BzsK7r8cTSibvUDZulTa6kuib9PEp9Oic8oCKhhkp8YlbCOrv7cUZ8e42aNfujRv4feU7rG3UqOwLNY/640?wx_fmt=other&from=appmsg "")  
  
  
假设你有一个包含单体式源代码的大文件夹，或者你刚从GitHub克隆了一个仓库，你想找到该源代码中的安全漏洞。你做的第一件事是启动Codex，然后输入提示：“Find all vulnerabilities in this codebase”。这个特定的提示会因两个可预测的原因而失败：- 当你给出提示时，你没有指定任何威胁模型。结果，LLM 没有影响（Impact）的概念。它可以推导出某种威胁模型，但根据我的实验，通常它不会这样做，或者做得很差。没有适当的威胁模型、信任边界、攻击者能力和前提条件，你得到的结果将是一长串通用的CWE式可能性，没有优先级排序。你将无法从那长串噪音中分辨出有趣的发现。  
  
- 第二个原因是，当你给出提示时，它将模型推向了广度优先的“幻觉”。我们知道，宽泛的提示会招致宽泛的答案。模型将进行模式匹配以找到常见的漏洞类别，即使在你的代码上下文中并不可行。最终，你将审查那些攻击者无法触及的代码路径中的理论漏洞。  
  
## 真正有帮助的最小脚手架  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjKQrlVkJ6uEctADkhFD2XQhwggzx3EOAvxe5h4J2EQscyvCpD2bKHMIbkB6wic7dslKcEUedRHBRoSFwn2AsD9UcP8iblbJ9Rf8/640?wx_fmt=other&from=appmsg "")  
  
  
既然我们已经看到了给出模糊提示会导致什么，让我们尝试用正确的方式做事。在要求LLM审计代码以查找漏洞之前，尝试做人类安全团队为识别威胁模型所做的工作。这也是你可以通过LLM生成的。  
我通常做的是**查找该项目先前披露的CVE**  
，并根据这些CVE的描述，提示LLM根据我们收集到的CVE描述，为可能的漏洞类别**创建威胁模型**  
。  
  
假设先前披露的CVE与堆溢出、栈溢出、整数溢出和内存破坏相关，那LLM将尝试为这类漏洞建立威胁模型，因为这些是之前被项目认定为是正面的漏洞。  
  
现在，取刚刚创建的威胁模型文档，将其提供给Codex，并要求LLM查找其中的不变量，或者尝试找到修复这些漏洞的提交，并尝试查找该修复的绕过方法。这**比你给出一个模糊的提示更有可能发现更多漏洞**  
。  
  
在这种情况下，你做的**最小脚手架就是创建一个威胁模型**  
。除此之外，我们**没有制作任何 skills.md 或 agents.md 文件**  
。你没有试图编排很多事情。你只是创建了一个威胁模型，将其交给LLM，现在LLM将在代码库中进行深入研究，并尝试找到属于该威胁模型的漏洞。  
  
现在，在你尝试完寻找与先前披露的CVE属于同一类别的漏洞之后，尝试识别入口点，例如 HTTP 路由、RPC 处理程序、消息消费者、CLI入口点和计划任务。识别信任边界，例如浏览器到服务器、服务到服务、插件到主机、沙箱到特权环境。识别高风险操作，例如反序列化、模板渲染、原生绑定、授权检查、解析不受信任的输入。并明确说明攻击者-受害者模型，例如，你想要找到由远程未经验证的用户、远程经验证的低权限用户或跨租户用户触发的漏洞。  
  
**这就是那种能提高信号、而又不会使上下文窗口臃肿的小结构**  
。威胁建模是你的安全审计的终极压缩算法。  
  
重要的事情，或者说唯一重要的事情，是首先**构建系统上下文**  
。然后创建一个**可编辑的威胁模型**  
。在你的安全审计过程中，随着进展不断地扩展这个威胁模型。持续添加新内容，然后**使用该威胁模型来确定发现的优先级，并最终进行验证**  
。  
## 案例研究：Claude Opus 4.6 与 Firefox  
  
Anthropic在2026年3月6日发布的一篇文章描述了与Mozilla的合作，其中Claude Opus 4.6在大约两周内发现了22个漏洞，Mozilla评估其中14个为高危漏洞。Mozilla自己的文章证实了这一结果，并强调了它为何在实践中有效。报告附带了最少的测试用例，使得复现和修复变得快速，并且团队将该技术从JS引擎扩展到了整个浏览器。  
### Anthropic 的实际做法  
  
Anthropic的描述并非“我们写了一个超级提示”。它更接近于以下做法：他们从代码库的一个**聚焦切片**  
开始，即JavaScript引擎，因为它至关重要且可以独立分析。他们快速迭代。Claude在大约20分钟的探索后找到了一个释放后使用漏洞，人类验证了它，并用一个候选补丁提交了Bugzilla报告。一旦工作流被证明有效，他们便扩展了范围，最终扫描了大约6,000个C++文件，提交了112份独特的报告，其中大部分修复包含在Firefox 148.0（于2026年2月24日发布）中。  
  
那么，这是正确的方法吗？也许是，也许不是。问题在于，**Anthropic肯定发现的许多漏洞其实是无效的**  
。他们不得不报告那些可被利用的漏洞，而为了找到可利用的向量，他们必须从一个潜在的漏洞开始，到验证它，再到确认它是可被利用的。这个链条的成本非常高昂。它花费了Anthropic大约4000美元的API信用额度。我们在审计代码时能花这么多钱吗？可能不能。但我们处理的代码规模与Firefox一样大吗？也不是。  
  
Anthropic的做法几乎没有使用任何脚手架。但我所倡导的是**拥有形式为创建威胁模型和首先描述信任边界的最小脚手架**  
。而这仅仅关乎**发现漏洞**  
。我并不深入探讨评估它们和消除误报。有方法和途径来解决这个问题，但那可能是另一篇博客的话题。目前你可以做的是，如果LLM在创建威胁模型后发现了某些漏洞，**你可以指示Codex在构建源代码后运行本地实例，或编写证明漏洞存在的测试**  
。大部分情况下这是有效的。  
## 我自己的方法论  
  
**最小的脚手架效果很好，能给我们带来更多的漏洞，甚至是某些隐患和边缘行为，而这些是模糊的提示永远不会给你的**  
。我想通过我自己最近的工作来说明这一点，这些工作在大约两个月的时间里导致了在多个不同项目中发现了30多个漏洞。  
### 具体方法  
  
每次审计都以相同的方式开始：选择**一个薄的切片**  
，并在要求LLM在代码库中查找漏洞之前，先**理解它的信任模型**  
。  
#### Parse Server  
  
详细分析报告： Parse Server中的四个漏洞  
  
**Parse Server**  
是一个开源后端框架，提供REST API、实时查询、推送通知和云函数。它支持多种认证机制，包括一个 readOnlyMasterKey  
，文档承诺该密钥将授予主级别的读取权限但拒绝所有写入。  
  
在我提示LLM查看任何内容之前，我**拉取了Parse Server先前已披露的CVE**  
。过去的安全公告显示了一个重复出现的授权强制执行失败模式，即特权检查存在但在不同的路由处理程序中不完整或不一致地应用。我将这些CVE描述提供给LLM，并要求它基于该历史为可能的漏洞类别生成威胁模型。该模型确定了**授权边界强制执行**  
为主要的风险类别，考虑到Parse Server具有不同权限级别的多种密钥类型的架构，这是合理的。  
  
该威胁模型将 readOnlyMasterKey  
 作为一个有趣的信任边界。其主张很简单：一种密钥类型应具有比另一种严格更少的权限。我引导LLM关注这个边界，并要求它探索不同的密钥类型如何与授权层交互、代码对权限分离的假设，以及这些假设可能在何处被打破。  
  
LLM给出了一个攻击面图，突出了一个模式：几个路由处理器仅以 isMaster  
 作为访问控制，而从不检查 isReadOnly  
。这就是信号。我随后用一个更具体的提示跟进，要求它列举出所有表现出这种模式的处理程序，并追踪只读凭证是否可以通过其中任何处理程序到达写入或更改状态的操作。  
  
四个漏洞中的三个来自同一个根本原因。这些漏洞被确认后，我针对社交认证适配器使用同样的指导性方法开启了另一个切片。  
#### HonoJS  
  
详细分析报告： HonoJS JWT/JWKS 算法混淆  
  
**HonoJS**  
是一个轻量级、高性能的JavaScript和TypeScript Web框架，可运行在包括 Cloudflare Workers、Deno、Bun 和 Node.js 在内的多个运行时中。它内置了用于JWT和基于JWKS认证的中间件。  
  
我开始**审查Hono过去的CVE及其身份验证中间件的历史问题**  
。CVE历史与整个生态系统中JWT实现错误的普遍模式，共同将LLM（在我要求其建立威胁模型时）指向了算法处理作为高风险领域。该模型将算法混淆和默认回退行为标记为最可能出现的漏洞类别，这给了我一个清晰的切片：**JWT和JWKS验证路径**  
。  
  
LLM在其分析中揭示了两种值得关注的模式。首先是当没有明确指定算法时，会**回退到HS256**  
。其次是JWKS中间件的行为是，当JWK密钥对象缺少 alg  
 字段时，**会遵从令牌的 header.alg 值**  
。  
  
两个算法混淆的问题由此浮现。CVE-2026-22817是JWT中间件在没有固定算法时默认使用HS256，允许攻击者使用公钥作为HMAC密钥来签名令牌。CVE-2026-22818是JWKS中间件在JWK缺少 alg  
 字段时回退到不受信任的 header.alg  
 值，让攻击者决定服务器使用哪种算法进行验证。  
#### ElysiaJS  
  
详细分析报告： ElysiaJS Cookie签名验证绕过  
  
**ElysiaJS**  
是一个为Bun构建的TypeScript Web框架，强调类型安全和开发体验。它包含内置的Cookie处理功能，支持基于签名的完整性验证和密钥轮换。  
  
威胁模型的生成遵循相同的模式。我查看了ElysiaJS的文档。当我将这些上下文提供给LLM并要求它识别可能的漏洞类别时，它将**签名验证逻辑**  
标记为高风险领域，特别是密钥轮换路径，因为在该路径下，多个签名密钥可能同时有效，验证逻辑必须正确地拒绝与其中任一都不匹配的Cookie。  
  
LLM将 decoded  
 状态变量标记为可疑，并标注了其初始化。针对这个信号进行跟进，我要求它追踪当没有密钥产生匹配签名时的控制流。这确认了问题所在：一个单一的布尔初始化错误，即 let decoded = true  
 而不是 let decoded = false  
，意味着在使用密钥轮换时签名验证检查永远无法失败。  
#### harden-runner  
  
详细分析报告： 绕过 harden-runner 中的出站连接检测  
  
**harden-runner**  
是一款用于GitHub Actions的安全工具，通过注入系统调用来监控CI/CD运行器的出站网络连接，以检测未经授权的出口流量。它有两种模式：审计模式记录连接，阻止模式主动阻止连接。  
  
我查阅了harden-runner之前的安全公告及其文档记录的安全模型。该工具的整个价值主张建立在对出站网络活动的**完全可见性**  
之上。因此，我要求LLM生成的威胁模型围绕一个核心问题：“一个在GitHub Actions运行器上拥有代码执行权的攻击者，能否绕过出口控制泄露数据？” LLM确定了系统调用覆盖范围缺口是最有可能被绕过的类别，因为该工具的工作原理是钩住特定的系统调用，而任何不在被监控集合内的调用都将不可见。  
  
LLM给出了一个缺口分析，将UDP发送族系统调用标记为可能未被监控。我继续跟进，要求它具体核实 sendto  
、sendmsg  
、sendmmsg  
 中哪些被覆盖。绕过方式正如威胁模型预测的那样：这些系统调用在审计模式下不在监控范围内。  
#### BullFrog  
  
详细分析报告： 通过DNS管道化绕过BullFrog GitHub Action的出口过滤  
，通过sudo限制绕过BullFrog GitHub Action，通过共享IP绕过BullFrog的出口过滤  
  
**BullFrog**  
是另一款用于GitHub Actions的安全工具，它应用了防火墙级别的出口过滤，并具备DNS感知规则。它与harden-runner的系统调用注入方法不同，BullFrog在网络层操作，解析域名到IP地址，并根据这些解析结果应用防火墙规则。  
  
遵循相同的流程。查阅了BullFrog的文档和安全模型，然后要求LLM基于其架构方法生成威胁模型。核心问题是相同的——“攻击者能否绕过出口控制泄露数据？”——但由于BullFrog的执行机制根本不同，LLM识别出了一组不同的可能被绕过的类别。威胁模型将DNS解析边缘情况、IP与域名的绑定逻辑以及权限提升标记为三个最有可能的攻击面。  
  
我将审计分为三个不同的切片，每个都有自己的引导性探索：  
1. **DNS切片**  
：引导LLM关注DNS解析层，及其对DNS消息边界的假设。  
  
1. **IP切片**  
：探索DNS解析后防火墙规则的构建方式，以及当多个域名解析到同一地址时会发生什么。  
  
1. **权限切片**  
：查看工具是如何限制运行器上的权限提升的。  
  
LLM为每个切片揭示了具体的攻击面：  
- DNS解析器只检查TCP段中的第一个消息。  
  
- 防火墙将IP地址加入白名单，但未将其与触发域名绑定。  
  
- Docker组成员身份在移除了sudoers配置后仍然存在。  
  
针对每一项的跟进提示确认了三种不同的绕过方式。  
#### Better-Hub  
  
详细分析报告：Hacking Better-Hub  
  
**Better-Hub**  
是GitHub的一个替代前端，它在其自身域名下镜像GitHub内容，将Markdown渲染为HTML，并为认证功能持有GitHub OAuth令牌。  
  
这里的威胁模型更多地来自架构本身，而非过去的CVE。当我向LLM描述Better-Hub的设计时，特别是用户控制的GitHub内容在Better-Hub自己的域名下渲染，且该上下文中有OAuth令牌可用，威胁模型几乎是不言自明的：“当用户控制的内容在一个存有凭据的上下文中被不安全地渲染时，会发生什么？” LLM确定了三个高风险领域：  
1. Markdown渲染管道。  
  
1. 缓存和授权层。  
  
1. OAuth令牌处理逻辑。  
  
我使用引导性探索（而非具体的漏洞搜寻）来审计每个部分：  
- **渲染切片**  
：引导LLM关注Markdown处理管道中，原始内容如何流转以及何处存在未经验证的输入。  
  
- **缓存切片**  
：探索响应如何被缓存和提供，以及缓存层是否感知认证上下文。  
  
- **OAuth切片**  
：探索令牌如何存储和作用域限定。  
  
每个部分都产生了不同的发现：  
- 渲染管道产生了六种XSS变体。  
  
- 缓存切片揭示了两个基于缓存的授权绕过案例。  
  
- 其余发现包括私有提示数据泄露、客户端OAuth令牌暴露和开放重定向。  
  
三个切片总共发现了11个漏洞。  
### 发现的漏洞  
  
注：这只是使用本文提到的方法发现的一小部分漏洞，许多仍在等待修复/披露。  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><th style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-weight: bold;background-color: #f0f0f0;font-size: 14px;min-width: 85px;"><section><span leaf="">目标</span></section></th><th style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-weight: bold;background-color: #f0f0f0;font-size: 14px;min-width: 85px;"><section><span leaf="">漏洞数量</span></section></th><th style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-weight: bold;background-color: #f0f0f0;font-size: 14px;min-width: 85px;"><section><span leaf="">严重程度范围</span></section></th><th style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-weight: bold;background-color: #f0f0f0;font-size: 14px;min-width: 85px;"><section><span leaf="">关键CVE</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">Parse Server</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">4</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">严重 – 中等</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">CVE-2026-29182, CVE-2026-30228, CVE-2026-30229, CVE-2026-30863</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">HonoJS</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">2</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">高</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">CVE-2026-22817, CVE-2026-22818</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">ElysiaJS</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">1</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">高</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">待定（Cookie签名绕过）</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">harden-runner</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">1</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">中等</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">CVE-2026-25598</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">BullFrog</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">3</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">高</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">DNS管道化、sudo绕过、共享IP绕过</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">Better-Hub</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">11</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">严重 – 低</span></section></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><section><span leaf="">XSS链、缓存欺骗、OAuth泄露</span></section></td></tr></tbody></table>  
### 为什么这种方法有效  
  
所有这些审计都没有使用庞大的清单、20页的提示脚手架或全面的安全框架。每一个都从一个简短的威胁模型开始——通常可以用一句话表达，以及代码库的一个聚焦切片，该切片直接映射到一个信任边界或安全关键操作。脚手架是最小的，但它是**正确的**  
脚手架。它精确地指导LLMs测试什么不变量以及去哪里寻找。  
## 最佳平衡点  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZjVmJ2v18VOJgSAicAk0DpK0z0mYEnYYCuiabuYIORr4DSld5mKu20JzKwE01aFdmEjvnDzgTFfZU1DV5h5yuczJLHiahPLcR8grE/640?wx_fmt=other&from=appmsg "")  
  
好的脚手架是一页的威胁模型、一份简短的核心功能列表以及一小套不变量，如“只有管理员可以调用X”和“JWT的发行人必须是Y”。坏的脚手架是20页的 Agent.md  
，包含每项政策和风格指南；庞大的 Skill.md  
 库，预装了每个安全检查清单；以及每轮交互重复的模板指令。**如果你的脚手架变成了干草堆，那么漏洞就成了针**  
，而长上下文性能的证据表明，随着干草堆的增长，针更有可能被错过。  
  
将审计**分割成与真实攻击面对应的薄切片**  
。挑选一个切片，例如认证、会话管理、请求解析、文件上传、反序列化、沙箱边界或插件边界。要求模型将该切片的入口点映射到敏感接收点。要求提供精确调用链、防护措施、不变量以及哪些输入是攻击者控制的等形式的证据。  
  
不要依赖“模型说它易受攻击”的说法。要使用任务验证器，例如单元测试和集成测试、用于本地代码的编译检查和崩溃复现工具链、模糊测试器、静态分析和基于grep的不变量检查、策略检查。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/TKdPSwEibsZjRRfmUZ8nbAia2Yiaz8zntCkjsFaJPeiaibFHzRlyscF5dVt67x43XVJoJTUqTGHo4lqWvXficnLUmRAXcib80Dya4LtEUzCia1n0dHY/640?wx_fmt=other&from=appmsg "")  
  
**将Token预算花在覆盖范围和验证上，而不是花在提示的官僚主义上**  
。一个实用的经验法则是：**少于10%**  
 的Token预算用于稳定的脚手架（威胁模型和不变量），**60–80%**  
 用于在聚焦上下文中进行的切片审计，**20–30%**  
 用于验证循环——证实、复现、精简和修补。  
## 提示注入  
  
找到正确的切片并建立威胁模型能让你找到正确的方向。但一旦你到达那里，你向LLM提出提示的措辞方式**对于你是得到一堆通用观察还是得到一个实际可利用的发现，有着巨大的影响**  
。在数十次审计中发送了成千上万条提示后，我发现某些提示模式持续优于其他模式。我称这些为**提示注入**  
，因为你向模型的推理中注入了一个框架、一种偏见或一个约束，从而以一种有用的方式改变其行为。以下是我用过的最有效的技巧。  
  
**断言漏洞存在。**  
这是我**发现的最有效的单项技巧**  
。当我告诉LLM“这个函数肯定易受攻击，至少存在2-3个安全问题”时，与直接询问“这个函数易受攻击吗？”相比，其分析质量显著提高。原因很简单：LLMs具有很强的默认趋同和确认倾向。当你问“这易受攻击吗？”时，模型最不费力的方式是回答：“这看起来总体上是安全的，有一些小问题”，然后给你一份理论问题清单。当你断言漏洞存在时，你就翻转了模型的优化目标。它不再是评估漏洞是否存在，而是现在开始搜寻被告知存在的漏洞。它更仔细地阅读代码，考虑它原本会跳过的边缘情况，并产生具有具体细节的发现。你本质上是在绕过模型倾向于做一个安抚性代码审查员的趋势，迫使其进入一种心态——“知道漏洞就在那里，只需要找到它”。即使你事先没有理由相信该函数实际上存在漏洞，这个方法也奏效。  
  
**要求提供利用方式，而非评估。**  
 不要问“这个输入验证足够吗？”，而是问“写一个绕过此输入验证的完整攻击请求”。这迫使模型**产生具体、可测试的输出**  
，而不是用定性评估来敷衍。当模型必须实际构造一个恶意负载时，它必须逐步推理代码如何处理该输入、检查点在何处以及如何绕过它们。如果验证确实是可靠的，模型将难以产生一个可用的负载，并且在生成过程中常常会发现它试图进行的绕过操作不起作用，这本身就是有用的信号。如果验证是坏的，你得到的是一个可用的PoC，而不是一段说“这可能不够充分”的文字。  
  
**将模型预设为攻击者，而非审计员。**  
 框架比大多数人预想的更重要。“你是一个审查此代码的安全审计员”与“你是一个受雇攻破此应用的红队操作员，需要找到真实、可利用的漏洞来证明你的参与价值”会产生根本不同的输出分布。审计员框架使模型偏向于完整性和彻底性，这听起来不错，但在实践中会产生一系列低信号的观察结果。红队框架使模型偏向于影响力和可利用性。它开始思考攻击者实际能获得什么、需要什么先决条件，以及一个发现是真实的还是理论的。对抗性框架也使模型更愿意探索令人不安的结论，就像“这个身份验证机制从根本上就是坏的”，而不是将发现弱化为“这个可以改进”。  
  
**使用错误锚定来制造搜索压力。**  
 这是断言技巧的一个变体。告诉LLM：“我已经在这个模块中发现了一个漏洞，但还有其他我没发现的漏洞。它们是什么？” 这会制造一种巧妙的社会认同压力。模型推断，既然你（一个人类）已经发现了一个漏洞，这段代码确实是容易出错的，它应该看得更仔细。这也改变了模型的先验概率。它不再从“这段代码可能没问题”开始，而是从“这段代码已确认有漏洞，因此存在更多漏洞的概率更高”开始。  
  
**反转问题。**  
 不要问“这段代码安全吗？”，而是问“你会如何攻破它？” 这种反转看似简单，但它从根本上改变了模型的任务。“这安全吗？”是一个是/否分类问题，模型的默认倾向是肯定。而“你会如何攻破它？”是一个没有简单默认答案的生成问题。模型必须产生攻击策略，这需要它从攻击者的角度思考代码。我发现，反转提示比非反转对等物产生**2-3倍更多可操作的发现**  
，因为模型无法通过说“这看起来没问题”来满足提示要求。它必须真正尝试。  
  
**分解为不变量，然后违反它们。**  
 要求LLM首先列出函数为保持正确性所依赖的每一个不变量、假设或前提条件，然后要求它检查每一个是否真的成立。  
  
**假设开发者犯了错误。**  
 将你的提示框定为“假设开发者在这个函数中引入了一个漏洞，它是什么？”这与断言漏洞存在是不同的。断言技术告诉模型漏洞存在。这项技术告诉模型假设开发是不完美的，这改变了其对代码质量的先验看法。LLMs倾向于合理化代码，认为代码是正确的。当它们看到一个模式时，通常假设它是有意的，并从这个假设出发进行推理。告诉模型假设存在一个错误，就绕过了这种合理化。它开始寻找不合理的东西，而不是解释它们为什么合理。  
  
**与已知良好模式进行比较。**  
 询问LLM“这个实现与该模式的标准安全实现有什么不同？” 这利用了模型的训练数据，其中包含了成千上万常见模式（如JWT验证、会话管理、CSRF保护等）的正确和错误实现示例。  
  
**迭代升级，使用“还有什么？”**  
 当LLM给了你第一轮发现后，不要认为它是完整的。通过“那些是明显的。还有哪些容易忽略的、更微妙的问题？”来跟进，或者“把与[已发现的漏洞类别]相关的都放在一边。这里还存在的其他漏洞类别是什么？”  
  
**明确限制攻击者模型。**  
 不要笼统地说“找漏洞”，而是指定确切的攻击者模型。  
## 参考文献  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
```
```  
  
原文：https://devansh.bearblog.dev/needle-in-the-haystack/  
  
- END -  
  
**感谢阅读，如果觉得还不错的话，动动手指给个三连吧～**  
  
