#  ClaudeOpus4.6发现Firefox22个安全漏洞，AI自主漏洞研究实现关键突破  
 安全客   2026-03-11 02:57  
  
**两周时间，22个安全漏洞，其中14个被评定为“高危”**  
。这不是某个顶级安全团队数月攻坚的成果，而是人工智能公司Anthropic的模型Claude Opus 4.6，**在2026年2月与Mozilla合作期间**  
，扫描Firefox代码库所交出的答卷。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g5KiabmYVDH0JTkzIdCNWvwYCVTwwTib4wBYz4qdylJiamNnxGr1Ca4oL5UJkcr0TNHGwTichxGOCnzjkdBs8w59eKQib6c2WVzUiaLicSjkBia8P84/640?wx_fmt=png "")  
  
  
这个数字意味着什么？按照Anthropic自己的说法，**仅这14个高危漏洞，就相当于Firefox在2025年全年修复的全部高危漏洞总数的近五分之一**  
。换一个更直观的参照：**Claude两周发现的高危漏洞，比2025年任何单月人工报告的数量都要多**  
。  
  
  
这标志着，AI在高级漏洞研究领域，正实现从辅助工具到自主威胁狩猎能力的跨越式升级。安全攻防的游戏规则，或许正在被彻底改写。  
  
  
**1**  
  
  
**效率革命：20分钟锁定高危漏洞**  
  
这次合作的起点颇为低调，最初只是Anthropic内部的一次评估练习。团队注意到**上一代模型Claude Opus4.5在CyberGym基准测试中表现接近满分**  
，为了验证更真实的场景，他们让Opus4.6直接面对现役的Firefox代码库，目标是找出从未被报告过的全新漏洞，彻底排除“训练数据里藏着答案”的可能性。  
  
  
**结果来得很快，快得令人有些不安。**  
  
  
**仅仅不到二十分钟**  
，Claude就在Firefox的JavaScript引擎中锁定了一个“释放后使用”（Use-After-Free）漏洞。这类内存缺陷允许攻击者用恶意内容覆盖系统数据，属于高危级别中的常见且严重的一种。三名Anthropic研究人员随后在独立虚拟机中分别验证了这一发现，并附上Claude自动生成的候选补丁，提交至Mozilla的漏洞追踪系统Bugzilla。  
  
  
而当第一份报告提交时，Claude**已经发现了另外五十个独立的崩溃输入**  
。  
  
  
整个项目期间，Anthropic共扫描了**近6000个C++文件**  
，提交了**112份不同的报告**  
。Mozilla随后在Firefox 148.0版本中修复了其中大多数问题，更新已推送至全球数亿用户。  
  
  
2  
  
  
**能力不对称：挖掘高效，利用薄弱**  
  
发现漏洞是一回事，把漏洞武器化、变成可落地的攻击程序，是完全不同的另一回事。  
  
  
Anthropic**没有回避这个更敏感、也更关乎攻防平衡的测试**  
。他们给Claude下达了明确任务：基于已发现的漏洞，生成可实现目标机器本地文件读写的基础漏洞利用程序（exp）。为了这项测试，团队**累计消耗了约4000美元的API算力**  
，进行了数百次自动化尝试。  
  
  
最终的结果，呈现出**极强的不对称性：Claude仅在2个案例中，成功生成了有效的漏洞利用程序**  
。而且这两个程序都极其粗糙，只能在特意关闭了沙箱防护等多项浏览器核心安全机制的受控测试环境中运行。在用户日常使用的正式版 Firefox 中，浏览器的纵深防御架构，完全可以有效阻断这类AI生成的攻击。  
  
  
Anthropic将这个结果定义为**「漏洞发现与利用的能力不对称性」**  
，并将其视为当前阶段对防御方最有利的核心窗口期。他们的核心逻辑很明确：AI 找漏洞的能力，已经显著超过了把漏洞武器化的能力。这意味着，如果防守方能率先用好这些工具，就能在攻击方掌握同等利用技能之前，提前把系统里的安全隐患清理干净。  
  
  
3  
  
  
**双刃出鞘：攻防的天平易位**  
  
这次合作选择Firefox作为测试对象，本身就说明了一定问题。**Firefox是现存规模最大、测试最密集的开源项目之一**  
，拥有数百万行代码，背后有来自全球的安全研究员持续盯防。在这样的项目里翻出新漏洞，难度远远高于那些缺乏维护的软件。  
  
  
Anthropic此前曾记录过Claude在多个开源项目中发现**超过500个零日漏洞**  
，但Mozilla这次合作在难度和现实意义上明显更上一层。  
  
  
这个论断在安全界引发了不少讨论。有分析指出，**发现漏洞本身并不等同于降低了网络风险，关键在于修复的速度能否跟上AI扫描的速度**  
。另有报道显示，AI已经把安全漏洞从披露到被攻击者利用的**传统32天窗口压缩到了约5天**  
，这意味着防御者手里的时间比以前少得多。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g5KiabmYVDH239KS6GyfyM9cNW0xIdpOXg1KicDdicVPDN1xadKAzicru9MOja3zamGH0HlSfmgb0YLphs3rZ33FQUkIMASIL8WjIzXO87MH95o/640?wx_fmt=png "")  
  
  
Anthropic自己也没有讳言隐忧。公司明确表示，如果未来模型**缩小了“发现”和“利用”之间的能力差距，就需要引入额外的安全措施防止滥用**  
。Claude Code Security目前已开放限量预览，目标是把快速发现和修复漏洞的能力直接交到防御者手中，抢在恶意行为者掌握同类技能之前构建防线。  
  
  
AI扫描代码的能力正在以人类难以匹敌的速度提升。这对防守方是利器，对攻击方也是潜在的诱惑。**两周22个漏洞，只是这场博弈的一个早期读数**  
。  
  
  
这次合作最令人震撼的，或许不是AI找到了多少漏洞，而是它找到漏洞的方式和速度。当传统安全研究还依赖经验、直觉和大量手工测试时，**AI已经能够系统性地扫描数千个文件，在二十分钟内锁定人类可能需要数月才能发现的内存安全问题**  
。  
  
  
但硬币总有另一面。AI在漏洞利用上的笨拙，暂时给了防御方一个宝贵的时间窗口。这个窗口期有多长？没人知道。安全领域的“猫鼠游戏”正在进入一个全新的维度——不再是人与人之间的智力对抗，而是人与机器、机器与机器之间的速度竞赛。  
  
  
Mozilla安全团队的回应或许代表了大多数防御者的心态：他们将AI辅助分析视为**“安全工程师工具箱中一项强大的新增能力”**  
。工具本身没有善恶，关键在于谁先掌握它，以及如何使用它。  
  
  
对于每一个依赖软件安全的普通人来说，这次事件传递的信息很明确：**更新你的浏览器，保持软件最新，因为AI正在让漏洞的发现和修复都变得比以往任何时候都要快**  
。  
  
  
消息来源：Cybersecuritynews   
  
  
推荐阅读  
  
  
  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-shadow: rgb(0, 0, 0) 0px 0px 0px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">01</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 14px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span style="font-size: 12px;box-sizing: border-box;"><span leaf=""><a class="normal_text_link" target="_blank" style="" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789723&amp;idx=1&amp;sn=864d06bec8122f6ed8a2dd34d43c29f7&amp;scene=21#wechat_redirect" textvalue="OpenAI发布应用安全智能体" data-itemshowtype="0" linktype="text" data-linktype="2">OpenAI发布应用安全智能体</a></span></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">02</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 12px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span leaf=""><a class="normal_text_link" target="_blank" style="" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789645&amp;idx=1&amp;sn=2f03e4c73edb0311c9d0c51237788490&amp;scene=21#wechat_redirect" textvalue="AI协作24小时共创全新编程语言已开源" data-itemshowtype="0" linktype="text" data-linktype="2">AI协作24小时共创全新编程语言已开源</a></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">03</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 12px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span leaf=""><a class="normal_text_link" target="_blank" style="" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789621&amp;idx=1&amp;sn=d5f11dfa319b3471e1c14e45e8a11b9b&amp;scene=21#wechat_redirect" textvalue="新兴AI攻击威胁与五步杀伤链分析" data-itemshowtype="0" linktype="text" data-linktype="2">新兴AI攻击威胁与五步杀伤链分析</a></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr></tbody></table>  
  
  
**安全KER**  
  
  
安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g5KiabmYVDH0lGF732N7tzWyCNaKV5I4YZEfeLFa6spoTkacO9eWE0Ft5qkcMCkyibF7ic33ZvRkCvNof6Iic9oszSicLEh5cXvVKetHvKpdTXpk/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g5KiabmYVDH1qXMHEicN23IBicv6Nv9hwXK4HZo3W2Azh8rn62dlRBm8P2glmhjcqMfZmk0ta6qyFXHxCxbCs0LcyULch4gPlxsKk3R0mlFFwM/640?wx_fmt=png "")  
  
**注册安全KER社区**  
  
**链接最新“圈子”动态**  
  
