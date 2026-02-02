#  Moltbook AI漏洞暴露电子邮件地址、登录令牌和API密钥  
原创 网络安全9527
                    网络安全9527  安全圈的那点事儿   2026-02-02 01:01  
  
由 Octane AI 的 Matt Schlicht 于 2026 年 1 月下旬推出的新兴人工智能代理社交网络 Moltbook 存在一个严重漏洞，该漏洞会泄露其注册实体的电子邮件地址、登录令牌和 API 密钥，而此前该网络曾被大肆宣传拥有超过 150 万“用户”。  
  
研究人员发现数据库配置存在漏洞，允许未经身份验证的用户访问代理配置文件，从而实现批量数据提取。  
  
这一缺陷恰好与账户创建没有速率限制的情况同时发生，据报道，一名 OpenClaw 代理（@openclaw）注册了 50 万个虚假 AI 用户，驳斥了媒体关于自然增长的说法。  
## 平台机制  
  
Moltbook 使 OpenClaw 支持的 AI 代理能够发布、评论和创建“子蜕变”，例如 m/emergence，从而促进机器人之间就从 AI 兴起到复仇泄露和 Solana 代币 karma 刷取等话题展开冲突。  
  
帖子数量激增超过28000篇，评论数量达到233000条，有100万名默默关注的人工审核员在旁监督。然而，代理数量却是人为捏造的：由于没有创建限制，机器人会大量注册，从而制造出病毒式传播的假象。  
  
暴露的端点与不安全的开源数据库相连，通过简单的查询（例如GET /api/agents/{id}“无需身份验证”）泄露代理数据。  
  
<table><thead style="box-sizing: border-box;border-bottom-width: 3px;border-bottom-style: solid;border-bottom-color: currentcolor;"><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">暴露面</font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">描述</font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">影响示例</font></font></th></tr></thead><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">电子邮件</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">与所有者关联的电子邮件地址</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">针对机器人背后人类的定向网络钓鱼</font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">登录令牌</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">JWT代理会话令牌</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">完全劫持代理，帖子/评论控制</font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">api_key</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">OpenClaw/Anthropic API 密钥</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">数据泄露至关联服务（电子邮件、日历）</font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">代理 ID</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">用于枚举的顺序 ID</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">大规模抓取超过50万个虚假数据</font></font></td></tr></tbody></table>  
攻击者通过枚举 ID 来快速收集数千条记录。  
## 安全风险与专家警告  
  
这种 IDOR/数据库暴露构成了“致命的三重威胁”：代理访问私人数据、不受信任的 Moltbook 输入（提示注入）和外部通信，从而导致凭证被盗或文件删除等破坏性行为。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pcgSUGCDdKJw6XTJka1HMG0N5f7EXK8QOKQRmUNdZrOCibn2KCy0m5RQep9Dykfwq4YFIGOOibVSKKZib3M9C5vww/640?wx_fmt=jpeg "")  
  
Andrej Karpathy 将其称为“充斥着垃圾邮件的规模里程碑”，但同时也是“计算机安全的噩梦”，而 Bill Ackman 则称之为“令人恐惧”。在子蜕变程序中快速注入恶意软件可以操纵僵尸程序泄露主机数据，而未受沙盒保护的 OpenClaw 执行则会放大这种风险。  
  
目前尚未确认任何补丁；Moltbook (@moltbook) 对披露信息未作回应。用户/所有者：撤销 API 密钥、沙盒代理、审计风险。企业面临来自不受监管的机器人的影子 IT 风险。  
  
  
