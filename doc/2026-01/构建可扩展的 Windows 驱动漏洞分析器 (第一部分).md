#  构建可扩展的 Windows 驱动漏洞分析器 (第一部分)  
splintersfury
                    splintersfury  securitainment   2026-01-25 02:24  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://threatunpacked.com/2026/01/21/building-a-scalable-windows-driver-vulnerability-analyzer-part-1/</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">splintersfury</span></section></td></tr></tbody></table># 背景  
  
随着我在内核驱动上花的时间越来越多，这种兴趣也逐渐增长。在 Windows 驱动里发现我的第一个 CVE 促使我更认真地关注这个方向。差不多同一时期，我开始阅读更多关于驱动工作的实战写作，包括 eversinc33 的一篇文章，介绍如何解包一个 VMProtected kernel driver。它写得直观、动手性强，让驱动研究变得更具体。  
  
不久之后，我看到 vx-underground 发了一条推文，提到大约有 48.5 GB 的 Windows 驱动被送进 IOCTLance 进行处理。推文里没有给出结论，只有大量驱动和一大堆输出。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtibUN7ia5aLs409ia1oJD1GxXRCt1N2Yia5jj2iaRySHSQ0mLsctEh2X8jSg/640?wx_fmt=png&from=appmsg "")  
  
图 1: 点燃这一切的火花——对驱动进行规模化分析。  
  
让我一直记住的是这两端之间的落差：手工驱动分析很慢但很精确；大规模自动化推进很快，但输出往往缺乏上下文。  
  
后来我开始觉得一个更简单的想法很有意思：如果有一个系统，当你对某个驱动感到好奇时，可以把它上传，然后让它跑过一套分析流程呢？做基础分类，补一些上下文，再给出一份面向漏洞的报告，让你有个切入点。它不替代手工工作，但能让你更容易决定某个驱动是否值得投入时间。  
  
这个项目就由此而来。  
## 使用 MWDB 和 Karton  
  
沿着这个想法，我接触到了 MWDB 和 Karton。  
  
MWDB 提供了一种很直接的方式来存储样本并浏览分析结果。Karton 则通过一个简单的流水线模型补齐了自动化分析这一块——文件被推入，workers 取走并处理它们，结果再被传递到下一阶段。尽管这种组合通常用于 malware 样本，但它并不局限于 user-mode 二进制。归根结底，它就是一种把文件推过流水线并收集结构化输出的方法，同样也很适用于驱动。  
  
把 MWDB 和 Karton 组合在一起意味着：驱动只需要上传一次，就能自动处理，并集中存放，方便之后再深入探索。  
  
问题在于：我需要的服务一个都不存在。没有 worker 用于识别 Windows kernel driver；没有 worker 用于提取驱动特有的元数据；没有 worker 以适合批处理的方式运行 IOCTLance；也没有 worker 用于把结果聚合成可用的东西。所以这些服务必须自己实现。  
  
Karton 提供框架和消息传递，但分析逻辑完全在 workers 里。大部分工作都花在：如何把流水线拆成更小的阶段，以及每个阶段应该产出什么信息。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtiaRmjhGHc1wMBIGL36HCMkIJJQRj5CtDia1MXSqLKKRtjiaE5xabpQc2A/640?wx_fmt=jpeg&from=appmsg "")  
  
图 2: 高层驱动分析流水线  
## 实现流水线  
  
流水线的每个阶段都实现为一个 Karton service。每个 service 的职责都很窄，并向下一阶段输出结构化结果。  
### 文件分类  
  
第一个 service 做基础分拣 (triage)。它用简单的启发式规则和 magic bytes 来判断上传的文件是否看起来像一个 PE 二进制文件。不像 PE 的文件会在这一阶段被丢弃，以避免后续流水线做无用功。  
### 驱动识别  
  
并不是所有 PE 文件都是 kernel driver。下一个 service 会解析 PE 头，并检查一些基础属性 (例如 subsystem)，以判断该文件是否为 Windows kernel-mode 驱动。只有被确认的驱动才会继续。这一阶段的目的在于过滤，而不是验证正确性。  
### 签名与元数据提取  
  
对已确认的驱动，下一步是提取元数据。这个 service 会通过 Wine 运行 sigcheck64.exe，并提取可用信息，例如签名状态、签名者名称、产品名称、版本以及描述字符串。这些元数据不用于做安全决策；它的价值在于提供上下文，并让后续的分组与筛选成为可能。  
### IOCTL 分析  
  
IOCTL 分析阶段封装了 IOCTLance。对每个驱动，IOCTLance 会对 DriverEntry 做符号执行，定位 IOCTL dispatch routines，并探索 handler 的代码路径。目标是暴露那些常与高风险行为相关的模式，而不是完整探索每一条路径。  
  
这一阶段天生就慢且噪声多。超时与探索不完整都是预期之内。每次运行都会产出一份结构化的 JSON 报告，描述探索了什么，以及哪些路径看起来更值得关注。  
### 报告与存储  
  
最后一个 service 会聚合前面所有阶段的输出。它打上 tags，附加 artifacts，并把结果存入 MWDB。到这一步为止，就可以按元数据或分析结果去浏览与筛选驱动，从而更容易从批量导入切换到有针对性的深入分析。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtb31GibQe51IRMKtexfjdb0KJvLn3lDJ3QXQudFhAvkXN7s0wbibKjtYw/640?wx_fmt=png&from=appmsg "")  
  
图 3: MWDB 列表视图，展示已处理的驱动与基础元数据。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOej62ceNicv24nRx6jMuFdtnsaOUEYtM18KPh6S2Ania41W7XzeI5EBYFKsRbXoicV5wY1mFcFW8jSg/640?wx_fmt=png&from=appmsg "")  
  
图 4: 驱动样本页面，包含提取的元数据与分析产物。  
## 集成挑战与解决方案  
  
让流水线稳定跑起来并不只是写分析代码这么简单。把这些工具集成到一起，需要解决一些非常具体的约束问题。  
### 1. MWDB 权限与自定义元数据  
  
MWDB 对可上传的数据非常严格。默认情况下，即便是 admin 用户也可能没有权限添加自定义 tags，或动态定义新的 metadata attributes。我不得不实现一个 bootstrap 脚本来：  
- 为 admin  
group 授予诸如 adding_tags  
、adding_parents  
(用于附加分析产物时至关重要) 以及 adding_all_attributes  
等能力。  
  
- 在 reporter service 使用之前，显式注册自定义 metakeys (例如 ioctl_vuln_count  
、sig_product  
、sig_verifier  
)。没有这些注册，reporter 在尝试推送更细的上下文时，要么会静默失败，要么会记录错误日志。  
  
### 2. 产品标签化  
  
一个目标是按产品名称对驱动分组 (例如 "GeForce"、"Razer Synapse")。然而，从 PE version info 提取到的原始字符串往往很脏：有空格、特殊字符，或大小写不一致。我在 Reporter service 里实现了一个 sanitization 层，用 regex 把这些字符串规范化为合法的 MWDB tags (例如把 " Razer Synapse 3 "  
转换为 product:Razer_Synapse_3  
)。这样可以确保 tags 可点击，并且便于筛选。  
### 3. 使用 Karton 处理分析产物  
  
在 workers 之间传递大型分析结果会比较棘手。与其把完整的 IOCTLance JSON report 塞进 task payload (这可能会压垮 message broker)，我选择使用 Karton 的 resource system。IOCTLance worker 会把完整的原始报告作为一个 Resource  
附加上去，它会被高效地存储在 MinIO 中，并以引用的方式传递。随后 Reporter worker 拉取该 resource，并将其作为 analyzed sample 的 child object 上传到 MWDB。这样就建立了 parent-child 关系：主样本保持干净，同时又能在 MWDB UI 里直接查看完整的 JSON report。  
## 当前状态  
  
写这篇文章时，流水线已经在运行。各个 service 已部署并在处理输入。数十 GB 的驱动正在被上传与分析，MWDB 也在持续被结果填充。  
  
本文主要聚焦系统的设计与搭建。关于流水线规模化运行后的观察，会在 Part 2 中展开。  
  
---  
> Building a Scalable Windows Driver Vulnerability Analyzer (Part 1)  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
