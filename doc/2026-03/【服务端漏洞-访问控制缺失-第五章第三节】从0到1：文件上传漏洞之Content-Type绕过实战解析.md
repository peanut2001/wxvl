#  【服务端漏洞-访问控制缺失-第五章第三节】从0到1：文件上传漏洞之Content-Type绕过实战解析  
原创 升斗安全XiuXiu
                    升斗安全XiuXiu  升斗安全   2026-03-15 04:56  
  
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
上一节[【服务端漏洞-访问控制缺失-第五章第二节】漏洞分析：文件上传功能中，那些“想当然”的设计是如何酿成大祸的](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797976&idx=1&sn=fd4af414403b1625f7564c508d8ba841&scene=21#wechat_redirect)  
 这边给大家分享了一个简单的文件上传漏洞挖掘及利用方式。  
  
但在实际场景中，我们很难遇到像之前分享案例那样完全未设置文件上传防护的网站。但这并不意味着现有的防御机制就足够稳固——即便存在防护措施，我们仍有可能利用其中的设计缺陷成功获取Web Shell，实现远程代码执行。  
  
怎么做？这里就涉及到“  
有缺陷的文件类型验证机制”了  
  
在提交HTML表单（上传文件的请求）时，浏览器通常使用内容类型  
application/x-www-form-urlencoded的POST请求发送数据。这种格式适用于发送简单的  
文本信息（如姓名或地址），但并不适合传输大量二进制数据，例如完整的图像文件或PDF文档。在此类场景下，通常会使用  
multipart/form-data内容类型。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGFBoYwgp86koV6CxsecETtFq69ricjb1ouywSeiaTekEnLK9vDht195ibsSEopo3fWfH3otd3IUIadg2W7qpy1gTibsxkcGx9hRUsI/640?wx_fmt=png&from=appmsg "")  
  
假设存在一个包含图片上传、图片描述及用户名输入字段的表单。具体提交该表单时生成的请求报文可能如下所示：  
```
POST /images HTTP/1.1
Host: normal-website.com
Content-Length: 12345
Content-Type: multipart/form-data; boundary=---------------012345678901234567890123456
----------012345678901234567890123456
Content-Disposition: form-data; name="image"; filename="example.jpg"
Content-Type: image/jpeg
[example.jpg的二进制内容...]
-----------012345678901234567890123456
Content-Disposition: form-data; name="description"
```  
  
这种上传内容中通常还会包含一些有趣的图片描述文本，比如下面这段。这些也是我们需要关注的。  
```
------------012345678901234567890123456
Content-Disposition: form-data; name="username"
wiener
------------012345678901234567890123456--
```  
  
如示例所示，报文主体根据表单输入字段被分割为多个独立数据块。每个数据块都包含  
Content-Disposition头，提供对应输入字段的基础信息。这些数据块还可能包含  
各自的Content-Type头，用于向服务器声明通过该输入提交数据的  
MIME类型。  
  
网站验证文件上传的一种方式是  
检查输入字段特有的 Content-Type 标头是否  
与预期的 MIME 类型匹配。例如，如果服务器只期望接收图像文件，它可能只允许 image/jpeg 和 image/png 这类类型。当服务器隐式信任此标头的值时，问题就可能出现。  
  
如果服务器没有执行进一步的验证来检查文件内容是否确实与其  
声称的 MIME 类型相符，那么这种防御措施就可以使用 Burp Repeater 等工具轻松绕过（直接修改  
Content-Type 标头  
的允许上传类型  
）。  
  
关于文件上传的另一个关注点，今天就先分享到这。至于如何结合以上内容，来进行实际的实验尝试，这边后续会继续给大家分享，感兴趣的可以先点点关注。  
  
觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png "")  
  
  
