#  【接口漏洞第八章第二节】挖掘GraphQL漏洞第一步：高效发现端口的三大实战技巧  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-01-21 10:44  
  
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
上一节[【接口漏洞第八章第一节】挖洞前必修课：一文读懂GraphQL API核心概念](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797764&idx=1&sn=da6733327b48ce9bb23c60e66c1b6583&scene=21#wechat_redirect)  
中，我们大概了解了  
GraphQL API的相关概念，今天我们来进一步了解下，  
如何  
寻找GraphQL端点  
  
在测试  
GraphQL API之前，首先需要找到其端点。由于   
GraphQL API 所有请求都使用同一端点，因此这一信息非常关键。  
  
注意：我们在这里介绍的是如何  
手动探测GraphQL端点。但   
BurpSuite 工具的   
Scanner 在扫描过程中可  
自动测试 GraphQL 端点，若发现此类端点，工具就会报告“发现GraphQL端点”问题。如下，就是工具自动发现的端点。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3F93Cd2L6ddp5TeXdia32XlX8o1dicKdD2Yc1jxReqxHicdIjwyNSOrkQZQy5QSTcQRLI7HAYaozuyQ/640?wx_fmt=png&from=appmsg "")  
  
通过通用查询来查找端点：  
  
如果向任意GraphQL端点发送查询   
query{__typename}，其响应中某处会包含字符串  
 {"data": {"__typename": "query"}}。这称为“通用查询”，这是是探测某URL是否对应GraphQL服务的实用方法。  
  
此查询之所以有效，是因为每个GraphQL端点都有一个保留字段   
__typename，该字段会以字符串形式返回被查询对象的类型。  
  
通过常见端点命名来查找端点：  
  
GraphQL服务常使用相似的端点后缀。测试GraphQL端点时，可尝试向以下位置发送通用查询：  
- /graphql  
  
- /api  
  
- /api/graphql  
  
- /graphql/api  
  
- /graphql/graphql  
  
  
如果这些常见端点未返回GraphQL响应，还可尝试在路径后追加   
/v1。  
  
注意：  
  
GraphQL服务常对任何非GraphQL请求返回“  
查询不存在”或类似错误。测试端点时请记住这一点。  
  
通过不同的请求方法来查找端点：  
  
尝试使用不同请求方法也是  
寻找GraphQL端点的一种方式  
  
通常情况下 GraphQL 端点最佳做法是仅接受   
content-type 为   
application/json 的   
POST 请求，这有助于防范CSRF漏洞。但有些端点可能接受其他方法，例如   
GET 请求或使用   
x-www-form-urlencoded 作为   
content-type 的   
POST 请求。  
  
如果通过向常见端点发送POST请求未能找到GraphQL端点，可尝试使用其他HTTP方法重新发送通用查询。  
  
通过以上方式后，一旦发现端点，我们就可以发送一些测试请求以进一步了解其工作原理。如果该端点支撑着某个网站，可尝试在浏览器中探索该Web界面，并通过HTTP历史记录检查发送的查询，并进一步挖掘   
GraphQL API 相关漏洞。更加详细的挖掘方式和思路，我们在后续章节中，会陆续分享。  
  
今天的内容就先分享到这，对这块感兴趣的话，可以点点关注，这边会持续输出相关分享内容。  
  
觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。  
  
