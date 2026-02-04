#  EDU漏洞挖掘杂谈分享  
原创 zkaq-nnsae86
                    zkaq-nnsae86  掌控安全EDU   2026-02-04 06:50  
  
扫码领资料  
  
获网安教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1 "")  
  
  
# 本文由掌控安全学院 -  nnsae86 投稿  
  
**来****Track安全社区投稿~**  
  
**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  ）**  
# 前言  
  
EDU漏洞挖掘分享，主要是一些RANK上分技巧和捡洞方式分享，针对新手小白也可以挖出漏洞，只要会用工具就行，漏洞类型多种，没啥难度，纯分享，大佬勿喷。  
# sessionkey泄漏1  
  
这种漏洞是比较简单的，很多小程序都会有，并且不需要技术要求，危害却很大。  
  
某小程序，访问发现登记功能点，需要登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMee4mzaNjCn6PdEqKXgXSHhasUfofD789UTRyWBkA6BBM5lGudrByGGCQ/640?wx_fmt=png&from=appmsg "")  
  
登录口直接抓包，发现泄漏sessionkey和iv以及encrytedata信息  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKXNL5LdzJCiabu7419NMA22UxavBZvq8e9CB9u5IXvibia4EYegC5tXovZmAicg5ibeEmcDQlGfgEnvx0HFcRVlqR3Zv3w4R0WCWYE/640?wx_fmt=png&from=appmsg "")  
  
直接使用微信一键登录解密工具，成功解密，这个工具微信上有很多公众号都发不步了的，可以去微信上找找。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeesF6Ypia7zy5XvLwlllMjadicNm67ReRVIelOicHAuxN9RibFgDUJoTBCmA/640?wx_fmt=png&from=appmsg "")  
  
这里直接更改手机号然后加密回去在登录发包，成功进行任意用户登录。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeel70OkG9G9JicicRWB2e1jOJAwqEkHpEH2chzoMhEk50LK7WmpZmRiaalg/640?wx_fmt=png&from=appmsg "")  
# sessionkey泄漏2  
  
也是某学校小程序  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeice1zp9s658KbHlm2iaL7zNpWnOz4yL5qzGdsrN0uTp0GxicNdfZvKL0w/640?wx_fmt=png&from=appmsg "")  
  
登录抓包，发现泄漏iv以及encrytedata信息但是没有sessionkey却在phonekey字段有一串base64编码的字段，解密，里面存在sessionkey  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIeJGREJne6XfVrM3IreiaKvwKX5Hd9t1tSxKUUuMjiaNDiaB4b9iaJvl8Kth7QibD5DZogWCgTbcLolg1P3osVk5Mia3HpbwQvoUmwk/640?wx_fmt=png&from=appmsg "")  
  
解密成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeejo8swfdbKOH6vojIurDXibFs6uia8ib6BpTcHicucY4N8LGm8JibicDceKoQ/640?wx_fmt=png&from=appmsg "")  
  
直接更换手机号加密发包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeexiawXldCW6GnKW1Zs0TkPehxiaYubQvdaZLytVa06CbgO77jXQRksGyQ/640?wx_fmt=png&from=appmsg "")  
  
成功登录其他用户账号  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKLf4ZvrG9GcLUTd5YqugkduawtIic82cibXQAAIr3zkAYiaApHzs0uJ3jDYtsEbwdmLMoQp1ITBhqhl4hA7Deh4HPgpFdksVMtpA/640?wx_fmt=png&from=appmsg "")  
# 支付漏洞  
  
支付漏洞，这个纯捡洞，我都没有打开burp啥工具，就是随便点一下，发现可以充值，并且没有限制位数，因此可以冲0.019元，看看最后实际到账是多少  
  
ps:图片金额写错了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeemwbJDR0yutGwBt17UPlhdOZEdUWgZdggibPnfVj3XmtuYyqMYxs02Mg/640?wx_fmt=png&from=appmsg "")  
  
这里直接充值0.01元  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIQj091wyLSBj8NT67sLx7xrotezyrgql7XUry1JiaSkMuA1Zzh91ylg0MLPAUcR3FkWmMHZNicDL9aEwp77AibdENSerCE0AsUP8/640?wx_fmt=png&from=appmsg "")  
  
但是发现钱包金额为0.02元，成功拿下支付漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIU75ZL5MhVeJzBnYqNHw4WGicYzLAcAxadHx2gUmSvmWnvodP3PicSHv1SaJUibW3BvmbbYZzMy4ofypFWAKeGciclSrdgfR0UTMk/640?wx_fmt=png&from=appmsg "")  
  
还有更炸裂的，充值的金额可以申请退款，那这不就相当于捡钱嘛，如果你充100，最终退款200，你就白捡嫖 00，这个洞的危害其实挺大的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeekgiannNLTEtXpocgfSXA5oFwsT9MM7rZh4UDcA6ecQk1096H9sIKqbw/640?wx_fmt=png&from=appmsg "")  
# 任意账号登录  
  
这个漏洞其实也简单，登录账号需要手机号，但是该系统只有学校用户才能使用，因此无法登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeefjYYBKDxsfCn3biawAZsjpdPLUx5uF9WUluUKAFYhEBhpP9dL9hOjFQ/640?wx_fmt=png&from=appmsg "")  
  
这里通过抓包发现主要通过phone手机号进行登录操作，因此我们可以爆破手机号或者去信息收集拿到手机号，这里直接替换为校园用户的手机号  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMee7GBjnwEiapGkqrhPMwFbSGcEVIKbdVp8hHBTXCy25W0wk5okZOVWgzw/640?wx_fmt=png&from=appmsg "")  
  
发包，成功登录其他用户账号  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoK7zlyJBrlhfWfKTFputBtKEyj01KCN10ic0eJD8XyvtaWD2uD0l7MqnmbkCbUtaag1LLUVia1YLI91IbJ35S3ohHuy3HQuGTvzk/640?wx_fmt=png&from=appmsg "")  
  
里面有很多的用户信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeLqqhpTBOOp1vNQ43micSVwmVwTxv3THg3fyqhoeGicmiat1uDIeXxVtTw/640?wx_fmt=png&from=appmsg "")  
  
400+的手机号信息，相当于可以任意账号登录这400+用户的账号  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeZagrwCa87xd7FOHtDoFBxPUhMSVfoOyialy1UlyEBozkKkULicpHUJSQ/640?wx_fmt=png&from=appmsg "")  
  
这里又测试了另一个手机号，也是成功登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeePHkrpyPI9ggCEY2y3Sq5K72K2RNWPJSiaias8j5NR7ic9xhy2SCicR3lSA/640?wx_fmt=png&from=appmsg "")  
## 越权  
  
上述登录后发现某个学生账号，泄漏了身份证，手机号信息等，但是没有任何权限查看其他用户信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKIR15d6v3Hn3Yib3vougRCDyncPY8mk1youesDTzsyydxYjYDd7yRSv3dgqm0OmSeSIUeH7NGXle6iaYibbvQ3icmkO5FL5pu4wWU/640?wx_fmt=png&from=appmsg "")  
  
这里直接替换接口为上述查看所有用户手机号的信息，成功越权  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMee5CauCHvyn3Uhxz0l8VYxdabbWia8D2gT70xhoLZTF7PQoegL2WibZ8yg/640?wx_fmt=png&from=appmsg "")  
# 暗链  
  
这个洞我觉得性价比最高的，也是最简单轻松的，有时候走在路上或者身边没有电脑的时候随便找找公众号，服务号啥的点点说不定就有了。而且这个漏洞给rank3分，其实挺多的，一般的中危可能才2rank  
  
某公众号，点进去，发现两个功能，微xx和翼xx  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeKNTuNqgenSKYzqOBY0Pict2ozPNlMQUwrnnOPrdPRFmfQS6LmZgZzmA/640?wx_fmt=png&from=appmsg "")  
  
点进去发现是菠菜网站，这真是捡洞，这个是我在路上随便搜索公众号点一点就挖到了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoL3iazwG56urdvv8TmgnVle3fo0JsTcFApeia7RLZ28Y7LKYatNggW4jb6KTlW1jbt5yWGlGpYj2PLzULuOiclkQeHKBBeS0soSI4/640?wx_fmt=png&from=appmsg "")  
# 信息泄露  
  
还有一种漏洞spring信息泄漏，这种小程序很多，基本上就是burp一开，小程序点开然后随便点点功能点或者有登录口随便试下弱口令，burp插件会自动进行spring信息泄漏扫描  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeemQHoCVLY2GribdmZI7nQGJvOBLvc9xhLKo6W5nXOT2DfyVWt4aUuZnA/640?wx_fmt=png&from=appmsg "")  
  
这里也是通过burp拿下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeYJD0n2H2M13RPHj6W3EaBgs1npo5veIxujdg5Qkmw4ylJNnSXu8fhw/640?wx_fmt=png&from=appmsg "")  
  
这个也是一样  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeHdyjfdGs1FoyR1dL52dYxECPa7eiakDJpYubZhhvhnDKEbLe66yFJGA/640?wx_fmt=png&from=appmsg "")  
  
直接下载heapdump文件，不过这种漏洞可能很多都被挖掘过喽，大部分可能重复，但是你可以试试，说不定就有没叫过的呢？而且发现heapdump文件可以看看有没有弱口令aksk啥信息，说不定可以进一步利用也不一定，我这里就是发现里面泄漏了数据库密码，而且数据库开放在公网，直接进去，哪些数十个管理员权限账号，打包提交给了8rank  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeqBm4ib2Yt1cr21fklNl0ZwCLenRqPKYwojPIlroAQ4YMib9q3ySqGhnQ/640?wx_fmt=png&from=appmsg "")  
# 短信验证码缺陷  
  
这种洞也简单，都不用开burp  
  
某注册处，需要验证码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIf5WNZ8iafM0bGCdk9icpib0KQMnqpR7Vmh9ekxEXDToArUQrXDc7GmDjmOadUpmlmkcYJ4mDmA9OUBVMdQGdYW6D9icvTPrrCX8E/640?wx_fmt=png&from=appmsg "")  
  
验证码任意输入，长度，字符都不限  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKPIWmlnL6ZQicNRUIlIxuDHl6RE66A36zqFWSvTLcrRHQusibWWw3mkGsah4x06raD1UFjUZ0dWy5HbYdXAc4PvI5OJ6GrOvw1Y/640?wx_fmt=png&from=appmsg "")  
  
注册成功可直接登录，而且这个网站存在忘记密码处，经测试，同样有效。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeebGFfZvZGqencQyX8gAAyoL6frtDSYlK3CdgN1l4MGspneTEame5NRw/640?wx_fmt=png&from=appmsg "")  
# 逻辑缺陷  
  
这个洞奇葩，其实危害不是很大，但是也是第一次遇到所以给大家分享一下  
访问网站，输入手机号，发送验证码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeH22YoiboSm1wE52lZmhJ3ZyiaLHficu9aHq5TQbGJvOw6vAW6azopRmVg/640?wx_fmt=png&from=appmsg "")  
  
抓包，phone参数后面再拼接手机号  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeTpTKzAGc7ibsMqiaYTmWHCrSfiaYCn1QDJmIJgrfYQKLt9hQ2TNiaeMM9g/640?wx_fmt=png&from=appmsg "")  
  
验证码可以发现两个手机号均发送同样验证码，如下图：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeTFNZXSickgpBFGmKqNuUP7yxiay3Ph921EO551NnaoyiaXBRTCNhLicNQg/640?wx_fmt=png&from=appmsg "")  
  
但是我登录的时候发现这两个手机号都不对，就是比如使用A账号+验证码935539以及B账号+验证码935539都提示不正确。  
  
因此这里直接把手机号改为  
192xxx,134xxx，登录成功，发现个人信息处手机号变为了192xxx,134xxx。太奇葩啦。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeUamCVUa1bgV0Ed5WwpytkFb6NA9icjYraOYfpvJ8LaWVOfLwkia93ZkA/640?wx_fmt=png&from=appmsg "")  
## 短信轰炸  
  
而且通过测试，发现可以填无数个数组，且显示发送成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMee3oDz8Tv50zZ5ETfh0F7FWq8A0gOVRkHTc8shr1jTxnFiblZjaKBbb5Q/640?wx_fmt=png&from=appmsg "")  
  
多次发送请求直接造成短信轰炸  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMee46aL30Kic4q25eJHic0wz5pIZwtr0ibeu4dcEiaHX8QibSbpbA6yfic6ficEg/640?wx_fmt=png&from=appmsg "")  
# 积分刷取  
  
这里还发现积分刷取，这个比并发更牛逼，完全就是逻辑设计缺陷，点击首次登录会自动获取81积分  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLvicnoaGiaK4plUQ9TicR5NLDbpiaJ3OApnicrVFBRf1S6Eia3WUZPtmkcibEeI34lTicICydoLUPhmiaibZ4S7TwmQ4FYPsRabPanK9rwc/640?wx_fmt=png&from=appmsg "")  
  
然后可以完成任务，比如实名认证，评论，点赞报名啥的，可以获取更多积分，这里进行认证，直接把sourceType值改为2  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMee0QahQDRr28bgDL27XfGglWeph41AzO2aoPVJKSuXbUdOrxuZRsCibBg/640?wx_fmt=png&from=appmsg "")  
  
积分变为83  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeS1JNibcDT6pxpfma7l4Lf0Tia04j9TnoPibek1icJtdlK7Xic1btG4ZbBsQ/640?wx_fmt=png&from=appmsg "")  
  
多次发送上述请求包，直接批量获取积分。积分可以换东西，相当于一种变现了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcoGBW1ZSDiaTucbKoIMtvMeeAOwHNH0Zucic5bwCicQLwBJiaJVibxga8tcF7bTnnF3csToTENwhmXBSibw/640?wx_fmt=png&from=appmsg "")  
  
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，  
  
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34 "")  
  
**没看够~？欢迎关注！**  
  
  
**分享本文到朋友圈，可以凭截图找老师领取**  
  
上千**教程+工具+交流群+靶场账号**  
哦  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=35 "")  
  
******分享后扫码加我！**  
  
**回顾往期内容**  
  
[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)  
  
  
            [文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)  
  
  
[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)  
  
  
[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)  
  
  
[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)  
  
##     代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=36 "")  
  
点赞+在看支持一下吧~感谢看官老爷~   
  
你的点赞是我更新的动力  
  
