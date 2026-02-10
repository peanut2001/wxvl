#  Axios 曝高危漏洞，可致 Node.js 服务崩溃  
看雪学苑
                    看雪学苑  看雪学苑   2026-02-10 09:59  
  
近日，全球广泛使用的 HTTP 客户端库 Axios 曝出一个高危漏洞（CVE-2026-25639），CVSS 评分为 7.5。该漏洞存在于核心配置合并函数 `mergeConfig` 中，当处理包含 `__proto__` 自有属性的配置对象时，会触发 TypeError 错误，导致 Node.js 进程崩溃。  
  
  
主要受影响的场景为：  
- 使用 Axios 的 Node.js 服务器；  
  
- 应用程序接收用户输入，通过 `JSON.parse()` 解析后，将其传入 Axios 配置。  
  
攻击者只需构造类似 `{"__proto__": {"x": 1}}` 的恶意 JSON 载荷，一旦被解析并传递给 Axios，即可引发服务拒绝，使得整个应用下线，需人工重启才能恢复。  
  
  
Axios 维护团队已发布版本 1.13.4 修复该问题，建议所有开发者立即升级至 1.13.4 或更高版本（如 1.13.5），以避免潜在的服务中断风险。  
  
  
参考来源：  
- 漏洞编号 CVE-2026-25639    
  
- Axios 官方发布版本 1.13.4 修复该问题    
  
- CVSS 评分来自通用漏洞评分系统  
  
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
  
