#  《OWASP TOP 10-2025》发布（附下载）及漏洞赏金榜首  
原创 破天KK
                        破天KK  KK安全说   2026-02-13 08:06  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUDKx7Re03yMQsfP8UpzKZbOLXc1JQ0z6bOjj4zaF1AEXC2GoW4amor8wsVbXkkQicOM4X2EYp7USgA/640?wx_fmt=png&wx_&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=0 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUDKx7Re03yMQsfP8UpzKZbOVibIb6pPpphqCgtzZbeAhVGCWOdYiaFGpeKYNXHwNPyHSBzmnoc0rsjw/640?wx_fmt=png&wx_&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=1 "")  
  
**OWASP TOP 10-2025 中文版**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn4UQsuSPibycgVNox22LQBnDD0NdumaMoicrNPKGwwtFSl9sNEHkmkYibOymTOVNSWLjzicQXiaXITbQzA/640?wx_fmt=gif&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=2 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn4UQsuSPibycgVNox22LQBnDD0NdumaMoicrNPKGwwtFSl9sNEHkmkYibOymTOVNSWLjzicQXiaXITbQzA/640?wx_fmt=gif&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=3 "")  
  
欢迎阅读 OWASP Top 10：2025版本发布内容。  
  
OWASP Top 10是面向开发人员与Web应用安全的标准安全意识文档，代表了业界对 Web应用最关键安全风险的广泛共识。  
  
  
  
**1**  
  
**介绍**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUDKx7Re03yMQsfP8UpzKZbOE7CBe7RwoZYE2UWTqgh1MMDgZnoWxPJxTkIDYl5IDB4wwCe1AOLWRA/640?wx_fmt=png&wx_&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=4 "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mfa4R3URBqibhhpZ28NkjzMbicfQyeF4kEgd1xvllbsxjZgEeyGMQhPzdEibicl4sTUq8JemnVISSgPDTwWQaATMX375muGianWpZTmwml33FQ7Q/640?wx_fmt=png&from=appmsg "")  
  
  
  
2025 版 Top 10 中新增两个类别，并对一个类别进行了合并。我们尽可能保持对“根因”而非“症状”的关注。由于软件工程与软件安全本身的复杂性，要在仅 10 个类别中完全避免一定程度的重叠，基本是不可能的。 请扫上图二维码进行下载阅读全文。  
  
![图片](https://mmecoa.qpic.cn/sz_mmecoa_jpg/AA7xLoo4FKZsxcu7lk3IPLpK2DoE9fA8wE8icEGFWGduba5TCFBcvVcq3RyibgmJicL07qtWu5GZ43XN3WBiclrdQSBa6hyriagOvlSv4yicycJ6U/640?wx_fmt=jpeg&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=5 "")  
  
  
  
  
**01**  
  
**prompt安全**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWh5gLsXiaV56WIr34CqGET1Nb4J3ibEFKxyhFvCcKibLk9YYcVdTdibKRM83wCh3QoUeVPQtK0fRfTp5A/640?wx_fmt=gif&from=appmsg&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=6 "")  
  
  
1. A01:2025 - 访问控制失效  
  
2. A02:2025 - 安全配置错误  
  
3. A03:2025 - 软件供应链失效  
  
4. A04:2025 - 加密机制失效  
  
5. A05:2025 - 注入  
  
6. A06:2025 - 不安全的设计  
  
7. A07:2025 - 身份认证失败  
  
8. A08:2025 - 软件或数据完整性失效  
  
9. A09:2025 - 安全日志记录和告警失效  
  
10.A10:2025 - 异常情况处理不当  
  
  
  
  
**2**  
  
**团队成员**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/MPS72cibJRUDKx7Re03yMQsfP8UpzKZbOE7CBe7RwoZYE2UWTqgh1MMDgZnoWxPJxTkIDYl5IDB4wwCe1AOLWRA/640?wx_fmt=png&wx_&tp=wxpic&wxfrom=10005&wx_lazy=1#imgIndex=7 "")  
  
  
中文版项目组成员：张坤 肖文棣 王斌  
  
审核组成员：王颉  
  
由于成员知识与翻译水平有限，存在的错误敬请指正。  
  
邮箱：wangj@owasp.org.cn  
##   
##   
##   
## 核心问题：登录界面之外  
  
从简单的电商网站到复杂的企业门户，所有应用程序都依赖于强大且不可逾越的边界。**访问控制缺陷（OWASP A01）代表着这些边界的根本性失效。当应用程序能够正确识别****用户身份**  
 **（身份验证）**但严重错误地管理**用户权限**  
 （授权）时，就会出现此缺陷。****  
  
对于风险管理者而言，这是首要关注的问题。该漏洞一直被列为**“头号关键风险”**，因为它会导致最严重的后果：账户完全被盗用、大规模未经授权的数据修改以及系统范围内的信息泄露。对于安全新手来说，学习如何查找访问控制漏洞是快速提交高危漏洞报告的最佳途径。  
## 失败的三大支柱：漏洞猎人的蓝图  
  
访问控制漏洞并非随机出现，而是遵循可预测的模式。安全专家将这些故障分为三类。掌握这一模式对于系统化的漏洞赏金计划至关重要。  
  
按回车键或点击查看完整尺寸的图片  
  
## 支柱一：垂直权限提升（角色跃升）  
  
这是影响最大的缺陷：低权限用户（LPU，例如标准客户或基本用户）成功执行了高权限用户（例如管理员或经理）保留的功能或查看了资源。  
  
攻击的核心在于绕过用户界面 (UI) 的限制。攻击者会想当然地认为端点是安全的，因为它对他们来说是隐藏的。我们通过手动调用该端点来证明它是不安全的。  
  
**可执行的测试策略（如何找到它）：**  
1. 使用最低级别的测试账号登录。  
1. 使用代理工具（如 Burp Suite）拦截和分析所有流量。  
1. 在URL 、路径名或参数中查找暗示提升访问权限的关键字：admin，，，，，或。managedeletesuper_userinternalconfig  
1. 如果标准请求是无效的GET /api/v1/user/settings，请手动编辑并提交一个针对已知管理员功能的请求，例如GET /api/v1/**admin**/user_list在使用 LPU 会话 cookie 的情况下。如果服务器返回管理数据，则垂直访问控制失效。  
按回车键或点击查看完整尺寸的图片  
  
## 第二支柱：横向权限提升（用户交换：IDOR）  
  
横向权限提升是指用户访问属于**同一权限级别**其他用户的数据或功能。这种行为的通用名称是**不安全的直接对象引用（IDOR）**。  
  
问题在于服务器依赖于可预测的标识符。应用程序使用直接引用（例如数字 ID）来获取资源，但未能验证当前会话是否是该资源的授权所有者。  
  
**可操作的测试策略（如何找到它）：**每次在请求中看到一个独特的、可预测的值时——无论是在 URL、JSON 正文还是隐藏参数中——都必须更改它。  
- **目标**：寻找id=，，，或user=。accountNo=invoiceId=  
- **有效载荷：**将您的 ID（user_id=456）更改为已知目标的 ID（user_id=457）或常用占位符user_id=1（通常是第一个创建的用户）。如果服务器返回其他人的数据，则说明您已找到一个关键的 IDOR。  
按回车键或点击查看完整尺寸的图片  
  
## 第三支柱：客户端控制绕过（安全假象）  
  
这是一个非常常见的开发捷径：安全检查完全在浏览器中使用 JavaScript 实现，而不是在受信任的服务器端环境中实现。  
  
技术上的现实是，浏览器的代码可以被检查、修改，甚至完全忽略。攻击者只需绕过前端，直接向 API 端点发送请求即可。由于服务器看不到任何授权逻辑，因此会满足请求。  
  
**可执行的测试策略（如何找到它）：**  
1. 找出用户界面中对您用户角色隐藏的敏感功能（例如“删除”或“批准”按钮）。  
1. 确定隐藏按钮将要执行的底层 API 调用。  
1. 完全绕过前端，使用命令行工具或代理转发器直接发送请求。例如：  
```
```  
- 如果使用低权限 cookie 时此请求成功，则客户端上的访问控制实现不安全。  
## 技术指令：故障记录  
  
真正的安全能力不仅在于了解“访问控制失效”的概念，更在于掌握每种故障模式的细粒度分类。以下列表由行业标准的**常见弱点枚举 (CWE)**组成，展示了审核和保护应用程序所需的技术深度，证明了对该领域的精通。  
  
按回车键或点击查看完整尺寸的图片  
  
## 类别 CWE ID - 故障模式描述 I. IDOR 和缺少授权（核心缺陷）  
  
**CWE-862-缺少授权：**代码在授予访问权限之前未能执行任何检查。  
  
**CWE-863-授权错误：**检查存在但有缺陷（例如，检查您是否已登录，但未检查您是否是所有者）。  
  
**CWE-639-通过用户控制的密钥绕过授权：**使用可预测的密钥直接映射到**IDOR （不安全直接对象引用）。**  
  
**CWE-425-直接请求（“强制浏览”）：**未经预期导航路径直接访问特权 URL。**二、数据泄露和路径遍历**（信息泄露）  
  
**CWE-200-敏感信息泄露给未经授权的参与者：**许多访问控制失败的普遍后果。  
  
**CWE-548-通过目录列表泄露信息：**未能禁用 Web 服务器目录索引，导致文件路径泄露。  
  
**CWE-22-路径名限制不当（“路径遍历”）：**允许攻击者读取目标 Web 目录之外的文件（例如，/etc/passwd）。**III. 权限和配置**（架构缺陷）  
  
**CWE-732-关键资源权限分配错误：**对文件或目录设置了弱权限或过于宽泛的权限（例如，全局可写）。  
  
**CWE-276-默认权限错误：**应用程序或系统默认安装时具有不安全的访问权限（违反了“默认拒绝”规则）。  
  
**CWE-749——暴露的危险方法或功能：**将高风险或诊断功能提供给非特权用户。IV **. 会话和令牌管理不当**（Cookie/JWT 缺陷）  
  
**CWE-1275-具有不正确 SameSite 属性的敏感 Cookie：**（OWASP Top 10 问题中日益增多）由于 cookie 策略薄弱，允许 CSRF 攻击。  
  
**CWE-922-敏感信息存储不安全：**将令牌或敏感数据存储在易于访问的位置。  
  
  
## 金本位制的捍卫：一项不容谈判的指令  
  
确保访问控制安全需要开发理念的根本转变。解决方案并不复杂，但对于系统完整性而言却是必不可少的：  
1. **默认拒绝：**这必须是安全的初始状态。除非策略**明确**授予用户权限，否则应拒绝访问所有资源。切勿编写“允许所有访问，但……除外”的代码。  
1. **服务器端强制执行：**  
 **永远不要信任客户端。**所有授权和访问检查都必须在受信任的服务器端代码或 API 网关上执行，攻击者无法访问这些代码逻辑。  
  
1. **使用会话范围的间接对象引用：**不要使用可预测的 ID user_id=123，而应使用与用户会话绑定的临时随机标识符（例如安全生成的 GUID 或安全哈希）。授权检查通过后，服务器应将此令牌映射回真实的对象 ID。  
> **“人在最小的事上忠心，在大事上也忠心；人在最小的事上不义，在大事上也不义。”** ——路加福音 16:10（NASB）  
  
  
这一原则是稳健应用程序安全性的基石。如果开发人员在“很小的地方”犯了“**不公正”**  
 **（不安全**）的错误——例如缺少授权检查（CWE-862）、简单的IDOR（CWE-639）或忘记的权限（CWE-276）——那么应用程序就无法在**“大部分”（整个系统）上做到“**忠实”（安全）。  
  
  
