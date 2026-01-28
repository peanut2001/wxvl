#  【接口漏洞第八章第八节】攻防升级：实战绕过GraphQL内省防御机制  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-01-28 11:30  
  
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
我们在前面章节[【接口漏洞第八章第七节】赏金猎人实战：如何快速从GraphQL自省中挖出高危漏洞](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797816&idx=1&sn=d650326041af511587bcf818de924354&scene=21#wechat_redirect)  
和[【接口漏洞第八章第六节】GraphQL端点发现了，然后呢？实战利用自省功能“透视”API](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797795&idx=1&sn=a305ddf68d807bf90e068d78fea239bd&scene=21#wechat_redirect)  
中，详细分享了如何利用  
GraphQL 内省功能，并实现漏洞挖掘。但如果系统对这块功能有进行防御的话，我们又应该如何做呢？  
  
今天我们就来分享一下如何绕过   
GraphQL 内省防御机制  
  
如果无法在测试的 API 中执行内省查询，可尝试在  
 __schema 关键词后  
插入特殊字符。  
  
当开发者禁用内省功能时，可能会使用正则表达式来排除查询中的   
__schema 关键词。此时可尝试添加  
空格、  
换行符或  
逗号等字符，因为   
GraphQL 会忽略这些字符，但存在缺陷的正则表达式可能不会忽略。  
  
例如，若开发者仅排除了   
__schema{，则以下带换行符的内省查询将不会被排除：  
```
graphql
# 带换行符的内省查询
{
    "query": "query{__schema
    {queryType{name}}}"
}
```  
  
若此方法无效，可尝试通过其他请求方法发送探测请求，因为内省功能可能仅针对   
POST 请求被禁用。可尝试使用   
GET 请求，或   
Content-Type 为   
x-www-form-urlencoded 的   
POST 请求。  
  
以下示例展示了通过 GET 请求发送的 URL 编码参数内省探测：  
```
# 以 GET 请求发送的内省探测
GET /graphql?query=query%7B__schema%0A%7BqueryType%7Bname%7D%7D%7D
```  
  
如果通过手动一个个添加特殊字符，效率较低，这时我们就可以通过使用burpsuite的intruder来进行辅助测试。具体如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q0EXw8iajmdCicADsCAdz4muwfYz7CDF5QGsF5gggWzI6QZqZ9AADvjcmUv4ao6q10mb7J3aAMfSV1Q/640?wx_fmt=png&from=appmsg "")  
  
好了，关于如何绕过  
GraphQL 内省防御机制  
，今天就先简单介绍到这，明天我会结合具体的实际场景，对这种绕过方式进行分享，感兴趣的话，可以点点关注。  
  
觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。  
  
