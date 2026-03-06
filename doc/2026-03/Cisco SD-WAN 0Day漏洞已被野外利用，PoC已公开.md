#  Cisco SD-WAN 0Day漏洞已被野外利用，PoC已公开  
 FreeBuf   2026-03-06 10:07  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1jtZXgPBcibnpmf1icnicFNBMmNtGPtpMp3NAVuiabbIcPdEnLF8Ktiad9cibibUQaDKsZBFrl0RiaNb2IiaZCROhOufictTQEedvycxMR0/640?wx_fmt=jpeg&from=appmsg "")  
##   
  
针对Cisco Catalyst SD-WAN控制器和SD-WAN管理器中的最高危0Day漏洞（CVE-2026-20127），研究人员已公开概念验证（PoC）漏洞利用代码。该漏洞自2023年起就已被攻击者野外利用。  
  
  
Cisco Talos将该威胁活动追踪为UAT-8616集群，称其为针对全球关键基础设施的"高度复杂网络威胁行为体"。zerozenxlabs在GitHub发布的PoC包含可运行的Python漏洞利用脚本和JSP webshell（cmd.jsp），同时还提供了可部署的WAR文件，降低了其他攻击者利用这一关键漏洞的门槛。  
##   
  
**Part01**  
## 攻击原理分析  
  
  
该漏洞源于受影响Cisco SD-WAN系统中的对等认证机制存在缺陷。未经身份验证的远程攻击者可向SD-WAN控制器的REST API发送特制HTTP请求，完全绕过登录流程，无需有效凭证即可获取管理员会话。  
  
  
UAT-8616在入侵后执行了多阶段攻击链：  
  
- 初始访问：利用CVE-2026-20127获取高权限（非root）管理员访问，并向SD-WAN管理/控制平面添加恶意对等设备  
  
- 权限提升：故意降级软件版本重新引入旧漏洞CVE-2022-20775，从而获取完整root权限  
  
- 版本恢复：将系统恢复至原始软件版本以消除降级操作的取证证据  
  
- 持久化：在/home/root/.ssh/authorized_keys中添加未授权SSH密钥，在sshd_config中设置PermitRootLogin yes，并修改SD-WAN启动脚本  
  
- 横向移动：利用NETCONF（端口830）和SSH在SD-WAN设备间横向移动，操纵整个架构配置  
  
- 痕迹清除：清除syslog、bash_history、wtmp、lastlog及/var/log/下的日志  
  
**Part02**  
## 应对建议  
  
  
Cisco Talos建议管理员立即审计SD-WAN日志中的控制连接对等事件，检查是否存在未经授权的vManage对等连接、异常源IP和异常时间戳。任何显示添加恶意对等设备、SSH密钥修改或版本降级/升级周期的日志条目都应被视为高可信度的入侵指标。  
  
  
美国网络安全和基础设施安全局（CISA）已将CVE-2026-20127添加到其已知被利用漏洞（KEV）目录，并要求联邦机构立即修补。使用Cisco Catalyst SD-WAN的组织应立即应用补丁，查看安全公告，并参考澳大利亚网络安全中心发布的《SD-WAN威胁狩猎指南》检查是否已遭入侵。  
  
  
**参考来源：**  
  
PoC Exploit Released Cisco SD-WAN 0-Day Vulnerability Exploited in the Wild  
  
https://cybersecuritynews.com/poc-exploit-cisco-sd-wan-0-day-vulnerability/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335724&idx=1&sn=2d144482a43dfe8583cb475e06c7dd4e&scene=21#wechat_redirect)  
  
  
### 电报讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
