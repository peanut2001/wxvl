#  买“帮助台”，搭售“远程后门”？SolarWinds Web Help Desk 认证前RCE链深度分析  
 幻泉之洲   2026-03-10 04:59  
  
>   
  
## 老毛病，新补丁  
  
说到SolarWinds Web Help Desk，安全圈的朋友不感到陌生。  
  
它本质上是一个工单和资产管理系统，但最近几年在安全新闻里露脸，十有八九是因为远程代码执行漏洞。2024年的CVE-2024-28986是一个先验（pre-auth）Java反序列化RCE，CVSS评分高达9.8，在野利用让它上了CISA的已知被利用漏洞目录。  
  
但你以为这是故事的结尾？恰恰相反，2025年又冒出来两个先验反序列化漏洞，CVE-2024-28988和CVE-2025-26399。后者看起来是前一个的补丁绕过。  
  
我们的想法很简单，先复现一下CVE-2025-26399。没想到，复现过程直接引出三个新的零日漏洞：  
- CVE-2025-40552 / WT-2025-0099 - 认证绕过  
- CVE-2025-40553 / WT-2025-0100 - 通过反序列化的远程代码执行  
- CVE-2025-40554 / WT-2025-0101 - 另一个认证绕过  
最终形成的攻击链，允许攻击者在完全打过补丁的系统上，无需认证即可获取系统权限。  
## 技术债：用着20年前的老框架  
  
SolarWinds Web Help Desk运行在Java WebObjects框架上。这玩意最后一个主要版本发布是接近20年前的事了，基本处于被抛弃状态。  
  
说实话，让现在安全团队去维护和保护一个明显不是为了现代安全需求设计的废弃框架，真是件糟心的事。  
  
WebObjects这种有状态Web框架的工作方式挺特别。你看它的URL，里面总是一串用点分隔的数字，比如/helpdesk/WebObjects/Helpdesk.woa/wo/1.4.6。第一个数字是当前请求的状态计数器，后面一串数字代表了页面和组件的层级路径。  
  
你得按正确的“树”结构访问嵌套的组件，不能直接跳过去。这套机制是整个系统访问控制的基础，也成了我们寻找突破口的出发点。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeerqRpICJY8L93RKKtecdZefpRTM6fZsXAPh2VURbA0D4yelTcia2G33W7XUGaUxfpm62UJGfZu0DOLWfQvbeM6araXtUq1ia1E/640?wx_fmt=png&from=appmsg "")  
## 危险的“代理”：反序列化的起点  
  
在我们仔细浏览组件时，一个叫LookAndFeelPref的页面引起了注意。登录后可以通过“设置 - 常规 - 外观”访问它。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibd28AU2BiaGoYwu0unILnbByIOibDML6jlbTibag2E6yicf4cOE6zVTmIb7C1wzKqCHIM98xY9pgdS8pXdichvE1zk2d3yFSJNMGN5o/640?wx_fmt=png&from=appmsg "")  
  
这个页面里有个AjaxFlexibleFileUpload组件，它又关联到一个AjaxProxy组件。AjaxProxy立刻显得可疑起来，因为客户端JavaScript会直接向它发请求，而且请求路径里的层级字符串长得出奇。  
  
这个代理端点允许调用者通过method键指定要调用的服务器端方法，并通过params列表提供参数。更重要的是，它可以枚举出140多个可调用的方法。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeJibLbnjiaticQaOwg7icof7VXkwibbxjTtldy30b4PZrib9liafzjOHNsW2ibfHS2dvNuoH8ibvYMzagHFognIR2UEIibR9XRicZrE8N13s/640?wx_fmt=png&from=appmsg "")  
  
其中一个方法叫wopage.takeValueForKey，它的Java实现是这样的：  
  
public void takeValueForKey(Object value, String key) {	DefaultImplementation.takeValueForKey(this, value, key);}  
  
第一个参数的类型是Object。我们知道可以通过params JSON字段提供参数，这意味着**服务器必须把攻击者控制的输入转换成Java对象**。  
  
到这里结论就很清楚了：这些参数必须在服务端被反序列化。  
  
真正的处理发生在AjaxProxy.handleRequest和后续的JSONBridge.call里。关键在于unmarshallArgs方法，它最终路由到org.jabsorb.JSONSerializer.unmarshall。  
  
它的逻辑很简单：  
- 根据期望的参数类型和JSON中的值表示方式，选择一个反序列化器。  
- 如果期望类型是Object，而我们提供的是一个JSON对象，它就选择BeanSerializer。  
BeanSerializer会从javaClass字段读取目标类型，用默认构造函数实例化它，然后**通过setter方法填充字段**。  
  
这就是一个经典的基于setter的反序列化攻击，攻击者控制目标类型，剩下的就是找一个可用的gadget链。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfXtdwW0423DlAjp5ldBuDRficn9HYFF2rga4jW2CGvuoiaUngkszFfOvXWJ9Op06ic7NyotCbiaiaTPutuVWeVneTNbkqabib22IQmk/640?wx_fmt=png&from=appmsg "")  
### 最初的Gadget：C3P0  
  
简单翻一下应用自带的依赖，我们发现产品包含了C3P0库。这个库包含一个已知的基于setter的gadget：WrapperConnectionPoolDataSource，它允许攻击者提供一个十六进制编码的序列化payload，然后通过Java原生的readObject进行反序列化。  
  
于是最初的攻击payload长这样（已简化）：  
  
{	"id": 1, 	"method": "wopage.takeValueForKey", 	"params": [		{			"javaClass": "com.mchange.v2.c3p0.WrapperConnectionPoolDataSource", 			"userOverridesAsString": "HexAsciiSerializedMap:aced0005737...hex..."		},		"test" 	]}  
  
这就是SolarWinds WHD原始的反序列化RCE路径。它暴露了问题的根源：一个基于遗留WebObjects代码构建的应用，暴露了一个能够将攻击者控制的对象具体化并通过方法调用来操作它们的AjaxProxy组件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeW3bZiarA7mianaY4C8F2ETVsGM9I6icSMia8QU22uE1t8fOicUGfuaRZdq8ReyIQCofZzBLzyrUsubagwXyOGUaQjp64UqCu6VA54/640?wx_fmt=png&from=appmsg "")  
## 猫鼠游戏：绕过补丁检查  
  
前面提到，CVE-2025-26399是对先前漏洞的一个补丁绕过。我们开始通过比对漏洞版本和补丁版本的代码，来研究这个补丁是怎么被绕过的。  
  
补丁主要修改了com.macsdesign.util.MDSApplication.dispatchRequest。在热修复之前，请求只被checkSuspeciousPayload（注意，拼写错误不是我们加的）检查。  
  
热修复之后，新增了一个sanitizeRequest步骤，之后才交给checkSuspeciousPayload。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibc9sRJ1HzTxuFrshgXtbbWI1HnV5ictMaxhrp4wh5xnbb4FM2wUgzKdNzWibl3QlUibmdTYvUSfNg0OTGoAY15PCISMJFiansg8WUk/640?wx_fmt=png&from=appmsg "")  
  
要想复现CVE-2025-26399，就得想办法绕过checkSuspeciousPayload的保护。这个方法的逻辑如下。  
### 第一关：绕过正则检查  
  
checkSuspeciousPayload首先会对请求负载进行“规范化”和解码，然后应用几个检查：  
- 检查请求URI是否包含ajax，负载是否为JSON，且解码后的JSON字节数是否超过1048。  
- 对解码后的负载应用一系列正则表达式，查找恶意反序列化的迹象。例如，它会查找javaClass、c3p0、aced等关键词。  
我们自然会想到用编码技巧。比如，发送java\u0043lass？不行，因为负载在正则检查前就**已经被Apache Commons解码过了**。黑名单针对的是已解码的字符串。  
  
转机出现在我们发现老旧的、自定义的org.json.JSONObject解析器上。  
  
这个解析器支持一个Apache Commons**不识别**的转义序列：\xNN（十六进制转义）。于是我们可以发送java\x43lass。  
- 安全检查时，Apache Commons无法解码\x43，正则匹配失败。  
- 真正要反序列化时，JSONObject会正确解码\x43为C，拿到javaClass。  
这样，正则检查就被绕过了。  
### 第二关：绕过长度检查  
  
长度检查只有在isJSON()返回true时才会执行。isJSON()方法会用JSONObject或JSONArray尝试解析字符串。  
  
一个精妙之处在于：isJSON()操作的是已经被Apache Commons解码过一次的字符串，而JSONObject会再次解析它。  
  
于是我们可以在JSON中插入一个转义序列，让它在第一次解码后就变成语法无效的JSON。比如，加入键值对"wat":"\u0022"。  
- 第一次解码后，它变成"wat":"""，这是一个无效的字符串（双引号不匹配）。  
- JSONObject解析失败，isJSON()返回false。  
- 因为isJSON失败，长度检查（> 1048 字节）根本不会执行！  
至此，CVE-2025-26399的补丁就被绕过了。我们能再次在打过这个补丁的系统上触发RCE。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfGzYkicMutpw7t7lAkztv9Q0cCn6YufibzqgpWCQI01fFqjKbHqIqj6lVuOt0bOPFiaMdiaKOLUNiaxc8KAfqoCToPHAhSd0ahgsK8/640?wx_fmt=png&from=appmsg "")  
## 更深的洞：绕过新的“净化”补丁（CVE-2025-40553）  
  
但我们对复现CVE-2025-26399的方式其实有点不安。那些检查看起来很脆弱，一个挥之不去的念头是：我们是不是找到了补丁绕过，而不是原始的利用路径？  
  
事实证明，我们的担忧是对的。我们用来绕过CVE-2025-26399补丁的“编码技术”，同样可以用来绕过为CVE-2025-26399**本身**设计的补丁！  
  
关键就在sanitizeRequest里调用的sanitizeJson方法。它的核心逻辑很简单：  
1. 用Jackson的JsonNode解析JSON。  
1. 检查JSON是否包含params键。  
1. 如果有，就用一个空数组覆盖掉params的值。  
这招挺绝的。如果AjaxProxy的请求没有参数了，自然就反序列化不了东西。  
  
但我们可以用同样的\xNN编码把params键“藏”起来。比如写成"p\x61rams"。  
- Jackson的解析器看不懂\x61，它不会把这个字段识别为params，也就不会去修改它。  
- 但后续真正处理时，老的JSONObject会正确解码\x61为a，我们的参数又回来了！  
这让我们成功绕过了最新的防护，得到了另一个RCE漏洞，编号CVE-2025-40553。  
  
不过问题来了，这个RCE调用点（在LookAndFeelPref页面）是**需要认证**的。没有认证绕过，这个RCE的价值大打折扣。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdiaeMhYAj1H65uJBjKGn1MT75x0pl8iaxK6vI7mStrM2Lib39fXQL4mCFH78IMLOdbicRqTM5jicvD72bX971TzJc4gdic95VYkhc1Q/640?wx_fmt=png&from=appmsg "")  
## 撬开大门：认证绕过大放送  
  
于是我们需要一个认证绕过。经过一番折腾，我们发现了两个：  
- **WT-2025-0099 (CVE-2025-40552)**：一个强力的认证绕过，它能无视WebObjects的层次化执行模型，**无需认证**就直接调用几乎任何组件。这从根本上破坏了WebObjects所依赖的核心安全模型。  
- WT-2025-0101：一个稍弱但技术上也很有趣的认证绕过，它允许攻击者无需认证调用Ajax相关操作，也足以到达我们的反序列化触发点。  
这里我们重点解释第一个，它更强大也更容易说清楚。  
  
攻击者可以通过一个GET请求初始化一个新的未认证会话。WebObjects会为这个会话附上主页面（WHDMain）。在正常情况下，没有认证的情况下无法从WHDMain页面“跳转”到LookAndFeelPref这样的组件。  
  
然而，在WebObjects的请求处理器ERXComponentRequestHandler._dispatchWithPreparedSession中，如果它无法根据URL中的elementID（组件路径）找到对应的页面，会调用handlePageRestorationErrorInContext。  
  
这个方法的实现是问题的关键：  
  
public WOResponse handlePageRestorationErrorInContext(WOContext context) {  String requestedPage = (String)context.request().formValueForKey("wopage"); // 从请求体中读取wopage参数  return this.pageWithName(requestedPage, context).generateResponse(); // 用这个名称切换到对应页面}  
  
看到了吗？如果URL中的elementID是无效的，它就会从请求体中的wopage参数里读取一个页面名称，然后直接把当前会话切换到那个页面！而且没有认证检查！  
  
利用这个漏洞，我们可以通过以下两步，以未认证的状态直接绑定LookAndFeelPref页面到我们的会话：  
1. 先GET请求主端点获取会话Cookie。  
1. 然后发送另一个GET请求，URL中带一个无效的elementID（如/wo/1.2），并在请求体中包含wopage=LookAndFeelPref。  
成功之后，我们可以通过递增缓存键和提供正确的组件路径（例如0.7.1.1.1），直接构造请求访问AjaxProxy组件，触发反序列化。  
  
看起来，把认证绕过（WT-2025-0099）和我们的RCE（WT-2025-0100）结合起来就大功告成了？  
  
不，事情还没完。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibd5HxeBuu5tpRuba41C0Or1SUQDvic4VBAaTXamzniao0NPwVvCicz2vxyzc6R9Z3SHyw80TuD9iavFFezerbJibIeib2AE2orOUyiaH0/640?wx_fmt=png&from=appmsg "")  
## 补丁的小字部分：移除C3P0  
  
我们被SolarWinds“摆了一道”。在为CVE-2025-26399发布的ZIP热修复包中，他们要求**手动将c3p0库从classpath中移除**。我们之前检查补丁代码时忽略了这份文档。  
  
这意味着我们依赖的C3P0 gadget**没有了**。  
  
所以，尽管我们能无需认证到达反序列化触发点（WT-2025-0099），也能反序列化任意类（WT-2025-0100），但我们之前找到的RCE gadget蒸发了。没有能触发代码执行的gadget链，整个攻击链就断了。  
  
但我们还是报告了这个反序列化问题，原因有俩：  
- 有些管理员可能漏掉了这个手工步骤，C3P0还在。  
- 即使没有RCE gadget，基础的SSRF和DoS gadget依然存在。  
我们当然不甘心，决定再找一个新的RCE gadget。毕竟我们能反序列化带默认构造函数和setter的几乎任何类，而SolarWinds打包了海量的第三方库。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeiayHIqaI7Pd1ILX3pXW4ic3gGg37LFmiasGKLWrX8hZRXC7LicSKNsOyfsns7KbP9gic2g3iccQENIpIaxLDM2NfQwSqGLWWM6CSRw/640?wx_fmt=png&from=appmsg "")  
## 柳暗花明：转向数据库执行命令  
  
在找不到直接RCE gadget后，我们把目光投向了通过JDBC触发恶意SQL执行。我们找到了一个有趣的候选者：org.apache.commons.dbcp2.BasicDataSource。  
  
它有一个validationQuery成员，用来在数据库连接成功建立后立即执行一个SQL查询，作为连接有效性验证。我们的设想是：  
1. 用反序列化设置BasicDataSource的连接属性，连到SolarWinds自带的嵌入式PostgreSQL数据库。  
1. 在validationQuery里放一个恶意SQL语句。  
难点在于，jabsorb的反序列化流程只允许我们设置属性，但不会自动触发连接初始化。  
  
等等，有办法。还记得吗？**jabsorb在反序列化参数、调用方法后，会把方法返回的对象再序列化回来**。而BasicDataSource有个getConnection() getter，这个方法会初始化数据库连接。  
  
于是攻击场景变成了：  
1. 反序列化BasicDataSource对象，设置好连接字符串和恶意的validationQuery。  
1. 让目标方法调用这个数据源对象的某个getter（比如getConnection）。  
1. jabsorb会执行这个getter，这会触发数据库连接初始化，从而执行我们的validationQuery。  
1. 查询结果又被jabsorb序列化返回。  
但这个方案需要数据库用户名和密码才能连接。幸运的是，我们发现了两个关键信息：  
1. SolarWinds WHD**始终**会安装一个PostgreSQL13ServiceWHD服务，以SYSTEM权限运行PostgreSQL，并且默认自动启动。就算管理员配置了使用外部数据库，这个服务也还在。  
1. 我们检查了这个嵌入式PostgreSQL的pg_hba.conf配置，结果是：**信任所有本地连接**。也就是说，通过localhost连接数据库，**根本不需要密码**。默认的whd用户是数据库的超级管理员。  
这意味着我们可以用COPY ... FROM PROGRAM语句执行任意操作系统命令。  
  
至此，最后的拼图完成了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibe3jLacgSroaAY7bv6KGlYhqWbFRXLC2HbfIxwLhyyEd82picWebGibUUqicvoEl1JUXyw60IOz848BwBNwky5hDbus89uqtSHfSA/640?wx_fmt=png&from=appmsg "")  
## 完整的攻击链：无需认证的SYSTEM权限  
  
让我们把整个攻击链串起来：  
1. 获取一个未认证会话Cookie：GET /helpdesk/WebObjects/Helpdesk.woa。  
1. **认证绕过 (CVE-2025-40552)**：使用无效的elementID和wopage参数，将会话切换到LookAndFeelPref页面。  
1. 针对绑定后的页面，构造请求到AjaxProxy组件的路径。  
1. **反序列化RCE (CVE-2025-40553)**：发送精心构造的JSON载荷。利用\x编码绕过所有关键词检查、长度检查和参数净化。
    - 载荷实例化一个BasicDataSource。  
    - 通过jdbc:postgresql://127.0.0.1:20293/postgres?user=whd连接到本地信任的PostgreSQL。  
    - validationQuery里包含COPY ... FROM PROGRAM 'cmd.exe /c ...'。  
    - 利用jabsorb调用getter的机制，触发数据库连接和SQL执行。  
  
1. 载荷实例化一个BasicDataSource。  
1. 通过jdbc:postgresql://127.0.0.1:20293/postgres?user=whd连接到本地信任的PostgreSQL。  
1. validationQuery里包含COPY ... FROM PROGRAM 'cmd.exe /c ...'。  
1. 利用jabsorb调用getter的机制，触发数据库连接和SQL执行。  
1. PostgreSQL以SYSTEM权限执行操作系统命令。  
整个攻击最终被浓缩成下面这个HTTP请求，它能在我们测试的、**完全打过所有补丁**的SolarWinds Web Help Desk实例上，无需认证执行任意命令。  
  
POST /helpdesk/WebObjects/Helpdesk.woa/ajax/2.0.7.1.1.1 HTTP/1.1...{    "id": 1,     "method": "wopage.validateValueForKey",     "p\x61rams":     [        {            "java\x43lass": "org.apache.commons.dbcp2.BasicDataSource",            "driverClassName":"org.postgresql.Driver",            "url":"jdbc:postgresql://127.0.0.1:20293/postgres?user=whd",            "validationQuery":"CREATE TABLE watchTowrsvhet06r1(output text); COPY watchTowrsvhet06r1 FROM PROGRAM 'cmd.exe /c whoami > C:\\Users\\Public\\poc.txt'",        },        null    ],    "wat": "\u0022"}  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfILicGFfO14MeKx4yA6fOvVpJBzG32Gm4ebSB3B8giaImOD7UlKohJFjj5dhmeWeJC5479ApjKdZX7qpXe3nOvh5iaqQUPwRXuQc/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibd3yyOqVMBYqFrUFbuV9VM1Wnt1wz7prib9d8tUyNKcvdDvZZzKbFKj4TLVNhqpMictAwxNINFMZ18cAVTr1ia7XibOKlicYqZHXcps/640?wx_fmt=png&from=appmsg "")  
## 总结与反思  
  
从CVE-2024-28986到现在的CVE-2025-40553，SolarWinds Web Help Desk的反序列化漏洞更像是一场**补丁-绕过-再补丁-再绕过**的循环。问题的核心在于：这是一个建立在安全设计意识淡薄的**遗留框架（WebObjects）**上的应用，框架本身暴露了危险的能力（通过AjaxProxy反序列化对象），而修补只是针对单一症状的“创可贴”。  
  
这次的案例给了我们几个深刻的教训：  
1. **技术债的代价**：维护一个超过20年前的框架且未进行现代化安全重构，会持续带来根本性的安全风险。  
1. **黑名单与编码的陷阱**：单纯黑名单匹配特定的恶意字符串（如javaClass、aced），很容易被不同组件间对编码处理的微小差异所绕过。  
1. **架构级的旁路**：认证绕过漏洞（WT-2025-0099）本质上绕过了WebObjects框架的整个层次化页面导航安全模型。这表明对框架核心流程的安全假设必须严格验证。  
1. **“隐式”基础设施带来的风险**：即使管理员使用了外部数据库，SolarWinds Web Help Desk**仍然默认安装并运行一个本地、以SYSTEM权限启动且配置为“信任连接”的PostgreSQL实例**。这是攻击者绝佳的横向移动和权限提升跳板。  
对于SolarWinds来说，彻底解决这个问题可能需要付出巨大成本，比如重构或替换基于WebObjects的组件。对于企业用户而言，如果仍在运行这些版本，最好的建议是**仔细评估其暴露面（是否面向互联网？），并尽快考虑迁移或部署强化的安全边界控制**。简单的打补丁，可能无法终结这场猫鼠游戏。  
>   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdbQj21JmU0jUckb2pntqaiaTnWAuBfaxLQRmXxy9rk4YKZzKibpCmRiavibW16PsbbTpcWWpBRLfBuDfibz2FmREE89rb84jwuUvxo/640?wx_fmt=png&from=appmsg "")  
  
附：漏洞时间线和检测工具（DAG）地址（GitHub）。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeNGiaickZYLX0jqbEGZ1JQxkVakMXfibIXfJliauia7eedpvOtBmFGR3DCPLWm5GE53sUmblhIkXqCpol8kln4TaCvEV1HFewvMCuE/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdFHlz4MhW5ZF5UPZjsKG9vyKuSxgJwEVjWrl0D6KJVUJfjltmTibTAdZr9c0RFnQZuHPmSCblSz2BBBd4ic6XuzzdGTozKDDFAk/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibc2zTaYAOlqFBtav78PVeCPmeSJtBL4AuoQLjTtnw36vStJ9Rb5qVneHRmqMicao0oCy6zTeBoSJh6KKXwcFiaB61icklSBV9Diaok/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfyZgKm2ibYiclibJh595mkUde7QTiaA84hS3yX9K4PDVJfwfOJSZTubo9E9bibgte7IbfAeGxd5Y2DIs4z4CZfecBJQ3OIAFPNcicbQ/640?wx_fmt=png&from=appmsg "")  
### 参考资料  
  
[1]   
https://labs.watchtowr.com/buy-a-help-desk-bundle-a-remote-access-solution-solarwinds-web-help-desk-pre-auth-rce-chain-s/  
  
