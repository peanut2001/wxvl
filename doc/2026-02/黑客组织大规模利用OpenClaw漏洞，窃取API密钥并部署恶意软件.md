#  黑客组织大规模利用OpenClaw漏洞，窃取API密钥并部署恶意软件  
 黑白之道   2026-02-24 01:18  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MgKsBqQMyRyuv1ruAEQ2MjnfibbJliaNZria9FIEANS4b5wRPBuUq4Kv6GfX1xiakGG2aE9PdXX8ubWcpKBt3rIZt4wh7jzlvkQ5M/640?wx_fmt=png&from=appmsg "")  
  
**Part01**  
## OpenClaw遭大规模利用  
  
  
多个黑客组织正在广泛利用OpenClaw（前身为MoltBot和ClawdBot）部署恶意载荷。这款由Peter Steinberger开发的开源自研AI框架（现开发者已加入OpenAI），在2026年1月下旬病毒式传播后已成为高危攻击目标。  
  
  
该架构赋予系统高级权限、持久内存访问能力以及与敏感服务的集成能力，使其成为凭证窃取和数据外泄的绝佳目标。在大规模部署72小时内，威胁分子就开始利用多个严重漏洞，包括高危远程代码执行漏洞（CVE-2026-25253）、供应链投毒以及通过暴露的管理界面窃取凭证。  
  
  
Flare分析师已发现超过3万个遭入侵的OpenClaw实例被用于窃取API密钥、拦截消息，并通过Telegram等恶意通信渠道传播信息窃取型恶意软件。  
  
  
**Part02**  
## ClawHavoc攻击行动：  
## 供应链大规模感染  
  
  
2026年1月29日检测到代号"ClawHavoc"的早期破坏性攻击行动。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0CiaXyicR0LicoPcnBfGc2xdAYe28iaDOIOKicb4ibgXURLwQXWn9A9icBQMJXWl0bxasuhFoPkliasUohIoVBzyfBVMHe16IBAjYukkY/640?wx_fmt=jpeg&from=appmsg "")  
  
  
该供应链攻击将Atomic Stealer（针对macOS）和键盘记录器（针对Windows）等恶意载荷伪装成合法加密工具。用户通过所谓的"安装"脚本无意中下载了窃密软件，导致攻击者能提取持久内存数据并在企业系统内横向移动。  
  
  
2月初，第二个攻击行动"通过ClawHub实施自动化技能投毒"出现在OpenClaw社区市场。由于平台采用开放发布模式且缺乏代码审查，攻击者从看似可信的GitHub账户（如Hightower6eu）上传带有后门的"技能"。这些恶意更新会执行远程shell命令，使攻击者能实时窃取OAuth令牌、密码和API密钥。  
  
  
2026年2月18日的Shodan扫描显示，超过31.2万个OpenClaw实例运行在默认端口18789上，其中许多未启用身份验证且直接暴露在互联网中。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0fgkp1Wv7bA8GKKSPX5D9Mbnia4qWUNGxHnOOHnibjeqK5KjFxsUicK23CH4ibxJsvsGr0Fj7BsiadUwEqKRlugbagCFFYlichU9nnk/640?wx_fmt=jpeg&from=appmsg "")  
  
  
与此同时，暴露的管理界面加剧了危机。蜜罐部署记录显示，系统在暴露几分钟内就会遭到攻击尝试。OpenClaw事件标志着自研AI Agent安全性的关键转折点——有组织的威胁团体快速适应环境，将优先考虑功能而非网络安全的生态系统武器化。  
  
  
随着OpenAI吸纳OpenClaw的开发者，专家警告这些事件凸显了在未来AI框架中采用"安全设计"方法的紧迫性。Flare建议使用或测试自主助理的企业保护好API凭证并隔离AI工作负载。  
  
  
**参考来源：**  
  
Multiple Hacking Groups Exploit OpenClaw Instances to Steal API key and Deploy Malware  
  
https://cybersecuritynews.com/hacking-groups-exploit-openclaw/  
  
  
> **文章来源 ：FreeBuf**  
  
  
**精彩推荐**  
  
  
  
  
# 乘风破浪|华盟信安线下网络安全就业班招生中！  
  
  
[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650575781&idx=2&sn=ea0334807d87faa0c2b30770b0fa710d&chksm=83bdf641b4ca7f5774129396e8e916645b7aa7e2e2744984d724ca0019e913b491107e1d6e29&scene=21#wechat_redirect)  
  
  
# 【Web精英班·开班】HW加油站，快来充电！  
  
  
‍[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650594891&idx=1&sn=b2c5659bb6bce6703f282e8acce3d7cb&chksm=83bdbbafb4ca32b9044716aec713576156968a5753fd3a3d6913951a8e2a7e968715adea1ddc&scene=21#wechat_redirect)  
  
  
‍  
# 始于猎艳，终于诈骗！带你了解“约炮”APP  
  
[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650575222&idx=1&sn=ce9ab9d633804f2a0862f1771172c26a&chksm=83bdf492b4ca7d843d508982b4550e289055c3181708d9f02bf3c797821cc1d0d8652a0d5535&scene=21#wechat_redirect)  
  
**‍**  
  
  
