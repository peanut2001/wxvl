#  【攻防渗透集锦】漏洞组合拳与JS攻击面的博弈  
一天要喝八杯水
                    一天要喝八杯水  神农Sec   2026-02-21 01:18  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。  
#   
  
文章作者：  
一天要喝八杯水  
  
文章来源：  
https://forum.butian.net/share/4619  
  
01  
  
0x1   
【攻防渗透集锦】漏洞组合拳与JS攻击面的博弈  
  
### Actuator泄露403绕过  
  
又又又又又又是经典的不能再经典的登录框开局,习惯性的看看雪瞳接口老师傅可能已经锁定接口了/prod-api/  
接口,此接口是springboot  
端点泄露高频接口,往往在后面就放置了envheapdump  
转储文件等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSHPwpd8nrBhRJic0KjicDbZdJEIQpZ8d5E1ODnPnHo18Q1vE0NLdxXFiag/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSiaP9L5fw6hW8biatiaABS35RBJV1aTzjgCv1vficfM18mCVSNF7OxWUEMQ/640?wx_fmt=png&from=appmsg "null")  
  
dirserach  
全部回显403  
应该是做了Filter  
权限校验,如果是404  
肯定是路径错了比如/prod-api/  
前置或者后置需要新的这层, 那么我想办法如何绕过403  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSlU2UZNmsHCumxzRoVo9HuQL6NYiahIZTWkpUdsicfG2MdbkDVIt6OkXw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSGQmfjSe1H2zswJHOutmia8WOK2CUYq9LurUrD0Y8duR8ndWSo0vZ4Tg/640?wx_fmt=png&from=appmsg "null")  
  
让actuator  
中的o  
编码为%6f  
，但常规url  
编码是不能对o  
进行编码的,他属于 "普通字符"（不在 URL  
 特殊字符集中，不会影响 URL  
 解析所以会原样输出），因此 **标准 URL 编码工具不会对 “o” 进行编码**  
，会直接保留为 o  
，而不是转成 %6F  
 ,我这里为了方便记忆才如此写下下,编码只会原样输出,正常情况下只能用ASCII  
 反推出值  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSOhicsSlxFrRWbm0jic00YpxCSOIC5qfWYxftZ6iaejQR8YAaJc2KJOAPQ/640?wx_fmt=png&from=appmsg "null")  
  
%6f  
会解码为o  
  
%6F  
 是 **十六进制 ASCII 码的 URL 编码形式**  
（%  
 后跟着两位十六进制数，表示字符的 ASCII 码）。因为 6F  
 对应的十进制是 111  
，而 111  
 正是字符 "o" 的 ASCII  
 码，所以 URL  
 解码时，%6F  
 会被还原为 "o"  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSzcPsVuMibKLIJ6tXtcicbGsttxG2D2ZDcZWlqT6bmPat6asJtyDk5BBQ/640?wx_fmt=png&from=appmsg "null")  
  
明白这一编码原理后又有读者要问了,主播主播**ASCII  
 **反推值又自己计算十进制再转换特别麻烦，有没有简单高效的方法,有的兄弟有的,把想要编码的值交给ai  
就完事了,通过回答可以知道r  
编码后为%72  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSMHKUVUK2bicIcHAEd1Y4S5cgEic6KUlxQwwMzTk0Hm03GcWYwfG9Q8EA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSyXkiciayESbGA10lAyDchCweThgUVtVFWnnaGOhWtU0GaTDXRvicyTgicA/640?wx_fmt=png&from=appmsg "null")  
  
解码正确证明交给ai  
编码转换是可行的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSwMljk78ZQ6dUJpLe1fiblr4HyexkOpKZTia3VibVcrj44yialxuB9qStJg/640?wx_fmt=png&from=appmsg "null")  
  
actuator  
中的o  
编码后就变成了actuat%6f  
r 那么这样携带去访问,成功绕过发现路径还有heapdumpenvnacosconfig  
 信息可以打开新的攻击面还有gateway  
路由更可以尝试是否可以路由rce  
, 后续访问其他接口详情也是需要在编码基础上访问,不然也是403  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSMrxLjEBH3PLc2sbcoHGy7CrfAFqJ8nKOBZ1ehk0MCOeHjwTSJcRBDw/640?wx_fmt=png&from=appmsg "null")  
```
https://xxxxxx.com.cn:8088/prod-api/actuat%6fr/  https://xxxxxx.com.cn:8088/prod-api/actuat%6fr/env  ------ 成功访问https://xxxxxx.com.cn:8088/prod-api/actuator/env  ------ 403
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS4Y2BkQfkTpKNjS7pF3aYib5fqldEbYic4a3ZNVFAQybswAQlrwOfgiaVA/640?wx_fmt=png&from=appmsg "")  
  
后面发现这款工具也可以帮助我们将字符进行ur  
编码推荐师傅下载使用,工具github  
搜索poc2jar  
即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSrYCAOrGx8jYsdK3zgZxu75AwxR7RGhLFzfaJKpeiccIRib7GpLBoElMA/640?wx_fmt=png&from=appmsg "")  
### 小程序Host渗透后台  
  
小程序开局,一番测试并未发现问题,鉴权做的很安全,越权、注入、逻辑漏洞均未发现,随即转变思路,尝试是否存在web  
后台地址,打开新的攻击面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSpEIIWHlyZNIBSBGVv2aLEKuWo81vfjjZLibNUqiaYxxdkxQsU3ktBOaQ/640?wx_fmt=png&from=appmsg "null")  
  
小程序一般会有后台管理页面,可能是其他子域名下放置的404页面 或者是小程序本身host  
域名其他目录下放置,这里首先尝试将host  
放置浏览器访问  
```
https://city.xxxxx.cc/
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSnR3CJFThK8IyDp5hP08npo5ol5Rjf2YTCGdO2QHpoMeziaOn2N8JdNw/640?wx_fmt=png&from=appmsg "null")  
  
根路径正常回显那么开始上dirserach  
递归目录尝试能否发现后台地址  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSrs4sU1iczW4ibxmB80BXpCmicPWwEA2d9nWCoKox365f69Ycanaf2EABA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSWlAaJdCKricenYRemkaAzcqialK6dl3kmJX8MFicmlCAl4ftL7nK4CMKw/640?wx_fmt=png&from=appmsg "null")  
  
也是很幸运字典加持下不到二分半就得到有效地址,fuzz  
 出第一层前置目录manage  
 携带访问后直接跳转到后台地址,那么可以测试的点就多起来,弱口令未授权,JS  
接口等等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSq0VPcjiboDec6k20vyfF93zdlV2JSg0hQLxTNG4dwGu2Kaqkia3cpUibA/640?wx_fmt=png&from=appmsg "null")  
```
https://city.xxxx/manage/------>https://city.xxxxx/manage/login?redirect=/
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSA410Yo5FKz9BbkbBwpIibxvyVpE5daREREiaEe26a8nibzasT4qePm4gQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSycSWv2k6WiaG2HAnCSGWKhpj0vvkI8RbWJXcqCUiaatnk6Pwy1mRKLTA/640?wx_fmt=png&from=appmsg "null")  
  
但是呢各位黑阔师傅们是否都会有先入为主的意识,我的目的就是为了找后台管理地址,现在我已经找到了,那么dirserach  
余下的会去完整的看完吗？域名下可能会设立不同的目录放置不同的登录口,耐心的看完所有信息至关重要,工具在这里又Fuzz  
出第二个前置目录,携带访问  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSFg1BuhQPrHVNEgrEeuKcGoNXzSt3YwhyPQnxvicZhKBibtWJB5Ugra0A/640?wx_fmt=png&from=appmsg "null")  
  
同第一个地址一样,携带第一层后就会完整的调整到新的系统,在这里发现了第二个系统为后续渗透埋下伏笔,至此dirserch  
任务完成直接X掉  
```
https://city.xxxxxxxx/backend/----->https://city.xxxxxx/backend/login?redirect=/
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSo1DiarkbrfF3lOicsiaKuzTttZ2mRLGmbUxw964KwJ9lMCea3PRobNomw/640?wx_fmt=png&from=appmsg "null")  
  
回到第一个manage  
目录系统,纯粹的弱口令,后台地址藏在目录后往往也觉得这样很安全,密码设置也会相对简单,细致的信息收集找到入口漏洞往往已经呼之欲出了,查询小程序内所有用户实名信息三要素并控制余额  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS3iazibLD2fKFkYXiazEhpNrsxlOgHALZXvxW76P3cLjicIplHbqazKkqFw/640?wx_fmt=png&from=appmsg "null")  
```
admin/123456
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSicCI7qtCYLOXbDlChNRA0qlkWT7MtkwzDjo1qanQ4NTiaV4Cg1Kv4FwA/640?wx_fmt=png&from=appmsg "null")  
  
依旧是亲切的大头照  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSVxeiaM0dN0hgPJEibuEC0JWNq5jyQLyOibxlbxcmIibnOXr7Cvfn3NELqA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSbR2eBLcaxKjZ9ibLE7xtdThdHNCribdIk9wTicGElTdbR3mRGhcQNj0mg/640?wx_fmt=png&from=appmsg "null")  
  
弱口令进后台还可以挖掘其他漏洞,更好的测试接口未授权问题,已经有了管理员权限那么调用所有一遍功能再把敏感信息接口删除token  
重发即可,当我测测时就发现了 ,第一个系统和第二个系统关联处,城市合伙人不就对应了第二个系统的名称嘛,账号大概率就是手机号了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSciaP4fHfFjicnGwhSt2v9cRAH02YwFcdZKC954KO2EcEkEkQQLqGRSSA/640?wx_fmt=png&from=appmsg "null")  
  
来到这里通过合伙人的账号配合初始第一个系统进入到弱密码,纯粹拿下第二个系统,渗透本质依旧是是信息收集  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSyyYL1Kw0Tuic6XRBkuYicXGV0zhkyDiasTPuykvbD0Y2XpgdjsNkWlLLw/640?wx_fmt=png&from=appmsg "null")  
```
手机号123456
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSEPIHViay48UJI7VonibbSiaB92UdHibfgkmUUkAibO01A7CqGFBuGHicUeiaA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSF2buunic8EDibJTyE26N35sUBCCB0sSM2aOyOFfOcMulicicickbbGkaAcA/640?wx_fmt=png&from=appmsg "null")  
### Shrio721容器Rce  
  
渗透项目拿到大量子域名资产使用Ehole  
指纹识别发现Shiro  
框架,反手掏出压箱底的反序列化梭哈工具  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSE42sM6a5YSJbTPVNX30gFicP6Xa46uCiaibSe6PNc4ibJHlicFckal8VoYw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSZbSNUMW8NIpUVG8ibicvzjtUicAF2Q3lZWJfAjgntbAmRGout0JKg9x6w/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSCl5T5VbsaIedpyGWYwU3KkxvV5HCAnaoPFwicrdPgaDmoCwOiaTjT7qQ/640?wx_fmt=png&from=appmsg "null")  
  
填入地址马上给我爆破出aeskey  
 有种淡淡不详的预感,猜测可能是docker  
容器,如果爆破的时间最长一些我还不会这么觉得,地址填入不到2s  
完成给我感觉就是等着我来测呢  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS0icqEIrlhm2rQVd7THaBNH4tdjia5Leo3ITFCCKSYC7ErDXZoFVYw7PQ/640?wx_fmt=png&from=appmsg "null")  
  
爆破一波利用链,如果是有key无链工具只能用JRMPClient  
分享其他师傅的文章工具可以去了解一下;这里出现了CommonsBeanutilsString  
这条链接,可以直接在功能区调用或者是生成内存马上线冰蝎  
  
Shiro无依赖链—Commons Beanutils_shiro 有key 无构造链  
  
https://cn-sec.com/archives/2673175.html  
  
检测非常规利用链工具：https://github.com/wyzxxz/shiro_rce_tool  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSEapFCLXXtiaXibrkdFWmj0WRKlx7qxko9m92QPIDbGhwRI0t5vkNDbUw/640?wx_fmt=png&from=appmsg "null")  
  
为了确定是否是容器执行此命令看看初始进程,如 systemd  
、init  
 或容器中的主进程）所属的 cgroup  
 信息，如果系统运行在容器中比如Docker  
），路径中通常会包含容器 docker/abc12345  
 ，根据回显判断出了确实容器是容器开启的服务,哈基W......还是办不到吗....  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaStd0E9EfDjbf8qlFnS01w6HkbB5mT0oF1wuPBFQwf3o26c5NkIvyAsA/640?wx_fmt=png&from=appmsg "null")  
```
cat /proc/1/cgroup
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaST2DcyibMphwGJWTg13YRksPB5VkQubkb3mouibsLG670B6ibiaVaJAN25g/640?wx_fmt=png&from=appmsg "null")  
  
但是即使是容器不能逃逸并非没有利用价值,机器内网它可能会通其他内网网段,如172、198、10  
等典型的内网段,后续就是注入内存马冰蝎连接,但推荐各位师傅可以玩玩Vshell C2  
工具,代建正向反向代理都很方便,省去了frp  
等操作，权限够大搞还可以一键命令反弹上线,上线后交给队伍其他人员尝试内网刷分即可,地址和教程如下  
  
带web界面的C2工具vshell_4.9.3  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSPFz18gic1jcmiaytvibicAQynZkwUWLk4PbXngxyAT28GtrZms15Byu2OQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSDxBNIBibqMH8feP6VVFbSTZV6knkLLLyZhxIC8kSXGLhuKsdWdWUuqw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSLz5DN87S104SPOfOSuJvzbgraiaFHKB5icjzicojhTRAgIGfedQ9bY25Q/640?wx_fmt=png&from=appmsg "null")  
  
有些shrio  
框架指纹识别工具并不能有效的扫描到,只有在我们对每个站点测试时通过响应和请求rerememberMe  
 字段发现,这无疑会错失很多,这里推荐一下P喵呜师傅提供的Shiroscan  
工具可以有效的识别出是否是shiro框架并进行shiro721  
测试  
  
https://github.com/pmiaowu/BurpShiroPassiveScan  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSUlPASINia4rzFWuCobEfy1x2ibD1nbNbpVyQZeGZxfd9kDGJy0GxY8Hw/640?wx_fmt=png&from=appmsg "null")  
  
安装插件后在给出的配置文件内可以自己填充常见的Shirokey  
 进行补充,安装好后安心测站就行,时不时看下说不定会有意想不到的惊喜。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSJHsRcQWPEr4kHE9uY6gjH4TicMNXdJJeBiaCWVkPgyrRVd7EJEfxu2uA/640?wx_fmt=png&from=appmsg "null")  
### Js同域名站点接口复用  
  
登录框Vue  
框架起手,先正常提取插件接口看看是否有信息泄露,无果可以再二次提取webpack  
接口  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSNxQosQEQ3ymMrbo3VXian9bze5IUAzHzKJn1KwYdQy8brSwoXkQxicrA/640?wx_fmt=png&from=appmsg "null")  
  
前端存在登录功能,调用接口后并经验应该是前置的目录api  
所以这里保留,直接放置接口作为payload  
进行爆破  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSwnWJk18Whia5e7tUQOOWARhQ62echXeMLqqv7uWtYCS9xpRSlfbZCAw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS3YicVJ7wQsmoQYjVNDVa2abf13rybqkTNKZNchwZm087GCwYVgiaa2LA/640?wx_fmt=png&from=appmsg "null")  
  
很可惜只有一处信息泄露但是这么大站点怎么会泄露这么二要素呢(姓名被unicode  
编码所以识别不出明文)  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSDuJkuZxDzKKg5wNpZsjg3mQDyMficrFOiaqVpajX1Elspp85CUWP0cng/640?wx_fmt=png&from=appmsg "null")  
  
这么点信息够谁交啊,让人看到还以为我挖不到洞呢,直接上控制页面参数拿下全部的信息，将近7k  
也够交差了,这也是在接口泄露中提升危害的小技巧,至于具体应该跟上什么页码参数如果其他接口响应能返回一部分信息那么利用响应包的信息拿到请求包使用尝试是否可行,如果不可行只能是Fuzz  
 下面给出我常用的页码组合参数，平时在渗透过程中也可以自己记录并填充,形成自己的渗透字典  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSH0zYEW3x04YhHQyZjhTvkAex5xzKHWJTWGhn4YCveWJRYBIekVicgcw/640?wx_fmt=png&from=appmsg "null")  
```
/api/users/error_list ?page=1&limit=10000页码组合参数：ET page=1&size=10000page=1&page_size=100pageSize-10&pageIndex=1&pageNum=1&pageSize=10POST{"pageNum": "1","pageSize": "100"}{"pageNo"1","pageSize":100,}{"pn":1,"size":10}
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSWLhZImmmPOu9fTjlC9OQYzSmGzVbMGA0AWwRTfwgGAfIAicR49ZHUzQ/640?wx_fmt=png&from=appmsg "null")  
  
常规JS  
并没有有效接口,那么最后一步提取chunk  
异步JS  
,也就只发现了一个有效接口所造成的信息泄露,和第一个接口一样泄露了二要素姓名电话还有一项家庭住址就去挖掘此域名下其他子域名了  
```
/api/test/test_user_list?page=1&limit=10000
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS55iaefibW9DMDicgKhUSwNGia0bX02h9m8ibYH9vKEp81aDfvibnnY3zRwhw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSqwjiaNa6qRtvSD7yKjOeQzUo8S8nc5kQYeQ3vSbd6qUpNRMLKY1I3BQ/640?wx_fmt=png&from=appmsg "null")  
  
hunter  
测绘到一处新站点,很明显二次一模一样,大家可以通过域名观察,第一个网站是我新发现的主域名站点,第二个网站test  
则是上文我进行挖掘的,那么可以进行最原始的利用方式了,同类似站点接口复用  
```
新发现站点: 根域名.com已挖掘站点: test.xxxx.com
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS7Q6OfEGibFpBiajYhUFf90n2spXAt5c3Vga2YvHBcyjn4Fax3swBlqkw/640?wx_fmt=png&from=appmsg "null")  
  
复用倒是可以复用,但只有复用一个接口且经过处理信息量还是较少,不如第一个站点一根  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSr2JQia5VY1CmxZrWHp89ZJicN8zGfJHdFH1O1JrcSMlLBicJAUqeOwHsA/640?wx_fmt=png&from=appmsg "null")  
```
/api/test/test_user_list?page=1&limit=10000# 复用成功/api/users/error_list?page=1&limit=10000# 复用失败
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSnPSKtq1oAQGrIPL3oAbKOK9iamCSmvUZ2vZtM006TibCxaMic4omOFBkQ/640?wx_fmt=png&from=appmsg "null")  
  
除了复用第一个站点接口,同时也要跟往常测站一样提当前站接口测试,但也只找到一个有效接口信息泄露也是量太少  
```
/api/users/search?page=1&limit=10000
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS7zrSsD2vhmSWUZqbGKu1W1X71K6JDhibRIKTD0yykhXcLKEIOLcmdng/640?wx_fmt=png&from=appmsg "null")  
### 业务功能注入+越权覆盖  
  
JS  
接口虽然是实用性较强的技巧,但是对于功能点挖掘也不容忽视,进入一处站点登录并注册,我会代理着BP  
大致浏览调用一整个页面的功能,然后在历史记录里稍微看看哪些接口可能会出现问题  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSqmy0qCJjXCs2SicDZrQibOkrz4FFmSEGrIfhzXBs4LXiaxicicUAXTk7okQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSu9x6cktEauicLIgM847QbMCyyKiaLDYic9f0xaztAMa4RqUI7CGPVn5LA/640?wx_fmt=png&from=appmsg "null")  
  
熟悉业务结束后如果直接出漏洞当然最好不过,但没有也没关系,毕竟第一步也只是为了熟悉一下业务功能点而已,后续针对每个功能点发的每一个才应该去细细测试,在一处显示列表出发现tagId  
参数,加入单双引号都不行返回的都是500  
```
tagId=119
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSrBIUPInwKhNKSZHAG74BYh5OJU2spDyoLp8eYlT7ch42Re3CMwExqA/640?wx_fmt=png&from=appmsg "null")  
```
tagId=119'--+ -----> 500tagId=119" --+ ----> 500
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSwHhphlcJdh1WUjG23G65lZv6iblJF4bxHxlQXl2hCgolkdZrzibP9Www/640?wx_fmt=png&from=appmsg "null")  
  
字段行不通,尝试测试数字型,利用and  
两边都满足看看是否拼接到了数据库内,1=1  
正常返回  
```
tagId=119+and+1=1
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSkz3F2Swo4mW793viaKDqNDJKRuMiapzswFoiaBHLRVdSMhX19DJPffeiaw/640?wx_fmt=png&from=appmsg "null")  
  
我们设定的条件为假所以肯定是不正常的,响应500  
不返回东西,确定了这个点肯定是有注入的,这种无回显情况除了典型的布尔测试,还可以利用延时函数等等  
```
tagId=119+and+1=2
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSnNNaOfNBZibY94zdSiabrlNdiaSAKEkiaibsvl1pT5DbqkoQ0bakvA4xtFA/640?wx_fmt=png&from=appmsg "null")  
  
通过布尔注入在and  
后面利用if  
来判断出数据库的长度后续再判断具体的值,数据库长度确实大于某个数字则为真走exp  
报错,不是的话则是为假,正常返回  
```
tagId=119+and+if(length(schema())>7,exp(999),1)
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSia9SJItFDs2OUqkhQjZ4fTMp4jj9AQbuibGLcEliaEJvU7cnVicOdCP2xg/640?wx_fmt=png&from=appmsg "null")  
  
那么大于6  
呢.确实大于6 那么就为真,根据上面的信息,数据库长度是大于6  
小于8的,确定了数据库的长度就是7  
了（少截一张图,但确定了数据库的长度就是7）  
```
tagId=119+and+if(length(schema())=7,exp(999),1)
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS08oibBRKMkkFQTafes3MFYHUjNEZicEvHf9s3ibjxL4a4iaH6DiaKkkbGjg/640?wx_fmt=png&from=appmsg "null")  
  
有了数据库长度再来测试具体的值substr  
函数截取数据库长度,从第一位开始,如果是a  
则是报错,不是则是返回正常,遍历26位字母和数字伴随其他标点符号,设置好两个payload  
位置这样可以快速出来,只跑7次就可以了,爆破的模式需要选择为集束炸弹  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSicc7NawdSmXQy2nNjbQ42wWL1JhxmbSQ0VZZ27QhcbnGKLCK0gNSeSQ/640?wx_fmt=png&from=appmsg "null")  
```
tagId=119+and+if(substr(schema(),1,1)='a',exp(999),1)tagId=119+and+if(substr(schema(), 爆破点 ,1)=' 爆破点 ',exp(999),1)
```  
  
最好成功的得出当前数据库名称为chatgpt  
 倒也符合这个站点业务基本都是ai  
生成相关  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSMNHnlIcXjOJDFrPRPvoRTVo5AibXR75Zhmk2clBwoop79bet5ehTTzA/640?wx_fmt=png&from=appmsg "null")  
  
一个站点存在无任何过滤的注入,那么肯定不值一个注入,带着这样的想法继续测试;被动扫描显示modeIType  
参返回了数存在XPATH  
报错信息,这不典型的报错注入嘛,后续就是朴实无华跟上一首Payload  
成功爆出数据库名称,也没有任何WAF  
 ;有WAF  
的话主播也只是会简单的替换函数、注释、编码这样,高难度的绕过组合拳只能白嫖朋友套  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS1f2fZTicV7moXj8icZTvDpc2M7QgF055QibLKAJoe8aZ5roEZyW1eicllw/640?wx_fmt=png&from=appmsg "null")  
```
modeIType=video' and extractvalue(1,concat(char(126),database())) and '
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSEbKdov87cEicQCUQ42R9TR5fibXctTYzd367xyd6V3DEibeOZ08W0zzNg/640?wx_fmt=png&from=appmsg "null")  
```
%23 == #  %0A == 换行& == 连接符%20 == 空格version（）——> @@version hex()、bin() ==> ascii()sleep() ==>benchmark() concat_ws()==>group_concat()mid()、substr() ==> substring()@@user  ==> user()  user()      system_user()   session_user() current_usercurrent_user()database() schema() 数据库名@@datadir  ==> datadir() 1、十六进制绕过eg：UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name=0x61645F6C696E6B2、ascii 编码绕过eg：Test =CHAR(101)+CHAR(97)+CHAR(115)+CHAR(116)3、Unicode 编码常用的几个符号的一些 Unicode 编码：单引号: % u0027、% u02b9、% u02bc、% u02c8、% u2032、% uff07、% c0%27、% c0% a7、% e0%80% a7空格：% u0020、% uff00、% c0%20、% c0% a0、% e0%80% a0左括号：% u0028、% uff08、% c0%28、% c0% a8、% e0%80% a8右括号：% u0029、% uff09、% c0%29、% c0% a9、% e0%80% a9
```  
  
往往一个站出现SQL  
注入就会伴随着多个,后面也是在此站点发现了多个注入,报错注入直接回显毕竟也是少数,大部分还是通过布尔页面利用页面回显不一样来判断,发现后和上文手住方法一样先测试出长度再遍历库名  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSaeb29dKftKiaSrAgfcJp0ANwNLmewwOjLARSmjqFVYVRhgImkyQqozg/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSI8ictm80sIeOUX9DNic7S45ibMHzd8P7x9lXx3nkV0WiaRdbYfmuqOOqYA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSL3iafNOuXnr84ocXicdjGnKCGQZibB59lhibiaLEJ9k4WEJybUNHP6KWg2g/640?wx_fmt=png&from=appmsg "null")  
  
测试到头像上传功能点时,图片上传到存储桶,虽然无法打出一些webshell  
操作,但仍可以对存储桶进行列桶,htmlxss  
 、put  
上传等测试,不过这里我却发现了不寻常的地方,响应包上传后生成的图片名称回显在了请求包,经过测试上传文件名可控,并且下方目录也可控  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSNQEmQibiaMVMKIzZibeSEOaXZo4Bmwm8ITCicibiatm2v28GCq5uvjOU2ITA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSFeHCSTHArLhbB9cP4PCnMQCfT2Gl29cLibseiaVuIETWVmZcTJicXKicibw/640?wx_fmt=png&from=appmsg "null")  
  
数据包内出现文件名,经过大小号替换图片地址测试,可通过文件名覆盖对方同名上传文件,文件内容也由自己控制,但是这个漏洞利用较难,因为受害者的文件名是固定的,只要可以一直爆破原理上是肯定可以覆盖掉任意人的,但是利用难度较大没有意义  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS3S9kBTKH9xX59ewxzkZKTUeuicoS8nm3bbBBwBq824USu3n5Q0Gc9xA/640?wx_fmt=png&from=appmsg "null")  
  
转而寻找可以带出用户信息的功能点,类似排行榜评论区这类,可惜一无所获,但是测试页面发现网站内的图片也是全部存储在存储桶的路径内,上传头像和网站图标只是目录不一致,但桶也是同一个桶  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSaz8tvROmBjlHrRTDJrHwKcBpicUqticyDtRJmx7DwmcxbhCUOmsrbuTw/640?wx_fmt=png&from=appmsg "null")  
  
保留下原始的svg  
 到本地为了测试后还原,不破坏网站；然后在头像上传处再次上传,将上传地址改为得到的图标目录地址  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSdXloNOD4NpdHf9TZBI4dCBCj21O1rIdRqP2AsXCsJPAKZy9KaK1zmw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS3zowYlZxAtptd3bEGlydrG0BRWJ2KItpAib8H5M0X2He37sg2Ih38pw/640?wx_fmt=png&from=appmsg "null")  
  
成功覆盖证明危害即可后面靠备份图片进行还原,如果写脚本爬到网站内所有图片名称,遍历上传也是可以覆盖全站图片的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSsfz10n2NK9BAdPdfs9ssqu7dia129d4NsOzd2D8MnZPIOdickTWQwtaQ/640?wx_fmt=png&from=appmsg "null")  
### API接口组合拳Actuator  
  
Vue  
站点正常利用插件提取接口,正常跑跑看接口反馈什么情况再选择寻找前置目录还是进行Fuzz  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSY1OibgjMUYsic0nKpUKKoX8QxUU9qR1W70OsW3pMHYRYpcsw2njxf33Q/640?wx_fmt=png&from=appmsg "null")  
  
发现全部重定向回到前台,那么盲猜会有前置目录情况  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSMvicsGYeQhaGJXgTMbbiaBkf61m5RUnLYQZISJC0HMHgOgOiaJRibFydcA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSNY6iaX2gWgNmsPxabDSLz4sehsUO9zhcVvK1ZP5dQkfWVRLjWPicoN5g/640?wx_fmt=png&from=appmsg "null")  
  
老方法调用登录功能触发接口,依旧是熟悉的api  
 那么尝试固定此为前置目录在这个基础上爆破接口,GET POST  
均可以尝试  
```
/api/sys/login
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSYS0vIYGvCcYDkK3VOSA9elAmonMgWicWwjibGGNvLAGSCWPSOvicvpTEg/640?wx_fmt=png&from=appmsg "null")  
  
如此操作后虽然没有和第一次一样重定向会首页,但接口怎么看着这么奇怪呢一半响应401  
缺少token  
余下一半报错从上游服务器收到无效响应,继续在接口方面进行测试,最终通过两处信息让我确定接口处理有误  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaShkANS3vxAO6ibPHsmpOuHW0l4Ym8ibzod7CeLBDwHMpfjBObYarYKu6Q/640?wx_fmt=png&from=appmsg "null")  
```
/api/gcwms-boot/packing/cylinder/basCylinder/list
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSoJhicB39zc4tNUnxzWjYamF3EOfrrTlxiaeGkf9tLicR1VCxvqxdE9kqA/640?wx_fmt=png&from=appmsg "null")  
  
上文我提到测试前置目录我一般会进行调用功能点的操作,我得到的接口全称是如下,那么我将插件接口放到一处记事本,搜索后置接口/sys/login/  
是否被我插件所提取,这个插件是我确定不了前置接口的惯用操作,只要登录口可以调用功能对比接口快速确定  
```
/api/sys/login
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSKWDHxmxE3vavjzRwaOygm7WGM1qsZVEgtQ1KvEHZxHlxXhOLfGCgQA/640?wx_fmt=png&from=appmsg "null")  
  
搜索后置接口发现确实被插件所提取,但是前置的目录却是/gcwms-boot/  
那么不难猜出这个/gcwms-boot/  
接口对应的正是/api  
 想要正确的爆破需要将提取到的接口存在/gcwms-boot/  
的地方全部替换为api  
```
/gcwms-boot/sys/login
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSJpFfFz3NztWhgOdfzoZtfdIyQ9hlpNbJh5iasCn0uGUXODTMD8QrE3w/640?wx_fmt=png&from=appmsg "null")  
  
并且像这种前后端架构出现了Vue  
框架那么基本上可以确定为Vue+Springboot  
开发,我也习惯会去利用dirserach  
字典爆破,或者利用OnescanTsojanScan  
等被动扫描插件辅助测试,在这个场景下插件就帮我扫描出了经典的actuator  
端点泄露以及swaggerdruid  
等捡漏三件套  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSHib4XlTZdPI35P3vibibib5KjdUGROXUiapnqtbFwCDVNzbsaIDIqncn1xA/640?wx_fmt=png&from=appmsg "null")  
  
当我浏览器访问actuator  
端口目录时,虽然没有出现envheapdump  
等接口,但观察到页面显示的第一层目录为gcwms-boot  
但是浏览器对应的是api  
 既然我让gcwms-boot  
作为第一层目录会直接重定向会首页,那么全局修改提取到的接口,将前置目录修改为api  
再测试  
```
/gcwms-boot/actuator/api/actuator/gcwms-boot=api
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS8loSU8wFNxBXzYfibg6ooeXvp0c7Rz3v2qlRMlia3uxUvnaTA0BROwmg/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSIj7ibttpbibialnlDiahwtzvXjVcGZujkIx9KKgbbdYRRDahUxuiaruqaZA/640?wx_fmt=png&from=appmsg "null")  
  
全局搜索替换gcwms-boot  
为api  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSQ79rRibLS1ibk6oZw4TfeJDbO3aGbItys3BO8jccibwbgg3y9hia9zqAsA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS13uEWiaKwibE229O1Fichkquu8whibW6u4Jsq5DZTFj4Z2u6wObMFDczpg/640?wx_fmt=png&from=appmsg "null")  
  
接口全部正常响应没有出现502  
情况并且也出现了一些不痛不痒的配置信息,证明上文我的处理方式是正常的,但是大量接口响应401  
后端存在鉴权,无法获取有价值信息,依旧办不到。。。  
```
https://xxxxx.com/api/bas/basWarehouse/childList
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSls9u4kEnuhGOGNtFOm8icwjQfNzxwCVrXicU2c0esbtvsHicd64ib3HI8A/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSGl1ryF0PHJa67JLUJx2DEaUpUBxIFEBEsgbj3T3rmwbzGKK3STd9jg/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSRe9VojXvznoibF5HcCD5QmulWjvaLuwEhgx7dM9oia4jGDKXbOQJZ30Q/640?wx_fmt=png&from=appmsg "null")  
  
大家基本上都主要是关注env  
、heapdump  
，还有容易造成命令执行的、gateway  
、hystrix.stream  
、jolokia  
等等，httptrace  
和logfile  
 这类记录信息的接口却很容易被忽视，通常这二次不会一起出现,包括这里也只出现了httptrace  
,简单来说会记录登录鉴权信息,JWT cookie  
等  
  
httptrace  
可以记录每一个HTTP请求的信息，包括请求路径、请求参数、响应状态、返回参数、请求耗时等信息。一般会随着SpringBoot Actuator  
未授权同时出现  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSfiaftxGCMNPiaafQ1eplhygYL4tx9ZKWrbSM5do5mibgFuBXviaiahcrl8g/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS9hJ7PCrcXLJPlhR6UiaPkXB8jIia8gHRg7qPlicmL6Ia7gLx3bhE3JGVw/640?wx_fmt=png&from=appmsg "null")  
  
鉴权可能会过期所以下拉找到时间段最新的JWT  
```
x-access-token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjA5Mjk4MjAsInVzZXJuYW1lIjoiYWRtaW4ifQ.PuGa-Fo5o7N0mH2Dxmllov3XpLyJX5oDNGrJT-8fkz8
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSc4PkFcRe2G2dD8KqzTtV7XHbyzOOv6DX1nACibh7fryeoTbQtoUvDCg/640?wx_fmt=png&from=appmsg "null")  
  
携带token  
后再次遍历应该处理的接口,出现大量业务数据泄露,伴随很多xls  
表格记录着联系人列表供应商信息等等,拿下业务数据证明危害,已删除记录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSTLXHCmB425ickzQ2DP7H5sgCy6ib15Pn6dMIvwicldWrLw7jC9YCGHSYw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSEJVhxPxp1cKyDChbcWHfWwZfIlHHIrj8WXGSlSX5HeeeN184rJGMuQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSYHCEJkObOnoHFfNlYCicX0HYfIBh3qH7e2R5Uu3dudGMNxsd3JfquicA/640?wx_fmt=png&from=appmsg "null")  
  
如在攻防中,如演练手册信息泄露并不局限于公民三要素,那么通过JS  
接口拿下更多的业务数据也是一个不错的选择,各位师傅不要放过这些点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaScvBjweCGBScyWgUbWwcEDgzJxoKD9T57j5Da0ddYTSr04NbTmVCr3Q/640?wx_fmt=png&from=appmsg "null")  
### 民生业务信息收集思路  
  
某一众测项目,项目是某一城市水务公司,在web信息收集一圈并未发现比较好的目标,大多需要统一认证账号,转而去向业务点更丰富的小程序资产,但是即使我利用微信登录拥有了账号后,但还需要关键的居民用水账号,否则无法测试功能点,自此便开始了互联网信息收集之旅  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS3dKgIzyyV44Jhq1ibx4YTEib4YaicvjDNBEpHIjDzX0COtiaQZ37NCuVbQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSjyHmsRy5Qic3gAUjwh5OL2WibTEahreRp3icRNvQ1e3tFgfkZdUPuLQkg/640?wx_fmt=png&from=appmsg "null")  
  
在小红书亦或者抖音等社交媒体发帖平台,检索对应的关键字可得到相关信息,关键字偏实用性这样检索更为精确,后续就是在众多的帖子细细发现是否出现了户号、姓名等  
```
xxx水费xxxx水费缴纳xxxxx水费太贵了
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSs8YzVkIybbQkMNWTibHeCqWDdUItHOcVLlelruD7ctOdXzPaavjmic6g/640?wx_fmt=png&from=appmsg "null")  
  
不得不说现在的网友网络安全意识是越来越好了,基本都会把关键信息打码,这也为我们的信息收集增加了一点难度,但肯定会有漏网之鱼  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSuibhribtBQXBSfBXjSOvNDssu2l7bRlkicEue2v06Lx7L2mun7w1qDtcA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSzN8vX4RdYpIHydzTVsHIXtgSbRJe1TmKLz3zTIEwDicuMl1BoYZgXzA/640?wx_fmt=png&from=appmsg "null")  
  
应该长达两分半的小红书冲浪也是找到了一处比较全的信息,里面包含了户号还有后两位姓名等信息,但是姓名不全,接下来就是的单方面社工,浏览他的个人账号帖子、评论区、其他社交媒体,最终通过一个没打码的手机号配合sgk  
利用lm  
控制地区检索得到完整的姓名电话sfz  
三要素,各位师傅懂的都懂，不懂的慢慢学到后面也就懂了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS6Gia89RKgYCIYzP11186eDZM3FuY1BS8yjYKco27pdGMk8A46lp0FUw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSy9efWoNUFuEvFKwHWQW1EFt4ibeozpIw2X1d6hn2y6OP1dbEqZlrFxQ/640?wx_fmt=png&from=appmsg "null")  
  
凡事涉及大量居民日常必备的业务,如水务、电力、医院等行业均可以利用互联网公开资源进行信息收集,包括刚入门的师傅热衷于挖掘教育edu  
,见惯了谷歌语法学号密码，为何不试试看在抖音、小红书尝试检索xxx  
学校学生证掉了呢,这里我只起抛砖引玉的作用,思路有多好危害就有多大。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS64n0eyjQNtjrtgW7RCgso8SLh6x6X3r2z2TXr9fpY8OQrQpy51tEoQ/640?wx_fmt=png&from=appmsg "null")  
  
通过信息收集拿到完整的户号姓名后也是顺利绑定到了账号,测试到了几处越权也不算白费功夫,不要倒在信息收集这一步,有账号和没账号完全是天壤之别，如果身边有熟人那自然最好不过直接给个相关账号就行,如果没有只能老老实实信息收集  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaSLibwfrXNjoiaP7ta3HWxLmiaG1v2KqibtIBibX4u5qMH1ibGDII5gIlj0AcA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVz2jqgTThuC5h2EMrD8eiaS38hIbyGF6KoV1CycbEREJ16CicdiavWibG46fYWo6SELdPFlEyRpXSwkQ/640?wx_fmt=png&from=appmsg "null")  
### 结语  
  
后续文章方法依旧还会往漏洞挖掘案例,但不局限于JS  
接口方面,会把有意思的逻辑组合拳,如何测试业务逻辑漏洞,以及发现TOP10  
漏洞等等,让大家不止只会接口这一攻击面,如文章对师傅们有帮助,请点点推荐,你的点赞就是为创作的动力,并且在文章中插入我喜欢的表情包也是创造动力之一;秋意渐浓记得一天要喝八杯水。  
  
02  
  
0x2 培训课程介绍  
  
26  
  
**SRC漏洞挖掘培训课程**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6cIuvSQkkicOHhYFkQLTibYAMUR9rfZ9eUrI78toIC4V2304G909O6s6CnVrAGiaYLEJM9XuUARhzNfxCtYKQfQ83wfPSlqpshSScfoYzSKzgY/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=wxpic#imgIndex=4 "")  
  
  
**1.课程价格目前是325（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！**  
  
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
累计加入了341个学员  
了，课程培训招生任火热持续中，师傅们对于我们课程感兴趣的，想要学习技术，找工作的可以咨询我报名。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWOzgzYma0aBWuPe7OQQaI9BRibqEHyibXsvvaoABN1VejeBZ5ARK5ib2drdTShm4jYJzU6ibwXxZrppP6wt5uYy66umcHw092Fuew/640?wx_fmt=png&from=appmsg "")  
  
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
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWosTnDNnM3R38KnB6xnicyNlnGxcpRIQH44bRDIqqaggV9ibrOwlrk3wibY3Im7IubkH8FhicudlPkohHxyJZMB4xV2BYVfp9ia16Q/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21 "")  
  
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
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/mcko8AHj6QXACzqC7T7X5WgXKQ0RgJ8e2ibMVnEGeTb9Snw7PBmFCJgzXHL6mTicSulcl54gtTtB9G17mlujt2wJQBTMpC3dY2t4MstjoQRYQ/640?wx_fmt=jpeg&from=appmsg "")  
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
  
  
  
