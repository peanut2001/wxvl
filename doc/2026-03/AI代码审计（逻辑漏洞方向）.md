#  AI代码审计（逻辑漏洞方向）  
陌陌安全
                    陌陌安全  陌陌安全   2026-03-06 07:09  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aS4DWqW8icA7yiciaDOUcQ5skNkygGjMia1NhuVNWRNauQCq5EibxAVfnLMwibrhH3IArYP0KT5kPEsNHZZIafkv5JQpqtYtqujwYPG8E5Ja2MoEE/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aS4DWqW8icA4pbDKg5PCh6ia7wRVpHWGWzzIzLZ5wNpIia1AkOibYAGWHQbiauhNlXcsZELM4Kt4HfLcSkibH3r1WKgVCg1GbUvLE7icnic697KwNy0/640?wx_fmt=png&from=appmsg "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aS4DWqW8icA6ysj6J1SGXS30O8I5yRGCdLgpKmAIWtTKE69aLyII3WU1ODQpWU8gqzEia1cdOhJNLEia39hxgcCJy0dqnWVarTb8Vo4N42Uhhg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aS4DWqW8icA6UZczFfgAPg4NQvicrcC6nAPKG7jdsXxTeGTiccibzqMFzcSzw0WSw2DvscPBdyqBjIWWyZ70qReYGANvcDiaL01ClC0ssI02d258/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aS4DWqW8icA6Ptyt5Igd0xbEQ8DSZ0sr4ibASx3AHianWav9ggLbxJNykUgdAfibQ3DIrrIkKc9TP0pde9yPBqb0X03HwWVmsyCyKFAqpKDhyRE/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aS4DWqW8icA5Y8ibqEUibiaibjms3JaSUXPZjESFZRoBySNhqAErEbm6WoT2x7MfcEjwpiaMACgdibFKHqeo8oFicfNt169M94Gv2TkfUbiazyUfayI0/640?wx_fmt=png&from=appmsg "")  
  
 momosrc   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA7d5ZqEgp9EwhgSmWp6CpRu8xu7v9PGcGPQnP3bujpVnw7mibdwBh9HrqTzBdOq0Y8WibAaKB0gCHhhmTBJW8340TYe0nYHRavxc/640?wx_fmt=gif&from=appmsg "")  
  
**AI代码审计**  
  
**（逻辑漏洞方向）**  
  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aS4DWqW8icA4CicAUedyaAoxvvj1u6JSCcbMr6Dl8ZlMpPJibzglRZnOwm6icXMicHJHqegGt6o4aPmeKHuGzTWFu7A67CBAtfj8ChCibMy5IicfU0/640?wx_fmt=png&from=appmsg "")  
  
一、概述  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA4FNViawPuOZqOYjfibUoSgWIT11K423VoYI8kbIGEGwYcpYnksXYsaiapIbKpvrNjIxBIMMHTvbkEbAOxfJzOahGpjF9Nu51syAg/640?wx_fmt=gif&from=appmsg "")  
  
  
  
        
在上一篇“[AI代码审计的探索实践](https://mp.weixin.qq.com/s?__biz=MzI2OTYzOTQzNw==&mid=2247488870&idx=1&sn=dcdc61eef17bedd213778fab6ef7dc28&scene=21#wechat_redirect)  
”的文章中，我们探讨了利用AI进行常规Web漏洞（如SQL注入SRF、命令执行）的审计方法。对于这类漏洞，在代码形态上通常具有明显的特征，白盒审计可以很容易的定位。  
  
       然而，安全从业者都知道，逻辑漏洞（Business Logic Vulnerabilities）才是代码审计中的深水区。与传统的注入类或配置类漏洞不同，业务逻辑漏洞往往隐匿于复杂的跨过程控制流与数据流交互之中，具有高度的上下文依赖性与非通用性。越权访问（IDOR）、支付篡改、竞争条件等这些漏洞往往隐藏在复杂业务逻辑中，且代码本身在语法上是完全正确的，这导致通过漏洞代码的形态定位到具体sink点，是行不通的，于是在本期分享中，我们将分享一种新的AI代码审计框架，可覆盖常规漏洞与逻辑漏洞的扫描。  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aS4DWqW8icA4e92lyZvlfjqrgibbAcmKTfaJhhRibjeia5nYxNicX7AeHLwiazxmq2o4hSwHOfCqiaTTI5wXQef9fYf7QbYhhlwciaJNDiaVOVVTOv3w/640?wx_fmt=png&from=appmsg "")  
  
二、难点与痛点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA4A57ILWXvknfOt5vW3LxAa6IAndC9MgxibV3uD6WaZy9C1WicnMcbcGLN4y06oa9OjQm3X4QNfn1iagQ297CGLsEFvElwzC9rlib0/640?wx_fmt=gif&from=appmsg "")  
  
  
  
逻辑漏洞的核心在于状态与流程。  
  
  
上下文跨度大：  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA72r3ibNCvg8rlrTkRicbuXTlgxvVcFTLibf6mxEPoPNOIu99HqkjnPzPwrvB7Xpwibs8Jz7ZfgbQnl9PMQomZsEwEe2AAZM2KTEwk/640?wx_fmt=gif&from=appmsg "")  
  
  
Controller层的入口参数，可能经过Service层、Util层的多次流转，最后才在DAO层产生影响；  
  
  
  
缺乏明显特征：  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA7oYGORIMWTR23dzjRXUz118T1wFZ9FOaXQ3sfe0CEMxqxJFicMr4yogRu4RFSsNbviaCwJkkdbmgXjf4XQfDXpZmnEwKRCpRb14/640?wx_fmt=gif&from=appmsg "")  
  
  
不像eval()或system()那样有明显的危险函数特征，逻辑漏洞往往是“合法的代码执行了非预期的业务流程”；  
  
  
  
幻觉问题：  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA7soDDL3ktEJZ7ztzibSW6sXBT4SsMmfAsLEyY7CiagqgLkvyiaWQ5oicM5Zj3I1RCGtu3rkbpvHSn3mgDiaEXe6YVt6aVyOSdHZFyo/640?wx_fmt=gif&from=appmsg "")  
  
  
直接把仓库级代码丢给AI，它很容易产生幻觉，或者因为丢失上下文而漏报；  
  
  
  
真实业务逻辑适配：  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA50sEZc97jNgOhcfhUIlG07uNklicJSZTrIN6EWBDq3O75ujSnmD1ibWoZy5nYNKr06gM36JJ5ibQuHgGtvs93J5fr2hnzrtEFv3E/640?wx_fmt=gif&from=appmsg "")  
  
  
很多情况下逻辑漏洞的判别需要与真实的业务场景、逻辑相结合，而不是直接丢给模型，让AI分析是否有逻辑漏洞  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/aS4DWqW8icA4qoazMawRXmmsO8eGR9jBmib4HRoll01nxbPjicdUH5vxicjqwnfyBaIYq2aFWj0qzhAYQicCR6ZYyje0UyzFHofMKxzmC5paicnA0/640?wx_fmt=png&from=appmsg "")  
  
三、技术路线架构  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA5tlhIzLEA7B45ObFDeAYOyEwg7IKG3GlmibNWGF4UGHNJynmqRpHFW62KhYB06DkURT9ia81azwyv80fCiaqqQ8TYezrzO5wbQY8/640?wx_fmt=gif&from=appmsg "")  
  
  
  
为了解决上述问题，我们采用以下架构：  
  
  
**01**  
  
代码结构化（Code Modeling）：  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA43h94cs5ZcE4uDG8gNw3Yarm2rYo2XdkMKpauzmOgib2GHSBEj3RlrT6XOnEa1lu3QvEC5nnHnyPpQws9tBAElXpwNfOIYhCJI/640?wx_fmt=gif&from=appmsg "")  
  
  
利用AST语法解析的能力将项目代码转化为代码属性图  
  
  
  
**02**  
  
关键子图提取（Subgraph Extraction）：  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA44mUw8zXle55gZjP5nEtmFbCG7DlR9KPuamfpnOM5VWVibJCCl3TcWnBOD0RdW8XibokEk1jmNpH7sibZzPyrooOgSlKRiciajJZBs/640?wx_fmt=gif&from=appmsg "")  
  
  
以实际路由为单位，利用图数据库查询路径，提取对链路分析有价值的上下文  
  
  
  
**03**  
  
AI推理与CoT（Reasoning）：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA7xwFKjogTv60bK1KMQ44z4ARhsLeeJIXnQAgqFmKazv9Ccp6uytbKbfZvE37DE99ZNicVhzxiayic7qOia4tft8gWm2Xn2D0yGJ1Q/640?wx_fmt=gif&from=appmsg "")  
  
  
将精简后的上下文投喂给LLM，利用贴合业务逻辑的思维链技术指导LLM进行逻辑推演。  
  
  
  
  
**整体架构图如下所示：**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA5Z8xgYOguxFfh4kibUuOc3SmropFJmnyItp8Szicp9tqf4mReGnn20DnpdFibNbibeEn1KhTq78M5nzKr8mdNfWfjpWH16DMhicvCE/640?wx_fmt=gif&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aS4DWqW8icA5kicEm5fqhUDF1ffnTFicdoo6QEXSjXsPKvwVtP5sL6CQ9VvLKvjfIOUZv9gG27CddfcBBenK7v553cgX1H3bfH4umIgERb3XTU/640?wx_fmt=png&from=appmsg "")  
  
  
  
Schema设计  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA7QeL3LHQYLP7kSdxWbLIgU5f0dPooMIJEibopKkEmgFfYn0jgeibgQhOHCyYGfEPictaRELWWZBhqHPeSasusBdCyTKicgwvn46Xk/640?wx_fmt=gif&from=appmsg "")  
  
  
在图数据库 NebulaGraph 中，我们需要定义清晰的 Schema 来描述代码仓库的函数调用关系，其中包括图的节点以及边的定义，如表3.1所示：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aS4DWqW8icA4D5PDvric0zmuiafiaZSTxcrE1IyHT0l9v3SMyBM6h6BE7dTkSA5QmTLtG4SRRoAJ87Mh1kNUqibdyutoUibFOIPCHeV0MVfn6Th9M/640?wx_fmt=png&from=appmsg "")  
  
  
构建流程  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA6HedWicfdts3B2cr3zIWLXIia11KOkiaFY1dMYrqh8LiccamlWLGqSPMwgvWyP4jgEGTM9WibnpGU4oFtYNms6CicqicNRgWe3pV9vibc/640?wx_fmt=gif&from=appmsg "")  
  
  
我们采用静态分析（Static Analysis）的通用思路来构建图谱：  
  
**·解析与提取：**  
利用语言对应的AST解析工具，遍历项目源码，提取出所有的函数定义（作为点）和函数之间的调用关系（作为边）；  
  
**·数据导入：**  
将提取的数据通过NGQL语法，连接至Nebula Graph并进行批量导入。  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA5NnyTunGG1icWCJkBFsUapVpY9dibzEsDL2hzpIJqF7uR6fFcx8dnVxfiaoxejFphDFS7btiaBOWVpzDWib4F4ibDYlFELe9picdKgDA/640?wx_fmt=gif&from=appmsg "")  
  
3.2 有效上下文提取  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA6lCp4E6lFfapZIP5jytvN1NOsCxRauhxOrkrFUefbicPBrO2rNsraeXoD9VHBGLvdibq7skE9WAwQMR0r7wvfDOho9VXFYHz2UY/640?wx_fmt=gif&from=appmsg "")  
  
  
与常规漏洞不同，逻辑漏洞没有定式的Source-Sink形态，所以逻辑漏洞的有效上下文应该为API的完整逻辑链路。与此同时，真实业务仓库中通常会利用注解符来对API注入拦截器、过滤器以及Controller增强类，在实际的AST解析时无法识别到这一引用关系，我们通过在项目扫描时，对这一部分单独提取扫描。  
  
  
  
上下文的提取分为三步  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA4BkQhlUcLYw4afE6Wfu0qgGSHOyic5q42yZHsTAqyL7v5zDYtTtpsJNd1SibyM9l5OXiaddZEWjDEpEEZO6ibT0htUF87uYI3K3a8/640?wx_fmt=gif&from=appmsg "")  
  
  
**·**  
识别仓库级的拦截器、过滤器以及Controller增强类的具体实现；  
  
**·**  
识别到整个仓库所有的API；  
  
**·**  
根据API获取包含所有调用关系的链路，以及链路上的代码实现（子图提取）。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA4GVL0icf96Fuhn3SFAYNCFIILnRyson9nBVFiacwPcFx2XHqTWtNp0jibYF4icrf3xDWMzShPwJeHuOf4ZZqmvhrlJHxNDRyxia3Hg/640?wx_fmt=gif&from=appmsg "")  
  
3.3 贴合业务场景的AI推理  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA5AnrF1R02QhCXLYKpKBhWViadMC2d3KNxpO8TQe3usLP0icH7u6Vau8QgSWDoEtbwGvv3vZ1KKia1Pw8MOnrTrI87BkZJO1kfojQ/640?wx_fmt=gif&from=appmsg "")  
  
  
在原本“图数据库 -> AI”的流程中，直接把所有提取出来的链路都丢给 AI（LLM）去审，虽然比审全量仓库代码，但依然存在两个问题：  
  
  
**·成本问题：**  
很多API链路在功能、 场景上不可能存在部分漏洞，没必要浪费 AI 的算力。如查看公开文章等功能路由，我们不需要关心其越权、并发问题。  
  
**·效率问题：**  
LLM的输出时间和输出Token量是正相关的，对于初筛步骤而言，我们只需要输出少量的内容用于标记其是否可能有漏洞，在全量仓库扫描时可以大幅度提升扫描速度  
  
  
因此，在 第二步（图查询） 和 第三步（AI 深度审计） 之间，插入一个 “基于业务场景规则的 AI 初筛（Pre-screening）” 环节，是工程化落地的关键。  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA4GPrG76w73Qfp6vxO8PzrMXfr4TDN0AKcKxmdgEGqgRyHQzbvN9FvVIyCywnWojrXcEBZHia1z4L185AkftBHC7tmZrSj0U4SA/640?wx_fmt=gif&from=appmsg "")  
  
3.4 RAG 增强的动态 Prompt 注入与 CoT 终极推理  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA4EWJR0oOSkr2H9KRKRdqhxGmIWhF2XiccdD9NAsIUaN2OIxGOq2Usnu3lncB6KZAFQmY2SV2oYkhd8olrwKBT1eAnXBKbmdHnM/640?wx_fmt=gif&from=appmsg "")  
  
  
这一步是整个系统的“大脑”。我们利用 RAG 技术，将通用大模型瞬间转化为懂业务、懂规范的定制化安全专家，并利用 CoT 进行深度逻辑推演。  
  
我们将这一步细分为三个阶段：动态 Prompt 注入 -> 思维链（CoT）四步推演 -> 结构化判决输出。  
  
  
动态 Prompt 注入（Context Injection）  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA60WkBnH7ticeibK7IvApib3kHia11iaicIMjIESpv6XSV3c3apcDsjc0WeNLgYEMe0GMNibV8KlnAdaXaJ4OLQP2el7LA9ibH2cEHCfPI/640?wx_fmt=gif&from=appmsg "")  
  
  
在进行推理之前，我们需要先构建一个向量数据库（Vector DB）作为 AI 的“外挂大脑”。当链路在上一步的初筛中给出漏洞标签（如条件竞争、越权）。在这一步，我们根据标签的内容，在向量数据库中进行检索，动态加载不同的**专家级 Prompt 模板**  
。  
  
  
  
CoT 四步推理  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA7mSoVFHKRmddiaALibMic9PhkLVXaMSk9KFicUgsRbsYo1Efx6xSUXxBHcOUqvLtQHhs1YEhq9ryo4tBrDrlATHJLJOd6kySLJy6c/640?wx_fmt=gif&from=appmsg "")  
  
  
在没有 CoT （Chain of Thought）的情况下，由于LLM 基于概率预测下一个字，容易产生幻觉，或者因为代码表面看起来没报错就认为没漏洞。  
  
引入 CoT 后，我们要求它在给出结论之前，必须先生成一段推理路径（Reasoning Path），基于LLM的注意力机制，最后输出的时候会受到推理阶段输出内容的影响，输出正确的逻辑链从而可以降低幻觉。  
  
我们将CoT的推理过程主要拆分成以下四步：  
  
**·识别场景与入口：**  
识别API的功能场景，分析用户可控的入口参数；  
  
**·防御机制审计：**  
寻找代码中的“锁”和“盾”，并结合框架层的防御内容分析防御机制的完备性与有效性；  
  
**·对抗性沙箱模拟：**  
使AI尝试设计PoC，经过真实链路代码中的逻辑处理后，观察是否可以真实触发漏洞；  
  
**·漏洞结果判定与证据链呈现：**  
基于推演结果，给出负责任的结论。  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aS4DWqW8icA7ZnXyW0bDN5MosYFFavHfjBERTe9DFdSgER5UQ3IMklHwee4RJ1vF12O39OoZJ8C48p8rNfSydwhiaDRSQOZYgE7FAsQibqicVIk/640?wx_fmt=png&from=appmsg "")  
  
四、结语  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/aS4DWqW8icA4W4vDwVmicprPibuQpKz7bWIQPF0FHxL0ibeZTDuZTZNsVSRXlxUYm9iaNiclTg8XKEeohRB5kSTwiavwKHpWMJrfqgguwABaD8vYRE/640?wx_fmt=gif&from=appmsg "")  
  
  
  
     从传统的正则匹配到 AST 静态分析，再到如今的 “图数据库 + RAG + CoT” 组合拳，代码审计技术正在经历一场从“特征识别”到“认知推理”的范式转移。  
  
在本文中，我们详细拆解了一套面向逻辑漏洞的工业级 AI 审计架构：  
  
**·数据层（Context）：**  
利用 NebulaGraph 的高性能图计算能力，解决了代码上下文的“碎片化”问题，将跨文件、跨层级的调用链路完整地呈现在 AI 面前。  
  
**·知识层（Knowledge）：**  
通过 RAG 技术，将企业沉淀的安全规范与历史漏洞转化为 AI 的“外挂大脑”，实现了审计能力的动态成长与业务对齐。  
  
**·推理层（Reasoning）：**  
借助 CoT 思维链，打破了 LLM 的黑盒幻觉，强制 AI 像安全专家一样进行“攻防推演”，从而精准捕捉那些语法正确但逻辑崩坏的深层漏洞。  
  
这套架构不仅解决了逻辑漏洞“难以自动化挖掘”的行业痛点，更通过“规则初筛 + 动态 Prompt”的漏斗模型，在工程上实现了成本与效果的平衡。  
  
  
  
About MMSRC  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/aS4DWqW8icA4lTnERPEo0EYJL4NJ1ud7Y3CbnQ1P3wx46hMyYwxxs7Dh5tXQ8ibWeCxqe9QKsEVfZNx8F3Le1d2Zuq7nxicpakFdqEKMw6Pib88/640?wx_fmt=gif&from=appmsg "")  
  
陌陌安全应急响应中心  
  
（MMSRC，MOMO Security Response Center）  
  
是陌陌安全建立的安全漏洞收集及安全应急响应平台，致力于保障陌陌旗下所有产品及用户信息安全，促进陌陌与白帽子及团队的交流合作。为感谢白帽子及团队为亿万陌陌用户信息安全做出的贡献，陌陌安全应急响应中心特别设立年度百万奖金池，单漏洞或情报奖励可达万元，活动期间可获取更高奖励。于此同时，我们会不定期组织、赞助安全会议等线下活动，为广大白帽子创造线下交流沟通机会。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aS4DWqW8icA5z8ULkdfs2GX9oxicIx7IdVbIicsu22ZyHH7t9ib7bADvj1ltvibj2tquxlzAFRFyMKrPzQOJPY7L4NJxDeBRxf2gpk0foTekdbbk/640?wx_fmt=png&from=appmsg "")  
  
「陌陌安全」  
  
扫上方二维码关注我们，惊喜不断哦  
  
  
M   O   M   O   S   E   C   U   R   I   T   Y  
  
  
  
