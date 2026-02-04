#  微软将默认禁用NTLM协议，终结30年高危身份验证漏洞  
 FreeBuf   2026-02-04 10:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icfgFySDVR8vQfO3iablplDY5SAjruXACeMGSD6L5768Wc3RrHuQ9mO0x7I7icZ3hHaro1YOHN5BH6Q/640?wx_fmt=jpeg&from=appmsg "")  
  
  
微软正在加速淘汰NTLM（新技术局域网管理器）这一已在Windows系统中存在三十余年的传统身份验证协议。该公司宣布将在未来Windows版本中通过分阶段路线图逐步减少、限制并最终默认禁用NTLM，这标志着Windows身份验证安全体系的重要演进。  
  
  
NTLM长期以来作为Kerberos不可用时的备用验证机制。但由于协议年代久远且存在固有加密缺陷，使其容易遭受重放攻击、中继攻击和哈希传递攻击等安全威胁。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icfgFySDVR8vQfO3iablplDYcxKW8UIpZzevUicRuicUIicKNY7CRMicCGgrSCQwiaAGwN8J4IAttEhfFwg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part01**  
## 三阶段过渡路线图确保平稳迁移  
  
  
随着现代安全威胁不断演变，NTLM对这些攻击向量的脆弱性给企业环境带来重大风险。微软决定默认禁用NTLM，反映了采用更强大、基于Kerberos的身份验证机制以符合当代安全标准的必要性。  
  
  
过渡过程采用三阶段方案以最大限度减少对组织的干扰：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icfgFySDVR8vQfO3iablplDYYX1d3UtKjCb0poSGXqbeenh8LsnciayQYkac64kygicA1zGr4Fibes2pA/640?wx_fmt=png&from=appmsg "")  
  
  
值得注意的是，微软将为仅支持NTLM的传统场景提供内置支持，最大限度减少对使用旧系统或定制应用程序的组织造成影响。  
  
  
**Part02**  
## 迁移期间保持向后兼容性  
  
  
微软强调，默认禁用NTLM并不意味着完全移除该协议。在过渡期间，NTLM仍将保留在操作系统中，必要时可通过策略重新启用，确保持续的向后兼容性。这种方案在实质性安全改进与实际组织需求之间取得了平衡。  
  
  
微软建议各组织立即着手准备，包括部署增强型NTLM审计、梳理应用程序依赖关系以及将工作负载迁移至Kerberos。同时应在非生产环境中测试禁用NTLM的配置。微软鼓励企业联合身份认证、安全和应用程序负责人共同确保平稳过渡。  
  
  
对于存在特殊NTLM依赖场景的组织，微软已设立ntlm@microsoft[.]com作为联系渠道。这种分阶段、协作式的过渡方案将使Windows迈向更安全、无密码的未来，同时为企业环境保留支持的迁移路径。  
  
  
**参考来源：**  
  
Microsoft to Disable NTLM by Default as a Step Towards More Secure Authentication  
  
https://cybersecuritynews.com/microsoft-disable-ntlm-by-default/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334591&idx=1&sn=7a53f598d945f86ed376200b93146133&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
