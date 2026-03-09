#  OpenAI发布应用安全智能体：可自主发现、验证并修复漏洞  
 安全客   2026-03-09 08:01  
  
近日，OpenAI正式发布其**专为应用安全**  
打造的智能体——Codex Security。这款内部代号为「Aardvark（土豚）」的工具，标志着应用安全领域正**从传统的静态扫描，迈向基于「智能体推理」**  
的新范式。它不仅能自主识别企业级与开源代码库中的复杂安全漏洞，更能主动验证漏洞的真实性，并生成可直接落地的修复方案，**旨在彻底解决安全团队长期面临的告警噪音与误报难题。**  
  
  
**1**  
  
  
**核心能力：从“标记”到“验证与修复”的跃迁**  
  
和传统应用安全测试工具完全不同，Codex Security走的是「全流程智能闭环」路线，不是简单的代码规则匹配，而是**真正懂代码、懂业务、懂风险**  
。  
  
  
先建威胁模型，再做风险评估，真正懂业务上下文  
  
  
它不会上来就扫代码堆告警，而是先给目标项目**量身打造一套可编辑的专属威胁模型**  
，把系统的信任边界、风险暴露面摸得一清二楚。  
  
  
基于对业务场景的完整理解，它会按照漏洞的真实业务影响划分优先级，而不是用通用启发式规则瞎打分，**从根源上减少无效告警**  
。  
  
  
沙箱实锤验证PoC，彻底告别误报地狱  
  
  
最绝的核心能力，是它会**自己在沙箱环境里执行概念验证（PoC）漏洞利用代码**  
，主动验证漏洞是不是真的能打！  
  
  
只有实锤确认的有效漏洞，才会推送给用户，彻底把误报掐死在源头。OpenAI内测数据直接拉满：  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g5KiabmYVDH12GODY8MHHI7eRxeY9XyGru9I1oLLL27fWP9gGzU6asUYD5M0Uv9DddLvvGY7gmYVSNnx0KXp2ekCt6Fy4huWhwmsnkunzhh0/640?wx_fmt=png "")  
  
  
一键生成贴合业务的修复补丁，解决代码审核瓶颈  
  
  
光找漏洞还不够，它还会直接生成贴合系统架构、最小化代码回退风险的修复方案，从发现、验证到修复，全流程自主完成，**完美解决AI开发时代的代码审核瓶颈**  
。  
  
  
内测期**最后30天**  
，它直接扫描了外部仓库**超120万次代码提交**  
，精准揪出了**792个关键漏洞**  
、**106561****个高危问题**  
，而关键漏洞在所有扫描提交中的占比**不到0.1%**  
——真正做到了只给你看最该关注的风险。  
  
  
2  
  
  
**赋能开源：守护数字世界的基石**  
  
Codex Security落地的核心场景之一，是**对关键开源软件（OSS）的安全审计**  
。OpenAI已利用该智能体对OpenSSH、GnuTLS、PHP、Chromium等广泛依赖的开源项目进行了深度扫描，其原则是**“优先输出可落地的安全情报，而非无实际价值的推测性报告”**  
。  
  
  
这些审计已发现多个高影响零日漏洞，并推动官方分配了14个正式CVE漏洞编号。OpenAI特别强调：**“我们不会输出大量推测性的告警结果，而是要打造一套优先聚焦高置信度漏洞的系统，让项目维护者能够快速采取处置动作”**  
。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g5KiabmYVDH0CenEYKnn6zS75xkh67ic4iaDXmvxh7fzuljPcLgUADXqlIQAhRxwpvwZ1Hmcjf84y4cozf3LgFibV2WPxPbMla0O8QfiamTRm9qs/640?wx_fmt=png "")  
  
  
为进一步补强开源生态安全短板，OpenAI同步启动**「Codex开源专项计划」**  
，针对性帮扶资源紧缺的开源项目维护者，**符合资质的维护者可免费享受三大专属权益**  
：免费的ChatGPT Pro/Plus账号、专属代码审核支持服务、在自有项目中全量使用Codex Security能力。目前vLLM等早期参与项目，已将该智能体融入日常开发流程，实现漏洞前置防控，在恶意利用发生前就完成排查与修复。  
  
  
3  
  
  
**落地实操：快速解锁智能防护**  
  
眼下，Codex Security已通过Codex网页端，向ChatGPT专业版(Pro)、企业版(Enterprise)、商业版(Business)及教育版(Edu)用户**开放研究预览权限**  
，各类群体可对照以下实操步骤，快速接入这款安全利器，正式入局智能安全时代：  
  
  
·  
企业用户：前往ChatGPT企业版控制台，申请Codex Security权限，快速搭建适配自身业务的企业级智能安全防护体系；  
  
  
·  
开源维护者：访问OpenAI官网，提交“Codex开源专项计划”申请，免费解锁专属安全能力，赋能开源项目开发；  
  
  
·  
全团队：查阅OpenAI官方开发者文档，完成代码仓库集成配置，实现安全工具与研发流程的无缝衔接。  
  
  
从ChatGPT掀起AI辅助开发的浪潮，到如今Codex Security直接杀入安全攻防的核心环节，**OpenAI这一步的颠覆性，远比我们想象的更深远**  
。  
  
  
过去，AI安全工具大多停留在「辅助扫描」的初级阶段，而Codex Security**直接实现了 「上下文理解→威胁建模→漏洞发现→PoC验证→补丁生成」的全流程自主闭环**  
 。它把安全团队从重复、低效的告警筛选、误报排查工作中彻底解放出来，让安全人能把核心精力放在真正关键的风险防控与体系建设上。  
  
  
当然，**它不会替代安全专家**  
，但一定会成为安全从业者手中最强大的武器。它让顶尖的安全能力，能够覆盖到更多中小企业、更多开源项目，最终筑牢整个数字世界的安全底座。  
  
  
最后给所有从业者提个醒：  
  
  
・安全与研发团队可尽快查阅OpenAI官方开发者文档，完成代码仓库集成配置，搭建适配自身业务的基准威胁模型；  
  
  
・开源项目维护者可通过OpenAI官方平台，提交「Codex开源专项计划」申请，免费获取相关能力；  
  
  
・使用了文中提及的受漏洞影响组件的机构，应立即跟踪对应厂商的安全公告，及时部署官方验证通过的修复补丁。  
  
  
Codex Security的发布，**不仅是OpenAI在AI安全领域的一次重磅落子，更是对整个应用安全行业范式的一次强力冲击**  
。当AI不仅能发现问题，还能验证问题、给出可落地的解决方案时，安全工程师的角色，也将**从 “漏洞筛选工” 向 “风险决策者” 加速演进**  
。  
  
  
消息来源：Cybersecuritynews  
  
  
推荐阅读  
  
  
  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-shadow: rgb(0, 0, 0) 0px 0px 0px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">01</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 14px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span style="font-size: 12px;box-sizing: border-box;"><span leaf=""><a class="normal_text_link" target="_blank" style="" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789714&amp;idx=1&amp;sn=e6360c1e3d02d5c6e9b2e11b55f5a99f&amp;scene=21#wechat_redirect" textvalue="OpenAI下场做竞品，要掀翻代码托管赛道" data-itemshowtype="0" linktype="text" data-linktype="2">OpenAI下场做竞品，要掀翻代码托管赛道</a></span></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">02</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 12px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span leaf=""><a class="normal_text_link" target="_blank" style="" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789628&amp;idx=1&amp;sn=eeee12f87f31b54f145b66896be008fa&amp;scene=21#wechat_redirect" textvalue="GPT-5.2可稳定量产零日漏洞利用" data-itemshowtype="0" linktype="text" data-linktype="2">GPT-5.2可稳定量产零日漏洞利用</a></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">03</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 12px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span leaf=""><a class="normal_text_link" target="_blank" style="" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789606&amp;idx=1&amp;sn=7d2c4b5698325f59429e7cdcb01b28b8&amp;scene=21#wechat_redirect" textvalue="暗网犯罪论坛遭攻破，32万用户数据全泄露" data-itemshowtype="0" linktype="text" data-linktype="2">暗网犯罪论坛遭攻破，32万用户数据全泄露</a></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr></tbody></table>  
  
  
**安全KER**  
  
  
安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/g5KiabmYVDH0lGF732N7tzWyCNaKV5I4YZEfeLFa6spoTkacO9eWE0Ft5qkcMCkyibF7ic33ZvRkCvNof6Iic9oszSicLEh5cXvVKetHvKpdTXpk/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/g5KiabmYVDH1qXMHEicN23IBicv6Nv9hwXK4HZo3W2Azh8rn62dlRBm8P2glmhjcqMfZmk0ta6qyFXHxCxbCs0LcyULch4gPlxsKk3R0mlFFwM/640?wx_fmt=png "")  
  
**注册安全KER社区**  
  
**链接最新“圈子”动态**  
  
