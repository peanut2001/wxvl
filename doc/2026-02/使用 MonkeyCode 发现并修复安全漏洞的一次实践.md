#  使用 MonkeyCode 发现并修复安全漏洞的一次实践  
 GG学安全   2026-02-10 12:07  
  
最近用 AI Coding 平台   
https://monkeycode-ai.com/ 做了一次挺有意思、也挺“实战”的尝试：把一个真实的开源项目直接丢给 AI，让它帮忙做安全审计，并且 真的找到了漏洞，还顺手修掉、合并进了主干 。  
  
这篇文章简单记录一下整个过程。  
  
  
01  
  
漏洞发现  
  
  
事情的起因很简单。  
  
我把 1Panel 的代码仓库直接交给   
MonkeyCode，然后只说了一句话：  
  
看看这个仓库里有没有安全漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vHkGQ9mbNmR3y3sDuMJib6me74OTQ4bQJhoLsiaoiab0E9RwAGP0xtu6n4EXjAGgZ5J9GX2HIjFRn9WbQb1eTibGpoB0zreWrocibVYnMD1T8QHQ/640?wx_fmt=png&from=appmsg "")  
  
接下来   
MonkeyCode 就开始自己干活了：   
  
从代码结构、数据流、危险调用一路分析下去， 连续跑了十几分钟 。  
  
最后给出的结论是：  
- 2 个 SQL 注入  
  
- 8 个命令注入  
  
为了确认不是“AI 幻觉”，我随手挑了其中两个漏洞，在 1Panel 官方 Demo 上做了简单验证。  
  
结果很明确：  
  
 👉 确实可以注入，AI 并没有瞎说。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vHkGQ9mbNmS2Bn6l3ictLA1s9ytvTQLgibRqh7icTWJsAbJIpr9FZiaOP9FNlu2hsRuJqwmrEibfqwEicKPXCHjiby1EZS1HWgRRtLNOnc6E6GicFzY/640?wx_fmt=png&from=appmsg "")  
  
  
02  
  
漏洞修复  
  
  
确认漏洞存在之后，就进入修复阶段。  
  
我基于前面的检测结果，又分别发起了两个开发任务：  
1. 一个用于修复 SQL 注入  
  
1. 一个用于修复 命令注入  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vHkGQ9mbNmQU4Sb3eQJCYyia4BDuVQ0NdaicLEAdibWy7RibafawCZpAcy1vxZnTSaxXJlNIozy9qQjIJcS9MmK4XicRpEiaGzmK93ia7XaJWBRC6Q/640?wx_fmt=png&from=appmsg "")  
  
这一步明显比“发现漏洞”要快得多：  
  
MonkeyCode 根据上下文直接定位代码  
- 给出具体修改方案  
  
- 顺手把补丁补完整。  
  
大概一分钟左右，修复就完成了 ，从代码层面看也比较干净、规范。  
  
接下来就是常规流程：   
  
👉 把修复推到 GitHub，提 PR，等 1Panel 官方团队合并。  
  
  
03  
  
Review  
  
  
PR 提交之后，我顺手又喊了   
MonkeyCode  
 的机器人来 review，让它自己当 Reviewer 把代码再过一遍。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vHkGQ9mbNmQ3uwIMmS7WQTNBbvvcroVlsS7yZRYULhdBPq1LW7qpcr2TndQYBX1t6icC3TzomlVeMJrtyGibCoQeYKze4Ik3grTXVRKicsXEkQ/640?wx_fmt=png&from=appmsg "")  
  
打个广告，  
MonkeyCode  
 的 review 功能真的非常好用，在 github 上直接 @  
MonkeyCode  
-ai 就可以调用，也可以配置 webhook 让仓库自动触发。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vHkGQ9mbNmTyZzt77skaBQibnIHzJ5VG0DibMupBPrHWoUorgBtQ4eholUEOpaoAy9CbJHAMBrb5ibeTlGHKyOsicCwtBkk0r3s8nS7JsVHyLLE/640?wx_fmt=png&from=appmsg "")  
  
这一步其实挺有意思的，相当于：  
- 同一个 AI  
  
- 站在 开发者视角 修漏洞  
  
- 再切换到 审计 / Review 视角 查问题  
  
整体 Review 结果也比较符合预期，没有发现明显的逻辑或安全回退问题。  
  
  
04  
  
合并  
  
  
PR 刚提交没几分钟，就收到了官方的响应（给 1Panel 团队点个赞）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vHkGQ9mbNmQL3OvHqW5TkjAKLtTUAPUdR0CpqyETt6icHlMlMURXbUJ0v3ROgIx4K0lMj22ISjzJrCBRicb3nwoReZHSu0tkiaDhgaQFEY5ujE/640?wx_fmt=png&from=appmsg "")  
  
中间过程十分顺畅，又过了几分钟， PR 顺利合并 。  
  
至此，MonkeyCode 也算是正式成为了 1Panel 的一名“贡献者”。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vHkGQ9mbNmRtU4RPUliaOKlZ97vOzhNoTlEpBWSoy0iaBLU1lBuJmHpVlVpmhUZLV0fakibibjxaCX4VtzlPeKNawk0Oz4YEYdbuKrV28vNCoqk/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vHkGQ9mbNmQicTUq5TpicmRuVCH27IDHn7k8YmWicAKYHVoqicbG6PjJ1mfpAt0NoFzk9j4PcnP1qQzGPjzVOAZDEUyKuexb1r1O1OFvnybYHhQ/640?wx_fmt=png&from=appmsg "")  
  
  
05  
  
一点感受  
  
  
这次体验下来，一个很直观的感受是：  
  
AI 不只是 “帮你写代码”，而是真的可以参与到 安全审计 → 漏洞修复 → Code Review → 开源协作 的完整流程里。  
  
而且在这种真实项目、真实漏洞的场景下，效果并不虚。  
  
后面如果还有类似的实战案例，应该还会继续拿 MonkeyCode 折腾一折腾。  
  
