#  利用 Ivanti EPMM 系统零日漏洞的攻击激增  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-02-12 01:03  
  
**导****读**  
  
  
  
针对Ivanti Endpoint Manager Mobile (EPMM)中的一个严重漏洞 CVE-2026-1281 的攻击尝试出现了前所未有的激增。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PaFY6wibdwyJYRmKWXZ4lzgbtuuok4mMIYiaFkRcs1vd0xhcAtFbu4WuHalhiaRhISUwf4icJFEWD60nnaDWfhIJ2bQR5zZ567OiaMOhs8aIv7ibc/640?wx_fmt=png&from=appmsg "")  
  
  
2026 年 2 月 9 日，Shadowserver 扫描显示，超过 28,300 个不同的源 IP 地址试图利用该漏洞，这标志着今年针对企业移动管理基础设施观察到的最大规模的协同攻击活动之一。  
  
  
CVE-2026-1281 是一个预身份验证代码注入漏洞， CVSS 评分为 9.8，攻击者可以利用该漏洞在易受攻击的 EPMM 实例上实现未经身份验证的远程代码执行。  
  
  
该漏洞源于端点 Bash 处理程序中输入清理不当/mifs/c/appstore/fob/，使得攻击者能够通过 URL 参数注入恶意有效载荷，并以 Web 服务器用户身份执行任意命令。  
  
  
对攻击基础设施的分析显示，攻击的地理分布高度集中，其中美国约占 20,400 个 IP 地址，占所有观察到的攻击源的 72%。  
  
  
英国以3800个源IP地址位居第二，俄罗斯紧随其后，有1900个地址。此外，伊拉克、西班牙、波兰、法国、意大利、德国和乌克兰的网络也发起了显著的攻击活动，但数量远低于英国。  
  
  
GreyNoise 和 Defused 的安全研究人员发现，此次攻击浪潮中存在一个复杂的组成部分：一个疑似初始访问代理一直在被入侵的 EPMM 实例上部署“休眠”webshel  
  
l。  
  
  
超过 80% 的攻击活动都可追溯到运行在防弹托管基础设施后面的单个 IP 地址，这表明这是一项高度协调的行动，旨在建立持久访问权限，以便其他威胁行为者进行后续攻击。  
  
  
这种延迟激活方法与典型的机会主义攻击有很大不同，因为后门会一直处于休眠状态，直到为特定操作激活为止。  
  
  
鉴于 EPMM 管理企业环境中的移动设备、应用程序和内容，成功利用该漏洞将使攻击者能够对企业移动基础设施进行广泛的控制，包括向受管设备部署额外的有效载荷，以及在目标网络中进行横向移动。  
  
  
Ivanti 于 2026 年 1 月 29 日首次披露了CVE-2026-1281和CVE-2026-1340，承认针对客户环境的有限实际利用。  
  
  
美国网络安全和基础设施安全局 (CISA) 立即将 CVE-2026-1281 添加到其已知利用漏洞目录中，并史无前例地设定了三天的补救期限，凸显了该威胁的严重性。  
  
  
Shadowserver 基金会正通过其蜜罐 HTTP 扫描器事件报告系统积极共享攻击者 IP 数据，其中 vulnerability_id 已过滤为 CVE-2026-1281。  
  
  
各组织机构可通过 shadowserver.org 获取此威胁情报，以识别并阻止试图利用其基础设施的恶意源地址。Ivanti 已针对受影响的版本发布了临时 RPM 补丁，永久修复程序计划于 2026 年第一季度在 12.8.0.0 版本中发布。  
  
  
管理 EPMM 部署的安全团队应立即应用可用的补丁，监控入侵指标（包括意外的 webshel  
  
l 工件），并审查访问日志，以查找对易受攻击端点的可疑请求。  
  
  
S  
hadowserver安全公告：  
  
https://www.shadowserver.org/what-we-do/network-reporting/compromised-website-report/  
  
  
新闻链接：  
  
https://cybersecuritynews.com/ivanti-epmm-0-day-flaw-exploited/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
