#  【动态靶场】一个博客系统，他有一个XSS漏洞-1  
 好靶场   2026-02-11 02:11  
  
## 靶场平台  
  
学安全，别只看书上手练，就来好靶场，靶场已开放，欢迎体验：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ODoR0oa3ju3KRDbjOtXzh2LbPrL3LkGBud1aODKOIl3PChux22GtfwOiaZiabMFqiaqdnh5FhMz6IgL2vQ8lljyLUk9N8f2o80lp9zCQltib3Tg/640?wx_fmt=png&from=appmsg "")  
  
🔗入口： http://www.loveli.com.cn/see_bug_one?id=430  
  
✅ 邀请码： 9f8316c443dd409a  
## 测试正文  
  
首先拿到一个站测试xss，要从用户可控的输入入手，看到搜索框用户可控输入内容  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ODoR0oa3ju1g7kNF1V11ca0OK406kibTxUmKFmZ0Sz7PhWhGb7Jmyyo7TmbClp10aMlZlbA7HTW0X1AxAb2qQlI6gvM8TicZyzjXtY9Vuy2cY/640?wx_fmt=png&from=appmsg "")  
  
```
<input type="search" class="form-control border-0 shadow-none bg-white rounded-0" placeholder="搜索文章、作者或内容" name="q" value="111" style="min-width:160px;">
```  
  
q的value可控但是需要闭合使用">,  
  
然后测试哪些字符没有被过滤  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ODoR0oa3ju3Rk0qgJibiaEdxN4QVkciacAkyGCqsvxiaGhZbUZ3YcJmR5iaBxyNHGJa3dw0iafnPeC9Oia7SKpOSSJXibmCxDpfNVFMQ3c4xmlkmWia0/640?wx_fmt=png&from=appmsg "")  
  
发现">被过滤导致无法插入xss（也可能是水平有限，会的大佬教教）  
  
发现不登陆没有别的输入点了因此登陆测试  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ODoR0oa3ju11O3FLCkwDCMicran7yE0J7iaBZKh2Egfs4uvIGygGMKoPiaK4l9wiaHN2hNJFtnG7pVds8U5hb9lDQt71MJ4D3iaMu3hATeAtr7HI/640?wx_fmt=png&from=appmsg "")  
  
注册的内容也会显示在界面中也需要测试，先注册一个正常的去观察正常的样式  
```
<p class="text-muted mb-0">欢迎，111</p>
```  
  
发现在p标签中，进一步测试，由于在p标签中，我想要触发xss就需要让插入的自带标签才能有可能触发xss如果我不自带标签就不可能触发xss，只会被识别为字体  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ODoR0oa3ju3J9dsqCwpzcVh8GYe9mFSNfwAR0PZhXXDpwBrQTicDO6tKbqxGjAkamkdW3xrCW2MuHtLnAQRQR3gA2AoYSvS4uhLaJfbrthdg/640?wx_fmt=png&from=appmsg "")  
  
  
由于上面测试>被拦截所以这个位置也没有成功，接下来登陆正常的进行测试，首先测试发表文章这里  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ODoR0oa3ju2vzEMcW2M2seibwlQciaAzAkQb4QH2ialBRgns4K4YRnUFtiaNH8BkYibSlz22n8lWnMvFeia6pMTcGRbUqwdqt2zVlZYuvWwIUZhKQ/640?wx_fmt=png&from=appmsg "")  
  
  
通过输入123456逐个地方测试  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ODoR0oa3ju361ZEZeG6MerJHLne9ibpgatMt1Zl1NC4yyU84XahKtHs0RicibWloUiaTnKbC7FE8ojoEylshpribcibDiaVQOgCxobluzXW3YyZ26M/640?wx_fmt=png&from=appmsg "")  
  
```
<h1 class="mb-4">111</h1><h6 class="mb-0">222</h6><p class="lead text-secondary">333</p><div class="fs-5" style="line-height: 1.9;"> 444 </div><strong>555</strong><p class="mb-0 text-secondary">666</p>
```  
  
这6个地方根据经验444的xss可能最大  
```
身份判断： 看这 style="line-height: 1.9;" 和 fs-5（字体大小），这明显是文章的正文（Body/Content）部分。为何脆弱：富文本需求： 正文通常需要支持换行、加粗、插入图片、甚至视频。这意味着开发者不能简单粗暴地把所有 < > 都转义（否则文章就乱码了）。过滤难度大： 既然允许部分 HTML 标签存在，开发者就必须写一套复杂的“黑白名单”过滤逻辑（比如“允许 <b> 但不允许 <script>”）。逻辑越复杂，漏洞就越多。XSS 向量多： 这里通常允许 <img>、<a>、<iframe> 等标签，这些都是挂载 XSS 载荷的完美宿主。
```  
  
但是经过测试，没有发现带<>的标签是302的  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ODoR0oa3ju3ibBAVnfcDZYu8KJeVDAyso3gZLfa8ahjR6CTrf3icpEic3VMeyp7YBSQ4ic50jXJicNicwOouV3dBlxeov0awLZTy8d4qiaUHiajVdzU/640?wx_fmt=png&from=appmsg "")  
  
  
于是测试发表评论的地方  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ODoR0oa3ju3U61AGPUDc2uWeIAptGA3XHIhicx8Jq6TO6kic6bRB4BFA8jtJBL0vCic4gV5icU4dBBwMQHmxssFSSs5bDHTDNlJ86FhiaveOYuibw/640?wx_fmt=png&from=appmsg "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ODoR0oa3ju1dnjmolPZloG3muGV6A7YrkLQytP2ruSyjkCUe7LzFAJq75IzeUzc1ic71S7aCzlj7fV44BX0eibRz8stGWHy4lJEaaGmXjQPgE/640?wx_fmt=png&from=appmsg "")  
  
  
发现<ifram>、<embed>  
这两个是带<>的标签所以判断是通过这两个进行xss  
```
<iframe src="data:text/html;base64, PHNjcmlwdD5hbGVydCgveHNzLyk8L3NjcmlwdD4="></iframe>
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ODoR0oa3ju2mQoIhGh1oYpiaulhiaw7QWsSGtxMGNaZnDs5Cxviam0UhzSo5PAswcZ6dbiaqicTNQAMTYOliaZaWdkDBrnFXxItF2UDEjgHJ62ykA/640?wx_fmt=png&from=appmsg "")  
  
  
然后呢我是小丑🤡xss进去了没给我弹flag我就重启了一下，忘了重启会改变xss防护规则  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ODoR0oa3ju3H3eOq7KBlRiaosM6fu11y0tQIz26RtIH0YNx23eEO1ib6Rm6ia5tztrgmOiaOlvrq6kOmkr8gjuaSzQSjWeNGJnTnz4FT4b71np4/640?wx_fmt=png&from=appmsg "")  
  
```
<button onclick=alert(1)>
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ODoR0oa3ju1hicpDr6mgdokmnDccfadticltTQzJfk68FbQWJ4x8Ijictf2ZKe1Q7HvvCkTTVukicIazOicW2r7sPJNTQ0ib6dMPZTmf55XTQgmYE/640?wx_fmt=png&from=appmsg "")  
  
  
好吧我又是小丑🤡，复盘发现单位网的防火墙拦截了我的一些流量换了网就ok了。  
  
测试的手法是一样的只是对应的位置和标签不一样一共10个规则（之前有40个的）在本篇触发了2个，大家可以多重启几次对规则进行多次测试  
  
  
  
  
