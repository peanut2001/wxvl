#  GCP Apigee跨租户读写漏洞剖析  
Dubito
                    Dubito  云原生安全指北   2026-02-11 00:35  
  
   
  
> 注：本文翻译自   
Omer Amiad[1]  
 的文章  
《GatewayToHeaven: Finding a Cross-Tenant Vulnerability in GCP's Apigee》[2]  
，可点击文末“阅读原文”按钮查看英文原文。  
  
  
全文如下：  
## 一、引言  
  
几个月前，我发现了 **GatewayToHeaven**  
 漏洞，这是 Google Cloud Apigee 中存在的一个安全问题，允许读取和写入详细的跨租户访问日志与分析数据。部分数据包含明文的访问令牌（access tokens），这些令牌可能被窃取，用于潜在冒充任何使用 Apigee 组织的终端用户。该漏洞被分配编号   
CVE-2025-13292[3]  
。  
  
本文适用于：  
- • **云安全研究员和漏洞赏金猎人**  
：希望寻找在复杂多租户架构中发现漏洞的新方法。  
  
- • **云和软件工程师**  
：有兴趣了解自身架构中潜在的风险点，并了解攻击者可能如何针对其 SaaS 产品发起攻击。  
  
我们将深入探讨 Apigee 的内部架构、如何在 Apigee 的租户项目（tenant project）中获得初始立足点，以及如何提升权限并访问属于其他组织的数据。  
  
**若想了解关于此漏洞更简短、技术细节较少的概述，请随时查看这份执行摘要[4]。**  
## 二、什么是 Apigee  
  
根据 Google 的  
官方说明[5]  
：  
> Apigee 提供了一个 API 代理层，它位于您的后端服务与希望使用这些服务的内部或外部客户端之间。  
  
  
您可以使用自定义策略在整个请求流程（从终端用户到后端，再返回）中配置其行为。这些策略可用于为不支持身份验证的后端添加验证、将请求或响应从 XML 转换为 JSON（或反之）、移除和添加 headers 等等。  
  
Apigee 是一项托管服务（managed service），这意味着 Google 负责设置运行所需的相关资源。您无需自行部署服务器并在其上运行 Apigee 基础设施——Google Cloud 会为您完成这些工作。这些资源是在一个特殊的 Google Cloud 项目中设置的，该项目被称为 **租户项目（tenant project）**  
。  
## 三、什么是租户项目  
  
您可能知道，Google Cloud Platform（GCP）中的项目（projects）用于在资源之间建立明确的安全边界，即使它们属于同一个组织。  
租户项目[6]  
（tenant projects）简单来说就是由 Google 组织（organization）配置的 GCP 项目，用于托管专为单个服务消费者提供的托管服务资源。  
  
在一个项目中启用 Apigee 时，Google 会创建一个与其关联的专用租户项目，用于托管与 Apigee 相关的资源。每一个启用了 Apigee 的项目都关联一个不同的租户项目。这样，即使所有资源都由 Google 管理，也能在一个租户与其他租户使用的资源之间实现强大的逻辑隔离。由于租户项目由 Google 管理，消费者（consumers）没有直接访问这些项目的权限。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5BWRPQfbFAianpQnr39YicWn2tAGDalaXEv226MYrasK452G42FHOcffLWIHXDKcJPOBfGx6VBOc5OMFnhvanPHibwrTJKIibknWZ8/640?from=appmsg "null")  
  
租户项目之所以值得关注，是因为它模糊了属于消费者和属于 Google 的界限。这就引出了几个问题：Apigee 租户项目包含哪些资源？这些资源是否与任何 Google 管理的服务账号（service accounts）关联？是否有服务账号能够访问位于租户项目之外的跨租户资源？  
  
如前所述，消费者无法直接访问租户项目中的资源，这使得对其进行枚举变得非常困难。为了深入了解其内部架构，我们必须首先找到一种方法，在租户项目中获得初步的立足点。  
## 四、获取对 Apigee 服务账号的访问权限  
  
截至目前，这是我们对租户项目以及理论上的跨租户目标的认知情况：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DZx7MaSUV9bbVLChKdQcswQDFALZafn0HfFicCOlGCgGF6REVtVp9Y6VzwhibaUUkJoibSibZp9OHqyuaIKjMwWQ7oGSEJ05bOc8w/640?from=appmsg "null")  
  
如图所示，我们目前掌握的信息还非常有限。  
  
当面对一个新的云研究项目时，一个好的起点是查阅文档。Apigee 还有一个混合版本（hybrid version），允许部署在云环境之外，从而也就在租户项目之外。虽然云部署和混合部署在某些方面有所不同，但在其他许多方面又很相似，探索文档齐全的混合版本可以揭示云版本中各组件的配置方式。  
  
这是 Apigee 混合部署的一个  
大致示意图[7]  
：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DXIJWMlic4EAruickvhORM2R00mWd6yAiclJEcoP05N493PsLnERJbLhKGkYdE1D1Dica0yJV4tgOCZYQ1Wgvia1RZhTqlfoSErdmg/640?from=appmsg "null")  
  
这个架构很复杂，但目前并非完全相关。需要注意的是，它基于 Kubernetes，云部署同样使用了 Kubernetes——并且 Apigee 的主要组件是消息处理器（Message Processor），即图中标黄的组件。  
  
消息处理器是位于终端用户和后端服务之间的 API 代理——所有通过 Apigee 的终端用户请求都由它处理。所有其他组件的存在都是为了确保它能按预期工作——为它提供最新的配置，并将分析数据流回 Google。  
  
在 Google Kubernetes Engine 中，像消息处理器这样的 Pod 可以访问一个  
元数据端点[8]  
，就像它们所运行的底层  
计算实例[9]  
一样。这个虚拟端点可以被工作负载（workloads）用来获取其执行环境的信息，例如它们运行的实例名称、配置的 GCP 项目等。这个元数据端点也用于向工作负载  
分发短期服务账号令牌[10]  
（short-lived service account tokens），这使其成为攻击者提升权限的绝佳目标。可以通过托管在地址 169.254.169.254  
 上的 HTTP 服务器访问此元数据端点。  
  
这就引出了一个有趣的问题——我们能否配置 Apigee 将元数据端点作为后端？因为消息处理器是将我们的请求转发到后端的代理组件，配置地址 169.254.169.254  
 应该会将其自身的元数据端点暴露给终端用户。  
  
我们还需要先解决另一个问题：Apigee 默认会为所有被代理的请求添加 X-Forwarded-For  
 标头（header），这会导致元数据端点拒绝该请求，这是针对服务器端请求伪造（Server-Side Request Forgery，SSRF）的一种防御机制。幸运的是（对我们而言），可以通过使用 Apigee 的   
AssignMessage[11]  
 策略来绕过它，该策略可用于在请求发送到后端之前移除其中的标头。  
  
通过暴露消息处理器的元数据端点，就可以请求与该工作负载关联的服务账号的令牌：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5B6azy6V2Pnh8eC1NNetCQwwGu7SJY3jSz46nrj8PtMZdzPiaAStxwL9eKm8hQtpea2K72ChQsNJaznj4KicfEEhfftSQ0xneiawo/640?from=appmsg "null")  
  
与 Apigee 服务账号关联的电子邮件是 service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com  
。该电子邮件地址的域名表明，此服务账号是在 gcp-sa-apigee  
 项目下创建的，这是一个由 Google 管理的项目。由于它是一个 Google 管理的服务账号（Google-managed service account），很可能对某些 Google 管理的资源拥有权限。  
## 五、租户项目侦察  
  
在获得 Apigee 服务账号的令牌访问权限后，我们可以尝试用它来枚举租户项目中存在的其他资源和工作负载（workloads）。为此，我们需要了解该服务账号究竟拥有哪些权限。  
gcpwn[12]  
 是一个有用的权限枚举工具，它可以遍历服务账号可能拥有的所有权限并进行检查。  
  
该工具发现的一些有用的权限包括：  
- • 对租户项目中计算磁盘（compute disks）和快照（snapshots）的完全访问权限。  
  
- • 对租户项目中所有存储桶的读写权限。  
  
- • 对租户项目中 PubSub 主题（topics）的写入权限。  
  
凭借这些权限，我们可以列出和读取磁盘、快照等资源，并控制我们知道名称的存储桶内容。这是使用 Apigee 服务账号令牌在租户项目上执行 gcloud compute disks list  
 命令的输出：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DdicN9iaZJfoSBqicIDdu8hicvSb37RSed5uibgFCOzXkRuzUFglV8CZiab0v4LtKkxFiaADLFCndtvhvFrpfJsmn1M3Gz8J3omAmY2o/640?from=appmsg "null")  
  
其中包含 Google Kubernetes Engine（GKE）磁盘、PVC 磁盘（某些 GKE Pod 使用的持久化磁盘）以及与某种分析流水线（analytics pipeline）相关的磁盘。读取这些磁盘的内容将使我们能够揭示租户项目中各组件的运行行为。  
  
为了转储磁盘的内容，需要执行以下步骤：  
1. 1. 创建磁盘的快照（snapshot）。  
  
1. 2. 将其迁移到我们控制下的另一个项目。  
  
1. 3. 在我们自己的项目中从该快照重建一个新磁盘。  
  
1. 4. 创建一个计算实例并将磁盘附加到该实例。  
  
1. 5. 挂载磁盘并查看其内容。  
  
我开始研究时，先快速浏览了转储文件（dumps）中的所有日志和配置文件，尝试绘制租户项目的架构图。此外，我一直在寻找任何跨租户资源访问的线索。虽然我查看了所有内容，但最让我感兴趣的是那个分析流水线磁盘。  
  
在该磁盘中，有一个名为 boot-json.log  
 的文件，它包含了关于该分析计算实例行为的日志：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5Dzo4cIV4a2wekdKrhumCF9EvdzS1FMEfSpXQk9DunrbF3bXacW7ncXicA2F6JuggAeNyQDS9rpXw5nMNuhFAwF4pWWia3yciauY8/640?from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5Dibxo1U0YXc2fsib6Vvj8G1e9cSFIF1KlcTVTVItKwVvFOCXvb0qMFU9aXDg7T63MdR8b3vr4lRXelCrMGXVuxHkXLpIwbjDW5o/640?from=appmsg "null")  
  
这些日志显示了两件事：  
1. 1. 该租户项目配置了   
Dataflow[13]  
，此磁盘属于它的一个计算实例。正如 Google 所描述的，**Dataflow 是一个 Google Cloud 服务，用于大规模统一进行流式和批量数据处理**  
。Dataflow 可用于创建数据管道（pipelines），从一个或多个源读取数据，进行转换，然后将数据写入目的地。  
  
1. 2. 初始化时，Dataflow 管道会访问一个存储桶（bucket），下载 JAR 文件，并在执行时将其作为依赖项使用。  
  
下载 JAR 文件的存储桶位于租户项目内，并且 Apigee 服务账号拥有对该存储桶的读写权限。我们可以利用这些权限，用恶意代码 patch 其中一个 JAR 文件，从而在 Dataflow 计算实例上实现远程代码执行（Remote Code Execution，RCE）。  
  
但这真的对我们有帮助吗？这样做我们能获得什么呢？  
  
从转储文件中的另一个文件 pipeline_options.json  
 可以看出，Dataflow 管道是使用另一个服务账号执行的，即 apigee-analytics@TENANT-PROJECT.iam.gserviceaccount.com  
：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5AWw6NehvgstrxjZsR93K9icgFTpCbibjVKquNvnxjnibtfoE7YrNic8gpuv4CibMfa4xibRbgQ4hAZSiceOqeXpepJ5hwzgcwWjeicPz0/640?from=appmsg "null")  
  
这个服务账号**可能**  
拥有某些跨租户的权限。同一个文件中还有以下配置值：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5AYIbUGJaoRLdFqBqhN7b1moSRianSqz4Pria5EfM3fF8zqTPh9VmctXo9c6GibVuWe8scTaV7VFr18jMSfksUiaFzLgicuWV4ACLWw/640?from=appmsg "null")  
  
其中指定的元数据存储桶名称没有任何随机后缀，暗示它可能包含跨租户的元数据。  
  
随后，我反编译了 Dataflow 的 JAR 文件，以便进一步研究元数据存储桶是如何被使用的。这揭示了更大的潜力！  
  
如下面的截图所示，元数据存储桶是几个缓存目录的根路径，其中之一是 tenant2TenantGroupCacheDir  
：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DElHibvmvVDXbRcbZB18PcYcFgeMOHjyZ3ahr55HJdgvsb1CBB50mUicdhadh1K8tW1Sd6O1YJmtJdHRraX5eGUcINFSK6FKW7k/640?from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5B5rATNrsBCBDSFeU6kERN5iaecLUVketx8OrQA0MTukEugrg4W5iajsCfhrjKHY0NwYZtfde0MQqpOB6IFXcIWIm5wWvTxPkaQg/640?from=appmsg "null")  
  
构造缓存目录的函数的参数是：  
1. 1. getCustomerType  
：似乎总是返回字符串 revenue  
  
1. 2. repo  
：似乎总是字符串 edge  
  
1. 3. ds  
：字符串 api  
 或 mint  
 中的一个。  
  
这个路径中的任何参数都不包含任何租户特定的值！这表明文件路径并不依赖于租户本身，因此多个租户可以访问同一个缓存文件！  
  
稍后在 refreshApiUapContext  
 函数中，tenant2TenantGroupCacheDir  
 被传递给 getTenant2TenantGroup  
，结果被保存到上下文对象的 TENANT_2_TG  
 下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DCUDiabOpKiaw3onBFhqAqPgQO1wQarRiaa2FbyyMKTibmcMu5ULGEZia1zxmBeb8RicNXKrZJu0iaDDs0vLYEaccpzueprZD7EN997E/640?from=appmsg "null")  
  
getTenant2TenantGroup  
 函数读取并解析缓存目录中最新的 JSON 文件，遍历所有租户组（tenant groups），并为每个租户将租户名称映射到租户组名称：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DJunuOp9vV8A6GFKf3YNWgpKDQ5Xct7tSjBg6zZ0SxxKyQfhDYSHKFgeYLtzGaho8ZU6ianwSgFicOib6gGvHQvz1MZibBpbPg6EI/640?from=appmsg "null")  
  
看起来由 Dataflow 初始化的租户组映射应该包含所有 Apigee 租户的名称！  
  
回顾简化后的租户项目架构，我们可以看到它现在看起来是这样的：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5D9wHMibhrbO4wAETdvaaYxt7ObRubhe8tya7licvzm5OZcmYhu76nxAD2ff2K2c6IFf9Pf5uKm0KEVqHHZoagC359AWlOpNPSeg/640?from=appmsg "null")  
  
其中，跨租户元数据存储桶被所有租户项目中的 Dataflow 管道访问。  
  
从攻击者的角度来看，单个租户项目的架构现在变成了这样：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5AibKFTRflvQbz19OMMwGvyS7y9ib9dC59zTxJ6MfR9b1jqiaaBWju8ibDmElKoOSJUcPyCPMr79ibbicJhPgafO5LwK0zFRicqB1L6Lc/640?from=appmsg "null")  
  
这足以让我确信这个漏洞利用具有相当严重的潜在影响。那么，最后一步将是在 Dataflow 实例中执行代码，并获取 Apigee 分析服务账号的令牌。  
## 六、提升为 Dataflow 服务账号权限  
  
回顾一下，我们之前发现 Apigee 服务账号拥有对存储桶的写入权限，该存储桶存放着 Dataflow 管道执行的 JAR 文件。我们还发现，Dataflow 管道很可能有权访问跨租户资源。  
  
为了将权限提升至 Dataflow 服务账号，我们可以从存储桶下载 Dataflow 的 JAR 文件，并使用诸如   
Recaf[14]  
 这样的 Java 补丁工具进行修补。我们的恶意实现将简单地访问 Dataflow 计算实例的元数据端点，获取 Dataflow 服务账号的令牌，并将其上传到我们控制的远程服务器。  
  
修补 JAR 文件后，我们可以使用 Apigee 服务账号覆盖存储桶中的现有文件：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5C7BGHgeKd77r58nS2Q5ic1ENhPsebkbKyw18KjFicDHR17lXicJbQQFBno57ia3zKibwO3xEJNbXPOvH3oviaLcseMeheicPDvmObhJU/640?from=appmsg "null")  
  
仅仅这样做并不会自动感染现有的 Dataflow 实例。这些 JAR 文件只会在新的 Dataflow 计算实例被配置（provisioned）时才会被获取——而通常没有充分理由的情况下，这种情况不会发生。  
  
为了促使创建新的 Dataflow 实例，我们可以利用 Dataflow 的自动扩缩（autoscaling）机制，该机制会在现有实例负载过重时配置新实例。通过向现有的 Dataflow 管道发送大量伪造的分析事件，系统就会使用恶意的 JAR 文件配置一个新的 Dataflow 实例。  
  
前面提到的 pipeline_options.json  
 文件引用了一个   
PubSub[15]  
 输入订阅（input subscription）的名称：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5D0v5nib8DGpC1hOlvTCJiaIzm9956WDdSrBfUCEPpTaE8nJXYrEPzBNPhOnxibP0kOEJgOS4YvxDcEeSW5ia0BDjM5ZNHiaTS3MSRc/640?from=appmsg "null")  
  
并且反编译的 Dataflow 代码显示，事件正是从这个订阅读取的：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5AC0qPUcleqd4djZpzNSJVibFpqW7XlAibncQm7kLHWCxnibaLJUmChZrrE58AwMtrJ4gDKOtM7ofoXz1OEbMCKbYwYb8rs08YkHw/640?from=appmsg "null")  
  
在 Google 的 PubSub 中，事件从订阅（subscriptions）读取，并写入主题（topics）。在租户项目中，与 apigee-analytics-notifications  
 订阅关联的主题（topic）名称相同。现在，我们可以编写一个脚本，利用 Apigee 服务账号的凭据，向该 PubSub 主题写入大量事件，给现有的 Dataflow 实例施加压力，从而促使系统配置新的实例：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5C41ukeABSD3b5bDcBxiaZdFPU3frUTJICoJ0wgwqSoGIpXtFqr1iaRmODmpeCeIBKU21GGAadpjfqicnzKSBibtDHQ1ExvWxJNibuI/640?from=appmsg "null")  
  
这种技术成功地配置了一个获取了 JAR 文件的新 Dataflow 实例，但我们的远程服务器没有收到任何令牌。这是因为租户项目中的 Dataflow 计算实例配置为无法访问互联网，从而阻断了恶意 JAR 与服务器的通信。  
  
为了解决这个问题，我们可以用一个 Google 存储桶（Google storage bucket）来替代服务器作为接收令牌的目的地。尽管 Dataflow 屏蔽了互联网访问，但它仍然可以在内部访问 GCP API：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5ACbVqX4qIwpJrY2XqdgGYDBiclJYlqiar9mtCcbKRbic5F2FPzLxjszka9MyXux9wG3ibGh6YMCxicoWia4FCBqFpNjNhKtMoAvUe60/640?from=appmsg "null")  
  
按照上述设置后，我们就可以从存储桶中读取令牌，它确实属于 Dataflow 服务：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5DrBHOlhmJM7HYzddNe4eZ4oDtoFfkhtcLw7975aQJEc7kHPqewdOpR8M5ZibGTIGeUQ9W8QVxxY9bCZexQp3hbFzicw2s3iaUP9k/640?from=appmsg "null")  
## 七、漏洞影响  
  
凭借该令牌，最终得以访问跨租户的元数据存储桶！在存储桶 tenantToTenantGroup  
 文件夹下的缓存目录中，我们可以看到许多无关租户的 GCP 项目名称及 Apigee 环境名称，它们因某些原因被归为一组：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5BTBKbz2fyibN71q8xhSwtObpepMF804Da7CjCHxtPEZKDtiaMvtqD1m4iaddRWbGVDaibgibd2UGIiaJv5SEFWykEDVp8OO5CAShibV8/640?from=appmsg "null")  
  
我甚至发现，我今年早些时候创建的一个 Apigee 项目，与所有这些随机的其他租户被归在同一个租户组下！  
  
在 customFields  
 文件夹下，所有不同 Apigee 租户的自定义分析字段（custom analytics fields）都可以被访问。这是一个租户的自定义分析字段示例：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5Ba7gafHot8Vm3s0ChWTA2EehsC5OaexETPdIMd3krMyqNFvNm4T92eweULtCWT5Kiarslpkw0ibf1Ofs65fYv0nLmWjSUia01L9E/640?from=appmsg "null")  
  
但最有趣的文件夹是名为 datastores  
 的那个。它引用了一些"GCS 数据存储（GCS datastores）"，每个 GCP 区域一个：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5CHS3qn2421BGviaxy25A2RPbq3ZaZfoWNxs9buNMVQeWRfXIVo9ZmWNl9NyRIkHvO6cp8a64WmBmmQQ6Jq6LWtoKRUicgC4nSt4/640?from=appmsg "null")  
  
使用 Dataflow 服务账号同样可以访问这些存储桶。经过仔细检查，**这些存储桶似乎包含了 Apigee 所有租户的每一次请求的分析数据**  
。例如，从某个随机租户的以下分析事件中，我们可以推断其后端是某种文件服务器，并且可以看到所获取文档的完整路径：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5DI55JXzZakxdSZ7lUNOKGau1doXb20cZW4sYia4NoPvh3S4rzqsvGfB6LRrmichJmDoeaEoqZMkgyw87nafjVwevK5wYDZxicQqQ/640?from=appmsg "null")  
  
以下是一个大型电子商务平台的分析事件，其中包含了终端用户的真实 IP 地址，并且他们的访问令牌以明文形式可见！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5D8D253aW9YMW5WsnNAyw2Ea6NLOEBv28ZP9yRfJCLYibdub5QZtjJLuVQtMUdrSwJvmlWebbAzpfeTyR0twpPcDRlicia7zdCictA/640?from=appmsg "null")  
  
这个访问令牌是攻击者从这些日志中能够提取到的最敏感的信息。攻击者可以窃取这些令牌，并利用它们以任意 Apigee 租户的任意终端用户的身份进行身份验证并发起请求。  
  
举例来说，假设“Bank of Cyber”选择使用 Apigee 作为其后端服务的代理层，并利用安全策略为终端用户添加身份验证和授权。约翰是“Bank of Cyber”的客户，他刚刚通过 Apigee 访问了其后端服务并发起了一笔新的转账请求。此时，攻击者可以访问跨租户的访问日志和分析数据，获取约翰的访问令牌，并冒用其身份发起一笔恶意转账。  
  
除了访问日志，这些数据存储桶中还有一个名为 queryresults  
 的文件夹，里面存放着 Google 内部执行的查询结果的 CSV 输出，这可能是提供给高端 Apigee 客户的某种高级服务：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5AWYw4ibgnpNTGciaTswr2ribyX22D6wL7QUr4IgUQJekKDP9OQAZcDErrKI5biaM0wgFFNlE22H2YQrz1dr2QSfYOLqtzpOCtz2Bc/640?from=appmsg "null")  
  
除了读取权限，Dataflow 服务账号对这些存储桶还拥有写入权限。我没有尝试向其中任何存储桶写入数据，因为这可能会影响我尚未完全了解的生产系统，因此无法确定其确切影响。Google 最终将此漏洞评定为读写跨租户漏洞，这表明写入权限也可能被用于恶意目的。  
## 八、结论  
  
本文讨论了在 Apigee 中发现跨租户漏洞的研究和发现过程。希望这篇报告能对您的漏洞赏金和红队工作有所帮助，或者反过来，帮助您检查并加固自己的云架构，以防出现类似问题。  
  
完整的攻击路径如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Kric7mM9eA5BXU8wMAd8hgVl2LOlHzeakMeiaae93WXtmrodR9rdqAy3Rh7AybGLiaJWT3vRevosib39kvXHdxF8ibibOGZ8wm1yPIuvYwyricm9cQ/640?from=appmsg "null")  
1. 1. 攻击者将 Apigee 指向 GKE 的元数据端点，获取其自身租户项目中消息处理器（message processor）的服务账号令牌。  
  
1. 2. 攻击者利用 Apigee 服务账号的权限转储租户项目中的磁盘，发现了 Dataflow 暂存存储桶（staging bucket）的名称。  
  
1. 3. 攻击者将一个恶意 JAR 文件上传至 Dataflow 暂存存储桶。  
  
1. 4. 随后，他们向 PubSub 主题（topic）发送大量垃圾信息，使现有 Dataflow 实例负载过重，从而触发自动扩缩并配置新的 Dataflow 实例；这些新实例会拉取并执行恶意的 JAR 文件。  
  
1. 5. 恶意 JAR 文件从元数据端点获取 Dataflow 服务账号的令牌，并将其上传到攻击者控制的 GCS 存储桶，从而绕过 Dataflow 的网络限制。  
  
1. 6. 攻击者利用 Dataflow 服务账号的令牌访问跨租户存储桶，检索所有 Apigee 租户的分析信息，其中包括高度敏感的 OAuth 令牌，从而获得了冒充用户的权限。  
  
#### 引用链接  
  
[1]  
 Omer Amiad: https://omeramiad.com/  
[2]  
 《GatewayToHeaven: Finding a Cross-Tenant Vulnerability in GCP's Apigee》: https://omeramiad.com/posts/gatewaytoheaven-gcp-cross-tenant-vulnerability/  
[3]  
 CVE-2025-13292: https://www.cve.org/CVERecord?id=CVE-2025-13292  
[4]  
 执行摘要: https://focalsecurity.io/blog/gatewaytoheaven-gcp-cross-tenant-vulnerability  
[5]  
 官方说明: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee  
[6]  
 租户项目: https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant  
[7]  
 大致示意图: https://cloud.google.com/apigee/docs/hybrid/v1.15/what-is-hybrid#about-the-runtime-plane  
[8]  
 元数据端点: https://docs.cloud.google.com/compute/docs/metadata/overview  
[9]  
 计算实例: https://docs.cloud.google.com/compute/docs/instances  
[10]  
 分发短期服务账号令牌: https://docs.cloud.google.com/docs/authentication/application-default-credentials#attached-sa  
[11]  
 `AssignMessage`: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy  
[12]  
 gcpwn: https://github.com/NetSPI/gcpwn  
[13]  
 Dataflow: https://docs.cloud.google.com/dataflow/docs/overview  
[14]  
 `Recaf`: https://github.com/Col-E/Recaf  
[15]  
 PubSub: https://docs.cloud.google.com/pubsub/docs/overview  
  
   
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/Kric7mM9eA5Bhd8h2TwQY9GSugq2RD9X7FibHXOprRj6GYhMo28tupaq11nibqmmRB4HkuhAZ6nBUaoEMicx2kc1YpVBsIsdbDa3vZZlic7ibJX4M/640?wx_fmt=gif&from=appmsg "")  
  
  
  
**交流群**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Kric7mM9eA5AGHtVzEOmcFsA9fhK5cGhZnibuwCmZJUmuFGibZbMzyvhnl7lj3kaMAicDMeXTqCI0LL1OUYfsNcd7vJN51FGZOgo6EhgVWJibZRI/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
