#  警惕！Ivanti RCE零日漏洞复盘：这是一场针对IT管理者的“外科手术式”打击  
原创 Hankzheng
                    Hankzheng  技术修道场   2026-02-11 23:59  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kBd83kxr9I54wlKv9qd6YBIV2fZMmyQicpYe5pVUGr7OKEazrfyFEgH8qQMicKLS1f2AZ5RNh64aLpPr0MEbC4EnmhGhJcHm5MJnBBzACTMYI/640?wx_fmt=png&from=appmsg "")  
  
大家好，这两天技术圈的朋友圈估计都被一条消息刷屏了：**荷兰、芬兰政府机构接连“中招”，欧洲委员会也未能幸免。**  
  
而罪魁祸首，竟然是咱们IT运维最信任的工具之一——**Ivanti Endpoint Manager Mobile (EPMM)**  
。说实话，看到这个消息时，我第一反应是：**又是它？**  
  
作为一名在坑里爬了多年的IT，今天我想带大家拆解一下这次 Ivanti 零日漏洞事件。这不仅仅是一次简单的信息泄露，它背后暴露出的**技术实现逻辑**  
和**企业内网安全架构**  
，绝对值得咱们每个做架构和运维的兄弟深思。  
## 01. 噩梦般的 CVSS 9.8：到底发生了什么？  
  
这次出事的是 Ivanti EPMM（原名 MobileIron Core），这玩意儿大家应该不陌生，是专门用来管理企业移动设备（MDM）的。它的权限极大：管理App、配置策略、甚至远程抹除手机。  
  
但也正因为它处于“核心地位”，一旦出事就是顶级灾难。这次曝出的两个漏洞简直是“开门红”：  
<table><thead><tr><th style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;background-color: rgb(242, 242, 242);"><section><span leaf=""><span textstyle="" style="font-size: 15px;">漏洞编号</span></span></section></th><th style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;background-color: rgb(242, 242, 242);"><section><span leaf=""><span textstyle="" style="font-size: 15px;">CVSS 评分</span></span></section></th><th style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;background-color: rgb(242, 242, 242);"><section><span leaf=""><span textstyle="" style="font-size: 15px;">漏洞类型</span></span></section></th><th style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;background-color: rgb(242, 242, 242);"><section><span leaf=""><span textstyle="" style="font-size: 15px;">影响</span></span></section></th></tr></thead><tbody><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">CVE-2026-1281</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;"><strong style="color: rgb(231, 76, 60);"><span leaf=""><span textstyle="" style="font-size: 15px;">9.8 (紧急)</span></span></strong></td><td style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">RCE (远程代码执行)</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">未经身份验证的远程攻击</span></span></section></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">CVE-2026-1340</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;"><strong style="color: rgb(231, 76, 60);"><span leaf=""><span textstyle="" style="font-size: 15px;">9.8 (紧急)</span></span></strong></td><td style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">RCE (远程代码执行)</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 10px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">完全接管服务器权限</span></span></section></td></tr></tbody></table>> 科普：  
>  9.8分意味着什么？意味着这个漏洞不仅**危害极大**  
，而且**利用门槛极低**  
。黑客不需要任何账号密码，就能通过远程发送特定的数据包，直接在你的服务器上执行任意代码。  
  
  
荷兰数据保护局（AP）和法院系统就在 1 月底被黑客“黑了”，员工的姓名、办公邮箱、电话号码等敏感信息被洗劫一空。虽然官方说 9 小时内就控制了局面，但“痕迹”已经留下，损失已成定局。  
## 02. 技术细节拆解：那个“删了又没删”的神坑  
  
在这次事件的通报中，芬兰政府机构 Valtori 的遭遇最让我感触。他们有近 **50,000 名**  
 员工的信息泄露，而背后暴露出的技术细节简直是“教科书级”的教训。  
  
调查发现，黑客不仅拿走了现有数据，还拿走了**已经删除**  
的数据。为什么？因为该管理系统在处理数据时，并没有进行**物理删除**  
，而只是做了**逻辑删除**  
。  
  
**逻辑删除 vs 物理删除：**  
- **逻辑删除：**  
 只是在数据库里给这条记录打个标记（比如 is_deleted = 1  
），在 UI 界面上看不见了，但数据依然实打实地躺在磁盘里。  
  
- **风险点：**  
 这种做法在普通业务系统里为了方便“数据找回”很常见，但在**高权限的安全管理系统**  
里，如果权限校验被绕过（比如这次的 RCE 漏洞），黑客直接通过数据库脱库，就能把这些“陈年老账”全部翻出来。  
  
**碎碎念：**  
 兄弟们，咱们在写代码或者设计架构时，对于敏感信息（尤其是涉及身份校验的轨迹数据），千万要评估好“逻辑删除”的副作用。有时候为了省事，可能给未来埋了一颗惊天大雷。  
## 03. 为什么又是 MDM？“信任边界”正在塌陷  
  
watchTowr 的 CEO Benjamin Harris 说了一句话：  
> “这不再是随机的投机性攻击，而是**高水平、资源充足的黑客发起的精密行动**  
。任何被认为是‘内部’或‘安全’的系统，现在都应该被怀疑。”  
  
  
长期以来，我们习惯于把 MDM、VPN、网关这些设备当作“安全堡垒”。我们觉得只要这些东西守在门口，内网就是安全的。但现实是：**攻击者正在瞄准你最信任、嵌入最深的系统。**  
  
这就像是一个小偷不再费劲撬你家门，而是直接搞定了你家的智能门锁后台。一旦这类拥有高权限的管理工具被攻破，黑客就相当于拿到了进入你整个企业内网的“万能钥匙”。  
## 04. 咱们能从中学到什么？  
  
作为有几年经验的技术人，咱们不能只看个热闹，得看点门道：  
  
**1. 打补丁的速度就是生命线：**  
  
Ivanti 在 1 月 29 日发布了补丁，芬兰当天就装了，但黑客的速度可能比你想象的还要快。对于这类暴露在公网的高风险管理后台，**自动化监控和快速响应机制**  
比什么都重要。  
  
**2. 默认“不信任”任何组件（Zero Trust）：**  
  
不要觉得买了牛逼的安全软件就万事大吉了。所有的第三方商业软件，特别是具有远程代码执行权限的，都必须纳入监控范围。记住：**越是核心的系统，越要保持怀疑。**  
  
**3. 数据生命周期管理的闭环：**  
  
如果你的系统存储了大量员工或用户的隐私敏感数据，请重新审视你们的删除逻辑。**过期数据不仅是没用的数据，更是随时可能爆炸的资产风险。**  
  
写在最后：安全没有终点。身为技术人，我们不仅要追求代码的优雅和系统的稳定，更要时刻保持一颗“怀疑”的心。毕竟，在这个数字时代，最危险的地方，往往就是你认为最安全的地方。  
  
**关于这次“删了又没删”的逻辑坑，你在工作中遇到过类似的尴尬事吗？或者你对 MDM 的安全性有什么看法？欢迎在评论区留言，咱们聊聊！**  
  
如果你觉得这篇文章对你有启发，别忘了点个“推荐”并转发给身边的技术伙伴。  
  
咱们下期再见！  
  
