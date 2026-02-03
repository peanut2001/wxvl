#  Office 最新高危漏洞遭利用，多国政府机构被定向攻击  
看雪学苑
                    看雪学苑  看雪学苑   2026-02-03 09:59  
  
近日，一起利用 Microsoft Office 最新高危漏洞（CVE-2026-21509）的定向攻击活动被曝光。该漏洞在微软发布安全公告的次日便遭恶意利用，攻击目标直指乌克兰及欧盟国家的政府机构。以下是事件关键分析：  
  
**0****1**  
  
  
**攻击手法：钓鱼邮件 + 漏洞利用**  
  
  
攻击者通过钓鱼邮件投递恶意 Office 文档。一旦用户打开文件，便会触发 CVE-2026-21509 漏洞，自动执行恶意代码，在受害者系统中建立初始访问权限。攻击载荷通常从远程服务器下载，最终植入后门等恶意程序。  
  
  
**02******  
  
  
**攻击特征：快速、定向、有组织**  
  
  
高度定向：主要针对乌克兰及欧盟政府机构，诱饵文档经过精心伪装。    
  
反应迅速：漏洞公开后攻击立即开始，说明攻击者具备快速武器化能力。    
  
基础设施有组织：使用多个相似恶意域名，背后很可能存在团队协作。  
  
  
**03******  
  
  
**影响范围：政府机构面临多重风险**  
  
  
此次攻击可能导致敏感信息被盗、系统被控，甚至内网横向渗透。根据监测，攻击者使用的 C2 服务器及载荷分发服务器主要分布在德国、美国和摩尔多瓦。其中，德国（北莱茵－威斯特法伦州、黑森州）的 IP 最为集中，疑似为核心部署区域；美国与摩尔多瓦的节点则可能用于辅助或掩护。攻击基础设施的跨国分布，也增加了追踪溯源的难度。  
  
  
建议相关机构及时更新 Office 安全补丁，提高员工对钓鱼邮件的识别意识，并对网络流量进行监测，防范此类定向攻击。  
  
  
﹀  
  
﹀  
  
﹀  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
