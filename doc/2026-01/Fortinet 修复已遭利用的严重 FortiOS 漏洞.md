#  Fortinet 修复已遭利用的严重 FortiOS 漏洞  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-01-29 09:51  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**Fortinet****发布安全更新，修复了已遭在野利用的 FortiOS 严重漏洞CVE-2026-24858（CVSS评分9.4）。该漏洞是与 FortiOS 单点登录 (SSO) 相关的认证绕过漏洞，也同时影响 FortiManager 和 FortiAnalyzer。Fortinet 公司提到正在继续调查其它产品如 FortiWeb 和 FortiSwitch Manager 是否也受该漏洞影响。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
Fortinet 公司在本周二发布的一份安全公告中提到，“FortiOS、FortiManager 和 FortiAnalyzer 系统中存在一种通过替代路径或信道的认证绕过漏洞 [CWE-288]。当其它设备已启用 FortiCloud SSO 身份验证时，拥有 FortiCloud 账号和已注册设备的攻击者可能借此登录到其它账户名下的设备。”  
  
值得注意的是，FortiCloud SSO 登录功能在出厂默认设置中并未启用。只有当管理员通过设备GUI将设备注册到 FortiCare，且未关闭 ‘允许管理员使用 FortiCloud SSO 进行登录’的选项时，该功能才会被激活。  
  
几天前，Fortinet 公司证实称，身份不明的威胁人员正在滥用一个“新型攻击路径”在无需任何身份验证的情况下实现 SSO 登录。该权限被滥用于创建本地管理员账号以实现持久性，更改配置授予账号的VPN访问权限并盗取防火墙配置。  
  
上周，Fortinet 公司表示已采取如下措施：  
  
- 在2026年1月22日锁定两个恶意 FortiCloud 账号（cloud-noc@mail.com和cloud-init@mail.io）  
  
- 在2026年1月26日禁用 FortiCloud 上的 FortiCloud SSO  
  
- 在2026年1月27日重新启用 FortiCloud SSO，同时禁用从运行易受攻击版本登录的选项。  
  
  
  
换句话说，客户需要升级至最新版本才能使 FortiCloud SSO 身份验证特性正常运行。Fortinet 公司同时督促检测到妥协指标的用户应将其设备视为已遭攻陷，并建议采取如下措施：  
  
- 确保设备正在运行最新固件版本。  
  
- 用已知干净版本恢复配置或者审计任何未授权更改。  
  
- 更换凭据，包括任何可能连接到 FortiGate 设备的 LDAP/AD 账号。  
  
  
  
CISA已将该漏洞纳入KEV清单，要求联邦民事行政机构 (FCEB) 机构在2026年1月30日前修复这些漏洞。CISA 还发布更多相关指南，提到该漏洞可导致“具有 FortiCloud 账号和已注册设备的恶意人员，登录到已注册到 FortiOS、FortiManager、FortiWeb、FortiProxy和FortiAnalyzer 其它用户的独立设备，前提是启用了设备上的 FortiCloud单点登录功能”。  
  
FortiOS、FortiManager、FortiAnalyzer、FortiProxy 和 FortiWeb 的客户仍然受影响，应升级至最新版本以恢复 FortiCloud SSO 服务。  
  
Fortinet 公司仍在调查 FortiSwitch Manager 是否受该漏洞影响。该公司表示该漏洞进影响 FortiCloud SSO 且不影响第三方 SAML IdP 或 FortiAuthenticator 实现。另外，CISA督促用户“排查受该漏洞影响的所有可联网访问的 Fortinet 产品上的妥协指标，并尽快按照 Fortinet 发布的指南在更新发布后第一时间完成修复。”  
  
****  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[Fortinet：5年前的FortiOS SSL VPN 2FA绕过漏洞正遭活跃利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524747&idx=1&sn=4048d2d12b0a64ce62d92a0b79a83100&scene=21#wechat_redirect)  
  
  
[Fortinet 提醒注意严重的 FortiCloud SSO 登录认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524622&idx=1&sn=c4730e9500580e409534b376a56f70db&scene=21#wechat_redirect)  
  
  
[CISA要求政府机构在7天内修复这个 Fortinet 新0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524465&idx=1&sn=cf210939b4c44de97b60529383818aaa&scene=21#wechat_redirect)  
  
  
[Fortinet：注意这个严重的 FortiSIEM 预认证 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523808&idx=1&sn=ef2a5d044fa1a9c53dc3920c5ce650d5&scene=21#wechat_redirect)  
  
  
[Fortinet 修复FortiWeb 中的严重SQL注入漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247523530&idx=2&sn=e19607b9a1bbf6bc70c902e40f0de1d3&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://thehackernews.com/2026/01/fortinet-patches-cve-2026-24858-after.html  
  
  
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
  
