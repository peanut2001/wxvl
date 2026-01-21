#  研究显示：GPT-5.2可稳定量产零日漏洞利用  
 安全客   2026-01-21 03:13  
  
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
  
  
推荐阅读  
  
  
  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-shadow: rgb(0, 0, 0) 0px 0px 0px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">01</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 14px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span style="font-size: 12px;box-sizing: border-box;"><span leaf=""><a class="normal_text_link" target="_blank" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;color: rgb(87, 107, 149);text-decoration: none;-webkit-user-drag: none;cursor: default;max-width: 100%;font-family: &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 12px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: 1px;orphans: 2;text-align: justify;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789613&amp;idx=1&amp;sn=5fb152f4cb50fd27686f3bdee7900fff&amp;scene=21#wechat_redirect" textvalue="AI基础设施成自动化攻击新靶标" data-itemshowtype="0" linktype="text" data-linktype="2">AI基础设施成自动化攻击新靶标</a></span></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">02</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 14px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span style="font-size: 12px;box-sizing: border-box;"><span leaf=""><a class="normal_text_link" target="_blank" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;color: rgb(87, 107, 149);text-decoration: none;-webkit-user-drag: none;cursor: default;max-width: 100%;font-family: &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 12px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: 1px;orphans: 2;text-align: justify;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789606&amp;idx=1&amp;sn=7d2c4b5698325f59429e7cdcb01b28b8&amp;scene=21#wechat_redirect" textvalue="黑吃黑！暗网犯罪论坛被黑客攻破" data-itemshowtype="0" linktype="text" data-linktype="2">黑吃黑！暗网犯罪论坛被黑客攻破</a></span></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(62, 62, 62);border-style: none;box-sizing: border-box;padding: 0px;"><section style="box-sizing: border-box;"><section style="display: flex;flex-flow: row;margin: 10px 0% 0px;justify-content: flex-start;box-sizing: border-box;"><section style="display: inline-block;vertical-align: middle;width: auto;min-width: 10%;max-width: 100%;height: auto;flex: 0 0 auto;align-self: center;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(115, 215, 200);line-height: 1;letter-spacing: 0px;text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">03</span></strong></p></section></section><section style="display: inline-block;vertical-align: middle;width: auto;flex: 100 100 0%;align-self: center;height: auto;box-sizing: border-box;"><section style="font-size: 14px;letter-spacing: 1px;line-height: 1.8;color: rgb(140, 140, 140);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(224, 224, 224);box-sizing: border-box;"><span leaf="">｜</span></span><span style="font-size: 12px;box-sizing: border-box;"><span leaf=""><a class="normal_text_link" target="_blank" style="" href="https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&amp;mid=2649789621&amp;idx=1&amp;sn=d5f11dfa319b3471e1c14e45e8a11b9b&amp;scene=21#wechat_redirect" textvalue="Promptware:新兴AI攻击威胁与五步杀伤链" data-itemshowtype="0" linktype="text" data-linktype="2">Promptware:新兴AI攻击威胁与五步杀伤链</a></span></span></p></section></section></section><section style="margin: 5px 0%;box-sizing: border-box;"><section style="background-color: rgb(224, 224, 224);height: 1px;box-sizing: border-box;"><svg viewBox="0 0 1 1" style="float:left;line-height:0;width:0;vertical-align:top;"></svg></section></section></section></td></tr></tbody></table>  
  
  
**安全KER**  
  
  
安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4fn84CeJicpp1toTr8W74FQJzfFwClZqU9xZZPl97enicdWFjAic3dibCXY9jhb2hNDDUolo7IRNqRUg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4fn84CeJicpp1toTr8W74FQ3gBRyEfNXasIOo1WNIIHuGm8vaEQQUKgJresGuuyG4ib0J3sBUIkDUA/640?wx_fmt=png&from=appmsg "")  
  
**注册安全KER社区**  
  
**链接最新“圈子”动态**  
  
