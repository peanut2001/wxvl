#  LLM4VFD：基于大语言模型的多源信息融合漏洞修复检测框架  
原创 SecureNexusLab
                    SecureNexusLab  SecureNexusLab   2026-02-26 09:59  
  
   
## 1. 研究背景 (Research Background)  
  
近年来，随着开源软件（OSS）在软件开发中的广泛应用，其安全性问题日益凸显。漏洞修复检测旨在识别代码仓库中用于修复安全漏洞的提交（即漏洞修复提交），是保障软件供应链安全、实现快速漏洞缓解的关键环节。然而，在协调漏洞披露（CVD）模型下，漏洞修复提交的集成与公开披露之间存在时间差，为恶意攻击者提供了利用窗口。因此，自动化、准确地检测漏洞修复提交对于OSS用户至关重要。  
  
尽管已有一些自动化方法被提出，但它们存在显著局限性。例如，VulFixMiner和CoLeFunDa等方法仅聚焦于分析代码变更本身，忽略了关联的开发工件（如问题报告、拉取请求）所提供的上下文信息。而Vulcurator虽然集成了问题报告，但未能有效利用不同开发工件之间的语义关联，且无法处理混合了多种修改意图的“纠缠提交”。更为关键的是，现有方法仅提供二元预测结果，缺乏对决策背后逻辑的解释，这极大地限制了其在需要专业安全知识进行验证的实际场景中的应用。  
  
基于此，本文提出LLM4VFD，一个利用大语言模型（LLM）增强的、融合多源信息的漏洞修复检测框架。该框架不仅旨在提升检测精度，更致力于生成详细的解释性分析，以辅助安全专家理解与验证。  
## 2. 研究挑战 (Research Challenges)  
  
现有方法在实现高精度、可解释的漏洞修复检测时，面临三个核心且层层递进的挑战，其根源在于对复杂上下文的建模不足。  
  
**挑战一：纠缠提交中的噪声干扰。**  
 在实际开发中，一个提交可能包含多种目的的代码修改（如重构、功能增强、漏洞修复）。例如，如图1所示，一个包含164行变更的提交中，仅有2行与漏洞修复相关。现有基于代码变更分析的方法（如VulFixMiner）难以从大量无关修改中准确识别出安全相关的微小变更，因为这些无关变更构成了严重的噪声，导致模型难以聚焦于真正的漏洞修复意图。  
  
![Fig. 1. An example of tangled commit with 164 lines changed, while only two lines (in red box) are related to vulnerability fix. [60]](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYA9q2gx7BMz5GW8v9iaEFOKvpVq57dpicoZMQO52Sbs1MiaojSyUJMOibiaA/640?wx_fmt=png&from=appmsg "null")  
  
Fig. 1. An example of tangled commit with 164 lines changed, while only two lines (in red box) are related to vulnerability fix. [60]  
  
**挑战二：提交内部信息不足。**  
 许多提交的提交信息模糊（如“fixed [#2475”]()  
），且代码变更本身可能非常细微（如仅增加一个条件检查），如图2所示。仅凭提交消息和代码差异，即使是人类专家也难以判断其是否为漏洞修复。然而，关联的开发工件（如问题报告[#2475]()  
）往往包含了关于安全漏洞的详细描述，这些关键上下文信息在现有方法中被忽视，导致大量漏报。  
  
![Fig. 2. An example of a commit [21] with only 2 lines changed (in red box), while related issues reports [22] (in blue box) provided critical information.](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYPoib7yRvDrrr6yvbS1A51UAnME67JqpcicKAxTEB5WicXaRibDXWR5Xkrw/640?wx_fmt=png&from=appmsg "null")  
  
Fig. 2. An example of a commit [21] with only 2 lines changed (in red box), while related issues reports [22] (in blue box) provided critical information.  
  
**挑战三：项目特定上下文知识的缺失。**  
 准确判断一个提交是否修复漏洞，通常需要理解项目特定的领域知识或历史模式。例如，一个为setProperty  
函数添加原型污染检查的小修改，其意图难以从表面判断。然而，如果能在该项目的历史提交中找到类似的、已确认为漏洞修复的变更（如图3所示），则能为当前提交的判断提供强有力的类比依据。现有方法缺乏利用此类历史漏洞修复模式的能力。  
  
![Fig. 3. A commit only with small change by adding condition check (left [55]) and its relevant historical vulnerability fix commit (right [54]).](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYOM27U942sHa76iaN3ibnrOxnCwL8It8vOQiamIwLwm9ApCeHtq60xRIJw/640?wx_fmt=png&from=appmsg "null")  
  
Fig. 3. A commit only with small change by adding condition check (left [55]) and its relevant historical vulnerability fix commit (right [54]).  
## 3. LLM4VFD框架设计 (LLM4VFD Design)  
  
LLM4VFD是一个基于提示工程，融合代码变更意图、开发工件和历史漏洞信息，以提升LLM漏洞修复检测性能并生成解释性分析的框架。其核心设计如图4所示，包含四个协同工作的组件，分别针对上述三个挑战。  
  
![Fig. 4. The framework of LLM4VFD. 4 Methodology](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYS8BIJLb5zhEMlhib3pcIPrtaKVQMm6p0oltkq45zgbkXMGePNicQIoWg/640?wx_fmt=png&from=appmsg "null")  
  
Fig. 4. The framework of LLM4VFD. 4 Methodology  
  
**1. 代码变更意图（CCI）组件：**  
 该组件旨在解决挑战一（纠缠提交）。其核心功能是使用链式思维（CoT）推理技术，引导LLM分析原始提交数据（代码差异和提交信息），并生成一个结构化的“三方面摘要”，包括：代码变更摘要、变更目的以及变更影响。通过聚焦于抽象的“意图”而非原始的、可能包含噪声的代码行，CCI组件能够有效过滤无关修改，提炼出与安全相关的核心信息。其提示模板设计如图5所示，通过分步推理确保分析的深度和结构化。  
  
![Fig. 5. The prompt template of Code Change Intention.](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYPMofnOUSygS0evFtQ3X0tCzmiaJB82pELooxnPHAHh8RFC8ocwLmiccA/640?wx_fmt=png&from=appmsg "null")  
  
Fig. 5. The prompt template of Code Change Intention.  
  
**2. 开发工件（DA）组件：**  
 该组件旨在解决挑战二（信息不足）。它自动提取与当前提交关联的问题报告（IR）或拉取请求（PR），并同样使用LLM生成其“三方面摘要”。这相当于为提交补充了外部的、通常包含漏洞详细描述的上下文。例如，当提交信息简略时，关联的问题报告能明确指出的确存在一个可导致越界读取的安全漏洞，从而为判断提供关键证据。其提示模板如图6所示。  
  
![Fig. 6. The prompt template of Development Artifact.](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYEwtBWZtDogaal2EeX5s4WKMWMakuBCaMONhib6bKLpicdtCFCuDIczRw/640?wx_fmt=png&from=appmsg "null")  
  
Fig. 6. The prompt template of Development Artifact.  
  
**3. 历史漏洞（HV）组件：**  
 该组件旨在解决挑战三（缺乏项目上下文）。它预先构建一个历史漏洞修复提交的向量数据库。对于每个历史提交，同样使用CCI组件生成“三方面摘要”并向量化存储。当处理一个新提交时，HV组件会计算其CCI摘要与数据库中所有历史摘要的相似度，并检索出最相似的若干历史漏洞修复及其详细信息（包括CVE描述）。这为当前提交提供了可类比的、项目相关的历史模式参考。  
  
**4. 综合分析及漏洞修复检测（CAVFD）组件：**  
 这是框架的决策与解释生成核心。它将前三个组件的输出（CCI摘要、DA摘要、检索到的历史漏洞信息）与原始提交数据整合，构建一个全面的提示。该提示如图7所示，采用上下文学习（ICL）和CoT策略，要求LLM执行两步任务：首先比较当前提交与检索到的历史漏洞的异同以避免偏见，然后综合分析所有信息，最终生成一个包含详细推理过程的“分析”文本，并给出“是/否”的二元决策。这确保了决策过程的可追溯性和可解释性。  
  
![Fig. 7. The prompt template of Comprehensive Analysis and Vulnerability Fix Detection.](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYicQap0sewZgwFma5lbzbtROAAgfaaoJhKiaUY1LCwaehVMeEygOxia1QQ/640?wx_fmt=png&from=appmsg "null")  
  
Fig. 7. The prompt template of Comprehensive Analysis and Vulnerability Fix Detection.  
## 4. 实验与结果 (Experiments & Results)  
  
**实验设置：**  
 研究在新构建的多语言数据集BigVulFixes上进行评估，该数据集包含2023年后的1,689个漏洞修复提交和按1:16比例采样的26,468个非漏洞修复提交，以避免与LLM预训练数据发生泄露。评估了涵盖Llama、Qwen、Deepseek三个家族的6个不同规模（7B至236B）的LLM。基线包括SOTA的预训练语言模型（PLM）方法（VulFixMiner, CoLeFunDa, VulCurator）以及各LLM的零样本CoT（Vanilla）版本。评估指标采用F1分数、马修斯相关系数（MCC）、精确率和召回率。  
  
**核心性能对比：**  
1. 1. **vs. PLM基线：**  
 LLM4VFD在所有指标上均显著优于PLM方法。如表1所示，以F1分数论，LLM4VFD相比最佳PLM基线VulCurator提升了68.1%至145.4%。尽管VulCurator精确率较高（0.77），但其召回率极低（0.13），意味着漏报严重，实用性受限。而LLM4VFD在保持可观精确率的同时，实现了更高的召回率（如Deepseek-Coder-V2下为0.78），达到了更好的平衡。  
  
![Table 1. The performance of vulnerability fix detection approaches.](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYGxNOSIia9cynBib3ZrnjibhtEIJnLHpoDLtvdTw0BibHVcSmJbqQvoUdmQ/640?wx_fmt=png&from=appmsg "null")  
  
Table 1. The performance of vulnerability fix detection approaches.  
1. 2. **vs. Vanilla LLM：**  
 LLM4VFD框架对其基座LLM的性能有普遍提升。在F1分数上，提升幅度从12.7%到105.6%不等。一个关键发现是：**较小规模的模型从框架中获益更大**  
。例如，小模型（7B/8B）应用LLM4VFD后F1分数平均提升64.0%，而大模型（70B/72B）平均提升14.4%。这表明LLM4VFD通过注入多源上下文信息，有效弥补了小模型在代码理解和复杂推理能力上的不足。  
  
**组件贡献分析（消融实验）：**  
  
如表2所示，消融实验证实了所有三个组件对最终性能均有积极贡献。其中，**代码变更意图（CCI）组件的影响最大**  
，移除它导致精确率和F1分数显著下降（如在Qwen2-7B上精确率从0.52降至0.40）。这凸显了从纠缠提交中抽象出安全相关意图的核心重要性。开发工件（DA）和历史漏洞（HV）组件则主要提供了额外的上下文支持，进一步提升了模型的判断依据充分性。  
  
![Table 2. The ablation results. The cells with the lowest performance are marked in bold, indicating the largest contribution from that component.](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMY6X2WpIZ3Iia0MuxtnY1ugQEBvaZn7tJyZ1O9yOHFTgTib6iad7CIaPZLw/640?wx_fmt=png&from=appmsg "null")  
  
Table 2. The ablation results. The cells with the lowest performance are marked in bold, indicating the largest contribution from that component.  
  
**解释性分析的有效性（用户研究）：**  
  
针对安全专家的用户研究表明，LLM4VFD生成的分析具有很高的实用价值。在80.0%的案例中，分析帮助专家更高效地识别漏洞修复；在95.0%的案例中，分析有助于理解代码变更的意图。对于包含大量变更的复杂提交，分析文本能有效提炼核心，极大减轻了人工审查的负担。  
  
**失败案例分析：**  
  
对错误分类案例的深入分析（如表3所示）揭示了框架当前的主要局限：**难以精确区分漏洞修复与一般性的安全修复**  
。例如，许多误报（FP）是将非漏洞的安全增强（如改进认证）错误归类为漏洞修复；反之，许多漏报（FN）则是将真正的漏洞修复误判为一般安全修复。这表明LLM在理解“漏洞”的严格定义（可被利用的弱点）与更宽泛的“安全”概念时存在模糊地带。此外，HV组件偶尔检索到不相关的历史漏洞，也会对LLM决策产生误导。这些发现为未来研究指明了改进方向，例如引入更精细的漏洞分类知识或改进检索相关性。  
  
![Table 3. Bad Case Analysis on Qwen2 Models](https://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkqTicoPwuVYPAo1iaibQGdMMYRqFDnRzvxhPMLicF4iaWdiajnoCYnGyBlpBmOt6TRRkIbcYODWH0BTFFQ/640?wx_fmt=png&from=appmsg "null")  
  
Table 3. Bad Case Analysis on Qwen2 Models  
  
  
   
  
  
