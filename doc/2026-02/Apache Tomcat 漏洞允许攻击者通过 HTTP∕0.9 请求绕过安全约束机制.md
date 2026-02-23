#  Apache Tomcat 漏洞允许攻击者通过 HTTP/0.9 请求绕过安全约束机制  
 网安百色   2026-02-23 10:38  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnsJpurIAnlO94BA6cHkB0BDDXef2lAcmvEtRMvceYwfRGs5bHj8BDbHR4wLjLwNxB7giatJIPspsicibD9DvIc24UvyNCHoDECDAY/640?wx_fmt=jpeg&from=appmsg "")  
  
Apache Software Foundation  
 旗下的   
Apache Tomcat  
 披露了编号为   
CVE-2026-24733  
 的安全漏洞。该漏洞被评定为低危（Low），在特定访问控制规则配置方式下，可通过 HTTP/0.9 请求触发，从而绕过安全约束机制。  
  
Apache Tomcat 安全团队发现了该问题，官方安全公告于 2026 年 2 月 17 日发布。  
  
从技术层面来看，该漏洞的根源在于 Tomcat 未对 HTTP/0.9 请求的方法类型进行限制（未强制限定为 GET 方法）。HTTP/0.9 是一种已废弃的极简协议版本，早于现代 HTTP 方法及请求头处理机制，目前在实际环境中几乎不会被正常使用。  
  
然而，如果攻击者能够访问目标 Tomcat 实例，并发送构造的 HTTP/0.9 风格请求，Tomcat 在请求方法解析过程中可能出现策略执行缺口，从而影响安全约束的正确生效。  
  
该绕过场景具体发生在以下配置条件下：  
  
某 URI 被配置为允许 HEAD 请求；  
  
同一 URI 被配置为拒绝 GET 请求。  
  
在标准 HTTP 协议版本下，此类规则能够阻止通过 GET 方法获取资源主体内容。  
  
但在 CVE-2026-24733 情况下，攻击者可以发送一个不符合规范的 HTTP/0.9 HEAD 请求，从而绕过针对 GET 请求配置的访问控制限制。  
  
需要强调的是，该漏洞具有场景依赖性，触发条件包括：  
1. 访问控制策略必须为“允许 HEAD、拒绝 GET”的特定配置；  
  
1. 攻击路径中必须存在能够端到端接受并解析 HTTP/0.9 请求的链路。  
  
尽管如此，在以下环境中该问题仍具有现实意义：  
  
存在遗留系统集成场景；  
  
使用非标准或异常客户端；  
  
部分代理或网络拓扑结构中未进行协议规范化（Protocol Normalization）处理；  
  
允许协议降级（Protocol Downgrade）行为的反向代理或负载均衡设备。  
## 受影响版本及修复方案  
  
受影响范围涵盖当前仍在维护的 Tomcat 分支以及已停止维护（EOL）的旧版本。对于仍在使用 EOL 版本的组织，应将本次漏洞视为升级至受支持版本的重要警示，因为对 EOL 版本进行安全补丁回移（Backport）通常难以保证安全性与稳定性。  
<table><thead><tr><th><section><span leaf="">Tomcat 分支</span></section></th><th><section><span leaf="">受影响版本</span></section></th><th><section><span leaf="">修复版本</span></section></th></tr></thead><tbody><tr><td><section><span leaf="">11</span></section></td><td><section><span leaf="">11.0.0-M1 至 11.0.14</span></section></td><td><section><span leaf="">11.0.15 及以上</span></section></td></tr><tr><td><section><span leaf="">10.1</span></section></td><td><section><span leaf="">10.1.0-M1 至 10.1.49</span></section></td><td><section><span leaf="">10.1.50 及以上</span></section></td></tr><tr><td><section><span leaf="">9.0</span></section></td><td><section><span leaf="">9.0.0.M1 至 9.0.112</span></section></td><td><section><span leaf="">9.0.113 及以上</span></section></td></tr><tr><td><section><span leaf="">更早版本（EOL）</span></section></td><td><section><span leaf="">同样受影响</span></section></td><td><section><span leaf="">建议升级至受支持分支</span></section></td></tr></tbody></table>  
Apache 官方建议尽快升级至上述修复版本。  
  
作为额外的安全加固措施，安全团队还应：  
  
审查受保护端点中 HEAD 与 GET 方法的访问控制策略是否符合设计意图；  
  
验证前端反向代理或负载均衡设备是否存在协议降级或异常协议透传行为；  
  
确认代理链路中是否进行协议规范化处理，避免出现意外的 HTTP/0.9 解析路径。  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1 "")  
  
