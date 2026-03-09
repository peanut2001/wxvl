#  记edusrc&src任意用户登录漏洞挖掘技巧  
原创 陌笙
                    陌笙  陌笙不太懂安全   2026-03-09 09:19  
  
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
任意用户登录是渗透测试中常见的一个测试点
借我好兄弟的两个案例来分享一下挖掘手法
```  
  
挖掘前置  
  
不文字描述了太多了结合我总结的思维导图看吧  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ1XI1DRQicwB0JAynH8U2rEyM5aQKIsZI1De5AR1dPtHDFq6NC6md76fGHWeuXPloNUvk1rlPicYYgAO3zo0LLW13llScyOlqXQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRO9ZsGMwJTOEyAe5cjtUqetO9HDHg9NUHnedRBepm6Bq4uaRgqPtMvEKTXdV1Ijg57uc9YwUFaKdzY34cEF1f9Yo7mmoM8CWw/640?wx_fmt=png&from=appmsg "")  
  
漏洞挖掘  
  
案例一：  
  
正常信息收集，直接小程序搜索对应大学名字即可  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSjSWahDrBZYgrRH4QkyWicBZhy1KicztN14db5GBh2vicIzqdN0uhtMm4hRvicCgnEa4ib10e6mP5GtK84D1jq1MBm7XpMF65jSaL4/640?wx_fmt=png&from=appmsg "")  
  
拿到小程序点击进行登录  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSqGKtZjia3YHzwFFaL42mVDgHYtr9QGvEovlIBBKyJSUzm3DCySEI6t61OazufeSP693ylwTicQoZod93H7cgH5al8LjslWWkrc/640?wx_fmt=png&from=appmsg "")  
  
来到一个登录页面，这里可以结合登录口的一些测试手法进行测试  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQdaViaua7R1CQ8KOdvYh0632JMyOFnu9YFSc8Gp4tdIQh2K144Eeb9DQfPKBnYsJ2w7rpYOoO07mTqZEGBJZfBIlYMo1C9PeZo/640?wx_fmt=png&from=appmsg "")  
  
因为这里是小程序，直接使用快捷登录进行尝试  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTowDhWbpePP9NMKOc4VPahuFGzGJCibLa90YibaAdIJ6mmmoSjw9XPqrcV2SGicThsY7tffsuNbCiaNZ6VQpvsok8Lh7ZlI6y5W04/640?wx_fmt=png&from=appmsg "")  
  
点击快捷登录进行抓包可以看到这个数据包，看接口就是获取token的直接放行即可。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQOGeN3RElSZvPSSzk7VialNX2PCgf6MHVfom41DkZE4nNVakMlJGzPeY5cp3zkia4b5SeWeW6k1v5h6nmw1eiaRhetsZgKCnETiak/640?wx_fmt=png&from=appmsg "")  
  
然后来到第二个包，看接口命名应该是获取手机号的，拦截这个数据包的响应包  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSpzYI6IXHRAydrHWMna4dWcorHsicNsnLVgwReVWUg86rNlQiaSIIriaDtN8LlB5D9xQibA6micCP2wf13ouCPq8eLxP6VHiavkaHzI/640?wx_fmt=png&from=appmsg "")  
  
可以看到我们快捷登录的手机号  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTO91M0syv29YtYbZdciajvngLRluKQVvVmO3fSKaxibGcicTiaShG543pUdS5XLxolicB6I2iaQIya1bIT5dpTGTzqOgGcEWtD5LfNE/640?wx_fmt=png&from=appmsg "")  
  
将手机号修改为我们另一个手机的手机号进行放包  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTBhjtYwek2nu36PqZaVJ9lRtL12YbMw0yFdzhtJ4785SKR1EtOu98ic7nicLBwjZEbQpiaxWOmmZuf6ZuUMayBJyf0E5fa7FI5LA/640?wx_fmt=png&from=appmsg "")  
  
成功修改后的手机后进行登录，功能可以正常使用  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQWZ0oP2IVKR2PcLTzNG2qcNI61TN7Yobq3v65Zvy5T7Bm5ia1fOATShm59JKMHwrtoM6ibLXj4GpxscPxVMIVzcWxxMrRukGjGo/640?wx_fmt=png&from=appmsg "")  
  
  
实际测试过程中，这种情况很常见但是大多数都是，前端欺骗，修改后这是在这个页面显示的是修改后的手机号，但是其他功能信息都是快捷登录手机号的，这个没用不收，如果漏洞确实存在，可以通过google语法收集学生领导手机号进行测试，看实际信息扩大危害。  
  
案例二:  
  
依旧小程序起手  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTAw0byYwicyrqG69FR4iaHiaph19woEXsfmCzNBg1weIpHmm3qwIrHL5wuPiaUQI39f7KKKg2uEb54XRRwXfY2HNl3DrSJwg043lU/640?wx_fmt=png&from=appmsg "")  
  
点击小程序可以看到快捷登录页面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQy1kgRwwwI3K8uUs45Orh6oGNiar8rbmQuqSmMFRFMAfXsJE5ykFaOHx2fHoZCQV22HhjSclCB6108U8EFEA1q8QJ5iajlibAh3M/640?wx_fmt=png&from=appmsg "")  
  
点击登录进行抓包，放第一个数据包，看到第二个数据包是这个  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQXozSlNMHhzDF6S7G7pf49JTE7HA32fw0mDR8eravwaSIvVxjBowJHMJI71bEgQ01orHzJQ3Sc67ic1fz9DCt4y1aEFznr23H0/640?wx_fmt=png&from=appmsg "")  
  
拦截响应包，竟然看到了userid，经常挖掘越权的师傅应该对这个很敏感  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ1FbmPIYyzrBbLTCEqTiaZPE29mO1nMT1nWlnUTibOHdo9ibsZ7Rj4cLbuticicy6cuH6NKwRgoKRh5YeMKXU17T3Z65nF3JaVyxw8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR6ZTnEwTSiaJIumOwaicxHKpFsugXsgHgPmA1IRia6CnjDUo4ibH9lvayzAh0icQr0xlT2MbZc1O7frHaz7mTFxZDWCBBvBXcZEoF4/640?wx_fmt=png&from=appmsg "")  
  
可以修改userid进行测试  
  
因为可能不只在一个数据包中出现，直接使用bp规则进行替换  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQAUCKmm58cPJSkLSLibuax0wJFibDoFQkHwQIbb70fFibeYxBxPkq5OmVgvWt38dbSHZ7u58Wuibo1AoYbziavekqYFvKGH26hpgdA/640?wx_fmt=png&from=appmsg "")  
  
之后点击登录，成功使用他人身份登录，进来，造成任意用户登录漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRGcHia7vdr1IAhDXyibRUBHqmhgot9Pwib7y67jYDFQ4pQCzRzqxmftpALB5LwicEI4k59dkRmD4o6uyztIPToI661cy0JgGOH41g/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ2T2n8jT9PDYafuxLzbOh3zn4vDAgGS5WkOticuyI25TYrXWMTnfy6XlBATkeLtM48jxKrpzeggTI2hdtWxv8xtXH8Oy3v8VJw/640?wx_fmt=png&from=appmsg "")  
  
总结  
```
场景还有很多思维们可以结合思维导图多多尝试。
```  
  
  
后台回复  
加群  
加入交流群            
  
广告  
：  cisp pte/pts &nisp1级2级低价报考，货比三家不吃亏。                
  
有思路工具需要的师傅可以加入  
小圈子                                               
  
主要内容是（2025-2026/edusrc实战报告/思维导图/edu资产/漏洞挖掘工具/各类源码/ctf&src学习资料等）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQLW5X2q5ibOoTBfZeBTd8b8fCht2b9CSdmibG305NblA0TPI3kg3D8K02iaPBSEU3zpicppUFr1KrMuCWtpRIOiapFrl5J0HLV1vY/640?wx_fmt=png&from=appmsg "")  
  
部分思维导图展示（会根据自己看的报告自己学的内容进行更新但是不会是日更），其他内容可扫码查看。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQ0vRSQfUtaGWJ7K28K3QafSEib6NpRQTVCQCcq5qqicnzibv4cqoEEZ6cDzDaOTofjskmRMIozbRC68RgX5CBYicIJOtiayQeTT4PQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQibpWs0DjVyrica7aQ69miaHcL2g62EeroFVERMbljhHgtJADKmZa2CxiaHhBDM1Afdib1wUn2C4LD2J3T9qqNTRvt7WG2cnmMxE3M/640?wx_fmt=jpeg&from=appmsg "")  
  
其他内容懂得都懂，可以扫码查看详情，目前450多条内容，持续更新中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSbY9iaDZ9UMr1zGr1VJPNmGbiadDGnY2UoCOmicw9g7CbWt5HOKNKiamG6Cr6cK3eicHSjfNibRibS9Ksqz5zIF4nVWnWtY7bMAS7bFU/640?wx_fmt=jpeg&from=appmsg "")  
  
