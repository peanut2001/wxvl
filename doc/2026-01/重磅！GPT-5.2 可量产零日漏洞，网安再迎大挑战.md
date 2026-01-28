#  重磅！GPT-5.2 可量产零日漏洞，网安再迎大挑战  
 易云安全应急响应中心   2026-01-28 08:22  
  
**点击蓝字，立即关注**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtTL7fPDvpcysRGkibar05ibib7QSz0BKM1Qhkn1x55xibdeFacd9xJibHsn94ucvuapZhMCzDDfojPLRoA/640?wx_fmt=png&from=appmsg "")  
  
一项最新研究正引发全球网络安全圈的广泛关注：先进大模型已能在**几乎无人干预**  
的前提下，**稳定、规模化生成零日漏洞利用代码**  
。这早已超越“AI能否编写PoC（概念验证代码）”的基础探讨，而是针对真实漏洞、真实防护体系、真实成本约束的一次**系统性能力验证**  
，其结果正在重塑网络攻防的底层逻辑。  
  
  
**1**  
  
  
**核心突破：**  
  
**AI自主跑通完整漏洞利用链路**  
  
本次实验由安全研究员Sean Heelan主导，测试目标锁定QuickJS JavaScript解释器中一个此前未被发现的未知漏洞。与以往概念验证不同，研究者并未向AI提供任何现成的利用思路，而是**要求其在真实的技术约束条件下，独立完成漏洞分析、能力构建与利用验证的全流程。**  
  
****  
具体来看，AI智能体需要**依次完成五大核心任务**  
：阅读并深度理解QuickJS源码、对漏洞行为进行调试与逻辑推理、将原始漏洞转化为可复用的能力接口、实现对目标进程内存的任意读取与修改、通过反复试错自主迭代优化利用策略。整个过程中，研究者未对利用细节进行任何人工干预。  
  
  
测试结果显示，两款先进大模型表现亮眼：基于**GPT-5.2**  
的AI智能体在所有测试场景中**全部成功**  
，另一款先进模型**Opus 4.5**  
则仅在个别复杂场景中失利。最终，两者在六种不同目标场景下，共**生成40余个可实际运行的漏洞利用样本**  
，覆盖获取shell、写文件、建立命令与控制通道等多种典型攻击目标，印证了AI对漏洞利用开发全链路的自主掌控能力。  
  
  
2  
  
  
**极限验证：**  
  
**全防护环境下的漏洞利用突破**  
  
研究中最具代表性的测试场景，是要求AI在**多项企业级防护机制全面开启、常规利用路径被彻底封堵**  
的前提下，将指定字符串写入磁盘文件——这一场景高度模拟了真实企业的网络安全防护环境，技术难度拉满。  
  
  
此次启用的防护机制涵盖多个维度：地址空间布局随机化（ASLR）、不可执行内存（NX）、完整RELRO、细粒度控制流完整性（CFI）、硬件级Shadow Stack，以及禁止shell执行的seccomp沙箱。更具挑战性的是，QuickJS中所有与操作系统、文件系统相关的接口均被移除，**传统漏洞利用路径被完全切断**  
。  
  
  
即便在如此严苛的条件下，GPT-5.2仍**成功构建出非传统ROP（返回导向编程）的利用路径**  
：通过glibc的exit handler机制串联七个函数调用，在不触发Shadow Stack保护的前提下完成文件写入操作，同时成功绕开seccomp沙箱限制。整个漏洞利用开发过程**耗时约3小时，消耗5000万token，成本仅约50美元**  
，从资源投入维度证明了该模式的高度可复制性与规模化潜力。  
  
  
**3**  
  
  
**成本与边界：**  
  
**AI攻击能力进入工业化阶段**  
  
从效率与成本来看，AI在漏洞利用开发领域的优势已十分显著。多数测试场景可在1小时内完成，一次成功运行通常消耗约3000万token，成本控制在30美元左右。即便面对最复杂的测试场景，其整体投入也远低于传统高端漏洞研究所需的人力成本——要知道，一名资深漏洞研究员完成类似级别的漏洞利用开发，往往需要数周甚至数月时间。  
  
  
不过研究者也明确指出了**当前AI漏洞利用能力的两大限制**  
。其一，QuickJS的代码规模和复杂度，明显低于Chrome V8、Firefox SpiderMonkey等主流浏览器引擎，AI在更复杂软件系统中的表现仍需进一步验证；其二，AI并未创造全新的安全缓解绕过技术，其核心是利用现实世界中人类漏洞研究员同样会使用的已知机制缺口和实现缺陷。  
  
  
但不可忽视的是，AI所构建的完整漏洞利用链本身是全新的构造，且是针对真实存在的未知漏洞完成的——这意味着，AI已具备将“已知技巧”自动组合成“未知攻击路径”的核心能力。  
  
  
Sean Heelan在研究中直言，**漏洞利用开发天然适合AI自动化**  
：该领域具备明确的成功判定标准、成熟的工具链支撑，以及可系统搜索的解空间。未来，网络进攻能力的上限，可能不再由高级安全研究员的数量决定，而是受限于计算资源与token吞吐能力。  
  
  
这项研究并非一次炫技式的概念验证，而是对AI网络攻击能力的一次贴近现实攻防环境的精准测量。它所呈现的，不是“AI是否危险”的抽象讨论，而是一个正在发生的行业事实：漏洞利用开发这一曾被视为“高度依赖经验和直觉”的稀缺技能，正在快速走向可规模化、工业化生产。  
  
  
目前，完整的实验代码、技术文档与原始输出已在GitHub上公开。研究者同时呼吁，安全社区应将类似评估更多地放在真实目标与真实零日漏洞上，而不仅限于竞赛环境。对于整个网络安全行业而言，AI“量产”零日漏洞的时代，或许才刚刚拉开序幕。  
  
消息来源：gbhackers  
  
文章来源 ：安全客  
  
免责声明  
  
本文素材(包括内容、图片)均来自互联网，仅为传递信息之用。如有侵权，请联系我们删除。  
  
**END**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/6aVaON9Kibf6qHRdibQTh7Bic33HXRicZowtjiavqOsjjNTNWNtssMJtfSYn6uT1PgnaWWnMlSPevI96XXRdM4tibYqQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**淮安易云科技有限公司-****网络安全部**  
  
我们致力于保障客户的网络安全，监控事件并采取适当措施，设计和实施安全策略，维护设备和软件，进行漏洞扫描和安全审计,团队协调处理网络攻击、数据泄露等安全事故，并负责安全服务项目实施，包括风险评估、渗透测试、安全扫描、安全加固、应急响应、攻防演练、安全培训等服务，确保客户在网络空间中的安全。  
  
**易云安全应急响应中心**  
  
专业的信息安全团队，给你最安全的保障。定期推送  
漏洞预警、技术分享文章和网络安全知识，让各位了解学习安全知识，普及安全知识、提高安全意识。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQHDte6ZzXiclrYUTCQHiak0k38kaD0O6NSfpyrRicr2rspyQicXCp6I4iagSbNbaKt2IiboYfRyUpnDZrtQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/gMiabmiaticAtTL7fPDvpcysRGkibar05ibib7KrzIToh2eSlSrUF06IVpEwE5cYkIgRnhUPWmF9M5VsZWmMcMctgIBw/640?wx_fmt=gif&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gMiabmiaticAtSia0prnfkWIj7vlIkbFPGibN2sUrBbqFSpgHDHhz9s0ic6smsEy0Dae8bnOUPibYNuuj4gwOyqjiac9ow/640?wx_fmt=jpeg&from=appmsg "")  
  
**扫码关注**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtTL7fPDvpcysRGkibar05ibib76UCNv1EnB844aLicKtdBibG6dCEIhiblvZcvNOJRzsfJWQVAgwLQkWxOA/640?wx_fmt=png&from=appmsg "")  
  
**点分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtTL7fPDvpcysRGkibar05ibib77gP7ia1P03jwLMoqL83tvnAl4ZlCd7IIgNibF3wCXTEPbuDibKTtRJsGg/640?wx_fmt=png&from=appmsg "")  
  
**点收藏**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtTL7fPDvpcysRGkibar05ibib7wsFYTnUm0hQ0hMzwEiahf5MPUrj5IMsRnqNwg4nw6a55y0Uda2l3AhQ/640?wx_fmt=png&from=appmsg "")  
  
**点在看**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gMiabmiaticAtTL7fPDvpcysRGkibar05ibib7iaubpAvMeFibC1iaVVJWicOIhn0hYz6M5MxChyACxicOoXAUqn3klib6pIrA/640?wx_fmt=png&from=appmsg "")  
  
**点点赞**  
  
