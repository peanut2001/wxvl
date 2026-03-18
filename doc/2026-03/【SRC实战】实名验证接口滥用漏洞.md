#  【SRC实战】实名验证接口滥用漏洞  
原创 渗透测试安全日记
                        渗透测试安全日记  渗透测试安全日记   2026-03-17 16:01  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息、工具等资源而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任!  
  
01 背景  
  
又又又来个“钱包”紧密相关的案例，也是各大SRC比较常见的一个漏洞，特分享此案例，丰富各位师傅的挖洞思路，助力获取赏金。  
  
号外号外，  
免费的睿鉴安全知识库上线了。点击下发链接，福利直达！！  
  
  
  
安全知识模块，主要放一些实战的案例，目前已更新五期内容，上新  
奇安信攻防社区专栏后续会持续更新。主要内容如下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4ddwM5QWicpjuQwA0qcAB3kjiapc4djsY8pgMjDPIv73wEBsjzovibo9CQn68vE8MSdKOhlWjsh1R5aQo9iasqdn3niaDWokH73cNCxg/640?wx_fmt=png&from=appmsg "")  
  
资源中心模块，主要会放一些安全工具，给各位师傅提供一站式下载的渠道，目前已上线20+款工具，主要工具如下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dc3iaKR5T6B301ZfrwCUDZmH17y5eJCugsMfbxMB0RA0O1R1H0r5eiadIIMiby591D2qwic0qd5haDVXVsy2hku0c8FeV5jCr40oZE/640?wx_fmt=png&from=appmsg "")  
  
  
02 实战过程  
  
首先通过信息收集，收到一个登录入口。直接输入手机号和验证码，默认注册账号后登录。  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dercAQJdecEr06JSTFdmSef0ib5ibiarwlO0ua6Yyc40tLeRiasvMicBPiadD22xqNlI2wMia6rI83dhF5zVwXTYicTCRBP7Z4bKm3CS5E/640?wx_fmt=png&from=appmsg "")  
  
登录后，可以看到。很显眼的要你输入真实的sfz信息，并确保和支付宝一致。一看就有洞。这个啥意思？  
  
意思就是你输入的身份证号，这个系统会拿去调用支付宝进行校验是否真实。注意这里调用第三方的身份真实校验接口是付费的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4dd2RAy9qzW2c51JlYNQdAkNspTbvhG3NMLUX4lpb8NO41BDVOXGMwKDsD6HQTWTsLjibs686PlGROXMibzSA4g0nmicfcLxs6covk/640?wx_fmt=png&from=appmsg "")  
  
好家伙，来真的了，现在之前用伪造的身份证绕过实名认证的方法用不了了。但这也导致了本案例中提到的实名认证的漏洞。可以看到用xia_liao生成的假的sfz号是用不了的。（需要这个burp插件的师傅小程序中取，推荐）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4deft2YvedL452ibEmiasrf5SPpRFNfCkMCTy2lK7HkZibwySf2KXVVdYf9mtKmJY3zkxPLl4WEZMIOoswHia9PG6vv3DDOcnw4aKA4/640?wx_fmt=png&from=appmsg "")  
  
输入相关信息后，点击保存。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4dcDNfeBzU2DgFkSXEwBYxpfY62YgEaek0KKkQFmLgOjArWkpJcbnfpxk4Jn2ykdcAKTOTJMMnDIK8pGpXt5ELKpW19rfo9br5s/640?wx_fmt=png&from=appmsg "")  
  
用burp抓包，并放至repeater中，可以看到，证件号码是校验不通过的。说明在支付宝侧没有注册或者这个sfz号是假的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Euxpicz6k4ddmlkEk1gmibu4MMRDX2ckkzEqIUQo0b8BRvfawUkvL4BK0sibqIicd8oLfvHAl1sTdwahPHfwthPlZUG7QbvLOLPzk4y8eVR0kBs/640?wx_fmt=png&from=appmsg "")  
  
此时，将上图中的最后一位改为6。可以看到校验通过，说明这个sfz在支付宝中是通过校验真实存在的。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Euxpicz6k4dcS1xHVBWrJcIrcfSmYj5AZ9kHHGzcZ9gzbh2icv92hu5JmppLMUsWvd7VMYr3JG0RbejYiaexf6Q0Qzk8ru2yIT4SsvKxdKld3c/640?wx_fmt=png&from=appmsg "")  
  
可以看到在保存时，无相关的图形验证码，所以可以进一步爆破进行查询，爆刷这个接口。  
  
那么这个漏洞的最终的危害就是造成此系统调用第三方接口的费用不断的提升，当达到上限时，服务不可用。  
  
同时也会造成经济损失(  
身份证二要素0.2元/次。只要系统收到了请求，都算一次调用  
)。还会给hei hui产利用，还是有危害的。  
  
点到为止，提交src。本次的实战结束。  
  
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
  
  
