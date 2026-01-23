#  “尽情享受您的管理员权限”：SmarterMail 关键远程代码执行漏洞在野外被利用  
sec随谈
                    sec随谈  sec随谈   2026-01-23 01:16  
  
就在SmarterMail 生态系统遭遇重大漏洞冲击几周后，安全研究人员又发现了一个新的严重漏洞，该漏洞已被攻击者利用。watchTowr Labs 的研究人员 Piotr Bazydlo 和 Sina Kheirkhah 披露了 WT-2026-0001 的详细信息，这是一个身份验证绕过漏洞，允许未经身份验证的攻击者劫持管理员帐户并实现完全远程代码执行 (RCE)。  
  
这一发现紧随此前一起远程电荷交换事件之后。正如研究人员略带讽刺地指出，这种情况的“时间线通常只有KEV名人堂成员才会遇到”。  
  
该漏洞存在于 SmarterMail Web 界面的强制重置密码 API 端点中。该功能旨在用于合法的密码恢复，但未能对系统管理员实施基本的安全检查。  
  
报告指出，该端点被标记为允许匿名访问，这在重置流程中属于标准做法。然而，关键故障发生在处理管理员请求的逻辑中。“这里没有任何安全控制措施。没有身份验证。没有授权。也没有对旧密码进行验证。”  
  
攻击者只需发送一个 JSON 请求，并将 IsSysAdmin 设置为 true，同时传入目标用户名和新密码。系统随后会覆盖管理员的凭据，而不会验证旧密码——讽刺的是，这一步骤对普通用户却是强制执行的。  
  
研究人员证实： “这完全绕过了系统管理员帐户的身份验证。尽情享受您的管理员权限吧！”  
  
该报告强调，威胁行为者正在积极利用这一漏洞来控制电子邮件服务器。  
  
watchTowr收到一位匿名读者的举报，称其日志显示，在厂商发布补丁几天后，系统出现了可疑活动。“确凿证据？日志表明，漏洞利用发生在补丁发布两天后。”  
  
提供的日志揭示了一种有效的攻击模式：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaYUeYwA2bzjkgC4N56kzliam1zBibfVRUtQSAmaJLJBBvJZQ5n4hzaDib7Dk2Iq4ytR7hPNIV1qQbHp3TabVctxBg/640?wx_fmt=png&from=appmsg "")  
- 10:51:58：攻击者以管理员身份成功登录。  
- 10:52:00：攻击者创建恶意事件。  
- 10:52:04：攻击者创建了域名 google.abc.com。  
- 11:49:02：日志条目“用户 @ 成功强制重置密码”出现，研究人员将其确定为“WT-2026-0001 中涉及的确切端点”。  
访问管理面板只是第一步。SmarterMail 包含一个“卷挂载”功能，允许管理员映射存储驱动器。然而，对于拥有管理员权限的用户来说，此功能实际上相当于一个内置的后门。  
  
报告解释说：“SmarterMail 公开了内置功能，允许系统管理员执行操作系统命令。”  
  
攻击者通过创建一个新卷并在“卷挂载命令”字段中提供任意命令（例如 cmd.exe /c calc），即可触发底层操作系统立即执行该命令。“在我们的概念验证中，这会导致目标主机上出现系统级 shell。”  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaYUeYwA2bzjkgC4N56kzliam1zBibfVRUtOAo1lh5Vr2gvNZnXSoMfPHbDW3wGGkibXRWseWqHu6qWBrzQ0Nge0og/640?wx_fmt=png&from=appmsg "")  
  
SmarterTools 于 2026 年 1 月 15 日发布了 Build 9511 版本，以修复此漏洞。该补丁增加了一个验证步骤，在允许重置密码之前会检查用户的旧密码。  
  
参考链接：  
  
https://labs.watchtowr.com/attackers-with-decompilers-strike-again-smartertools-smartermail-wt-2026-0001-auth-bypass/  
  
