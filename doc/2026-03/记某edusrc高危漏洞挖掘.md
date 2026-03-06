#  记某edusrc高危漏洞挖掘  
原创 陌笙
                    陌笙  陌笙不太懂安全   2026-03-06 10:16  
  
免责声明  
```
由于传播、利用本公众号所提供的信息而造成
的任何直接或者间接的后果及损失，均由使用
者本人负责，公众号陌笙不太懂安全及作者不
为此承担任何责任，一旦造成后果请自行承担！
如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```  
  
前言  
```
依旧登录框起手
```  
  
漏洞挖掘  
  
通过信息收集来到这个登录页面  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTw4U8r1aJ3IDya21k7QBOE04rxf2Qc9Wwx1FYuWtJ2AZC0hADfzabH3piaSOjicTNpePTTqoSUeqbEHmTic95NNyhe2QDS2ia6yG8/640?wx_fmt=png&from=appmsg "")  
  
使用常见的登录框手法进行测试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRvRibI1icwwicate250eAofo94gEwgWflEYpG3w9KVadjlpviaVmyml9m6xXB1iaSqzBO0Eqo96zeSCCXibfCbLOyzeCOoKe4Sic03BE/640?wx_fmt=png&from=appmsg "")  
  
针对当前的场景可以使用红色箭头的对应模块内容进行测试，本次突破在登录口常见nday -> 若依  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQoLQl641h4TFDM11VwvwjAbwIPMibZTmiaS6gd5SicTzibcVmeIO1Zh0IxGC0iafZibkOgKDjhm1Blr5lUZoSlgJS9iajmCl81xyMG1U/640?wx_fmt=png&from=appmsg "")  
  
如果是批量信息收集配合探活加指纹识别ehole应该能探测出来若以框架  
  
如果是手动测试碰到这个页面了我们可以通过一些特征来确定是若依  
  
比如这两个路径一起出现的时候  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQTxMTsxt8iabPmcWrQgjIXj8icVzyicE1jsfZj5OLlYJcnYJNiclUaJEGraSppq5VME9p6Seue1vzp81Uoj9lVqS4z6sn98CMGVicM/640?wx_fmt=png&from=appmsg "")  
  
或者直接查看源代码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS3zCLvN3q8NguWicq9CnM4brKHh3JlSWIfOibg0bTKsuRZvxap5Jia3oLZ4uc7wibQ0ksryOzibW0g5XcnOia2J9gXUkwVo376JbDqc/640?wx_fmt=png&from=appmsg "")  
  
也可以直接搜索ruoyi相关字眼,这个方法最好用。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRx6SlgSkKQ4EicuKiaiaofjodWuPYicrgfiayrZkpgfl9uHX36ukiaKb5aQWZhdeoDl1xicQwNVfslFnOS9kjTSrEs67Z7aom18uK9iak/640?wx_fmt=png&from=appmsg "")  
  
更简单的方法，直接使用各种指纹探测工具进行探测  
  
密探  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSctBiah8awWmIlaZuaic4ib8t7o2no6k1bNkhCtMDfffvCpQwChWZSpsEE7zuSNbMvpMRXzVWT1YxqaFmJte70FzsY7qXvCrEGu0/640?wx_fmt=png&from=appmsg "")  
  
tscanplus  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQbeicZHlSJenODQsKI8XPeUrGQXKFbW4AfdCCibgogkJ1O2tRA1Kq04gpemcydalLDcFgdX1caeHY3B7ib9T8w2XFcicFpKKPRLU8/640?wx_fmt=png&from=appmsg "")  
  
ehole  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTOKODI3lia5sxOaC1JY5UKUqsJey4J84xRBWUMD7CsaoyDxQ8mzj9G2Y6yeQe2JVXM7MuYN4GwVzRLbZSXW088gSGDXIaABia5o/640?wx_fmt=png&from=appmsg "")  
  
每种工具效果都不错，选择一款适合自己的定期维护就好。  
  
其他识别方法可以看我这篇文章  
  
[若依常见漏洞一把梭（上）](https://mp.weixin.qq.com/s?__biz=Mzk1NzgzMjkxOQ==&mid=2247487289&idx=1&sn=743528ef3e4a15b397cd42c08a5b3ecb&scene=21#wechat_redirect)  
  
  
开始测试  
  
使用工具梭哈一下，啥都没有  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTARbq4t6khbWEl290NU5pVDnATdSvThOrNvfKMFUpGb6XlibialmzVCUF3fvkd68TTMcRS0ecSEiakO2tDDCMSLXttVvtCrq5ibmM/640?wx_fmt=png&from=appmsg "")  
  
手工进行测试  
  
手动打一下nday  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQuqxzChBSAXJE8B1dpVNhrpILmYfw60mxeudkOu4I6jhJjdTW8Mn7Lpevb0JO18jQ5ib1ZUrSYpOxZj3dK5mpZVNXtRrSibibhFc/640?wx_fmt=png&from=appmsg "")  
  
发现出货了，任意文件读取  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR9BpHzTUicsbCJp9mJOLPbiaW2gLXE3p4Xt9TMkVzic6RH7JmWDRkqttS3mDic4DECd19MTjhdoF8p4NTfJmNoIich1G1xBxPPanJs/640?wx_fmt=png&from=appmsg "")  
  
继续测试，使用ruoyi常见目录进行扫描，可以使用字典配合dirsearch啥的扫描工具，也可以直接使用曾哥的spring扫描工具进行扫描  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSu98Hf7zwnta2doQkb35OMDIOROVb0AoHH6bkpDnZTwag2NLAC20iavmlUicrnT00Gja2XyrWXOv3K539mZFQW7bqXHQjRpONhQ/640?wx_fmt=png&from=appmsg "")  
  
发现druid未授权  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTYzib65lk9hXOJSH3kg6tpcXt9yRAIj2uQVSbvibVwqdB4bXAz7ypKdfEhpFficibLW576Eze3XWtt6AR837icdBYdbdblNfVbLTibs/640?wx_fmt=png&from=appmsg "")  
  
swagger文档泄露  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQgwbSzib9IyeFtB2tpkyibZxMxjibGhicQf9icM0HrC9OtLCLYnPl3jSmZuar5fzrWpibNziciaZwiaYFWzVU4fYz7as6hVbhIzYp5JLKY/640?wx_fmt=png&from=appmsg "")  
  
尝试进行访问测试，看到了几个比较有用的接口，一个接口其实就是一个功能，直接使用yakit抓包测试。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRpVvZyLia3PLkfFyu9JQp9yz0WUCyYjxgf3aictqmY7oTOrA3mdLfxoMzNZS06rTM2wCCu94mVb0dQ3gV3RbbljZn2fdqu5JoJI/640?wx_fmt=png&from=appmsg "")  
  
查看系统用户  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRNAxibH6zDeUic9r1GLJ3S1WI7sUUibicKQtncvcibfLYX6PRWIotx6da1JNKpe0WLSVeNEPoMaEoibBFAtVc2k8orHZKzEQeZ7UNm4/640?wx_fmt=png&from=appmsg "")  
  
尝试增加用户，直接成功  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRo3PTde7f3dibj8JXh5VCuWCLBgfMMnn5ibpfy2ZCpFMfwkFlhNJZicrt2PUAFvQjwibVISwosH5pPmgNz5zU8LricpZCaBhGW7tzw/640?wx_fmt=png&from=appmsg "")  
  
尝试进行删除，删除成功（这里路径一样但是方法是delete）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTr419zWRTJ6AOruyustOWeTSBjjcVNtt3ToCtczJGHPhkic18E1cBJLLHpd8TI2P2xe53ffIPjpruAaRseuwPCcBE48uQFfkb8/640?wx_fmt=png&from=appmsg "")  
  
又来一个未授权，后续可以利用弱口令进入后台继续深入测试，打打别的nday,不在一一进行演示。  
  
可以参考这两篇文章  
  
[若依常见漏洞一把梭（上）](https://mp.weixin.qq.com/s?__biz=Mzk1NzgzMjkxOQ==&mid=2247487289&idx=1&sn=743528ef3e4a15b397cd42c08a5b3ecb&scene=21#wechat_redirect)  
  
  
[若依常见漏洞一把梭（下）](https://mp.weixin.qq.com/s?__biz=Mzk1NzgzMjkxOQ==&mid=2247487336&idx=1&sn=e110f44e7d47bf138735038afad695c8&scene=21#wechat_redirect)  
  
  
  
后台回复  
加群  
加入交流群      
  
广告：  cisp pte/pts &nisp1级2级低价报考，货比三家不吃亏。          
  
有思路工具需要的师傅可以加入  
小圈子  
                                         
  
主要内容是（2025-2026/edusrc实战报告/思维导图/edu资产/漏洞挖掘工具/各类源码/ctf&src学习资料等）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQLW5X2q5ibOoTBfZeBTd8b8fCht2b9CSdmibG305NblA0TPI3kg3D8K02iaPBSEU3zpicppUFr1KrMuCWtpRIOiapFrl5J0HLV1vY/640?wx_fmt=png&from=appmsg "")  
  
部分思维导图展示（会根据自己看的报告自己学的内容进行更新但是不会是日更），其他内容可扫码查看。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQ0vRSQfUtaGWJ7K28K3QafSEib6NpRQTVCQCcq5qqicnzibv4cqoEEZ6cDzDaOTofjskmRMIozbRC68RgX5CBYicIJOtiayQeTT4PQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQibpWs0DjVyrica7aQ69miaHcL2g62EeroFVERMbljhHgtJADKmZa2CxiaHhBDM1Afdib1wUn2C4LD2J3T9qqNTRvt7WG2cnmMxE3M/640?wx_fmt=jpeg&from=appmsg "")  
  
其他内容懂得都懂，可以扫码查看详情，目前430多条内容，持续更新中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSbY9iaDZ9UMr1zGr1VJPNmGbiadDGnY2UoCOmicw9g7CbWt5HOKNKiamG6Cr6cK3eicHSjfNibRibS9Ksqz5zIF4nVWnWtY7bMAS7bFU/640?wx_fmt=jpeg&from=appmsg "")  
  
