#  思科：注意已遭利用的两个 Catalyst SD-WAN 管理器 0day 漏洞  
Ravie Lakshmanan
                    Ravie Lakshmanan  代码卫士   2026-03-06 09:07  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif "")  
    
聚焦源代码安全，网罗国内外最新资讯！  
  
**编译：代码卫士**  
  
**思科披露了另外两个已遭在野利用的、位于Catalyst SD-WAN Manager（原 SD-WAN vManage）的漏洞CVE-2026-20122和CVE-2026-20128。**  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfUxPgd0CRa5YD79E3Q1r0gEboibYU8YNNrzxxaKZFMickc9WibfJVgbF0QdBiaqJ0IQL8QeNb2iadyWzq2n7RvbOqS2PjwtHRDxu52Q/640?wx_fmt=gif&from=appmsg "")  
  
**已遭活跃利用**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXsSKQ4ibopOeXhzjcavriczRlaMj7bFX55LWjbuDersrNOwTmDha6QrcoNSiaMQat8hIGZ0RwLKTXJA3tH6acO0fNboLvxKJyFsA/640?wx_fmt=gif&from=appmsg "")  
  
  
  
CVE-2026-20122（CVSS 评分：7.1）是任意文件覆盖漏洞，可导致经身份验证的远程攻击者覆盖本地文件系统上的任意文件。成功利用该漏洞需要攻击者在受影响的系统上拥有有效的、具有 API 访问权限的只读凭据。  
  
CVE-2026-20128（CVSS 评分：5.5）是一个信息泄露漏洞，可导致经身份验证的本地攻击者在受影响的系统上获取数据收集代理 (DCA) 用户权限。成功利用该漏洞需要攻击者在受影响的系统上拥有有效的 vManage 凭据。  
  
思科上月末发布了针对这两个漏洞以及 CVE-2026-20126、CVE-2026-20129 和 CVE-2026-20133 的补丁，涉及以下版本：  
  
- 早于 20.91 的版本 - 迁移到已修复版本  
  
- 版本 20.9 - 修复版本为 20.9.8.2  
  
- 版本 20.11 - 修复版本为 20.12.6.1  
  
- 版本 20.12 - 修复版本为 20.12.5.3 和 20.12.6.1  
  
- 版本 20.13 - 修复版本为 20.15.4.2  
  
- 版本 20.14 - 修复版本为 20.15.4.2  
  
- 版本 20.15 - 修复版本为 20.15.4.2  
  
- 版本 20.16 - 修复版本为 20.18.2.1  
  
- 版本 20.18 - 修复版本为 20.18.2.1  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXEvQicntaxOC6u7d4voxLxqic5TA3Mdibb4bvanPFKZNkTz6qBLGAoqVZ8GRoLBCcuKP1icYdoiaysqnQwhBGIYHt0M3PZE6T59ibt0/640?wx_fmt=gif&from=appmsg "")  
  
**应尽快修复**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfVQwUtHsaAvzpSV3eyChEzAxNwEibyalGmNCXLrTFDTymIKiaSLDzPGINtm4G3zCL6HMsI5fkqlosMHgwXusv0eQHia3nLLmu53I4/640?wx_fmt=gif&from=appmsg "")  
  
  
  
思科表示："思科 PSIRT 于 2026 年 3 月获悉，CVE-2026-20128 和 CVE-2026-20122 中描述的漏洞正遭活跃利用。"该公司没有详细说明攻击规模及其幕后黑手。  
  
鉴于漏洞正遭活跃利用，建议用户尽快更新到已修复的软件版本，并采取措施限制来自不安全网络的访问、将设备保护在防火墙之后、禁用 Catalyst SD-WAN Manager Web UI 管理员门户的 HTTP、关闭不需要的 HTTP 和 FTP 等网络服务、更改默认管理员密码，并监控进出系统的日志流量中是否有任何异常流量。  
  
一周前，思科提到 Catalyst SD-WAN 控制器和 Catalyst SD-WAN Manager 中的一个严重漏洞（CVE-2026-20127，CVSS 评分：10.0）已遭利用，用于在高价值组织机构中建立持久据点。本周，思科还发布了更新修复了 Secure Firewall Management Center 中的两个CVSS满分漏洞（CVE-2026-20079 和 CVE-2026-20131，CVSS 评分均为 10.0）。这些漏洞可导致未经身份验证的远程攻击者绕过身份验证，并在受影响的设备上以 root 权限执行任意 Java 代码。  
  
  
 开源  
卫士试用地址：  
https://oss.qianxin.com/#/login  
  
  
 代码卫士试用地址：https://sast.qianxin.com/#/login  
  
  
  
  
  
  
  
  
  
**推荐阅读**  
  
[思科修复已遭利用的 Unified CM RCE 0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524955&idx=2&sn=922edf69046bb2a552b3f58f4f21f882&scene=21#wechat_redirect)  
  
  
[思科：速修复已出现 exp 的身份服务引擎漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524828&idx=1&sn=d0696191628f6b13a09be6edecbbec4d&scene=21#wechat_redirect)  
  
  
[思科修复 Contact Center Appliance 中的多个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524343&idx=2&sn=54f09a81eb6da8e9b06f5a17b8b70644&scene=21#wechat_redirect)  
  
  
[速修复！思科ASA 两个0day漏洞已遭利用，列入 CISA KEV 清单](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524078&idx=1&sn=a668c49a8bfda90e1da60201307dc79b&scene=21#wechat_redirect)  
  
  
[思科修复影响路由器和交换机的 0day 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524071&idx=1&sn=31248d9d535baaa71b2ec67ceef617e8&scene=21#wechat_redirect)  
  
  
  
  
  
**原文链接**  
  
https://thehackernews.com/2026/03/cisco-confirms-active-exploitation-of.html  
  
  
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
  
