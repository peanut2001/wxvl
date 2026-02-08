#  入门SRC简单漏洞案例  
小*咔
                    小*咔  陌笙不太懂安全   2026-02-08 09:20  
  
免责声明  
```
由于传播、利用本公众号所提供的信息而造成
的任何直接或者间接的后果及损失，均由使用
者本人负责，公众号陌笙不太懂安全及作者不
为此承担任何责任，一旦造成后果请自行承担！
如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```  
```
作者:小*咔
原文链接:https://xz.aliyun.com/news/14381
```  
  
前言  
  
许多新手师傅在尝试挖掘SRC漏洞时，常常找不到合适的切入点。刚开始接触SRC时，我们可以从一些中低危漏洞入手，通过逐步积累经验和自信心，逐渐挑战高危漏洞。在挖掘SRC的过程中，保持良好的心态非常重要，不要急于求成。如果暂时没有找到漏洞，就当作是熟悉大厂的业务逻辑。接下来，为想要入门SRC的师傅们介绍一些简单的案例，帮助大家快速找到自己的第一个漏洞。  
  
信息泄露   
  
关于信息泄露，主要是选择几个接口信息泄露的案例，非常简单也非常容易出洞。  
  
案例一   
  
我们登录到一个平台内，获取到js接口，js接口泄露了公司人员内部的一些信息，数据包下面还泄露了其他内容，这里就不贴出来了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRS47w2p1nU5l63CFkBd8tLhhCTXQLHcibJwzkYAxROS8COaibibjMdAKKicVb7MaBNFphBlYxIuI0dyicTal5vQMxgEZibP7ueOAgKk/640?wx_fmt=png&from=appmsg "")  
  
案例二   
  
这里也是登录一个平台后，通过js文件获取了api接口，该接口泄露了公司内部工作人员的姓名和邮箱信息  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSeibvmdvYvq2Q0lp6qWteuHxicu6z6XU1ibEHj4f7BCnu09kia8poAIoN2pxn8vhYl5fen7rRqlMFOMHYknuEhze6lS4yXRQ1R5kI/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRebWNibwkDC7zTvm7u7qicwBaILy8vGcROudMr4wHmMh6HRrxWae85T3gON56U1YLu4iawJDUjAsibfq9hCurIm8YHr24la0bDwS0/640?wx_fmt=png&from=appmsg "")  
  
案例三   
  
这个案例也是通过登录后，抓取数据包，即可看到其他用户的手机号信息，造成信息泄露，非常简单  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSfkWfPxUcMFAfeJu9IibVmm4MSlzyIGZdxOcTjC7ln84gtFDHqq2KibI873j5b3If6KMnqADLClrNg8BXwpK5Hphvg0D41NGgJM/640?wx_fmt=png&from=appmsg "")  
  
案例四   
  
该案例也是通过寻找到/xxx/logic1、/xxx/loadUser两个接口，泄露了用户的手机号信息  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTRrZzYJLB2czMcE4RxiaWS6ypzvKrzLb7pXNxD7DtXpZ3cPmW6RicCdiasH7XfdnsLw0hWElAAuCF0VgjPdEI6sLVaLbsqYSH3b4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQU5y6U0YX6rRLjIxhDuiay2u79sZ1ooibfKoaWQX03yLXCeOciafZXWjnQqFeibcq6ywCg844KW6VOppPz93ticRYnY33gAcjbm2qo/640?wx_fmt=png&from=appmsg "")  
  
上面介绍的这几个信息泄露的漏洞都是非常简单的漏洞，就是查找一些接口，案例三都不需要找接口，访问网站查看数据包就可以看到，新手师傅们在挖掘src的时候可以多关注下接口的信息。  
  
未授权访问   
  
未授权也是挖掘src经常遇到的漏洞    
  
案例一   
  
这个未授权案例我也没想到有什么危害，感觉没有什么用处，但是厂商也给了个低危，神奇！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS2ziarXJwtwv6pfCDgNUEqqZ08A86yXKqlWqW3N3CgziaAcp9A4vgahA3ZaJdatTGeDteqdHQayjOszkPlMzYduiaqBPWB4ZKb1A/640?wx_fmt=png&from=appmsg "")  
  
然后通过js文件获取到一个接口，返回包显示项目名称不能为空  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQowt5okCJOwveN164aY52JibQWibGJ9Tns5BTbiaklnO8IR8ccUtU3c3iaATlDEK9Zbkl1ibLAV0Up47Nm0MeaHiaOBJvklqhrTbYbg/640?wx_fmt=png&from=appmsg "")  
  
但根据接口名称create猜测这个接口应该是创建项目的接口，然后构造一个name参数发现可以创建成功.  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSycCPtz7ZTicIqVmCd0P0kRW3icMPGaVZiatGlVXObYWhNDBYsoFZ9F9AribqK53O33mC6MvaHvz2vZ8PuWOYa2zSibARnztK0sW1E/640?wx_fmt=png&from=appmsg "")  
  
在通过其他接口，可以看到我们刚创建成功的项  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRL5HIHhtk0AJ5j6XibkugVn9IzAHqiaMd0PpblYwz3kel3lOGnV89A8iaEAiaibFYKxtYBYWIEx4GosvmGc1miaKCVRJ6lpobHarzKA/640?wx_fmt=png&from=appmsg "")  
  
案例二   
  
访问该网站的登录界面，没有账号，也没有注册功能，无法登录进去，然后通过接口未授权下载合同文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSRYvVQbjYMVic8gzUM4RMGXugatwoa2LFtd60Ik5BX625zJhtWh86vMeYMEibULKVwmQdIdHjDM6nIYFtIApBhXoW8taX19Toqs/640?wx_fmt=png&from=appmsg "")  
  
通过接口/xxx/service.doc、/xxx/player.docx、/xxx/manager.docx可未授权下载文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRVFJOFIcQwibyLnCW1DYtYhibtExA6HMuweuN55Io0sSdQFZwlhjzQiaY1Mm8QuCyqyKpiaQj7b0K3SdicpnicvHeUcGrTAdeSW1OxM/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboStKU8kaGMpj5pqEux6pf2b0L07vNEh21X6CVFQic6EdJWiaX25LgybBo7kzqvFKbzrbQoM1lrxz5iatPCAoOicaE83dPvJsV1AQbw/640?wx_fmt=png&from=appmsg "")  
  
案例三   
  
这是一个高危案例，通过不同接口获取到了手机号、邮箱、姓名和身份证号信息，数量较大，但是该案例也非常简单 /xxx/api/user/cert/certs，该接口泄露了邮箱、真实姓名和身份证号信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTkbJ8TurPtaE2RKq1OezC8qcpcCIt6M6EbT1GBYcaZbiaWHG9XyKiamPy7tZVyibAjkic5K9ziammsZgn1qWflrM4opfPWwiaPrjjiaI/640?wx_fmt=png&from=appmsg "")  
  
/xxx/api/enterprise/certs该接口泄露了邮箱、真实姓名、手机号信息  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR5aXbCDpMltzVgWIsm20HrPSoF4u3R5VVyUoWRF1VVP6ib77mj1kMib1jhdvlaHovshPcFamELqiaWFIJCDvy8XQP5zJvNkAt2Ts/640?wx_fmt=png&from=appmsg "")  
  
案例四   
  
该案例都不需要打开burp，鼠标点URL就造成了未授权访问 访问该URL，这是个测试环境，不需要登录直接跳转到后台，厂商给了中危  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTnT9M4DRN2efMWKJPll9vgrmbZ1XGqWFtgyFFXHXIsG8uXkGq3aTlBox021hPazicsjrsJ41V4EkwRyfVCfziaB5vXhBH2jy06I/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBf98bfdXw1YXqHh8L58uB0NRTRibxC3RoKibAFcU3s6gmZyRUGyib79etvzHtaMicibMrblP3zX2rBcSVb8NRLkymxlnriaV1ViafsE/640?wx_fmt=png&from=appmsg "")  
  
这篇主要介绍一些不需要什么技术，刚入门的师傅们都可以捡到的中低危漏洞。  
  
总结:  
```
感觉有危害就提,反正不过也不扣钱。
```  
  
  
后台回复  
加群  
加入交流群  
  
有思路工具需要的师傅可以加入  
小圈子    
     
  
主要内容是（2025-2026/edusrc实战报告/edu资产/漏洞挖掘工具/src学习资料等）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSMYAAb65KZnQkVFcsNPuWkaHzYQDCTCA7hX917eB1uj6oNbwVXl1wXJtLnGWKsB6MRCCNRytNniajUlG7XUH7ujOMz05F7F6rw/640?wx_fmt=png&from=appmsg "")  
  
其他内容懂得都懂，可以扫码查看详情，内容持续更新中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV25rGkkJ8qOPAooDwASNSaiaGJibu3z2mOqnD2vCnOQB6ia3AfuuOZ0ZDg/640?wx_fmt=jpeg&from=appmsg "")  
  
