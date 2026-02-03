#  一个漏洞，控制所有VM：CloudCone事件的技术复盘  
原创 AI安全工坊
                    AI安全工坊  AI安全工坊   2026-02-03 09:23  
  
# 一个漏洞，控制所有VM：CloudCone事件的技术复盘  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BibeFvVBkRAibzQZBnnUhDvIOf5JdjBicosrdicDdAkqE1fUJrV4lTglfQUoZnBJqZy0xqyah26jPuqaOST7qSzzYA/640?wx_fmt=jpeg&from=appmsg "")  
  
 1月30日凌晨，CloudCone 的用户们醒来后发现：自己的 VPS 挂了。  
  
不是普通的宕机。是那种"你的数据永远回不来了"的挂法。  
  
CloudCone 官方在工单里写得很直白：“攻击者已经破坏了你服务器关联的磁盘，数据无法恢复。”  
  
没有商量余地。没有恢复方案。没有备份的话，数据就是真的没了。  
  
这不是个例。同一时间，HostSlick 报告超过 25% 的基础设施被感染，OuiHeberg 也中招。更让人不安的是，至少还有 8 家使用相同技术架构的服务商可能面临同样的风险。  
  
下面是这次攻击的技术复盘。  
## 攻击链解析：一场"隐身入侵"  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BibeFvVBkRAibzQZBnnUhDvIOf5JdjBicosvm9AdI09GoiaJkebegNb1VQDX7CkwV83UA2lwxJmGC3nbeOiclZ3DT8A/640?wx_fmt=jpeg&from=appmsg "")  
### 为什么 SSH 日志里什么都没有？  
  
这次攻击最诡异的地方：受害者的 SSH 登录日志完全正常。  
  
没有异常登录记录。没有暴力破解痕迹。没有可疑 IP。  
  
CloudCone 在事件报告中确认：“证据表明，这次活动是通过管理层访问发起的，而非直接 SSH 连接，这解释了为什么没有异常 SSH 登录记录。”  
  
攻击者根本没走前门。他们走的是后门：VPS 管理面板。  
### Virtualizor：那个被忽视的"超级管理员"  
  
大多数廉价 VPS 服务商使用 Virtualizor 管理面板。它能让服务商批量管理成百上千台虚拟机：创建、删除、重启、迁移，一键搞定。  
  
Virtualizor 还有一个 WHMCS 插件，用来对接计费系统。用户付款后，系统自动开通 VPS；欠费了，自动暂停。  
  
问题就出在这个插件上。  
  
根据 LowEndBox 的报道，早在 2025 年 11 月，法国服务商 OuiHeberg 就遭遇了类似攻击。他们的安全团队成功复现了攻击路径：  
> "  
> “我们的内部团队成功复现了攻击——通过 WHMCS 插件与 Virtualizor API 的通信执行 payload。”  
  
  
翻译成人话：攻击者找到了 WHMCS 插件和 Virtualizor API 之间的通信漏洞，可以通过这个漏洞向所有连接的虚拟机发送命令。  
  
一个漏洞，控制所有 VM。  
### 攻击手法类比：和 Google AI 助手被黑如出一辙  
  
这让我想起之前分析过的案例：Google 的 AI 编程助手 Antigravity 被攻击。  
  
那次攻击中，黑客在网页里用 1 像素大小的字体隐藏了恶意指令。AI 助手读取网页时，把这些隐藏指令当成了正常任务，然后乖乖执行：收集用户密码，发送给攻击者。  
  
整个过程，用户毫无察觉。因为 AI 表面上还在"正常工作"。  
  
CloudCone 这次攻击的逻辑几乎一样：  
- • Antigravity 攻击：恶意指令隐藏在网页中 → AI 读取并执行 → 绕过用户感知  
  
- • CloudCone 攻击：恶意命令通过管理 API 发送 → 虚拟机执行 → 绕过 SSH 日志  
  
核心都是：**攻击发生在"可信通道"内部**  
。  
  
AI 助手信任网页内容，所以执行了隐藏指令。VPS 虚拟机信任管理面板的命令，所以执行了恶意脚本。  
  
传统安全措施（SSH 日志监控、防火墙规则）完全失效，因为攻击根本没走这些路径。  
## Virtualizor 的回应：否认  
  
OuiHeberg 把漏洞报告给了 Virtualizor。Virtualizor 的回应？  
  
**否认。**  
  
他们在 LowEndTalk 论坛上发帖说：“这次安全事件不是 Virtualizor 造成的。”  
  
OuiHeberg 直接反驳：  
> "  
> “Virtualizor 否认这个攻击向量，并要求我们也否认，以避免’损害他们的品牌形象’。但事实是，攻击者确实是通过 Virtualizor 的 WHMCS 插件进入的。”  
  
  
他们甚至表示会发布漏洞利用的视频演示，让 Virtualizor “试着修复这类攻击”。  
  
截至我写这篇文章时，Virtualizor 仍未承认漏洞存在，也没有发布任何安全补丁。  
  
所有使用 Virtualizor + WHMCS 组合的服务商，可能都还暴露在同样的风险中。  
  
根据 Cyber Kendra 的报道，潜在风险服务商包括：ColoCloud、Virtono、SolidSEOVPS、Naranjatech、LittleCreek、DediRock、Chunkserv、RareCloud。  
  
如果你正在使用这些服务商的 VPS，现在就去做备份。不是明天，是现在。  
## 2025-2026：虚拟化层成为勒索软件重灾区  
  
CloudCone 事件不是孤例。  
  
Huntress 的研究数据显示：2025 年，针对虚拟化层（hypervisor）的勒索攻击占比从上半年的 3% 飙升到下半年的 25%。  
  
增长了 700%。  
  
为什么攻击者开始瞄准虚拟化层？  
  
传统勒索软件需要一台一台感染。但攻破一个 hypervisor，就能同时加密上面运行的几十甚至几百台虚拟机。  
  
一次入侵，批量收割。  
  
这就是为什么 VMware ESXi 漏洞在过去一年被疯狂利用。这也是为什么 Virtualizor 这样的管理面板成为高价值目标。它们是虚拟化基础设施的"中枢神经"。  
  
控制了管理面板，就控制了一切。  
## 廉价 VPS 的代价  
  
CloudCone 是一家以"便宜"著称的 VPS 服务商。他们的年付套餐低至 14 美元。一年。  
  
便宜有便宜的代价。  
  
低价意味着低利润，低利润意味着有限的安全投入。有限的安全投入意味着：当漏洞出现时，你可能是最后一个知道的人。  
  
我不是说贵的服务商就一定安全。但当你选择年付 14 美元的 VPS 时，你需要清楚地知道：  
1. 1. **你的数据安全，主要靠你自己**  
  
1. 2. **服务商的安全能力，可能不如你想象的强**  
  
1. 3. **出事之后，你能得到的补偿可能只是"免费重装系统"**  
  
CloudCone 在事件公告中强调：“客户个人数据和计费系统未受影响。”  
  
但对于那些丢失了网站、数据库、项目代码的用户来说，这句话大概没什么安慰作用。  
## 你能做什么？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BibeFvVBkRAibzQZBnnUhDvIOf5JdjBicosIhkLicCMR0a3HTQ4niay9icU5gkKPEfakVg2yjuBD0qdb9DMva5FPoBAA/640?wx_fmt=jpeg&from=appmsg "")  
### 1. 备份，备份，备份  
  
不要依赖服务商的备份。自己做。  
- • **关键数据**  
：每小时备份  
  
- • **一般数据**  
：每天备份  
  
- • **备份存储**  
：必须在不同的服务商、不同的地理位置  
  
如果你的备份和生产环境在同一个服务商，那它就不是真正的备份。  
### 2. 假设你的服务商会被黑  
  
2025 年的安全形势：68% 的勒索软件受害者在 6 个月内会遭遇第二次攻击。41% 的成功攻击与零日漏洞相关。  
  
没有任何服务商能保证 100% 安全。  
  
设计你的架构时，要假设任何一个节点都可能失效。数据要有冗余，服务要能快速迁移。  
### 3. 监控你的 VPS 管理面板  
  
传统的安全监控关注 SSH 日志、系统日志、网络流量。  
  
但这次攻击告诉我们：管理面板也是攻击面。  
  
如果你的服务商提供 API 访问日志，定期检查。如果没有，考虑换一家。  
### 4. 关注你使用的服务商的安全动态  
  
CloudCone 的状态页在 1 月 30 日就发布了事件通知。但很多用户是在数据丢失后才知道发生了什么。  
  
订阅你服务商的状态页更新。加入相关的社区（比如 LowEndTalk）。信息差可能就是你数据的生死差。  
## 写在最后  
  
CloudCone 事件给我最大的感触：**安全边界正在模糊**  
。  
  
以前我们觉得，只要 SSH 密钥够强、防火墙规则够严、系统补丁够新，就能高枕无忧。  
  
但现在，攻击可能来自你信任的管理面板。来自你依赖的第三方插件。来自你从未想过会出问题的"可信通道"。  
  
这不是说传统安全措施没用了。而是说，它们不够了。  
  
我们需要更全面的安全思维：  
- • 不只是保护入口，还要保护整个供应链  
  
- • 不只是监控异常，还要假设正常流量中也可能藏着攻击  
  
- • 不只是依赖服务商，还要有自己的兜底方案  
  
最后，回到那个最朴素的建议：  
  
**去做备份。现在。**  
  
如果你正在使用任何 VPS 服务，不管是 CloudCone 还是其他家，花 10 分钟把关键数据备份到本地或者另一个服务商。  
  
这 10 分钟，可能是你今年最值的投资。  
  
**参考来源**  
：  
- •CloudCone官方状态页：https://status.cloudcone.com/incidents/346624  
  
- • Cyber Kendra 报道：https://www.cyberkendra.com/2026/02/mass-vps-provider-breach-exposes.html  
  
- • LowEndBox 报道：https://lowendbox.com/blog/provider-claims-virtualizor-whmcs-plugin-vulnerability-caused-breach-virtualizor-refuses-to-admit-the-problem-exists/  
  
  
  
  
  
## AI安全工坊内部社群  
  
  
  
**🔥 AI安全工坊社群 · 6大核心价值 🔥**  
  
****1. **AI安全实战**  
→ AI渗透测试 | 模型加固 | 数据防护 | 模型测评  
  
1. **开发全栈指南**  
→ 大模型应用 | Agent开发 | 行业解决方案 | AI安全工具 | AI产品开发  
  
1. **商业落地加速**  
→ 案例拆解 | ROI优化 | 合规指南  
  
1. **专属学习支持**  
→ 文档库 | 答疑 | 代码示例 | 1v1 解答  
  
1. **独家资源网络**  
→ 工具包 | 漏洞库 | 行业报告 | AI视频课程 | AI多模态资源  
  
1. **高质量AI社群**  
→ 技术交流 | 内推机会 | 项目合作  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRAicHn7IC6WXiaPEfumEvmO15U6l7p2efUz1oia0ugSlK5FwtEbMNcUMoGOt3hoSNfibSmiaNtFu80V138g/640?wx_fmt=png&from=appmsg "")  
  
  
## AI安全工坊-AISecKit安全工具资源平台  
  
  
  
**网站地址：https://aiseckit.com/**  
  
**网站介绍：AISecKit 提供了一个专注于 AI 安全工具和大型语言模型安全资源的平台，为专注于 AI 安全和网络安全专业人士提供了一系列的工具和资源。**  
  
****  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8OoawLw7oR4iaTVrY2q4h0ictEjkEkjf68kicX0Yyb4Dpnriay22UDxnIWTClicVKia16yicNEZYjIUaibJw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
## 福利赠送  
  
  
  
🎁 **立即获取福利，在公众号后台私信发送下方关键词，即可免费领取专属工具和教程：**  
<table><tbody><tr><td data-colwidth="268" width="268" valign="top" style="word-break: break-all;"><section><span leaf="">关键词</span><span style="display: none;line-height: 0px;"><span leaf="">‍</span></span><span style="display: none;line-height: 0px;"><span leaf="">‍</span></span></section></td></tr><tr><td data-colwidth="268" width="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">AI大模型安全评估标准和指南</span></span></td></tr><tr><td data-colwidth="268" width="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">智擎 - AI业务场景提示词生成器</span></span></td></tr><tr><td data-colwidth="268" width="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">AI医疗助手-AI安全工坊</span><span style="display: none;line-height: 0px;"><span leaf="">‍</span></span></span></td></tr><tr><td data-colwidth="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">AI 智能体商业应用全景图</span></span></td></tr><tr><td data-colwidth="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">DeepSeek离线部署资源包</span></span></td></tr><tr><td data-colwidth="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">AIPOC</span></span></td></tr></tbody></table>- 免责声明  
  
   
  
  
  
  
