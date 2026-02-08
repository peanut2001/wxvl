#  EPSS深度解析：如何利用漏洞预测评分系统优化现代漏洞管理  
 极客零零七   2026-02-07 23:31  
  
漏洞利用预测评分系统（Exploit Prediction Scoring System, EPSS）是由事件响应与安全团队论坛（FIRST）管理的一种数据驱动框架，旨在解决现代漏洞管理中面临的“优先级危机”。随着每年新披露的通用漏洞披露（CVE）数量激增（2024 年约 4 万个），传统的基于严重性（如 CVSS）的防御策略已难以为继。  
  
核心观察：  
  
• 范式转移： EPSS 将关注点从“理论严重性”转向“现实利用可能性”，提供漏洞在未来 30 天内被在野利用的概率评分（0 到 1）。  
  
• 资源优化： 研究表明，仅修复 CVSS 高分漏洞效率极低。通过集成 EPSS，组织可将紧急修复的工作量减少约 95%，同时维持 85% 以上的在野利用覆盖率。  
  
• 数据驱动： 该系统利用机器学习（XGBoost）分析包括 CVE 元数据、利用代码库（GitHub/Metasploit）及实时攻击遥测在内的 1100 多个变量。  
  
• 协同效应： EPSS 并非 CVSS 的替代品，而是互补工具。CVSS 衡量“如果被利用会有多糟”，而 EPSS 衡量“被利用的可能性有多大”。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg "")  
  
01  
  
EPSS 核心机制与架构  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg "")  
  
  
  
1.1 定义与目标  
  
EPSS 是一个开放的、由社区驱动的项目，旨在通过估算软件漏洞在野外被利用的可能性，协助安全团队优化修复优先级。  
  
1.2 评分指标  
  
EPSS 为每个已发布的 CVE 分配两个关键数值：  
  
• 概率（Probability）： 范围 [0, 1]（或 0-100%），表示漏洞在未来 30 天内被利用的估算概率。  
  
• 百分位数（Percentile）： 表示当前 CVE 评分相对于所有已评分漏洞的排名，比例越高意味着该漏洞比更多漏洞更具威胁。  
  
1.3 数据来源与模型更新  
  
EPSS 模型（如最新的 v4.0 版本）基于超过 1100 个变量进行训练，主要数据源包括：  
  
• 漏洞特征： MITRE 的 CVE 列表、NVD 的 CVSS 向量、漏洞年龄、引用数量。  
  
• 利用情报： Metasploit、ExploitDB 及 GitHub 中的公开利用代码。  
  
• 扫描器数据： Jaeles、Nuclei、Sn1per 等安全扫描器的检测特征。  
  
• 实时观察（基准真相）： 来自 Fortinet、AlienVault 等合作伙伴的在野攻击实时观测数据。  
  
EPSS 评分每日更新，以反映不断变化的威胁景观。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg "")  
  
02  
  
EPSS与CVSS 的协同应用  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg "")  
  
  
  
长期以来，业界依赖 CVSS（通用漏洞评分系统）进行优先级排序，但 CVSS 存在无法反映现实利用情况的局限性。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L7VicJKsiaibFCqpnxHj5BM98REwjykNgicjRYnlLN89xsWkDpZ9S4ek9BG7MUjNOIibd7zRInuVibFZsW0FfS5nniac7Y4vrNAsOQichgVwanK4hiak/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
  
2.1 优先级矩阵（四象限策略）  
  
结合 CVSS 和 EPSS，安全团队可以将漏洞划分为四个优先级象限：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L7VicJKsiaibFC0XlYI84Lyz5mwvFbpTphVrdFjVN1Cgr9SAu10Ht29LFJRYKweSXPX3lKxNDSu0icx4OaFVhwibBXFsbr8Cru7Beia9TZOiastfL4/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
1. 高 EPSS / 高 CVSS（右上）： 最危急。极可能被利用且影响巨大，必须立即修复。  
  
1. 高 EPSS / 低 CVSS（左上）： 虽然单个漏洞影响有限，但极可能被利用（或用于链式攻击），应优先考虑。  
  
1. 低 EPSS / 高 CVSS（右下）： 理论影响大但现实威胁低。应持续监控，一旦利用概率上升则提升优先级。  
  
1. 低 EPSS / 低 CVSS（左下）： 低优先级。可推迟修复或仅按标准补丁周期处理。  
  
![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg "")  
  
03  
  
漏洞管理链  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg "")  
  
  
  
为了进一步提升效率，研究提出了一种集成 CISA 已知利用漏洞（KEV）目录、EPSS 和 CVSS 的决策树框架。  
  
3.1 决策逻辑  
1. 威胁过滤（第一阶段）： 检查漏洞是否在 CISA KEV 目录中，或者其 EPSS 评分是否 ≥ 0.088。  
  
1. 严重性评估（第二阶段）： 对通过第一阶段的漏洞，检查其 CVSS 是否 ≥ 7.0。  
  
1. 优先级分配：  
  
• 紧急（Critical）： 存在于 KEV 且 CVSS ≥ 7.0。  
  
• 高（High）： EPSS ≥ 0.088 且 CVSS ≥ 7.0。  
  
• 监控（Monitor）： 存在利用证据但 CVSS < 7.0。  
  
• 延迟（Defer）： 无利用证据。  
  
3.2 效率与覆盖率对比  
  
• 效率（Efficiency）： 指修复的漏洞中确实存在在野利用的比例。  
  
• 覆盖率（Coverage）： 指成功捕获的在野利用漏洞占总利用漏洞的比例。  
  
研究数据显示，相比于仅修复 CVSS ≥ 7.0 的漏洞，集成策略在保持约 85% 覆盖率的同时，将效率提升了 14-18 倍。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg "")  
  
04  
  
实际应用与效益  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg "")  
  
  
  
4.1 组织工作量减轻  
  
• 减少疲劳： 一些研究表明，集成 EPSS 洞察可减少组织高达 80% 至 95% 的补丁工作量，使团队能够专注于真正重要的少数漏洞。  
  
• 资源优化： 企业每月通常只能修复 5%-20% 的漏洞，而 EPSS 能够精准定位那 2%-7% 真正会被利用的漏洞。  
  
4.2 国家政策与威胁评估  
  
• 优化合规要求： 美国 DHS 曾发布指令要求 30 天内修复所有高危漏洞。EPSS 证明这会浪费大量资源处理永不会被利用的漏洞。  
  
• 零日漏洞决策： 在漏洞公平程序（VEP）中，政府可利用 EPSS 客观评估保留或披露漏洞的防御性成本。  
  
4.3 企业级威胁扩展  
  
EPSS 可用于估算整个系统、子网或企业的总体威胁。基于事件独立性统计属性，一个拥有 100 个漏洞（每个利用概率为 5%）的组织，其至少有一个漏洞被利用的概率计算如下： P = 1 - (1 - 0.05)^100 = 99.4% 该指标可用于跨时间或跨部门比较安全态势。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg "")  
  
05  
  
真实世界利用特征分析  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg "")  
  
  
  
通过对实际利用数据的观察，发现以下模式：  
  
• 持续时间（Duration）： 有些漏洞仅被利用几天，而有些则长达数年。  
  
• 密度（Density）： 部分漏洞被高频连续利用，而另一些则存在长期的沉寂期。  
  
• 利用延迟（Delay）： 许多漏洞在公开披露后立即被利用，甚至在披露前（零日攻击）。  
  
• 共存利用（Co-exploitation）： 多个漏洞常在同一时间段被针对，暗示了攻击者常用的“漏洞链接”技术。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg "")  
  
06  
  
局限性与实施建议  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg "")  
  
  
  
6.1 系统局限性  
  
• 零日漏洞挑战： EPSS 依赖已公开的 CVE 及其元数据，因此无法预测未知的零日漏洞。  
  
• 数据依赖： 预测准确性取决于输入数据的质量，且可能无法反映特定环境下的缓解措施。  
  
• 排除业务影响： EPSS 本身不考虑受影响资产的业务价值（如支付系统 vs 开发服务器）。  
  
6.2 实施建议  
  
• 设定动态阈值： 组织应根据自身的风险偏好设定阈值（如：高可能性为 0.7-1.0；中等为 0.4-0.69）。  
  
• 集成自动化工作流： 将 EPSS API 接入漏洞管理平台（如 ServiceNow、Tenable、Splunk），自动触发补丁任务。  
  
• 结合业务语境： 必须结合资产的关键性（Asset Criticality）和网络可达性（Exposure）进行决策。  
  
• 持续验证： 使用攻击路径验证或漏洞模拟（BAS）工具，确认高 EPSS 漏洞在特定环境下是否确实可被利用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Lgu1K9Ehrgdg03vhsFuCooliabwT2VLwDoLdb1YyuTC6rM4zY4w76KZdR22uszLbCLEL25nlicrbNUfuQiciaSJksw/640?from=appmsg "")  
  
  
“EPSS 标志着从反应式补丁到预测式防御的转变，使网络防御者能够用更少的资源修复更多可能产生实质威胁的漏洞。”  
  
  
  
往期推荐  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/bXjDV0BBFOoDHPpN1sRVsQ3whL0dDumUNIJCTT7g0a5ekH3n4pRhKk5z8ENHMtmZGVou7empyOBnNJSnjKtNrw/640?from=appmsg "")  
  
  
[黑客部落｜像黑客一样思考，向专家一样成长！](https://mp.weixin.qq.com/s?__biz=Mzk2NDgwNjA2NA==&mid=2247486068&idx=1&sn=82b6baff1058aa3b2ab68f20df6f35fb&scene=21#wechat_redirect)  
  
  
[NeuroSploit 架构分析：AI驱动的渗透测试框架](https://mp.weixin.qq.com/s?__biz=Mzk2NDgwNjA2NA==&mid=2247486044&idx=1&sn=3477b11f003798618f3922bad9072cd9&scene=21#wechat_redirect)  
  
  
[写好渗透测试报告的核心要点：内容篇（附报告模板）](https://mp.weixin.qq.com/s?__biz=Mzk2NDgwNjA2NA==&mid=2247485944&idx=1&sn=6b8d28a4833c0ecb124598fdc910f9dc&scene=21#wechat_redirect)  
  
  
[React2Shell：撕开现代前端安全幻象](https://mp.weixin.qq.com/s?__biz=Mzk2NDgwNjA2NA==&mid=2247485909&idx=1&sn=96d9acede41ecb231545f94cdf1f1110&scene=21#wechat_redirect)  
  
  
  
参考资料：  
  
https://www.first.org/epss/  
  
https://research.empiricalsecurity.com/research/introducing-epss-version-4  
  
https://arxiv.org/html/2506.01220v2  
  
