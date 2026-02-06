#  Claude新模型4.6：开箱即挖500个0day漏洞，源代码审计即将颠覆  
点击关注👉
                    点击关注👉  马哥网络安全   2026-02-06 09:00  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAk1nlByTOFiahZKGHekfZGC180aw53rHwCE1KXCFEyHULHRFVH3sTdiaibVFgTPic4UWScria3Vocb1TyQ/640?wx_fmt=png&from=appmsg "")  
  
一睁眼，Anthropic上新模型，让  
Claude Opus 4.6  
来给您拜！年！了！  
  
  
消息一出，金融数据服务商FactSet最惨盘中暴跌10%，S&P Global、穆迪、纳斯达克公司纷纷下跌，各大指数全线跳水。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX39upMkkcZR6LQwOL5DnYVD5npEABv1iaeDe1j92uId6mFQJTZys5wh4e7IP0Aa0Mmyrl00bVccmm1WNvsws5RnibPHjBFY5XHnc/640?wx_fmt=png&from=appmsg#imgIndex=1 "")  
  
  
这已经是Anthropic你小子本周第二次搅动市场了。  
  
  
几天前，它旗下一款自动化法律工作的插件悄悄上线，直接引爆了万亿美元级别的软件股暴跌。  
  
  
投资者的恐慌聚焦在一个问题：谁能保证几年内不被AI颠覆？不能就抛售。  
  
  
想不到今天的Anthropic更狠。  
  
  
今天以前，大家对Claude的印象，就是编程能力断档性的强。  
  
  
Claude Opus 4.6冷笑一声，梆梆一拳打破这个印象：俺在网络安全领域也很强！  
  
  
**Part01**  
## 源代码审计颠覆  
  
  
官方博客显示，Opus 4.6一出，几乎无模型能与其争锋。  
  
  
在编码、知识工作、搜索、推理等核心场景，Opus 4.6有显著突破。  
  
  
多项评测成绩超越前代及行业竞品。  
  
  
尤其在编程能力方面，Opus 4.6在Terminal-Bench 2.0中拿到了最高分。  
  
  
从成绩背后的实际能力来看，Opus 4.6能更周密地进行任务规划，可在大型代码库中稳定运行，代码审查与调试精度提升。  
  
  
而且能自主发现自身错误。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0x8oYaibsfKxybtDAxee0fxWzSWmaZtUILEBCEM5icxcDmMlCzhalYWwgSK0RN7MiaqDqwIzfKkjjjibmPRicdY3xUwaeRLLpaT2vM/640?wx_fmt=png&from=appmsg#imgIndex=2 "")  
  
  
难得的是，这种智力的飞跃并没有以牺牲安全性为代价。  
  
  
在Anthropic最看重的自动化行为审计中，Opus 4.6的对齐水平极高，同时，欺骗、奉承等负面行为极低。  
  
  
Opus 4.6甚至解决了目前AI圈普遍头疼的“过度拒绝”问题——  
  
  
在面对正常的、无害的请求时，它比以往任何模型都更少地表现出那种死板的拒绝。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3dNUzmltbHdfjRrBNv0fUBCc3TRML7f4qF9hQJBs9zNVic6WBc72vNONxpYJsn0ICibO67RgMt96CmAqNOzN6HNuhQ1ictIh5puM/640?wx_fmt=png&from=appmsg#imgIndex=3 "")  
  
  
**Part02**  
## 500个零日漏洞，开箱即挖  
  
  
Opus 4.6在网络安全领域的表现让Anthropic自己都有点意外。  
  
  
在发布前的测试中，Anthropic的前沿红队把Opus 4.6扔进一个沙箱环境，给它Python和常规漏洞分析工具（fuzzer、debugger那些），没有任何专门指令或领域知识，让它自己去找开源代码里的漏洞。  
  
  
结果它  
挖出了超过500个此前未知的高危零日漏洞  
。  
  
  
每一个都经过了Anthropic团队成员或外部安全研究员的验证的哦。  
  
  
具体案例包括：  
  
- 在GhostScript（一个处理PDF和PostScript文件的常用工具）中发现了一个可导致崩溃的漏洞，而且是在传统fuzzing和人工分析都没找到问题之后，Claude自己翻了项目的git提交历史才挖出来的；  
  
- 在OpenSC（处理智能卡数据的工具）和CGIF（处理GIF文件的工具）中发现了缓冲区溢出漏洞；在CGIF那个案例里，Claude甚至主动写了PoC（概念验证代码）来证明漏洞真实存在。  
  
Anthropic前沿红队负责人Logan Graham说，如果这成为未来开源软件安全审计的主要方式之一，他一点也不惊讶。  
  
  
不过Anthropic也承认，这种能力可能被滥用。  
  
  
为此，  
团队加了六套新的网络安全探测机制，未来可能会上线实时拦截系统来阻止恶意流量。  
  
  
**参考来源：**  
  
Claude新模型4.6来了！更多饭碗没了：华尔街财务、编译器、安全白帽、PPT…通通失守  
  
https://mp.weixin.qq.com/s/Z5J48QTKmm4lt_GQqtqLIQ  
  
****  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAkmMvIEVFdiaG19OichW7IMqrianjXzneqZoJ3rMMFygyGVdictzTMWy15vH5nhoWznKInJQ9yXzBpBFg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
