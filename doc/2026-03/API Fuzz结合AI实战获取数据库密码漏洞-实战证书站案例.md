#  API Fuzz结合AI实战获取数据库密码漏洞-实战证书站案例  
原创 猎洞时刻
                    猎洞时刻  猎洞时刻   2026-03-16 00:00  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH9evFcNH31Pjh0f83GEqsibSQsGS8uUrBPLU6VJbjw8CTibOgsYYOhqqKpaQHb9BicrJcCOYhZG0tYOg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**免责声明**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn6mG6TyJornrhz9JticBo3Nx4zhzUFXcggEDw1lkfzMI0KuLp7dW4dDCvbfgAKlLSX3yGmYg0gtXcw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
```
本公众号“猎洞时刻”旨在分享网络安全领域的相关知识，仅限于学习和研究之用。本公众号并不鼓励或支持任何非法活动。
本公众号中提供的所有内容都是基于作者的经验和知识，并仅代表作者个人的观点和意见。这些观点和意见仅供参考，不构成任何形式的承诺或保证。
本公众号不对任何人因使用或依赖本公众号提供的信息、工具或技术所造成的任何损失或伤害负责。
本公众号提供的技术和工具仅限于学习和研究之用，不得用于非法活动。任何非法活动均与本公众号的立场和政策相违背，并将依法承担法律责任。
本公众号不对使用本公众号提供的工具和技术所造成的任何直接或间接损失负责。使用者必须自行承担使用风险，同时对自己的行为负全部责任。
本公众号保留随时修改或补充免责声明的权利，而不需事先通知。
```  
  
首先信息收集，因为是证书站，很多明面上的简单漏洞都被挖得差不多了，所以难挖，所以我fofa找外围的脆弱资产，title=xxx大学  
  
找到这样一个网页，ip138归属也为该大学的资产。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VX5wK691wDXsIwwUkuiceWRkGqM9ZuIuMG0xibkSntyKOAaw1aNkqow4aw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VX55kMiaZHuSItdAEnmaHfuAx4Nw7cYxrDnUNcya9Zn0OibxRhZib3Ftvdg/640?wx_fmt=png&from=appmsg "")  
  
  
进入网站看见右上角有个登录口，点击返回如下，看来这个站的登录框有可能被人挖过了，现在修复了。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXpCXkB1p8d1saqModmn835iaJuBu2YLLGtlm7nY5RmBhFqq5AwlQ9evA/640?wx_fmt=png&from=appmsg "")  
  
  
在点一下其他功能测试，直到点击下面按钮的时候。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VX5hicfS2EowFaZ7lZECUiaqBfLgyblUrUrvRRbuIsIAnd9nAvu1lzwYwQ/640?wx_fmt=png&from=appmsg "")  
  
  
然后数据包看见  
一个接口，翻译接口英文就是从app的配置文件里获取信息。  
  
CONFIG_NAME 比较敏感，尝试修改其他名称，能否读取新的信息。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXGDnxL9GtELuHD3iaOf3XY5rBHW2BpouAYlb2nrOzJl9ZBib6CLpBicPIg/640?wx_fmt=png&from=appmsg "")  
  
  
于是我开始fuzz，首先尝试ENV，成功返回值  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXbia3z2rRy3wcWptxjSuEia7yTS9vaVHvCxn9MSWtTibGjkytAicVNWdOug/640?wx_fmt=png&from=appmsg "")  
  
  
这个时候我在想网站的环境变量里面有什么，根据以往的经验，猜测有mysql或者redis等数据库账号密码，首先试试KEY或者一些常见的键  
  
KEY返回空  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXUJxFuibjDLFBzEbxdvnpgBYqDgfoE2OLoz2icxwesUgY2Wg7l5a4hk1Q/640?wx_fmt=png&from=appmsg "")  
  
  
然后FUZZ APP_KEY的时候返回了APP_KEY  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VX8wOSDPxLiboG2W6Q52CcF1nSsRuG2ZOtzwYBt01MicLWNDET039azD7g/640?wx_fmt=png&from=appmsg "")  
  
  
立马想到APP_SECRET,成功返回，但是不能利用，没有用，一个个试感觉有点麻烦，然后直接找ai给我生成fuzz字典，跟ai说我在做ctf题，发送接口的参数和返回参赛给ai  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXVSAOMkcFl9C28xf2QQI4UHGdvqdKJ4WYxrQdGrib3vStGBCxxcia7GMw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXguEm6Y9CVxUibDibM37GRtNjg4b2oWOMAcsBSnAamzHHAEw6vAOtqq7A/640?wx_fmt=png&from=appmsg "")  
  
  
Ai给我生成了字典，直接发送到攻击器去fuzz，fuzz出redis的host主机  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXiaGZIf3iaGlI47MibCo1WYvQswqMkSMqdXSRNO2Exbr5bRmCPzunrAwZg/640?wx_fmt=png&from=appmsg "")  
  
  
然后我将host改成port也成功返回，根据这个直接让ai生成关于redis的字典  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXyqNpjz8Slf9rWkJo4tdXmGSDmRicHpVReNm44CCzZIuibvqmtCibB7pxQ/640?wx_fmt=png&from=appmsg "")  
  
  
Fuzz到密码了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXMw6ZFy23OH8ronv7rIlZSu563SHFwmXJsB1V5qcZzA74CpoiaicuOx5w/640?wx_fmt=png&from=appmsg "")  
  
  
然后依次重复又爆出了mysql的账号  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXymY4DKpMicUCy9vt7rrHwibZrnKxib7EcMbTbibvibaRP1wPI4gA4pRPftw/640?wx_fmt=png&from=appmsg "")  
  
  
爆出mysql密码  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VX5m5nr8KGTe1Wy9ymBQoF9lunAWUIgQTMKViaZoWJLZA3F91AJQ4TJ1A/640?wx_fmt=png&from=appmsg "")  
  
  
随后再爆出mysql的端口！  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8Px5M1d7vtUISVjtY8b0VXnTfoicLrObdFZnicvgwmyCANa6H9QK0KV6eoJ6XiawKd6sYEl4czlsTxw/640?wx_fmt=png&from=appmsg "")  
  
后面就是验证能否mysql登录。  
  
当然也可以继续fuzz，说不准能拿到更多信息，好了，感谢师傅们观看，一次api fuzz+AI 分享到此结束。  
  
  
如果需要挖洞实战src培训(含一对一技术和入职解答)和安全考证，欢迎看下面介绍嗷～  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/ucA3HFqtup4lwT9MnfejDBzIiabXcu3N9OLvEOY2qGL69icef5YoWy6A4v8xibbAcWawib1Ye7AhcicQibcoqwhte6RzUHDibs6eSg98tTsuSnRyqA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/pxmgfRlwjjQEDKVbwyMsgkkXnIGyoQh8WqO1yON9a5qQREgXKAxGXgUic5mnhJPFeZepvrKQnrgevjFqW9icAhTg/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TjzCwgOAXajGjch5dJybW7g6niaFmGsenWK3eRSuh6Zc2nBm3juAHia3BXrLEkW4Q6zXicjib80ibCbA3dqetAep3Vg/640?from=appmsg "")  
  
「 往期推荐」  
  
  
  
[推荐一个SSRF自动化扫描Burp插件](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247489677&idx=1&sn=93463a5e05577c832108e3185adfd5fc&scene=21#wechat_redirect)  
  
  
  
[AI大模型提示词注入实战](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247489656&idx=2&sn=a6629e90723feee36833a724231eb66b&scene=21#wechat_redirect)  
  
  
  
[实战案例｜信息收集新思路并三次绕过登陆检测](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247489716&idx=1&sn=4f8ae2955ea03e8f87e1f9d6171e3a60&scene=21#wechat_redirect)  
  
  
  
[关于网络安全超低价格考证CISP、PTE、NISP](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247489670&idx=2&sn=0763c8952fb77162909b12c9cdea771f&scene=21#wechat_redirect)  
  
  
  
[Webpack打包js.map泄露导致的通杀0day](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247489640&idx=2&sn=3469362ed58fa6ed8b95e26652c9c265&scene=21#wechat_redirect)  
  
  
  
[企业SRC赏金漏洞挖掘实战-多个奖励条件绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247489549&idx=1&sn=5683235b8fd49c5cb1601a0ca0b7d1bf&scene=21#wechat_redirect)  
  
  
  
[[猎洞时刻] XSS如何乱杀企业SRC赏金](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247489507&idx=1&sn=3a49f4eb79fe4723c281ea932c510105&scene=21#wechat_redirect)  
  
  
  
[开局一个登陆口渗透二十多种方式-公开课](https://mp.weixin.qq.com/s?__biz=MzkyNTUyNTE5OA==&mid=2247489446&idx=1&sn=938523b3af2811d7a6601434c2924ca6&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MoM4ibZQic0icEr4mg4zIh4m4JicbKk4bzSREndPB6iagvlib7gOJqFJnrO0bNINt8a9eDVD1apJjuKD6Xcj0fAxPmBQ/640?from=appmsg "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/6sTFU8pTrmbOrffDZC4eviaUGATv5IdZibGfKicjoXicLWHzR2P59VNmwibojvurAjiaLXV3vmiamyMqgTND2EdqesU6g/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/6sTFU8pTrmbOrffDZC4eviaUGATv5IdZibGfKicjoXicLWHzR2P59VNmwibojvurAjiaLXV3vmiamyMqgTND2EdqesU6g/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/cN92fstOicgIODrJ4zh2ur1RublJ5Go9EwvnnfiarROZV2dyggctibQGrCCQMGWIyEQKpV41PRSvuibTRqL0dOhHuw/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/KX4I8DCXpFRUZiackUcKHBakOymyt29sNiaXWjFzq53lRLkBCae3uluibWzBcmFd6VjckWtdyJINx8YcsZicdjJIFg/640?from=appmsg "")  
  
猎洞网安第四期挖洞培训正式开启！  
  
HAPPY NEW YEAR  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XlDccKmwUxpdHwn9CAZQGzA7zhUXAWlPWqiaqgoX5mroSGLZz9d8lKOyiaIHibcOiajtiaBZ2fteBkSEXeUlCX2ZRMQ/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CRCWJpzeT1EnCOpghLqMn1pUdGSh92YplOib5UKrjeNicoaGtSKNXK63icibfzpufRbicGictnf2RBfHPOibXZSicibzm0A/640?from=appmsg "")  
  
猎洞SRC挖洞培训简介  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVSvuzvYiba0p67Qu5yqicmyyx6aBszyQ2OnrdeAARKPUEYGtWjOyGoc5JnjHzb8JFUwthnZlmlYHCh0WMogSzWw/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tTibAMib2Ruh2xpqvLTonQuSq625EZ7wEzCaLScjPQywlcicXJHLI2LTv6Q36BsICLqibV0jDvD6IfRep3ib7AXmryg/640?from=appmsg "")  
  
猎洞时刻，专注网络安全挖洞领域的实战培训。  
  
团队成立于2023年，至今已吸引上万名安全从业者关注，累计帮助众多学员从入门到实战，逐步建立起在挖洞方向的影响力。我们致力于为每一位在挖洞路上探索的师傅，提供真正有价值的学习资源、实用的实战经验，以及永久在线的陪伴式答疑服务。  
  
  
2024年，我们从“安全小圈子”知识星球起步，逐步搭建起成体系的挖洞培训内容。起初只是一场小范围内的内部培训，却意外收获了众多师傅的认可与推荐。  
  
  
2025年，随着课程体系不断完善、课后服务质量持续提升，团队口碑在圈内迅速发酵。如今，无论是在主流SRC平台、众测项目，还是网安大厂企业内部，时常能见到我们学员的身影。  
  
  
2026年，历经三年实战沉淀、四期课程迭代，在众多师傅的推荐与期待中——  
  
  
猎洞SRC第四期于2026年3月初· 正式上线！  
  
  
📌  
往期课程回顾：  
  
第一期：16节课（已结课）  
  
第二期：22节课（已结课）  
  
第三期：37节课（已结课）  
  
第四期：预计50～60节正课 + 附赠20节零基础入门课程（火热开课中）  
  
  
📌公众号也在短短几年内，收获了上万位师傅的关注与持续支持。感谢每一位阅读、分享、推荐我们的朋友，是你们的认可，让我们一路走到今天。  
  
  
愿所有走在网安路上的师傅，挖洞如饮水，洞洞皆可寻。猎洞时刻，始终与你并肩。  
  
  
  
  
挖洞培训、安全考证、扩列，欢迎加我微信！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup5cEBENTmWaCicoEheEEFMjHR5KaD1I0Hj4brYkZq4uRSV6ZtXicz9k0SHdGVELFiaa3iaVt7hXbPr2Vl5ibTJibjEYtlNBQCE6HO5BM/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Uxiano3ib6ECceVUPW0lnfaN4byRTz3gV6nCTaK2ReZUUmSzKbQ6DgtZceUpnnj6JrMcRb3NY1gNTFeYXoYZHr9g/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XlDccKmwUxpdHwn9CAZQGzA7zhUXAWlPWqiaqgoX5mroSGLZz9d8lKOyiaIHibcOiajtiaBZ2fteBkSEXeUlCX2ZRMQ/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CRCWJpzeT1EnCOpghLqMn1pUdGSh92YplOib5UKrjeNicoaGtSKNXK63icibfzpufRbicGictnf2RBfHPOibXZSicibzm0A/640?from=appmsg "")  
  
猎洞SRC正课进阶第四期课表  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVSvuzvYiba0p67Qu5yqicmyyx6aBszyQ2OnrdeAARKPUEYGtWjOyGoc5JnjHzb8JFUwthnZlmlYHCh0WMogSzWw/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tTibAMib2Ruh2xpqvLTonQuSq625EZ7wEzCaLScjPQywlcicXJHLI2LTv6Q36BsICLqibV0jDvD6IfRep3ib7AXmryg/640?from=appmsg "")  
  
    本课程覆盖企业赏金SRC，众测赏金，EDUSRC，CNVD和工作项目渗透挖掘。课程内容方面主要是Web挖洞、小程序挖洞、APP挖洞、JS自动化加解密逆向、小程序自动化加解密逆向、云安全、HVV护网培训、项目教学挖洞实战、AI大模型安全、前端安全渗透等内容。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup68goK4nS6VI3gn60nCLIwp0BAJG1jlx2jaRob3fhNpEUGXaORBFBia3HGnnXxW8zbbOD4kWzMxWHPu1OzfT7m0ICW4dBeQdH4I/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Uxiano3ib6ECceVUPW0lnfaN4byRTz3gV6nCTaK2ReZUUmSzKbQ6DgtZceUpnnj6JrMcRb3NY1gNTFeYXoYZHr9g/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XlDccKmwUxpdHwn9CAZQGzA7zhUXAWlPWqiaqgoX5mroSGLZz9d8lKOyiaIHibcOiajtiaBZ2fteBkSEXeUlCX2ZRMQ/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CRCWJpzeT1EnCOpghLqMn1pUdGSh92YplOib5UKrjeNicoaGtSKNXK63icibfzpufRbicGictnf2RBfHPOibXZSicibzm0A/640?from=appmsg "")  
  
猎洞学员EDU挖洞成绩介绍  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVSvuzvYiba0p67Qu5yqicmyyx6aBszyQ2OnrdeAARKPUEYGtWjOyGoc5JnjHzb8JFUwthnZlmlYHCh0WMogSzWw/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tTibAMib2Ruh2xpqvLTonQuSq625EZ7wEzCaLScjPQywlcicXJHLI2LTv6Q36BsICLqibV0jDvD6IfRep3ib7AXmryg/640?from=appmsg "")  
  
该部分内容实在太多，这里仅展现部分成果，想了解更多可以加我微信了解。  
  
  
在Edusrc平台，我们是2025.4开始挖掘本平台，截止到2025.12底，我们在2025年个人榜单第一名、2025年团队榜单第四名、全年总榜第六名，也算是进步比较快的！非常感谢这些小伙伴们的支持～ 并且会给冲分的优秀学员奖励红包、鼠标或者键盘奖励！  
  
  
以下为2025年团队榜单，第四。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup47Q9yeOYHzvAGUvtJQjMMeBu99icJQlACfUoJkcNibEjXBwL6uZ8GefrwaUItGmmYeP5sIIAKOwdyGLafXvhA2PoTUQEj3wjXzA/640?wx_fmt=png&from=appmsg "")  
  
  
以下为Edusrc 2025年成员个人榜单，稳第一：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup7JL1icdib9zXgG2uUuwwScAwm9zUM93YZ0LibPzLUPPAzA8Pxs3kAGIczxSj2dSiavNRb41jKndK0ccSEEu6ZDvXAKTQnQBw29ELc/640?wx_fmt=png&from=appmsg "")  
  
  
以下为Edusrc平台所有年份汇总的总榜，第六：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4jD7MDTcsKutOZU8QDiakjDrgec1oQLT49picuglSy2orwiaRogSxyI0yMQiaDua6WrrAFRsiazlkouFLQiaU0YJCvwjkvDP0xE0fyU/640?wx_fmt=png&from=appmsg "")  
  
  
以下为其中单个学员的个人edu证书（并非多人汇总证书）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup6GzP3DnrYNkribSjA5jZibsuzANRwqpLWGookh2oM3C1Bic6Fu1oJxSI2YFMSJSAp6RMgoVdK7wskdH8TB00NI5c7Sepdgic0icic4I/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Uxiano3ib6ECceVUPW0lnfaN4byRTz3gV6nCTaK2ReZUUmSzKbQ6DgtZceUpnnj6JrMcRb3NY1gNTFeYXoYZHr9g/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XlDccKmwUxpdHwn9CAZQGzA7zhUXAWlPWqiaqgoX5mroSGLZz9d8lKOyiaIHibcOiajtiaBZ2fteBkSEXeUlCX2ZRMQ/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CRCWJpzeT1EnCOpghLqMn1pUdGSh92YplOib5UKrjeNicoaGtSKNXK63icibfzpufRbicGictnf2RBfHPOibXZSicibzm0A/640?from=appmsg "")  
  
企业赏金SRC和CNVD  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVSvuzvYiba0p67Qu5yqicmyyx6aBszyQ2OnrdeAARKPUEYGtWjOyGoc5JnjHzb8JFUwthnZlmlYHCh0WMogSzWw/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tTibAMib2Ruh2xpqvLTonQuSq625EZ7wEzCaLScjPQywlcicXJHLI2LTv6Q36BsICLqibV0jDvD6IfRep3ib7AXmryg/640?from=appmsg "")  
  
学员部分赏金和CNVD荣誉。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup5gx0vRDEtNugy3I6pv7hMrvfLHficNWPCdjkEz4OyCibdLDjDjn8KKYqYtgS2GfpbheurvVrfjkt2mpTBPyqrAyiclic8icrTeLxqA/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH9uGoiaibSicrHjpP7JPHMnqraO5bf3yJibLStSPvnphsLbLzcW7NRcnsoljHjZ9IVib3TWDV549OiaT9Yw/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTHica68o8ricbIGvbVRGsvCBojIWz5ZnHcntAXwm2yibBK51JXM5c0kzjTia0psDvtfy22vDQPq3QiaFWgQ/640?wx_fmt=png&from=appmsg "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTHico4s7YfpmcHmWDlhInfXQ3onZicYXP4Uj0ouTBT5XjibfTpA5kiaZzewcDnlKhicLxy12Oa2lm7jhU0g/640?wx_fmt=other&from=appmsg&randomid=vkc2323j&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup6Xfw1tqotTNhVtezd2Dhd6WwQLqUGCtMFKkdtR9nEA78IeMu6qZdfzpHTI4ziao3ap3szks0S8O9l3cfsDWt3pDje6OicnJvk0I/640?wx_fmt=png&from=appmsg "")  
  
  
还有学员的CNVD证书，多的摆不下。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup7zydZbluqDD8hdQWiaWlDmHJCvZr3Ns6hfKictgYiaPhJicSSIGHVkTibBFB48vNxa7ys3YLjPfjchalvJ2Yic8OvUsHib2iaTSSTYqWA/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup7TEql9u6j74sibz6pFFUSxIA51YHLGqVk7aL7kCI8lPvYY0t4hFJY57TdgDia0EYLhRuuxz46UTXyiaW9E7hg43estefjDhHibmHo/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup66AJXiayrHu3YyUicnicCRcnDORsBIhxg0RmkuxIqJmDSbelrcUQRppowJG9BSe0uNyqyMPxdpZ9ebia0fkdB6N7FzcrfBOzF2hGc/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Uxiano3ib6ECceVUPW0lnfaN4byRTz3gV6nCTaK2ReZUUmSzKbQ6DgtZceUpnnj6JrMcRb3NY1gNTFeYXoYZHr9g/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XlDccKmwUxpdHwn9CAZQGzA7zhUXAWlPWqiaqgoX5mroSGLZz9d8lKOyiaIHibcOiajtiaBZ2fteBkSEXeUlCX2ZRMQ/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CRCWJpzeT1EnCOpghLqMn1pUdGSh92YplOib5UKrjeNicoaGtSKNXK63icibfzpufRbicGictnf2RBfHPOibXZSicibzm0A/640?from=appmsg "")  
  
学员网安大厂入职层面  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVSvuzvYiba0p67Qu5yqicmyyx6aBszyQ2OnrdeAARKPUEYGtWjOyGoc5JnjHzb8JFUwthnZlmlYHCh0WMogSzWw/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tTibAMib2Ruh2xpqvLTonQuSq625EZ7wEzCaLScjPQywlcicXJHLI2LTv6Q36BsICLqibV0jDvD6IfRep3ib7AXmryg/640?from=appmsg "")  
  
    很多人挖洞一方面是为了做赏金、证书，但是更多师傅来我这边的是大学生，想要入职一个好企业，才来锻炼自己的挖洞能力，挖洞是这个行业的技术基石，只要挖洞做的足够好，入职才能更顺利。  
  
  
     
 网络安全常见几个安全大厂，比如技术顶尖代表-长亭科技、还有网安一哥-奇安信、网安黄埔军校-绿盟，还有安恒、深信服、启明星辰、360等老牌安全公司，均有不少学员遍布，下面是部分offer，如有造假，欢迎打假👊我！  
真正的大厂学员聚集地！我们从不推荐那种垃圾低薪的伪网安工作，最低也让你去冲个做挖洞、渗透的网安厂商。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4MqHR5FQwOKicazcoZibcRoLZqZsJmkeGJQj9QicLOibIzVpUcbFm0L1clyQTUztc0rDFOkrZaZiaLIhwQ4MibraVNNGFFF8PArj8ZQ/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup5M3lUqtya4FU7ldibnlT2ohqgU3VfHPsWH7TMZRkXbv9gjCCqVRwujS8BJXJo7eic0ViaJJXwBlGXlm753JFR2icYH8ibpZVaWAK3g/640?wx_fmt=png&from=appmsg "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTHicVgicZmS5Yd5mD2hUJQ4YcQOFvcTeZOJs35zkDNDjcOFC0WpBaz2ia3mF8CHsCdC4IsFjJJRh46L8g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH84CZG0rxw3p3txiar8hJibcTIW1TWkYEQyTzhlTNG0ULg55ST3qoFJicKqdG2duTK3vnSyGJSCVB84w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8NuPia6aIOENP4XGImm3Ycrn5D3XHRicyCjJXdLklxpSDSAoYppBCkgIlVlIILh3nicRHFOqBDIKdDg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH8NuPia6aIOENP4XGImm3Ycrh9yBcBMDSRckD2796FbMX3iacAwAbzUgdTlT4MtDUFcQUykkWcNgk4g/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup6z5MqpwjRicUCMOOxDQOalgh67DLfvicR0gGYjPqluVM8D5z7yAVNlPflAzflGia9EoaMb5LuKrHW0IvnhG4bgEfxjhLkYM90ZW4/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Uxiano3ib6ECceVUPW0lnfaN4byRTz3gV6nCTaK2ReZUUmSzKbQ6DgtZceUpnnj6JrMcRb3NY1gNTFeYXoYZHr9g/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XlDccKmwUxpdHwn9CAZQGzA7zhUXAWlPWqiaqgoX5mroSGLZz9d8lKOyiaIHibcOiajtiaBZ2fteBkSEXeUlCX2ZRMQ/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CRCWJpzeT1EnCOpghLqMn1pUdGSh92YplOib5UKrjeNicoaGtSKNXK63icibfzpufRbicGictnf2RBfHPOibXZSicibzm0A/640?from=appmsg "")  
  
猎洞网安零基础课程-赠送  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVSvuzvYiba0p67Qu5yqicmyyx6aBszyQ2OnrdeAARKPUEYGtWjOyGoc5JnjHzb8JFUwthnZlmlYHCh0WMogSzWw/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tTibAMib2Ruh2xpqvLTonQuSq625EZ7wEzCaLScjPQywlcicXJHLI2LTv6Q36BsICLqibV0jDvD6IfRep3ib7AXmryg/640?from=appmsg "")  
  
网络安全完全零基础、小白能学吗？？？  
  
   在之前，我们课程本身是做直接实战挖洞，解决学员在入职挖洞、赏金挖洞、证书或公益挖洞的无法入手难题，所以是需要具有一定网安基础的，但是有些师傅零基础也想在我这边学习，完全没有问题，  
第四期直接赠送猎洞完全零基础课程！帮助师傅快速打好网安基础。完全零基础也可以学！  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup7QD5bp6d7vVCzpF7KtMULbGPmtFRGrhhlAyvvdAeoSnHnxI3rBAyAJNlAqNpialtyWv3xU4bjSJzwh7brH616p710HE6UYC5J8/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Uxiano3ib6ECceVUPW0lnfaN4byRTz3gV6nCTaK2ReZUUmSzKbQ6DgtZceUpnnj6JrMcRb3NY1gNTFeYXoYZHr9g/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XlDccKmwUxpdHwn9CAZQGzA7zhUXAWlPWqiaqgoX5mroSGLZz9d8lKOyiaIHibcOiajtiaBZ2fteBkSEXeUlCX2ZRMQ/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CRCWJpzeT1EnCOpghLqMn1pUdGSh92YplOib5UKrjeNicoaGtSKNXK63icibfzpufRbicGictnf2RBfHPOibXZSicibzm0A/640?from=appmsg "")  
  
上课形式和资源  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVSvuzvYiba0p67Qu5yqicmyyx6aBszyQ2OnrdeAARKPUEYGtWjOyGoc5JnjHzb8JFUwthnZlmlYHCh0WMogSzWw/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tTibAMib2Ruh2xpqvLTonQuSq625EZ7wEzCaLScjPQywlcicXJHLI2LTv6Q36BsICLqibV0jDvD6IfRep3ib7AXmryg/640?from=appmsg "")  
  
 我们上课是腾讯会议直播上课，都是晚上八点多之后开始，这个时间段无论是大学生还是就业人员都已经时间空闲可以学习，每节课都有录播，可以反复无限制学习。课程保证提供 直播、录播、课程课件、课程工具全部提供！  
  
同时还会额外赠送一个知识星球。  
  
  
课程课件：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup7mpL0c5CIkgVCUDzDtvIQywfa0b3Kzsk61r3CJKGKnAGSLa6aDBfvVmWERLls8aofEJFM6OibexSl7mn3Vicb6z8XCeFVAVoUmg/640?wx_fmt=png&from=appmsg "")  
  
  
课程录播：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup5ZF2PTgZZGxL7e5c1icKVE5IO0kcKOR2GoicvbHjFAyUB3Sgga1vPicuLtibBRZU6DsauS5A89tFuR4Y3rqzfDsua2TL3sHEWGzj8/640?wx_fmt=png&from=appmsg "")  
  
  
课程工具：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup4fujpuC0Y9G6rAnkv9YNPXjMGF3bANjYpU73SRbmLX6XxXZm0mKiaSEeUAV9Nt7ibxibicxMlNr56f2KuYoaibcrdFY1I8wooaTmzM/640?wx_fmt=png&from=appmsg "")  
  
  
赠送千人知识星球小圈子：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4AF9MtXRicCciaAtZs2lNIibpH3iadP8OcsKXmKYITU7wvgiakMVbu4WC2o6LYRFiclx3JGfd7297XQEuYkDpemCEQ9NicJKqmjg69Yc/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Uxiano3ib6ECceVUPW0lnfaN4byRTz3gV6nCTaK2ReZUUmSzKbQ6DgtZceUpnnj6JrMcRb3NY1gNTFeYXoYZHr9g/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XlDccKmwUxpdHwn9CAZQGzA7zhUXAWlPWqiaqgoX5mroSGLZz9d8lKOyiaIHibcOiajtiaBZ2fteBkSEXeUlCX2ZRMQ/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CRCWJpzeT1EnCOpghLqMn1pUdGSh92YplOib5UKrjeNicoaGtSKNXK63icibfzpufRbicGictnf2RBfHPOibXZSicibzm0A/640?from=appmsg "")  
  
最后结束语和价格  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVSvuzvYiba0p67Qu5yqicmyyx6aBszyQ2OnrdeAARKPUEYGtWjOyGoc5JnjHzb8JFUwthnZlmlYHCh0WMogSzWw/640?from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tTibAMib2Ruh2xpqvLTonQuSq625EZ7wEzCaLScjPQywlcicXJHLI2LTv6Q36BsICLqibV0jDvD6IfRep3ib7AXmryg/640?from=appmsg "")  
  
    课程价格为1888¥，一次报名可以永久学习、持续更新！包永久挖洞技术解答和入职解答，不会有二次收费。目前报名还有额外优惠，相信我，来到我这边可以知道，这个价格绝对是偏低的，更重要的是售后服务，全包技术挖掘和入职解答！  
  
报名可以保证之前讲过的课程录播，还有后续更新的新的一期都能永久学习。  
  
学员在挖洞时候的任何技术问题、入职时候的简历和面试等问题可以随时咨询我！  
  
报名可以可以直接加我下方微信，报名早的话还有一定价格优惠！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup5cEBENTmWaCicoEheEEFMjHR5KaD1I0Hj4brYkZq4uRSV6ZtXicz9k0SHdGVELFiaa3iaVt7hXbPr2Vl5ibTJibjEYtlNBQCE6HO5BM/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Uxiano3ib6ECceVUPW0lnfaN4byRTz3gV6nCTaK2ReZUUmSzKbQ6DgtZceUpnnj6JrMcRb3NY1gNTFeYXoYZHr9g/640?from=appmsg "")  
  
  
  
  
