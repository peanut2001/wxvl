#  日均欺诈百万用户，DNS漏洞沦为恶意广告温床？  
 聚铭网络   2026-01-20 09:31  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/uaicMoGl6iaSz34icEtlMpNrZxACe3gTguJiahs3ias2D2kS6ozGicAjicWicluQ1LHzMVaFmAuGP4ibdB4nJY8Y1Dmxgcg/640?wx_fmt=gif "")  
  
**安全快讯**  
  
**2026年1月**  
  
**NEWS**  
  
”  
  
近期，Infoblox 研究人员揭露的全球恶意广告劫持DNS漏洞事件引发行业震动——利用 “坐以待毙”（Sitting Ducks）漏洞，攻击者认领被遗弃却仍保持DNS委派活跃的域名，构建起覆盖全球60余种语言、日均欺诈百万用户的恶意推送网络。Android Chrome用户沦为主要受害者，日均接收140条虚假金融通知、病毒警报等欺诈内容，南亚地区更是重灾区，孟加拉国、印度等四国占比达50%流量。这起事件不仅暴露了DNS管理的普遍短板，更揭示了当前网络安全防护中“流量可视性不足、异常识别滞后”的核心痛点。  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uaicMoGl6iaSyJm0IJAzpgnh5c5jib3maTOoItIyyMZXQvdf74s8x6O9sh8GocpQB7RO2gxqdHF9fxZUmH3FSvsfw/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
**一**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/uaicMoGl6iaSxvQlaztC5STr12IxTCYGadiaZQNpYvwkLOK7weibD2eNm8dIwdPk9ffUuuFnbq0M5ib9sJNgmuvHH6Q/640?wx_fmt=gif&from=appmsg "")  
  
**漏洞本质与攻击链路**  
  
  
这起攻击的核心漏洞“坐以待毙”，  
本质是域名所有者未及时清理休眠域名的DNS解析记录，导致攻击者可通过DNS提供商直接认领这些“被遗弃的数字资产”。其完整攻击链路清晰且隐蔽：  
- 域名劫持：攻击者筛选出原所有者放弃但DNS委派仍有效的域名，通过合法认领流程接管控制权；   
  
- 流量劫持：受害设备仍试图连接原恶意基础设施，流量被劫持至攻击者控制的服务器；   
  
- 恶意推送：向设备批量发送伪装成金融服务、名人丑闻、病毒警报的欺诈通知，诱导点击钓鱼链接；   
  
- 黑产变现：通过虚假流量刷量、广告联盟分成获利，即便点击率仅为六万分之一，仍持续规模化运营。  
  
值得警惕的是，攻击不仅针对普通用户，更牵连合法组织——若企业未能及时清理休眠域名的DNS记录，这些域名可能被攻击者利用，伪装成正规品牌实施诈骗，直接损害企业声誉。而传统防护手段因缺乏对DNS解析层的深度监测和全流量分析能力，往往难以发现这类“合法外衣下的恶意行为”。  
  
  
  
二  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/uaicMoGl6iaSxvQlaztC5STr12IxTCYGadiaZQNpYvwkLOK7weibD2eNm8dIwdPk9ffUuuFnbq0M5ib9sJNgmuvHH6Q/640?wx_fmt=gif&from=appmsg "")  
  
**传统手段为何难以应对DNS劫持攻击？**  
  
  
此次事件暴露出当前网络安全防护的四大核心短板，也成为黑产持续泛滥的关键原因：  
- DNS管理混乱：企业普遍忽视休眠域名的DNS解析清理，给攻击者留下可乘之机，且缺乏自动化监测手段发现异常域名认领行为；   
  
- 流量可视性不足：攻击流量混杂在正常网络请求中，每秒30MB的海量日志数据远超人工分析极限，传统工具难以精准识别恶意推送的流量特征；   
  
- 威胁识别滞后：攻击者频繁冒充正规金融机构、公众人物，恶意内容伪装性强，缺乏威胁情报联动的防护工具无法快速匹配欺诈特征；   
  
- 溯源能力薄弱：攻击覆盖全球多个地区，分布式部署的恶意基础设施使得攻击源头追溯难度极大，难以从根本上遏制攻击。  
  
三  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/uaicMoGl6iaSxvQlaztC5STr12IxTCYGadiaZQNpYvwkLOK7weibD2eNm8dIwdPk9ffUuuFnbq0M5ib9sJNgmuvHH6Q/640?wx_fmt=gif&from=appmsg "")  
  
**聚铭网络流量智能分析审计系统解决方案**  
  
  
面对隐蔽性强、波及范围广的 DNS 劫持攻击，  
聚铭网络流量智能分析审计系统（iNFA）全面采集并实时分析南北向与东西向流量，深度融合流量解析、行为建模与威胁检测能力，精准识别已知威胁，高效挖掘未知风险，并实现追踪溯源、快速拦截与闭环处置，全面保障企业信息系统安全高效运行。  
  
  
1、全流量采集+基线预警，筑牢第一道防线  
  
  
- 全协议流量采集：全面捕获DNS、HTTP/HTTPS、TCP/UDP等多协议流量，确保不遗漏任何与恶意域名的通信痕迹。   
  
- DNS状态监测：实时校验域名解析状态，自动识别休眠域名、过期域名的异常解析活动，及时告警可能被劫持的高风险域名。  
  
- 智能行为基线建模：基于海量历史数据，通过统计模型构建正常DNS解析基线，当出现“批量设备连接同一异常域名、解析频率突增”等偏离基线的行为时，立即触发告警。  
  
2、  
AI穿透+多维度分析，精准识别隐蔽恶意行为  
  
  
- DNS隐蔽通道检测：基于机器学习模型分析DNS请求的包长分布、域名熵值、响应负载等特征，精准识别DNS隧道等数据走私行为。  
  
- 加密流量深度解析：无需解密即可通过TLS握手特征、流量时序模式等维度建模，结合千万级恶意样本训练库，对Cobalt Strike 等恶意载荷的加密通信检测准确率达99.8%。   
  
- 违规外联与跨境行为监测：实时碰撞聚铭威胁情报库，快速识别恶意IP /域名、非法跨境VPN连接等行为，并通过TCP/UDP探测技术，发现内网设备违规联网行为，封堵“隐形跳板”。  
  
  
  
3、  
实时阻断+全链路溯源，实现威胁处置闭环  
  
  
- DNS实时阻断：在DNS解析阶段即比对恶意域名、钓鱼站点、C2服务器情报库，一旦命中立即丢弃响应包，切断终端与恶意服务器的连接，阻断成功率可达100%。  
  
- 全链路溯源取证：通过流量指纹、IP 画像、域名关联分析等技术，精准定位攻击源地理位置与基础设施分布，为执法与反制提供关键证据；同时完整留存会话日志与原始流量，满足等保2.0合规审计要求。  
  
- 动态策略优化：基于实时监测与处置反馈，自动更新防护规则，并生成可视化报表，直观呈现DNS异常分布、终端受攻态势等，助力企业持续加固安全体系。  
  
  
  
  
  
**结语**  
  
  
  
  
此次全球性恶意广告劫持事件再次敲响警钟：  
DNS 不仅是互联网的地址簿，更是安全的第一道闸门。正如研究人员所言，  
遗弃的DNS记录就像遗落在街边的玩具——看似无害，却极易被恶意拾取。  
  
对于企业而言，仅靠人工清理域名记录远远不够，唯有借助智能化、自动化的工具，才能实现从被动响应到主动防御的跃迁。  
聚铭网络流量智能分析审计系统（iNFA），以全流量可视、智能化识别、深度化溯源为核心能力，不仅能有效抵御DNS劫持类恶意广告攻击，更能应对勒索病毒、钓鱼攻击、数据泄露等各类网络安全威胁，帮助企业筑牢网络安全防护屏障，避免因基础设施管理疏漏而沦为黑产攻击的“帮凶”。  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/uaicMoGl6iaSz34icEtlMpNrZxACe3gTguJPlSjxtBOOQPcKa7ZrIzTnxic8cqjicISYj6JgEeictFCc2Mq1iaupIYicaA/640?wx_fmt=gif "")  
  
  
**★**  
  
  
  
**往期回顾**  
  
  
  
**★**  
  
[](https://mp.weixin.qq.com/s?__biz=MzIzMDQwMjg5NA==&mid=2247492709&idx=1&sn=d13d438443bd9246e1020f605120d860&chksm=e8b15a44dfc6d3525bd1ff3c187ac55be18b1f9ab41c00916b75d128ae158dc2502d7956e794&scene=21#wechat_redirect)  
  
  
[](http://mp.weixin.qq.com/s?__biz=MzIzMDQwMjg5NA==&mid=2247503780&idx=1&sn=e7c699de33ef4a7b679a143d83c15c60&chksm=e8b17185dfc6f8931fcf92ce663578de1f19d0ffb69b36c2c201d318d11f475f30ed9eb75b9f&scene=21#wechat_redirect)  
  
  
[](https://mp.weixin.qq.com/s?__biz=MzIzMDQwMjg5NA==&mid=2247497553&idx=1&sn=e0824e093b4800e0b34beec69253cbf2&chksm=e8b14970dfc6c066a37f89a5f1c4f0b45d4df5ffae78d75a8be533896ab9e42ed5a00c5d8ed3&scene=21#wechat_redirect)  
  
  
  
