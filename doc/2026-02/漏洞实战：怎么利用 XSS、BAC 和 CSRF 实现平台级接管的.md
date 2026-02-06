#  漏洞实战：怎么利用 XSS、BAC 和 CSRF 实现平台级接管的  
原创 Pwn1
                        Pwn1  漏洞集萃   2026-02-06 02:16  
  
   
  
> **免责声明**  
  
本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。  
  
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
1.    
  
1.    
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
在最近的一次安全审计项目中，我当时负责的目标，是某一家企业内部在用的社交内网平台。这个平台本身的定位，其实就是给现代企业用的那种数字化办公平台，用来做内部协作、知识分享，还有把一些常见的生产力工具整合到一起，整体来说，算是企业内部用得比较频繁的一类系统。  
  
那么在这次测试的整个过程中，我慢慢发现了一组比较关键、而且彼此之间是可以串联起来的安全问题。后来我意识到，如果把**访问控制缺陷（BAC）**  
、**存储型跨站脚本（Stored XSS）**  
，再加上一个**CSRF 防御绕过**  
，这三点放在一起用的话，攻击者其实是有机会直接跨越组织边界的，甚至可以一步一步做到，最终拿下任意目标企业的管理员权限，最后演变成一个平台级别的接管。  
  
接下来这篇文章，我就按照当时真实的测试顺序，来复盘一下整个漏洞链是怎么一步一步被发现，又是怎么被我串起来利用的。  
### 一、突破  
  
本次渗透测试在前期的信息收集阶段基本结束之后，我当时需要选一个功能点作为切入方向。结合对平台整体结构的了解，最后我把注意力放在了平台里的一个核心功能上，也就是所谓的“页面组（Page Groups）”。  
  
这个功能的设计初衷，其实是让用户可以创建一组页面，然后邀请其他人一起参与协作，比如给别人分配查看权限，或者编辑权限之类的。按照正常的业务逻辑来说，这里有一个非常明确的前提：**用户只能邀请自己所在组织里的成员**  
，这是一个非常基础、也非常常见的权限边界。  
  
然后，在我开始具体测试“邀请成员”这个功能的时候，我就特意去看了一下系统底层到底是怎么识别用户身份的。这个过程中我注意到一个细节：系统在处理邀请逻辑时，用的是用户的**内部 User ID**  
 来做授权判断。  
  
接着我又顺着这个点继续看了一下，结果发现这些 User ID 并不是什么随机值，而是那种非常典型的**顺序递增整数**  
，比如 1、2、3、4 这样一路往上加。  
  
说实话，当时看到这里，我脑子里第一反应就冒出来一个很直接的想法：  
  
**如果我在这里填的不是自己组织里的用户 ID，而是另一个组织的 ID，会发生什么？**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZbobKic4HXdAVWw4Av4y69MN4e9B4jBia6Ia5G1NMEYZlc9Mpayl2jwzmfw/640?wx_fmt=png&from=appmsg "")  
  
  
于是接下来我就实际动手验证了一下这个猜想。  
  
我先拦截了“添加成员”的那个请求，然后在请求参数里，把原本合法的用户 ID，手动替换成了一个随机选的、明显不属于当前组织的数字。改完之后，我就直接把这个请求发了出去。  
  
这个时候发生的事情，其实还挺出乎我意料的。系统在服务端这边，并没有去校验这个 ID 到底是不是属于当前组织，而是直接就接受了这个请求。随后，系统马上就把这个外部组织的用户，加进了我创建的页面组里，并且赋予了对应的访问权限。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZboIdibW5k5Pl8odxZeFc0fseLXbQPGKN02wBXXYCbBagAsx2lBltM4Cfg/640?wx_fmt=png&from=appmsg "")  
  
  
那么到这里，其实就已经可以非常明确地判断，这是一个典型的**越权访问问题（Broken Access Control）了。换句话说，我可以把平台上的任何用户**  
，不管他属于哪家公司、哪个组织，都强行拉进我控制的页面组里来。而这一点，也就顺理成章地，成为了后面整个攻击链里最关键的那个入口。  
### 二、存储型 XSS  
  
在确认了这个访问控制的突破口之后，然后我就继续把测试重点，转移到了页面组内部的具体功能上，尤其是**页面编辑器（Page Editor）**这一块。  
  
随后，我开始拦截并分析更新页面内容时产生的请求。在这个过程中，我基本是按照老习惯，一个参数一个参数地去看，去试，看看有没有什么过滤不到位的地方。  
  
慢慢地，我注意到了组件配置里的一个参数，名字叫做 placeholderText  
。从它的用途来看，这个参数本来应该只是用来显示一些占位提示文字的。但在测试过程中我发现，这个字段对输入内容的过滤似乎并不严格，看起来是允许直接插入 HTML 标签的。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZboV9IDHia3tSibMlKErBELVucq4DlTicNAYCic9gJBdyLyTpkr5DD2t3UD9Q/640?wx_fmt=png&from=appmsg "")  
  
  
于是我就顺手试了一下，往这个参数里塞了一个非常基础的 XSS Payload。  
  
接着我保存页面，然后刷新了一下。  
  
就在这个时候，浏览器页面上非常干脆地弹出了一个 alert  
 警告框。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZboN96Ih76yShWVVEic5R8eZ9ht0AQ9XkeJhjLFXBFLEVZibWNYHF9Xo6cw/640?wx_fmt=png&from=appmsg "")  
  
  
那么到这里，其实就已经没什么悬念了，这个点可以明确确认是一个**存储型 XSS（Stored XSS）**  
。也就是说，只要有其他用户访问了这个页面，他的浏览器就会自动执行我事先存进去的那段 JavaScript 代码。  
### 三、绕过 CSRF 防护  
  
不过话说回来，仅仅是在页面上弹一个警告框，本身其实并没有太大的实际危害。一般来说，如果想要真正做到账户接管，或者做一些高危操作，还是得想办法利用 XSS 去干点更“有用”的事情。  
  
所以接下来，我就开始专门分析平台的认证和防护机制，看看有没有可以被利用的空间。分析之后我发现，平台这边主要用了两种凭证：  
  
第一种是 **unvrsession**  
，这是一个用于身份验证的 Cookie，而且它是设置了 HttpOnly  
 标志的。也就是说，JavaScript 是没办法直接读取这个 Cookie 的。  
  
第二种是 **xsrftoken**  
，这是平台用来做 CSRF 防御的 Token。这个 Token 比较关键的一点在于，它既存在于 Cookie 里，同时也会出现在请求头中的 X-Csrf-Token  
 字段里。  
  
那么到这里，思路其实就慢慢清晰了。  
  
unvrsession  
 有 HttpOnly 保护，直接偷 Cookie 这条路基本走不通。  
  
但是 xsrftoken  
 这个东西，是**可以被 JavaScript 读到的**  
。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZboedtIUZgpj4dF7TAJPmPBNbWgE67eM9gTors408L91Q5kCAJ880vs2w/640?wx_fmt=png&from=appmsg "")  
  
  
于是我当时的想法是：  
  
既然我已经可以通过 XSS 执行任意 JavaScript 了，那么我完全可以在脚本里先把 xsrftoken  
 读出来，然后再手动构造一个合法的 HTTP 请求，把这个 Token 原封不动地塞进请求头里。这样一来，从服务器的角度看，这就是一个**完全合法的、由受害者发起的请求**  
，CSRF 防护自然也就被绕过去了。  
### 四、攻击链路的闭环：从单点突破到全面接管  
  
到了这个阶段，其实我手里已经有了三张牌，而且每一张单独看都不算特别复杂：  
1. **BAC**  
：我可以把任意用户拉进我控制的页面组。  
  
1. **XSS**  
：我可以在页面组里埋一段恶意脚本。  
  
1. **CSRF Bypass**  
：我可以利用脚本，以受害者的身份去调用敏感接口。  
  
但是如果我只是针对自己组织里的成员做这些事情，影响范围其实还是比较有限的。所以接下来，我就开始考虑，能不能把这个攻击场景，设计成一个**跨组织的利用链**  
。  
  
最终我给自己定下来的目标是：  
  
**强行把我自己，邀请成受害者组织里的管理员。**  
  
整个攻击流程，大致是按照下面这个顺序来设计的：  
1. 首先，利用 BAC 漏洞，通过遍历 User ID 的方式，把其他组织的用户，强行拉进我控制的页面组里。  
  
1. 然后，等这些用户某天登录平台的时候，他们会在页面列表里看到一个新的页面组。一般来说，出于好奇，他们大概率是会点进去看一眼的。  
  
1. 接着，在页面加载的那一刻，之前埋好的 XSS Payload 就会被触发。  
  
1. 随后，恶意脚本会在后台自动完成一整套操作流程：  
  
1. 先读取受害者的 xsrftoken  
  
1. 然后调用接口，获取受害者所在组织的 organisationId  
  
1. 再利用这些信息，向管理员邀请接口发送请求，把攻击者的邮箱添加为该组织的管理员  
  
### Payload 构造细节  
  
不过在真正实现自动化之前，我还需要解决一个实际问题。  
  
那就是：**我一开始并不知道受害者的 organisationId 是多少。**  
  
后来我在翻接口的时候，发现了 /api/apps/user  
 这个接口。这个接口看起来还是会返回当前登录用户的详细信息的，而且返回数据里，正好就包含了 organisationId  
 这个字段。  
  
基于这一点，最终我构造出来的 Payload 逻辑，大概就是下面这样（这里用伪代码简单说明一下思路）：  
```
// 1. 获取 CSRF Tokenvar token = document.cookie.match(/xsrftoken=([^;]+)/)[1];// 2. 然后去获取受害者的组织 IDfetch('/api/apps/user', {    headers: { 'X-Csrf-Token': token }}).then(response => response.json()).then(data => {    // 3. 接着发送管理员邀请请求    fetch('/api/app/organisations/' + data.organisationId + '/invites', {        method: 'POST',        headers: {            'Content-Type': 'application/json',            'X-Csrf-Token': token        },        body: JSON.stringify({            email: 'attacker@gmail.com',            asAdmin: true // 关键点：这里设置为管理员        })    });});
```  
### 五、漏洞复现与危害评估  
  
如果按照实际操作来复现的话，整个过程基本可以拆成下面这几个步骤：  
  
1、攻击者先创建一个页面组，然后在页面组件的 placeholderText  
 参数里，注入提前准备好的恶意 JavaScript 代码。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZbopiaSBbJYpmf8ClvZbvTb0CNJ54mA432AQ0WmUaBVHPibTDO6nsLeH1qg/640?wx_fmt=png&from=appmsg "")  
  
  
2、接着，编写一个脚本，利用 BAC 漏洞，把目标 User ID（比如从 1 一直跑到 200,000）对应的用户，批量添加为该页面组的编辑者。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZboIdibW5k5Pl8odxZeFc0fseLXbQPGKN02wBXXYCbBagAsx2lBltM4Cfg/640?wx_fmt=png&from=appmsg "")  
  
  
3、做完这些准备之后，就只需要等待受害者上线。一旦有受害者点进了这个页面组，攻击代码就会在后台静默执行。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZbolaN1Tfpa9vHFzqNvX5xyN9OO67IpiacJMz0FLuHHJmCtFXD5tia0VO8w/640?wx_fmt=png&from=appmsg "")  
  
  
4、最后，攻击者只需要查收邮件，接受管理员邀请，然后登录平台，进入受害者组织后台，把原有管理员移除即可。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZboH0evNu9yMSQOYoGZOXeESSuVBibfThg8jIbdzk2sL57o858H5d6Bnwg/640?wx_fmt=png&from=appmsg "")  
  
  
从整体危害来看，这已经不是单个组织的问题了。  
  
因为 User ID 是顺序递增的，攻击者可以非常轻松地通过脚本进行批量攻击，甚至都不需要提前知道任何目标用户的邮箱或者姓名。只要某个用户点进了那个页面组，他所在的整个组织，就有可能被直接接管。这种攻击方式，本质上是一种**隐蔽性和传播性都非常强的平台级攻击**  
。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLiamicUfdR0Uc9MSSWrIJZboH0evNu9yMSQOYoGZOXeESSuVBibfThg8jIbdzk2sL57o858H5d6Bnwg/640?wx_fmt=png&from=appmsg "")  
  
  
  
原文：https://medium.com/@0xs3fo/how-i-was-able-to-take-over-all-organizations-on-the-platform-via-stored-xss-chained-with-bac-and-24ea39046b0c  
  
  
   
  
觉得本文内容对您有启发或帮助？  
  
点个**关注➕**  
，获取更多深度分析与前沿资讯！  
  
  
👉 往期精选  
  
[攻防演练中的“降维打击”：逃逸出内网边界的影子资产与SaaS供应链挖掘](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484699&idx=1&sn=9455a5c988e2a477fec61e266b526aac&scene=21#wechat_redirect)  
  
  
[【实战】利用 Salesforce ID 格式特性实现用户遍历](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484848&idx=1&sn=514665a8b9e06b5f30ca1ef9584b640e&scene=21#wechat_redirect)  
  
  
[API 渗透实战：从 JSON 响应倒推隐藏的高危路由](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484828&idx=1&sn=376a99fecd6210283cc43c2a79633b26&scene=21#wechat_redirect)  
  
  
[使用 Frida 在运行时拦截 OkHttp - 实用指南](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484910&idx=1&sn=9c0e1ee6b39d754de6da5b30355a4ca0&scene=21#wechat_redirect)  
  
  
[一种利用 HTTP 重定向循环的新型 SSRF 技术](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484872&idx=1&sn=085b9ed569eefc9a96122fd164da9707&scene=21#wechat_redirect)  
  
  
  
