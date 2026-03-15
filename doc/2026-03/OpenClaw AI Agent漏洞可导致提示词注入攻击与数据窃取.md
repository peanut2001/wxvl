#  OpenClaw AI Agent漏洞可导致提示词注入攻击与数据窃取  
 FreeBuf   2026-03-15 10:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2rlJ12kFM9a3OQmABh76l20Z7tXpQaMEicyvnnGOTIPZf5D7L78PLnicHWHCJDibTM3gkpUlib8IlPXUxibw3Ru7aDwGXOuqFLtL5Y/640?wx_fmt=png&from=appmsg "")  
##   
## 中国国家计算机网络应急技术处理协调中心（CNCERT）近日发布安全警告，指出开源自主托管AI代理OpenClaw（前身为Clawdbot和Moltbot）存在严重安全隐患。该机构在微信公众号发文称，该平台"默认安全配置存在固有缺陷"，加之其具备执行自主任务所需的系统高权限访问能力，可能被攻击者利用以控制终端设备。  
##   
  
**Part01**  
## 间接提示词注入风险凸显  
  
  
风险主要源于提示词注入攻击——当AI代理被诱导访问含有恶意指令的网页内容时，可能导致敏感信息泄露。这类攻击也被称为间接提示词注入（IDPI）或跨域提示词注入（XPIA），攻击者并非直接与大型语言模型（LLM）交互，而是通过劫持网页摘要、内容分析等正常AI功能来执行被篡改的指令。攻击场景包括规避AI广告审核系统、影响招聘决策、实施搜索引擎优化（SEO）投毒，以及通过压制负面评价生成带有偏见的响应。  
  
  
OpenAI在本周发布的博客中指出，提示词注入攻击已从简单的外部指令植入，演变为包含社会工程学元素的复合攻击。AI代理越来越具备网页浏览、信息检索和代用户执行操作的能力，这些能力虽然实用，但也为攻击者提供了新的系统操控途径。  
  
  
**Part02**  
## 真实攻击案例曝光  
  
  
OpenClaw的提示词注入风险并非理论假设。上月PromptArmor研究人员发现，当通过间接提示词注入与OpenClaw通信时，Telegram或Discord等即时通讯应用中的链接预览功能可能沦为数据外泄通道。攻击原理是诱使AI代理生成攻击者控制的URL，当该链接在通讯应用中呈现为预览时，无需用户点击即可自动向攻击者域名传输机密数据。  
  
  
AI安全公司指出：在具备链接预览功能的代理系统中，只要AI代理对用户作出响应，数据外泄就会立即发生，无需用户点击恶意链接。在此类攻击中，代理被操控构建包含攻击者域名的URL，并附加动态生成的查询参数，这些参数包含模型所知的用户敏感数据。  
  
  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX36Msy3jj4NGibls3TP1oUibDHLbFTicF9y3FbMTlHRfPtS5aBrvyVJgBjVZhErKzlJU9Zd764e99A9E6CCfnY7apQtSTkicIUg2gE/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part03**  
## 多重安全隐患并存  
  
  
除恶意提示词外，CNCERT还警示了其他三项风险：  
- OpenClaw可能因误读用户指令而不可逆地删除关键信息  
  
- 攻击者可向ClawHub等仓库上传恶意技能模块，安装后会执行任意命令或部署恶意软件  
  
- 攻击者可利用OpenClaw最新披露的安全漏洞入侵系统并泄露敏感数据  
  
  
CNCERT表示：对金融、能源等关键行业而言，此类漏洞可能导致核心业务数据、商业秘密和代码仓库泄露，甚至造成整个业务系统完全瘫痪，带来不可估量的损失。  
  
  
**Part04**  
## 防护措施与政策响应  
  
  
为应对风险，建议用户和企业采取以下措施：加强网络控制、避免OpenClaw默认管理端口暴露在互联网、采用容器隔离服务、避免明文存储凭证、仅从可信渠道下载技能模块、禁用技能自动更新功能，以及保持代理程序最新状态。  
  
  
OpenClaw的病毒式传播也促使攻击者借机散布伪装成OpenClaw安装程序的恶意GitHub仓库，用于部署Atomic、Vidar Stealer等信息窃取程序，以及基于Golang的GhostSocks代理恶意软件（采用ClickFix式指令）。Huntress安全公司表示：该活动未针对特定行业，而是广泛攻击试图安装OpenClaw的用户，恶意仓库包含Windows和macOS环境的下载指令。攻击得逞的关键在于恶意软件托管在GitHub上，且该恶意仓库成为Bing AI搜索'OpenClaw Windows'时的置顶结果。  
  
  
**参考来源：**  
  
OpenClaw AI Agent Flaws Could Enable Prompt Injection and Data Exfiltration  
  
https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)  
  
  
### 电报讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
