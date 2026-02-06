#  利用 LLM 加速漏洞挖掘：我是如何在 Scada-LTS 中发现 Stored XSS 并拿到人生第一个 CVE 的  
haidragon
                    haidragon  安全狗的自我修养   2026-02-06 06:54  
  
# 官网：http://securitytech.cc  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnu0RibsgJibRSpzbmJCxLVH5AmNWXYF3LwPFu8SgO0XcibTvc9WjxxfoKzNCSKg7p01FFmA0Rbqn50pBnUQKrX3mjRdZ1usm8NeDk/640?wx_fmt=png&from=appmsg "")  
## 📌 引言  
  
我最初是在准备一份关于漏洞挖掘的培训材料。与其只做 PPT、用传统工具，我决定做一次真实实验，使用我最喜欢的一些**大语言模型（LLMs）**  
。  
  
具体来说，我组合使用了 **ChatGPT 5 + GitHub Copilot**  
。目标是看看这些工具在真实世界漏洞的**初筛、分析与利用**  
流程中，究竟能加速多少。  
  
结果非常惊人：  
  
原本需要我**几天**  
做的人工审计、静态分析和动态测试，我在**大约 3 小时内完成**  
了。  
  
期间我在 Scada-LTS  
  
 中验证了 **3 个 Stored XSS 漏洞**  
，提交到 VulDB，并最终注册为 CVE。这对我来说也是一个里程碑：**我的第一个 CVE。**  
## 🔧 Fork Scada-LTS 与 Semgrep 初步筛选  
  
实验的起点是从 GitHub fork Scada-LTS 项目。  
  
Scada-LTS 是一个用于工业环境的开源 **SCADA / ICS 平台**  
，非常适合作为测试对象。Fork 完成后，我把代码库接入了 Semgrep  
  
 —— 一个能够高亮不安全编码模式的静态分析工具。  
  
Semgrep 标出了多个热点位置，包括：  
- XML 解析器中的潜在 XXE  
  
- JavaScript 中不安全的 innerHTML  
  
- Java 中的路径遍历  
  
- 拼接格式化 SQL 字符串  
  
这些都是非常适合深入分析的候选点。  
  
与其手动逐条检查，我直接把这些标记行作为入口，交给 ChatGPT 继续深入分析。  
> 点击查看大图  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnsffpPibFSgPUJ79CYLLMiaH4CpJ3WngiciaAky1OQnPAmohUzfMsvc7P7AGmwLMd2c2dEB9SxfP5Ug66KHCr0VXl45FkNy6icsAMjw/640?wx_fmt=png&from=appmsg "")  
  
Semgrep 输出的潜在问题位置  
## 💻 ChatGPT 连接终端环境  
  
我在 macOS 上配置了 ChatGPT 5 App，并让它直接连接我的终端（MacOS App 的一个特性）。终端中运行的是 Kali Linux，但不是原生，而是通过 Exegol  
  
 容器环境模拟。  
  
Exegol 配合 Orb  
  
 栈提供编排支持，能够快速启动，具备：  
- 加速网络  
  
- Rosetta x86 模拟  
  
- VirtioFS 文件共享  
  
- 多项性能优化  
  
这让我在 ARM 主机上也能得到近似原生性能的 x86_64 Kali。  
> 点击查看大图  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvrdcicicHHwibhQYZ7TyMj8nkCNAVRX3nzL4VYQzhqEjrQUm2dfxR5Wuca40K0TtbCY2BDlg72bKzEMtEsfBic3aJ5QNvFuf5LvnU/640?wx_fmt=png&from=appmsg "")  
  
Exegol Kali x86_64 启动  
  
通过这种集成方式，我可以直接让 ChatGPT：  
- 给出终端命令建议  
  
- 查找代码引用  
  
- 解析输出结果  
  
- 将 Semgrep 命中点与真实代码路径关联  
  
整个流程是**迭代式的**  
：  
  
Semgrep → ChatGPT → 精准搜索 → ChatGPT 再分析。  
  
其中一个效率提升点是：我用 ripgrep  
  
 替代了 grep。  
  
ripgrep 的优势：  
- 默认递归  
  
- 自动跳过 .gitignore  
  
- 速度更快  
  
- 高亮更清晰  
  
这样可以在几分钟内，把成千上万行结果过滤成少量热点。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnvzJGXibea7bY8VlNnhDJBZxiah4N010szDtia8r91eYuCBr13r2Cxicc3dOvahG42mex2kiaPwlFaWhyDp6iaW976laOqLh6sV7vRwI/640?wx_fmt=png&from=appmsg "")  
  
ChatGPT 直接检查终端输出  
## 🤝 ChatGPT + Copilot 组合拳  
  
ChatGPT 用来**引导调查与提出假设**  
，而 GitHub Copilot 则非常适合做**验证工作**  
。  
  
Copilot 可以访问整个仓库的上下文，帮助确认 Semgrep 标出来的路径：  
- 是否真的可利用  
  
- 还是只是误报  
  
例如 Copilot 确认：  
  
虽然 XML 中允许 DOCTYPE，但外部实体被禁用，因此远程 XXE 不太可能，但仍可能触发 **Billion Laughs DoS**  
。  
  
这种组合方式：  
> ChatGPT 探索 + Copilot 验证  
  
  
极大加速了分析。  
> 点击查看大图  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntib6V2d1XHIcraibL85F5fVDibKQWHCIW4zDibsriaNsZLOFS9KUHVd6Y0qgibrf93lsF60WooM4lbJ9VmvtgGiazApNy6c8IQXX5FbE/640?wx_fmt=png&from=appmsg "")  
  
使用 Copilot 进行二次确认  
## 🔍 填充应用数据并验证漏洞  
  
定位完热点之后，就要进入动态测试阶段。  
  
问题是：Scada-LTS 需要大量配置数据才能正常跑起来，手动填会花好几个小时。  
  
借助 ChatGPT Agent Mode，我查到了一个可以直接导入的**示例项目**  
，可以快速填充真实数据点、事件和报表。  
  
导入后，我开始系统性测试字段。  
  
第一个成功的利用点来自：  
```
data_point_edit.shtm
```  
  
Payload：  
```
<imgsrc=xonerror=alert(1)>
```  
  
我在 **Data Point Name**  
 字段实现了 Stored XSS。  
  
随后又在：  
- Data Source Edit  
  
- Reports 模块（Colour 字段）  
  
发现了第二、第三个漏洞。  
  
每个都能成功弹窗。  
  
这验证了 Semgrep 最初发现的：  
- 不安全 innerHTML  
  
- 未转义 JSP 表达式  
  
确实可以被利用。  
> 点击查看大图  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBntmSxyvHicUMiad0KCC4I9pCh1ECvUmm28WakPY6RuoT6yvHPeGiaBNcoumpiciasNzmzcD1rW2sQaCM8aH4bStcYDdXJG4HSlsw1oY/640?wx_fmt=png&from=appmsg "")  
  
漏洞验证成功  
## 🆔 从 VulDB 到 CVE  
  
为了正式发布漏洞，需要和 **CVE Numbering Authority（CNA）**  
 合作。  
  
CNA 是由 CVE.org  
  
 授权的机构，负责验证漏洞并分配 CVE ID。  
  
如果厂商没有自己的 CNA，可以使用独立 CNA，例如 **VulDB**  
 或 MITRE。  
  
我选择了 **VulDB**  
，因为它：  
- 快  
  
- 稳定  
  
- 分析可信  
  
流程非常清晰。  
  
发布流程如下：  
1. **提交报告**  
：向 VulDB 提交完整漏洞文档。  
  
1. **验证确认**  
：检查影响、重复性、标准符合度，并进行厂商协调披露。  
  
1. **分配 CVE**  
：其中三个漏洞合并后生成  
**CVE-2025-10234、CVE-2025-10235**  
。  
  
1. **公开登记**  
：VulDB 提交到 CVE.org 公布。  
  
> 点击查看大图  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnvnUCXfcPZraoS04aP3nNTx1bUn4g8b2iaIZibXg1fUjgpicTxk50pCc3s8jgpObU7FQIWibm54lbQIROibLaxpY9lXZS8FD79viaIzE/640?wx_fmt=png&from=appmsg "")  
  
VulDB 控制台  
## ⏱ 时间线与总结  
  
整个流程：  
```
Semgrep → ChatGPT/Copilot → 利用 → CVE 注册
```  
  
总共只用了 **约 3 小时**  
。  
  
而传统方式通常需要好几天。  
  
这个实验说明：  
> LLM 并不是取代人类，而是在**放大人的能力**  
。  
  
  
它们可以：  
- 减少噪音  
  
- 聚焦真正问题  
  
- 加速研究流程  
  
- 提高质量  
  
- 节省时间去打游戏 🎮  
  
## 🧠 总结一句话  
> 以前：人工 + 工具  
  
现在：人工 × LLM  
  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
##   
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vBZcZNVQERGMBGbdxsdiaj8ZUicr210FQ092YpsgXmyaqwxqPcvPlLaxq84Ndm9Anx4IKy9ibuvaC5s4HFrpTw1ew/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=15 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
