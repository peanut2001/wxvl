#  【服务端漏洞-访问控制缺失-第四章第三节】SSRF进阶：从“受限访问”到“内网横移”的实战绕过技巧  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-03-12 09:55  
  
**【文章说明】**  
- **目的**  
：本文内容仅为网络安全**技术研究与教育**  
目的而创作。  
  
- **红线**  
：严禁将本文知识用于任何**未授权**  
的非法活动。使用者必须遵守《网络安全法》等相关法律。  
  
- **责任**  
：任何对本文技术的滥用所引发的**后果自负**  
，与本公众号及作者无关。  
  
- **免责**  
：内容仅供参考，作者不对其准确性、完整性作任何担保。  
  
**阅读即代表您同意以上条款。**  
  
****  
在上一节[【服务端漏洞-访问控制缺失-第四章第二节】一个SSRF，打穿内网：漏洞挖掘实战案例分享](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797952&idx=1&sn=665d76f5fbadb07c6987efd0eb4b882e&scene=21#wechat_redirect)  
中，我们分享了一个比较简单的   
SSRF 漏洞挖掘场景  
。但在很多情况下，很多系统的内网都是做了限制的，只允许你访问内网的特定位置和数据。  
  
但在某些情况下，应用服务器能够与用户无法直接访问的后端系统进行交互。这些系统通常拥有不可路由的私有IP地址。由于网络拓扑结构的保护，后端系统的安全防护往往较为薄弱。许多内部后端系统包含敏感功能，任何能够与其交互的人都可以在无需认证的情况下访问这些功能。这可能就会造成“  
内网横移访问”的情况产生。  
  
具体是怎么出现的，这种漏洞的表现又是怎么样的？今天这边就结合一个实际例子来给大家分享一下  
“  
内网横移访问”的情况。  
  
这个系统，跟上一节的系统存在相同的功能，都是从第三方中获取数据，但它不同的是，它是从服务器内网IP地址中获取的，具体如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGFTD7jYgrt0vYM1OF5jicic4jazxPbOH6qKoCGLMZ2n6tJ7w3ic6LMxo1X5kRu7oQ7I3BCmLcStXiaVWW0wNk5zpJ2nW4W7xw8HYwc/640?wx_fmt=png&from=appmsg "")  
  
可以发现，获取数据的请求地址是内网IP地址+端口号的。我们直接将这个地址改为访问内网的根目录，看下是怎么响应的：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGG7jDH59jbo8icakKDSeibwqbhkGNo0Mue011w5hncXaNG3EMoHz8blFzBo4r4XsjjmtZN2bOlB5bAsXpxJ4FYNVwG9ENdngv1jw/640?wx_fmt=png&from=appmsg "")  
  
发现系统是限制了只有固定的内网访问路径才允许访问的，其他路径访问均会返回“  
Missing parameter  
”的提示了。  
  
这种情况下，不能轻易放弃，既然系统明确告知了是可以向内网系统获取数据的，那么有没有可能系统中存在了其他的内网IP？这些内网IP有没有可能没有那么强的限制？  
  
要验证以上猜想，我们可以将以上请求发送到intruder中，来遍历请求内网IP地址，看看是否有意外收获：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGFjyKgP8kw2LO6RcoMqvPuArh6DnrKuPoEBHqJ0iaLRqPlRyNbX7JCx8bqMtIwllHwicaPBmNcMQF2mx2HIIbLDGA9iaoPgtiama6A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGEF9Pib6Xqj0e0AvHxUoj0btXLp6RsZhAeNyxVwum4urC1AZVvRWLkCmicGvEDYZ5PjgHiatd9z9DDgc1oTXGQrH6rLGoFsHXF0mU/640?wx_fmt=png&from=appmsg "")  
  
经过遍历后发现，这个系统除了请求内网IP地址192.168.0.1以外，还对  
192.168.0.113也开放了请求数据的权限，直接返回了404的状态码。  
  
这就是意外的收获了，针对这个例外的内网地址，我们只要尝试访问系统常用目录，就有可能成功欺骗服务器，并拿到本无权限操作的内容。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHzW7rEv0Ksnyia7Q3XXAeFfuBHNnv7I3Cg5UTa0oxa9ibhbPDBxCkqZrWTmNVBo7RqiccicPVrzwrGicMSCxjNO9CmUaqO9FdChX8Q/640?wx_fmt=png&from=appmsg "")  
  
如以上，当我们通过内网IP地址 192.168.0.113:8080/admin 来欺骗服务访问数据时，服务器竟然真的给返回了内部操作的地址。这样，我们就只需要将这些内部的操作地址放入，就成功达成了欺骗服务器进行越权操作的目的了。  
  
好了，关于SSRF的进阶漏洞挖掘案例，就分享到这了。后续这边还会继续分享更多有关服务端的漏洞原理、利用、挖掘方式，感兴趣的你，欢迎关注。  
  
觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
  
  
