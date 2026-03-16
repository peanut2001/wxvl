#  【服务端漏洞-访问控制缺失-第五章第四节】挖洞实录：一个Content-Type验证缺陷，让我拿到了服务器的敏感信息  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-03-16 00:22  
  
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
在上一节中[【服务端漏洞-访问控制缺失-第五章第三节】从0到1：文件上传漏洞之Content-Type绕过实战解析](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797982&idx=1&sn=af742e28558d10009e29206077e76183&scene=21#wechat_redirect)  
 我们对文件上传时使用的 content-ytpe 进行了分析，这个地方如果控制不当，就极有可能会造成漏洞的产生。  
  
今天这里就结合着这个内容，给大家分享一下在实际情况下，如何对这块内容进行验证并实现漏洞的挖掘、利用的。  
  
同样的，这个系统中存在一个头像上传的功能，我们上传正常的图片后，是能够正常上传，并能返回图片上传到服务器后，通过什么样的路径来访问该文件。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGEpeU4GGB2wlGQdOBPQbp2gB2KK8Rf7X7icav4gmSVo44X51W2jD2qdPzJ9HjpicNRUYxicDsxJTgoamdgviboePSjBEiaqUW9Yialia0/640?wx_fmt=png&from=appmsg "")  
  
当尝试直接上传带一句话木马的.php文件后，发现系统是有做限制的。系统不允许我们上传非png 和 jpeg 格式的文件。具体如下  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGGNp1JZrCHf8FT3QDn57k02FibK7EYiaxzy0FGCkm9DSgEqbib4ibxpNmbdwmGQ1fxiauNthX8n2MoKhBAnXmicZWvoxV2sofGsKENNU/640?wx_fmt=png&from=appmsg "")  
  
遇到这种情况时，我们就可以结合上一节的理论知识，对系统在上传文件时的 content-type 进行验证测试了。如何验证？很简单，只需要将这个上传一句话木马的请求，用burpsuite进行抓取，并发送至repeater中。直接请求后，系统服务器是返回拒绝的提示的：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGH1GOpxWUF8F8G77KSd28BjMSeUHtJzjEYSvnuVx6uLRaZibOTzN1cLeMdtdCmTdibKsmezSQ58Ox9HZhVnXic7LWqMXqeXv50h0E/640?wx_fmt=png&from=appmsg "")  
  
这里需要注意的是，在上传文件请求时，可以发现系统是会自己获取到上传文件的   
content-type 的，如上面这个图中，系统自身就会将这个  
content-type 按照我们实际的文件类型进行设置并发送给服务器。这里的这个文件的   
content-type 是   
text/php.  
  
这个时候，如果我们直接将这个文件的   
content-type 修改为符合系统要求的图片类型呢？会不会就能直接欺骗并绕过系统的限制？直接在repeater中将   
content-type 修改为   
image/jpeg  
，果不其然，直接成功。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGFWmTvI7JibOsDm2tE12wm3o0BrGjQkIkdvsxyX9q5GJ8vmzzmjZIdwe1Slibj55dLlFOyI8ndnesjVBtoqcUCAP9Ba8IslvqRVc/640?wx_fmt=png&from=appmsg "")  
  
检验上传结果，直接访问已上传的文件地址即可，成功执行并达到预期效果，直接获取到服务器的密码信息：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGHCz1ibBDZ4xqKAeqSXq2b6CTEpNvY2RKZqKpnz7cQHKrWnz3fs81YC7FHXUh6icaV9XEMBeJ9dt6WNpkgZ2tDicXw7Y5OsKkKIIM/640?wx_fmt=png&from=appmsg "")  
  
好了，结合上一节的分享的根据系统的 content-type 做进一步验证并渗透的实际案例，今天就分享到这。关于服务器的各种漏洞，这边还会持续地分享输出，感兴趣的话，可以点点关注。  
  
觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
  
  
