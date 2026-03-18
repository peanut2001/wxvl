#  Chrome Gemini AI组件曝高危漏洞，可劫持摄像头与麦克风  
原创 甲子元
                    甲子元  安全代码   2026-03-17 23:28  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/2CXZ5ByPoJbDDS7UPQZBHRwiafAVwzmgEIibFC57lhUL1e1ibPpgfiatKxDpyJWVU7dicgMF5evK18fZuXp5qgsxvrg/640?wx_fmt=gif&from=appmsg "")  
  
近日，谷歌浏览器Gemini Live集成组件中被发现一处高危漏洞，编号CVE-2026-0628。该漏洞可被恶意浏览器扩展利用，劫持Gemini侧边栏，实现对用户摄像头、麦克风及本地文件的未授权访问，将用户隐私置于严重风险之下。  
  
**漏洞根源：侧边栏与标签页安全机制不一致**  
  
据Palo Alto Networks Unit 42研究人员披露，该漏洞的核心问题在于Chrome在侧边栏中加载Gemini Web应用时，采用了与普通标签页不同的安全处理机制。为支持AI任务的复杂功能，Gemini面板被赋予更高权限，包括读取本地文件、访问摄像头与麦克风等。  
  
攻击者通过declarativeNetRequests  
 API拦截并修改HTTPS请求，在Gemini面板中注入恶意JavaScript代码，从而劫持应用并窃取这些高权限。研究人员强调，在普通标签页中注入代码并不会获得特殊权限，但在面板中注入则极为危险。  
  
**潜在后果：摄像头开启、文件读取、屏幕截取**  
  
成功利用该漏洞后，攻击者可在Gemini面板的高权限环境内执行任意代码，可能导致：  
- 未经用户同意开启摄像头与麦克风；  
  
- 访问操作系统中的本地文件与目录；  
  
- 对任意HTTPS网站截取屏幕；  
  
- 借助可被信任的Gemini面板界面实施高隐蔽钓鱼攻击。  
  
上述行为仅需极低用户交互，用户只需打开Gemini面板即可能被利用。  
  
**修复进展：谷歌已发布补丁**  
  
Unit 42于2025年10月向谷歌合规上报该漏洞，官方已在2026年1月初发布修复补丁。此事件凸显了AI与浏览器深度集成带来的全新安全挑战，随着智能代理浏览器功能日益普及，持续的安全监控与权限隔离机制至关重要。  
  
来源：安全客  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/2CXZ5ByPoJaCZo3iaHicUlpfsHplbY8pNptagz6URJ0c7y9okfK3SGguRFJ8E7PJtsLC9pUmoPbgRICzxzWjb3GA/640?wx_fmt=gif&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/GCSG9VLghhrNph1icHNJs6Luesa5vygQIL2E0bJFicfjicjZfcTdjEeQ3bxYAOd1yP3X4NauDHZQLLB8nrSggJ6aQ/640?wx_fmt=png "")  
  
**山西甲子元科技有限公司**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/w3Y1fbBttohia5eUkE5R0S8E5oOTOePy2ayE0lmzsUmWtZkLd7c1M40ujxAvia4mFYrDU4Bdzk7siawjRLvcDagJw/640?wx_fmt=jpeg "undefined")  
  
产品介绍：  
  
  
  
软件：防泄密、行为管理、行为审计、云文档安全管理、数据智能备份等安全管理系统。  
  
电话：0351-3366668  
  
  
