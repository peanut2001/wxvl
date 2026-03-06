#  记一次SSRF+文件上传组合拳：复盘我是如何组合漏洞一步步Getshell的  
1266136730734380
                    1266136730734380  只会看监控的实习生   2026-03-06 06:48  
  
# 0x01 druid弱口令  
  
  
1.前期对这个web应用做信息收集时，没有收集到任何有用的信息，它看上去就像是一个简单静态页面展示（这里就不截图展示了，厉害的大佬能根据页面找到这个web）。但是当我打开浏览器devtools进行抓包时，发现其存在网络请求，并且每个请求包的一级路由都是相同的，在查看服务器信息发现是ngnix → 推断为前后端分离的项目。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFH8qsSqcB2KJDDAMHicicsyGMBsOUaPEYUWaW6iaCeQU55jUWpwhWdds35apCdUW5dzjSOLGS5tia1IQUtfxXMRNd9by9Z06vD8gYM/640?wx_fmt=png&from=appmsg "")  
  
  
2.如果是前后端分离的项目，首先想到的就是java web应用（按目前市面上主流开发来看的话）。并且如果是spring的项目话一般是会有默认报错页面的，这里为了验证猜测，我直接在浏览器访问了这个路由。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHGiclOw8f6dtXqdfPlXRO1KZhvwoVVKiaCRtpzOhnb3ToHSRNd1Xw2QpjlHqPtUpiaYDYksc8QKHNXNZWX3IVOxHcUzO90RE1aRA/640?wx_fmt=png&from=appmsg "")  
  
3.显而易见，这是一个java spring的项目。spring项目一般是存在很多敏感目录和敏感文件的，我们可以使用字典来进行进一步的信息收集。这里我用的是曾哥的SpringBootScan：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFEp4Q5UicM8uNltXKp5QTic7zfed5aWkMOaRJcJT57wcxdeP7FkquI30n32daRbnYLEoLeFGbgTiacXV0lBPnZ3mu1Pg5bbcbILQ/640?wx_fmt=png&from=appmsg "")  
  
4.发现接口文档路径和druid的登陆页面，这里我先打开druid的页面看是否存在未授权或者弱口令。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHs1Ry6BOETCHUhibSHynicHOxpAXwTAiaicUSyn3TS0Cdv9iaAvlbteo7J4NIjjMPWbFHXQN9u5YW8iazhYSvBLI3ibbd5fHusfI0PgI/640?wx_fmt=png&from=appmsg "")  
  
5.好吧没有未授权，但是存在登陆页面，只能默认密码或者弱口令爆破了。结果直接默认密码登陆成功了，成功拿到一个druid的弱口令漏洞。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFE5vZZ3v7iaeNaVNbmV8qaicEMnlj6dIKtaoHRJ4k8mntMGIDk1s1wTs2icNAy8jBADicKkw1wpvjx1ohwgW33Yc6StSiawg5mlbPrQ/640?wx_fmt=png&from=appmsg "")  
  
6.然后我就想能否找到后面页面，通过druid的session监控里面的session爆破session登陆到后台，可惜并没发现任何后台地址或路由信息。到这里只能放弃了。  
  
# 0x02 组合漏洞xss：接口未授权访问+文件上传+xss  
  
  
1.根据前面SpringBoot敏感信息收集的swagger文档里面，我找到了一个文件上传接口（存在未授权访问）。由于是一个jar包启动的项目，他不像tomcat中间件启动的项目能够解析jsp文件以便于我们获取webshell，对于这类java项目通过文件上传的方式获取shell是不太可能的。于是我就想能否上传一个html页面，实现一个xss。请求包构造payload发送结果如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGQVF6eabrAzGPicZLFMYmia1UcFKYe9XxnXFtReib3lcdibbaKG2sgUBsoogQ6FA4ubyLNs8dE8F5qesXIXywPI4aGKiaZGlmLDS78/640?wx_fmt=png&from=appmsg "")  
  
2.他是一个图片上传接口，但是我将后缀改为html是没有任何校验的，得到这个返回结果发现只是将文件名重写了并未重写后缀，访问页面，成功拿到一个xss漏洞：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEUIltHhhfialHhVxf5ia8rMVOhNwUakWQhzDWoagbG639kibCxfKGgL6XagCfxRUrhyeDBZTxcxaEFo1YgeXia52icpmFgQxRIWGY0/640?wx_fmt=png&from=appmsg "")  
# 0x03 java组件存在ssrf、任意文件读取等多个漏洞  
  
  
1.swagger文档没有获取到其他可以利用的点，跑回前端对前端代码做一个简单的审计（主要目的是挖掘更多的路由、url、资产地址等），这个位置存在了大量的接口地址信息，并且有一个地址很独特，看名字像是一个图片预览地址：/preview/onlinePreview?url=  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFH2DNRV1sGRB05FfPYzbicBYBxyZlSibT3ibNiamA0xfqpgc4HoYxnCB2Y86hJg9kehnhV28OMl7e9NvBE8PF8ib863JcKoJY2xws4s/640?wx_fmt=png&from=appmsg "")  
  
2.访问地址/preview/onlinePreview?url=，页面如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEqghJ6XsvCvibnSToibwFCEh9LhHdhyveVFShsxWCQiavuicoS9VmEiatH5AcshhdyYNYWbTgJnXejKDKyQFFgdOpHQia8GLe9DkuP0/640?wx_fmt=png&from=appmsg "")  
  
3.直接拼上百度地址首页图片是springboot默认页面报错，虽然是500报错码，但没有具体报错信息，无法进一步利用。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFJwsSF7Moj3cEkHgh7CIPic0wmSWxBBm01liatfS9L8Pf2R2cH5k4L7vfbbkNic4ibeDFRHTNdF4IltYq9bHsPeVkFBQ3NvhIiarfo/640?wx_fmt=png&from=appmsg "")  
  
4.然后我就去掉了url参数意外发现了报错信息，这里比较关键的是这个包信息：cn.keking → 进行进一步收集发现是一个叫做**kkFileView**  
的java组件  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFHI2GRgj5osk9Jo17IPWMhT6Pw2iaAuro0DGiaQ6ImtYT4ns75b7IMOucGupTjezY2VNNz4QfCWPT3rdm9qicXXDLvDwnY3o7icS80/640?wx_fmt=png&from=appmsg "")  
  
5.查看官方的文档说明，发现其是一个单独的springboot项目，并且存在一个主页面，上面会记录其最新版本更新说明。  
  
思考：如果我能获取到目标的这个kkFileView服务主页面的更新说明，能否根据其版本信息查询到一些历史漏洞呢？→ **最终得到其版本信息为v4.0.0**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHGibmPwWvEvB7JkuXQ4Bb1QS190pJ10KotA2ZhKXUPxibWL4jNicJJricS4omLQJVdkib91MVnHVicN0cs475MwIwoueYIxUqfo9Bpg/640?wx_fmt=png&from=appmsg "")  
  
6.收集版本对应历史漏洞主要如下：   
  
1）存在zip slip文件解压进行文件替换造成的RCE   
  
2）SSRF   
  
3）文件读取  
  
  
（第一个漏洞危害有点大了，他会替换文件，实在不行再考虑利用）  
  
## 文件读取漏洞  
  
  
这里我们主要是用了ssrf和文件读取，最终利用成功，这里我读取了  
/etc/passwd  
：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEtJVy9C5mqREHCJZGsS0jBBAfNkdPbGNXVZaushKkecf2DjpIXuzNiamib3rFYH0iaYN0ibfRibicIFFS6rBlAhpsPkyFp2W6ZCGu6U/640?wx_fmt=png&from=appmsg "")  
## ssrf漏洞  
  
  
然后读取云服务信息，这里通过whois查询发现是腾讯云服务器，读取元数据信息：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHn1OicrhMkup1Hvl13PNmOPtoicABPDJVe52PyR7UFZpewoPyBtUwXpkeSzm6WVBXryia1BSvSV9yCwR1PSLdDFPoN3YAW7CktJE/640?wx_fmt=png&from=appmsg "")  
  
后续我想通过元数据信息拿到accesskey接管其账号，没有利用成功（有厉害的大佬可以交流一下），貌似其并没有开通ram信息接口地址等导致我无法获取临时的token。  
# 0x04 通过文件上传拿到webshell  
  
  
1.最终我还是想拿到服务器权限，有没有什么其它方式呢？ → 把想到了办法都用了，搞了半天，最终还是审计源码给了我突破口。  
  
  
（分享点小经验，当找不到服务源码具体路径或者其它文件路径时：不妨查看一下.bash_history，说不定有惊喜）  
  
  
2.通过file协议对其服务jar包进行下载，反编译后审计，找到一个文件上传接口存在路径穿越：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHXtphb92LaicGjHic8SxlJYGRtia5WxcInaRYCeknwu5MS6B1vQA1MaNolATtNJOOia1ib8OWNCWvpPg8mn8iaxCFGt04DY86T9Ik48/640?wx_fmt=png&from=appmsg "")  
  
3.第一部分path是获取的config.properties配置的路径信息，第二部分filename是file.getOriginalFilename()获取的全文件名，后续代码并未对其进行过滤直接进行了路径拼接。这里有一个问题：如果存在文件名为../../../，将会达到一个任意目录穿越的效果，最终形成任意文件上传到任意目录的一个漏洞。  
  
  
  
4.这里由于前期的信息收集，我是发现其存在一个tomcat的服务。于是我利用这个任意目录的任意文件上传，上传jsp后们到了tomcat服务中。数据包构造如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFHTQ8SDnU8N2WgcGqowI0Zd9LtMOEWeHu6HhJGnNl16Ffvrn8I8SM6psJP5Uy5vo0PJhibdiaHmxB8KyiaCIicckUpzyibnoYgVkbzg/640?wx_fmt=png&from=appmsg "")  
  
5.通过哥斯拉连接后门，成功拿下服务器权限：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFdp2435y61SgHRsl6THQThMfcibAVIMBTrT1zPIjiaz7eDwEOkstniad1tHvawJjv1M3MpVjzGM6kM4g3LibweVficVp08aZW3icZb4/640?wx_fmt=png&from=appmsg "")  
  
原文链接：  
https://xz.aliyun.com/news/91668  
  
  
  
