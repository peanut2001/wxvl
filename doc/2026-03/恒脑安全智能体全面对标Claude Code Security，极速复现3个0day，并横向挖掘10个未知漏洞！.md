#  恒脑安全智能体全面对标Claude Code Security，极速复现3个0day，并横向挖掘10个未知漏洞！  
 安恒信息   2026-03-02 00:27  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icVz8RbowK3zzWCaicK1LPbSTJDDcicxleNaqXXSxYPFppNTsB1z02AlkKRMHgtzdCselqbaOWGGfYJPqibodouxRQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
![]( "")  
![]( "")  
![]( "")  
![]( "")  
![]( "")  
![]( "")  
  
恒脑安全智能体  
  
近期，Anthropic发布Claude Code Security后，在其官网提及基于最新Claude Opus 4.6模型的Claude Code Security工具发现的  
三个典型0day漏洞（现维护者已修复）。安恒信息恒脑安全智能体在  
完美复现了其公开披露的3个漏洞，并在此基础上，在相同模块中  
自主挖掘出10个未被披露的全新0day漏洞，用实打实的战绩证明了中国AI安全技术的深度与速度。  
  
  
  
一、100%极速复现——  
  
验证恒脑安全智能体基本功  
  
  
面对Claude Code Security披露的漏洞信息，安恒团队第一时间启动恒脑安全智能体进行对标验证。其目标不仅是“跟着走一遍”，更是“验证基本功”。  
  
  
01  
  
复现过程如下：  
  
  
  
  
  
  
  
01  
  
gs_type1_blend 函数调用堆栈越界读取漏洞  
  
  
  
02  
  
card-piv.c piv_process_history函数缓冲区溢出漏洞  
  
  
****  
****  
  
  
  
  
03  
  
LZW压缩模块pLZWData缓冲区溢出漏洞  
  
  
  
  
扫码获取链接，深度了解漏洞复现过程  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/QsTClNuIiapHhfrcrsysc4ia1utglop50dViaQCV23icGEATyDqZ6R1UJMZoQpPxWx8zjrRxQtwF5Whf5SsEno5BORHBAwNjWmLZgJ255nibyRP0/640?wx_fmt=jpeg "")  
  
  
  
02  
  
复现结果如下：  
  
  
  
  
100%复现  
：3个官方0day漏洞全部成功复现，攻击链与触发路径被完整还原。漏洞的利用条件与影响范围，与官方披露结果完全一致。  
  
  
  
效率反超  
：更令人惊喜的是，在部分复杂场景的复现过程中，恒脑展现出了更高的效率与稳定性。  
  
  
  
恒脑安全智能体展示出极速、精准的复现能力，体现出其基本功，也证明了恒脑具备与全球顶尖AI  
的  
安全  
能力  
同等的漏洞深度理解与工程化实现能力。  
  
  
二、  
横  
向挖掘——  
  
发现Claude Code Security未能发现的10个0day漏洞  
  
  
在验证完官方漏洞后，我们基于同一目标系统模块，启动了更深层次的横向扩展测试与攻击面延展挖掘。  
  
01  
  
成果如下：  
  
  
  
  
针对相同模块的进一步审计，恒脑安全智能体  
额外挖掘出了10个全新的0day漏洞！（7个属于ghostscript项目，3个属于opensc项目，相关漏洞均已报送  
国家漏洞库）  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/QsTClNuIiapEWziboBNlqjrLiayrXMy7GT2DRu1eric94RMdGY3guO961VmfQiarczQ72A4OiaGdibBbHHlHqTEnkMxbohXzKib4OWxcDBpkucYa6Bo/640?wx_fmt=png&from=appmsg "")  
![]( "")  
![]( "")  
![]( "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RTMjPYV9EDzdkXAajhE2h0mdmdBJWQQkoBjt3UzibibxVibgYZC131fa75YiaVEic1ezvdVgn1lvHzuQvaew5uf0iapA/640?from=appmsg "")  
  
“横向挖掘”的深层含义  
：像一位经验丰富的“安全侦探”，顺藤摸瓜，系统性地扫描整个关联模块和各种攻击面，将那些隐藏极深、逻辑复杂的风险一一揪出。这正体现了  
恒脑所构建的“高精专作战体系”，而非单纯的通用智力引擎。  
  
  
02  
  
亮点阐述：  
  
  
  
  
 这不仅仅是数量上的“13>3”，其背后是  
AI自主发现能力的质变。它意味着恒脑并非依赖已知规则进行模式匹配，而是通过深度代码推理与逻辑分析，  
发现了对手遗漏的、更深层次的同类漏洞变种与安全隐患  
。  
  
  
从一个点到一张网，从“发现已知”到“挖掘未知”，这正是AI自主作战能力的质变时刻。  
  
  
三、能力基石——  
  
恒脑安全智能体为何如此“能打”？  
  
  
恒脑能在短时间内交出如此硬核的答卷，绝非偶然。其  
核心壁垒在于  
 “AI能力”与“安全Know-How”的深度融合。  
  
  
1.不止于通用大模型：恒脑安全智能体将通用AI能力，与安恒信息十余年积累的独家安全私有数据、实战攻防经验深度融合。这使得它  
能理解业务配置风险、多漏洞组合利用链等复杂场景，这是缺乏行业深度的通用工具难以企及的。  
  
  
2.全流程自动化闭环  
：从自动获取代码、深度理解逻辑，到精准挖洞、生成PoC验证，再到输出报告，恒脑实现了规模化、高效化的全流程自动化。这正是它  
能快速响应并开展大规模深度挖掘的技术保障。  
  
  
3.经过顶尖赛事淬炼  
：就在2026年1月，恒脑安全智能体作为  
全球首位AI选手，亮相第六届“天府杯”国际网络安全大赛，与人类顶尖黑客同台竞技，并在漏洞防护赛中一举杀入  
前三。这场实战充分验证了其  
在真实、高对抗环境下的技术实力已超越绝大多数顶尖安全专家。  
  
  
此次3+10的实战，是恒脑能力的一个缩影。未来，安恒信息将以恒脑为核心引擎，践行“产品即服务，服务即产品”的理念，全面发力主动威胁狩猎、自动化渗透测试等“高阶专家级”服务，用AI将过去高度依赖人工的重度安全服务，推向智能化、自动化的新纪元，持续  
筑牢国产自主AI安全屏障。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/QsTClNuIiapFraamN4w3EPWwR4NkEFX7tmbZ7n9yRjK8ZFKHSL8mwKjqquyFu616bI04P2iaVpvsfr3GRGiagl9lZbqb8ILWb33F32pfjeATdU/640?wx_fmt=png&from=appmsg "")  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6Ppczr1X4OOTmbg4rENrqwqbYqRtgl3icicic9an9TicNrOnKOT4t2icSyx7w/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7 "")  
  
**点点赞**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6P0OFJt7aruYwYjIWic5WCu7iaE9ZYWmW6TKPcvrib6Itmpc0dnMqlANmow/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8 "")  
  
**点分享**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PwKHSiaCHQrj4D3mJJZ7QGPX1zbt3rJEKjhdBkX12A8r5L47fI28upaA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9 "")  
  
**点喜欢**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icVz8RbowK3xzIKqgIUoHg8ON8MPvhQMkOB9mG8MplP3nlQiafURYtS2fgRnV3VDzZGw30stEsVncKTibBOztr1fw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icVz8RbowK3xzIKqgIUoHg8ON8MPvhQMkayLWbo5FibOofeRRQK28aqM8UjzLN9k9qYf4vvwRLmOcHgUg6bMKsAA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=16 "")  
  
点击下方名片立即关注  
  
不走丢哦！  
  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PzUETDErlviazPRtpVtc98iasfL8RCCib8yzmeGJ9HrBlJASFn5qz95QwQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=9 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6Pb2aOfdTZnZZbozL1mvicIWsdWicdDcibz2SAuHblLHicWQc8CmX6WT6OMA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/icVz8RbowK3w0BggvHRq4iaXMuxkRPMb6PBQVNtt5ynIG7UjUHbRJFvFXgKjZW6mzjjhlxfjwtXfrdJyPgroKWQA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11 "")  
  
  
**往期**  
**精彩****回顾**  
  
  
  
  
  
  
[王欣深度解读中国版“Claude Code Security”与ClawdSecBot应用逻辑](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650646495&idx=1&sn=700558b0863a38eeac2c1f4398dc14d5&scene=21#wechat_redirect)  
  
  
2026-02-27  
[](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650646495&idx=1&sn=700558b0863a38eeac2c1f4398dc14d5&scene=21#wechat_redirect)  
  
  
[金融信创安全三大破局之战！安恒信息揭示智能化安全新路径](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650646469&idx=1&sn=a76ee7cb5731c852e52b1e6e21e834eb&scene=21#wechat_redirect)  
  
  
2026-02-26  
[](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650646469&idx=1&sn=a76ee7cb5731c852e52b1e6e21e834eb&scene=21#wechat_redirect)  
  
  
[安恒正式推出中国版“Claude Code Security”!恒脑安全智能体漏洞挖掘能力跑出行业加速度](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650646468&idx=1&sn=e59e896dc7f57d33d661435f3d857652&scene=21#wechat_redirect)  
  
  
2026-02-25  
[](https://mp.weixin.qq.com/s?__biz=MjM5NTE0MjQyMg==&mid=2650646468&idx=1&sn=e59e896dc7f57d33d661435f3d857652&scene=21#wechat_redirect)  
  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/icVz8RbowK3wm5VicXg2ibVyMsjPZ3OJSzTwdeSU207GIcBicQDzkDVgFNvXD0npWKhFtBb2VtiaczibVqM8HE0vRoNw/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14 "")  
  
