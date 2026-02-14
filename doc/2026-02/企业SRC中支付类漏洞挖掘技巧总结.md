#  企业SRC中支付类漏洞挖掘技巧总结  
中铁13层打工人
                    中铁13层打工人  神农Sec   2026-02-14 01:03  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。  
#   
  
文章作者：  
中铁13层打工人  
  
文章来源：  
https://forum.butian.net/share/2778  
  
01  
  
0x1   
企业SRC中支付类漏洞挖掘技巧总结  
## 前言：  
  
支付类逻辑漏洞在漏洞挖掘中是常常出现的问题之一。此类漏洞挖掘思路多，奖励高，是炙手可热的漏洞。此篇文章主要围绕挖掘支付逻辑漏洞时的一些思路分享。  
## 支付逻辑漏洞成因：  
  
支付漏洞可能由以下原因造成：  
1. 前端验证不充分：在前端页面上，没有进行足够的验证和限制，使得用户可以通过修改页面元素或发送自定义请求来篡改支付金额、支付类型、支付状态等。  
  
1. 客户端数据不可信：客户端（如移动应用）在进行支付时，没有对传输的数据进行完整性验证和加密，导致恶意用户可以直接修改数据包中的支付金额、订单号等与订单有关的参数。  
  
1. 服务器端验证不严格：支付请求在到达服务器端时，没有进行足够的验证和校验，使得攻击者能够更改支付相关参数并绕过服务器端的验证机制。  
  
1. 不安全的存储和传输：支付金额数据在存储或传输过程中未经适当的加密保护，导致黑客可以窃取或篡改数据。  
  
## 支付逻辑漏洞挖掘技巧：  
  
在实际漏洞挖掘中，一般最先尝试的就是更改数据包发包内容，可以直接修改支付金额、更改支付状态、更改支付类型、更改提交订单支付的时候其中的订单信息等等，当然也会有一些新奇的功能点可以测试。这些在测试中会遇到的操作可以分为以下几类：  
#### 一、更改支付金额  
  
在支付流程中，可以修改支付价格的步骤有很多，包括订购、确认信息、付款等。在涉及到价格的步骤中都可以尝试修改，如果网站在某一环节存在逻辑上的漏洞，就可以利用该漏洞对支付价格进行修改。可以直接修改提交订单中的价格字段，一般可尝试0.01，1.00，1等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXDbNEW3Z3NKDe2MUncWzT2dPqV4s92toiaxa1YwfVCh5z4vAxDxKpmBVLwJec2glaf8BnDpB19eQpIkIgT6ic3m8RFdN2ibBUy0g/640?wx_fmt=png&from=appmsg "")  
#### 二、更改支付状态  
  
在测试中有的时候订单得支付状态是由用户提交订单时的某个数据包参数决定的，服务端通过支付状态判断订单支付与否，这时我们可以尝试找到这个参数（可以通过正常支付订单的数据包进行对比），对支付状态进行修改。或者还有一种情况是通过检查订单是否支付，这个时候可以通过抓取已支付的订单数据包将其中的订单编号改为未支付的编号，实现绕过。  
  
1、直接修改为已支付状态  
  
2、修改未支付的订单号为已支付订单号  
#### 三、修改支付类型  
  
通常在提交订单付款时，这里的type一般是对支付方式的判断，可能会存在开发人员测试的时候遗留的无需支付的type值，根据支付方式判断支付与否。可以通过fuzz特定值去实现绕过。比如比较常见的值0（这里需要结合实际进行测试不同的处理方式type值不同），可以实现不需要付款订单就会自动生成。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QX8bqzRfrDvmZ7KD2hyy3mEVBtZL2jpiaO93lD3xQGoy1zAtKqHb5mj3QxCZIic5vPLxMl7BiajniazM2N3PXM8EaBXsSjIJ5ya910/640?wx_fmt=png&from=appmsg "")  
  
#### 四、更改订单信息  
  
服务端只检查支付是否完成，并没有确认订单金额与银行支付金额是否相同，过分信任客户端提交的数据。此时可以通过替换支付订单号、更换商品id的方式，来完成花少钱买更贵的东西。同时生成两个订单号，一个贵的一个便宜，首先支付便宜的，银行往回返回的时候，替换订单号，然后就可以完成两个订单的同时支付。  
  
常见位置在生成订单、生成支付链接等。  
  
1、修改商品编号  
  
直接在生成的订单中替换商品编号。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWOAOSLeK0o5OmOAIEpiaR4icREvDia7vADRZWFtKHQgiaEPBRwd6NNYFTldpWricwqhL8mZdIfReL7MDaNRDLCxXLKib2KNA2UWGeN4/640?wx_fmt=png&from=appmsg "")  
  
  
2、修改订单号  
  
将金额不同的订单进行替换，可以支付一个金额较少的订单，然后将订单号修改为金额较大的订单，少付实际金额。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVXib4Dlt9IDticKAQ6myJic90TndTNnpRGVKlrEvBzCc6hDwMeW5FHkwEg0m8iaEqhSibVor5WqGfunh1UhJtWphQ5ib7RaLvM30O8M/640?wx_fmt=png&from=appmsg "")  
  
3、越权使用他人优惠券、越权使用他人积分等  
#### 五、更改数量实现优惠支付  
  
支付金额是由购买数量乘以商品单价决定的，这时我们在数据包中修改购买数量，将其修改为负数或者小数，如果站点后台对此没有进行过滤，就有可能存在支付漏洞。  
  
1、将正常的数量值修改至最小值0.01，可以实现低价购买。比如：原价300修改修量为0.01后实付金额变为3。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXojs9tT0Wo0zss5f1p4cnu3xYuat99of3BD1rftlK9eB5FlO8oLBXP1IPfjfx9oeQpJxwkFiblChicxVOXaXbMIXWS4wAJfBv84/640?wx_fmt=png&from=appmsg "")  
  
  
2、未对负数做检验的还可以将数量改为负数。（这里需要注意，因为后端大部分会校验不允许实付金额小于0或者0.01等，所以有的时候要想实现订单成功生成需要结合实际修改价格）  
  
生成订单时有参数表示商品数量，修改为-1  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUxFnko52SWUomAX8ibCcKDmqP7ek6k19icTZcXhZUiaqFxby2Tm6ibfr9nkib6rnf9nkOa2e3ibpTkG06UOicm4HxN6Z7tasAUWERcuQ/640?wx_fmt=png&from=appmsg "")  
  
  
修改数量为-1后会发现，此时金额为负数。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUugeeB9std1X7gQz9Cf9yibe6ramTxycoXefhl1fd12ruZ02LbTVWpWYxJa9pm1yq3E7QOCg0peibmibpSEsKYPsRTQj40zEtcb4/640?wx_fmt=png&from=appmsg "")  
  
  
在提交订单支付的时候，为保证支付成功需要修改金额。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV2LIUm1tygLPuU9SctmnzXu8Gzlxf4UulpLhvCibWpY00W9ZUMHO4uMDpEmIOXospQZUcKnicgmZGyOggjJRmvVd1lkxNp8GmbU/640?wx_fmt=png&from=appmsg "")  
  
  
3、对数量没有做负数校验的时候也可以巧用负数抵消实现0元购  
  
在计算价格时，没有对负数进行验证，通过修改某个商品数量为-1实现与1的抵消实现0元购。  
  
同时购买两件商品，修改两件商品其中价格低的商品的金额为负数，实现价格的抵消，低价购买商品。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUzm2kyt0nLpadsUSfysSNic5czDEYzhIrWsnuBt1sI2MVp7Z8nzNibbqTf7dqNdUMzuUggmAdJ9Exzyn3C03DSvJv1urr6TWc8M/640?wx_fmt=png&from=appmsg "")  
  
  
4、手动增加订单中商品相关的多个参数以达到少付多买的目的。  
  
有的时候在提交订单时抓取数据包可以看到只有一套商品的信息，尝试多添加几套同样的参数订单是否会有变化。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUyibYk8RFpTcvCFd5vQjC0icFnP4c35Kzn7cYyCutvdv6XFgWwyPKvw4kqnfST0xb3eshJBsMdbjN4cHB9XuZvicZnzNvAfPGJj8/640?wx_fmt=png&from=appmsg "")  
  
  
尝试在提交订单的时候多添加几个此类参数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QW80O04vNK06ibDmKt8vTQ3mRhzkoTorEjpxa4fle3BvCibjheyIoE5SOAQVXUIIjCKIoOJfOauGCMeOgvEHmk9SDtHQJkb9uFQ4/640?wx_fmt=png&from=appmsg "")  
  
  
提交订单实际支付金额未变仍是一个商品的价格，但是实际套餐已经变成了四个。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVZIf92dUkr8jKo7XvpRB8NonfzAb3tneu13aDwwQ89RMgSyTArGice4ib0xnG0g8kBGh5eQibPbgmguVIUJAyqpucYe9g0SYMta4/640?wx_fmt=png&from=appmsg "")  
  
#### 六、重复支付，突破限购  
  
在支付系统中，服务端没有做好相关验证，比如订单状态被错误更新或者未更新，未对订单多重提交进行校验。那么就可以并发订单实现优惠订单多次提交。需要注意的是这里有的时候会根据实际支付订单判断，并发了多个订单也可能只有一个优惠订单可以正常支付。  
  
并发订单，多台设备同时提交优惠订单。  
  
常见于限购，一个账号仅许购买一次等  
  
1、限制一个优惠订单时直接并发生成多个优惠订单  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWpMGzqcS2HqMyuWhZX2gj6OHondecmsmdQtnawicXfzRCFRXGr3e2zrhnzW2BxTrYRSy71asO08rTSQra6cMuMCy3vXA75IXyQ/640?wx_fmt=png&from=appmsg "")  
  
  
2、使用多台设备、多个浏览器、多种支付方式（wx、支付宝等）购买优惠订单  
  
常见于购买会员，会员第一个月往往会有优惠价。生成一个优惠订单后不支付，打开多个设备或者虚拟器设备，同时提交生成优惠订单，再分别支付，有的时候会发现会员截至日期顺延，突破限制以优惠价格购买会员。  
  
3、退款处并发。退款的时候可以发起同一订单多次退款，达到多退款的目的。  
#### 七、优惠券多次使用  
  
常见于涉及优惠券的订单中。可以在提交订单的时候修改发包中优惠券的值尝试使用大额优惠券，或者按照原数据包中优惠券的构造参数手工添加几张优惠券，达到优惠券叠用的目的。有优惠券面值参数的也可以直接修改数据包中优惠券的面值。  
  
1、在一个订单中叠加使用优惠券  
  
2、修改优惠券标识，尝试使用其他商品中的大额优惠券  
  
3、直接修改优惠券的面值。实际金额计算会扣除优惠的部分，此时修改优惠券面值可以实现低价购买。  
#### 八、遍历隐藏或者下架优惠id获取优惠链接  
  
漏洞常见位置：会员处、商品处（隐藏商品，已下架商品，开发测试低价商品等）  
  
1、遍历隐藏优惠券  
  
一般会有一些开发时测试的大额优惠券，或者已经过期下架的优惠券，通过遍历可以被使用。  
  
2、遍历商品id从而fuzz到已下架的商品  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXv0xtcibBB2c1autsXMxGog7Qrun88v2wDMDvQhEtibFlrWjbMzT9yOP1RZDdVDjlDeBU3ylW9kZtbwLiavJiaPVcq8jJjP8thPkM/640?wx_fmt=png&from=appmsg "")  
#### 九、利用小数点精度四舍五入  
  
0.019=0.02（比如充值0.019元，第三方支付截取到分也就是0.01元，但是系统四舍五入为0.02）。  
  
02  
  
0x2 课程背景  
  
哈咯，各位师傅们好久不见！  
神农安全内部小圈子从  
2024年开始搞起来的，到现在也已经有小一两年了，期间承蒙各位师傅们的  
关注和支持  
💗  
非常感谢大家。  
  
「神农安全」知识星球目前已经  
累计1600+网络安全爱好者的加入，在这个过程中收获到了很多师傅们的  
好评与鼓励  
🎉  
，  
内部小圈子：一个知识星球+内部小圈子交流群+知识库。一直一来价格都没有超过50（都给师傅们发优惠卷），基本上加了小圈子的师傅都会说一句——  
“  
这圈子加的真值啊  
”。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthLEynEQtMibH6uWjBva44EEEkCx8bX12KA8gsZKQlllwGfyAEiaDHqY8g/640?wx_fmt=other&from=appmsg "")  
  
我平常呢也特别的爱  
分享技术文章，特别是每当学习到一个新技术，我都会去详细认真的写一篇对应的博客文章进行发表。  
活跃于先知社区、FreeBuf、奇安信攻防社区、知乎与CSDN等技术社区，id：  
一个想当文人的黑客，累计发表   
500+篇原创技术文章。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthlexDYBvDy8LwERVHKlbb7086Gm5KFIV78taz23NJicAWpDYA9T4svTA/640?wx_fmt=png&from=appmsg "")  
  
发表的公众号文章也从来没有设置过  
付费模式，哪怕一篇文章写个一个星期左右，好几万个字一篇的文章也都向来如此。喜欢看我写文章的师傅们都知道我写的技术博客文章：要有  
实战案例截图+详细知识点汇总，所以这样也是吸引到了很多师傅们观看我的文章，也是一年时间迅速在网络安全的圈子里面发展了自己的  
内部小圈子  
（成绩也不错）  
🎉  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWX3SIic6S4hEtLspuFkYL0w3LaPPsV0u8gXdAC0wuz2xobUIMR9ibfrkKzsgBQ1keNgnuMo3aXuO1ibQ/640?wx_fmt=png&from=appmsg "")  
  
后面也是小圈子做大起来了，师傅们也都喜欢看我文章，想让我开课教下思路，所以想着自己花时间做了  
 ✨  
课件和课表，都是纯自己手搓的，大家也可以看下课表的内容，**课程价格目前是325**  
（后面也会随着人数越多，涨价）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWX3SIic6S4hEtLspuFkYL0w3c0V9SHia9KaMfIRkaRLia8mhrxjITkWvU6UJuibbGmrHe9La4CK96XUeg/640?wx_fmt=png&from=appmsg "")  
  
  
不是小圈子的师傅们报名成功再送内部小圈子（知识星球）一个，都有对应的  
专属微信群聊  
 ✨  
。  
  
一周1-2节课程，**直播+录播形式**  
，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课  
  
目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的  
  
上课结束后，会把**视频录播+课件笔记**  
一起打包发直播群  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthM2sjuWQFbmvWv79V058KwI0DswFF9LysewGtULj81Vp5bX9nTEK78A/640?wx_fmt=png&from=appmsg "")  
  
03  
  
0x3 课程特色  
  
课程  
主打真实，  
一线SRC漏洞挖掘师傅是如何学习和挖掘SRC漏洞的，让你真正了解SRC漏洞挖掘，助力在岗人员和大学生的能力提升，掌握新的技能树，为下一次  
跳槽涨薪做好准备。本  
课程内容覆盖企业  
SRC、众测项目挖掘、护网HVV红蓝攻防技巧、CVE、CNVD、EDUSRC等平台通杀案例技巧挖掘方法。  
  
本课程  
适合人群  
（光看不挖啥也不会）  
```
1、想从0转行入行的大学生或自学者
2、想从CTF比赛/Web或SRC进阶到项目实战的选手
3、想参与项目/找工作/提高收入的转型者
```  
  
课程价格：325元  
  
报课成功的师傅们直接免费送内部小圈：一个知识星球+内部小圈子交流群  
```
1、课程价格真心实惠，绝不割韭菜
2、两三百的课程价格让你体会大几千的培训课程内容
3、带着大家从0到1，本人上课坚持手搓课件（实战案例+知识体系）
4、拒绝使用PPT演讲模式（无实操，很枯燥）
```  
  
直播培训教学方式  
  
课程  
一周1-2节课，课程特色涵盖直播多人上麦活跃回答，直播过程中有问题随时解决或私信我。  
拉微信群：一个知识星球内部小圈子交流群+课程培训直播通知群。有项目/工作/护网第一时间内推报课的师傅，  
一对一简历优化，助力在岗人员和大学生的能力提升。  
  
一次报名每期均可永久学习，并且赠送内部「神农安全」知识星球，一对一永久解答、无保留教学！  
  
欢迎关注微信公众号：神农Sec，报名咨询添加微信：  
routing_love  
  
课程均为线上交付，报名成功后  
不支持退款  
  
内部小圈子  
（知识星球+内部小圈子交流群+知识库）  
  
对内部小圈子感兴趣的师傅们也可以看下下面的这个  
跳转链接，里面有对小圈子的详细介绍，报名课程成功的师傅们直接免费送一个（直接点击下面直接可以跳转）。  
  
[强烈推荐一个永久的SRC挖掘、渗透攻防内部知识库](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247501608&idx=1&sn=5eb836122ac222ca9767a7bbc3c4521b&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltth4VWMmSt5ZBYAUuNNGuEjU3tvKRAN0yqMTPSnzKxibReCfiaFGibLxdAYw/640?wx_fmt=png&from=appmsg "")  
  
讲师介绍  
  
id：一个想当文人的黑客  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthqvGuVSjkR43eeaNibf1KbGU4nia5ibXFYpTBFeAbQewTq43IqJHIMhhhg/640?wx_fmt=png&from=appmsg "")  
  
欢迎关注微信公众号：神农Sec，报名咨询添加微信：  
routing_love  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
04  
  
0x4   
第一期挖洞培训课表内容  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVMibw6HiaoHUxJgNHUVfqCicbGSauW0QQBjLcC9H4gdOEyW3ZzLjTfyYibqGdaSueO9GDbbyicmckia2Kg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**内部圈子介绍（报课赠送）**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
  
**圈子专注于更新src/红蓝攻防相关：**  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、知识星球专属微信“小圈子交流群”
3、微信小群一起挖洞
4、内部团队专属EDUSRC证书站漏洞报告
5、分享src优质视频课程（企业src/EDUSRC/红蓝队攻防）
6、分享src挖掘技巧tips
7、不定期有众测、渗透测试项目（一起挣钱）
8、不定期有工作招聘内推（工作/护网内推）
9、送全国职业技能大赛环境+WP解析（比赛拿奖）
10、十个专栏会持续更新~提前续费有优惠，好用不贵很实惠
11、每日内部资料分享，内部圈子资料1000+
12、联系圈主获取：内部漏洞知识库+圈子使用手册+内部圈子交流群
13、VX：routing_love，技术交流+疑问解决
```  
  
  
**内部圈子**  
**专栏介绍**  
  
知识星球内部共享资料截屏详情如下  
  
（只要没有特殊情况，每天都保持更新）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibRSekfPpgmzg6Pn4yH440wEZhQZaJaxJds7olZp5H8Ma4PicQFclzGbQ/640?wx_fmt=other&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibgpeLSDuggy2U7TJWF3h7Af8JibBG0jA5fIyaYNUa2ODeG1r5DoOibAXA/640?wx_fmt=png&from=appmsg "")  
  
**知识星球——**  
**神农安全**  
  
**知识库部分大纲目录如下：**  
  
知识库跟  
知识星球联动，基本上每天保持  
更新，满足圈友的需求  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFhXF33IuCNWh4QOXjMyjshticibyeTV3ZmhJeGias5J14egV36UGXvwGSA/640?wx_fmt=png&from=appmsg "")  
  
  
知识库和知识星球有师傅们关注的  
EDUSRC  
和  
CNVD相关内容（内部资料）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFKDNucibvibBty5UMNwpjeq1ToHpicPxpNwvRNj3JzWlz4QT1kbFqEdnaA/640?wx_fmt=other&from=appmsg "")  
  
  
还有网上流出来的各种  
SRC/CTF等课程视频  
  
量大管饱，扫描下面的知识星球二维码加入即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFxYMxoc1ViciafayxiaK0Z26g1kfbVDybCO8R88lqYQvOiaFgQ8fjOJEjxA/640?wx_fmt=png&from=appmsg "")  
  
  
不会挖CNVD？不会挖EDURC？不会挖企业SRC？不会打nday和通杀漏洞？  
  
直接加入我们小圈子：  
知识星球+内部圈子交流群+知识库  
  
快来吧！！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJ5wUOL9GnsxoXibKezHTjL6Yvuw6y8nm5ibyL388DdDFvuAtGypahRevg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJO0FHgdr6ach2iaibDRwicrB3Ct1WWhg9PA0fPw2J1icGjQgKENYDozpVJg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
神农安全知识库内部配置很多  
内部工具和资料💾，  
玄机靶场邀请码+EDUSRC邀请码等等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDNtEt0PfMwXQRzn9EDBdibLWNDZXVVjog7wDlAUK1h3Y7OicPQCYaw2eA/640?wx_fmt=png&from=appmsg "")  
  
  
快要护网来临，是不是需要  
护网面试题汇总  
？  
问题+答案（超级详细🔎）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDbLia1oCDxSyuY4j0ooxgqOibabZUDCibIzicM6SL2CMuAAa1Qe4UIRdq1g/640?wx_fmt=png&from=appmsg "")  
  
  
最后，师傅们也是希望找个  
好工作，那么常见的  
渗透测试/安服工程师/驻场面试题目，你值得拥有！！！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDicYew8gfSB3nicq9RFgJIKFG1UWyC6ibgpialR2UZlicW3mOBqVib7SLyDtQ/640?wx_fmt=other&from=appmsg "")  
  
  
**神农安全公开交流群**  
  
有需要的师傅们直接扫描文章二维码加入，然后要是后面群聊二维码扫描加入不了的师傅们，直接扫描文章开头的二维码加我（备注加群）  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mcko8AHj6QWiaPriaTftDaibbN8h7yh3sfEQxsI9gdmdcDCaQEeNJ8fkWial36juNDPyyN6LedicicryhWNaicicNYW4HicIibbD9l8ffuQaLkUx6biaiao/640?wx_fmt=jpeg&from=appmsg "")  
```
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif "")  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic "")  
  
**往期回顾**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic "")  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[手把手js逆向断点调试&js逆向前端加密对抗&企业SRC实战分享](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247495361&idx=1&sn=48283073b325e360823da8dec27a7508&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[浅谈src漏洞挖掘中容易出洞的几种姿势](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247489731&idx=1&sn=c3a5ef01648fad496ecda36b653b6e21&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[HVV护网行动 | 分享最近攻防演练HVV漏洞复盘](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247488672&idx=1&sn=493bb70011a02eb971ff1b74c733f1d9&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[攻防演练｜分享最近一次攻防演练RTSP奇特之旅](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247492377&idx=1&sn=a94ad30e30e08bd96e888dad744e9814&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[JS漏洞挖掘｜分享使用FindSomething联动的挖掘思路](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247492315&idx=1&sn=88991e98058a277e267a9a79b8518e16&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[渗透测试 ｜ 从jeecg接口泄露到任意管理员用户接管+SQL注入漏洞](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493292&idx=1&sn=611fd43361089a30e5f7bcda21274b95&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[分享SRC中后台登录处站点的漏洞挖掘技巧](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247485439&idx=1&sn=3fd7e4cef57edca8e73104f8af38fc05&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[企业SRC支付漏洞&EDUSRC&众测挖掘思路技巧操作分享](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247492839&idx=1&sn=b9781f60580c1da8e2151166f0494ba5&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[渗透测试 ｜ 分享某次项目上的渗透测试漏洞复盘](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493495&idx=1&sn=791bebc6faa651cc3c585c2f5f481d21&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[【宝典】分享云安全浪潮src漏洞挖掘技巧](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247494877&idx=1&sn=2d00c0f651fd7375e881be86638e53ce&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[实战SRC挖掘｜微信小程序渗透漏洞复盘](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247494468&idx=1&sn=f0da4b4ff7763cbb83b858fb5a8964f9&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[综合资产测绘 | 手把手带你搞定信息收集](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493749&idx=1&sn=d2e0febcdcf9dcd8aa44be0d43b51936&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[【宝典】针对若依系统nday的常见各种姿势利用](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493489&idx=1&sn=d3ef10a1ae3b8c161d7174cb42702fac&scene=21#wechat_redirect)  
  
  
  
