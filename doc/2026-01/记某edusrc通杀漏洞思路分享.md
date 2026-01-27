#  记某edusrc通杀漏洞思路分享  
原创 陌笙
                    陌笙  陌笙不太懂安全   2026-01-27 09:47  
  
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
想出洞就得找脆弱资产，这次我们直接中学起手。
```  
  
漏洞挖掘  
```
通过一番测试锁定这个小程序。
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXCh19BvtxhibbAuficLqZ6z4Uf5SSN0qwC8qSZP2OF4Lic43wLpoiaOExNA/640?wx_fmt=png&from=appmsg "")  
  
点击小程序进行登录,挂上bp,让流量都过一下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXEWj7QBUgV6ZzG8ejsINia0LbLzzOuPzsmDT0ibwvOCDNbwicMDkfKh1MA/640?wx_fmt=png&from=appmsg "")  
  
直接进行授权一键登录  
  
（我这里是已认证，因为我是挖完写的文章，如果第一次登录，需要输入姓名,sfz,班级之类的信息进行认证,这里没有限制,随便输入信息就能认证成功）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXsGanNPpia3WA9w3cWuiabHKqGw8xfRichRktM5lFcia2FcB4ZHO2mVdQMQ/640?wx_fmt=png&from=appmsg "")  
  
认证成功之后来到首页,开始对功能进行测试,一项一项的测就行，我这里直接写漏洞点  
  
点击校友查询  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXoyd8IEyMNrWCaibJLBB4anea8ibRHbVsjxZyMzIn4mGz8CxMCZ2icG8FQ/640?wx_fmt=png&from=appmsg "")  
  
会跳转到校友查询这里  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXkNBvVNI0cvyy5Yib8nTw95ATvgppVX4l8wwACuicLIWX0K9pibWrAChtQ/640?wx_fmt=png&from=appmsg "")  
  
点击同届校友,会直接出现同届的同学  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIX6KIH89UaEibWlQl4zLMXCByJ4MOqeeqnb37iaujCJmliad739PhtPOq4Q/640?wx_fmt=png&from=appmsg "")  
  
这里随便点击一个进行bp拦截，进行观察，可以返回这个人的所有信息  
  
包括三要素等等，且看到经常出现越权的id参数  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXuwxLStYPZicEibibMN4fEIK7SyDReM8syIqg7BIUYK7oraNYU52hZic4icw/640?wx_fmt=png&from=appmsg "")  
  
直接丢到repeater模块修  
改  
member_id进行尝试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXGXER4QZQDicyDrIlfyMzSpiaaLWicxePV3WTmIGeNywu5uL5DIkRJcqOg/640?wx_fmt=png&from=appmsg "")  
  
果然可以越权，返回其他人的信息，直接丢到intruder模块进行遍历  
  
可以成功获取系统内所有用户的敏感信息。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIX5NtxZruOe5jzcF9CM6nubj9NgGiatDjkZKZUb1nNcq9NgF97aWMKV8A/640?wx_fmt=png&from=appmsg "")  
  
其他功能点也有东西,接口不一样不在进行说明。  
  
这里就要想了，一个高中可能有自己的系统吗？  
  
我是没见过，所以这系统肯定是第三方公司开发的。  
  
既然是第三方公司开发的，又不可能只卖给一个学校，  
  
这里就可以扩展一下，看有没有其他资产。  
  
因为是小程序，尝试检索一下关键字，看看有没有什么相关资产  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXcDqBoPic6Qqs2RfUTCghMqRgHwFSPlCzOnOanicNicQSnFPgmpAXqew5Q/640?wx_fmt=png&from=appmsg "")  
  
看着差不多，其实都不是。  
  
然后直接把小程序转化为web，通过web+资产测绘找资产。  
  
复制小程序网址,浏览器访问,看到了管理后台。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXFeX4hJiccelnr3erZQfS9H7AjADQiblRnhkiaddoEJ9aSOOibljn34FyIQ/640?wx_fmt=png&from=appmsg "")  
  
那就先看看后台有没有洞，测了一下弱口令啥的，没成功，  
  
不能直接爆破，有滑动验证码，把小程序登录成功的数据包，进行替换，没反应，提示权限不够。  
  
看看接口，直接跑了一下没东西，我直接拿到小程序登录后数据包跑，依旧空军  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIX0NNKhpsYq0j2LAggZzwTByWYgLuJSE7v7TsQEoDQR7z0jYeRFHhJibg/640?wx_fmt=png&from=appmsg "")  
  
发现admin-api和越权数据包app-api相似直接替换，那就把admin-api都替换为app-api再跑一遍依旧空军  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXQsW8Tia0Bw2xsSiccGjhx3iasIEdcgu5WjJ7PY8z6hgibmB8sKAjF7ic0OA/640?wx_fmt=png&from=appmsg "")  
  
根据上传接口构造数据包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXhoLWVpBhpJgQEwx20xGic2oooqFEe92cA7pgXtpialsQRwdKEM7krCxg/640?wx_fmt=png&from=appmsg "")  
  
真是一次完美的测试！！！  
  
继续回归正题找资产。  
  
从登录页面提取一些内容,title,body之类的放到测绘引擎里面瞅瞅。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXQ37h7rjwAUeCZSjyU65H1owhKcibSia9OpHDk28SSLtN0Bhxpq0F7vAg/640?wx_fmt=png&from=appmsg "")  
  
点了几个发现有一样的，后台管理页面，说明确实多个学校再用  
  
在通过hunter和quake都找一下资产，hunter这里可以配合公司备案找。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIX28SEDt4tErMX59F7tjibT0abqR9d0UXib3FPvRibg750BddI8AxUa8oRw/640?wx_fmt=png&from=appmsg "")  
  
后续通过ip，host,之类找了一些，为了全面，将所有资产导出，进行去重汇总，丢给httpx进行探活截图，不要一个一个看，太耗费时间了。  
> httpx使用方法  
  
> 陌笙不太懂安全，公众号：陌笙不太懂安全[渗透测试漏洞挖掘如何轻松找到脆弱资产](https://mp.weixin.qq.com/s/kjM1twQU4xNkw7Wm7X2X8A)  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXcX7h1NjScLia2ibpGCV81oTfU5JXu6ibjIkOqPPbF2GHRwA9ib6hvIibNibw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXeeqbFfBqEeVyXkHm3GbUqWGgcBGIpDibDOImQFQGbgbJveVQOtsQWaQ/640?wx_fmt=png&from=appmsg "")  
  
直接对一样的登录框进行打开查看就行，拿着打开后资产里面的学校名字  
  
回到小程序进行测试，一测一个准,这里只做资产查找思路分享。  
  
后面继续观察探活结果，还有意外的惊喜。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXJIaARDMibicRCUrGEnxLibSorE0y0SmNHeBVTSf4zUlibgBBE0FmfyzdibQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO6TUDDN5j5bkibNDJhicCcyIXfnQCm42anQbe5Ly9vTPV7ZibL5N4pSIezicntowlHOfrcyQq1OX6gpeA/640?wx_fmt=png&from=appmsg "")  
  
跑路跑路。  
  
后台回复  
加群  
加入交流群  
  
有思路需要的师傅可以加入  
小圈子   
      
  
主要内容是（2025-2026/edusrc实战报告/edu资产/漏洞挖掘工具等）   其他内容懂得都懂，持续更新中  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV25rGkkJ8qOPAooDwASNSaiaGJibu3z2mOqnD2vCnOQB6ia3AfuuOZ0ZDg/640?wx_fmt=jpeg&from=appmsg "")  
  
