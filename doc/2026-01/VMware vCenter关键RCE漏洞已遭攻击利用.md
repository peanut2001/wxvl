#  VMware vCenter关键RCE漏洞已遭攻击利用  
 FreeBuf   2026-01-26 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39HonLcKiaspBzoEOs6Ltos7M8c6rt1ftXrhao6Wtw3EJKk6MSPQ9xfOtGcUjayILS0L1dpKWIZYcg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
美国网络安全和基础设施安全局（CISA）已将影响博通（Broadcom）VMware vCenter Server的关键漏洞列入其已知被利用漏洞（KEV）目录。此举证实CVE-2024-37079漏洞已在野被活跃利用，对依赖vCenter进行虚拟化管理的企业环境构成重大威胁。  
  
  
该漏洞最初由博通披露，被归类为DCERPC（分布式计算环境/远程过程调用）协议实现中的越界写入问题。攻击者通过网络访问vCenter Server后，可成功利用该漏洞执行远程代码，最终可能完全控制受影响系统。  
  
  
**Part01**  
## CVE-2024-37079技术分析  
  
  
该漏洞源于DCERPC协议实现中的内存处理缺陷。未经身份验证的攻击者通过向vCenter Server发送特制网络数据包即可触发漏洞。由于vCenter Server是管理VMware vSphere环境的集中式管理工具，攻陷该系统通常意味着攻击者能横向渗透整个虚拟化基础设施。  
  
  
虽然该漏洞与CWE-787（越界写入）相关，但其特殊性在于无需用户交互即可触发，攻击媒介完全基于网络。尽管CISA当前数据显示"已知用于勒索软件活动"状态为"未知"，但该漏洞特性使其成为初始访问代理和勒索软件团伙的理想切入点。  
  
  
**Part02**  
## CISA强制修复要求  
  
  
CISA于2026年1月23日将CVE-2024-37079列入KEV目录，要求联邦民事行政部门（FCEB）机构在2026年2月13日前完成修复。该机构建议所有组织（不仅限于联邦实体）立即优先修补该漏洞，推荐措施包括应用厂商提供的缓解方案，若无法缓解则应停用相关产品。  
  
  
博通已发布vCenter Server更新修复该问题，管理员应尽快升级至最新安全版本。为防范此威胁，安全团队应采取以下措施：  
  
- 立即修补：应用博通安全公告中提供的相关补丁  
  
- 网络分段：确保vCenter Server接口不暴露在公共互联网，仅限可信管理网络访问vCenter管理界面  
  
- 流量监控：实施网络监控以检测针对vCenter服务器的异常DCERPC流量  
  
- 日志审查：审计管理界面的未授权连接尝试记录  
  
距离2月中旬的最后期限仅剩有限时间，各组织需尽快修复此关键漏洞，以免其成为自动化攻击工具的标准目标。  
  
  
**参考来源：**  
  
CISA Warns of Critical VMware vCenter RCE Vulnerability Now Exploited in Attacks  
  
https://cybersecuritynews.com/vmware-vcenter-rce-vulnerability/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334254&idx=1&sn=60c1a1f106cdbab728bc207a35262d08&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
