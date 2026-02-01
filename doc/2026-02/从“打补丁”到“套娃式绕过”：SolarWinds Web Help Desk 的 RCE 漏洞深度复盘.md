#  从“打补丁”到“套娃式绕过”：SolarWinds Web Help Desk 的 RCE 漏洞深度复盘  
原创 Kit Chung
                    Kit Chung  安全圈动向   2026-02-01 02:17  
  
![](https://mmbiz.qpic.cn/mmbiz_png/cGfIHiaxhOA8Uiba2thHAFJ6eLcBhoWgchLYbpSAyDISxh7DOuSRPlk9LuoeBBESHJ8IFAqSvhhVXtOWsueduS7g/640?wx_fmt=png&from=appmsg "")  
  
如果你在 IT 圈混迹多年，提到 **SolarWinds**  
 这个名字，那是“如雷贯耳”。当年那场震动全球的供应链攻击还没被彻底淡忘，最近这家公司的 Web Help Desk (WHD) 又出大事了。  
  
作为一名天天和漏洞打交道的 IT 工程师，我太清楚这种收到“高危预警”的痛苦了。而这次，WHD 爆出的不仅仅是一个漏洞，而是成串的“王炸”。SolarWinds 刚刚发布的 2026.1 版本里，一口气修复了 4 个评分高达   
9.8  
 的超危漏洞。最离谱的是：**不需要任何登录凭证，黑客就能在你的服务器上执行任意代码（RCE）。**  
  
今天我们就来深度扒一扒，这几个漏洞到底是怎么回事，以及为什么 WHD 的补丁总是“打了一个又来一个”。  
## 一、 技术深挖：为什么这次漏洞这么“致命”？  
  
这次爆发的漏洞家族里，最值得我们关注的是 **CVE-2025-40551**  
 和 **CVE-2025-40553**  
。它们被称为“渗透者的梦想”，原因就在于其极高的稳定性和零门槛。  
### 1. 致命的“不安全反序列化”  
  
这两个漏洞的核心原理都是**不安全的反序列化（Untrusted Data Deserialization）**  
。在 Java 开发中，反序列化本来是把字节流转回对象的常规操作。但如果程序在“进货”时没检查清楚，黑客就可以构造一段“恶意数据包”。  
  
当 WHD 系统尝试解析这段数据时，就会触发隐藏在里面的恶意代码，直接在服务器主机上执行 OS 命令。**由于不需要身份验证（Unauthenticated）**  
，这意味着只要你的 WHD 端口暴露在公网上，黑客就像进了自家后花园一样。  
### 2. “AjaxProxy”：这个老地方又翻车了  
  
安全研究员 Sebree 发现，这次的重灾区还是在 AjaxProxy  
 功能模块。这已经不是它第一次出事了。黑客的攻击链路非常精巧：  
- **第一步：**  
 建立一个有效会话并提取关键 Key 值。  
  
- **第二步：**  
 创建一个特定的 LoginPref  
 组件。  
  
- **第三步：**  
 修改组件状态，强行开启文件上传等受限权限。  
  
- **第四步：**  
 利用 JSONRPC 桥接技术，在后台“偷梁换柱”生成恶意的 Java 对象。  
  
- **最后：**  
 触发这些对象，直接拿到系统 Shell。  
  
## 二、 让人无语的“补丁套娃”现象  
  
作为技术人员，我最想吐槽的是 SolarWinds 这一年多来的“补丁史”。如果你仔细观察近期的 CVE 列表，你会发现一个让人哭笑不得的“套娃”现象：  
> CVE-2024-28986 → 补丁被绕过 → CVE-2024-28988 → 补丁再被绕过 → CVE-2025-26399  
  
  
这种**“补丁绕过（Patch Bypass）”**  
的频繁发生，说明代码底层可能存在严重的逻辑坏账，或者是修补方案过于表面，没有从根源上重构认证逻辑。对于我们运维人员来说，这简直是没完没了的加班噩梦。  
## 三、 避坑指南：漏洞清单速查  
  
为了方便大家理解，我把这次 2026.1 版本修复的关键漏洞整理成了表格：  
<table><thead><tr><th style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;background-color: rgb(244, 244, 244);font-weight: bold;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">漏洞编号</span></span></section></th><th style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;background-color: rgb(244, 244, 244);font-weight: bold;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVSS 评分</span></span></section></th><th style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;background-color: rgb(244, 244, 244);font-weight: bold;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">漏洞类型</span></span></section></th><th style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;background-color: rgb(244, 244, 244);font-weight: bold;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">技术影响</span></span></section></th></tr></thead><tbody><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><strong style="color: rgb(211, 47, 47);"><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2025-40551/53</span></span></strong></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><strong style="color: rgb(211, 47, 47);"><span leaf=""><span textstyle="" style="font-size: 16px;">9.8</span></span></strong></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">不安全反序列化</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><strong style="color: rgb(211, 47, 47);"><span leaf=""><span textstyle="" style="font-size: 16px;">未授权 RCE，直接拿权限</span></span></strong></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><strong style="color: rgb(211, 47, 47);"><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2025-40552/54</span></span></strong></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><strong style="color: rgb(211, 47, 47);"><span leaf=""><span textstyle="" style="font-size: 16px;">9.8</span></span></strong></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">认证绕过</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><strong style="color: rgb(211, 47, 47);"><span leaf=""><span textstyle="" style="font-size: 16px;">跳过登录调用敏感方法</span></span></strong></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2025-40536</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">8.1</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">安全控制绕过</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">访问受限业务功能</span></span></section></td></tr><tr><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">CVE-2025-40537</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">7.5</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">硬编码凭据</span></span></section></td><td style="border: 1px solid rgb(221, 221, 221);padding: 12px;text-align: left;"><section><span leaf=""><span textstyle="" style="font-size: 16px;">通过 &#34;client&#34; 账户获取后台权限</span></span></section></td></tr></tbody></table>## 四、 总结与建议：别等被黑了才后悔  
  
CISA（美国网络安全局）已经多次把 WHD 的漏洞列入“已知被利用”名单了。这意味着黑客们已经手里攥着武器，满世界扫那些还没升级的“肉鸡”。  
  
**听我一句劝，赶紧落地以下三点：**  
  
1. **立刻升级：**  
 升级到 **WHD 2026.1**  
 或更高版本。这是目前唯一的解法，不要心存侥幸。  
  
2. **收缩暴露面：**  
 如果你的 Help Desk 不需要对外开放，赶紧把它缩到 VPN 后面，或者加一层严格的 ACL。别直接发布到公网。  
  
3. **深度审计：**  
 检查一下服务器日志中涉及 AjaxProxy  
 的请求，尤其是带有异常 JSONRPC 载荷的记录。  
  
技术人的尊严，往往就藏在这些细节的守护中。千万别让一个已知的漏洞，成了你职业生涯的“滑铁卢”。  
  
如果你觉得这篇文章对你有启发，欢迎**点赞、在看、转发**  
三连！  
  
**想了解更多 Java 反序列化防御实战？欢迎在评论区留言，我们下期深挖！**  
  
