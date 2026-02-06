#  web渗透实战 | js.map文件泄露导致的通杀漏洞  
原创 zkaq-bielang
                    zkaq-bielang  掌控安全EDU   2026-02-06 04:03  
  
   
  
扫码领资料  
  
获网安教程  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
  
# 本文由掌控安全学院 -  bielang 投稿  
  
**来****Track安全社区投稿~**  
  
**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn）**  
  
# 一.简介  
  
**js.map**  
 文件是 JavaScript 的 **Source Map**  
 文件，用于存储压缩代码与源代码之间的映射关系。它的主要作用是帮助开发者在调试时，**将压缩后的代码还原为可读的源代码**  
，从而快速定位问题。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4Tia6S7Hx5UFb0Ws0sh9diaialtxdtGec9PCayJNadcbO6dqPe4kspSI0Ow/640?wx_fmt=png&from=appmsg "null")  
  
  
平时渗透过程中，会遇到很多的 webpack 打包的站点，webpack 加载的 js 大部分都是变量名混淆的，渗透测试者不好直接查看不同的接口和调试网页。  
# Webpack 如何导致 Vue 源码泄露？  
  
**Source Map（.map 文件）泄露原始代码**  
- • **问题**  
：  
  
Webpack 默认生成 **Source Map（.map 文件）**  
，用于调试压缩后的代码。如果 **.map**  
 文件被部署到线上，攻击者可以借助工具（如 **reverse-sourcemap**  
）还原出完整的原始代码。  
  
**示例**  
：打包后的 **app.js**  
 附带 **app.js.map**  
，攻击者可以：  
```
bashreverse-sourcemap --output-dir ./stolen_src ./dist/app.js.map
```  
  
直接还原出 **Vue 组件、API 接口、加密逻辑等**  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TdDia0ptck2IaxX752dj2tHWQUKdsIXxnUDUZARrzaLnK4tsrjKJU5ww/640?wx_fmt=png&from=appmsg "null")  
  
  
**未压缩/未混淆的代码**  
- • **问题**  
：  
  
如果 Webpack 未启用代码压缩（如 **TerserPlugin**  
）或混淆（如 **uglifyjs**  
），打包后的代码可能仍然保留 **可读的变量名、注释、甚至敏感信息**  
。  
  
**示例**  
：代码里有：  
```
jsconst API_KEY = "sk_live_123456"; // Stripe 生产环境密钥
```  
  
攻击者可以直接在 **bundle.js**  
 里搜索关键词（如 **API_KEY**  
、**password**  
、**secret**  
）找到敏感数据。  
  
**未正确设置 Webpack 的**  
 **mode: 'production'**  
- • **问题**  
：  
  
如果 Webpack 配置未指定 **mode: 'production'**  
，可能会导致：  
  
- • 未启用代码压缩优化  
  
- • 包含 **开发环境调试代码**  
（如 Vue 的 **devtools**  
 警告）  
  
- • 暴露 **未使用的代码路径**  
（如测试接口、未启用的功能）  
  
**第三方依赖泄露**  
- • **问题**  
：  
  
如果项目中使用了未正确处理的第三方库（如某些 npm 包可能包含敏感信息），它们也会被打包进 **bundle.js**  
。  
  
- • **示例**  
：  
  
某些库可能在代码里硬编码测试环境的数据库密码、内部 API 地址等。  
  
# 二.工具  
# 1. reverse-sourcemap  
  
**reverse-sourcemap**  
 是一个工具，用于从 **.map**  
 文件中逆向还原 **JavaScript**  
 或 **CSS**  
 的源码。  
### 1.1. 安装：  
1. 1. 需要先 安装 Node.js 和 npm。（我没写，自己网上找）  
  
1. 2. 使用以下命令全局安装 reverse-sourcemap：  
  
```
npm install --global reverse-sourcemap
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TTzlN9CNcMK2iaj809FYPib2MkKqicRtwdc2wfBmmJJuhrgNNMceSXuHlw/640?wx_fmt=png&from=appmsg "null")  
  
  
安装完成后，可以通过以下命令检查是否成功：  
```
reverse-sourcemap -h
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TCLK5XpPcKuIiaVPmEkwHGY5ojex1XD8XmI21ateF9liaE5Em59aS9AQA/640?wx_fmt=png&from=appmsg "null")  
  
### 1.2. 工具使用  
  
在终端中运行以下命令，将源码输出到指定目录：  
```
reverse-sourcemap --output-dir sourceCode example.js.map
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TBxef8Fw9cE1lFgWEgwm9ib5uE5hwICR24VOWiaNaPqEzh2icibjbYvQMhA/640?wx_fmt=png&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TMXGgCxVIHvKNSJBYia9jOZicR4cLbaPVLLQYD2k3Ml2GTCwXiaib2hANsg/640?wx_fmt=png&from=appmsg "")  
  
  
现在就还原出来了。  
  
如果需要递归处理多个 .map 文件，可以添加 -r 参数：  
```
reverse-sourcemap -r --output-dir sourceCode
```  
# 2. SourceDetector（插件）  
### 2.1. 简介  
  
SourceDetector是一个自动发现.map文件，并帮你下载到本地的一个chrome extension。  
### 2.2. 项目地址  
```
https://github.com/LuckyZmj/SourceDetector-dist
```  
### 2.3. 使用  
  
下载 zip 包之后然后解压，谷歌浏览器添加扩展程序（注意是添加文件中的dist文件夹）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TmBr7VFKibhmQ52SVO2ZIdTJAFibicsfYfGDC8bZhicT9LiaFibZqCuGIYljA/640?wx_fmt=png&from=appmsg "")  
  
  
之后你在浏览任何网页时，该插件将自动检测是否有.map文件。其会自动按网站分组显示源码文件，并可点击下载全部或部分源码文件。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TLlLRcWJODibiaaW3PictiaiaOdmzfbDib2wwkFNthocaoWwUe6TzT8aQK6xQ/640?wx_fmt=png&from=appmsg "")  
  
# 三.实战复现  
  
访问到一个站点，：  
```
http://oa.xxxxx.com:2345/login?redirect=%2F
```  
  
登录口，常规手法无效，无突破。  
  
发现.js.map 文件，反编译发现大量接口：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TUarApHXNo1wPaqWrKRtQtflxicS6ufSiboKDib3tZ40VIdZvFib94zLXvg/640?wx_fmt=png&from=appmsg "null")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TcHVNuUgRleE41tia97HpaKNSNsQPVvZ7QFGZHbt3upst7dOpDmUxmPA/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TouBxMiciahPLO5m7KTjS0EIicA0bX2Eicic9RODu1ribN2Ju3JvTZOs3JW5A/640?wx_fmt=png&from=appmsg "null")  
  
  
审计 js 发现好几个接口未授权，但是没什么有价值东西，还是不能突破登录口，于是提指纹找相同系统，运气很好，找到一个测试站点：  
```
http://xx.xx.xx.xx:7777/ 
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TFibXyqWoZJOIGK1bLiawbHYW4N6ukKkaB409fZmmA6SA4ROlS7sszDicQ/640?wx_fmt=png&from=appmsg "null")  
  
  
使用超管账号登录查看 bp 流量：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TYrhW7Gpa9tsTDrfibTwl2UU5nC9SqED8bOTnNZwwpdfmicoyr8nXQWlg/640?wx_fmt=png&from=appmsg "")  
  
  
发现一个接口通过 token 返回了管理员的账号和密码：  
```
/xx/xx/getInfoByToken?token=eyJxx.xx.xx
```  
  
突发奇想将当前系统的接口以及 token 信息带到不同网站去尝试：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4Taz7Q30Llc9lCYU38RHmgZDVice2IUjG5icJ5xyVvra9kRZqkSr2gXvzg/640?wx_fmt=png&from=appmsg "null")  
  
  
结果也返回了当前系统的管理员信息，解密 md5 值：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TpgBPUdzFBX65FrM7mvaLymvW1oIj5KDPibm9icmutJy71550gbNokbnw/640?wx_fmt=png&from=appmsg "null")  
  
  
成功进入系统：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TRlG8s6JtUicha9Ztb2iczjMIVrwKBqln10NIUt4VJia4urRx35iaFAKMeA/640?wx_fmt=png&from=appmsg "null")  
  
  
最后提取指纹看看资产多少：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4T5MkDthnMRcvnp0ALxibqsnjzaxSfiaQibkVtA2Mb0BpBajRYOuasrFwjQ/640?wx_fmt=png&from=appmsg "null")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrEn9SsFkvpa67vCjOaQic4TTY15dtOv2CjSLqNsEwMq5zFSewOnb03Iib5TJoSFpIA41U8JL2BawVg/640?wx_fmt=png&from=appmsg "null")  
  
  
   
  
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，  
  
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
**没看够~？欢迎关注！**  
  
  
**分享本文到朋友圈，可以凭截图找老师领取**  
  
上千**教程+工具+交流群+靶场账号**  
哦  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp "")  
  
******分享后扫码加我！**  
  
**回顾往期内容**  
  
[我与红队：一场网络安全实战的较量与成长](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247550558&idx=1&sn=589aa46a61b9ab02ab953ccb9539b1d3&scene=21#wechat_redirect)  
  
  
[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)  
  
  
[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)  
  
  
[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)  
  
  
[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)  
  
  
[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)  
  
##     代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp "")  
  
点赞+在看支持一下吧~感谢看官老爷~   
  
你的点赞是我更新的动力  
  
  
