#  【接口漏洞第八章第七节】赏金猎人实战：如何快速从GraphQL自省中挖出高危漏洞  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-01-27 10:41  
  
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
在上一节[【接口漏洞第八章第六节】GraphQL端点发现了，然后呢？实战利用自省功能“透视”API](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797795&idx=1&sn=a305ddf68d807bf90e068d78fea239bd&scene=21#wechat_redirect)  
中，我们知道如何通过利用 GraphQL API 的自省功能，发现可疑的参数，并尝试对可疑参数的校验。  
  
但应该不少小伙伴应该会有相同的疑问，通过自省功能后，得到的参数和接口都非常多，如果一个个验证，非常耗时费精力。有没有简单快速验证的方法呢？当然是有的，今天我们就给大家分享对  
自省功能得到的接口进行快速审查的具体的方法。  
  
首先，同样的是先找到确定的 GraphQL API 端点路径，然后使用burpsuite进行抓取，并发送到该工具的repeater中。比如如下这个，在请求登录之后请求了 GraphQL API端点。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q26iaumHlsdTfxfCQicCaRxWniaEK6FAMpviacLq6xyBlqgKb5ich8n1WqnjmGdSv0Zf3y8iawVXT59mzMQ/640?wx_fmt=png&from=appmsg "")  
  
跟上一章节同样的，我们就可以  
直接进入repeater菜单中的 GraphQL 功能，并选择 Set introspection query 功能项，对接口进行自动拆解，获取内部文档内容。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q26iaumHlsdTfxfCQicCaRxWnFiaonEDKNtKArPFsHRicRzwI9IoiaBMCkWA8tDC2UHlm0gZSwd4ibLDIeA/640?wx_fmt=png&from=appmsg "")  
  
接下来这一个步骤就跟上一章节不一样了，  
这个步骤也是本次分享的重点内容，在获取到API内部文档内容后，我们可以右键，将响应的文档内容直接发送至工具的   
site map  
 中，这样就可以自动将获取到的文档详细内容，直接转换为具体的请求体内容。具体如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q26iaumHlsdTfxfCQicCaRxWnXh7ExdKjHRwUf1MyaqvEyuaGHQoM5JMnyiazSMiceSvibZ3elxGBHF9Lw/640?wx_fmt=png&from=appmsg "")  
  
我们来看看在  
site map  
 中，会转换成什么样，正如前面介绍的一些基础知识一样，   
GraphQL API  
 端点，都是通过不同的请求体来控制响应内容的，所以我们看到转换内容中，也就是生成了大量相同访问路径，不同请求体内容的请求。具体如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q26iaumHlsdTfxfCQicCaRxWns1ZtUzAremBicW9eTbdz1iclTMc3LnyiavXyZic20Onk2kQEzTdsvxPiciaA/640?wx_fmt=png&from=appmsg "")  
  
最后，在一次性获取到所有已解析的请求路径及请求体内容后，我们只需要简单审查下生成的请求路径，就可以发现并验证可疑的   
GraphQL API  
 端点，比如通过审查以上得到的端点和请求体内容后，发现一个可以通过ID来查询用户名密码的自省参数详情。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q26iaumHlsdTfxfCQicCaRxWnp7W6lVQpjE7pYJ2MP48dDd3Dic9cG6lfiauPvJCxF606FOvEFrSKvh8w/640?wx_fmt=png&from=appmsg "")  
  
这下我们要验证自己的猜想就很简单了，直接将该请求发送至repeater中，并将id的值修改，就可以验证了，如下，当修改为1后，直接能够获取到超级管理员用户名密码。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q26iaumHlsdTfxfCQicCaRxWn0dhxDbgmRNoiaYKwKksh5SiadhnguLhoXR8Wk1gnzmR0xmNQZvKhrZpQ/640?wx_fmt=png&from=appmsg "")  
  
好了，关于快速梳理自省功能后获得的文档内容的实际操作内容，就分享到这里。后续这边还会继续分享更多有关API接口漏洞的内容，感兴趣的话，可以点点关注。  
  
觉得内容对你有用或无用，欢迎点赞或留言，这边会不断更正。  
  
