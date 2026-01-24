#  CISA更新KEV目录，新增四个正在被积极利用的软件漏洞  
原创 ZM
                    ZM  暗镜   2026-01-24 08:45  
  
美国网络安全和基础设施安全局 (CISA) 周四在其已知被利用漏洞 ( KEV ) 目录中添加了四个安全漏洞，并指出有证据表明这些漏洞正在被积极利用。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt89zcsSpzdKiaE0aj0Es7lWSS1K28mtowObGiasQZ8bt3uTFGEd6ugeVhxOQKHdnKA7730lUhgxWaHw/640?wx_fmt=png&from=appmsg "")  
  
  
漏洞列表如下：  
- **CVE-2025-68645**（CVSS 评分：8.8）- Synacor Zimbra Collaboration Suite (ZCS) 中的一个PHP 远程文件包含漏洞，远程攻击者可能通过构造对“/h/rest”端点的请求，在无需任何身份验证的情况下，从 WebRoot 目录中包含任意文件（已于 2025 年 11 月在10.1.13 版本中修复）。  
- **CVE-2025-34026**（CVSS 评分：9.2）- Versa Concerto SD-WAN 编排平台中存在身份验证绕过漏洞，攻击者可能利用该漏洞访问管理端点（已于 2025 年 4 月在12.2.1 GA 版本中修复）。  
- **CVE-2025-31125**（CVSS 评分：5.3）- Vite Vitejs 中存在访问控制不当漏洞，可能允许使用 ?inline&import 或 ?raw?import 将任意文件的内容返回给浏览器（已于 2025 年 3 月在6.2.4、6.1.3、6.0.13、5.4.16 和 4.5.11 版本中修复）。  
- **CVE-2025-54313**（CVSS 评分：7.5）- eslint-config-prettier 中存在嵌入式恶意代码漏洞，可能允许执行名为 Scavenger Loader 的恶意 DLL，该 DLL 旨在传播信息窃取程序。  
值得注意的是，CVE-2025-54313 指的是针对 eslint-config-prettier 和其他六个 npm 包（eslint-plugin-prettier、synckit、@pkgr/core、napi-postinstall、got-fetch 和 is）的供应链攻击，该攻击于 2025 年 7 月曝光。  
  
网络钓鱼活动以验证电子邮件地址（作为常规帐户维护的一部分）为幌子，通过虚假链接窃取软件包维护者的凭据，从而使威胁行为者能够发布木马版本。  
  
据CrowdSec称，针对 CVE-2025-68645 的攻击活动自 2026 年 1 月 14 日以来一直在进行。目前尚无其他漏洞在实际环境中被利用的详细信息。  
  
根据具有约束力的操作指令 (BOD) 22-01，联邦民事行政部门 (FCEB) 各机构必须在 2026 年 2 月 12 日之前采取必要的补救措施，以保护其网络免受活跃威胁。  
  
  
