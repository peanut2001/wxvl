#  CISA警告：VMware vCenter 严重远程代码执行漏洞已被攻击者利用  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-01-26 01:02  
  
**导****读**  
  
  
  
美国网络安全和基础设施安全局 (CISA) 已将影响博通 VMware vCenter Server 的一个严重漏洞添加到其已知利用漏洞 (KEV) 目录中。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaGbicauxtFjZJ0k39muicxVd3B7Rv2s057kKcwzGnjWZCd7ZG7iaInGLhcibwHbKOFvAHb2Vy4EUTW5Pw/640?wx_fmt=png&from=appmsg "")  
  
  
此次新增内容证实，CVE-2024-37079已被实际利用，对依赖 vCenter 进行虚拟化管理的企业环境构成重大风险。  
  
  
该漏洞最初由博通公司披露，被归类为 DCERPC（分布式计算环境/远程过程调用）协议实现中的越界写入问题。  
  
  
成功利用漏洞后，攻击者可以通过网络访问 vCenter Server 来执行远程代码，从而有可能完全控制受影响的系统。  
  
  
此漏洞源于 DCERPC 协议实现中不当的内存处理。未经身份验证的攻击者可以通过向 vCenter Server 发送特制的网络数据包来触发此漏洞。  
  
  
由于 vCenter Server 是管理 VMware vSphere 环境的集中式管理实用程序，因此，一旦 vCenter Server 遭到入侵，攻击者通常就能在整个虚拟化基础架构中进行横向移动。  
  
  
虽然该漏洞与 CWE-787（越界写入）相关，但它尤其危险，因为它不需要用户交互。攻击途径完全基于网络。  
  
  
尽管 CISA 目前的数据将“已知用于勒索软件活动”的状态列为“未知”，但该漏洞的性质使其成为初始访问代理和勒索软件组织极具吸引力的入口点。  
  
  
2026 年 1 月 23 日，CISA 将 CVE-2024-37079 添加到 KEV 目录中，强制要求联邦民事行政部门 (FCEB) 机构在 2026 年 2 月 13 日之前修复。  
CISA  
同时建议所有组织（不仅限于联邦机构）立即优先修复此漏洞。建议采取的措施是应用供应商提供的缓解措施，如果无法获得缓解措施，则停止使用该产品。  
  
  
博通公司已发布vCenter Server 更新以解决此问题，并敦促管理员升级到最新的安全版本。  
  
  
为保护虚拟化基础设施免受此威胁，安全团队应采取以下步骤：  
- 立即修补：应用博通安全公告中提供的相关补丁。  
- 网络分段：确保 vCenter Server 接口不暴露于公共互联网。仅允许受信任的管理网络访问 vCenter 管理界面。  
- 监控流量：实施网络监控，以检测指向 vCenter 服务器的异常 DCERPC 流量。  
- 审查日志：审核访问日志，以发现未经授权连接到管理界面的尝试。  
新闻链接：  
  
https://cybersecuritynews.com/vmware-vcenter-rce-vulnerability/  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
