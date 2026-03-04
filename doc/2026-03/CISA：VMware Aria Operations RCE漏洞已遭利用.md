#  CISA：VMware Aria Operations RCE漏洞已遭利用  
Lawrence Abrams
                    Lawrence Abrams  代码卫士   2026-03-04 10:30  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**美国网络安全和基础设施安全局 (CISA) 将 VMware Aria Operations 漏洞CVE-2026-22719纳入“已知遭利用漏洞 (KEV)” 分类表中，表明该漏洞已遭利用。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
博通公司也提醒称，已获悉表明该漏洞已被利用的报告，但表示无法独立证实这些说法。VMware Aria Operations是一款企业监控平台，可帮助组织机构跟踪服务器、网络和云基础设施的性能和运行状况。  
  
该漏洞最初于2026年2月24日作为VMware安全公告VMSA-2026-0001的一部分被披露并修复，评级为"重要"，CVSS评分为8.1。该漏洞已被 CISA 纳入 KEV 必修单，并要求联邦民事机构在2026年3月24日前修复该问题。  
  
博通公司在最近对安全公告的更新中表示，已获悉表明该漏洞已在攻击中被利用的报告，但无法证实这些说法。更新后的公告指出："博通公司已获悉关于CVE-2026-22719可能被野外利用的报告，但我们无法独立确认其有效性。"  
  
目前，关于该漏洞可能如何被利用的技术细节尚未公开披露。博通公司并未就报告的利用活动问询做出回复。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWoribN7MrhXhiaaeDFnibu5uk5G2uX4Lkd0uqvH0HbFmZPDqdj845baZDx5qTPF3vnyW0icOhOuvk4F0GpbibdEPxoicRhKsDY4yKqY/640?wx_fmt=gif&from=appmsg "")  
  
**命令注入漏洞**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfW4ZRhic2QrxDiagpXtEGe9PYyDWG0BjibH5bJxG5FJQmjS8UjLW5oNqjkpmFgYIoErjhoiaSibrqIicm9mGM4PBGxvicsAD6pxgAtu8M/640?wx_fmt=gif&from=appmsg "")  
  
  
  
据博通公司称，CVE-2026-22719是一个命令注入漏洞，允许未经身份验证的攻击者在易受攻击的系统上执行任意命令。  
  
该公告解释道："在支持辅助的产品迁移过程中，未经认证的恶意攻击者可能利用此问题执行任意命令，从而导致VMware Aria Operations中的远程代码执行。" 博通公司已于2月24日发布安全补丁，并为无法立即应用补丁的组织机构提供了临时解决方案。  
  
该缓解措施是一个名为"aria-ops-rce-workaround.sh"的shell脚本，必须在每个Aria Operations设备节点上以root权限执行。该脚本会禁用迁移过程中可能在漏洞利用时被滥用的组件，包括删除 “/usr/lib/vmware-casa/migration/vmware-casa-migration-service.sh”以及允许vmware-casa-workflow.sh以root权限无密码运行的以下sudoers条目：  
```
NOPASSWD: /usr/lib/vmware-casa/bin/vmware-casa-workflow.sh
```  
  
建议管理员尽快应用可用的VMware Aria Operations安全补丁或实施缓解措施，尤其是在该漏洞正在被积极利用于攻击的情况下。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[Vmware 修复 Pwn2Own 柏林大赛上遭利用的四个 ESXi 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523602&idx=1&sn=3ec9fd59b332276a13eb21d88cdd9217&scene=21#wechat_redirect)  
  
  
[VMware 紧急修复多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523082&idx=1&sn=1ddbeb4f3e454706eafa9900777eed09&scene=21#wechat_redirect)  
  
  
[博通：注意 Vmware Windows Tools 中的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522590&idx=1&sn=ee578730b1733ca26a369770366c3b00&scene=21#wechat_redirect)  
  
  
[博通修复3个已遭利用的 VMware 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522410&idx=1&sn=0f5b704ab0b14c7dd3262ffbc0697b07&scene=21#wechat_redirect)  
  
  
[VMware 修复 Aria Operations 中的多个高危漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521645&idx=2&sn=3a85491541969226b45d2bca18f4373b&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.bleepingcomputer.com/news/security/cisa-flags-vmware-aria-operations-rce-flaw-as-exploited-in-attacks/  
  
  
题图：Pixa  
bay Licens  
e  
  
  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg "")  
  
**奇安信代码卫士 (codesafe)**  
  
国内首个专注于软件开发安全的产品线。  
  
   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif "")  
  
   
觉得不错，就点个 “  
在看  
” 或 "  
赞  
” 吧~  
  
