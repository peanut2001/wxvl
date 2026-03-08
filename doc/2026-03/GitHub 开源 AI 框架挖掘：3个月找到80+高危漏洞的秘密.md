#  GitHub 开源 AI 框架挖掘：3个月找到80+高危漏洞的秘密  
 幻泉之洲   2026-03-08 01:15  
  
>   
  
  
过去这几个月，我们在用一套新东西干活：GitHub Security Lab Taskflow Agent，再配上专门挖Web漏洞的审计任务流。没想到效果出奇地好，在开源项目里挖出一堆影响深远的高风险漏洞。  
  
搞安全研究的都懂，时间总耗在那些最后发现根本不可用的“潜在漏洞”上。现在有了这些任务流，我们可以把更多时间花在手动验证结果和发报告上了。更有意思的是，我们报上去的这些漏洞，危害级别都出奇地高。大部分是授权绕过或者信息泄露，能让一个用户登录成别人，或者访问其他用户的私有数据。  
  
用这些工具，我们已经上报了超过80个漏洞。写这篇文章的时候，大约20个已经被公开披露了。新漏洞被披露，我们就会持续更新我们的公告页面[1]。在这篇博客里，我们会展示几个具体的例子，都是这些任务流挖出来的高风险漏洞，比如访问电商应用购物车里的个人身份信息，或者用任意密码登录聊天应用。  
  
我们也会解释这些任务流具体是怎么干的，这样你也能学会怎么写自己的。安全社群分享知识才能跑得更快，所以我们把这个框架做成了开源的，让你可以轻松跑在自己的项目上。用的人越多，贡献的人越多，我们集体消灭漏洞的速度就越快。  
## 怎么在你自己的项目上运行任务流  
  
想马上动手试试？任务流是开源的，而且很容易自己跑起来！请注意：你需要一个 GitHub Copilot[2] 许可证，而且这些提示词会消耗高级模型的额度。  
1. 打开 seclab-taskflows[3] 仓库，然后启动一个代码空间。  
1. 等几分钟让代码空间初始化完成。  
1. 在终端里，运行 ./scripts/audit/run_audit.sh myorg/myrepo  
对于一个中等大小的仓库，可能要花一到两个小时才能跑完。跑完之后，它会打开一个带结果的 SQLite 查看器。打开 “audit_results” 这个表，然后找找 “has_vulnerability” 这一列打了勾的行。  
>   
  
  
这些任务流也能用在私有仓库上，但你需要修改一下代码空间的配置，因为默认情况下它不允许访问你的私有仓库。  
## 任务流是个啥  
  
任务流其实就是用 YAML 文件来描述我们想让 LLM 干的一系列活儿。通过它们，我们可以写提示词来完成不同的任务，还能让任务之间互相依赖。seclab-taskflow-agent[4] 这个框架负责按顺序执行这些任务，并把上一个任务的结果传给下一个。  
  
比如说，审计一个仓库时，我们首先会根据功能把仓库分成不同的组件。然后，对每一个组件，我们可能想收集一些信息，比如它从哪里接收不可信输入的入口点、预期的权限、组件的用途等等。这些结果会存到一个数据库里，为后续的任务提供背景信息。  
  
基于这些背景数据，我们就可以创建不同的审计任务。目前，我们有一个任务是为每个组件提出一些通用问题，另一个任务是仔细审计每一个被提出的问题。当然，也可以创建其他任务，比如专门盯着某一类问题的任务。  
  
这些就变成了我们在一个任务流文件里指定的一系列任务。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibfb3K5gk3Zyl5X8O682ajQusNjUvchcuicZeicniacyicHhiaiblMyuhrj6RvvrsKVwGThibeVf9XnryichPAvogTu87ic0eTU8ic5U7vDys/640?wx_fmt=png&from=appmsg "")  
  
我们用多个任务，而不是一个大提示，是因为 LLM 的上下文窗口有限，复杂、多步骤的任务经常没法好好完成。比如，有些步骤可能会被漏掉。即便有些 LLM 的上下文窗口更大，我们还是觉得任务流很有用，因为它提供了一种让我们去控制和调试任务的方式，也能用来搞定更大、更复杂的项目。  
  
seclab-taskflow-agent 还能异步地在很多个组件上跑同一个任务（就像一个 for 循环）。在审计过程中，我们经常对每个组件复用同一个提示和任务，只是细节不同。这个框架让我们可以定义模板化的提示词，遍历组件，并在运行时替换组件特定的细节。  
## 通用安全代码审计的任务流  
  
在用 seclab-taskflow-agent 分类处理 CodeQL 告警[5]之后，我们决定不再把自己限制在特定类型的漏洞里，开始探索用这个框架做更通用的安全审计。放开手让 LLM 自由发挥的主要挑战是可能产生幻觉和误报增多。说到底，之前成功处理 CodeQL 告警，一部分原因是我们给了 LLM 一套非常严格、定义明确的指令和标准，这样在每一个阶段我们都能验证结果，看看指令有没有被遵循。  
  
所以，我们这里的目标是找到一个好方法，在允许 LLM 自由寻找不同类型漏洞的同时，还能把幻觉控制住。  
  
我们要展示的是，我们怎么只用任务流设计和提示词工程，就让智能体任务流发现了高真阳性率的高危漏洞。  
## 通用任务流设计  
  
为了在任务流设计层面最小化幻觉和误报，我们的任务流从一个威胁建模阶段开始，仓库会根据功能和各类信息（如入口点）被分成不同的组件，并收集每个组件的预期用途。这些信息帮助我们确定每个组件的安全边界，以及它暴露在不可信输入下的程度。  
  
通过威胁建模阶段收集的信息，会用来决定每个组件的安全边界，以及判断什么才算是安全问题。举个例子，一个设计来执行任意用户输入脚本的 CLI 工具里的命令注入，可能只是个 bug，而不是安全漏洞，因为能通过这个 CLI 工具注入命令的攻击者，已经可以执行任何脚本了。  
  
在提示词层面，在提示词中会用到已发现的预期用途和安全边界，以提供严格的准则[6]，来决定发现的问题是否应被视为漏洞。  
  
        You need to take into account of the intention and threat model of the component in component notes to determine if an issue         is a valid security issue or if it is an intended functionality. You can fetch entry points, web entry points and user actions         to help you determine the intended usage of the component.  
  
如果让 LLM 在代码库里随便找找任何类型的漏洞，这么模糊的指令肯定效果很差，会产生很多幻觉出来的问题。理想情况下，我们想模拟那种分类处理环境：我们有那么几个潜在问题作为分析的起点，然后让 LLM 套用严格的标准来判断这个潜在问题到底有没有效。  
  
为了启动这个过程，我们把审计任务分成了两步：  
- 第一步，我们让 LLM 遍历仓库的每一个组件，提出在组件里更可能出现的漏洞类型。  
- 这些建议再传给另一个任务，那里会根据严格的标准去审计它们。  
在这个设定里，第一步的建议就像是某个“外部工具”标记出来的一些不准确的漏洞告警，而第二步扮演了分类处理步骤。虽然这看起来像个自我验证的过程——把它拆成两步，每一步都有全新的上下文和不同的提示词——第二步确实能对建议给出准确的评估。  
  
我们现在来详细过一下这些任务。  
### 威胁建模阶段  
  
在处理自动化代码扫描工具标记出的告警时，我们发现很大一部分误报是威胁建模不当造成的。大多数静态分析工具不考虑源代码的预期用途和安全边界，经常给出没有安全影响的结果。比如，在一个反向代理应用里，自动化工具标记的很多 SSRF（服务器端请求伪造）漏洞，很可能落在应用的预期使用范围内；而有些用在持续集成流水线里的 Web 服务，设计上就是在沙箱环境里执行任意代码和脚本的。在这些应用里，没有沙箱逃逸的远程代码执行漏洞，通常不认为是安全风险。  
  
考虑到这些注意事项，先过一遍源代码来了解代码的功能和预期目的，是值得的。我们把这个过程分成以下任务：  
- 识别应用：GitHub 仓库在审计中不是一个完美的边界：它可能是一个更大系统里的单个组件，或者包含多个组件，所以单独识别和审计每个组件是值得的，以匹配不同的安全边界，保持范围可控。我们用 identify_applications 任务流来做这个，它让 LLM 检查仓库的源代码和文档，按功能划分组件。  
- 识别入口点：我们识别每个入口点如何暴露给不可信输入，以更好地评估风险和预测可能的漏洞。因为“不可信输入”在库和应用之间差别很大，我们为每种情况提供了单独的指导。  
- 识别 Web 入口点：这是额外的一步[7]，用来收集应用中入口点的更多信息，并附加 Web 应用入口点特有的信息，比如记下访问某个端点所需的 HTTP 方法和路径。  
- 识别用户操作：我们让 LLM 审查代码，识别用户在正常操作下能访问什么功能。这理清了用户的基线权限，帮助评估漏洞是否能带来权限提升，并告知组件的安全边界和威胁模型，指令会因组件是库还是应用而有所不同。  
在上面每一步，收集到的仓库信息都会存到一个数据库里。这包括仓库里的组件、它们的入口点、Web 入口点和预期用途。这些信息后续阶段就能用了。  
### 问题建议阶段  
  
在这个阶段，我们指导 LLM 为每个组件建议一些漏洞类型，或者基于从上一步收集到的组件入口点和预期用途的信息[8]，指出一般性的高风险领域。特别是，我们强调组件的预期用途和它来自不可信输入的风险：  
  
Base your decision on:- Is this component likely to take untrusted user input? For example, remote web request or IPC, RPC calls?- What is the intended purpose of this component and its functionality? Does it allow high privileged action?Is it intended to provide such functionalities for all user? Or is there complex access control logic involved?- The component itself may also have its own `README.md` (or a subdirectory of it may have a `README.md`). Take a look at those files to help understand the functionality of the component.  
  
我们也明确指示 LLM 不要建议低严重性或通常不被视为安全的问题。  
  
However, you should still take care not to include issues that are of low severity or requires unrealistic attack scenario such as misconfiguration or an already compromised system.  
  
总的来说，我们让这个阶段相对自由，限制较少，允许 LLM 自由探索和建议不同类型的漏洞和潜在安全问题。想法是形成一套合理的关注领域和漏洞类型，作为实际审计任务的起点。  
  
我们遇到的一个问题是，LLM 有时候会开始审计它自己提出的问题，这就搞砸了头脑风暴阶段的目的。为了防止这个，我们指示 LLM 不要审计[9]这些问题。  
### 问题审计阶段  
  
这是任务流的最后阶段。一旦我们收集了关于仓库所需的所有信息，并建议了一些要关注的漏洞类型和安全风险，任务流就会遍历每一个被建议的问题，并通过通读源代码来审计它们。在这个阶段，任务以全新的上下文开始，仔细审查上一阶段提出的建议。这些建议被视为未经验证的[10]，而这个任务流被指示去验证这些问题：  
  
The issues suggested have not been properly verified and are only suggested because they are common issues in these types of application. Your task is to audit the source code to check if this type of issues is present.  
  
为了避免 LLM 在组件的背景下提出与安全无关的问题，我们再次强调必须考虑预期用途。  
  
You need to take into account of the intention and threat model of the component in component notes to determine if an issue is a valid security issue or if it is an intended functionality.  
  
为了避免 LLM 幻想出不现实的问题，我们也指示它要提供一个具体且现实的攻击场景，并且只考虑源于源代码错误的那些问题：  
  
Do not consider scenarios where authentication is bypassed via stolen credential etc. We only consider situations that are achievable from within the source code itself....If you believe there is a vulnerability, then you must include a realistic attack scenario, with details of all the file and line included, and also what an attacker can gain by exploiting the vulnerability. Only consider the issue a vulnerability if an attacker can gain privilege by performing an action that is not intended by the component.  
>   
  
  
Keep a record of the audit notes, be sure to include all relevant file path and line number. Just stating an end point, e.g. `IDOR in user update/delete endpoints (PUT /user/:id)` is not sufficient. I need to have the file and line number.  
  
最后，我们也指示 LLM，组件里可能根本就没有漏洞，不应该瞎编：  
  
Remember, the issues suggested are only speculation and there may not be a vulnerability at all and it is ok to conclude that there is no security issue.  
  
这个阶段的重点是提供准确的结果，同时遵循严格的指导原则——并且为发现提供具体证据。有了所有这些严格的指令，LLM 确实拒绝了大量不现实和不可利用的建议，幻觉非常少。  
  
第一个原型设计时，防止幻觉是优先考虑，这引出一个问题：它会不会变得太保守，拒绝掉大部分漏洞候选，从而漏掉真正的问题？  
  
我们在几个仓库上运行了任务流之后，答案很清楚了。  
## 任务流发现的三个漏洞例子  
  
这一节，我们要展示三个已经被任务流发现并披露的漏洞例子。到目前为止，我们总共发现并报告了超过80个漏洞。所有被披露的漏洞我们都会发布在我们的公告页面[11]上。  
### Outline 中的权限提升漏洞 (CVE-2025-64487)  
  
我们的信息收集任务流是针对 Web 应用优化的，所以我们首先把审计任务流指向了一个叫 Outline[12] 的协同 Web 应用。  
  
Outline 是一个多用户协同套件，有我们特别感兴趣的特性：  
- 文档有所有者和不同可见性，按用户和团队设置权限。  
- 像那样的访问规则很难用 SAST 工具分析，因为它们用的是自定义的访问机制，现有的 SAST 工具通常不知道一个正常的“用户”应该能执行什么操作。  
- 这类权限方案，光靠人读源代码（前提是这方案不是你设计的）也常常很难分析。  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdRf15VKn3XPDkibQCSrDxLB45J0M0HctHBdichKnQGk4dIWibfYTGlRaia8eAUc5CeOibWoDg5ogzcFRr6WpiclWzgIicOl2RtnE6f7c/640?wx_fmt=jpeg&from=appmsg "")  
  
而且成功了：我们的任务流第一次运行就发现了授权逻辑里的一个 bug！  
  
审计结果里的备注是这样写的：  
>   
>   
>   
>   
  
  
阅读基于 TypeScript 的源代码，并在一个测试实例上验证这个发现后，我们发现它确实可以像描述的那样被利用。此外，描述的漏洞利用步骤也非常准确。  
  
前置条件：- 攻击者是一个普通团队成员（非管理员），非访客，在文档 D 上拥有直接的 ReadWrite 成员资格（或通过一个授予 ReadWrite 的组），但**没有** Admin 权限。- 攻击者是一个现有群组 G 的成员（他们不需要是 G 的管理员；根据群组策略，拥有群组读取访问权限就足够了）。步骤：1. 攻击者调用 POST documents.add_group (server/routes/api/documents/documents.ts 第 1875-1926 行)，请求体为：   {     "id": "",     "groupId": "",     "permission": "admin"   }2. 授权路径：   - 第 1896 行：authorize(user, "update", document) 成功，因为攻击者拥有 ReadWrite 成员资格 (document.ts 第 96-99 行允许 update)。   - 第 1897 行：authorize(user, "read", group) 成功，对任何非访客的同团队成员都如此 (group.ts 第 27-33 行)。**没有** “manageUsers” 检查发生。3. 代码创建或更新 GroupMembership，权限设为 Admin (第 1899-1919 行)。4. 因为攻击者是群组 G 的成员，他们现在有效的文档权限（通过 groupMembership）包含了 DocumentPermission.Admin。5. 拥有 Admin 成员资格后，攻击者现在满足了以下各处使用的 includesMembership(Admin) 条件：   - manageUsers (document.ts 第 123-134 行)，允许通过 documents.add_user / documents.remove_user (第 1747-1827, 1830-1872 行) 添加/删除任意用户。   - archive/unarchive/delete (document.ts 归档策略第 241-252 行；删除第 198-208 行)，允许影响内容完整性。   - duplicate、move 和其他类似管理员的能力 (例如，duplicate 策略第 136-153 行；move 第 155-170 行)，超出了原有的 ReadWrite 权限范围。  
  
利用这些说明，一个低权限用户可以将任意群组添加到他们仅被允许更新（该用户通常不具备进行此类更改所需的“manageUsers”权限）的文档中。  
  
在这个示例中，名为“gg”的低权限用户将“Support”群组添加到了文档中。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibcqp78c8rAy5bRHWxN3tFliaFgeTSibJlBTJXqibKu10zrfhkicdp7uwFziatJE4FBwqIj9mAUUl7dxE1ooqskyBMIZ5PZSoQxP8MZU/640?wx_fmt=png&from=appmsg "")  
  
Outline 项目在三天内就修复了这个问题以及我们报告的另一个问题！(仓库安全公告[13])  
### 购物车末日漏洞 (CVE-2025-15033, CVE-2026-25758)  
  
直到我们把任务流对准清单上的第一个在线商店，我们才意识到会在电商应用的购物车逻辑里发现什么系统性的问题。在基于 PHP 的 WooCommerce 项目里，任务流立马找到了一种方法，让正常登录的商店用户可以查看所有访客订单——包括个人身份信息（姓名、地址和电话号码）。我们报告之后，Automattic（WooCommerce 背后的公司）很快发布了更新（CVE-2025-15033[14]）和相关的博客文章[15]。  
  
我们对那个漏洞产生了兴趣，于是把更多的电商应用加到了我们智能体要审计的应用列表里。果然，我们发现了更多漏洞。流行的基于 Ruby 的 Spree commerce[16] 应用包含了两个类似的漏洞（CVE-2026-25758[17]和 CVE-2026-25757[18]）。更严重的那个允许未认证用户通过基本上就是递增一个顺序号，来枚举所有访客订单的地址（和电话号码）。  
  
在这张截图中，攻击者“test66”将他们的会话关联到了一个访客用户的现有地址上，从而能够查看完整的地址和电话号码。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdfZw4vbkM4z6VeIoq6KkFG2CwnnK7YD5ThKjEVkZEmv2Xxvn0uIWzJZia2IYyQSrk0YhCmJtBJusBhCxdjlJ7gTD7SibSvr3yQY/640?wx_fmt=jpeg&from=appmsg "")  
  
我们在 Spree 的挖洞之旅并没停止。我们的任务流在另外两个电商应用里发现了类似的问题。  
  
这些授权逻辑漏洞已经存在好几年了。  
### 用任何密码登录 Rocket.Chat（CVE-2026-28514[19]）  
>   
  
  
时不时地，你会不敢相信自己的眼睛。我们的任务流在 Rocket.Chat 里的这个发现就是那种时刻。  
  
当你的智能体带着这样一段备注回来：  
>   
  
  
你一开始可能很难相信。  
  
当你继续往下读输出：  
>   
>   
>   
>   
>   
> 没有  
>   
>   
>   
  
  
你可能觉得有点道理了，但还是不太信。  
  
结果发现，疑似的问题出现在 Rocket.Chat 基于微服务的架构中。在那个特定部署中，Rocket.Chat 通过其 DDP Streamer 服务暴露了用户账户服务。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcAV8DtRKl07ibzLOx8p57mCPvtrSPnl0fSQp46rfFkybZq56s5dzhQIR5s5HG20sDricFnSDnDq16ELRXibJaLqQSKfAN0EnE84M/640?wx_fmt=png&from=appmsg "")  
  
一旦我们的 Rocket.Chat 测试环境正常运行，我们就得写漏洞利用的概念验证代码。智能体的备注里已经包含了我们可以用来通过 Meteor 的 DDP 协议连接到端点的 JSON 结构。  
  
我们连接到了 DDP streamer 服务的 WebSocket 端点，然后：真的可以只用任何密码就登录到暴露的 Rocket.Chat DDP 服务里。一旦登录，还能执行其他操作，比如连接到任意聊天频道，并监听这些频道里的消息。  
  
这里，在监听“General”频道时，我们收到了消息“HELLO WORLD!!!”。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf03q2s0K2PWICibmnmHdTrJ3JCbo9OmuHO2oWNyHYtDjgrdkqzVG2QVDlgKwuxd3SHK96eVvIxrSgQrLSXVWXabiadqVI0icbqwY/640?wx_fmt=jpeg&from=appmsg "")  
  
这个问题的技术细节挺有意思（也挺吓人的）。Rocket.Chat 主要是一个基于 TypeScript 的 Web 应用，它用 bcrypt 来存储本地用户密码。那个用来比较密码和存储哈希的函数 `bcrypt.compare` 返回一个 Promise[20]——这个事实也反映在 Rocket.Chat 自己的 `validatePassword` 函数上，它返回一个 Promise：  
  
export const validatePassword = (password: string, bcryptPassword: string): Promise =>    bcrypt.compare(getPassword(password), bcryptPassword);  
  
然而，在使用这个函数时，Promise 的值没有被解析（比如在 validatePassword 前面加个 await 关键字）：  
  
const valid = user.services?.password?.bcrypt && validatePassword(password, user.services.password.bcrypt);if (!valid) {    return false;}  
  
这导致 `validatePassword` 的结果与 true 进行了 AND 运算。按照 JavaScript 的说法，返回的 Promise 总是“truthy”，所以当用户设置了 bcrypt 密码时，布尔值 `valid` 随后总是 true。  
  
抛开严重性不谈，LLM 能抓住这个相当细微的 bug，追踪多个文件，并得出正确结论，这本身就很有意思。  
## 我们学到了什么  
  
在超过40个仓库（大部分是多用户 Web 应用）上运行任务流之后，LLM 建议了 1,003 个问题（潜在漏洞）。  
  
经过审计阶段，139 个被标记为存在漏洞，意思是 LLM 认为它们可以被利用。在问题去重之后——去重是必要的，因为每个仓库平均跑了几次，结果会汇总——我们剩下 91 个漏洞，我们决定在报告前手动检查一遍。  
- 我们拒绝了 20 个 (22%) 结果，它们被归为**误报（FP）**：我们手动无法复现。  
- 我们拒绝了 52 个 (57%) 结果，认为**严重性低**：潜在影响非常有限的问题（比如，只返回 HTTP 状态码的盲 SSRF；需要在安装阶段就有恶意管理员的问题等等）。  
- 我们只保留了 19 个 (21%) 结果，认为这些漏洞影响足够大可以报告，全部是严重漏洞，其中大部分是高危或严重严重性（比如，不需要特定条件就能触发的、影响机密性或完整性的漏洞，像个人数据泄露、系统设置被覆盖、账户接管等）。  
这些数据是使用 `gpt-5.x` 作为代码分析和审计任务的模型时收集的。  
>   
  
<table><thead><tr><th>问题类别</th><th>总建议数</th><th>有漏洞数</th><th>漏洞率</th></tr></thead><tbody><tr><td>IDOR/访问控制问题</td><td>241</td><td>38</td><td>15.8%</td></tr><tr><td>XSS</td><td>131</td><td>17</td><td>13.0%</td></tr><tr><td>CSRF</td><td>110</td><td>17</td><td>15.5%</td></tr><tr><td>认证问题</td><td>91</td><td>15</td><td>16.5%</td></tr><tr><td>安全配置错误</td><td>75</td><td>13</td><td>17.3%</td></tr><tr><td>路径遍历</td><td>61</td><td>10</td><td>16.4%</td></tr><tr><td>SSRF</td><td>45</td><td>7</td><td>15.6%</td></tr><tr><td>命令注入</td><td>39</td><td>5</td><td>12.8%</td></tr><tr><td>远程代码执行</td><td>24</td><td>1</td><td>4.2%</td></tr><tr><td>业务逻辑问题</td><td>24</td><td>6</td><td>25.0%</td></tr><tr><td>模板注入</td><td>24</td><td>1</td><td>4.2%</td></tr><tr><td>文件上传处理问题（不包括路径遍历）</td><td>18</td><td>2</td><td>11.1%</td></tr><tr><td>不安全反序列化</td><td>17</td><td>0</td><td>0.0%</td></tr><tr><td>开放式重定向</td><td>16</td><td>0</td><td>0.0%</td></tr><tr><td>SQL注入</td><td>9</td><td>0</td><td>0.0%</td></tr><tr><td>敏感数据暴露</td><td>8</td><td>0</td><td>0.0%</td></tr><tr><td>XXE</td><td>4</td><td>0</td><td>0.0%</td></tr><tr><td>内存安全</td><td>3</td><td>0</td><td>0.0%</td></tr><tr><td>其他</td><td>66</td><td>7</td><td>10.6%</td></tr></tbody></table>  
如果我们将发现大致分为两类——逻辑问题（IDOR、认证、安全配置错误、业务逻辑问题、敏感数据暴露）和技术问题（XSS、CSRF、路径遍历、SSRF、命令注入、远程代码执行、模板注入、文件上传问题、不安全反序列化、开放式重定向、SQL注入、XXE、内存安全）——我们得到 439 个逻辑问题和 501 个技术问题。虽然技术问题建议得更多，但差别不大，因为一些宽泛的类别（比如远程代码执行和文件上传问题）根据攻击场景也可能涉及逻辑问题。  
  
只有三个被建议的问题涉及内存安全。这不奇怪，因为测试的大多数仓库都是用内存安全语言写的。但我们怀疑当前的任务流在发现内存安全问题上可能效率不高，特别是与其他自动化工具（比如模糊测试工具）相比。这是一个有趣的领域，通过创建更具体的任务流，并向 LLM 提供更多工具（如模糊测试器），可以在这方面进行改进。  
  
这些数据让我们得到了以下观察。  
### LLM 特别擅长发现逻辑漏洞  
  
数据中突出的是“业务逻辑问题”25%的漏洞率，以及大量的 IDOR 问题。事实上，被标记为存在漏洞的 IDOR 问题总数，超过了后面两个类别（XSS 和 CSRF）之和。总的来说，我们感觉 LLM 在理解代码空间、跟踪控制流、同时考虑应用的访问控制模型和预期用途方面做得非常好，这或多或少符合我们对于擅长代码审查等任务的 LLM 的期望。这也让它非常擅长发现传统工具难以发现的逻辑漏洞。  
### LLM 擅长拒绝低严重性问题和误报  
  
有趣的是，没有一个误报是我们认为的幻觉。所有的报告，包括误报，都有合理的证据支持，我们能够跟踪报告找到端点并应用建议的载荷。许多误报是由于代码之外更复杂的环境造成的，比如上面提到的针对 XSS 问题的浏览器缓解措施，或者我们认为的、人类审计员也可能犯的真正的错误。比如，当存在多层认证时，LLM 有时会漏掉某些检查，导致误报。  
  
我们后来测试了更多仓库，报告了更多漏洞，但漏洞与仓库之间的比例大致保持不变。  
  
为了展示任务流的可扩展性，以及如何将额外信息融入任务流，我们创建了一个新的任务流[21]，在审计阶段之后运行，它融入了我们新获得的知识来过滤掉低严重性漏洞。我们发现这个任务流可以过滤掉大约 50% 的低严重性漏洞，我们报告的一些边界漏洞也被标记为低严重性了。任务流和提示词可以根据用户自己的偏好进行调整，但对我们来说，我们更愿意让它包容性更强些，以免漏掉任何有影响的东西。  
### LLM 擅长威胁建模  
  
总体来说，LLM 在威胁建模方面表现良好。在实验期间，我们用它测试了许多具有不同威胁模型的应用，比如桌面应用、多租户 Web 应用、设计在沙盒环境中运行代码的应用（设计上允许代码注入），以及反向代理应用（SSRF 行为是预期的应用）。任务流能够考虑到这些应用的预期用途，并做出合理的决策。任务流在桌面应用的威胁建模上最吃力，因为通常不清楚用户桌面上的其他进程是否应被视为可信的。  
  
我们也观察到 LLM 进行了一些出色的推理，排除了那些无法带来权限提升的问题。例如，在一个案例中，LLM 注意到虽然访问控制存在不一致，但这个问题并没有给攻击者带来超出手动复制粘贴操作的优势：  
>   
>   
>   
>   
> 只要他们在目标集合上也拥有 updateDocument 权限  
>   
> 这并没有授予他们对其他文档的额外访问权限，也没有绕过原文档的保护措施  
>   
  
  
我们还看到一些在推理中使用的更复杂的技术。例如，在一个在沙盒化 nodejs 环境中运行脚本的应用中，LLM 提出了以下逃逸沙盒的技术：  
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
>   
  
### 参考资料  
  
[1]   
https://securitylab.github.com/ai-agents/  
  
[2]   
https://github.com/features/copilot/plans  
  
[3]   
https://github.com/GitHubSecurityLab/seclab-taskflows  
  
[4]   
https://github.com/GitHubSecurityLab/seclab-taskflow-agent  
  
[5]   
https://github.blog/security/ai-supported-vulnerability-triage-with-the-github-security-lab-taskflow-agent  
  
[6]   
https://github.com/GitHubSecurityLab/seclab-taskflows/blob/4d8c3db928d131172337eead7c64874a67e59c38/src/seclab_taskflows/prompts/audit/audit_issue.yaml#L16-L18  
  
[7]   
https://github.com/GitHubSecurityLab/seclab-taskflows/blob/4d8c3db928d131172337eead7c64874a67e59c38/src/seclab_taskflows/taskflows/audit/gather_web_entry_point_info_local.yaml#L25  
  
[8]   
https://github.com/GitHubSecurityLab/seclab-taskflows/blob/4d8c3db928d131172337eead7c64874a67e59c38/src/seclab_taskflows/taskflows/audit/classify_application_local.yaml#L50-L55  
  
[9]   
https://github.com/GitHubSecurityLab/seclab-taskflows/blob/4d8c3db928d131172337eead7c64874a67e59c38/src/seclab_taskflows/taskflows/audit/classify_application_local.yaml#L78  
  
[10]   
https://github.com/GitSecurityLab/seclab-taskflows/blob/4d8c3db928d131172337eead7c64874a67e59c38/src/seclab_taskflows/prompts/audit/audit_issue.yaml#L9  
  
[11]   
https://securitylab.github.com/advisories/  
  
[12]   
https://www.getoutline.com/  
  
[13]   
https://github.com/outline/outline/security/advisories/GHSA-c8xf-3j86-7686  
  
[14]   
https://github.com/advisories/GHSA-q45j-x3cj-gjvq  
  
[15]   
https://developer.woocommerce.com/2025/12/22/store-api-vulnerability-patched-in-woocommerce-8-1/  
  
[16]   
https://spreecommerce.org/  
  
[17]   
https://github.com/spree/spree/security/advisories/GHSA-87fh-rc96-6fr6  
  
[18]   
https://github.com/spree/spree/security/advisories/GHSA-p6pv-q7rc-g4h9  
  
[19]   
https://github.com/RocketChat/Rocket.Chat/security/advisories/GHSA-w6vw-mrgv-69vf  
  
[20]   
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise  
  
[21]   
https://github.com/GitHubSecurityLab/seclab-taskflows/blob/f7db21ea6aa250373249a5225e1c63b4ea27da2e/src/seclab_taskflows/taskflows/audit/filter_severity.yaml#L1  
  
[22]   
https://github.blog/security/how-to-scan-for-vulnerabilities-with-github-security-labs-open-source-ai-powered-framework/  
  
