#  CISA：四款企业软件中的漏洞已遭利用  
Bill Toulas
                    Bill Toulas  代码卫士   2026-01-26 10:08  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**美国网络安全与基础设施安全局（CISA）警告称，Versa和Zimbra开发的企业软件、Vite前端工具框架以及Prettier代码格式化工具中的四个漏洞正遭受活跃攻击。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
这些安全问题已被列入CISA的已知可利用漏洞（KEV）目录，表明该机构已掌握黑客在现实攻击中利用这些漏洞的证据。其中一个漏洞为CVE-2025-31125，是去年3月披露的一个高危严重性访问控制不当漏洞。当服务器被明确暴露于网络时，攻击者可利用该漏洞窃取未授权访问的文件。该漏洞仅影响已暴露的开发环境实例，并已在6.2.4、6.1.3、6.0.13、5.4.16及4.5.11版本中修复。  
  
另一漏洞是CVE-2025-34026，于2025年5月披露，是位于Versa Concerto SD-WAN编排平台中严重的身份验证绕过漏洞。该漏洞由Traefik反向代理配置不当引起，可导致攻击者访问包括内部Actuator端点在内的管理接口，从而泄露堆转储和跟踪日志数据。受影响的产品包括 Concerto 12.1.2 至 12.2.0 版本，其它版本也可能受到影响。网络安全公司 ProjectDiscovery 的研究人员于 2025 年 2 月 13 日向供应商报告了这些问题，Versa Concerto 向 BleepingComputer 确认已在 2025 年 3 月 7 日修复。  
  
第三个已遭利用漏洞是 CVE-2025-54313，它是一个由于供应链受攻击导致的高危漏洞，影响了用于解决代码检查工具 ESLint 与 Prettier 代码格式化工具之间冲突的 eslint-config-prettier 包。去年 7 月，黑客劫持了多个流行的 JavaScript 库，其中包括 "eslint-config-prettier"，并在 npm 上发布了嵌入恶意代码的版本。安装受影响的软件包（版本8.10.1、9.1.1、10.1.6和10.1.7）会运行恶意的install.js脚本，该脚本将在Windows系统上加载node-gyp.dll恶意载荷以窃取npm身份验证令牌。  
  
第四个已遭利用的漏洞是CVE-2025-68645，于2025年12月22日披露，是位于Zimbra Collaboration Suite 10.0和10.1版本中Webmail Classic UI的本地文件包含漏洞。该漏洞源于RestFilter servlet对用户提供参数的处理不当。未经身份验证的攻击者可以利用/h/rest端点包含WebRoot目录中的任意文件。  
  
CISA现要求所有受BOD 22-01指令约束的联邦机构必须在2026年2月12日前应用可用的安全更新或供应商建议的缓解措施，或停止使用相关产品。该机构尚未分享任何关于漏洞利用活动的具体细节，且这些漏洞在勒索软件攻击中的利用状态被标记为“未知”。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[CISA KEV 清单共收录1048个已遭利用漏洞，2025年增长20%](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524804&idx=1&sn=1381c6e257d31d7dbe89101f6123fd8b&scene=21#wechat_redirect)  
  
  
[CISA提醒注意 WHILL Model C2 电动轮椅中的严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524792&idx=2&sn=b115387a5980ae618431dc31a198d636&scene=21#wechat_redirect)  
  
  
[CISA 将已遭利用的 Digiever NVR RCE漏洞纳入KEV](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524761&idx=2&sn=1b94ad55c3aaf6d0f95f5c0d1386a2e4&scene=21#wechat_redirect)  
  
  
[React2Shell：30家机构已受陷77k IP地址易受影响，被列入 CISA KEV](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524607&idx=2&sn=73748657190a71ffd47cbbeb32fe077e&scene=21#wechat_redirect)  
  
  
[CISA 将 OpenPLC ScadaBR 纳入必修清单](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524567&idx=2&sn=51761f3ab07806bb1af7abb9723370e1&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://www.bleepingcomputer.com/news/security/cisa-confirms-active-exploitation-of-four-enterprise-software-bugs/  
  
  
题图：Pixa  
bay Licens  
e  
  
  
**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg "")  
  
**奇安信代码卫士 (codesafe)**  
  
国内首个专注于软件开发安全的产品线。  
  
   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif "")  
  
   
觉得不错，就点个 “  
在看  
” 或 "  
赞  
” 吧~  
  
