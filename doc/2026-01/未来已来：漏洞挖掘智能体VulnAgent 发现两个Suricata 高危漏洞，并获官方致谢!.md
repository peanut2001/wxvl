#  未来已来：漏洞挖掘智能体VulnAgent 发现两个Suricata 高危漏洞，并获官方致谢!  
原创 云鼎实验室
                    云鼎实验室  云鼎实验室   2026-01-21 10:09  
  
**01**  
  
****  
****  
  
**引言：从**  
3  
小时到  
2  
周的开发实践  
  
  
  
  
  
2026   
年  
 1   
月，腾讯安全云鼎实验室自研的  
 AI   
漏洞挖掘智能体在  
 Suricata   
中发现了两个高危漏洞，均已获得  
 CVE   
编号和官方致谢。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0l5LtWBBq57hmdRoyKOLQXpSgS8g8utvGc2Ox7rF3S5NeCPphSqomYsAkeWaaDqeOvCHuvAwkfnNg/640?wx_fmt=png&from=appmsg "")  
  
  
为什么选择  
 Suricata  
？  
作为全球部署量最大的开源网络威胁检测引擎，  
Suricata   
被广泛集成于企业级  
 NDR  
、云服务商安全基础设施以及众多商业防火墙中。我们发现的两个漏洞分别是：  
- CVE-2026-22258  
：无界分片缓冲（  
Unbounded Fragment Buffering  
），被评定为  
   
CRITICAL  
  
- CVE-2026-22259：类Zip Bomb 内存放大攻击（DNP3 Parser）  
  
两个漏洞都属于不受控的资源消耗（  
CWE-400/CWE-770  
）。攻击者只需发送极小流量的恶意数据包，就能远程导致内存耗尽使引擎崩溃。  
这种威胁在腾讯内部  
 NDR   
产品中得到了生产环境的验证  
。由于我们的及时发现，内部产品已抢在官方发布补丁前完成修复，闭环了从发现到保护的全过程。  
  
这不是一次普通的人工审计，而是一次自动化漏洞挖掘的实践：  
- 全流程自主  
：从代码分析到漏洞定位，从漏洞假设到  
 PoC   
构造，全流程由  
 AI Agent   
自主完成；  
  
- 发现仅需  
 3   
小时  
：  
Agent   
从启动任务到发现漏洞仅用了  
 3   
小时；  
  
- 开发仅需  
 2   
周  
：这个具备  
 0-Day   
挖掘能力的  
Agent   
初版，仅由一人在  
 2   
周内开发完成。  
  
我们认为，这展示了一个明确的发展方向：  
AI   
正在显著提升漏洞挖掘的效率，让大规模、持续性的自动化审计成为可能。  
  
  
  
**02**  
  
****  
  
从手动引导到自主  
Agent  
  
****  
  
  
  
**>**  
**>**  
**>**  
  
发现过程  
  
故事始于一次  
 AI   
辅助审计实践。在使用  
 AI   
协助分析  
 Suricata   
时，我们发现  
 AI   
展现出了远超预期的专业能力  
——  
它不仅完成了攻击面分析、代码审计，最终还成功构造出了可复现的  
 PoC  
。  
  
**>**  
**>**  
**>**  
  
现有方式的局限  
  
但这种  
"  
人工引导  
"  
的方式存在明显瓶颈：  
- 人力成本高  
：需要人持续对话引导，无法实现真正的自动化。  
  
- 试错效率低  
：  
AI   
的错误需要人工不断纠正，流程不闭环。  
  
- 路径冗长  
：从漏洞发现到验证复现缺乏自动化的端到端机制。  
  
**>**  
**>**  
**>**  
  
设计思路  
  
我们意识到：  
AI   
已经具备了全流程能力，欠缺的仅仅是合理的编排  
。  
   
如果能设计出合适的工作流，让  
 AI   
真正自主地完成从情报挖掘到  
 PoC   
验证的每一个环节，就能将人从重复劳动中解放出来。这就是  
 VulnAgent   
的诞生动机。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0l5LtWBBq57hmdRoyKOLQXplHSktJic3tLv7JEhymtibN3ms49GdcUTv6iaDoPAENZxAlF18tIEEbQcA/640?wx_fmt=png&from=appmsg "")  
  
   
  
**03**  
  
**技术架构：流程编排与能力底座**  
  
  
**>**  
**>**  
**>**  
  
技术选型：  
LangGraph+OpenCode SDK  
  
漏洞挖掘是多步骤、有状态、需要动态决策的复杂流程。  
- LangGraph  
（流程大脑）  
：负责复杂的有状态编排。它让  
 VulnAgent   
的每个节点维护自己的状态，根据执行结果动态路由，并实现审计失败重试、验证失败回溯等循环逻辑。我们的核心代码只需专注于  
"  
流程编排  
"  
，而将原子能力解耦。  
  
- OpenCode  
（能力底座）  
：开源  
 AI   
编程助手（对标  
Claude Code/Gemini CLI  
）。  
VulnAgent   
使用其  
 SDK   
获得了开箱即用的代码理解能力、多模型支持及工具调用（代码搜索、  
LSP  
、  
Git   
操作、文件读写）。  
  
**>**  
**>**  
**>**  
  
架构优势：可扩展性设计  
  
这种设计的精妙之处在于，  
VulnAgent   
可以随着技术发展持续进化：  
- 向上：  
它能第一时间吃到基础模型（如  
 GPT-5  
、  
Claude 4  
）迭代带来的推理能力跃迁。  
  
- 向下：  
它能无缝继承  
 OpenCode   
生态中不断涌现的新工具、  
Skills   
和标准的  
 MCP   
协议插件。  
  
**>**  
**>**  
**>**  
  
状态管理与持久化  
  
漏洞挖掘是长期任务，  
VulnAgent   
实现了完整的状态管理：  
- 全局状态  
(MainState)  
：  
记录项目信息、分析进度、已发现漏洞列表。  
  
- 断点恢复(checkpoint)：  
定期保存审计状态，支持任务中断后恢复。  
  
  
**04**  
  
**工作流程：从分析到验证**  
  
  
  
  
VulnAgent   
将安全研究员的思维模式抽象为两个闭环阶段：  
  
**>**  
**>**  
**>**  
  
审计阶段：逐步深入  
  
  
1.   
项目分析  
：  
自动化理解代码结构与核心模块。  
  
2.   
威胁情报挖掘  
：  
从  
 Git   
历史、  
CVE   
数据库、安全公告中学习漏洞模式。  
  
3.   
攻击面分析  
：  
识别高风险入口（协议解析器、内存管理边界）。  
  
4.   
静态审计  
：  
基于情报驱动生成漏洞假设，进行数据流追踪。  
  
5.   
结果汇总  
：  
整理可疑点并锁定验证优先级。  
  
**>**  
**>**  
**>**  
  
验证阶段：沙箱环境测试  
  
AI   
在隔离的  
 Docker   
环境中循环尝试：  
生成  
 PoC →   
准备目标  
 →   
执行攻击  
 →   
分析判定  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NNSr7XSrt0l5LtWBBq57hmdRoyKOLQXpRYGicEic1CNJlVBq3uciaH8UW5QbTbW1x5iag07sDrib2BpVicn8npqiaibRMA/640?wx_fmt=png&from=appmsg "")  
  
  
**05**  
  
**实战结果：流程设计的重要性**  
  
  
  
  
本次  
 Suricata   
漏洞的发现，我们并未使用最先进的模型，而是使用了  
 GLM-4.7  
。  
  
这验证了我们的观点：在基础模型能力已经达到一定水平的今天，  
流程设计比单纯的模型能力更重要  
。通过合理的编排逻辑和工程支撑，即便不是最先进的模型，也能在较短时间内发现开源项目的漏洞。这意味着  
 VulnAgent   
具有进一步优化的空间  
——  
当集成更强大的模型时，效果将会更好。  
  
  
  
**06**  
  
**当前限制与改进方向**  
  
  
  
  
必须坦诚，  
VulnAgent   
目前仍处于  
初具雏形的实验室原型阶段：  
- 自动化验证仍需人工干预  
：  
复杂项目上的环境搭建和边界条件微调仍有挑战，某些环节仍需人工引导。  
  
- 单线程串行设计  
：  
目前尚未实现大规模并行，距离真正的  
"  
工业化吞吐量  
"  
仍有空间。  
  
-    
结果判定的模糊性  
：  
区分环境异常与真实漏洞需要更深层的逻辑判断。  
  
  
  
**07**  
  
**扩展可能性：集成更多安全工具**  
  
  
  
  
目前的  
 VulnAgent   
依赖  
 AI  
的代码理解能力进行审计，并借助  
 Docker   
沙箱进行黑盒验证  
——  
这只是漏洞挖掘工具链的一部分。进一步的发展方向是：为  
 Agent   
集成  
   
IDA  
、  
CodeQL  
、  
LLDB   
等专业安全工具，并设计相应的工作流将它们有效串联。  
  
而  
   
Skills  
、  
MCP  
、  
Memory  
   
等机制只是当下的起点，未来  
 AI Agent   
的能力扩展方式还会持续发展。  
  
  
  
**08**  
  
**总结**  
  
  
  
  
CVE-2026-22258   
和  
CVE-2026-22259   
只是两个编号，但它们证明了一个清晰的信号：  
漏洞挖掘的工业化时代，不是即将到来，而是已经到来。  
  
AI   
的意义不在于替代，而在于赋能。  
   
未来，研究员的核心价值将从  
"  
亲自下场挖洞  
"  
转向  
"  
设计更精妙的工作流、编排更高效的  
 Agent"——  
让专家的直觉沉淀为可复用的流程，让经验驱动的艺术进化为工程驱动的科学。  
  
未来已来。  
  
**参考**  
  
>     - Suricata 8.0.3 and 7.0.14 Released -   
官⽅安全公告  
  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/FIBZec7ucChYUNicUaqntiamEgZ1ZJYzLRasq5S6zvgt10NKsVZhejol3iakHl3ItlFWYc8ZAkDa2lzDc5SHxmqjw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6 "")  
  
**END**  
  
更多精彩内容点击下方扫码关注哦~  
  
  
关注云鼎实验室，获取更多安全情报  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/NNSr7XSrt0mfEkibaEU8uriaORBdj9W37EhEIZlIFuzudKVafyia4vTv1q1usxN57bsdeAY4icwcKw9qJ1W4COeR4Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7 "")  
  
