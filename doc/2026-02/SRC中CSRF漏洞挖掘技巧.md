#  SRC中CSRF漏洞挖掘技巧  
原创 锐鉴安全
                    锐鉴安全  锐鉴安全   2026-02-21 23:00  
  
部分X  
  
dian'ji'weigweiID  
  
  
  
，  
  
zai  
  
  
cizhi'cizhici  
  
  
s  
  
“证书站的未授权漏洞，忆校园青春  
[阅edu证书站的未授权漏洞，忆校园青春](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486254&idx=1&sn=993cd82bceba042301a009c28ca2d251&scene=21#wechat_redirect)  
  
  
  
点击蓝字 关注我  共筑信息安全  
  
  
  
  
  
  
￼  
  
免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任！  
  
  
  
  
1  
  
  
  
  
背景  
  
  
本次实战的案例，源于某高校的人脸采集系统，听着都感觉危害很大，因为全是敏感信息，如身份证、人脸等，拿到就是高危漏洞。从无账号到登录系统，靠的就是fuzz，详细的过程见实战过程。  
  
  
  
  
  
  
2  
  
  
  
  
实战过程  
  
  
通过一系列的信息收集，高校的人脸采集系统引起了作者注意，为什么？因为有敏感信息。  
  
  
  
  
连Hunter、Fofa都没索引到这个系统，作者靠灯塔拿到了，灯塔确实好使，关键还免费，需要的师傅可以文末获取下载链接！  
  
  
  
  
系统的首页如下图，可以看到，只用一个登录按钮。  
  
  
￼  
  
  
  
  
看下findsomething，也没有找到“注册”功能相关的关键字，同时也跑了下接口，并无接口未授权问题。  
  
  
￼  
  
  
  
  
  
本次案例的关键操作来了，首先抓包观察下登录系统的数据包情况，随意输入账号密码，点击登录。  
  
  
￼  
  
  
  
可以看到登录的数据包中有个login关键字，秉着试试的心态！  
  
  
作者将login改为register，惊喜时刻，注册账号成功。  
  
  
￼  
  
  
  
使用注册成功的账号登录系统。  
  
  
￼  
  
  
  
可以看到获取到了身份凭证。  
  
  
￼  
  
  
  
登录到了个人信息首页。  
  
  
￼  
  
  
  
任意用户注册账号漏洞拿下，这个fuzz操作确实有点妙。都登录系统，肯定得把全量的功能测一遍，一般可以测试sql注入、越权、文件上传等漏洞。  
  
  
  
  
co  
  
  
点击蓝字 关注我  共筑信息安全  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlNDd8O4wJKfGhV48dQHTMk8icXxCBI5BKxPqWQOfwFWxPtG2e8iazqUssJg/640?wx_fmt=png&from=appmsg "")  
  
**免责声明：**  
请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息、工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任！  
  
  
**1**  
  
  
  
**背景**  
  
分享一个CSRF漏洞挖掘的技巧，无论是SRC还是安全仔的安全服务服务都用的上，并附上了一些实战案例，详细过程见实战部分。  
  
  
号外号外，  
免费的睿鉴安全知识库持续更新中。点击下发链接，福利直达！！  
  
  
  
模块介绍  
  
安全知识模块主要会放一些学习材料以及之前个人的一些实战案例，目前  
已更新资源，含四期案例集合，还在持续上新中，请各位师傅持续关注。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVK44khe5C5Giad8m3micGSgWJUz9Nl2DIGwH0EDoptibuqicg8JibzrkkBtwhxicnKzFciaETXxAr7IIpGDcp4XKqSNeIL8IHcjTCrXY4/640?wx_fmt=png&from=appmsg "")  
  
  
主要的一些案例  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVIzEkhLwKc41VkyNOibI5Lv4G6q5f32L6NxnTgyzAnsaCCLgvs9iciczu4icWShHc2koPLN7oyXYpXQGUakXEoqW61efmUSiaGu8UPk/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVKsXVZtpTYkTB5Z4hDGX4I1u8moJaE9fjGQn9XYIME4DtWU4tLhrr46AOK9S3tWwhBghz0JCM3jV7IoQXtuiaV7wt684TdluEj0/640?wx_fmt=png&from=appmsg "")  
  
  
  
资源中心主要会放一些个人经常用到的工具，做成了一个集合，目前已发布十几款工具，后续各位师傅可以直接在这里获取到下载链接。一站式获取到你想要的工具。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVJXnTTAZQ08cFZqfeeproGFOG0iccKVDichC29XV5ibZStJLicma2D6ZK25C2KtkIciaPicGJmK6lPCL29UfJWko2QWKyAeBqK4eswFw/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVLaibEkS7L7gUcPJQl21aAs5cNYic7NOq27ibMUH9LXnJKOib1LyicRTWSHpEwHor6YHI7qRaYiaF15BQpIZ9ia7UqtYng9IWsiaEjDc6k/640?wx_fmt=png&from=appmsg "")  
  
  
**2**  
  
  
  
实战过程  
  
什么时候会发生CSRF?当我们可以使目标对象浏览器发送HTTP请求到别的Web 网站时,就会发生跨站请求伪造（CSRF)攻击。  
  
  
该Web网站会执行一些操作,使得请求看起来是有效的,并且发自目标对象。这种攻击一般依赖于目标对象之前已经通过了具有漏洞的网站的身份认证,并且攻击者向该网站发起的提交动作和网站的响应不被目标对象感知。  
  
  
当CSRF攻击成功时,我们就可以修改服务器端信息并很有可能完全接管用户的账号，以及造成一些DDOS攻击如造成全量用户自动退出登录账号。  
  
  
方式一：GET方法的CSRF  
  
攻击者需要在发送给李X网银的HTTP转账请求中包含李X的cookie信息。但是因为攻击者没有办法读取到李X的cookie，所以他不能只是简单地生成一个HTTP请求并发送给李华的网银。  
  
  
相反，攻击者可以使用HTML 的<img>标签来精心生成一个包含李X cookie的GET请求。<img>标签对网页上的图像进行渲染，并且包含一个用来告诉浏览器去哪里定位图像文件的src属性。当浏览器渲染<img>标签时,它会向标签的src属性发起一个包含任何已有的cookie的 HTTP GET 请求。  
  
  
方式二：POST方法的CSRF  
  
这种类型的CSRF危害没有GET型的大，利用起来通常使用的是一个自动提交的表单，也更难去利用，如：  
  
<form action=http://XXX/csrf.php method=POST>  
  
    <input type="text" name="xx" value="11" /></form><script> document.forms[0].submit(); </script>   
  
  
访问该页面后，表单会自动提交，相当于模拟用户完成了一次POST操作。  
  
  
实战案例  
  
某站的个人信息中心，发现保存图片的参数可控，登录之后来到个人中心。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVI4bice8ArWNrU1asibS1VTZUgEkq9fYrHhaXfOhMZ9B7UoXhNuIYCPhdjEiaLOPgYVtvPsS7HQcKDBZllvWic6ghPpARVSRuT4BWk/640?wx_fmt=png&from=appmsg "")  
  
  
点击更换头像，可以发现portrait就是存头像的地址，把这个包发送到repeat尝试修改为其他地址。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVKcCbp0hamYAcgc0A7sWB6qgVmPy4AQGVAGq2ZNiac38ExUgdEkjicPzMvIhsfAiaCG9uUQTz6UdddtVPf3CBP1vsic0DJcT4KEkug/640?wx_fmt=png&from=appmsg "")  
  
  
这时候，可以看下登录退出功能的具体链接，用于下一步的用户DOS操作。假设为xxx/logout  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVKfGJxm4uicM38mpEvgJCjYlWljYYrEeBiaUeWCbQFq6Rzjd4DLibsKicEYoJTuhJYCgdbickNwyGmp5Jc4XicrQ5RicVvJEPkMCmNHLc/640?wx_fmt=png&from=appmsg "")  
  
  
替换完后，再次进入个人中心，此时会触发请求个人头像，如下图，会退出当前的个人账号。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVLylEak40GG4hyzNEUVkYSLq1F0kRRu6NqJVbbkV28dXMfic7eicDcRjOhiaic0qFSwa5DOKhKYmvgNSs17tLPx922CVyPA61QWPHk/640?wx_fmt=png&from=appmsg "")  
  
  
进一步的提升危害，可以在论坛、留言区进行浏览，那么此时，只要是访问了这个主题的用户，都会去请求xxx/logout的链接，造成当前用户账号退出，服务不可用。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qvoCyTM5aVKYZmGOtR075J7ybrDhWBIia5LbH7UdNa0mRtWvIzz4hySlrRYv25WVM4tia1UeHJ6RddWhIaRGkQusbUftZXVOynOUm1Efmqc18/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
3  
  
  
  
经验总结  
  
本次案例主要分享下CSRF的漏洞原因及主要的利用方法，希望对各位师傅有所帮助。  
  
  
  
  
  
  
往期好文推荐  
  
[记一次"高危"逻辑漏洞挖掘实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487704&idx=1&sn=f2f296b6870ed8ddbaa6d142c93ea114&scene=21#wechat_redirect)  
  
  
[安服仔薅洞必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487810&idx=1&sn=6fb51d171d6546386a5bdbda662046f7&scene=21#wechat_redirect)  
  
  
[记一次SRC支付漏洞实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487822&idx=1&sn=0cfb1fd7754a8bb5fee12d44e450cd53&scene=21#wechat_redirect)  
  
  
[记一次SRC渗透测试实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487518&idx=1&sn=9d4498c7829a31051be9ba9813d367ec&scene=21#wechat_redirect)  
  
  
[从微信扫描登录到账号接管，细节实战](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247488142&idx=1&sn=874e5fcfabd9dda5cccb9506c0b25fb8&scene=21#wechat_redirect)  
  
  
[更新|帆软、用友、泛微、蓝凌等常见OA系统综合漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487310&idx=1&sn=f27b0f1199b3f52b086d1c7dc18685d0&scene=21#wechat_redirect)  
  
  
[Web渗透测试综合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486715&idx=1&sn=1d507a1a89b525e5c1ad4d75d0d9eedc&scene=21#wechat_redirect)  
  
  
[Swagger漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487229&idx=1&sn=07acbbae48db8862efe4bb8062056a96&scene=21#wechat_redirect)  
  
  
[Java漏洞专项检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487205&idx=1&sn=e0d8353342f7d33fc3ce5bd5e747c861&scene=21#wechat_redirect)  
  
  
[渗透测试集成工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247487068&idx=1&sn=e343013c9f5a4f736865236e6dfd4bf0&scene=21#wechat_redirect)  
  
  
[AntiDebug_Breaker最新版,Hook必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486930&idx=1&sn=2684c990c45276e6fb23de5c48a1c85a&scene=21#wechat_redirect)  
  
  
[有趣的Fuzz+BucketTool工具等于双高危！](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486814&idx=1&sn=1d114995e1cf5745e824d2018cdbd615&scene=21#wechat_redirect)  
  
  
[推荐一款资产“自动化”筛选工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486679&idx=1&sn=288fe9f4312c3267c33765cfa9e3ab06&scene=21#wechat_redirect)  
  
  
[EDU SRC学号、账号等敏感信息收集工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486657&idx=1&sn=847f77601dd94eed5a5b04b5bf8176a1&scene=21#wechat_redirect)  
  
  
[Jeecg-boot最新漏洞检测工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486651&idx=1&sn=70d0e3d5ac4920684f52a4ee52531854&scene=21#wechat_redirect)  
  
  
[js.map文件还原组合工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486582&idx=1&sn=a08daa5cc01f04b813d827e5d8bf444b&scene=21#wechat_redirect)  
  
  
[Nacos漏洞检测专项工具,攻防必备](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486606&idx=1&sn=595219ca87296bd633d89d0e966d40a6&scene=21#wechat_redirect)  
  
  
[微信公众号，微信小程序，钉钉,飞书等第三方平台接管工具](https://mp.weixin.qq.com/s?__biz=MzkxMjg3NzU0Mg==&mid=2247486471&idx=1&sn=1a9ddf83c74be73ab70bbbf202771a19&scene=21#wechat_redirect)  
  
  
  
入交流群扫下方二维码：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/qvoCyTM5aVJPZ5SwuG3vOJxaKLd9l42U3Wic1TTXEkV2ic5gaNywwRnrrVRnBJVrwH3SLOEoJq6oia64VUwgJ7P0F1MtwMIvr6RL1jXSMtjjYQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/RLTNmn7FBP6LllD9Qm4I2eKvyHt1WlND18ovUTvvzp4MagwzrEIAu6ZHoicVWA2YvfmEgZicxv4tvVibeFB8T7w3A/640?wx_fmt=gif&from=appmsg "")  
  
  
