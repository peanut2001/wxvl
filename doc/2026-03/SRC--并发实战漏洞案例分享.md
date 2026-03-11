#  SRC--并发实战漏洞案例分享  
原创 chunliunai
                        chunliunai  chunliunai   2026-03-11 11:56  
  
    本篇文章主要分享本人在SRC挖掘过程中遇到一些并发漏洞的案例分享，主要进行一个思路分享和记录。  
  
    并发漏洞就是对同一个数据包在短时间内大量发送，对于一个共享资源进行超出预期的操作和影响。  
  
      
突破限制——最常见的并发  
  
     
 案例1--突破限制  
  
         
 站点有个资信库，创建最多三个达到数量上限——敏感：是否能利用并发突破上限  
  
![](https://mmbiz.qpic.cn/mmbiz_png/A3icsHic8DribbgAOK028Y91O4jPbqwiaAy0ggSj2iaSAALUuFVwbBia2qKsOzjBHmDOCXPVr99mgv9NUyVWctekYU6LlXGyZJt3R6Or2wQcA0iaIM/640?wx_fmt=png&from=appmsg "")  
  
这里用利用bp的turbo插件对创建的数据包进行一个并发操作  
  
![](https://mmbiz.qpic.cn/mmbiz_png/A3icsHic8DribaNKyNZRo5qIS90TXjv7twpMZweBrKFTAdBdzmL6UMYmRbvImdGsYGFkGer15nIkztCkZEaibkzTvYibegzCbT3ydial8V1GhyZOM/640?wx_fmt=png&from=appmsg "")  
  
可以看到响应长度一致，均创建成功实现了简单的通过并发实现突破限制  
  
![](https://mmbiz.qpic.cn/mmbiz_png/A3icsHic8DribbX8bawxVsceVwBGjun5mzpiaiaeNcWAbyzJAT7wPQckicxGuNicdnyMCoX1xLXUkTWgvJ6xK58r6Fz5F9GoN9qCN2hDqyzByuayfs/640?wx_fmt=png&from=appmsg "")  
  
     
 案例2--分组并发  
  
        分组并发主要用户对于同一个数据包，但是需要调用的参数值不相同的情况。  
  
        场景是一个ai批改写好的作文的地方，但是只有一次的免费批改机会  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribYDI18B7ibnVcGpeTbOpd14KQQfz7abibPEE3iaRbJibzOKqwGDNmRlndiaibZhbnEUY9wHEdQ51VkvOC1iasOrdr7pLDiaVAtdkYIqTxg/640?wx_fmt=png&from=appmsg "")  
  
这里如果想要对多个不同的文章进行一个并发操作突破只能修改一次的使用上限—即可通过分组并发实现。  
  
这里完成多个作文，并先保留，不进行批改  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribbthEbYwnCsQCqQBdwXhjQtoMg8vfjpNJ8MznicY234P0icB2zfrCfpcZGR57gUct8HdrRic1hd9WibAEIrgXcC4zTFUftzHDk9EZU/640?wx_fmt=png&from=appmsg "")  
  
依次把五篇作文点击批改并把数据包发送至repeater再丢弃掉  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribbQyic3uVHZ6g1qWwrsZfTdD7SMvUMIiccThWh9bqqaBeb2qNwzniaI8yarBnrCgj2tuLkSz6qpOjUrbbE0dBNFh2ibrhNX6uYcccU/640?wx_fmt=png&from=appmsg "")  
  
把五个数据包设置为一组，并通过组并发将五个数据包一起发送  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribZvTiamQuVDic1e7nGBv18343EicMaUB4lhL4iaM1VzTqnI4ofZXcCbgaGzIJ3nhm6qbiceATZ0XVFTU8XUIbTWKZiax2aYZBEzXkWfc/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/A3icsHic8DribYRMicliaq25rQDS1eclXL5l2d3j51aibXicfITOSD6ia7tLLSwqicLFVP7SZHLrIjibeiawHJqDF2egBNPJ111LXuMpnEjtZVUuLyxJ9o/640?wx_fmt=png&from=appmsg "")  
  
发现五个数据包均发送成功——实现了突破一次的免费使用批改多个作文  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribaRUo2qxc0OfNickgy4gp7VjicXu7v3jDuTxYBbhAusvZFjyB7yyZDVySxyTI7pHCBYJL5EgHqOZDgkIbxicLGxLYLN6v7y0zhuow/640?wx_fmt=png&from=appmsg "")  
  
     
 事半功倍——额外获取资源  
  
      
案例3--并发领取会员  
  
      
这个案例也是比较满意的一次挖掘案例。  
  
    场景是一个添加客服可免费领取一定天数vip的地方——这里的并发不是说突破限制，而是想着是否能实现通过并发领取vip的数据包实现额外的领取呢。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribYSWcR3Y6CD1uXk4zyib8PIDCBz9Q0R8w86icmp4ubXsRjomEMZW5Zp4qMU7JRJrc8TJ71nNvkZd8Cc3AtN9nooRmx579rgKia8So/640?wx_fmt=png&from=appmsg "")  
  
点击免费领取，会让你先添加客服  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribZPAyYlhBd7IRdm8URJWo2wNxDfwf7QZEmVjAtlFcMCjAvXAxMicibPV7swWHRe6x5VDRtkSrOJxAicWD6evqZghSBwmD3iaPMTgBc/640?wx_fmt=png&from=appmsg "")  
  
可以进行抓包，发现有个接口/vip/is-wechat-added用于判断是否已经添加好友；  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribY3tODZGE9dCOdlNKhyE00gPs1gFU8XgJrF4Xgq9VKlaevibVNkJicO3X9B45698eyCXRg6c3vc6pNkKWItjhnsc2kIUibVN5l1yg/640?wx_fmt=png&from=appmsg "")  
  
可以通过拦截返回包，is_friend判断是否是好友来一手经典的false改true，绕过了校验  
  
然后将领取vip的数据包进行一个并发操作  
  
![](https://mmbiz.qpic.cn/mmbiz_png/A3icsHic8DribYm7EPRwicPDEOYtiamLXEaF6uWhHRMPvdPyE0c1Z68E1iazWfeoiaCP4L15Gwd14zAeYuJKWzSXVlAWjF2zAMoXBR1DE4VOawSO1E/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribZObELTj4d7hTIOQAW7lwtz4l67RnIl6axZnicb84Tc5H7uLdgevqRBFHX6krL9PfZGk8g7KVk0CBib4a0CiccD0uDFpgd7J0S0YI/640?wx_fmt=png&from=appmsg "")  
  
并发成功，额外领取了多天的vip  
  
![](https://mmbiz.qpic.cn/mmbiz_png/A3icsHic8DribbrWJ5D68d1fnpHKsP102eUODNn27vbYQE9LY4YmMYB3YccGXPSX2dXssXJz6GibicO65biaMbo8t88z7mHUA3A8uT4tpn4IvKD2Q/640?wx_fmt=png&from=appmsg "")  
  
   
   反向并发——逆向思维  
  
      
案例4--无限空间扩容  
  
      
场景是一个知识库的地方，每个人有一定的空间容量限制；它删除文件会释放对应的空间容量，这里可以尝试并发删除文件的数据包让它额外释放更多的空间容量实现无限空间扩容。  
  
    当前知识库内已经上传几个文件占用了一定的容量，这两个文件一个占用300多MB，一个占用500多MB  
  
![](https://mmbiz.qpic.cn/mmbiz_png/A3icsHic8DribaIH5RGMgbN3WnW3TucfYkK63WvHssBykIj98ZyMKOCibKGcAdNO5EN6u4ysUkCB65lGmW7bxzZxWiahNOOGCvD2jUCp6oD8ry34/640?wx_fmt=png&from=appmsg "")  
  
尝试对其中一个文件进行删除操作  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribbdE5e8WibRCbf9ysKLHIMRquPm6m3fqAwlbVRBLOBWhjadMXOMryibWFS8OcUzX7dYODudGwTGT6czA5gdkDE1UviaRPC0ibNA42k/640?wx_fmt=png&from=appmsg "")  
  
尝试使用turbo插件发现无法利用插件并发；点击多个数据包进行一个同时发送试试；bp开启拦截，然后多次点击删除功能，生成了多个数据包  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribbooD0Fu9oVfHOqg40mdprIFBDlAkZBrcbJUEEgeAcfUrdpJYK6GKEZkLLlicuyzOBjGuE2W1WpSDswPurWiaccrAGlicXcsbPkJQ/640?wx_fmt=png&from=appmsg "")  
  
直接放包，发现在另外一个文件仍然存在的情况下，免费空间占用为0  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/A3icsHic8DribavPGYgqibEwlpEBjPe7YslfqZVtE29z1HGpeNnohiaxcTqqNLgqLNhCzs2FfgoxnXEWtb87YJpS9U1icxvq6pRicEszYOyZTEg5RM/640?wx_fmt=png&from=appmsg "")  
  
再次上传新文件，从0开始计算  
  
![](https://mmbiz.qpic.cn/mmbiz_png/A3icsHic8DribZjjkVg6vDWwQ82ia0ZgeWT54SPyszBodosawibd97LD64wyC97XbBNx40drJlTbgvJ2xTUsojRzzpDULlwVDko4msmH7nBWv1Gc/640?wx_fmt=png&from=appmsg "")  
  
即可通过反向并发实现空间的无限扩容的一个操作  
  
ps：本篇仅用于个人技术案例分享，欢迎师傅们讨论交流。  
  
