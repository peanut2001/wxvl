#  Kubernetes 中的 node/proxy GET 权限漏洞：实现远程代码执行（RCE）  
原创 助力行业的
                    助力行业的  李白你好   2026-01-28 00:02  
  
## 前言  
  
在 Kubernetes 集群中，权限管理是安全的核心组成部分。然而，一个鲜为人知的授权绕过问题可能导致严重的远程代码执行（RCE）风险。具体来说，任何分配了 nodes/proxy GET 权限的服务账户，如果能够通过 10250 端口访问节点的 Kubelet API，就可以向 /exec 端点发送请求，从而在任意 Pod（包括特权系统 Pod）中执行命令。这不仅可能导致整个集群被攻破，而且 Kubernetes 的审计策略不会记录通过直接连接 Kubelet API 执行的命令，从而使攻击难以追踪。本文将基于相关研究和分析，探讨这一漏洞的原理、利用方式、潜在影响以及缓解措施。  
  
![What is Kubernetes? | Microsoft Azure](https://mmbiz.qpic.cn/mmbiz_jpg/XoIcX2HtlUCcLedIUGCA927t6aic7NBzvstsibdzcAv11QUS7j4iaOZHibqYNnQUQ2bD6tWRv57ATApAZMzzicZ7nicw/640?wx_fmt=jpeg&from=appmsg "")  
## 漏洞背景  
  
Kubernetes 的 Role-Based Access Control (RBAC) 系统用于管理对资源的访问权限。其中，nodes/proxy 子资源允许用户通过 API Server 代理访问节点的 Kubelet API。正常情况下，/exec、/run、/attach 和 /portforward 等端点被映射到 proxy 子资源，这些端点用于在 Pod 中执行命令或附加进程。  
  
![Executing Commands In Another Pod](https://mmbiz.qpic.cn/mmbiz_gif/XoIcX2HtlUCcLedIUGCA927t6aic7NBzvZwaQ7cEIvEAam1qKloibhU7DlyVxIHTZtxaXkn7aibtBLudticyoN9oCA/640?wx_fmt=gif&from=appmsg "")  
  
问题在于 Kubelet 在处理 WebSocket 连接时的授权逻辑：WebSocket 握手使用 HTTP GET 方法，而 Kubelet 仅基于初始 GET 方法进行授权检查，并未在连接升级后验证实际操作所需的 CREATE 权限。这导致拥有 nodes/proxy GET 权限的用户可以绕过写操作的权限要求，直接执行命令。这种行为被 Kubernetes 安全团队视为“按设计工作”，因此未分配 CVE，但它暴露了实际的安全隐患。  
  
许多 Helm 图表（如 Prometheus、Grafana 和 Datadog）会授予 nodes/proxy GET 权限用于监控目的，这进一步扩大了潜在暴露面。研究显示，至少有 69 个 Helm 图表存在此类权限配置。  
  
![An Overview of Kubernetes Architecture and Container Deployment - Applied  Information Sciences](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUCcLedIUGCA927t6aic7NBzvnt5QmBah4Sb5qVzQMAIARic7Usy2TyA37O90iaG8CrhbrNhBcZCyosoQ/640?wx_fmt=png&from=appmsg "")  
## 利用原理和高水平步骤  
  
要利用此漏洞，需要满足以下前提条件：  
- 服务账户拥有 nodes/proxy GET 权限。  
  
- 能够网络访问目标节点的 Kubelet API（端口 10250）。  
  
- 持有有效的 Bearer Token。  
  
- 目标节点的 IP 地址可达。  
  
利用过程大致如下：  
1. 确认服务账户权限，仅限于 GET 操作。  
  
1. 使用工具建立 WebSocket 连接到 Kubelet 的 /exec 端点，指定目标 Pod 和命令。  
  
1. 通过连接执行任意命令，如读取敏感文件或运行系统命令。  
  
![Security Audit - kubernetes/kubernetes#119270](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUCcLedIUGCA927t6aic7NBzvjibECBsibAUGN1Lw7ucu2PesB9GLAEQcNtVtUnyEgx1yMRWsYcoY16JQ/640?wx_fmt=png&from=appmsg "")  
  
例如，在攻击者 Pod 中，可以提取节点名称和 IP，然后通过代理端点列出所有 Pod，并针对特定 Pod 执行命令。这允许攻击者从一个节点 Pivoting 到其他节点，甚至访问控制平面组件如 etcd 或 kube-apiserver。 由于审计日志仅记录通过 API Server 的操作，直接连接 Kubelet 的命令不会被记录，进一步增加了隐蔽性。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUCcLedIUGCA927t6aic7NBzvT6AzgAwSK7HicyTkArZibVnQ1XycpoO4ko0bJ8hvnu1GGWy2UdeuFibiaQ/640?wx_fmt=png&from=appmsg "")  
  
需要注意的是，这种利用依赖于 WebSocket 协议的特性，Kubelet 未对升级后的操作进行二次授权检查。  
## 潜在影响  
  
这一漏洞的后果可能极其严重：  
- **Pod 级 RCE**  
：攻击者可在任意 Pod 中执行命令，包括特权 Pod 如 kube-proxy。  
  
- **集群 compromise**  
：通过窃取服务账户 Token，攻击者可横向移动，提取 Secrets，或挂载主机文件系统。  
  
- **持久化访问**  
：访问 etcd 等组件可能导致持久化后门或数据泄露。  
  
- **无日志记录**  
：绕过审计策略，使检测变得困难。  
  
在实际场景中，这可能导致整个 Kubernetes 集群被完全控制，尤其在多租户环境中。  
## 检测和缓解措施  
### 漏洞检测  
  
可以使用专用脚本扫描集群中的 ClusterRoles 和 Bindings，识别授予 nodes/proxy 权限的主体（如 ServiceAccount）。脚本会检查 ClusterRoleBindings 和 RoleBindings，输出潜在漏洞账户，并提供验证命令。 注意，此类脚本仅检测显式授予的权限，不包括从更高级角色（如 cluster-admin）继承的权限。推荐结合工具如 kubectl-who-can 进行全面审计。  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/XoIcX2HtlUCcLedIUGCA927t6aic7NBzvZwaQ7cEIvEAam1qKloibhU7DlyVxIHTZtxaXkn7aibtBLudticyoN9oCA/640?wx_fmt=gif&from=appmsg "")  
### 安全建议  
- **限制网络访问**  
：通过网络策略或防火墙阻止对 Kubelet 端口（10250）的直接访问。  
  
- **权限最小化**  
：审查并移除不必要的 nodes/proxy GET 权限，尤其在 Helm 图表中。考虑迁移到细粒度 Kubelet API 授权（KEP-2862），尽管它尚未完全可用。  
  
- **监控和审计**  
：虽然直接 Kubelet 操作不记录日志，但可以加强网络监控和使用第三方工具检测异常。  
  
- **更新配置**  
：对于特定应用（如 Cilium），使用替代方案如 Spire 避免授予此类权限。  
  
Kubernetes 社区已认识到问题，但目前无官方补丁。管理员应主动审计权限以减少风险。  
  
**漏洞分析及检测可参考**  
```
https://grahamhelton.com/blog/nodes-proxy-rcehttps://gist.github.com/grahamhelton/f5c8ce265161990b0847ac05a74e466ahttps://labs.iximiuz.com/tutorials/nodes-proxy-rce-c9e436a9
```  
## 结论  
  
nodes/proxy GET 权限漏洞突显了 Kubernetes RBAC 系统在处理代理和子资源时的潜在弱点。尽管被视为设计意图，但它为攻击者提供了绕过授权的途径，导致严重的 RCE 风险。通过理解其原理并实施严格的权限管理和网络控制，管理员可以显著降低暴露面。建议定期审计集群权限，并关注社区对 Kubelet 授权的未来改进，以提升整体安全性。  
## 网络安全情报攻防站  
  
**www.libaisec.com**  
  
综合性的技术交流与资源共享社区  
  
专注于红蓝对抗、攻防渗透、威胁情报、数据泄露  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUCcLedIUGCA927t6aic7NBzvdjcSdBM8tayEfQMBRHaiaNElxsbp93gbHymumwpXGmPwIOlZV2QZ83w/640?wx_fmt=png&from=appmsg "")  
  
  
