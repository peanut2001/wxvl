#  Claude Opus 4.6 找到主流开源库中的500多个高危漏洞  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-02-10 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**人工智能公司 Anthropic 披露称其最新大语言模型 Claude Opus 4.6从开源库如 Ghostscript、OpenSC和CGIF 中发现了500多个高危 0day 漏洞。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
Claude Opus 4.6 于上周四推出，它改善了编程技能如代码审计和调试能力，并增强了金融分析、研究和文本创建等任务能力。Anthropic 公司表示该模型在发现高危漏洞方面“明显更出色”，且无需任何针对特定任务的工具、定制框架或专门提示。该公司称目前正利用该模型查找并帮助修复开源软件中的漏洞。  
  
Anthropic 公司补充道："Opus 4.6能够以人类研究者的方式阅读和理解代码——通过查看过去的修复记录来发现未被解决的类似漏洞，识别容易引发问题的模式，或者深入理解某段逻辑，从而精确掌握触发漏洞所需的条件输入。"  
  
在该模型正式发布前，Anthropic的Frontier红队将其置于虚拟化环境中进行测试，并为模型提供了调试器和模糊测试器等必要工具，以在开源项目中寻找漏洞。该公司表示，此举旨在评估模型的开箱即用能力，测试过程中未提供任何工具使用说明，也未给予任何可能帮助模型更好识别漏洞的提示信息。  
  
公司还表示，他们对所有发现的漏洞都进行了人工验证，确保这些漏洞并非模型虚构（即幻觉现象），同时利用大语言模型作为工具，对已识别的最高危内存损坏漏洞进行优先级排序。  
  
以下是Claude Opus 4.6识别出的部分安全缺陷案例，相关维护者目前已发布修补程序：  
  
- 通过解析Git提交历史，发现Ghostscript中因缺失边界检查可能导致崩溃的漏洞。  
  
- 通过搜索strrchr()和strcat()类函数调用，识别OpenSC中的缓冲区溢出漏洞。  
  
- CGIF中的堆缓冲区溢出漏洞（已于0.5.1版本修复）。  
  
  
  
Anthropic提到："CGIF漏洞尤其值得关注，因为触发该漏洞需要理解LZW算法的核心原理及其与GIF文件格式的关联。传统的模糊测试工具（甚至覆盖引导式模糊测试器）都难以触发此类漏洞，它们需要精准选择特定的分支路径才能实现。实际上，即使CGIF实现了100%的代码行覆盖和分支覆盖，该漏洞仍可能被遗漏：因为它需要非常特定的操作序列才能触发。"  
  
Anthropic公司将Claude等AI模型定位为防御者的关键工具，以"实现攻防平衡"。但同时强调，随着潜在威胁的出现，公司将不断调整和更新防护措施，并增设额外安全护栏以防止技术被滥用。几周前，该公司曾表示，当前Claude模型能够仅使用标准开源工具，通过发现和利用已知安全漏洞，成功对拥有数十台主机的网络实施多阶段攻击。Anthropic公司指出："这充分说明AI在相对自主的网络攻防工作流中的应用门槛正在迅速降低，同时凸显了及时修补已知漏洞等安全基础工作的重要性。"  
  
****  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[用AI攻击AI：Ray AI开源框架中的老旧漏洞被用于攻击集群](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524465&idx=2&sn=41ec03ab3c0572c4ecc61e20dcd8fdb6&scene=21#wechat_redirect)  
  
  
[Zeroday Cloud 黑客大赛专注开源云和AI工具，赏金池450万美元](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524136&idx=2&sn=1ab345272edbec98f4aedbfa52607ee0&scene=21#wechat_redirect)  
  
  
[微软利用AI从开源引导加载器中找到20个0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522638&idx=1&sn=15b5a925b5a9f1eecca2dc4a721a63a9&scene=21#wechat_redirect)  
  
  
[研究员在开源AI和ML模型中发现30多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521331&idx=1&sn=e13cd9f9dccd9d17953e551df9108205&scene=21#wechat_redirect)  
  
  
[开源AI框架 Ray 的0day已用于攻陷服务器和劫持资源](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519162&idx=1&sn=3872fcc82018e2c561d9e4e7574f0c8e&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://thehackernews.com/2026/02/claude-opus-46-finds-500-high-severity.html  
  
  
题图：Pixa  
bay Licens  
e  
  
  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg "")  
  
**奇安信代码卫士 (codesafe)**  
  
国内首个专注于软件开发安全的产品线。  
  
   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif "")  
  
   
觉得不错，就点个 “  
在看  
” 或 "  
赞  
” 吧~  
  
