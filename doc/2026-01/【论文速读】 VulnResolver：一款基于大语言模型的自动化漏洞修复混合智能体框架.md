#  【论文速读】| VulnResolver：一款基于大语言模型的自动化漏洞修复混合智能体框架  
原创 知识分享者
                    知识分享者  安全极客   2026-01-29 09:35  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/vWuBpewLia8QmTLhv0jB8GS6Wtic69pG44V8Gib7ccD3FZolnOVkdOPafA3YULibw9S5AEkdO8sstRLGNFVDj7SgRg/640?wx_fmt=jpeg&from=appmsg "")  
  
**基本信息**  
  
  
原文标题：VulnResolver: A Hybrid Agent Framework for LLM-Based Automated Vulnerability Issue Resolution  
  
原文作者：Mingming Zhang, Xu Wang, Jian Zhang, Xiangxin Meng, Jiayi Zhang, Chunming Hu  
  
作者单位：Beihang University (Mingming Zhang, Xu Wang, Jian Zhang, Xiangxin Meng, Chunming Hu); Nanyang Technological University (Jiayi Zhang)  
  
关键词：automated vulnerability repair, LLM-based framework, hybrid agent system, context pre-collection, safety property analysis, SEC-bench  
  
原文链接：https://arxiv.org/abs/2601.13933  
  
开源代码：暂无  
  
  
**论文要点**  
  
  
论文简介：随着软件系统规模日益庞大且高度互联，安全漏洞的出现频率显著增加，给系统安全性和经济成本带来了严重威胁。尽管自动化检测工具（如fuzzer）已取得长足进步，能够发现大量漏洞，但漏洞的有效修复仍高度依赖人工专家经验。现有的自动化漏洞修复（Automated Vulnerability Repair, AVR）方法大多严重依赖人工提供的额外标注，例如故障位置或CWE类别标签，这些信息获取困难且耗时，同时普遍忽略了开发者在问题报告（issue report）中自然嵌入的丰富语义上下文，这些上下文往往包含理解和修复漏洞的关键线索。  
  
本文提出了 VulnResolver，这是首个基于大语言模型（LLM）的混合代理框架，专门用于自动化漏洞问题解决（automated vulnerability issue resolution）。VulnResolver 通过两个高度特化的代理，将自主代理的灵活适应性与确定性工作流引导的修复稳定性相结合：上下文预收集代理（Context Pre-Collection Agent, CPCAgent）能够自适应地探索目标代码仓库，收集依赖关系和相关上下文信息；安全属性分析代理（Safety Property Analysis Agent, SPAAgent）则负责推断、生成并验证被漏洞违反的安全属性（safety properties），从而深入揭示漏洞的语义根因。这两个代理共同生成结构化的分析报告，与原始问题报告融合，形成显著增强的问题描述，进而驱动更精准的漏洞定位和补丁生成。在 SEC-bench 基准测试中，VulnResolver 在 SEC-bench Lite 子集上成功修复了 75% 的漏洞问题，取得了最佳性能；在完整 SEC-bench 上也大幅超越当时最强的基线方法（基于代理的 OpenHands），充分证明了其在真实世界端到端自动化漏洞修复任务中的有效性与安全性意识。  
  
研究目的：现有软件工程（SWE）系统和自动化漏洞修复方法在处理真实世界安全漏洞时面临两大核心挑战：  
  
首先，当前主流的 SWE 范式可分为两类：基于代理的系统（如 SWE-agent）依赖 ReAct 循环自主决策，具有高度灵活性，但容易出现非确定性规划、在庞大动作空间中探索不足，导致补丁生成不完整或直接放弃；基于工作流的系统（如 Agentless）采用确定性流水线，具有更高的稳定性，但严重依赖单一问题报告进行上下文构建，完全放弃了代码仓库级别的自适应探索，难以获取足够丰富的上下文信息用于精确修复。因此，亟需一种混合范式，将工作流的稳定性与代理的针对性仓库探索能力相结合。  
  
其次，现有的 SWE 系统主要针对通用软件缺陷设计，缺乏针对安全漏洞独特特性的专门机制。安全漏洞本质上是程序违反了某些关键的安全约束（security constraints），这些约束可以形式化为“程序执行过程中某些坏事永远不会发生”的安全属性（safety properties）。尽管安全属性已在漏洞检测领域得到应用，但在 LLM 驱动的 SWE 系统和最新 AVR 方法中仍未被充分探索和利用，现有方法（如 PatchAgent、SAN2PATCH）缺乏显式编码或利用漏洞特有约束的组件，导致修复缺乏原则性与安全性保证。  
  
因此，本文的研究目的在于：提出一种全新的、专门面向真实世界漏洞问题的端到端自动化解决框架 VulnResolver，通过融合确定性工作流与特化代理能力，同时引入仓库自适应上下文收集和基于安全属性的语义根因分析，实现更准确、更安全、更具原则性的自动化漏洞修复，填补现有方法在语义理解、上下文完备性和安全性意识上的关键空白。  
  
研究贡献  
  
- 研究方向：据研究者所知，VulnResolver 是首个系统性地探索“自动化漏洞问题解决”（automated vulnerability issue resolution）的研究工作，能够直接、自主地处理真实世界漏洞问题报告，从而为自动化漏洞修复（AVR）开辟了全新的研究方向。同时，本文首次提出“混合代理范式”（hybrid agent paradigm），将工作流的稳定性与代理的灵活性有机结合，共同推动基于 LLM 的软件工程向更实用、更自主、更具安全意识的程序修复方向迈进。  
  
- 核心技术：提出了 VulnResolver，一个基于 LLM 的混合代理系统，它将确定性工作流与两个特化代理深度集成：上下文预收集代理（CPCAgent）负责自适应仓库探索，安全属性分析代理（SPAAgent）负责基于属性的漏洞语义推理。通过上下文获取与属性级语义理解的结合，VulnResolver 构建出显著增强的问题报告，从而驱动更有效的漏洞定位和补丁生成。  
  
- 全面实验验证：在首个针对该任务的标准基准 SEC-bench 上开展了大规模实验。VulnResolver 在所有基线中表现最佳，在 SEC-bench Lite 上较基础工作流提升 53.8%（75.0% vs. 48.8%）；在 SEC-bench Full 上展现出强泛化能力，大幅超越排行榜最佳系统。进一步的消融实验验证了每个代理及整体框架设计的有效性，充分证实了所提方法的优越性。  
  
  
  
  
**引言**  
  
  
真实世界软件项目日益复杂且高度互联，导致安全漏洞的发生率显著上升，这些漏洞不仅提升了安全风险，还带来了巨大的经济成本。因此，及时缓解这些漏洞对于维护软件的安全性和可靠性至关重要。诸如模糊测试（fuzzing）等漏洞检测技术已在实践中发现了数千个漏洞，漏洞发现者通常通过提交问题报告（issue report）来通知维护者，例如NJS-482。尽管自动化检测取得了进步，但正确且有效地修复这些问题仍高度依赖人类专家的专业知识，这激发了自动化漏洞修复方法的开发。  
  
自动化程序修复（Automated Program Repair, APR）旨在自动修复软件缺陷，基于大语言模型（LLM）的APR方法已展现出强劲性能。SWE-bench的引入进一步推动了全自动化问题解决，激发了多种SWE系统用于真实世界缺陷修复。在漏洞领域，一些自动化漏洞修复（Automated Vulnerability Repair, AVR）方法减少了手动努力并实现了自动化缓解，但许多方法（如VRepair、VulRepair、APPATCH）仍需要人工提供的故障位置或CWE标签，这些标注获取困难且耗时。像PatchAgent和SAN2PATCH这样的方法虽然从 sanitizer 日志自动化了定位和修复，但忽略了问题报告中的语义上下文，这些上下文往往包含理解和修复漏洞的关键线索。这种差距激发了开发能够直接利用结构化和语义洞见的系统来解决漏洞问题。  
  
然而，有效的漏洞解决仍面临挑战。首先，当前SWE范式可大致分为基于代理的框架（如SWE-agent）和基于工作流的框架（如Agentless），各自有明显的优势和局限性。基于代理的系统利用ReAct范式迭代调用工具，每个LLM代理基于先前推理和工具反馈选择后续动作。尽管灵活，但它们往往受非确定性规划和在大动作空间中的次优探索影响，经常产生不完整或放弃的补丁。相反，基于工作流的系统使用确定性流水线进行定位和修复，避免了不受控的代理行为，实现更高的稳定性。然而，Agentless仅依赖问题报告进行漏洞定位和上下文构建，完全放弃了仓库级别的自适应探索，限制了其获取足够上下文信息以实现准确修复的能力。因此，一个有前景的方向是结合两种范式的优势：一个混合代理系统，在确定性工作流下运行，同时通过代理启用针对性仓库探索。  
  
其次，现有的SWE系统主要针对通用软件问题，缺乏针对安全漏洞独特特性的设计。漏洞往往源于违反特定安全约束，例如CWE-125（越界读取）通常发生在有界缓冲区被超出有效索引范围访问时，违反了索引必须保持在界内的约束。此类约束可形式化为安全属性，这些属性规定程序执行过程中“某些坏事永不发生”。尽管安全属性已在漏洞检测中得到利用，但它们在SWE系统和最近的基于LLM的AVR方法中仍未得到充分探索。例如，PatchAgent和SAN2PATCH虽然关注端到端漏洞修复，但没有融入显式编码或利用漏洞特定约束的设计组件。因此，将安全属性推理融入漏洞问题解决中，对于实现更原则、更有效且更具安全意识的自动化修复至关重要。  
  
本文提出VulnResolver，一个基于LLM的框架，专为自动化漏洞问题解决而设计。1）结合代理灵活性和工作流确定性，VulnResolver基于Agentless风格的问题解决工作流，同时通过特化代理集成自适应工具调用能力，形成混合代理式自动化问题解决框架。工作流驱动结构确保了关键修复阶段（如漏洞定位、补丁生成和补丁选择）的稳定性和一致性，而代理通过针对性仓库探索增强了适应性和上下文理解。通过维护确定性工作流骨干，VulnResolver避免了全代理或多代理系统中的不受控决策漂移。2）针对自适应上下文获取，研究者引入上下文预收集代理（CPCAgent），它利用一套基于静态分析的代码搜索和符号解析工具，对目标仓库进行结构化探索。在LLM推理指导下，CPCAgent逐步收集相关上下文信息，直至达到充分覆盖，然后将收集的上下文和派生洞见合成全面的上下文分析报告（报告I）。这一过程赋予工作流仓库意识，并增强后续定位和修复过程。3）捕捉漏洞特性，VulnResolver融入安全属性分析代理（SPAAgent），它运用静态分析和动态执行工具来推断、生成和验证描述安全程序行为的安全属性。具体而言，SPAAgent探索易受攻击的代码库和概念证明（PoC）执行来假设潜在安全属性，用这些属性对仓库进行插桩，并通过引导PoC重新执行进行验证。然后，代理基于验证结果迭代精炼其属性假设，实现对漏洞根因的更深语义理解。一旦收敛，SPAAgent生成属性分析报告（报告II），封装生成的属性及其安全含义。  
  
最终，VulnResolver将问题报告与两个代理生成的报告（报告I和报告II）整合成增强的问题报告，汇总仓库探索和安全属性推理的洞见。这一丰富输入改善了定位和补丁生成，将工作流确定性与代理推理统一，形成原则、自适应且具安全意识的AVR系统。研究者在SEC-bench上进行了广泛实验，以评估VulnResolver的有效性。遵循其原论文的评估协议，研究者构建了两个基准变体：SEC-bench Lite和SEC-bench Full。VulnResolver在SEC-bench Lite上成功解决75%的issues，取得最佳性能；完整VulnResolver配置较基础工作流提升53.8%（75.0% vs. 48.8%），证明了整体设计的有效性。SEC-bench Full上的泛化实验显示VulnResolver成功解决67.5%的issues，比最佳排行榜基线OpenHands+Claude-3.7-Sonnet提升98.5%，比基础工作流提升37.8%，进一步确认了研究者的方法。主要贡献总结如下：方向（首个探索自动化漏洞问题解决，并引入混合代理范式）；技术（提出VulnResolver，集成确定性工作流与两个特化代理）；全面研究（在SEC-bench上超越所有基线，并通过消融研究验证设计有效性）。  
  
  
**VulnResolver框架详解**  
  
  
VulnResolver是一个基于大语言模型（LLM）的混合代理框架，用于自动化漏洞问题解决，它结合了代理系统的适应性和工作流驱动修复的稳定性。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8TA41ibjxK4XH69C9pGKLGBSDzkE7uhRjDsjCicyrvqSafcjxF5vSc6DFKQYpKgZr0u8bFk8X68E70g/640?wx_fmt=png&from=appmsg "")  
  
如图1所示，VulnResolver将两个特化代理集成到框架中，每个代理配备工具包，在目标仓库的沙箱环境中运行。这些代理包括上下文预收集代理（CPCAgent）和安全属性分析代理（SPAAgent），共同增强漏洞分析和修复。具体而言，CPCAgent使用静态分析工具自适应探索目标代码库，收集与漏洞相关的关键上下文信息，生成上下文分析报告（报告I）。相反，SPAAgent利用静态分析和动态执行工具，迭代分析、生成、插入和验证描述安全程序行为的安全属性，最终产生属性分析报告（报告II）。将这两个报告与原始问题报告结合，形成增强的问题报告（a）。这一增强报告随后作为基础工作流（Section 2.5）的输入，包括漏洞定位（b）、补丁生成（c）和补丁选择（d）阶段。通过将代理的自适应能力与结构化工作流集成，VulnResolver形成了一个针对真实世界AVR的有效框架。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8TA41ibjxK4XH69C9pGKLGBSFkzbUNF6KHEPibKQeaHbmSsRUzGumchTcEo09SbuQ3CkjXNicGEib8G0A/640?wx_fmt=png&from=appmsg "")  
  
代理工具包（Section 2.2）：为了支持CPCAgent和SPAAgent，研究者设计了一系列工具包，作为代理的动作集成。这些工具包使代理能够分析漏洞并实现其目标：上下文预收集和安全属性生成。如表1所示，包括：(1) 代码搜索工具包，用于在目标仓库中搜索和读取源代码；(2) 代码符号分析工具包，用于解析代码依赖（如查找函数定义）；(3) PoC执行工具包，用于在控制环境中编译仓库并运行PoC；(4) 项目编辑工具包，用于修改仓库以插入或修复安全属性，支持Git提交和回滚；(5) Python代码执行工具包，用于运行代理生成的Python代码，进行轻量分析（如处理长日志），在隔离的Docker中运行以防不安全操作。  
  
上下文预收集代理（CPCAgent, Section 2.3）：CPCAgent负责自适应探索仓库，收集与漏洞相关的上下文信息，生成报告I。它使用ReAct框架迭代调用工具，直到上下文充分。目标是识别漏洞根因，支持后续诊断和修复。可用工具为代码搜索和符号分析工具包（静态分析）。输入包括问题报告和仓库结构（Linux tree-like格式，仅源文件）。分析过程：1) 初始分析检查问题报告，识别触发条件、漏洞类型和崩溃位置；2) 上下文识别确定需要收集的元素（如函数、变量或崩溃周围行）；3) 上下文收集从直接相关代码开始逐步扩展，使用工具检索片段；4) 报告生成合成报告，包括枚举上下文（源代码、来源、注解、解释）和总结洞见。输出为结构化报告，提供仓库意识，弥补工作流不足。  
  
安全属性分析代理（SPAAgent, Section 2.4）：SPAAgent专注于推断和验证安全属性，这些属性描述安全程序行为（如“索引始终在界内”）。它通过程序插桩（插入断言）实现，使用SAFETY_PROPERTY_ASSERT宏编码属性。代理使用ReAct框架迭代精炼属性。目标是生成描述安全行为的属性断言，揭示漏洞语义根因。可用工具为所有五个工具包，支持静态和动态。输入包括问题报告、CPCAgent的报告和仓库结构。分析过程：1) 初始PoC执行无修改运行PoC，观察崩溃；2) 属性假设分析崩溃点，生成初始属性（如边界检查、非空指针），使用编辑工具插入；3) 属性验证运行插桩后的PoC，检查违反，保留相关属性；4) 迭代精炼基于结果向后分析，生成更精确属性，直到收敛；5) 报告生成合成报告，包括枚举属性（断言代码、位置、目的、执行结果、解释）和总结洞见。输出为结构化报告，提供原则性指导。  
  
问题解决工作流（Issue Resolution Workflow, Section 2.5）：工作流是框架骨干，LLM驱动，受Agentless启发，包括四个阶段，确保确定性和效率。1) 报告增强调用两个代理生成报告，与原始报告结合。2) 漏洞定位通过文件定位（提示+检索）和代码元素定位（骨架文件上识别元素）。3) 补丁生成基于增强报告和定位元素，提取完整实现+上下文，LLM生成T个SEARCH/REPLACE补丁。4) 补丁选择应用补丁，运行PoC过滤有效者；规范化（格式化、移除注释）；多数投票选最终补丁，转为Git diff格式。整体流程从报告增强开始，确保适应性和安全性；工作流确定性避免代理漂移。实现细节使用libclang解析C/C++元素，支持多补丁生成（T=5默认）。  
  
  
**实验设置**  
  
  
本节围绕 VulnResolver 的性能验证展开实验设计，共设置三个核心研究问题，分别是对比 VulnResolver 与现有漏洞修复方案的有效性、探究不同设计选型对其修复效果及大语言模型 API 成本的影响、验证其在更多漏洞修复任务中的泛化能力。  
  
实验基于 SEC-bench 基准测试集开展，该数据集源自开源 C/C++ 项目的真实漏洞案例，配备 Docker 镜像与自动化补丁验证工具，包含 200 个覆盖 16 类 CWE 类型的漏洞，分为含 80 个漏洞的精简版与含 200 个漏洞的完整版，分别用于有效性、消融实验与泛化性研究，且两个版本的数据集均有明确的项目数量、漏洞数量及补丁修改统计特征。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8TA41ibjxK4XH69C9pGKLGBSxUTWncjZuuEChKdVcf2C9UTFZ7NPJ0UCSkensmvLJQ7ZR4qjkbODcQ/640?wx_fmt=png&from=appmsg "")  
  
VulnResolver 基于 Python 开发，采用 libclang 解析 C/C++ 代码元素，借助 clangd 实现符号分析，通过 SWE-ReX 与 llm sandbox 保障安全的容器交互与代码执行，基于 LangChain 构建两款专用智能体，选用 DeepSeek-V3.2-Exp 等三款大语言模型作为基础模型并将前者设为默认模型，同时采用 text-embedding-3-small 实现检索式可疑文件定位，遵循 Agentless 的相关配置生成补丁并做标准化处理，最终使用 SEC-bench 的自动化脚本完成性能评估。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8TA41ibjxK4XH69C9pGKLGBSOD8rHRc3gvGXX6iaujydjibFrVNvAmpj17uWlW7QkdB4gw4DicnvYRx3A/640?wx_fmt=png&from=appmsg "")  
  
实验选取 SWE-agent、OpenHands、Aider 三类先进软件工程系统，结合三款大语言模型形成 9 种基线配置，同时纳入 PatchAgent 作为额外基线，为保证对比公平性，还使用 DeepSeek-V3.2-Exp 模型重新评估了三类系统，共形成 13 个基线方案。评估环节则采用修复数量与修复率、平均 API 调用成本两项核心指标，综合衡量工具的修复效果与成本效益。  
  
  
**研究评估**  
  
  
本节围绕三个核心研究问题，结合 SEC-bench 数据集的测试结果，对 VulnResolver 的性能、设计合理性及泛化能力展开全面实验验证与分析。在 RQ1 有效性对比中，基于 SEC-bench 精简版（80 个漏洞）的测试显示，VulnResolver 以 75.0% 的漏洞修复率大幅领先所有基线方案，相较于采用同款 DeepSeek-V3.2-Exp 模型的最优软件工程系统 SWE-agent（37.5%）性能翻倍，较先进自动化漏洞修复方案 PatchAgent 提升 30.43%；即便更换 o3-mini、GPT-4o 模型，其修复率也分别达 57.5%、51.3%，均优于同模型基线。成本方面，其平均单漏洞成本 0.072 美元，每美元可修复约 10 个漏洞，成本效益显著，这一优势源于 DeepSeek-V3.2-Exp 模型的稀疏注意力机制，能大幅降低推理开销，且在 13 个测试项目中 12 个排名第一，仅在 njs 项目位列第二，展现出优异的项目适配性。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8TA41ibjxK4XH69C9pGKLGBSqLp8Fq0LHnPwhp2FCia7u1GpYV8HrZtcSeibqCPe5Myt6CNVPcZicB9Gw/640?wx_fmt=png&from=appmsg "")  
  
针对 RQ2 的消融实验，全面验证了方案各设计模块的必要性与协同价值。双智能体（CPCAgent 与 SPAAgent）协同作用显著，使修复率较基础版本提升 53.8%，其中单启用 CPCAgent 可提升 25.6%，单启用 SPAAgent 提升 41.0%，凸显后者在安全属性分析中的核心作用；两阶段增强机制中，补丁生成阶段增强（+43.6%）比漏洞定位阶段增强（+7.7%）效果更显著，二者结合可实现性能最大化；基于 PoC 的补丁选择策略比简单投票策略修复率高 16.7%，以漏洞报告为输入比消毒器日志修复率高 15.0%，且确定生成 5 个补丁为最优选择，超过该数量后性能趋于平稳，成本却额外上涨 7.0%。同时，方案在 GPT-4o、o3-mini 等不同基础模型下均能稳定提升修复率，工具使用呈现明显阶段化特征 ——CPCAgent 聚焦静态上下文采集，SPAAgent 负责动态属性分析与验证。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8TA41ibjxK4XH69C9pGKLGBSzL2809UvblgW5LUliaTxXjicRRfBeZgNNibtDX9IsVQ6NK9Xs8IVjIo9g/640?wx_fmt=png&from=appmsg "")  
  
在 RQ3 泛化性研究中，基于 SEC-bench 完整版（200 个漏洞、29 个项目）的测试结果表明，VulnResolver 修复率达 67.5%，成功修复 135 个漏洞，较截至论文提交时排行榜最优方案（OpenHands+Claude 3.7 Sonnet，34.0%）性能提升 98.5%，且较自身基础版本提升 37.8%。尽管其完整版修复率略低于精简版，主要因完整版漏洞平均需修改更多文件、代码块及行数，修复难度更高，但仍在 29 个项目中的 23 个表现最优，成本也与精简版测试基本持平（单漏洞 0.0734 美元，基础版 0.0274 美元），充分验证了该方案在复杂、大规模场景下的泛化能力。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8TA41ibjxK4XH69C9pGKLGBSTw0E4FEp5XRdmQP1LhdoLE6C5t4FP0nuRicqz5C6KomGa3icWMmfiboow/640?wx_fmt=png&from=appmsg "")  
  
RQ3（泛化研究）：在SEC-bench Full（200问题）上，VulnResolver解决67.5%（135/200），比排行榜最佳OpenHands + Claude 3.7 Sonnet（34.0%）提升98.5%，比基础工作流（49.0%）提升37.8%。每个项目：在29个中23个最佳，确认泛化。Full解决率低于Lite因问题更复杂（更多修改）。成本：$0.0734/问题，基础$0.0274，保持高效。  
  
评估和分析确认VulnResolver的设计有效，代理和属性推理显著提升性能和泛化，同时保持成本效益。  
  
  
**有效性威胁**  
  
  
有效性威胁包括外部和内部有效性。外部有效性：语言扩展性，研究者的方法仅在C/C++上实现和评估，但可通过适应代理工具包扩展到其他语言，如使用特定于语言的静态分析工具和LSP库（例如Java的Spoon和Eclipse JDT Language Server）。内部有效性：(1) 数据泄露，基准补丁可能与LLM训练数据重叠，为缓解，研究者使用与基线相同的基线模型评估，确保不 unfair 优势；性能显著优于基础工作流，进一步缓解；(2) 超参数选择，大多数超参数（如N、M、温度、块大小）基于Agentless经验，补丁空间大小T=5基于初步实验，其影响在RQ2中探索；(3) 安全威胁，通过在单独Docker容器中隔离PoC和代理生成Python代码执行，防止影响主机；(4) API成本，使用LLM可能增加成本，但研究者评估平均成本/问题，并证明性能提升 justify 额外开销，且比现有LLM-based SWE基线更具成本效益。  
  
相关工作分为软件问题解决和自动化漏洞修复。软件问题解决：自动化程序修复（APR）旨在自动修复缺陷，包括问题解决子集。基于LLM的APR方法表现出色，SWE-bench推动了SWE系统的发展，可分为代理-based（如SWE-agent、OpenHands，使用工具交互环境）和工作流-based（如Agentless，通过定位和生成步骤）。研究者的方法结合两者，形成混合代理系统，平衡灵活性和确定性。其他如SWE-bench Multimodal评估多模态问题，GUIRepair使用无代理框架；AGENTISSUE-BENCH评估代理解决其他代理问题。研究者聚焦漏洞问题解决，在SEC-bench上评估，取得SOTA。自动化漏洞修复（AVR）是APR子集，聚焦漏洞修复。基于LLM的AVR方法需人工标注（如VRepair、VulRepair、APPATCH），PatchAgent和SAN2PATCH自动化但忽略报告语义上下文，且缺乏AVR特定设计，与通用APR类似。研究者聚焦漏洞违反安全属性的特性，SPAAgent迭代理解和生成属性，提供更深洞见，显著优于无属性分析的变体。预LLM时代AVR如Senx使用符号执行，但仅支持预定义类型、缺乏语义理解、路径爆炸问题。研究者放弃符号执行，转而用LLM代理编辑和动态执行PoC，实现迭代反馈。总之，研究者结合通用探索与漏洞特定属性分析，实现有效且特定于漏洞的修复。  
  
  
**论文结论**  
  
  
本研究提出了一种全新的自动化漏洞问题修复方案 ——VulnResolver，该方案兼具智能体系统的灵活性与工作流驱动修复方案的稳定性。具体而言，VulnResolver 集成了两款专用智能体，分别用于自适应上下文预采集与基于安全属性的推理，可实现更高效的漏洞定位与补丁生成。实验结果表明，VulnResolver 的性能显著优于现有方案，充分验证了本方案在真实场景漏洞修复任务中的有效性。  
  
-End-  
  
[](https://mp.weixin.qq.com/s?__biz=MzkzNDUxOTk2Mw==&mid=2247495405&idx=1&sn=67249648d5c312b5c178b23b077d28f3&scene=21#wechat_redirect)  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8R7Rm0KL55HCcIiasO8JJ7IibXzYxx3losWVb2eddxdClACzWxWtQLwl0wkAl1ZLibcESVWvx5dCeibtQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/vWuBpewLia8QRqLMRicZIN6VJg0ue41W1HVSmDpDqkj86j5SNicNE3X5KkPgcdv1ZmxM7FXrFUdkBes8dpos7d27w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4 "")  
  
