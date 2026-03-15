#  记一次SSRF+文件上传组合拳：复盘我是如何组合漏洞一步步Getshell的  
点击关注👉
                    点击关注👉  马哥网络安全   2026-03-15 09:00  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAk1nlByTOFiahZKGHekfZGC1V0p6QaXc4CnbPBMZQuFGAnW00CX43Xk9JXONUTxeqYxActf31UiajMg/640?wx_fmt=png&from=appmsg "")  
# 0x01 druid弱口令  
  
  
1.前期对这个web应用做信息收集时，没有收集到任何有用的信息，它看上去就像是一个简单静态页面展示（这里就不截图展示了，厉害的大佬能根据页面找到这个web）。但是当我打开浏览器devtools进行抓包时，发现其存在网络请求，并且每个请求包的一级路由都是相同的，在查看服务器信息发现是ngnix → 推断为前后端分离的项目。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj54JRVJiaia7xicBk1mBia3xicnGagITlRZvwIwy83GbWASOyBdDicsbaVwa2cjJQxYBFMficBQC73jfbEhEF9lg1ww7HlTmfPiaPKoFyoI/640?wx_fmt=png&from=appmsg "")  
  
  
2.如果是前后端分离的项目，首先想到的就是java web应用（按目前市面上主流开发来看的话）。并且如果是spring的项目话一般是会有默认报错页面的，这里为了验证猜测，我直接在浏览器访问了这个路由。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj556zYV01UUE05zwouegtZEGWXh2X7QHVKtX8pw0F72fHphcTBpjuxt7d4AN66FlJqMHnQMdfkM7tsV2QHxr976enu8NjX8rdjY/640?wx_fmt=png&from=appmsg "")  
  
3.显而易见，这是一个java spring的项目。spring项目一般是存在很多敏感目录和敏感文件的，我们可以使用字典来进行进一步的信息收集。这里我用的是曾哥的SpringBootScan：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj55EQy8icqvHichCRWRAVuhHjc5u6OzU1F2l9Kco2llNHBMf4P41BE9GsH5FtnFVKF18TsjVFzIIWibuicc5VVhIkib8sRQ1DSSCzYqY/640?wx_fmt=png&from=appmsg "")  
  
4.发现接口文档路径和druid的登陆页面，这里我先打开druid的页面看是否存在未授权或者弱口令。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj55oBPjWoQoOj9KvHSNKHJTqH03do1pORkmbwnD1el7FsCtvCLflMRibqMa2BKjIdALPUiaKt4wCtz422E76ldibs9UgH3tGWibxEWo/640?wx_fmt=png&from=appmsg "")  
  
5.好吧没有未授权，但是存在登陆页面，只能默认密码或者弱口令爆破了。结果直接默认密码登陆成功了，成功拿到一个druid的弱口令漏洞。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57hzlsHxSepJgZVkP8gwXKQCDibrtRNX1UVdNdTsoQF839zCYxnJRFXhb1vAJNGm6lhTpvmctdtzgXBhRR14lDSEVWdDfOVSeHA/640?wx_fmt=png&from=appmsg "")  
  
6.然后我就想能否找到后面页面，通过druid的session监控里面的session爆破session登陆到后台，可惜并没发现任何后台地址或路由信息。到这里只能放弃了。  
  
# 0x02 组合漏洞xss：接口未授权访问+文件上传+xss  
  
  
1.根据前面SpringBoot敏感信息收集的swagger文档里面，我找到了一个文件上传接口（存在未授权访问）。由于是一个jar包启动的项目，他不像tomcat中间件启动的项目能够解析jsp文件以便于我们获取webshell，对于这类java项目通过文件上传的方式获取shell是不太可能的。于是我就想能否上传一个html页面，实现一个xss。请求包构造payload发送结果如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj56MgXOxPn7hnE5Hj2HBeUdLNUBabyAZQJnJ0FrLC1xKQ5SXR2rgBnAPR39zZ6ViacEStCUNiaCjXCI7beIt1Dk882Gvbza6wt3kk/640?wx_fmt=png&from=appmsg "")  
  
2.他是一个图片上传接口，但是我将后缀改为html是没有任何校验的，得到这个返回结果发现只是将文件名重写了并未重写后缀，访问页面，成功拿到一个xss漏洞：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57ia8YbOPJ3lchYkicsicN12cuIpEmiaT2kbQhZ0Zic8UN7w5icSoe2ic80Z9ibqSU7yu4MicLiboeibvJT4J7DQPrwpicQw0m3qdTQ9TkXJYU/640?wx_fmt=png&from=appmsg "")  
# 0x03 java组件存在ssrf、任意文件读取等多个漏洞  
  
  
1.swagger文档没有获取到其他可以利用的点，跑回前端对前端代码做一个简单的审计（主要目的是挖掘更多的路由、url、资产地址等），这个位置存在了大量的接口地址信息，并且有一个地址很独特，看名字像是一个图片预览地址：/preview/onlinePreview?url=  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj54pLSiaCARfBcyF5WjumDbibBBxICLtBT3tWojkkX38FPKicsXUDibumicKUa8ZTich3SsIhRbXYvBXqP5UIEaZS1ynFhA53AhhV7ibyA/640?wx_fmt=png&from=appmsg "")  
  
2.访问地址/preview/onlinePreview?url=，页面如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj551M9ibewYFCfwqeJ5ZrZzrdRjgUqj8YicroqOkgvwefFKmBe7hl7pgsqvlTiaHppKwPHuvibJYIwQ5uouiaYRPwD2PNN5biaZQY37Tg/640?wx_fmt=png&from=appmsg "")  
  
3.直接拼上百度地址首页图片是springboot默认页面报错，虽然是500报错码，但没有具体报错信息，无法进一步利用。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57dKScsmEutArZWibBrNYibUSsEJOS4zKV3O63SO4iaRKQw0yBj83V4jqjd7f0jceYVrqia6nIQjIeSYTbztpgHhFDpLd14DpPM0fk/640?wx_fmt=png&from=appmsg "")  
  
4.然后我就去掉了url参数意外发现了报错信息，这里比较关键的是这个包信息：cn.keking → 进行进一步收集发现是一个叫做**kkFileView**  
的java组件  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj57icOb8Hg2udFenoxO9omE8sFtB8zyraMPBBvD01hWrRo52BaLjYpnWpibSCq4PNG6qib8TbPTqQ6KQqLzV1HVMccKuv7AkI5z12U/640?wx_fmt=png&from=appmsg "")  
  
5.查看官方的文档说明，发现其是一个单独的springboot项目，并且存在一个主页面，上面会记录其最新版本更新说明。  
  
思考：如果我能获取到目标的这个kkFileView服务主页面的更新说明，能否根据其版本信息查询到一些历史漏洞呢？→ **最终得到其版本信息为v4.0.0**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57jwHbTLNHnB3WPZOb1iaXK33BBOIRvWicMj5xy2CfMK48M3rcYjC2JibE9l5S2TkVHCl0ibtZ1mEkZSfsPNyn2An8Uib94Lnx6WNaY/640?wx_fmt=png&from=appmsg "")  
  
6.收集版本对应历史漏洞主要如下：   
  
1）存在zip slip文件解压进行文件替换造成的RCE   
  
2）SSRF   
  
3）文件读取  
  
  
（第一个漏洞危害有点大了，他会替换文件，实在不行再考虑利用）  
  
## 文件读取漏洞  
  
  
这里我们主要是用了ssrf和文件读取，最终利用成功，这里我读取了  
/etc/passwd  
：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj574icWlxdKh8by1l0FOIyEyaN5pEDOpouicf0IhfJefTfZIib7BQWQFMMLQqEenPSG2aTibKVGKN0yFKFKcWHSn9Myqic9JbxAjUeb4/640?wx_fmt=png&from=appmsg "")  
## ssrf漏洞  
  
  
然后读取云服务信息，这里通过whois查询发现是腾讯云服务器，读取元数据信息：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56KkwfvtClskEscmdcfLF5RRFcTlX64iatEX2yq9INyNPzY8sGVE2QCN4gueuMGuibgF3qHicSE7uIibsEbT37BOZWvS8kiaRkyn2aA/640?wx_fmt=png&from=appmsg "")  
  
后续我想通过元数据信息拿到accesskey接管其账号，没有利用成功（有厉害的大佬可以交流一下），貌似其并没有开通ram信息接口地址等导致我无法获取临时的token。  
# 0x04 通过文件上传拿到webshell  
  
  
1.最终我还是想拿到服务器权限，有没有什么其它方式呢？ → 把想到了办法都用了，搞了半天，最终还是审计源码给了我突破口。  
  
  
（分享点小经验，当找不到服务源码具体路径或者其它文件路径时：不妨查看一下.bash_history，说不定有惊喜）  
  
  
2.通过file协议对其服务jar包进行下载，反编译后审计，找到一个文件上传接口存在路径穿越：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj57YSF4wPFmglwNpaC2NjHJJkozAIgXqW1aPibMvUxZkrqOe2zia3ictbmqmRZjVMW1dic9qpIGRE0ErIUvJFdSlQ7OasWyWy5V4xVM/640?wx_fmt=png&from=appmsg "")  
  
3.第一部分path是获取的config.properties配置的路径信息，第二部分filename是file.getOriginalFilename()获取的全文件名，后续代码并未对其进行过滤直接进行了路径拼接。这里有一个问题：如果存在文件名为../../../，将会达到一个任意目录穿越的效果，最终形成任意文件上传到任意目录的一个漏洞。  
  
  
  
4.这里由于前期的信息收集，我是发现其存在一个tomcat的服务。于是我利用这个任意目录的任意文件上传，上传jsp后们到了tomcat服务中。数据包构造如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj56rZskP63Kg7ibJrSza0iaicCNou3FERyehRKhe4qyasUzUJHBhZKPjZEB0oGIBSiaFP8CsU93YDnY4rQU0qLwsv5KL5zvC7dUFf1s/640?wx_fmt=png&from=appmsg "")  
  
5.通过哥斯拉连接后门，成功拿下服务器权限：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56LGgoKPz70o7b9WoN0gIadZhv1PUeh2tDHBzWpfwc9YJFLnksahic4Whl7QibJicbVUVoE7iaiaCh6qSGTVTCGUNtE3bhkVTMexalE/640?wx_fmt=png&from=appmsg "")  
  
原文链接：  
https://xz.aliyun.com/news/91668  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/VwaIJp80uug4IfOOz8QDT8hlhwrxRjonkLYs9zAzodxhicEqQFaVRO6RZJ6pjx3x9752hoicFhHlmld2znUIqmSA/640?from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2 "")  
  
3月技能成长计划  
  
🌱   
3月技能成长计划，今日重磅开启！  
  
🔥 7天限时狂欢，三重好礼等你来拿！  
  
  
🎁   
报名即享：最高立省  
4700元，加赠  
实战专题课 + 钻石学习卡 + 京东卡/瑞幸卡（二选一）  
  
🎁   
直播福利：免费领取  
《2026面试宝典》，助你职场先人一步  
  
🎁   
推荐有礼：  
邀好友报名，得大额京东卡，多推多得！  
  
  
⏰   
活动时间：3月12日-3月18日  
  
👉 立即私信老师，锁定好礼名额！  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj54EmMJ7PQzS4yUxQpvvTX80y4DRdCuv67jibfJvLgbVkyFkgnnnmvj2SjAWrS9SSYkh0Offonm6HM5WfQkgQRebeNVibzuib2b9Ww/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnzUZSPvXhVfSqMdycgzQNticibKVKkmlzZLP2DUgwGgOicCNjooP2mY2cSjhia7tW2SPpJ14Ued1q6eg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21 "")  
  
  
