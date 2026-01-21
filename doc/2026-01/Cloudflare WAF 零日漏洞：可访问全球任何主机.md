#  Cloudflare WAF 零日漏洞：可访问全球任何主机  
助力行业的
                    助力行业的  李白你好   2026-01-21 00:02  
  
## 前言  
  
**Cloudflare 的 Web 应用程序防火墙 (WAF) 中存在一个严重的零日漏洞，攻击者可以利用该漏洞绕过安全控制，并通过证书验证路径直接访问受保护的源服务器。**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpUbJRYmxCqhticTq3ezWNjib5FS97qqiaGJEMEyVeVjXIn6zJuia0asFj1g/640?wx_fmt=png&from=appmsg "")  
  
或者，当 .well-known 远远超出 WAF 的范围。几乎所有现代网站上都存在一个专为机器而非人类设计的 URL。它位于 /.well-known/acme-challenge/  
 下，在证书颁发期间的几秒钟内，一个机器人会访问它来检查你是否真正控制该域名。这个访问本应是平淡无奇的，一项例行无声的任务。但在这种情况下，这个安静的路径变得非常喧闹！  
  
这篇报告讲述了针对该证书路径的流量如何即使在应用程序的其他部分被客户规则阻止时也能到达 Cloudflare 背后的源站，为什么这很重要，我们如何谨慎证明这一点，以及问题现在如何修复。它是为想要细节的研究人员和需要大局而不需教科书的安全领导者撰写的。  
## ACME 的 60 秒入门  
  
ACME 是证书颁发机构验证域名控制的协议。在 HTTP-01 方法中，CA 期望你的站点在 /.well-known/acme-challenge/{token}  
 处提供一个一次性令牌。CA 会像其他任何客户端一样通过普通 HTTPS 获取该令牌；如果字节匹配，则颁发证书。意图是严格而最小化的：让机器人读取一个非常特定路径下的小文件，仅此而已。ACME 通道是为携带剪贴板的机器人准备的，而不是一群溜过守卫的人群。  
## 不符合的观察  
  
我们正在审查一组应用程序的访问态势，其中 WAF 配置为阻止全世界，只允许特定来源。在其他地方，WAF 完全按照其描述行事。但当我们将请求指向 /.well-known/acme-challenge/{token}  
 时，WAF 退到一边，源站用自己的声音回应。这个谁在说话的单一变化——Cloudflare 插页 vs. 源框架——就是线索。  
  
为了确保我们不是在追逐特定租户的错误配置，我们在 Cloudflare 后面启动了我们的受控演示主机，这些主机默认对正常流量阻塞：  
  
在普通路径下，你会遇到阻塞页面。将相同的请求指向 ACME 挑战路径，并使用任何真实令牌，你会得到源站生成的响应，通常是框架 404。即使没有头部，这种差异也是可见的：一个页面是 Cloudflare 的，另一个明显是应用程序的。  
## 我们信任的信号  
  
在演示主机上，我们使用小型、幂等的请求，并在令牌后附加一个无害的后缀（例如，在令牌后添加 **/ae**  
）来显示无需真实 ACME 文件即可出现该行为。在每种情况下，我们都在本应遇到 WAF 的地方收到了源站响应。  
  
以下是演示环境的代表性截图。第一张图片显示正常请求在 Cloudflare 的阻塞页面结束。第二张显示我们用于阻塞演示中 cf- 主机名的自定义规则。接下来的三张显示每个演示主机在请求针对 ACME 路径时返回源站生成的 404。  
#### 阻塞页面（正常请求）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpVIbCsJ4ukPs1GqGTqKbn0qOVhvT4zFf0LCvibLahHA6VMze2UItha0Q/640?wx_fmt=png&from=appmsg "")  
#### 自定义规则 - 阻塞 cf-* 主机名  
  
在演示中，我们创建了一个规则，阻塞任何包含 cf- 的主机名。在生产环境中，许多团队阻塞公共互联网，只允许公司 VPN 出口。此规则模拟了演示的态势。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicppuTWgfuuXx3PT2jQk75Mp5dCjiaHDPdsESbvStgBN8e4VCZzJxCia8xA/640?wx_fmt=png&from=appmsg "")  
#### 源站 404 (Next.js)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicp1kZJ8B6pkAzu4uKPdmtiaegibxW4vReRezT97TL8xc0iaGaBUzkiavwmOg/640?wx_fmt=png&from=appmsg "")  
#### 源站 404 (Spring)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpr52rhQDXw1qbmmRdQleVFqV1lNldfLic13smeSomicy4xRf3WM5bUAkQ/640?wx_fmt=png&from=appmsg "")  
#### 源站 404 (PHP)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpfzH8OxZHCG16Qx4Tbo6Mxcr1BLyuiaJibjZU4YC3h4l8A8wXmNj6oQjg/640?wx_fmt=png&from=appmsg "")  
## 我们如何获得稳定的挑战令牌  
  
为了可重复的演示，我们想要一个不会在中途消失的挑战令牌。Cloudflare 的 SSL/TLS 自定义主机名功能允许你管理 CNAME 到你的域名的第三方主机名和证书。我们添加了一个名为 cf-well-known.fearsoff.org  
 的自定义主机名，并明确选择了 HTTP 验证。下面的截图显示了添加流程和结果的待验证状态。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpekL0Fc4ic9OnhCYIjqRz7cKRVgKU0ILLibjyIeicdSb6kVYjlyENsn1aA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpZjTY9qEKrvUC3fdYqicaLZ8zOuUyMahY72ywClTDmiaJfv6a4ibKCUkcw/640?wx_fmt=png&from=appmsg "")  
  
我们故意没有为 cf-well-known.fearsoff.org  
 创建 DNS 记录，因此颁发保持无限期挂起。在挂起状态下，Cloudflare 会显示验证机器人最终会请求的 HTTP-01 URL，例如：  
  
http://cf-well-known.fearsoff.org/.well-known/acme-challenge/yMnWOcR2yv0yW-...Jm5QksreNRDUmqKfKPTk  
  
我们没有完成验证，也没有在该路径放置任何挑战文件。目标是为我们的 WAF 行为测试锚定一个确定的、长寿命的令牌形状，而无需与真实 CA 竞争。有了令牌，我们可以在全球所有 Cloudflare 主机上行使 /.well-known/acme-challenge/{token}  
 路由。  
## 为什么这在实践中重要  
  
WAF 控制旨在成为前门。当单个维护路径绕过该门时，“内部”的定义就会移动。在实际意义上，/.well-known/acme-challenge/...  
 的信任边界从 WAF 滑向源站。一旦源站从互联网可寻址——即使只有一个路由——普通 bug 就会获得网络路径，普通页面就会成为侦察。  
  
以下是我们演示中这种转变的样子。  
#### Spring / Tomcat  
  
在正常态势下，actuator 端点位于 WAF 和内部网络控制后面。通过 ACME 路径到达应用程序改变了该边界。使用某些 servlet 栈中著名的遍历 quirk ( **..;/**  
 )，请求可以落在 **/actuator/env**  
 上并返回进程环境和配置。这些数据通常包括敏感值——数据库 URL、API 令牌、云密钥——它实质上提高了源站中任何错误的爆炸半径。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicprASt7cOP9TLWaxEMZPocGRhBZZDVpr4kL2FVIrDyLZhXekYFx5ibg1g/640?wx_fmt=jpeg&from=appmsg "")  
  
服务器端渲染框架通常将服务器派生的值发送到客户端以水合页面。当 WAF 拥有前门时，这是没问题的。当源站直接响应时，同一页面可以暴露从未打算从公共互联网可达的操作细节。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpezfUSBAecIJU1IDBI7zwl3y7OVjbMyOXSaOE58WWdTZteUXH2dzoeA/640?wx_fmt=jpeg&from=appmsg "")  
#### PHP 路由  
  
许多 PHP 应用程序通过 **index.php**  
 路由所有请求，并使用查询参数选择视图。当该模式携带 LFI bug 时，公共可达性会将其转化为文件读取。请求 **../../../../etc/hosts**  
 就足以证明影响。在我们的演示中，即使是 404 流程也通过 **index.php**  
 路由，这就是为什么一旦源站开始直接说话，它就会暴露额外页面。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpy6byQkcricsicIcE7U1icDa7WJpQoicKicYxj1boKzXQEGPgJYT4H2u84xA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpCdbt628kCicUrAnyJycyvf4L2Adq647Fic4Tlu21icHdI7zmyp0rYrLVw/640?wx_fmt=png&from=appmsg "")  
  
这些演示是后果，而不是原因。根问题是特殊路径上的 WAF 决策。一旦门打开，源站内任何脆弱的东西突然就只需一个请求。  
## 不只是 404s - 账户 WAF 规则被忽略  
  
为了证明这不仅仅是绕道到框架 404，我们配置了账户级 WAF 规则来阻塞携带哨兵头部的请求。在根路径下，带有 **X-middleware-subrequest:**  
 的请求如预期被阻塞。针对 ACME 路径的相同请求被允许并由应用程序服务。换句话说，本应停止请求的账户规则对于该路径未被评估。  
  
为什么这个区别重要？许多真实应用程序基于头部做出决策，或将头部值传递到下游代码中。当检查头部的 WAF 规则被跳过时，整个类问题重新获得通往源站的路由：遗留代码中的头部驱动 SQL 连接、通过 **X-Forwarded-Host**  
 或 **X-Original-URL**  
 的 SSRF 和主机混淆、当缓存基于头部变化时的缓存键中毒、使用 **X-HTTP-Method-Override**  
 的方法覆盖技巧，以及连接到自定义头部的调试切换。显而易见的问题随之而来——有多少应用程序仍然比他们应该的更信任头部，有多少依赖 WAF 站在这种信任和互联网之间？  
## 可能发生什么以及修复  
  
我们在调查期间的工作假设是 **/.well-known/acme-challenge/**  
 下的请求在不同的代码路径上被评估——一个隐式例外，旨在帮助证书验证，在客户阻塞控制之前执行。这将解释 ACME 路径下的一致源站响应和其他地方的阻塞页面。  
  
2025 年 10 月 27 日，Cloudflare 部署了修复。我们重新测试了相同的模式，并观察到预期的行为：WAF 统一应用客户规则，包括在 **/.well-known/acme-challenge/**  
 上。无聊的路径再次变得无聊。  
## AI 和新攻击面  
  
像这种 WAF 绕过漏洞在不断演变的 AI 驱动攻击中变得更加紧迫。由机器学习驱动的自动化工具可以快速枚举和利用暴露的路径，如 /.well-known/acme-challenge/  
 ，大规模探测框架特定弱点或错误配置。  
  
例如，一个训练用于识别 servlet 遍历 quirk 或 PHP 路由 bug 的 AI 模型可以将此绕过与针对性负载链起来，将狭窄的维护路径转化为广泛的攻击向量。相反，AI 驱动的安全工具可以通过模拟这些攻击场景来帮助防御者，正如我们在与 Crypto[.]com 安全团队的合作中看到的，他们使用 AI 分析来验证问题。随着源站变得直接可寻址，AI 攻击者和防御者之间的竞赛加剧，使得稳健的 WAF 控制比以往更重要。  
## 时间线  
- 2025 年 10 月 9 日 - 通过 HackerOne 提交。  
  
- 2025 年 10 月 13 日 - 供应商验证开始。  
  
- 2025 年 10 月 14 日 - HackerOne 分诊。  
  
- 2025 年 10 月 27 日 - 最终修复部署；重新测试确认已修复。  
  
## 结语  
  
最危险的 bug 往往从例行细节开始。证书机器人的通道绝不应成为侧门。  
  
参考链接：https://fearsoff.org/research/cloudflare-acme  
## 网络安全情报攻防站  
  
**www.libaisec.com**  
  
综合性的技术交流与资源共享社区  
  
专注于红蓝对抗、攻防渗透、威胁情报、数据泄露  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUD0LPDib71VXU5N7sUkSnOicpYXERCGjDZUmdUumAsoGPeFAaNkHsNWNJ8CicXwAib87E7Bz6Y2ksial5w/640?wx_fmt=png&from=appmsg "")  
  
  
