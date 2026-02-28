#  全网首发 | 基于CORS漏洞示例验证的大模型能力Agent Skills能力从0到1全流程开发解析科普讲解，新手小白也能轻松上手  
原创 KamenRiderDarker
                    KamenRiderDarker  HexaGoners   2026-02-28 09:19  
  
最近Skill这个概念非常火啊  
  
鄙人在了解了一下之后发现，这个本质上就是一段非常灵活的渐进式披露的提示词机制，采用按需加载的思想，果然计算机行业到最后都是最优概念套娃么？（方法论）  
  
今天就给大家带来一款「基于通用型CORS漏洞扫描的Skill」的全流程解析，不仅覆盖从环境准备、前置检查到无登录态扫描的完整操作，还会同步补充Skill、MCP（模型调用协议）及大模型交互的核心知识点，以及如何去使用，还有Skill的开发思路，过程中遭遇的问题以及解决干货，希望能够帮助到还在和ai焦灼的小伙伴们，Skill格式目前只适配了Trae，其他vibe coding工具厂家未作适配，但是应该也不影响使用，我们先看一下运行效果：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMDz39fzSicDIsgH0d6Bo468yia3uahRUJXv3EXoxzkD27JjeLZ1UjJxVMnDG2qNdkwzzgycEJycdkMYf9eLEw67k8ZZNQaReibpoQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMAbRUCZZUI9qjhKUl855EtLTfianKiahPoCJvRjhecblLtmaNgPrP62ftAvsuJy4vSdU18ibsIt99ZxCvAibKM7m8cdms3lZWgiau78/640?wx_fmt=png&from=appmsg "")  
  
感觉还是可以的  
  
好了，话不多说，我们就赶快开始！  
  
先来基础知识补习，你也可以在阅读下列问题之前在自己心里过一遍：  
  
  
1、什么是prompt？  
  
prompt译为提示符，那中文说法说的顺畅一点，就是提示词了  
  
那很顾名思义了，就是一段带有指导提示的 ”指令/问题/引导语“  
- 简单理解：你想让 AI 做什么、怎么做、遵循什么规则，都通过 Prompt 告诉它。  
  
- 核心作用：定义 AI 的任务目标、约束条件、输出格式，引导 AI 生成符合预期的结果。  
  
  
那么prompt也有下列几种常见类型：  
  
**（1）基础 Prompt（无约束）：**  
  
**”写一篇关于AI Agent的短文“**  
  
**（2）结构化Prompt（带约束）：**  
  
**”任务：写一篇关于AI Agent的短文**  
  
**要求： 1. 字数控制在200字以内 2. 重点讲Skill的作用 3. 语言通俗易懂，避免专业术语 输出格式：纯文本，分段清晰“**  
  
**（3）Agent场景的Prompt：**  
  
**”你是一个智能助手，拥有以下技能：**  
  
**- web_search：根据关键词搜索网页信息，参数为keywords（必选）、top_k（可选）**  
  
**- code_generation：生成指定语言的代码，参数为language（必选）、function_name（必选）**  
  
**现在用户的问题是：“用Python写一个网页搜索的函数，要求能返回前5条结果”**  
  
**请分析：**  
  
**1. 是否需要调用技能？需要调用哪个/哪些？**  
  
**2. 调用时需要的参数是什么？**  
  
**3. 调用后如何整合结果并回答用户？“**  
  
**——————————————————————————————**  
  
**可以看到第三类提示词的描述复杂度是上升的，并且能够指导处理的问题程度也偏向复杂了，但是复杂度和描述之间是不成正比的，也就是说当你需要进行描述事情过程的复杂度到了超出大模型上下文能力时，就很难支持这种堆积如山的写法了**  
  
****  
2、  
什么是MCP？  
  
MCP全称 Model Context Protocol（模型上下文协议）  
  
你可以理解为：“AI大模型连接外部具体世界事物的统一万能接口”  
  
也就是这套协议，无论哪个厂家训练出来的具有基础功能的大模型，都可以通过这套协议并输出接近相同的操作，同时，还可以获取外部资源  
  
也就是说：MCP = 大模型和外部工具之间的 “通用翻译官 / 通用语言”：  
- 规定：怎么发请求  
  
- 规定：怎么返回结果  
  
- 规定：怎么调用功能、读数据、写文件  
  
-   
不管你是：  
- 百度文心  
  
- 阿里通义  
  
- OpenAI GPT  
  
- 字节豆包  
  
只要大家都**说 MCP 这门语言**  
，就能统一调用外面的工具。  
  
  
3、  
什么是Skill？  
  
Skill直接英译就是“技能/能力”的意思，你可以理解为：**AI 会做的 “具体本事”**  
。  
  
它是**封装好的一套做事流程**  
：比如 “查天气”，是不是应该先访问对应咨询的数据应用渠道，比如什么天气查询网站，或者手机的某个界面，然后点击进入，然后就看到了。  
  
一个完整 Skill 通常包含：  
  
（1）做什么（功能描述）  
  
（2）要什么输入（参数）  
  
（3）怎么一步步做（逻辑 / 流程）  
- （4）最终/每一步之间，返回什么结果（格式）  
  
说白了就是一本带目录的说明书  
  
  
4、  
那Skill和MCP之间的关联是什么？  
### 核心区别：一句话分清  
###   
- **MCP 管 “连接”**  
：解决 “AI 能不能连上外部工具 / 数据” 的问题。  
- **Skill 管 “做事”**  
：解决 “AI 怎么规范、高效地完成任务” 的问题。  
  
-   
#### 再举个目前就可以实现的例子：AI 帮你订机票  
####   
1. **Skill（订机票技能）：******  
查出发地 / 目的地 / 日期  
  
比价  
  
选航班  
  
生成订单  
1. **MCP（连接协议）：**  
帮 AI 连上外面的资源  
  
航空公司 API（查航班）  
  
连支付系统（付款）  
- 连你的日历（写入行程）  
  
-   
-   
**流程：**  
AI 调用「订机票 Skill」→ Skill 按流程走 → 每一步需要外部数据时，就通过 **MCP**  
 去调用对应服务 → 拿到结果后，Skill 继续处理 → 最后给你订单。  
  
—————————————我是分隔线————————————  
  
好了，在有了这些基础知识后，我们来看看如果要将Skill的思想结合到安全实践活动中，我们应该怎么做？  
  
这里我使用的是一个较为简单的漏洞——CORS啊  
  
那还是按照学术文章的惯例，我们先来复习一下这个漏洞的知识：  
  
CORS （Cross-Origin Resource Sharing）跨域资源共享，这本身是浏览器的一个机制，是一种基于 HTTP 头的，通过在返回给浏览器客户端的响应报文中，通过配置相应字段，允许服务器声明哪些外部源（协议、域名、端口组合）有权访问其资源。它解决了浏览器同源策略（Same-Origin Policy）对跨域请求的限制，使前端应用能安全地与不同源的后端 API 通信。  
  
举例子：  
  
在浏览器默认情况下，网站A不能读取网站B的数据，比如，张三正在观摩恶意不良网站，但是这时，张三电脑的浏览器内还缓存了其他网站的一些凭证信息数据，那么如果恶意不良网站的恶意js想要获取这些数据时，浏览器便会进行阻断  
  
那什么情况下，CORS漏洞会产生，还是这个场景，其他网站中的一个后台网站不小心配置了不当的CORS头字段返回到浏览器，那么此时，不良恶意网站便可以通过CORS这种跨域资源共享机制，获取到后台网站中保存的张三的一些个人凭证，以造成凭证等重要敏感信息窃取。  
  
那了解完了漏洞成因，我们还需要了解一下CORS的一些玩法和漏洞类型：  
  
CORS 请求分为两类，由浏览器自动处理：  
1. ‌**简单请求（Simple Request）**  
‌  
  
1. HTTP 方法为 GET  
、POST  
 或 HEAD  
。  
  
1. 请求头仅包含 Accept  
、Accept-Language  
、Content-Language  
、Content-Type  
（且值仅限 text/plain  
、multipart/form-data  
、application/x-www-form-urlencoded  
）。  
  
1. ‌**条件**  
‌：同时满足以下三点：  
  
1. ‌**流程**  
‌：浏览器直接发送请求，并自动添加 Origin  
 头。服务器需在响应中包含 Access-Control-Allow-Origin  
 头，浏览器才允许前端接收响应。  
  
1. ‌**预检请求（Preflight Request）**  
‌  
  
1. 使用 PUT  
、DELETE  
、PATCH  
 等方法。  
  
1. 自定义请求头（如 Authorization  
、X-Custom-Header  
）。  
  
1. Content-Type  
 为 application/json  
。  
  
1. ‌**触发条件**  
‌：请求为非简单请求，例如：  
  
1. ‌**流程**  
‌：  
  
1. 浏览器先发送一个 OPTIONS  
 请求（预检请求），包含 Access-Control-Request-Method  
 和 Access-Control-Request-Headers  
 头。  
  
1. 服务器响应预检请求，返回 Access-Control-Allow-Methods  
、Access-Control-Allow-Headers  
 等头，确认允许跨域。  
  
1. 浏览器收到允许响应后，才发送真正的请求。  
  
漏洞类型：  
  
1、完全宽松型  
  
特征：  
  
后端响应头中出现CORS配置字段，并且出现：  
  
Access-Control-Allow-Origin: *   
  
Access-Control-Allow-Credentials: true  
- *  
 表示允许**全世界任何域名**  
跨域访问  
  
- Allow-Credentials: true  
 表示允许携带 Cookie / 登录态  
  
危害性评估：高  
  
  
2、反射型Origin  
  
特征：  
  
后端会**直接把前端请求头里的 Origin 值，原样返回**  
到 Access-Control-Allow-Origin  
 里：  
- 前端发起构成的最终请求报文中： Origin: https://evil.com  
  
- 后端有CORS字段，且字段 Access-Control-Allow-Origin值为: https://evil.com  
  
危害性评估：中  
  
  
3、弱正则匹配（校验缺陷）  
  
特征：  
  
后端用**写得很烂的正则表达式**  
校验 Origin，比如：  
- 想只允许 https://xxx.com  
，但正则写的是 .*xxx.com  
  
- 黑客只需要构造 https://evilxxx.com  
，就能匹配上，被允许访问  
  
### 常见绕过方式  
- 正则漏写开头 / 结尾：xxx.com  
 → 绕过为 hackxxx.com  
、xxx.com.hack.com  
  
- 大小写绕过：Xxx.Com  
  
- 子域名滥用：hack.xxx.com  
（如果正则没限制子域名）  
  
危害评估：中  
  
  
4、宽泛根域名白名单配置  
  
和Access-Control-Allow-Origin: * 同理，只不过变成了  
Access-Control-Allow-Origin: *.com  
  
  
5、预请求配置不当  
  
特征：  
  
对于CORS 机制的预请求（OPTIONS 请求）报文，后端响应报文中返回：  
  
Access-Control-Allow-Methods: *  # 允许所有HTTP方法（GET/POST/DELETE等）Access-Control-Allow-Headers: *  # 允许所有请求头Access-Control-Max-Age: 86400    # 预检结果缓存时间过长  
### 危害评估：低  
  
  
好了，那么，关于CORS漏洞的大概知识，我们也复习了解完了，你坚持看到了这里，辛苦了，离成功还差2/3了  
  
  
—————————————我是分隔线————————————  
  
  
那么在了解完Skill和CORS的概念后，我们便可以来着手开始尝试写一下我们的Skill了  
  
我这里使用的是Trae CN版  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMBRvm3SEibXFne5CnG9FO5mWF6yhPAId4ibwJIStTVibBHIoQRUA7tricSUf8EuO73D2hefg6Nt9Y0VkfMWum84bRQZ2EMbWpic0aF4/640?wx_fmt=png&from=appmsg "")  
  
先来了解一下Trae对Skill的支持：  
  
切换到Solo模式，注意，Skill只有在Solo模式才支持Skill等一系列功能特性，没有Solo版本的小伙伴赶紧去申请吧，一般1-2天就可以申请到了  
  
  
来到右边页面右上角的齿轮，设置  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMDpXfp2UPjPsljicwqOKAsZd5nOJOqWLm4gxa6KbibCWoWwzezHokjjzzjCDBeYRGk0Uqe1N1VtBb2ukF9kR5L1rVDCxKLhaTj4I/640?wx_fmt=png&from=appmsg "")  
  
点击 “规则和技能”  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMCgGV9ibcflfvpiaicJjUBToA6IuoNVbeaEJlsJqAfkW9u0Mdt4ykFYOQ9ZN9RwvWaA6utvALJduu5vkROkREd7831ia6uw7eM69os/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMAwTxtpcz0DKtNN9WBLGrZlmvJTAtxH8ERbSeqxwDDqkibrmPmUe3P1nQHtNakXSjxpZlEywYBqOh9csYecSj6dogVt7c1iaxXls/640?wx_fmt=png&from=appmsg "")  
  
来到技能功能板块  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMBcicSFqib4l8g8bKzgYR3VS5icfVT9dGupUoeRxJiauSAnkoHneIOiaIj5DGIQldNSpYcLbSVXw8iaWUpZkGGygylTQPptlRotyBwH4/640?wx_fmt=png&from=appmsg "")  
  
首先来讲一下全局技能和项目技能的区别  
  
全局技能，意思是你使用Trae打开的任意项目都具备的初始技能，那么该功能所在的文件夹路径在：  
  
C盘/用户名/.trae-cn/skills下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMA2OwHFHzuzlY8MCfOBpULhzrOnx4useu0SyBMPVv4tiaW1ykcO4snG5DfyOsjibLzLuavMCfuJArvRvFl96juw0nbLxepas2iaRc/640?wx_fmt=png&from=appmsg "")  
  
而项目技能则在当前项目工程主文件夹的.trae-cn/skills下  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMC3uksmm5etPzek43l7cLzy67Fw5DfBnDXRLzXb4bx6iaoj3QqbSUUWYC2kGe2GcVdDcmXHK5KiaWYGibicBxQcxKXnyBx7icZKHhibk/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMA8q3qMCH94M4ZH97nhk7nrwGwibFWUpfaxwPpnFKQOQE3MO9wbRFle7yg4SYslRugDchicvs5DGxujPAAeIIWs6DeBPvBtwszRE/640?wx_fmt=png&from=appmsg "")  
  
项目技能跟随项目走，那当然你重新创建一个项目之后，便没有咯，但是你可以重新复制过来，甚至也可以复制到全局技能的文件夹路径中作为一个全局技能  
  
我们继续看如何创建技能，点击“创建”  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMC7MgMibJq6tqMy7fVBGhAnEvDDIVGNnHK2U7dBSSMkU4p8IxYB1D7icXRbW9LVicPmn8HsnPpco8kP4xsjYUwkOdw5k4qtsdvaDs/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMDAmK32ibM6zkKH1Njxf7I0Tdw1Wtrz8dvgic1LeXavYJbmC8VIicp6T1lrwdHykjLkwibLf9icbx8gNtXb5BD2hT1ibdVLyrwiajFh8E/640?wx_fmt=png&from=appmsg "")  
  
可以看到这里的界面其实支持两种创建方式，一种是直接上传技能压缩包，Trae会自动解压缩并且将技能放入对应的全局还是项目文件夹中，还有一种就是手动创建，输入技能名称，描述，和指令，例如下面的形式：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMBnZ2GVI2zf5j7UK7SZp3hObthsUbdJgG313beOpgYIh263vyCiaOvJics6nD44HyKsLsbu1t7yIx3HZP4dLJVQovo6yAibyqJ1T8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMAribKxzTziaFI7yjGN2GSiaJWseGAAX7s9kXQQ9T6GYwXxiaNVaYuIO4tyLGI6DOg6ZGLrUp60U4iaNuAgE9RpIgGdLscttr2gkl8A/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMAv1UyzplegvLFBbhmWgY2yTwoz5icaY49qicF7wibCPoypXqo3S0AuHwAvjDl7aqB8noNWVY8JprRMJrRlow8xcNAzxD9plmmX10/640?wx_fmt=png&from=appmsg "")  
  
（哈哈哈哈哈哈哈，严肃的码了半天字，让我皮一下，真的是很生动形象的解释了Skill的创建以及大致流程写法，希望小伙伴们这里不要太计较鄙人个人喜好，铠甲勇士我也非常喜欢）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMCj15eLAcYJiapjn4Kp66ibb7gyYJnVUQkeaWjyZsJpkJCOJS2ibnCYHtsDgb3LOia3cJGmJKoj4bldsyiaYabzESNcYCicygrhqkRyA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMCOaAFLbQiaUvjUe7QJibs6WEOTUw78XcnhlGGbQaCCtzGNlEJmKylXXBqorq3UJu0QZSkUPwoKRIrBljXYleViclC1jNYsXTicIia4/640?wx_fmt=png&from=appmsg "")  
  
  
那除了在设置中添加Skill，我们还有没有更简单的添加方式呢？  
  
有的，兄弟，像这样的方法我们还有两个，请看~  
  
1、通过自然语言描述并封装成技能  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMDtbKODRzcEHN7z43sX5h2WYqhZJzEh2ThBlB1ibJHMcWH0Zdx5ibvABjicpibTUzPh4h60ULptL74ACs6X7NXEKaKXcMhaZ05Ambc/640?wx_fmt=png&from=appmsg "")  
  
你可以描述一段流程，标签指明需要生成的是全局技能还是项目技能，但是这里推荐指定项目技能，翻车概率小，然后对应的大模型便会去进行一个流程化的行为：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMACvDYtepGooEBia2GOSviaMHLJVCBS04L1ibduxWq8Rmplewyib8vPztGHKzbviabcVlPia3XXg895Bxy5kDvohxG3ibbo8p2mjYSTQo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMBvBt69Snlabr7qSCib2q3ORhzbibh2DRjTVorR1FEuTEy0JwLaDNjCWJYdjC9FqjQdxDCJ7ibkiaiciaPuQdxf51dwJXiaPh8oB63q4A/640?wx_fmt=png&from=appmsg "")  
  
可以看到确实创建了项目技能，并且在正确的文件位置生成了Skill文件夹  
  
2、通过URL加自然语言描述进行技能安装  
  
以最近前端非常火热的一个技能包UI-UX-PRO-MAX为例：  
  
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMC7lGa8XMGG9VRT16oU65RDYVJg7vro0xf4yr74wMF8RNBKHovgBPWlbkUewj2faa64gJDO9EdJibvRQWWiaoBPZ8fgYfdO900ow/640?wx_fmt=png&from=appmsg "")  
  
我们复制对应github仓库的链接，然后来到对话框粘贴  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMB7LVOBOpbPGiaLIeDMLsLFbM38dIXzjr77HoteBWWskwaRw4o3kpGAV7jJq44c1ic4zkzD3m8DBcHuYN5sAP9CF3nHYUDBkTEW0/640?wx_fmt=png&from=appmsg "")  
  
那么就会在默认项目技能文件夹处出现所有的Skill技能文件，但是此处提示，UI-UX-PRO-MAX最新版通过此法安装可能会有文件缺失问题，因为人家的Skill里面出了一个类似cli脚手架的东西，需要node环境，运行适配Trae的Skill生成命令，然后再把生成好的Skill粘贴过来。  
  
好了，那我们现在已经完全了解了Trae是怎么支持Skill的，就可以开始Skill的开发了么？还是不行滴，少年，最后一步，我们需要详细深入了解Skill的编写和结构以及原理：  
  
2025年12月18日，Anthropic正式把Agent Skills 发布成了开放标准，使得Skills可以变得和MCP一样，朝着通用、跨平台规范的方向发展，以下是官网：  
  
https://agentskills.io/home  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMA0WD5TMbflCM8Z7ZGibbFJmp1aR5jia7cHelRgk5XoAYejuicvkmdeqVehpAeicOib0aQzj4NV4qorbaEJGPXW4D9SqUCEWwF3JZTA/640?wx_fmt=png&from=appmsg "")  
  
  
官方文档给出了如何去做一个Skill以及编写规范还有说明  
  
原理就简单说明一下吧：  
  
Skill这套思想把提示词拆成了三部分：matedata（元数据），Instruction（指令），Resource（资源）  
  
其中，只有元数据会必定被加载，而指令和资源都是按需加载，这样比起传统的prompt和mcp的方式，可以大大节省tokens，并且还能减少提示词的复杂耦合程度。  
  
这一块资料可以推荐大家去b站再巩固加深一下理解：  
  
【Agent Skill 从使用到原理，一次讲清】 https://www.bilibili.com/video/BV1cGigBQE6n/?share_source=copy_web&vd_source=c2dcee3ed1759c367f5e30e3f9314770  
  
那我们其实这里要知道的就是：  
  
编写一个skill，它的组成结构如下：  
  
技能名称 skill_name  
  
    元数据+指令层：SKILL.md+scripts(文件夹)  
  
    资源层（可选）：scripts（文件夹）+references(文件夹)+assets（文件夹）  
  
大概如下图所示：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMA6YdA8F8PD5d4M4rDNVuuN9uTTHQXHABCT7Bk3qzp7tlosa9caLibLSJWq4DfI7k8G2716JZ75F8gFC6MtM4Jq2TCiciaTwlQOZs/640?wx_fmt=png&from=appmsg "")  
  
可以看到：  
  
SKILL.md就是主要用来描述skill的markdown语法格式的文件  
  
scripts文件夹是存放例如main.py这种可执行脚本的文件夹  
  
referrences文件夹可以存放一些说明文档，这里可以存放一些资料充当知识库  
  
assets文件夹可以存放一些资源类型的文件，例如图片等  
  
还有data文件夹，其实这些文件夹的命名也不是很死，都可以在SKILL.md中通过相对路径描述来指定即可，不用纠结太多，但是必须注意，只有SKILL.md文件，文件名称必须要完全一样  
  
  
—————————————我是分隔线————————————  
  
  
好，那么接下来，我们就真的可以来开始实操”CORS漏洞扫描Skill“了  
  
那首先我们在项目文件夹的.trae\skills下创建一个文件夹，作为skill文件夹  
  
然后将文件夹名称改为你想要的名称，我这边就是“networksecurity-cors-vlun-scanner”了，因为我后期打算封装不同的skill，这是后话了。  
  
然后新建一个文件SKILL.md，这个文件名称是所有Skill约定俗成的，最好不要改变  
  
然后SKILL.md文件内部：  
  
这个没什么好说的，技能名称和技能描述  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMCe4cEbz1IvFpNlKhgia1IEIRykWoo993iabaqhW6F1aiaxlCYGEPqQt7KfmsI4g5TMz0DyjYGQUTOF1yhJibZR4FqFfd1fKuZ3p3A/640?wx_fmt=png&from=appmsg "")  
  
这个是详细指导，类似指导提示词，说明什么时候调用这个技能，这里像这样描述一下就行了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMBqUMuOzicV2zdI3CZKdg0IIzXGy6Oe2SDlTgVzc1RAU2Hh2sZoIzNKS9S7P1ibyQBXew1xRXPBIMFJRfwRvvbcGb5t7gDlvZoCM/640?wx_fmt=png&from=appmsg "")  
  
准备工作  
  
这里我们可以想一下，我们是作为一套指导方案来给到大模型去，对吧，那么我们传统意义上想编写这种漏洞POC脚本，大部分情况是使用python语言，那么在准备工作前，我们是不是需要检查一下是否有python环境，当然你要用别的语言，也就检查对应的运行环境就行，然后校验好python环境后，我们python脚本中是不是还有一些库，这些库一般是在requirements.txt中，所以我们还需要重复安装一下这些依赖库，当然这里你可以选择先手动安装，然后不写这一部分，我实际测试过，就算重复安装一遍也是没问题的，只是需要手动确认沙盒运行  
  
那么，这么写就行了：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMCicSGcRZWVfsU9Tkfia26Hic7q6ewQU4qTPWBIFs9r7LLnqoanjy0dEeX4oVmp9h2ibicNUQ8WUH6FSliakTrkvicRIpjzM5ltYjiaD58/640?wx_fmt=png&from=appmsg "")  
  
好了，那接下去就是：  
  
这么去使用这个技能，这里我其实算有点重复描述了，但是问题不大，和最开始的详细指导一样，我觉得这里最重要的就是  
“严格按照以下步骤执行”  
，这相当于给定一个了指导型命令  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMCuahaSc9AwdgwOWanoPPzeNQicb3Qdciby20Nz7bc0uibfzjS4DJ7YicMyySCJ6YJA1xjSY73aSkWDttibqCkJDU5UTCAdqAB61c7o/640?wx_fmt=png&from=appmsg "")  
  
然后再使用markdown中的标题段落语法表示属于子内容（[#]()  
[#]()  
[#]()  
），然后跟上“步骤1”或者“Step 1”  
  
开始按步描述我们的流程：  
  
接下去，就是比较干货的内容了  
  
STEP 1  
  
我们先来想一下第一步，应该干什么？  
  
现在正在看这篇文章的你也想一下，第一步应该干什么？  
  
既然是扫描技能，那是不是要有扫描对象，所以第一步是不是要有扫描对象，那这个扫描对象是给到大模型呢，还是扫描脚本？  
  
好，假设这里有的人会想可能是给到大模型，对吧，然后大模型再把输入的值传到脚本中去调用  
  
那这个方法可行吗？大模型可以把用户输入提示词中的某部分通过mcp传入到指定python脚本的一个方法中么？  
  
可以是可以，但是我只能说这种依赖大模型数据传参的方式非常不稳定，大家又用的基本是免费模型，对吧，能力非常有限，好的模型你需要排队，那何必呢？那我们是不是应该尽可能的避免这种不稳定的情况在数据方面，再者，如果你想要让大模型去传参，那么你必须在SKILL.md中的对应步骤中加入极其详细清楚的数据提取格式描述，增加了你自己的工作量之外，稳定性又是一个方面，当然你要是用付费api的高参数模型，可以试一下这种方法，我这里已经说的很明白了。  
  
那么怎么办呢，这个时候是不是就想起了前面说到过的，采用资源的方式，怎么做呢？  
  
哎，我能不能新建一个文件夹叫data，就用来存放一些配置文件和数据文件，然后再使用csv表格文件的方式进行存储，因为表格就是一个多维数组嘛，对吧  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMDxbUuTueZZwsJxp5MicHE6gOooY9mZOGTibORHI8vljKwy8YznD0G5TicBHE8fnSqxtI4q9NppmOA40hTy6Ha3xqW8ibd554uGXIs/640?wx_fmt=png&from=appmsg "")  
  
然后在TargetUrlInfo.csv中定义所需要的参数名作为列名  
  
我这里是考虑了url和cookie，当然这个字段可以看情况来定，这里其实只要url即可  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMB3H7WbrmvPicMZSMFDa3STJL20Nv8c3be7wia1FCN2fzDClueMmJ38M25nVMIkpLibmjic8FNmDGia2k1phSQpzibvaiciaomSlHtaibvc/640?wx_fmt=png&from=appmsg "")  
  
那现在有了存储扫描目标的数据部分，是不是还要有对应的校验机制啊，比如别人拿到你这个Skill之后，如果没有填写扫描目标直接运行，那不是就报错了嘛，然后是不是也要考虑到这种情况并且给出对应的提示，那这个部分，我认为可以由大模型来完成也可以由脚本来完成  
  
使用大模型来完成，优点是简单，缺点还是不稳定，不稳定带来的问题就是容错率非常低  
  
而使用脚本来完成，优点就是相对稳定，缺点就是需要有一套自定义版的mcp协议  
  
哎，有人说了，怎么就涉及到mcp了，如果没印象的小伙伴可以回到最开始的地方，mcp的概念，然后再看看这种脚本运行输出信息给到大模型的方式  
  
那这里，我选择  
了后者，我使用了脚本来完成，并且在这里还没有意识到需要使用mcp协议的  
概念，我踩了一个大坑  
  
那就是  
智能体会把脚本中输出中的内容再次当成语义提示的部分，例如我在python脚本中使用print函数打印出了：“请用户补充XXX文件信息”这类提示信息，本意是给到用户的，对吧，但是大模型就会理解成需要它来提示用户补充信息，而不是直接向用户输出“请用户补充XXX文件信息”，从而影响了整条链路，当时这点是非常的damm疼啊，困扰了我大概一个多小时  
  
于是我分析了一下：  
  
本质是大模型无法区分 “这是要转发的内容” 还是 “这是要执行的指令”，从而出现 “把转发内容当执行指令” 的误判。  
  
所以我只要给他一个结构化的协议格式输出，然后再明确告诉大模型 “哪些内容是要转发给用户的、哪些是内部指令、哪些是数据”。这样大模型就避免了通过语义猜测的歧义而引发错误  
  
于是，我设计了类似下列的结构化数据格式：  
  
output   
=  
{  
  
# user_prompt：需要提示用户  
,  
scan_result：检测结果  
  
"type"  
:  
"user_prompt"  
,  
  
  
# 要转发给用户的话术  
  
"content"  
:  
"请补充XXX文件信息（如assets/bypass_rules.json的完整路径）"  
,  
  
  
# 无数据时为null，对应type的值为scan_result的结果  
  
"data"  
:  
None  
,  
  
  
# 大模型内部参考语义部分（不转发）  
  
"internal_note"  
:  
"用户未提供绕过规则库文件路径，需补充后重新检测"  
  
}  
  
于是我就可以再根据脚本功能写出对应的代码了：  
```
# detectTarget.py
import csv
import json
from pathlib import Path
DATA_DIR = Path(__file__).parent.parent / "data"
csv_file = DATA_DIR / "TargetUrlInfo.csv"
def check_target_url():
    """
    检查TargetUrlInfo.csv文件是否存在且包含有效URL
    返回结构化JSON并输出到标准输出（供大模型解析）
    """
    try:
        # 1. 检查文件是否存在
        if not csv_file.exists():
            output = {
                "type": "user_prompt",       # 内容类型：需要提示用户
                "status": False,             # 检查状态
                "message": f"错误，TargetUrlInfo.csv 文件不存在（路径：{csv_file}）",  # 给用户的提示
                "internal_note": "文件缺失，需用户补充文件后重试"  # 大模型内部参考
            }
            print(json.dumps(output, ensure_ascii=False))
            print("---END-OUTPUT---")
            return output
        
        # 2. 检查文件是否有有效URL
        has_url = False
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # 先检查表头是否包含"url"列
            if "url" not in reader.fieldnames:
                output = {
                    "type": "user_prompt",
                    "status": False,
                    "message": "错误，TargetUrlInfo.csv 文件缺少'url'列，请补充正确的表头和URL信息",
                    "internal_note": "文件格式错误，缺少url列"
                }
                print(json.dumps(output, ensure_ascii=False))
                print("---END-OUTPUT---")
                return output
            
            # 遍历行检查有效URL
            for row in reader:
                if row.get('url', '').strip():
                    has_url = True
                    break
        
        # 3. 判断URL是否存在
        if not has_url:
            output = {
                "type": "user_prompt",
                "status": False,
                "message": "请先补充TargetUrlInfo.csv 文件中的url列信息（需填写有效的目标URL）",
                "internal_note": "文件存在但无有效URL，需用户补充"
            }
        else:
            output = {
                "type": "success",
                "status": True,
                "message": "TargetUrlInfo.csv 文件检查通过，包含有效URL",
                "internal_note": "可继续执行CORS漏洞扫描"
            }
        
        # 输出结构化结果
        print(json.dumps(output, ensure_ascii=False))
        print("---END-OUTPUT---")
        return output
    except Exception as e:
        # 统一异常输出格式
        output = {
            "type": "error",
            "status": False,
            "message": f"检查过程中出现异常：{str(e)}",
            "internal_note": f"异常类型：{type(e).__name__}，需排查代码或文件权限问题"
        }
        print(json.dumps(output, ensure_ascii=False))
        print("---END-OUTPUT---")
        return output
check_target_url()
```  
  
这样，我们就可以非常稳定的增加任意数量的扫描目标了，第一步到此为止达成  
  
那SKILL.md对应的，就是我们需要有数据判断，也就是STEP 1要做的事情：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMAHuT7MKgXn4mcAPED4NQzSiaBzjwkwov0t8Nhc2EReou34wBV9eIpk2mONSicdqctVv4zEOTlry2XOmNFjXnTvL27tkNIQMt6Xs/640?wx_fmt=png&from=appmsg "")  
  
STEP 2  
  
那么第二步，是不是是第一步大模型调用脚本的后续，然后进行判断，所以这里我们应该增加mcp协议的说明，也就是说除了在第一步中设计好协议的数据格式，这里也要进行相应的强制性说明，保证稳定性：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMAJRibB5J8fNk1PYCX5oSpy0hWebh0Cd4Q1jh8ELLQsXeOlbpx4hktBXEeOu4lZ5459IpTvUVACzb0ATuBreib9r1YRA42KpibE6g/640?wx_fmt=png&from=appmsg "")  
  
STEP 3  
  
第二步是告诉大模型怎么去解析第一步中脚本产生的输出，这里插播一条知识点：  
大模型本身**不能直接执行 Python 代码**  
，也无法直接获取脚本里return  
的变量 —— 它能拿到的只有脚本的 “标准输出（stdout）”“标准错误（stderr）”**，以及脚本的**  
退出码 。return  
 是 Python 程序内部的逻辑，大模型拿不到；print  
 是把内容输出到控制台（stdout），大模型能直接捕获。  
那现在是不是拿到了print后的结果数据并知道怎么去解析提取了，那是不是就要对提取的这部分开始进行判断了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMABGiaPez8iakf6Zzgr4ggiaiaGOzkn2whicKVo0c1HUlaAa1n9A5GzhxMj96c5RvR8L3ywYiatl76BE7keZnwMpGfdRJyFI7bNn51yo/640?wx_fmt=png&from=appmsg "")  
  
不知道前三步有没有让你对skill和mcp的理解更深入一点。  
  
STEP 4  
  
那接下来url扫描目标检查无误了，是不是就可以开始调用POC脚本去读取TragetUrl.scv中的url，然后进行漏洞扫描了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vMvqFvNsWMALibuJLugTJlCo6aJbIAlgbq77913eIZ2YV3k2S0WAibPkSwB9AXIvftLcAUmwEMmN9KhhkjesiaD9qAeWLtqhuXD8dZzWAicVSmk/640?wx_fmt=png&from=appmsg "")  
  
STEP5  
  
同样是对STEP 4中运行的结果的解析和提取：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMCSgQx8EbQicU7tuO3aaFPkY3nOYDCFe0EGRjeV4dkM8GnRdI4fFKFFTOnAOVJzpMeRHPYEWibqMuzJw2z8fA8X2VWyeiaXSXC7LE/640?wx_fmt=png&from=appmsg "")  
  
STEP 6  
  
步骤结束规范，照抄即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMC8ew9xmX5HMUbVDVTUJ505iaZUWiaEJgYErr1MgpM8LqaFTXzhSDB5dbquWZmicSupJGicIotMhibibiboPEvnH1Z4M4ibF2e3IwpvG00/640?wx_fmt=png&from=appmsg "")  
  
好了，到此为止，我们就已经完成了一个CORS漏洞扫描的SKILL，你能坚持看到这里，真的非常棒，我相信我已经讲解的够明确，够明白了，希望你有所收获，各位师傅们共同进步加油！！！  
  
  
这里打个广告，码字和分享知识心得属实不易，如果小伙伴你认可我这篇文章的知识贡献和文笔，可以移步加入我的知识星球：  
  
  
  
由于相关法律法规问题和业内环境，CORS漏洞的全类型POC扫描脚本这里我不提供，有需要的小伙伴可以加入我的知识星球获取完整Skill文件包，并且我会一直更新各种漏洞的Skill系列直到覆盖全安全服务范畴，以及红队和安全工作中结合AI的产品或者工具，感兴趣可以再参考上一篇信息收集全流程平台产品。（关于星球定价我叠个甲：本来我想定个18的，谐音“要发”吗，但奈何知识星球最低50起，我就想了个66 ，66大顺，希望自己和共同努力的师傅小伙伴们可以六六大顺，马年万事顺意）  
  
  
最后，非常感谢各位的阅读，如果文章有不当之处，欢迎指正，有红包激励，也欢迎私信加本人好友或者入水群探讨学术问题  
  
如果有什么漏洞Skill大家比较感兴趣，可以评论区留言，我们下期再见！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vMvqFvNsWMDyYnkK1fY06aibQvs0RKWwyaf4Se8c1Cwa2OgLvV1Wm13ARnpQ1lCPDPUpicVsUgp2yIcaNvibMpWibPrttqxiawFmwm76PLLYUrU0/640?wx_fmt=png&from=appmsg "")  
  
  
