#  你的漏洞，都藏在那些异步加载的JS里。  
 进击的HACK   2026-02-15 16:04  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DK1uyS4fCOPiaQMV8qhI3K3iaE56jEvJ1zxZGDvqFoSzwffRLUickwgw91SyDlK74kyUnt9VyYxfm9vk5qA8KKpZQ/640 "")  
  
关于异步js文件漏洞挖掘的思考  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/wMAsN0mk9vnD1Mia4etxUC88e3XkfAHkGa2UlmPGLDcectia71Shk2bvsm01ayGBrulxgztVSzNrp5GXqucgSdkA/640 "")  
  
大家好，我是TFour，目前就职于某乙方安全公司，岗位是渗透测试工程师，兼职红队。参加过大大小小不少的攻防30+，也算小有心得。所以我想把自己想到的，思考的，经验所获得的东西写下来，于是便有了此篇。  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TEmyKDW5r0kDUxc179RyQibQia9dRvSAib0cLC8jkVjlRpy5963p3KT7Fiaibic0okNWnN1cyYUibLFfkwkfqPOnvPib3A/640 "")  
  
  
  
  
NO.1  
  
  
30+攻防报告，那些关于异步js的故事。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DWQ0PVVdRRlTBUG3etRxHZhUUlANaU7MMd3X9ts5COWkRibdk15P7cEG2vKU8MLRoTkAoL8deXX4Up4oZ5Evc2Q/640 "")  
  
我和几位师傅对几十份攻防报告，进行了分析与讨论，关注到一个点，关于js的漏洞每次攻防都占比不低。  
  
直接上截图：(如下是一些实战报告中的漏洞说明，厚码请师傅们理解。)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4T3icCFUFXyYdlE2ApTFOQAVQTbFZvaMxSOPHkLAWhT6tFDuUhLibyaeJNZj8RXW7e85Qro7WRdicn3g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4T3icCFUFXyYdlE2ApTFOQAVrOm1ia9qLQuEEx9CNMU5Pe40mic518zKPO93MD0g7Ls0p0ick8gAiaUPPg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4T3icCFUFXyYdlE2ApTFOQAV9wT8SVPDgQVCc3pOyU64iacL4ROOcA0u1Zu5TZdVhQGnH3uiaGcaO1Ew/640?wx_fmt=png&from=appmsg "")  
  
  
以上我只是找几个案例，诸如此类的案例数不胜数。那么这些js从哪里来？我们对这些漏洞站点进行了访问并分析，得出以下结论：  
  
1.访问网站主动加载的js文件  
  
2.需要从网页源码和主动加载的js文件中对异步js逻辑进行提取并进行拼接访问的js文件  
  
以上两种，从漏洞挖掘角度就可以知道第二种明显更加困难。  
  
那么我们要怎么挖掘此类漏洞？又或者我们应该先思考一个点这些js漏洞站点有没有一些共同点呢？  
  
于是我们又经过对大量漏洞报告中出现js问题站点，从指纹角度进行分析，发现确实有一个共同点，那就是它们绝大多数使用了webpack打包器，也就是下面这个东西。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjgefswoIVPvgMpd6qCemSb8aFRtqO7CbhMeM5Ywtc3T3HekAeeMvlSg/640?wx_fmt=png&from=appmsg "")  
  
  
Webpack？简单来讲它的作用就是用来打包js文件的。所以我们也就理解了为什么这些漏洞站点存在这个指纹。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjSTSjtx3sszNJRcB9oKiaWO06WWlZEg5Dgdbfduo3MnnnsCIuicpibqdhg/640?wx_fmt=png&from=appmsg "")  
  
  
通过以上的思路，我简单地写了一张逻辑图：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjcyic43IWWsv1KH8tsibu0nicEkKmmLyGUXqmaLic9O6WCr7yticjdGMPm4Q/640?wx_fmt=png&from=appmsg "")  
  
  
相信大家通过以上的四条语句，可以观察出这中间最为关键的东西，也就是这个站是否使用了webpack打包器，换句话说就是，我们又怎么知道这个站使用了webpack打包器呢？  
  
通过刚才的截图我们可以知道Wappalyzer这个插件可以帮助我们识别，但是并不适用于我们攻防场景中大批量资产的情况。  
  
通过对开源信息的检索，我们注意到几个老牌的可以检测webpack的github高星工具  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjBZR5Ss4syetK7AQDibicHXdcDTTZAqZsUJjZR84b8GKcYfydRYktJ4ibw/640?wx_fmt=png&from=appmsg "")  
  
  
Packer-Fuzzer  
```
https://github.com/rtcatc/Packer-Fuzzer
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTj4vSLngzTCMch3gibMgNqgecibBCytSEhI65SAsyAOgaXP4OGKsCkc9LA/640?wx_fmt=png&from=appmsg "")  
  
  
通过分析该工具的代码执行过程输出的信息我们可以注意到一点  
  
这里说的前端打包器就是我们所说的webpack，那么它是如何进行识别的呢？  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjd1TxtQ7KPHhKO6oeRBb3ibktjKsVphaeU6ZVMkqHqRj9pCLeXP9XJ9Q/640?wx_fmt=png&from=appmsg "")  
  
  
通过查看工具的代码，我们定位到了一个py文件上，代码是通过如下的特征列表来进行的webpack的判断。  
那我们在知道了特征之后，是不是可以把这些特征提取出来就可以实现批量的识别了。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjoaRHp3KBicCGgLnJXD4MxdncePM60UjicCR9vysBDO4ZiaJDsNuYYzkcg/640?wx_fmt=png&from=appmsg "")  
  
  
实现的思路我主要有以下两种：  
  
1.新写一个工具，来单独进行webpack指纹的识别。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjMTlcENXWVEEslDAiczcDA5vu9oxOEpCr6QlKTgGibukanWPPFLDkJAicg/640?wx_fmt=png&from=appmsg "")  
  
  
通过上述自写的工具识别的结果与  
Wappalyzer进行了对比，识别的正确率基本一致，在80%-90%之间(比较单一)。  
  
2.把指纹特征集成到现有工具(更推荐，指纹更加多样化)。  
  
我常用的指纹识别工具有两个(其他工具思路一致)：  
  
1. dddd, 在finger.yaml文件中添加了如下的指纹  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjVHO7lC30CSelS45HDbgZKaEl9BEGk5RrhjsHkTXcgMVYmFPmWtSwtw/640?wx_fmt=png&from=appmsg "")  
  
  
body="<noscript" || body="webpackJsonp" || body="<script id=\"__NEXT_DATA__" || body="webpack-" || body="<style id=\"gatsby-inlined-css" || body="<meta name=\"generator\" content=\"phoenix" || body="<meta name=\"generator\" content=\"Gatsby" || body="<meta name=\"generator\" content=\"Docusaurus" || body="__webpack_require__" || body="<div id=\"___gatsby" || body="chunk" || body="runtime" || body="app.bundle" || body="manifest"  
  
2. ehole  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjibfBlvpV6OIFROIwrYsIvSgDbkicD3VzIfQzVjYNE2j7icK5TVqtQW3jQ/640?wx_fmt=png&from=appmsg "")  
  
  
通过实战使用下来从准确度上我更推荐dddd来进行识别(单独识别指纹)，各位师傅有其他更好的工具，也欢迎补充。  
  
注：这里我们也要注意一点，就是打包器特征的多样性，  
Packer-Fuzzer作者也在项目中提到一点。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTj3QavgvjZcibu6cIrHKpOVbPhpwvmDesgpuWgOQLJw4EgeDqmnWXX3GA/640?wx_fmt=png&from=appmsg "")  
  
  
目前市面上的打包器很多，  
所以实战中的积累与思考就显得尤为重要。也期待各位大牛能写出影响安全的攻防的好工具！  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjQmS2YohaLRDhqrTiaysIpBGHUSZdPszKAFBKWfhE560gDMLkZZ7fkGg/640?wx_fmt=png&from=appmsg "")  
  
  
  
NO.2  
  
  
异步js的提取,安全工具的开发。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/wMAsN0mk9vnD1Mia4etxUC88e3XkfAHkGnb2t295OT47axZpHxMfyhlFVC7f4wibkwQ4r2CrXfI8Npnb3ibH4mzbw/640 "")  
  
在我们基本解决了指纹识别的问题之后，我们接着往下走。  
  
接下来我们将面临几个难点：  
  
主动加载的js文件我们可以通过findsomething或者hae这样的工具来实现信息、接口等的检测，那异步js呢？我们该如何做到？  
  
我们通过对大量webpack站点的异步js进行了分析，给大家看几张截图：  
  
网页源码中异步js逻辑：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjSpe89H4XxattkYssxwaElUzU2r6PZvIicl1xxciafbs7Wa4xF9LUu9HQ/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjeEibtoFgE3SmTqD5p51JjENNzy5R83dNV4p0XJGAfSq0ucbjNIQ9icYg/640?wx_fmt=png&from=appmsg "")  
  
  
主动加载的js文件中的异步js逻辑：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTj5BAicAO0U2YicwhRwv50EJJWuEmGo7gEyqSMrEMhkZSjDVZoRh1afOvg/640?wx_fmt=png&from=appmsg "")  
  
  
从这几个图就可以知道，如果我们没有去访问这些异步js的文件，可想而知我们会错过多少东西。且异步js的逻辑不存在唯一性，多变且复杂。上述代码做了什么操作，又或者我们如何能够正确地访问到这些异步的js呢？  
  
现有开源工具的解决逻辑:  
  
1.Packer-Fuzzer  
  
该工具对于异步js的提取依赖如下的两种模式：  
  
（1）动态执行 Webpack 公共路径加载逻辑  
  
不依赖多个具体的正则表达式去匹配不同的异步加载代码结构，而是通过一个通用的模式识别出加载代码块，然后在Node.js环境中执行这段代码  
来还原出真实的JS文件路径。  
  
（2）二次遍历与数字爆破  
  
这是一种补充性的、启发式的猜测方法，用于发现一些通过静态分析难以找到的JS文件  
  
Packer-Fuzzer作者的解决方法非常的巧妙，但是在使用过程中也存在几个问题(单从异步js的提取角度)。  
  
1.异步js的提取依赖于沙箱环境，性能效率不高，一些复杂场景也提取不到。  
  
2.异步js的完整路径的拼接存在一些问题。  
  
2.  
ChkApi  
```
https://github.com/0x727/ChkApi_0x727
```  
  
  
该工具对于异步js的提取依赖如下的模式：  
  
基于静态正则表达式的 Webpack 块映射表 (Chunk Map) 解析模式  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjgzr1YxUYBBgwY4ERia1MBFRic6oiaxIeIngRKBsMbxDorwyuQEZic4gYNg/640?wx_fmt=png&from=appmsg "")  
  
  
在使用过程中存在的问题  
(单从异步js的提取角度)  
：  
  
1.目前版本无法检测网页源码中的异步js。  
  
2.异步js提取逻辑过于单一，不适用于大多数网站。  
  
通过以上工具，相信各位师傅也会头疼那到底该如何解决？为了解决这一痛点，我们分析了成百上千个webpack站点，特别对异步js的逻辑进行了分析和总结。提取的思路大致可以分为如下的三种模式(还是采取正则方式，提升攻防效率优先级)：  
  
直接上结论，拒绝废话，我们以下总结的几种模式，目前通过实战适用于绝大多数站点，由于异步js的逻辑多样性和复杂性我们目前也在不断的总结更新更多的提取拼接方法：  
  
模式一：动态路径前缀 + 双映射表模式 (新版 Webpack)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjFY6AoiabePflywuVGlv0KXsTYORaSDAqJOrUGqhMKgyj5o0vvdZFTfQ/640?wx_fmt=png&from=appmsg "")  
  
  
模式二：固定路径 + 双映射表模式 (旧版 Webpack)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjuXGuUtrvBugTNS9X85mO7HW5FW2hOOfNbhpvczY2VtkUTQiaJpnXhhA/640?wx_fmt=png&from=appmsg "")  
  
  
模式三：单映射表模式 (简化结构)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTj1MfO4iaqdUXBoicUuAyWWF5uJApIzDkCC7ogWExlOaajmZHRNUFE5Wbw/640?wx_fmt=png&from=appmsg "")  
  
  
可能有些师傅对于具体的模式的拼接实现不是很明白，没关系直接用就可以了，目前上述的提取模式已集成到开发的浏览器插件中。通过大量webpack站点的测试，目前插件都能够完美的解决异步js的提取问题。  
```
https://github.com/TFour123/Webpack_Insight/releases/tag/webpack_insight(v2.x)
```  
  
  
目前插件也在不断的更新中，对于一些复杂的异步js场景，也在不断地添加对应的解决方法。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTj8H08NhNTByxFTTyeW9iaanUB12vibaH2PFG6mNl2ZLeuWvOt7WKQrrLg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjItHweULRLccgHCmribDOypcYp3BYfXMVficFiaj4fAS3Iqk3SNjsgAH7Q/640?wx_fmt=png&from=appmsg "")  
  
  
这里说一下插件的使用方法，在之前的版本中我添加了检测敏感信息的功能，又在之后的版本做了移除。我在平时的攻防中还是更加的喜欢使用Hae来实现敏感信息的检测，hae的聚合面板非常的直观且好用。我们通过插件提取到异步的js文件后，点击访问所有文件，可在bp中产生对应的流量，最终可到hae的聚合面板中查看信息检测的结果。目前该插件就只做好一件事，就是提取异步js，其他不考虑。  
  
另外，我们也对优秀的  
插件Findsomething插件进行了以上提取异步js逻辑的融合，并对异步js的路径修正做了优化，具体差别如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTj3BzB8Vzv185fYRrAh13ov8LJ7qRqSeA99PpD87qmFQVnmbPGaTSNFw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjPTwzuQEQsH5l80LwfDyt2FokvlqbbzgQK7fib4AgtdjRQA2Pc4qDTaA/640?wx_fmt=png&from=appmsg "")  
  
  
项目地址如下：  
```
https://github.com/TFour123/findsomething_plus/releases/tag/Findsomething-plus%2B%2B
```  
  
  
  
NO.3  
  
  
异步js的漏洞挖掘,安全工具的预告。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/wMAsN0mk9vnD1Mia4etxUC88e3XkfAHkGnb2t295OT47axZpHxMfyhlFVC7f4wibkwQ4r2CrXfI8Npnb3ibH4mzbw/640 "")  
  
在我们基本解决了异步js的提取访问问题之后，下一步就是针对这些js文件涉及到的具体漏洞的挖掘。  
  
1.  
Packer-InfoFinder工具  
  
工具基于  
PackerFuzzer二开，只保留提取异步js逻辑，优化了部分异步js提取逻辑，并添加了批量扫描站点、以及加入使用hae的正则进行敏感信息的匹配模块。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjMPaWMkiaXY8uUtaCIZeEbBTMe5o3zibRLlsF3lsNwAaDrO4m4IV63rQg/640?wx_fmt=png&from=appmsg "")  
  
  
敏感信息检测报告输出  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjt5dhsAN0XubWErsmHuYMrwTicu8b0QqibXD5CbBQxb1QYYW42HVW4gBA/640?wx_fmt=png&from=appmsg "")  
  
  
2.JS深度分析工具(bp插件)  
  
利用当前主流大模型，deepseek和gemini模型，利用提示词实现对js内容进行分析。对于文件过大的js内容采用分区并含有重叠块的分析思路进行ai模型的分析。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjnSkJOiczX0PJOFaxYDy4cQJlg82wyiaIUkdCJgBiawFia0ZIzcMyAVDnEQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/5lDYXKaOQ4SauCjMibuzw3YX6z94gRZTjHIfObdOwVsngB6NqgN0NWwJNYfuLpZrcsISiccDUFkJ6jOygGh8MlZg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
请各位师傅敬请期待！也希望我的这篇文章能够给你们提供一些新的角度，新的思路。  
  
  
