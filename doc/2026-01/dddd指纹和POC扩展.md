#  dddd指纹和POC扩展  
安全艺术
                    安全艺术  安全艺术   2026-01-25 02:03  
  
写起来其实很容易，可真要坚持写上千个呢？写完还不算完，最怕扫出来满屏误报 —— 怎么精准揪出这些误报？又该怎么调整优化？今天没改完，明天保不齐又碰到同款问题，持续挠头？这两年参加大大小小的护网，还是硬着头皮坚持写下来了。多少有点强迫症在身上，实在看不得上千条资产的扫描器里出现一堆花里胡哨却没实际作用的指纹，更忍不了扫出来的成百上千的POC里夹杂着大量误报。  
  
这套法子，专治跟我一样有强迫症的渗透师傅。当然，也可以直接进圈子 “抄近道”，现成的资源直接享用。  
# 1. 收集指纹导出资产，如fofa等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KfhJ8QugBqZubuADK4kr550aInWqoKjpWUEMDclVgyQmnSyVP5PIg5Q/640?wx_fmt=png&from=appmsg "")  
# 2. burp批量打确定响应规则  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KPVp1p6WwialMsibSYsTqiaPE1cicRUT2SVAzeQeWQwrr0pibKovalPfS6Kw/640?wx_fmt=png&from=appmsg "")  
# 3. 编写yaml脚本，自编或者交给AI都行  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KjJZBRF8uOU7Ulzs4ncXW5CymaStarXIdicXm2hgG6bg9md87r6dg0cw/640?wx_fmt=png&from=appmsg "")  
# 4. 不断实战优化【持续性】  
  
持续奋斗一线吧，再好的工具也要靠实战结果来证明，在实战中不断优化指纹和POC。  
调试也很简单，  
借助dddd的proxy功能代理到burp中。有手就行，还是那句话，改一个很舒服，连续改100个，改1000个也许就允许误报发生了【🤣】，有强迫症状的师傅们还是要坚持住。  
当然，也可以直接进圈子 “抄近道”，现成的资源直接享用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KP5uWTEOEqRyDKRuQV8jF8g7sJibK5QMUrMVCkC459Jg7ric79XOzamrA/640?wx_fmt=png&from=appmsg "")  
  
安艺圈介绍  
  
圈主介绍：  
  
十年安全行业从事经验，多年攻防渗透和SRC挖掘经验，聚焦于实战思路案例集锦，基于实战的dddd优化版，多次护网中斩获上万分记录。  
  
知识库内容大多来源于多年攻防渗透工作经验，实战漏洞挖掘，漏洞利用思路、工具和案例等，严禁用于任何未授权扫描测试。  
  
圈子面向对象：挖SRC和打攻防挣钱的师傅们可以考虑下哈，单纯工作就没必要买了。  
# 1. dddd维护  
  
**选择这个工具的最重要的原因就是先识别指纹，然后根据指纹去扫描对应POC，高效高质且维护简单。实战配个代理池，产出还是很可观的，记得第一次用它参与国护时，第一天就进了某央企运维内网。**  
  
一张图看懂dddd运行原理。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KNJqhw2BgH6NNxd9V0yxwp83YwtZ8t3W2xib9Zbd5nLFElHRtR2UGc1Q/640?wx_fmt=png&from=appmsg "")  
## 1.1. 指纹POC  
  
**所有指纹POC均内置了。**  
  
集成指纹POC（基本看到新的就立马更新吧），workflow（纯体力活）和POC优化（误报太多，陆陆续续  
优化近3年了  
）。目前指纹数据: 11219 条，漏洞POC: 4710 条，workflow：3504条，目前应该是市面上集成力度最大的了。  
  
杂乱无章的指纹实战中不断新增，排除误报等。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KYcjPlDHPrtZjn22VpMGcHFTjvicbCfzx9PHM68shSarWMJ0JayBMh8Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7K58hJd6EHJ2sjHdSia3Em7ywg0tticzTdib76uRw9bYeCNK04Q6RtRpZdw/640?wx_fmt=png&from=appmsg "")  
  
**workflow（懂得都懂，纯体力话，也是坚持写了近2k条）。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KFW1icic8NzLl74clLjnRlLpYwibUoukDWxuNicGgJkaojrEncn4v6weClA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KIenBZsbRzN3P3WupibpAR4CYqcXx0xIP6RBPEyYakNjKWLd5YsUwm6A/640?wx_fmt=png&from=appmsg "")  
## 1.2. 蜜罐排除  
  
思路很简单，指纹识别超过10个默认是蜜罐，不进行任何扫描。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KGicgMOtLvNWuzficxBpnEArlicPcPGdhjg6f6jwn0HGPHTlvkqk6YBxNQ/640?wx_fmt=other&from=appmsg "")  
## 1.3. 指纹优化  
  
很多指纹又臭又多，基本没有poc可打，在两年时间里基本都删除了，保证扫描结果更加实用，不用花费精力眼里在无用的指纹上。同时，合并了很多公开的指纹库，也参考学习了很多付费圈子/星球的指纹库，但是合并后会发现每个指纹基本都存在重复内容的，最终还是需要进行去重处理（11253条指纹）。一个表格告诉你合并后每个指纹都至少有2到3个重复。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KkIMYs9wDtacZOOXl03EO07Arb78SyJBpjKSIqO4wibF840ZzIUyQm8A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7Khybiaa0TQ8ZZsUxuyRYZBeKtgI0Rg9ISUa3GHJR5H7rTYIV15BCzLQQ/640?wx_fmt=png&from=appmsg "")  
  
及时优化指纹误报，减少眼力精力损耗。这也算是一个强迫症患者吧，误报看多了，很影响心情。  
## 1.4. 目录指纹  
  
网站目录扫描：这块主要是针对SRC挖掘和HVV项目中碰到的比较多的需要路径信息的指纹进行补充的，新增了很多发现频率非常高的springboot相关的接口信息，并通过指纹信息精准匹配，基本扫到就可以进一步利用。  
  
网站指纹识别：这是圈子上线后来着圈友的需求，网站指纹识别输出，原版是统一输出的，没有任何区别，改版后新增了重点指纹（SRC和HVV漏洞高爆发点）高亮显示。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KlOnm6BvxLafZmY3dAw8uCW1ibZJJuELOCNNp4nuRqiaR7YNmc7fa6XeA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KIfZvYa1YpdgsicgCy3IImzibYIQ13PUKBK60X2OZq5zZxsrSDquXt72g/640?wx_fmt=png&from=appmsg "")  
## 1.5. POC优化  
  
主要基于实战进行新增或优化吧，以Nacos和Jeecgboot为例吧。  
  
1、有些Nacos版本需要加入一些  
特定header  
头才可以正常访问（回想下自己是不是错过了很多Nacos的洞）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KUu5ic7NWHsN1OrSCNjVQsQXW33rvWvvHaibC5icgBQ5ibQQiaGndRsofR2g/640?wx_fmt=png&from=appmsg "")  
  
2、jeecg-boot-jmreport-qurestSql-sqli（添加绕druid防护机制的poc）学习代码审计时看源码审出来的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KPtnvc6XMvyORAYZgjm6TCNGC0PQfamzquxy8BMjaFCz80DvsXD3BoA/640?wx_fmt=other&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KzEheSUAz9qGJWOQQJd67ROaJDvBibQM83gQp7ZXbTUdOLbOJFj00h6Q/640?wx_fmt=other&from=appmsg "")  
  
以上相关POC都已集成到圈子版的dddd中。我记得有圈友问过优化频率，这么说吧，一般发现问题都会及时优化。主要是我在工作中也一直在用dddd的，再加上具备强迫症，看到误报就想立马修复吧。  
## 1.6. 证书问题  
  
扫一个站，出现一堆站。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KeRYLCdjDOicAY069592cRtFibraDdRjpicpum6cv1oOVf62t1rN0HnjXQ/640?wx_fmt=png&from=appmsg "")  
  
优化（也好也不好，之前这样扫出过某src的一个rce漏洞，但也仅限这一次，所以考虑还是false掉吧）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KR0FXFwaGkIuibHeMt43WHr9GJIGPleediaXwmtZxM8icPugvz1aK65HWw/640?wx_fmt=png&from=appmsg "")  
## 1.7. 重定向问题  
  
是否跟随重定向，默认改为false  
  
false的话，有些OA默认跳转的，这种就只能加目录扫描识别，否则直接识别不出来的。  
  
true的话，挖wps的时候碰到过一种情况，https访问跳转到http，然后http访问就会超时，http拼接目录扫描就一直超时，但是https拼接目录扫描直接出了nacos的系统，然后还存在漏洞，差点错失一个高危洞。有些系统会跳转到非目标域名的其它系统，后续扫描也是浪费时间了。  
## 1.8. 顽固的JieLink+智能终端操作平台  
  
JieLink+智能终端操作平台指纹+poc会触发workflow报错。  
## 1.9. 默认拼接路径  
## 1.10. 目录扫描bug  
  
只拼接了根路径，目录路径未拼接。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KjE7OAKXGlfGd9CVzglwcQrU5JMDWZFyBzOf8XHcHvAqDstEXXkVHoA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KbPKLKLk0nJXSmV0Q2LLcs74AtQFSKiaOrzNs5pJSJmLGichMwd8MmH6A/640?wx_fmt=png&from=appmsg "")  
## 1.11. 运行死锁bug  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7K6UhJ1EBXeNicEUocmlEuooaR5OoVDtWUWPTa5ibmiaSktbAX2Piclxv4Kg/640?wx_fmt=other&from=appmsg "")  
# 2. 知识库维护  
## 2.1. JAVA代码审计  
  
自费999元跟班上课学习记录从0到1完整版。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7K1Mdja2sSy1PDMBxynsI5Zo21lhtUIxrKKU2vtAMXaCDR7icIHDvaROw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7Kk4hibkrpwXw5Woo2noicZrdhvGvhCgaIAibyfNw2E7HWAib81AkyMnyloA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KCC68qc5UFkZGJnZfzaibjkUsfztbibicsYU5xkoFPZRcvwd4G8lFjETyg/640?wx_fmt=png&from=appmsg "")  
## 2.2. Nday漏洞POC  
  
各种渠道收集整理的POC，公开的和非公开的等等。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KQVVCSJgD5dez0qyEgCxVAO7zrJga2d4nSmoJFPib878lRdqOrfSh2Sg/640?wx_fmt=png&from=appmsg "")  
## 2.3. dddd更新记录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KqPKRTic3jr9pcn7kRicicugvARicxl6nyQAicQKUR4ic5fl205ngt7vx5iagg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7Ky9XVMgpnU4BFU9C6O3LfPVEP4jAmnM5F7m6ia5YRaS3V4FJgggaxDCw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7Krl4vsqLKmbOccxqUfG2icPuzFoUDXEEdfO4oJzWsJj7o1zLicLe8RIgQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KSDaGpZNeQGFat6hicicR3JaTZOFPnibG7GGgNgp9ibAsKwLBH0ToaNJCWw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7Kz5kXBEHRCfwo5Lf9Y8xCjFHIqPib8YTwDv9q5NXSzHUoN3h3ynhuwicg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KhnCicChvXZvBYQUtJgSdvWPCLTrzW6e5GnAlUhjfibRiad7Co0OZr6xDA/640?wx_fmt=png&from=appmsg "")  
## 2.4. SRC实战记录  
  
目前SRC小成绩：猎聘和蔚来汽车SRC总榜第一，WPS、自如和货拉拉等多家SRC年榜前十。  
  
圈子中关于SRC的内容全是本人挖的，对以上SRC感兴趣的师傅们可以多多交流：  
  
**1、分享**个人**SRC漏洞挖掘完整过程，包括不限于漏洞挖掘思路、漏洞挖掘完整路径等；**  
  
**2、分享自用优化的burp插件或规则文件以及实战总结的账号密码字典等文件。**  
  
个人SRC实战案例，案例来源猎聘、蔚来汽车、WPS、自如、龙湖、货拉拉、讯飞等SRC。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KaBcCdkjIHv1hQyucZniaJY2m0xouC6eftgHPn2650k3y5actyMw3UOg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KnWr2jca8zJp3oWO0C5gLFuyRqVAXJMQIMcH0F6kWLqicqUMUia7hsUWA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7K9UX2DpdVrSPicjxhDsLDBfiaedGib0O7tau79BgUGicMnCsdyoQCC7bKYQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KIqjB7h2qQJFXhIv3qRNxll48w5OdS2u3eqicVZE58lsIeMZnqXQOovA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KVQdP7TREzRc7xiaxPWlAh49paSuQiacsDNJiae0ILx7yAbleFtpJ8181g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KwyULWKyG9kKSt9UoZtkpvXUgNtXlvycrEMboAbcY2opIm6xialbGgHg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KKJNW7YBhngA2QjWFbMuwibjorVw2WAgAyHicmgG0ahOmzyOwR0MAWVgA/640?wx_fmt=png&from=appmsg "")  
## 2.5. 漏洞利用手册  
  
高频漏洞深入利用方式整理总结，附带工具和案例。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KlLrXQYQfelXlMphXricTzAanbPrYttEWYsZlMHoV3R6u7ibzPu7o1nCg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KH6llp2Gtnia9j44jibzmvkeMKj91YdG6ERhV93H2ezicYo7h3ZbonwEWg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KFNj5hkGVLpKSx5NHY8ViaROxPBcJh5CQp4FK4nicT8Jwq5zshUqaee0g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KL4efojqPPubQSamN3hvdZGBugDQW19hYfulN023WQOFic9qlmycpPeA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KPKiafmKticy9CI1CoZKz77puctfsYYKBpgjRDKPTuup5goSZ3m3mgNpQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KfHtWo5drWezQD3iboQgRk5zRSlBjOC430edQlBhrk4oic4qcxqFfIzOw/640?wx_fmt=png&from=appmsg "")  
## 2.6. 实战技巧总结  
  
SRC、CNVD和HVV快速挖洞思路整理，附带实战案例。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KutKUUZSRUdgRScJ3iaibtvCZ0uqiaqWrhVrz00A4M6M4MUZgQgbEkCOsA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KyXcfLyaCDOAz76rmn7ZGA4arMiaZMdeQsd5o20kB1GBxEy3ts3h67eA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7K7K6UZEgOo5SlE2lNHhl5ibMSLnJye2SnYbLO6w5IV5VuWEWqRZ2jBPQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KsvNNKGWFIE3r6Y8siaKFQSrEJYDTl7iaYqyWmfPyB7AJIOLkrnFscAPQ/640?wx_fmt=png&from=appmsg "")  
## 2.7. 工具插件字典  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KSGgjEf1kHfQkFWGBNWySw6Licrq4agMicP5zxasKq1G1MQDzG9jHHR0g/640?wx_fmt=png&from=appmsg "")  
# 3. 如何加入  
  
**圈子面向对象：挖SRC和打攻防挣钱的师傅们可以考虑下哈，单纯工作就没必要买了。**  
## 3.1. 微信用户  
  
安艺圈内容如下（**随着内容不断增加，价格会不断上涨，圈子没有任何搞折扣的活动哈**  
）：  
  
1、dddd实战优化版：一年211（**dddd每人限1个激活码，激活前请选好常用电脑，如需经常更换电脑的，可分批次激活试用哈**  
）  
  
2、安艺圈知识库：一年399  
  
3、dddd实战优化版+安艺圈知识库：一年520  
  
有意加V，无意务扰哈（**加好友需要****备注dddd或者进圈****，否则不允通过哈）。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KaYm0dmlmLxLjE9HpwxbyVSqxhn7oFpIPLdyPBicKxdxFOpPKaQbWiaUQ/640?wx_fmt=jpeg&from=appmsg "")  
## 3.2. 纷传老用户  
  
登录纷传小程序或者APP中，点击"设置"进入设置界面进行截图，将设置截图和dddd运行截图通过微信发给我获取激活码。（**dddd每人限1个激活码，激活前请选好常用电脑**  
）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KZHJPxen9w6t3owhpicugog9HevlXu3DMLG85GDibsLF0fib8UBFlsW1ww/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KWweF5uibsna9Sw5mXUCBhFrK5epujIy1o8zU6xXR4EibO01HvticKUOaQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KHVWytviaLhRU512o6H5QkcVjCzsWYm0qApORGWGqBVaP44CdnZOZTfw/640?wx_fmt=png&from=appmsg "")  
# 4. 圈友互动  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7Khu1rqCmbu58uibxFGRKCpuWh8LyVmrA2dkqgf6icOICw5ZHDMa24xQLg/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KB2uvibdSbkickNQFrjtaricN93JickhuR26ve14QAdIr444D4eGL5j2Msg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7KtjsUrJL1tBFUs38xdpR8n9jPNZ5M9pyeqHwWpYibd3RrCPIMib3rhv0A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7K4MLF5Topw575XK1TMph6Qtc7RKvFWXItdEichxzrZYcLGWtCeicLDQJA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7K073gQsmhrjb24XrnJO3TdEicbUOl9Qwic5SYeT9hbV5c51rHU4J8g2Gw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2OqK5ulXyHZyDORqoPrYTv7Kh3XuIDyvXyvdKdudecb4NrR1V5liciatrROsiaur1ibFCOrSTiawUx4wF4Q/640?wx_fmt=png&from=appmsg "")  
  
  
