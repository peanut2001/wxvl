#  EDUSRC-高危漏洞-从信息收集到后台多个越权漏洞  
原创 神农Sec
                        神农Sec  神农Sec   2026-02-27 01:53  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。  
#   
  
  
01  
  
0x1   
EDUSRC-高危漏洞-从信息收集到后台多个越权漏洞  
  
0x1 前言  
哈咯，师傅们！好久没有在平台更新文章了，最近想着把之前EDUSRC的修复的一个高危漏洞给师傅们分享下，然后这里也不希望师傅们进行一些非法测试，有时间可以去多试试挖，然后最近这两年比较火的小程序漏洞建议师傅们看看。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXVibn6GLacmLGDDxvBpUaw8kRs3mJ1YiaN9ibebfEEU0mhmZ0B3U3gPV4Q/640?wx_fmt=png&from=appmsg "")  
  
这个漏洞主要是前期的一个账号密码收集，因为有了账号密码能够进入后台，后台的很多功能点我们才可以进行测试，特别是后台的越权漏洞。然后关于账号密码的收集，具体可以看我之前在社区平台写的 一些文章（大佬勿喷）。  
  
## 0x2 信息收集  
### 一、猜测注册接口  
  
这里说的信息收集，我下面会结合之前在社区平台分享的文章一起来说，因为之前的写的蛮详细了，就不再多说了。关于进行EDUSRC的测试，很多师傅问我要是没有账号密码怎么办，web前台登陆不进去是不是就寄寄了呢？  
  
  
我想说的不是，其实你账号密码是可以通过信息收集去拿到的，但是要是没有拿到其实问题也不是很大，因为学校的系统很多，站点不止这一个，有些系统，都是可以注册，但是有些系统可能说注册接口被隐藏了，举个例子，前段时间大火的若依系统，其实是有注册接口的，但是很多都会被开发给隐藏了，这个时候可以进行接口拼接。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaX4t4h8TtNseDpKdU3gSCLLljfCGPaSTDJ4meX5A3l1JCLIkFk98lIQQ/640?wx_fmt=png&from=appmsg "")  
  
  
通过在 url 中直接添加/register 或者在 js 中进行寻找”register“ 成功进入到注册地点。  
```
/register/register.php/register.jsp/register.html
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXhv180kX2bl2NBalXibiavNA8ptIsCqiazcmYnLUaMLMbos58VYNNYg0BA/640?wx_fmt=png&from=appmsg "")  
  
  
还有就是很多人会遗忘的js代码，建议师傅们没有思路了可以看看这里，有些开发也会把账号密码写在js里面，方便自己查看，然后这里也建议师傅们可以去学习下JS代码审计、加解密之类的，各种断点、调试操作。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXnJ2b53pXrjbWLo5OBh8nQibZMphwzNcbP3BECIWArN1PCIO4oXSuVqw/640?wx_fmt=png&from=appmsg "")  
###   
### 二、各种信息收集打法  
  
这篇文章主要是就是分享通过奖学金名单泄露学号，然后去看那个系统登陆页面，有没有那种账号密码提示，有些默认账号是学号，密码都是一样的初始化，比如：学号@abc等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXzSe8vhtf3hW5NyFFBKFofMCG9kvjJaBJTUIFrUrAFic47uXW6zAEEzA/640?wx_fmt=png&from=appmsg "")  
  
  
师傅们可以看到，像国家奖学金的公告都是之间公开的信息，像师傅们平常不知道怎么进行检索学号时，不妨可以使用这个非常简单，且很好用的方法进行一个学号检索  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXuO5vSG1sWtibNBn4XP16X3F0QWD3xSYYHBoxDQ2vqWZA60NdAcicJ6kg/640?wx_fmt=png&from=appmsg "")  
  
  
通过一些Google语法或者一些操作，可以找到网上泄露的敏感信心，比如：xh、sfz、xm、sjh等  
  
这里给师傅们附上一些好用的Google语法  
```
1.site:域名 intext:管理|后 台|登陆|用户名|密码|验证码|系统|帐号|manage|admin|login|system2.site:域名 inurl:login|admin|manage|manager|admin_login|login_admin|system3.site:域名 intext:"手册"4.site:域名 intext:"忘记密码"5.site:域名 intext:"工号"6.site:域名 intext:"优秀员工"7.site:域名 intext:"身份证号码"8.site:域名 intext:"手机号"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXoGcG8PKz04t9jP4ianbJ5AN5lDctWbl9Kz2Iiara9Aiajs9Dibwribtqibcw/640?wx_fmt=png&from=appmsg "")  
  
  
很多种挖掘EDUSRC时的一些信息收集方法，建议小白师傅可以多看看。  
  
当然你也可以加入班群，表白墙等容易泄露信息的地方。（如果你语雀玩的好，你可以通过语雀去查找重要信息）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXzmc9R0fKtARj4IvsZpNck3YxOEgoLxU704E2OpZticOickNhmOPdGCZA/640?wx_fmt=png&from=appmsg "")  
  
  
包括使用抖音平台，可以去检索某某大学录取通知书之类的信息，很容易可以找到该学校的一些用户信息，比如常见的学号和身份证号，都是可以收集的，然后对于某些大学的门户网站，是不是可以进行渗透一波了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaX9F8FqgWSkTsn2XRrQJPfr2z7Ks7QbKT1eCNcedoYG8eAMvtY38fvPQ/640?wx_fmt=png&from=appmsg "")  
## 0x3 渗透测试思路  
### 一、弱口令泄露敏感信息漏洞  
  
这里我就是先按照上面的思路进行收集，找找泄露的账号密码、学号、身份证信息等，然后通过猜测密码进行弱口令登陆，找到系统登陆后台，可以多尝试几个系统  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXsvbwiadiaPaxBDiaicghYicCG1AE94flHIiaF7A8uj1uKIkkibp0M3CTSrFbQ/640?wx_fmt=png&from=appmsg "")  
  
且这次我是收集到一个学校管理员老师的账号，进行登陆的，账号是教职工号，密码是123456  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXaBe3CvmyNuEJ2EPrzJnD1YdWwazfcOc9jpuicDcrgyj9fA0ic9UjyOmA/640?wx_fmt=png&from=appmsg "")  
  
这个老师的账号权限比较高，可以看到，可以进行一些修改和删除的操作，且学校老师的账号密码都可以重置，这样的弱口令如果要是在众测或者企业src中，都有好几千的赏金，所以有时候别瞧不起弱口令  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXnPWwgibpsaBbSjcOo2hL4RK3wiaNCOAcFr565Ql5oXmcV44qpqiatJ9TQ/640?wx_fmt=png&from=appmsg "")  
### 二、越权漏洞  
  
这里直接创建两个老师的账号（都是普通老师账号，看不到别的老师的信息），然后和我这个账号一起测试下越权，也就是企业src常用的A、B账号测试越权漏洞的手法了  
  
这里我直接先测试的是重置密码的接口，尝试看看有没有越权操作，登陆A老师账号，点击重置，再抓包，保存这个接口和后面的参数值  
```
/personnelManagement/TeacherManagement/xxxx
```  
  
然后再登陆B账号，进行上面的操作，再把后面的参数修改成A账号的，然后返回包的数据包显示修改成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXrjqwvpbibE7kRLq2FtElnzVoTnzETuKcXJfZHJQibxurWoxK6icJeTT9w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaXR2C7Zc9qSIDW1dynsN3Bib4cR6SzE0ZokXHqOJIDYiadXzicCjrsia4x8A/640?wx_fmt=png&from=appmsg "")  
  
尝试使用修改后的密码去登陆A账号，显示登陆成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUxMYhvbNTx2MbdTb6DpIaX0EciawnmCU1z6KQpCLAGiaOFdT3FnYenEXNZOYSBSurtS72bUkGeY02Q/640?wx_fmt=png&from=appmsg "")  
  
到这里这个越权就给大家分享完了，其实这个系统后台有好几个功能点是存在越权漏洞的，但是操作思路都差不多，也就不全写上去了，就拿最严重的修改密码的越权给师傅们演示下即可。  
## 0x4 总结  
  
到这里这篇文章就给师傅们分享完了，其实后面的操作不难，主要是前期的一个信息收集，特别是对于后台登陆系统，能够找到账号密码进去测试，特别是敏感信息和敏感操作多的（众测和企业src这样的弱口令赏金蛮多），然后建议新手师傅们要是web搞不来，可以去测试下小程序，然后有突破再转web端测试。  
  
02  
  
0x2 培训课程介绍  
  
26  
  
**SRC漏洞挖掘培训课程**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6cIuvSQkkicOHhYFkQLTibYAMUR9rfZ9eUrI78toIC4V2304G909O6s6CnVrAGiaYLEJM9XuUARhzNfxCtYKQfQ83wfPSlqpshSScfoYzSKzgY/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=wxpic#imgIndex=4 "")  
  
  
**1.课程价格目前是350（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！**  
  
**2.报名成功送知识星球一个，拉内部小圈子交流群+SRC直播通知群！✨**  
  
**3.一周2节课程，直播+录播形式，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课！❤️**  
  
**4.目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的！**  
  
**5.上课结束后，会把视频录播+课件笔记一起打包发直播群！**  
  
**6.哔哩哔哩SRC课程公开课，链接🔗直达：**  
  
**https://space.bilibili.com/642258933**  
  
  
SRC课程详情  
🔎  
：[神农SRC 漏洞挖掘实战课：从 0 到 1 成为赏金猎人](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247502159&idx=1&sn=b740b393592a4302791978f29030ec2c&scene=21#wechat_redirect)  
  
  
内部小圈子知识星球详情🔎：[强烈推荐一个永久的SRC挖掘、渗透攻防内部知识库](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247501608&idx=1&sn=5eb836122ac222ca9767a7bbc3c4521b&scene=21#wechat_redirect)  
  
  
欢迎关注微信公众号：神农Sec，报名咨询添加微信：  
routing_love  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QVcCkxIUpaBmNic17zibGfXMWrr9z89gE0DFtbOu3QYzD5d62zsp6qwc38Pssk60mLq8VKthcMOmctVlHU716S5G4KYmrKVrEj5c/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6 "")  
  
开课两个星期左右  
，课程目前已经  
累计加入了360个学员  
了，课程培训招生任火热持续中，师傅们对于我们课程感兴趣的，想要学习技术，找工作的可以咨询我报名。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV9JZMg9APhn0wnj5ic5r5AD14lE4oArvIedR8MLBOdCNjfpnpULqrao3dOkdqzF0xCRM3txI3y9sibCq2viaxKuArC6prxdIQfwM/640?wx_fmt=png&from=appmsg "")  
  
课程培训记录📝，每次上车在1-3小时之间，上课包括课程内部群大家  
交流氛围很好！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVITh8VvNrnXLk1uuBSYeYtdOxg96gnicdvmpa2GhwOVTvBGzKEA5ktu7C7wqFYWWRuYZgKmsI8TAoYFia1uC8iaiaLvUNXS7JMMqU/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18 "")  
  
课程上课笔记课件📒都会打包给师傅们，笔记都非常详细，很多几k价格的培训机构哪怕是课件笔记都没有的，我这里都是下课第一时间把  
录播+笔记打包发给大家！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV2abYZgbu4G7Z3GyVibCY54W9gUHCatZKfia1MK3pRqxEM3p6zoLPzkSI57hdIbGKokTZRKfliaW1VwOM3f12Yq79qEXZJQKnPRI/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19 "")  
  
平常也都会给学员进行一些项目发布，包括后面的  
工作、护网内推等，经常上麦交流，大家互相学习，简历优化等。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXvjjkgJibDEUhdDjErjibiangGsN0rqb0Av59xfyxBbDrTMNdfIAhNXlx0HQKvxIVBIEGAAbYrEENzd77j65asejlD4a50Sb4U7o/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20 "")  
  
SRC漏洞挖掘课程培训已经两个星期了，期间也是创建了  
“回本小群”，  
希望学员回本越来越多，创建这个群主要是鼓励学员学习进步，以及不定时发小项目！  
  
最后也是希望大家都可以赚钱，找到好工作  
🎉  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXWOzF7WkU3baE4ZWzNIZpfTwMCqiaQ0YSHYNTMqBnqKq1GWdKq5cbWAw4U3xDfbNPgjh0z2iabSLd8x55wRGbymj0LsVo2vbtico/640?wx_fmt=png&from=appmsg "")  
  
培训时间不长，感谢🙏师傅们的  
喜报  
，很开心看到师傅们给我分享自己的成果，希望师傅们越来越强！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUMAtEWv3xXZPDsGBRhESmwGRciaasCGibU8TtbP2U0YVZPBdf5tlLqpWAtQKBh5oFwgETyvicKBeW1JSsekAyJ5cbRlSdjooQkSM/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22 "")  
  
平常也会分享项目，下面是一些  
学员项目成果  
，群里报课的学员都是不抽成的，主要是帮助学员进行  
回本  
，让大家都可以进步！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWS8lR4pmzZrczwr6YjtG48EqF9q4FlAUH78M7DXkiboqF8Q1HkeWJLzpFPOQBToO3auj8r4rU9x3fuafXUDVMEcFj5EI6U3P9w/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23 "")  
  
上课结束后，会把  
视频录播+课件笔记  
一起打包发直播群  
  
「神农安全」知识星球目前已经  
累计1700+网络安全爱好者的加入！  
  
后面也是小圈子做大起来了，师傅们也都喜欢看我文章，想着给大家教下src漏洞挖掘思路，所以自己花了很长时间做了✨  
课件和课表，都是纯自己手搓的，大家也可以看下课表的内容。  
  
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
  
课程价格：350元  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QWoxDZKgWFyjP5ckCZqsziaGyXQ40oL7gaK0VHA3P3AJ9sD7DWd79QliaGTPMAia6blFToTS9Nd5lpWHibAXgeNzHy5DEjTfsdcTaI/640?wx_fmt=jpeg&from=appmsg "")  
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
  
  
  
