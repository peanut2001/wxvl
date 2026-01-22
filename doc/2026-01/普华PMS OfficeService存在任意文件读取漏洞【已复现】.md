#  普华PMS OfficeService存在任意文件读取漏洞【已复现】  
安全艺术
                    安全艺术  安全艺术   2026-01-22 00:30  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXEWVnZt75IyLRkYso3YXTibas7SuzFGyia931sn9DRGic5tRJ8xxQia25yg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXmvL7gd5UKZEapGokEs4hpSz2qNVTxCfghXmDjziapYYJtKkAEShh6nw/640?wx_fmt=png&from=appmsg "")  
  
新圈子上线  
  
  
圈主介绍：  
  
十年安全行业从事经历，多年攻防渗透和SRC挖掘经验，聚焦于实战思路案例集锦，基于实战的dddd优化版，多次护网中斩获上万分记录。  
  
知识库内容大多来源于多年攻防渗透工作经验，实战漏洞挖掘，漏洞利用思路、工具和案例等，严禁用于任何未授权扫描测试。  
  
圈子面向对象：挖SRC和打攻防挣钱的师傅们可以考虑下哈，单纯工作就没必要买了。  
# 1. dddd维护  
  
**选择这个工具的最重要的原因就是先识别指纹，然后根据指纹去扫描对应POC，高效高质且维护简单。实战配个代理池，产出还是很可观的，记得第一次用它参与国护时，第一天就进了某央企运维内网。**  
  
一张图看懂dddd运行原理。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXfnS5d6wWkicHae7Fibfv43QP3NhtcT5Yrlva7zD6icQ3qRb6mkxy4hpWQ/640?wx_fmt=png&from=appmsg "")  
## 1.1. 指纹POC  
  
集成指纹POC（基本看到新的就立马更新吧），workflow（纯体力活）和POC优化（误报太多，陆陆续续  
优化近3年了  
）。目前指纹数据: 11219 条，漏洞POC: 4710 条，workflow：3504条，目前应该是市面上集成力度最大的了。  
  
杂乱无章的指纹实战中不断新增，排除误报等。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXfibkp7icGvSaRYcnNlq34JiaTunzo8JAN4s1rTHbQwkKeyt8OBMCeOvjw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXDnTMPXsWlPtNfw6yW6QYich5icBKIGQ8tK5HnicYLcC4LzjvKDl1m7JYg/640?wx_fmt=png&from=appmsg "")  
  
**workflow（懂得都懂，纯体力话，也是坚持写了近2k条）。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXk0fGwfibBLF0I3rDM5SpZtrNchK8ZCWJgF2MgnhQPP93rR4beMjz40Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXmUB2VcI5cibtiaUwYqRItmbMrt1eOKhrRUV5pctwf9QKzHMw5jojmveQ/640?wx_fmt=png&from=appmsg "")  
## 1.2. 蜜罐排除  
  
思路很简单，指纹识别超过10个默认是蜜罐，不进行任何扫描。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2Or0K0FqZZVkVQJafpd3porXxb3PrbFZzm1Cibt1hWneB3rgYwG7VsYzmeSCrOy1dQD8c4KepWWMP9A/640?wx_fmt=other&from=appmsg "")  
## 1.3. 指纹优化  
  
很多指纹又臭又多，基本没有poc可打，在两年时间里基本都删除了，保证扫描结果更加实用，不用花费精力眼里在无用的指纹上。同时，合并了很多公开的指纹库，也参考学习了很多付费圈子/星球的指纹库，但是合并后会发现每个指纹基本都存在重复内容的，最终还是需要进行去重处理（11253条指纹）。一个表格告诉你合并后每个指纹都至少有2到3个重复。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXGhyI8pCd0eo1dpPRXLrZaYn4FmtvLmrIWt58vITLC7ptRicHtNUzYww/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX4eepX593ibDHW2iaL8lvXIl9QnO5kDZ6UpZWE0S7dJsnBq8ica3GUKjJA/640?wx_fmt=png&from=appmsg "")  
  
及时优化指纹误报，减少眼力精力损耗。这也算是一个强迫症患者吧，误报看多了，很影响心情。  
## 1.4. 目录指纹  
  
网站目录扫描：这块主要是针对SRC挖掘和HVV项目中碰到的比较多的需要路径信息的指纹进行补充的，新增了很多发现频率非常高的springboot相关的接口信息，并通过指纹信息精准匹配，基本扫到就可以进一步利用。  
  
网站指纹识别：这是圈子上线后来着圈友的需求，网站指纹识别输出，原版是统一输出的，没有任何区别，改版后新增了重点指纹（SRC和HVV漏洞高爆发点）高亮显示。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXGwe2a4nQtSVticT2Rr4mnQ47VxL5DuZsNeWMYQf3OWh3TkVQ9hE3Sqg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXvxruspibaianwI56Yu4HPMmXS008rczIJbRMp8o8FfrQM0iadghxpQUWQ/640?wx_fmt=png&from=appmsg "")  
## 1.5. POC优化  
  
主要基于实战进行新增或优化吧，以Nacos和Jeecgboot为例吧。  
  
1、有些Nacos版本需要加入一些  
特定header  
头才可以正常访问（回想下自己是不是错过了很多Nacos的洞）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXGicibFKMa1vXchZnPibibzOebOuAhDKc6YO2StTHU6T31yj2trtDNbG8xA/640?wx_fmt=png&from=appmsg "")  
  
2、jeecg-boot-jmreport-qurestSql-sqli（添加绕druid防护机制的poc）学习代码审计时看源码审出来的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2Or0K0FqZZVkVQJafpd3porXAGkufCCUvt2mLmnqqS7rxm7qSzfbI3X6A97LjUb5YibAkSOcB0F9ufQ/640?wx_fmt=other&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2Or0K0FqZZVkVQJafpd3porXcnpEAWrhTOia8EtSTdTia6leobkPmx3MDabfRialUiaVKzLiajxbmTVPqEg/640?wx_fmt=other&from=appmsg "")  
  
以上相关POC都已集成到圈子版的dddd中。我记得有圈友问过优化频率，这么说吧，一般发现问题都会及时优化。主要是我在工作中也一直在用dddd的，再加上具备强迫症，看到误报就想立马修复吧。  
## 1.6. 证书问题  
  
扫一个站，出现一堆站。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXqVVSMtq1Hueow5etYicMJ9ROdISv1RdnFVmzco51PYYrrPYiabe9TlJA/640?wx_fmt=png&from=appmsg "")  
  
优化（也好也不好，之前这样扫出过某src的一个rce漏洞，但也仅限这一次，所以考虑还是false掉吧）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXzztoaZJ9NTdXp2vosTfG0bh8YFFWjjAKZsKibJrCXoiazu55NHIOVzibQ/640?wx_fmt=png&from=appmsg "")  
## 1.7. 重定向问题  
  
是否跟随重定向，默认改为false  
  
false的话，有些OA默认跳转的，这种就只能加目录扫描识别，否则直接识别不出来的。  
  
true的话，挖wps的时候碰到过一种情况，https访问跳转到http，然后http访问就会超时，http拼接目录扫描就一直超时，但是https拼接目录扫描直接出了nacos的系统，然后还存在漏洞，差点错失一个高危洞。有些系统会跳转到非目标域名的其它系统，后续扫描也是浪费时间了。  
## 1.8. 顽固的JieLink+智能终端操作平台  
  
JieLink+智能终端操作平台指纹+poc会触发workflow报错。  
## 1.9. 默认拼接路径  
## 1.10. 目录扫描bug  
  
只拼接了根路径，目录路径未拼接。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXLXnjiawtKVydTjFvdzpBHdUT9spfoia3a8avwoRLtB9B8uricw8aicCXXQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXicsa2cBicm4wdbUj5HJq5hSzpFRTSywO2aoyDctPYwabiazg4Z4NcffOg/640?wx_fmt=png&from=appmsg "")  
## 1.11. 运行死锁bug  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2Or0K0FqZZVkVQJafpd3porXvVIrcBfVrLO8EanOaIbPYtjT9q4wH5BKibbia09EKyRicicLXKmzibezqFA/640?wx_fmt=other&from=appmsg "")  
# 2. 知识库维护  
## 2.1. JAVA代码审计  
  
自费999元跟班上课学习记录从0到1完整版。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXEkj5ia2PSNdAkr4cYnicAQtrPMAbwiaXABKmYUib7wYtITcolS2CgzTiacw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXmNntPD5b29iaS8dzXHE2PwqiblMK6ibzOL2hMibxXMPfiagTvlzeNTIPq8A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXs92BdmibLwk4JSvO7v8ic4G7dKy2Fic2ySlxbiaBdyplhOSPwtmFNayo9A/640?wx_fmt=png&from=appmsg "")  
## 2.2. Nday漏洞POC  
  
各种渠道收集整理的POC，公开的和非公开的等等。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXWrIgcsibenQq196Cx6G75icd57FnJVjTaww6tuxLplzUFgQcnwouVbng/640?wx_fmt=png&from=appmsg "")  
## 2.3. dddd更新记录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXg7Yt1UFvQzOKZTnVOTEd1Op0XsZKEoV7KBJyyT0gI2OZictoICLpsSw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXr4I3iccwUZicYzq1fncdw85NnCfnRia9ClP4PeZ0HJmjRjhUpeoWmD8bQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXNnZYXzadmM05mxBdEQrEoTYoIr5lnnfl4UquwYXIHHQcUbKxohlQhA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX06hytSDqtftXeAGfZm9DuTs7b6EKfDVDPrsNAJCsUH0pkupFiasEWmA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXTO03iaAhP9iczHbjjqSL6BwwR2TvCXbNQkroqesvZzJs42rR59Q6vyeA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXoibfzWVB7NISgxqEMhCX0BId9zLLwbCsPrBvlOnIRtBCImM5o7oObNw/640?wx_fmt=png&from=appmsg "")  
## 2.4. SRC实战记录  
  
目前SRC小成绩：猎聘和蔚来汽车SRC总榜第一，WPS、自如和货拉拉等多家SRC年榜前十。  
  
圈子中关于SRC的内容全是本人挖的，对以上SRC感兴趣的师傅们可以多多交流：  
  
**1、分享**个人**SRC漏洞挖掘完整过程，包括不限于漏洞挖掘思路、漏洞挖掘完整路径等；**  
  
**2、分享自用优化的burp插件或规则文件以及实战总结的账号密码字典等文件。**  
  
个人SRC实战案例，案例来源猎聘、蔚来汽车、WPS、自如、龙湖、货拉拉、讯飞等SRC。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXqBmDvysnwtOqpYZU2CWfLn7PyaAcoebJaQe8j3Vnf8EowYMh5ic8xDg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX5ApFvEt3NyYFZmr8PXuj9UHsuhiaT3mwlXcD20FvCsNJOPp1cXxmuuA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX85LHBzrZevaKqbg0hYTaQfXakLoud6md5H6kbBfyiaorLpu6psJFwEA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXL3hFjFIyiacUTH3D7VE1HkZqluFK8qvEt19LXp1cXlnCN3vEqry6ia9Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXYZc6tld118hAQ96O8rSf5IcJSE2Ch9NyYOgcZGEf7rQPicmjNkZZ3TA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXZx1zFZClP7VHKwbJgDTXUjqn5tibBdwaniaR1icMpYNbjuc4nQ4BPTgVA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXrgl2qujnOt8ZIHAZvUtYRiaSzpGYfMYttIicLsQQhCIqgj4mfSqWpx1w/640?wx_fmt=png&from=appmsg "")  
## 2.5. 漏洞利用手册  
  
高频漏洞深入利用方式整理总结，附带工具和案例。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX2b1rZiamBHBroLiaafylsLiaxEtKTt9Yf9icA55N6o0yf137lJaMOs5jWA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXAK26aZxOGjgUyxG896iatVbZsictB970JhzmMMHJDtkIx6MZrvnHQ9aw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXXPNyuHGC1JjXb7E3Uu8d7Zx26fSB63soA0ZW81e7QKAOXAVMyWvicaA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXpViaYsODDAo72fc8MLv8XDHACB3wmzt3CyvicP3HI5DzibSQBLt58kOTQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXpqibVpot111eNbRPpoIKwlxeEGXBpRzEo9CHVuD0PZq5Vw0KibJdzjdw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX73Q001E6H3GhGOgOZL0oq8gp9iaEa0SLlQbAsW92JtQcTpPON5uRuZw/640?wx_fmt=png&from=appmsg "")  
## 2.6. 实战技巧总结  
  
SRC、CNVD和HVV快速挖洞思路整理，附带实战案例。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX8iaKCaWcyoGkeaykj6DvDoAmibYAPdsp1uOXhmprcVWcY2aWvA889iazw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXa84Qa6f8DZLWXvznBzozr9icshJuPIkIoPP6ich6C4SsBdSLcRgJMGdg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX8sbCernicW5EYiazocScXzF50WSKNS3DlScT7FvPXvLiaV0akhKdDKaBw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXK4rddKrcoMfHaxrFjoqzcrjfVPEiaias43y30mheJ4xU4NiasvvMmgUEQ/640?wx_fmt=png&from=appmsg "")  
## 2.7. 工具插件字典  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXibBFVicEASIX2tpFxCuibYxYn2Ckr4AJpUTDUxfkV9HHC2nPW8A8XB6fg/640?wx_fmt=png&from=appmsg "")  
# 3. 如何加入  
  
**圈子面向对象：挖SRC和打攻防挣钱的师傅们可以考虑下哈，单纯工作就没必要买了。**  
## 3.1. 微信用户  
  
安艺圈内容如下（**随着内容不断增加，价格会不断上涨，圈子没有任何搞折扣的活动哈**  
）：  
  
1、dddd实战优化版：一年211（**dddd每人限1个激活码，激活前请选好常用电脑，如需经常更换电脑的，可分批次激活试用哈**  
）  
  
2、安艺圈知识库：一年399  
  
3、dddd实战优化版+安艺圈知识库：一年520  
  
有意（**加好友请****备注dddd****，否则不允通过哈）。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X5epWh2K2Or0K0FqZZVkVQJafpd3porXiaT8icgibWtmupvlFmjbjjprs1EpCGX63ercnSMOw5aBGoIlicqcuicicIgg/640?wx_fmt=jpeg&from=appmsg "")  
## 3.2. 纷传老用户  
  
登录纷传小程序或者APP中，点击"设置"进入设置界面进行截图，将设置截图和dddd运行截图通过微信发给我获取激活码。（**dddd每人限1个激活码，激活前请选好常用电脑**  
）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXLQ3wznxRhlICrEXc7HucTzWwgaC4EBzhib9cg8muTyfL5cZRaTJT0uQ/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXjG10D8TTxzrDsv24KibsblLPoOJxEKyeJmg81maiax9Z2LoWSDicbKk4g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXWr3aCLrAKDwpX4qVUkia2xbxLgI9icvcicv6YN9tK9mSL09tghpmthBKg/640?wx_fmt=png&from=appmsg "")  
# 4. 圈友互动  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX81JyfcAODpBXdzEARNTHH6FRZzjXWusKOABxGm7nV24Mx5jnsxV95A/640?wx_fmt=png&from=appmsg "")  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXwnpSgpIuygl12gOrF6G5wSTibaFUfgMrnvbibsL8aQvhBWEeicym19dZw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porX8ibibiaqNv1iaCwicLSk8tW01qBFs3qDuAsFmYI8sQ1oUpy6yd1IkL21BeQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXR9z7OWGPnKZlhiaXe3TsjNWHmyQHJJBZmB2qk1qmkSAbPOSIbUnRd1g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXMvRYe4so6DqqLPZRdcIsv7BouNQs0iaZVkPJQ5m6nKrbicEEJWanR08Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/X5epWh2K2Or0K0FqZZVkVQJafpd3porXypmWnN1hnnUqxc0vVXcShV7NAk8G7b9qgMI8h99Aibb9JSuTY3LWvsg/640?wx_fmt=png&from=appmsg "")  
  
