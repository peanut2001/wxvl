#  我是如何利用 AI 实现 Xray POC 自动转换的  
原创 是JC啊
                        是JC啊  江城安知   2026-03-16 01:01  
  
**前言**  
  
  
  
上一篇说到AI，这篇讲一下我过去几个月利用AI做的一些尝试。  
  
## 免责声明:  
## 本篇文章仅用于技术交流学习和研究的目的，严禁使用文章中的技术用于非法目的和破坏，否则造成一切后果与发表本文章的作者无关。  
  
**注意：**  
  
**本免责声明旨在明确指出，本文仅为技术交流、学习和研究之用，不得将文章中的技术用于任何非法目的或破坏行为。发表本文章的作者对于任何非法使用技术或对他人或系统造成的损害概不负责。**  
  
**阅读和参考本文章时，您必须明确并承诺，不会利用文章中提供的技术来实施非法活动、侵犯他人的权益或对系统进行攻击。任何使用本文中的技术所导致的任何意外、损失或损害，包括但不限于数据损失、财产损失、法律责任等问题，都与发表本文章的作者无关。**  
  
**本文提供的技术信息仅供学习和参考之用，不构成任何形式的担保或保证。发表本文章的作者不对技术的准确性、有效性或适用性做任何声明或保证。**  
  
****  
****  
****  
  
**01**  
  
**设计架构**  
  
  
架构图如下  
  
![wechat_2026-03-15_201828_665.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NVsU3bKAWjMKTia7aO1w401nWZ8icQaJ2f7EsmkvCxqeYzUBxVnzzPxNXbNyyhb2giaiaUjFAVvSfrwuamRubJ3K9tWUryR5mA5VZVwEsalbHyY/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
**02**  
  
**实现思路**  
  
### 本质上是一个反思型的状态机，第一轮为什么没写对，第二轮为什么报错了，第三轮终于成功了。核心思路可以概括为：“AI负责推理，工具负责审判，逻辑负责自愈”1. 闭环自愈 (Self-Healing Loop)这是最关键的设计。AI 生成的代码不可信，所以引入 Xray Lint 作为物理层面的“审判官”。失败回传：一旦 Lint 报错，脚本不只是机械重试，而是将“错误日志 + 刚才写的烂代码”打包再次喂给 AI。对症下药：让 AI 在“错题集”中学习，实现逻辑的动态修正。2. 知识注入 (Knowledge Injection)为了解决 AI 对 Xray 特定语法（如 bsubmatch、变量提取逻辑）的幻觉问题：专家模板：在 Prompt 中内置一套“百科全书式”的 YAML 示例，作为 AI学习的基准。少量的规则硬约束：将容易出错的转义规则、空行处理逻辑直接写进指令，强行规范 AI 输出。3. 工程化韧性 (Reliability)面对大规模转换（如上千个 POC）时的稳定性设计：Key 轮询切换：自动监控 API 状态（如 429 限流），无缝切换 API Key，确保任务不中断。状态检查点 (Checkpoint)：每处理一定数量文件记录一次成功率，方便中途分析模型适配度。4. 落地化存档 (Human-in-the-loop)承认 AI 的局限性，为那 30% 的“背锅侠”减负：成功重命名：自动标记已完成文件，避免重复扫描。失败现场留存：转换失败的文件会与它的报错 Log 存放在一起。人工复核时，一眼就能看到 AI 哪里卡住了。第一版我配置了10轮的反思，但是发现效果其实并不好成功率大概只有六成左右，这一版我使用的模型是gemini-2.5-flash，看起来它没有我想象的那么聪明。  
  
  
  
**03**  
  
**90%+的成功转换率**  
  
  
第二版的时候  
笔者  
在调试的时候，发现越是给AI的约束越多，它会越发的畏手畏脚，就像是一个害怕做错事的孩子一样，到最后连怎么走路都不知道了，导致成功率陡降。  
  
后来想了两天，直接把Xray的POC模板给它，顺便注释写好规范，告诉它用这个模板写，放手去干就行了，不强制约束语法。  
  
![图片.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NVsU3bKAWjMFjABhvx2Oyt90KHS8ibG9kPDyuROQrRVKmTfROE1s0icYYYVJNRNdqqQPqg2REcDxuJGYc5FaY7j5IcYfdnv2WAOuIkVVSBGn0/640?wx_fmt=png&from=appmsg "")  
  
等到第二步，xray lint check的时候他会意识到原来我这里写错了，需要改一下。  
  
![图片.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NVsU3bKAWjPibzbZwVOP8lClVJlR6q4G85S3rgKgF2ebArCLuJFhpjia7WdibzRblcMnkZS9rGPZhszY3TUJBkWuJL6RmRFULvnSSQu60rvgFw/640?wx_fmt=png&from=appmsg "")  
  
这是转换的日志和成功率  
  
![图片.png](https://mmbiz.qpic.cn/mmbiz_png/NVsU3bKAWjPqniawicQCHNuAqgxEtZHSWNJcWBRuoHSf802QBUUDNFjrUVnA9ZeiadjtPuuowsq45KmdbWYPnXeA1oY5dloO4nQXwcPjV2hS28/640?wx_fmt=png&from=appmsg "")  
  
这里对poc分了批次，方便随时停下来调试和观察。  
  
因为原始poc实在是太多了，人力根本无法完成这么多POC的转换。  
  
![图片.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NVsU3bKAWjPUo9ELFWdYib6SI7QTNtpEd4ibYmibCuInP87pknAricABszu1bBIfQV6Yuf102DqelkBK85vMTrrYkh2RyuOUcbxm7nA3LQ4JHNo/640?wx_fmt=png&from=appmsg "")  
  
当然，这一版  
笔者  
用的是最新的gemini-3-flash-preview，所以效果会更好。  
  
这里失败的大部分是硬骨头，比如说那种需要多步骤复现的POC，这部分主要人工来手工修正完成。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/iaDKhGCPz2E1leulribRxB0Es7scgNCI0HPSvzzTl9XP8qVoeYovKibe3vYHGy0NSuc7lkJvODwNp6w603lB46wLQ/640?wx_fmt=jpeg "")  
  
  
这是最后转换完成的POC  
```
```  
  
  
**04**  
  
**关于遇到的一些问题**  
  
  
1. AI修正poc的轮数不是越多越好，一开始为了提高转化率，  
笔者  
设置的10轮复盘，但是效果很差，非常反直觉。  
  
后来意识到，AI如果在3轮里能修改好的模板那么肯定走不到第10轮，走了很多轮的必然是有很大问题的，比如陷入了死循环（一开始改的方向就错了），越改越错。  
  
后来把10轮改为5轮就收敛，反而成功率大幅度提高，速度也快起来了。  
  
1. Token消耗的问题，大概花了一周左右才跑完（转换了大概3600+Poc），大概三千多次调用，花费七百多块钱，还是有点烧钱。  
  
  
  
![图片.png](https://mmbiz.qpic.cn/sz_mmbiz_png/NVsU3bKAWjMnwF9vsFu7uSwicxiar45xOa8y6ME0OIb8m55JZE8ZIRapwHj4mBwQU1deWqm29VVA9XaibPTT2jmt9iafIia3oRfe2YAUiacG9aKhA/640?wx_fmt=png&from=appmsg "")  
  
当然，因为是最新的顶级模型，所以用的人很多，经常503。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/NVsU3bKAWjN3HDtrmmRocSowntFiaQdqZV8AUtZicPDDsvkRm91sAjCMkRXP9vNmicCQE1DoVnCIfdHuGDDb1zoEEfsjtEztE5ureuF9ficReR0/640?wx_fmt=png&from=appmsg "")  
  
  
3.关于召回率：毕竟是AI写的POC，而且和原始的POC的质量有关系。笔者在翻POC的时候发现很多低质量的POC：例如判断时间盲注就直接判断响应码是不是200和延时时间是不是8秒取并集，但是实际环境网络差的时候，扫描被WAF封锁的时候那可不止8秒，这种其实也很正常，挑出来即可。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/iaDKhGCPz2E1leulribRxB0Es7scgNCI0HzFc9dJYl7eV40NLkeeaAkJyF1wibfHsPGWMqUGvfB2CfnbRb6NeoTbQ/640?wx_fmt=jpeg "")  
  
  
  
**👇关注我了解更多安全小技巧**  
  
  
****  
  
