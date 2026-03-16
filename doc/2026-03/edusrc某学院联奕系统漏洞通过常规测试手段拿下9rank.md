#  edusrc某学院联奕系统漏洞通过常规测试手段拿下9rank  
zkaq-takk
                    zkaq-takk  掌控安全EDU   2026-03-16 04:09  
  
扫码领资料  
  
获网安教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1 "")  
  
  
# 本文由掌控安全学院 -  takk 投稿  
  
**来****Track安全社区投稿~**  
  
**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  ）**  
  
  
开局主包通过弱口令进入系统，首先第一件事就是看教务系统有没有敏感信息泄露  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIXhPvqwV6kIK0EBa59LxkdqGaUW3rwuYLJltfmPfRxLdN2oXVapftFMPRMYKaJgpbJUy0yfP3YcrYfIpY56U0y354qPeXjHTw/640?wx_fmt=png&from=appmsg "")  
  
进入个人信息详细页看看 有没有 sfz 泄露  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKZwwL9VAaGz0ziblcvfqh619SzMBtEbJsna0YAsusRo4CPrZD1GPnHY04XXHIyYKAKfnNa16vbAJWqw2iaBVCiamtwb8VSMAnHfM/640?wx_fmt=png&from=appmsg "")  
  
很可惜个人信息详细里的 sfz 是打码的（难道连 1rank 都拿不到了吗 bushi，于是主包便每个功能都尝试一遍看能不能发现越权啥的  
  
  
最后在学生家庭信息发现了越权，只需要修改 xsid 即可查看他人家庭住址和联系人手机  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIZrK3tg93hQ0P1icyZicSpIYae8N8dBrst4PSXNlf7EdW8Jibkw0aSDddn3sRhRud7qRbnB3cnMpkQ2LaDTkIDgcPapNgT7pyI4E/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJtbEztj9UiahynUV7cBpfEqdbYicryeDgnzThLTGtsHgrBnbbDtvjjTJVIlRTK7RzVAe0xWMKsoicqxvX8pCKn9uDMUQG7BVh29k/640?wx_fmt=png&from=appmsg "")  
  
在主包不断尝试下又发现学生获奖申请功能存在 sfz 泄露  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJMZtNmqnyicgZVlzZ1eaZx7C08sxWlNlic7Vhfx0YYC1RcpjqI6bjaUFXH6Y7RuWjcslmVj6JZlCfbPOP11f4rkVxia5okWuBt38/640?wx_fmt=png&from=appmsg "")  
  
通常情况下添加的信息中，sfz 也是打码的但是我们直接抓接口的返回包可能就不打码了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIot4LNuAtc8veYfcRqq8At5PITBbRsTibLXx0IIFkxia3oONecV6IVKg95D8nRBM5cZ6eMGAibGibClAQdicXa20t1SiaAXlrZV2kac/640?wx_fmt=png&from=appmsg "")  
  
这里也是正常回显完整的 sfz 了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLu9oVXEX3rHWKPEmSZbYGWkLMTWQ4vVptjXOfCjfvzX9TqRg4tA4k51wDicOzgsrK4rW9JibTtLfzWaApA7ibTRt1m8icib94RhQxA/640?wx_fmt=png&from=appmsg "")  
  
在主包的火眼金睛下也是发现了测试用的账号和 sfz  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL2cfUuGZPJOIeH75gcONIRt6o2Hnarxn04Ku5vHMVJf1u9SjLdDU7iao2ickYX6N7e59JTAs1Z8h74Ae7QbAWqWRtqMQpu0KUv8/640?wx_fmt=png&from=appmsg "")  
  
直接弱口令登录管理员账号，后面能干的事就多了，点到为止  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIpe4icOXGjqo7qwkwk6LbNBGJITF8aNOchzicDgV13p1Jwl1vic9cjEtgWwe3Sgjm3k6Hhhw45GNKnibUSzzwJQf78HnBTnk8Itek/640?wx_fmt=png&from=appmsg "")  
  
也是成功拿下 9 分  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKW5c0qqyibcXnSdqQVH8ZCtOd5o3ibjngtdwC5glCViaAtkxnGodszmmYpeBG1zC7Q3uN3kkc8BVH1nDEsFLCB5U7y8q79ibYySL4/640?wx_fmt=png&from=appmsg "")  
  
总的来说难度不大，也是给挖不到洞的兄弟打打气吧，坚持挖下去肯定出洞  
  
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
  
  
