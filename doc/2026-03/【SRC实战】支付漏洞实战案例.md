#  【SRC实战】支付漏洞实战案例  
原创 渗透测试安全日记
                        渗透测试安全日记  渗透测试安全日记   2026-03-12 16:01  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息、工具等资源而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任!  
  
01 背景  
  
支付功能作为跟money紧密相关功能，必然受各大SRC比较关注的一种漏洞，不可能让羊毛随便薅吧。  
  
因此掌握此类漏洞的挖掘，在各大SRC中是很重要的，挖到就是高危，就有相应的赏金。所以分享一个支付相关的漏洞给大家。  
  
号外号外，  
免费的睿鉴安全知识库上线了。点击下发链接，福利直达！！  
  
  
安全知识模块，只要放一些实战的案例，目前已更新五期内容，上新  
奇安信攻防社区专栏后续会持续更新。主要内容如下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4ddwM5QWicpjuQwA0qcAB3kjiapc4djsY8pgMjDPIv73wEBsjzovibo9CQn68vE8MSdKOhlWjsh1R5aQo9iasqdn3niaDWokH73cNCxg/640?wx_fmt=png&from=appmsg "")  
  
资源中心模块，主要会放一些安全工具，给各位师傅提供一站式下载的渠道，目前已上线20+款工具，主要工具如下。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4dfu30WXichWhvt9ggicSKibQUYohDYEQHQYNMzf0zjTicTkIDTy9kCVIiaDxFfnEGGwIor7KzXkjkOxgicURCojo6FT7Z9puLDVzRPu4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4deobiaoh25Fwrjau4VoiauXe9qwUGTPicLjxPVtGDEic4UqiaqaeAPFn1e7QsxdwI2EfIv2jfwuqoYEgnAWBTGjujibWdWGQUUGgskQc/640?wx_fmt=png&from=appmsg "")  
  
  
02 实战过程  
  
首先将相关产品加入到购物车中。并进行支付。可看见官方商铺限制了只能购买两个。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4ddlWfibp3SPKg0OvDoUN4A8VqLelGyWYeaNLlTQ85ypTgcSBiaEk70CmcL24N9JTJvPZmakibmvicvOsibXPS3KOcMTWS7bUkEfg65c/640?wx_fmt=png&from=appmsg "")  
  
  
进一步探索支付的逻辑。如图所示。  
先是正常创建了两个限制商品A的订单，每个订单内的数量是1，再创建第三个是出现了下图提醒说明程序有检测。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dcP9phyQzaRLKDQNgn7P9rqiaictdSiaP6ulApnQP3vn5NiayoneY6jJA6aia25EBN7LOlQbsWpYUH9CyT8KfYgjAzuQzYngYvMjy6A/640?wx_fmt=png&from=appmsg "")  
  
所以现在的重点就是看怎么去绕过程序的检测，也是本次案例的出洞点。  
  
首先分析购买流程: 进去商品 -> 点击购买 -> 提交订单 -> 程序进行创建订单  -> 返回订单创建成功   
  
经过测试发现程序虽然存在检测，但是其检测方法存在逻辑漏洞。  
  
检测方法是在发创建订单包前，  
在前端进行检测，并不是在我们发送创建订单的后在后端进行检测判断，那么我们就可以抓取一个创建订单的包，进行无限放包，以此来绕过其检测逻辑。  
  
抓下创建订单的数据包。发送至repeater模块。重放。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4ddSCO3xLjw9NrHI0BPYncKTK2BOlStY2YPDurpic2I4Rco2dbSkvcV1SJ2yJhLhtGBU99ia0ZgVVQ0ZAtfcoFEZFBszvVicD9ApbY/640?wx_fmt=png&from=appmsg "")  
  
重放3次后，针对商品A生成了3个独立的订单。都可以单独支付。成功绕过限购2件的限制。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4df2b91yyo6T2RHaoSwJvAv640xicF5VcL7pJPMAKYiaTlRrJC9V7lumCtWziarYQ6Ifl9PrCTO3kW12FJoN4jaxxJ5Vt6lEWaIChw/640?wx_fmt=png&from=appmsg "")  
  
至此本次案例分享结束！！希望对各位师傅有帮助。  
  
还有什么其他的支付逻辑漏洞，欢迎各位师傅在评论区探讨。  
  
往期好文  
  
[网络安全人员的金牌证书：为你铺就高薪职业之路](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484847&idx=1&sn=62fefecfbed336486f417e60bdf5fdd2&scene=21#wechat_redirect)  
  
  
[【SRC实战】简单FUZZ拿下高危漏洞](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485405&idx=1&sn=669a4286abd1103b050059efdb3da268&scene=21#wechat_redirect)  
  
  
[【SRC实战】RedirectUrl劫持实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485901&idx=1&sn=dc9931b8afe21cca270f80e71fda1e20&scene=21#wechat_redirect)  
  
  
[AI大模型“越狱”实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485551&idx=1&sn=5e2accbd716bf890c37a9fb7be4c06b7&scene=21#wechat_redirect)  
  
  
[企业 SRC 低投入，高收益漏洞总结](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485784&idx=1&sn=d53f6491bccec7fdcd8eca356c04f0d8&scene=21#wechat_redirect)  
  
  
[【SRC实战】任意用户密码重置实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485484&idx=1&sn=e3ccb64ef54194ae4216c1d43606b651&scene=21#wechat_redirect)  
  
  
[【SRC实战】记一次越权测试实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485379&idx=1&sn=37985dd7e56a66b2d023548eabd845ea&scene=21#wechat_redirect)  
  
  
[免密登录某后台管理系统实战](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485024&idx=1&sn=71c596dd36800993e18f1f05b9d37547&scene=21#wechat_redirect)  
  
  
[安服人应急“薅洞”指南](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485381&idx=1&sn=d0195d62adf45f6d614c785886d04e92&scene=21#wechat_redirect)  
  
  
[推荐一款资产筛选工具](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484744&idx=1&sn=7d205189f4a95c2a0cce1b6e99014c64&scene=21#wechat_redirect)  
[【SRC实战】SRC常用的信息收集方法TOP 10](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247485754&idx=1&sn=da396a3501b1346d7becdc4201299a2a&scene=21#wechat_redirect)  
  
  
[【SRC实战】短信验证码爆破，拿下某众测中危](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484618&idx=1&sn=9ef1826481eaace69ebef6849995bcfa&scene=21#wechat_redirect)  
  
  
[【SRC实战】一次“链式”渗透，从站点A打到站点B](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247484164&idx=1&sn=9c2db3fc19000f60785499f2c4ad1f6f&scene=21#wechat_redirect)  
  
  
[用户账号接管实战，洞穿开发者逻辑](https://mp.weixin.qq.com/s?__biz=MzYyMTgwMTYwOQ==&mid=2247483991&idx=1&sn=c1f6e65233cf18ade53b6e566fa4b3af&scene=21#wechat_redirect)  
  
  
