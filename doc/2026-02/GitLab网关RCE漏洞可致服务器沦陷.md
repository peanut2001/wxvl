#  GitLab网关RCE漏洞可致服务器沦陷  
 FreeBuf   2026-02-10 10:04  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0lprwLheiaic6ibmcxLEZlSACplgQNibKEOH6w3LPfg3CUsUvvreDUpKzOMVKYsicHMGuibia5yN68AuUZn3Rcwf46Ria0M83gJTKcNuE/640?wx_fmt=png&from=appmsg "")  
  
  
GitLab向运行自托管版AI Gateway的组织发布紧急安全警报，警告存在一个高危漏洞可能允许攻击者使服务崩溃或执行任意代码。该漏洞编号为CVE-2026-1868，CVSS评分高达9.9（接近满分），表明未打补丁的实例面临迫在眉睫的危险。  
  
  
**Part01**  
## 漏洞影响核心工作流组件  
  
  
该漏洞存在于Duo Workflow Service核心组件中，该组件原本用于通过AI简化开发任务。但由于系统处理用户模板时存在疏漏，使得这个生产力工具成为黑客的潜在入口。  
  
  
**Part02**  
## 漏洞技术细节  
  
  
漏洞被描述为"GitLab AI Gateway存在不安全模板扩展问题"。本质上，系统在处理用户提供的"特制Duo Agent Platform Flow定义"时未能正确清理数据。  
  
  
虽然攻击者需要"获得GitLab实例的认证访问权限"，但潜在影响极为严重。成功利用该漏洞可使攻击者触发"拒绝服务"使网关下线，更严重的是能"在网关上获得代码执行权限"。  
  
  
这意味着已登录用户（可能是被入侵的开发者账户或恶意内部人员）理论上可以突破应用程序限制，在底层服务器上执行命令。  
  
  
**Part03**  
## 漏洞发现与影响范围  
  
  
该漏洞并非由外部研究人员发现，而是由GitLab团队成员Joern内部发现。漏洞影响特定版本范围内的自托管AI Gateway，运行早于修复版本的GitLab AI Gateway 18.1.6、18.2.6和18.3.1版本的系统均受影响。  
  
  
**Part04**  
## 修复方案  
  
  
GitLab已发布三个修复版本覆盖不同发布分支，强烈建议管理员立即升级至：  
  
- 18.6.2  
  
- 18.7.1  
  
- 18.8.1  
  
安全公告强调："我们强烈建议所有使用GitLab Duo自托管安装的客户立即更新至上述版本之一。"  
  
  
**参考来源：**  
  
CVE-2026-1868: Critical GitLab Gateway Flaw (CVSS 9.9) Allows RCE  
  
https://securityonline.info/cve-2026-1868-critical-gitlab-gateway-flaw-cvss-9-9-allows-rce/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
