#  edu实战之框架漏洞  
原创 zkaq-lclccc
                    zkaq-lclccc  掌控安全EDU   2026-02-10 04:01  
  
扫码领资料  
  
获网安教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1 "")  
  
  
# 本文由掌控安全学院 -  lclccc 投稿  
  
**来****Track安全社区投稿~**  
  
**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn）**  
  
  
在 edu 挖掘漏洞的时候，资产的选择往往就是决定你能否挖到漏洞的关键，所以，web 资产挖掘大多数时候都是没有收获，这是我们可以选择小程序方面下手，而且我们可以选择一些职校或者专科学校，他们的资产往往更脆弱，这里我也是用这个思路找到一个职专学校  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJEAVcQoOicgFC7RhQQbZTmib53Ye0V4cff5WgaOG392GoVdeMLniaFywEiaCichgMwXfckibrFCHibbasUxnzlicpv174uIZuC0niabZOU/640?wx_fmt=png&from=appmsg "")  
  
这个小程序里面是没有漏洞的，但我通过数据包找到一个图片的路径，尝试看看能不能目录遍历  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJtvicia4U0IdgOnGXbjnKJ0ibpJxe2WYe4Pic0u8JQ0libF9lyicicDNnx9Mzl0epaY5fBjNfYbOf443RR5Watho3iaHmNkjQ5F8gicodU/640?wx_fmt=png&from=appmsg "")  
  
访问该 url 并且尝试删除路径，发现了 springboot 的经典报错页面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIyyzZxlzhezEsPUS6DTUec56NbOBIKdHJX1kw5u5gmJqjGuk9PTJn1LMhO3ChaPcd0aWtXhPFhGfe74WK9538nHmnmfl5AYk0/640?wx_fmt=png&from=appmsg "")  
  
这里就得试试看是不是有 druid 路径以及一些后台管理文档系统，这里放到目录扫描工具，果然不出所料，找到许多有用的路径  
  
1.弱口令  
  
 拼接/druid/login.html，使用弱口令 ruoyi/123456,成功进入后台  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLI0rPbOrO0zmwPu16zVqjfKfzG0RqKc0NmI3lcbWQSX5zkl3RbVpgv3aG5TYF8yHgPnOg3EPBPPfuJwhJnxOqgXzLx8YOkwQ4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKLqU6Jkqib9MiaXXw72GFpMBUAFiarDUWlTW8fia4mIe3aYaiaDXwOKQ6l4pcib2WUic3jDaSk7rib5ibWpeewycb4DzEc9DlBuEdTSReg/640?wx_fmt=png&from=appmsg "")  
  
2.未授权+敏感信息泄露  
  
拼接/doc.html，这是个若依管理系统的接口文档，接口功能可以正常使用  
  
点击获取用户列表并且输入请求体内容发送即可泄露管理员的账号密码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJ4qED4y9RlgItcm7bGzOUSG1uicK2muibFEGTnmsdWvHVzRNV2K10WFIKveMcWqIDtEz2rVnjtBO1Nser5NBgS66CNr1LHubb5Y/640?wx_fmt=png&from=appmsg "")  
  
请求体如何获取呢？在小程序中登录之后就会分配一个Authorization 给你，在 bp 抓包找到并且填进去即可  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoK3VgG3FmbxJY95V2Rn7v5JjibW0tbtEsAuNHeiccCygPfrzK8cZGCjibSRNWz0UcFfhtLnibNicagsFyPyNm11sb4vUc54D9uLlvGs/640?wx_fmt=png&from=appmsg "")  
  
3.敏感信息泄露+管理员身份登录  
  
拼接/login?redirect=%2Findex 路径，并根据上面得到的账号密码，成功登录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoK6O6kGWcT7ghq3Qx0CepZwgSeZibANUHBAUSsibmrkzdFcEibKibyYN9h4dt8dpbCWicYpvk3N3rxgPgnF4YVrqfwqDONPpTEGLBXI/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoK0ibEr8iaxDgV75lbwRme8RmY2bGGYuSeo7Dn0bPLsKNEUxZtZJuzpZJTzlwKwdnA3RWGUUzQsribcibgqTrqohFvEahcOTVY0lPI/640?wx_fmt=png&from=appmsg "")  
  
而且在一个功能处泄露了 1000 多名学生的身份证等重要信息  
  
  
最后，我想说的是能否挖到一个漏洞，资产的选择信息的收集也是一个关键  
  
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，  
  
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20 "")  
  
**没看够~？欢迎关注！**  
  
  
**分享本文到朋友圈，可以凭截图找老师领取**  
  
上千**教程+工具+交流群+靶场账号**  
哦  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=21 "")  
  
******分享后扫码加我！**  
  
**回顾往期内容**  
  
[我与红队：一场网络安全实战的较量与成长](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247550558&idx=1&sn=589aa46a61b9ab02ab953ccb9539b1d3&scene=21#wechat_redirect)  
  
  
[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)  
  
  
[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)  
  
  
[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)  
  
  
[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)  
  
  
[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)  
  
##     代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22 "")  
  
点赞+在看支持一下吧~感谢看官老爷~   
  
你的点赞是我更新的动力  
  
  
