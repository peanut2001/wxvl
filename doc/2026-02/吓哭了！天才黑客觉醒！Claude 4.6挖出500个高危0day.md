#  吓哭了！天才黑客觉醒！Claude 4.6挖出500个高危0day  
原创 玲珑安全
                    玲珑安全  玲珑安全   2026-02-06 04:02  
  
![A piece of cardboard with a keyboard appearing through it](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zmF08GSBtAa8HzqcK1IhYa1qd8ss4FKO11b3uwrQrlTdJKoDzeF1WL4ZFiatLq2CMIXcTgOsRIcZh8PAicNU5w0ibQgrf4y4K0mzT0uricP9314/640?wx_fmt=jpeg "")  
  
这两天，网络安全圈子炸锅了！  
  
Anthropic最新发布的Claude Opus 4.6模型，竟然在测试阶段就自主挖掘出500多个此前未知的高危0day漏洞，这事儿瞬间刷屏各大科技媒体和X平台。  
  
想象一下，一个AI模型像个资深黑客一样，悄无声息地扫描开源代码，找出那些潜藏多年的安全隐患，这不光是技术突破，更是网安领域的地震级事件。不少从业者直呼“AI要抢饭碗了”，而普通网友则好奇：AI这么聪明，未来我们的数据安全该怎么守？  
  
事情的起因要从Anthropic的内部红队测试说起。这个AI巨头在正式发布Claude Opus 4.6前，给模型提供了一个沙盒环境，配备了Python和一些标准的安全分析工具，但没有给出任何特定指令或专业知识引导。  
  
结果呢？  
  
模型凭借“开箱即用”的能力，直接在开源库中发现了超过500个高严重性漏洞。这些漏洞从系统崩溃到内存破坏，应有尽有，全都被Anthropic团队或外部安全研究员验证通过。  
  
正如Anthropic红队在博客中所述：“So far, we've found and validated more than 500 high-severity vulnerabilities.” 这可不是小打小闹，涉及的开源项目包括GhostScript这样的PDF处理工具和OpenSC智能卡库，这些都是日常软件供应链中的关键部件。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zmF08GSBtAbsMibhwHCUicqbtotwgfj9mxOrxk1oTbwAfyoFk9yqtjCHoicA1jEuicUWfN196MxZzyCalDw99eqNjDsTjqfkO1vVAljmIMG4YRk/640?wx_fmt=png&from=appmsg "")  
  
更让人惊叹的是Claude Opus 4.6的技术亮点。它搭载了1百万token的上下文窗口，能一次性处理相当于1500页文档的信息量，这让它在分析复杂代码时如鱼得水。同时，模型引入了“代理团队”功能，能并行协作完成任务，比如自主编写漏洞利用代码来验证发现。  
  
Axios报道中提到：“Claude found more than 500 previously unknown zero-day vulnerabilities in open-source code using just its 'out-of-the-box' capabilities, and each one was validated by either a member of Anthropic's team or an outside security researcher.”   
  
这种能力远超以往模型，甚至在基准测试中碾压了OpenAI的GPT-5.2。在X平台上，一位AI研究者@somi_ai兴奋地分享：“Claude Opus 4.6 just dropped and the numbers are honestly stacked... it found 500+ zero-day vulnerabilities in open-source code before anyone else did.” 这种无监督的漏洞挖掘，简直像AI在自学黑客技能，效率高到让人脊背发凉。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zmF08GSBtAZ90ia1yWCE2dqYv2dy4UNkq8oJM1Qe1VaMQ5HqmAjBIW1zTlicsnWyH5r1gV3JdpdQuCwafjibxaOHXyJvibzfKkmomlCvxvU2DAc/640?wx_fmt=png&from=appmsg "")  
  
当然，这事儿的影响远不止于技术炫技。在网安行业，它像一把双刃剑。  
  
一方面，Anthropic正利用这个模型加强防御性安全工作，比如提前修补开源漏洞，帮助开发者堵住后门。VentureBeat报道称，公司开发了六个新的网络安全探针，来检测模型的潜在有害用途，同时强调Opus 4.6在欺骗和奉承等不良行为上表现最低。 这对防御方是天大好消息，能加速漏洞响应，减少零日攻击的窗口期。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zmF08GSBtAYx6RiamQhKyPLC9b75tic4dgIETYMibY3N8YndR7WaibmZVhaKTbreqet8UNtGLHcNdic0XB7xk8EtZWdoibIKkm21S8boMqNW2YJRc/640?wx_fmt=png&from=appmsg "")  
  
Hacker News上网友热议：“Opus 4.6 uncovers 500 zero-day flaws in open-source code”，许多人认为这将重塑软件安全审计流程。  
  
但另一方面，如果落入恶意之手呢？AI自主生成 exploits，攻击者只需坐享其成，这会放大网络威胁的规模。  
  
用户@rafaelgja发帖质疑：“Anthropic's latest AI model, Claude Opus 4.6, has identified 500 zero-day software vulnerabilities during testing... How prepared are companies to handle this?”   
  
确实，软件股最近暴跌，Thomson Reuters和LegalZoom股价大跌，也从侧面反映了市场对AI颠覆的恐慌。  
  
长远看，这事件敲响了警钟：AI与网安的融合已不可逆转。我们需要更严格的伦理框架和监管，确保AI成为守护者而非破坏者。  
  
Anthropic的负责人表示：“The models are extremely good at this, and we expect them to get much better still.” 这话听着振奋，却也让人警醒。  
  
网安从业者们，是时候增强审计、防护能力了；普通用户，也该多关注数据隐私。  
  
未来，AI或许会让网络世界更安全，但前提是我们先管好它。  
  
****  
**培训咨询/报名二维码**  
  
  
**ID：linglongsec**  
  
****  
****  
****  
**报喜专栏总览**  
  
**https://www.ifhsec.com/list.html**  
  
****  
****  
**SRC漏洞挖掘培训**  
  
**学员每一期的收获、我们每一期的进步**  
  
****  
玲珑安全第一期SRC漏洞挖掘培训  
  
  
玲珑安全第二期SRC漏洞挖掘培训  
  
  
玲珑安全第三期SRC漏洞挖掘培训  
  
  
玲珑安全第四期SRC漏洞挖掘培训  
  
  
玲珑安全第五期SRC漏洞挖掘培训  
  
  
玲珑安全第六期SRC漏洞挖掘培训  
  
  
[玲珑安全第七期SRC漏洞挖掘培训](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487217&idx=1&sn=42305c92cd949eaac54098830a25e9ef&scene=21#wechat_redirect)  
  
  
  
  
**玲珑安全B站公开课**  
  
免费课程观看/日常消息更新/学员赏金报喜  
  
https://space.bilibili.com/602205041  
  
  
  
**玲珑安全QQ群**  
  
191400300  
  
  
****  
**往期文章直达**  
  
关注公众号 各种优质好文速递  
  
  
[紧急预警！CTF神器ToolsFx老版本暗藏涉黄陷阱](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487323&idx=1&sn=3d29866e13562d1d8e03aaa6ab24ef17&scene=21#wechat_redirect)  
  
  
  
[谁在裸奔？1750万Ins用户数据泄露事件](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487314&idx=1&sn=a6e349da6ddf2796f3ab07e11c8876d7&scene=21#wechat_redirect)  
  
  
  
[Grok助推AI“脱衣”技术走向主流](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487306&idx=1&sn=b2593a6650b6cfd37399c8ef05c93b51&scene=21#wechat_redirect)  
  
  
  
[脆弱的锁：SAML 认证的新型绕过方式](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487298&idx=1&sn=bf20953a4367a6831a7ba2882b426ecf&scene=21#wechat_redirect)  
  
  
  
[快手至暗一小时-当公域流量入口被劫持，平台的主权究竟掌握在谁手中？](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487290&idx=1&sn=23a9c0cf59864ae9b05568af11cb56ce&scene=21#wechat_redirect)  
  
  
  
[离职当晚他敲下一行代码，不仅赔了600万，还把自己送进监狱](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487268&idx=1&sn=292b979a7274d8d608ada13f4499b9b9&scene=21#wechat_redirect)  
  
  
  
[揭秘Cookie前缀保护失效的真实成因与攻击技巧](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487263&idx=1&sn=7e609baa7958a4efe32c8a6c14918a21&scene=21#wechat_redirect)  
  
  
  
[从 Lyft 费用导出到本地/内网文件泄露的实战案例](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487258&idx=1&sn=028ed582b4247cf1490f44721566a01a&scene=21#wechat_redirect)  
  
  
  
[CSPT 漏洞原理、利用与实战浅析](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487253&idx=1&sn=f41dc0b3a9fabff2714c6fd86ccb9226&scene=21#wechat_redirect)  
  
  
  
[雅虎商业平台密码重置漏洞分析与利用](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487226&idx=1&sn=c23aeefbdbbbad583c10ceb7814af719&scene=21#wechat_redirect)  
  
  
  
[利用 Python 中不安全的文件解压实现代码执行](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487116&idx=1&sn=44b6d13d27c87a4df88bd30b425f6f21&scene=21#wechat_redirect)  
  
  
  
[Facebook 服务器上的远程代码执行](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487101&idx=1&sn=eee3fcb277c3acf137f88490aa62bfee&scene=21#wechat_redirect)  
  
  
  
[挖掘特斯拉Model 3上价值1w美元的漏洞](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487079&idx=1&sn=0984778c1477c705ac5a212a760fff88&scene=21#wechat_redirect)  
  
  
  
[入侵Chess.com并获取5000万客户记录](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487068&idx=1&sn=f390f9b13b47cff2e0b28c0e9b6d122a&scene=21#wechat_redirect)  
  
  
  
[入侵全球最大的航空公司和酒店奖励平台](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247486932&idx=1&sn=2637bc5362a6baebe08c97de465d8ab7&scene=21#wechat_redirect)  
  
  
  
[黑进斯巴鲁——只需车牌号，10秒接管车辆](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247486860&idx=1&sn=468f0cbffdbbc77dba97f69d9d73dc04&scene=21#wechat_redirect)  
  
  
  
[要挂科了？那就黑一下教务处系统吧...](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247486677&idx=1&sn=66f24e57c29ed5efa98599452843fd71&scene=21#wechat_redirect)  
  
  
  
[价值10w的Google点击劫持漏洞](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247486716&idx=1&sn=360e3382bd90ee5e9748403f5a97ee0e&scene=21#wechat_redirect)  
  
  
  
