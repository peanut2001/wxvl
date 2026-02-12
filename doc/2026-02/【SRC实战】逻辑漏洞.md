#  【SRC实战】逻辑漏洞  
 迪哥讲事   2026-02-12 03:00  
  
📝 **编者语**  
  
兄弟们，最近挖洞挖得我有点“不好意思”了。  
  
以前觉得挖洞是高智商攻防，是黑客与开发者的巅峰对决。但最近遇到的这几个系统，让我感觉开发者仿佛在给我发春节红包。  
  
今天遇到的两个逻辑漏洞，全是“送分题”。来，一起感受下这种朴实无华的快乐。  
  
(注：本文所有敏感信息已脱敏，仅供安全研究与教学交流，请勿用于非法用途。)  
  
1  
  
马年“送”码  
  
那天下午，我看上了某个小程序的登录框。  
  
输入手机号，点“发送验证码”，本来已经做好了要掏出   
Burp Suite  
大干一场的准备。  
  
我想着：是要爆破呢？还是要在参数里绕过签名？  
  
结果，当我习惯性地看了一眼  
Response  
时，我沉默了。  
  
服务器给我的回显是这样的：  
```
{
"code": "200",
"msg": "success",
"data": {
"verifyCode": "8842"  <-- 没错，它就在这
}
}
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zLwtVUBEibzhvxzLXqGOSw0XM1gPPRmaz8CLoRP3U3CMyD2XXCgBcJTiado6adSEcDaP8lS9bcStvA/640?wx_fmt=png&from=appmsg "")  
  
我当时就揉了揉眼睛。  
  
这就给我了？  
  
咱们之间是不是应该有点起码的“信任危机”？你把验证码直接放在响应包里，是怕我手机欠费收不到短信吗？  
  
操作步骤简直到离谱：  
  
1. 填入舍友的手机号。  
  
2. 点发送，拦截包。  
  
3. 抄下回显里的数字。  
  
4. 登录成功。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zLwtVUBEibzhvxzLXqGOSw0RNh9RILtmhs6wk2BO5WgpAUgTKfYGQwibrmg6RuD93UOlIgia6X51qiaQ/640?wx_fmt=png&from=appmsg "")  
  
这就是传说中的  
**露天大红**  
？补偿局？  
  
2  
  
暴力美学  
  
都知道是  
**大红局**  
了，那还不得好好挖挖，我又瞄了一眼注册接口。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4lN9trz7FSdNiaNcM6RhFh9mqPEg1ib5uSo9ueZ2suD99I2nTbLdlKQ89mBhIbPnvp9bqF7TsjTRUGVjhfLRo8ZPZJDibwWzs5uTU/640?wx_fmt=png&from=appmsg "")  
  
这次开发学聪明了，响应包里没有验证码了。  
  
但是，我又发现了一个盲点：验证码只有  
4  
位数。  
  
0000 - 9999  
，一共才  
10000  
种可能。  
  
关键是，我试着输错了几次，发现系统毫无反应——没有验证码错误次数限制，也没有频率限制。  
  
同时有明确的判断条件  
  
当输入错误的验证码，服务端返回4  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4kOmwuAWAlIf3EUg1Mky7wjsVS6SMMjNJs1M3nQp23WycvNXGR0O3QZicTcdHJRHhQicvUPlZEHtKicX4rWbhsTlvLeyqDND0iaQN4/640?wx_fmt=png&from=appmsg "")  
  
当属于正确验证码，服务端返回1  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zLwtVUBEibzhvxzLXqGOSw0Y5A3JyaRqibApysFCYrG8sw0uKLR2ic7eR9q599OwEnzk389ITAiaorHg/640?wx_fmt=png&from=appmsg "")  
  
既然嫂子都同意了，那我就不客气了。  
  
掏出  
Burp Suite  
，加载字典，线程拉满。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zLwtVUBEibzhvxzLXqGOSw0aibBEvFpa4ONxF9HxGEdZicw8NMtjvD5NJzwN4IUWic8nRxReIzsqOfZQ/640?wx_fmt=png&from=appmsg "")  
  
开始了嘛？不已经结束了！  
  
你怎么那么快？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zLwtVUBEibzhvxzLXqGOSw0PsibnTpsE82U5zJFwribY0EP4CMFaKMpl4mINKxfP9ev0CtfRkq0yibicw/640?wx_fmt=png&from=appmsg "")  
  
4 位数 + 无风控 = 嫂子你在“裸奔”啊。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zLwtVUBEibzhvxzLXqGOSw0v15aymtLEIoVSL34E7lwVIg7qN6vQsiaQlScUkLWVQsJqkCiaQmXLibVw/640?wx_fmt=png&from=appmsg "")  
  
这就意味着，我可以批量注册几千个账号，甚至把他们的数据库塞满垃圾数据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34zLwtVUBEibzhvxzLXqGOSw0zeSOwBsicA1ppEV32Jk8W1X7toaslHCggSbMmib6Lcpp3c6I0GAIIMcQ/640?wx_fmt=png&from=appmsg "")  
  
  
3  
  
举一反三  
  
今天这两个洞，就是短信验证码业务中最经典的安全盲区。  
  
如果这两个点被堵住了，我们是不是就没戏了？  
  
当然不是，逻辑漏洞的玩法远不止于此。  
  
在实战中，针对验证码/登录逻辑，我们通常还可以尝试以下姿势：  
  
1. **验证码复用：**  
  
有些系统虽然有验证码，但验证成功后不销毁。这意味着我可以拿着一个正确的验证码，在有效期内无限次使用，直接批量修改密码。  
  
1. **万能验证码：**  
  
为了方便测试，开发有时候会留后门，比如  
8888  
或  
0000  
可以登录任意账号。别笑，这种事在很多外包项目里真的存在。  
  
1. **返回包篡改：**  
  
如果后端只校验状态码（例如前端  
JS  
判断  
code: 200  
就跳转），那我们直接拦截响应包，把  
code: 403  
改成  
200  
，有时候能直接欺骗前端进入系统。  
  
1. **并发竞争：**  
  
如果系统有“每天只能发送  
5  
次”的限制，试试用   
Turbo Intruder  
发起高并发请求，瞬间发出去   
100  
个包，往往能突破次数限制，甚至造成短信轰炸。  
  
  
  
挖洞永远不是死记硬背，而是比开发者多想一步。  
  
  
如果你是一个长期主义者，欢迎加入我的知识星球，本星球日日更新,包含号主大量一线实战,全网独一无二，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg "")  
  
往期回顾#   
# 如何利用ai辅助挖漏洞  
#   
# 如何在移动端抓包-下  
#   
# 如何绕过签名校验  
#   
  
[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)  
  
  
[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)  
  
  
[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)  
  
  
[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)  
  
  
[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)  
  
  
[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)  
  
  
[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)  
  
  
[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)  
  
  
[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)  
  
[‍](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)  
  
  
  
  
  
  
