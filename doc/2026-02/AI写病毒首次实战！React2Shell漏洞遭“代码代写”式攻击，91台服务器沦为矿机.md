#  AI写病毒首次实战！React2Shell漏洞遭“代码代写”式攻击，91台服务器沦为矿机  
看雪学苑
                    看雪学苑  看雪学苑   2026-02-12 10:00  
  
你可能听说过“Vibe Coding”——程序员靠AI辅助写代码，边听歌边“意念编程”。但今天，这套开发范式正式流向了暗网。  
  
  
Darktrace全球蜜网“CloudyPots”近日捕获一例代号React2Shell的漏洞攻击。令人脊背发凉的是：攻击者使用的核心恶意代码，76%由大语言模型（LLM）生成。  
  
  
这不是概念验证。这是一场完全由AI“代笔”的真实入侵。  
  
  
攻击链复盘：从伪装容器到门罗币挖矿  
  
目标是一个故意暴露Docker API的蜜罐环境——模拟云原生架构中常见的配置失误。攻击者通过Docker API嗅探到开放接口，随即发起行动：  
  
  
第一步：投放“合法脸”容器  
  
一个名为`python-metrics-collector`的容器被创建。命名极力模仿真实监控服务，意图绕过基础检测。  
  
  
第二步：自动装配武器库  
  
容器启动后立刻安装curl、wget、python3等基础工具，并从Pastebin拉取依赖清单——整套动作干净利落，毫无冗余。  
  
  
第三步：GitHub Gist充当弹药库  
  
核心Python脚本托管在`smplu[.]link`，重定向至GitHub用户`hackedyoulol`的Gist。该账号现已被封禁。  
  
  
代码会“说话”：AI痕迹肉眼可见  
  
  
研究人员拆解Python载荷时发现了典型LLM指纹：  
  
注释密度异常高，甚至包含  
“Network Scanner with Exploitation Framework – Educational/Research Purpose Only”  
这类教育声明。  
  
  
结构极其规整，Next.js服务器组件Payload被刻意结构化，用于抛出异常以泄露命令输出——正是React2Shell漏洞的核心利用手法。  
  
  
经GPTZero检测，76%代码判定为AI生成。显然，攻击者以“学术研究”为由“越狱”了安全对齐的模型，拿到了可立即投入实战的漏洞利用脚本。  
  
  
91台主机，5英镑——但意义远超收益  
  
最终Payload是XMRig 6.21.0矿机，指向`supportxmr`矿池。截至报告发布，攻击者钱包地址显示  
感染91个节点  
，累计挖出0.015 XMR——按实时币价，约合  
5英镑  
。  
  
  
财务回报几近戏谑，但战术价值足以让防御者失眠：  
  
- 攻击者无明显技术水平，却完成了从漏洞发现、容器逃逸到矿机部署的全链路攻击。  
  
- 工具链由AI代工，意味着未来每一波攻击都可能是定制化、多形态、签名无效的。  
  
- 该恶意软件不含蠕虫自传播模块，扩散逻辑由攻击者远程控制——IP`49[.]36.33.11`（印度住宅IP）被怀疑为“播种机”中枢，这种人机协同模式进一步模糊了自动化攻击的边界。  
  
  
“React2Shell”事件向业界释放明确信号：  
  
AI不仅降低了入行门槛，更消灭了“代码复用”这个传统威胁情报赖以生存的前提。    
  
一个低技能攻击者，只需要一个有效的提示词，就能在一小时内生成一份语法干净、注释规范、逻辑严密的零日武器。  
  
  
静态哈希、域名黑名单、特征码匹配——这些防御手段在面对“AI每写一次就重构一次”的恶意代码时，正在快速失效。  
  
  
唯一有效的对抗路径：    
  
行为基线检测：  
无论代码如何变化，容器启动异常子进程、挖矿网络通信等行为模式依然可被识别。    
  
  
漏洞侧快速封堵：  
React2Shell这类漏洞本可通过及时打补丁消解。AI让漏洞利用变得廉价，也让补丁管理从未如此紧迫。  
  
  
  
参考来源  
  
本文信息综合自Darktrace安全团队发布的《Threat Actors Exploiting React2Shell Vulnerability Using AI-Generated Malware》事件分析报告及公开IoC数据。  
  
  
﹀  
  
﹀  
  
﹀  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
