#  Android 安全更新——修复 129 个漏洞及一个正在被利用的零日漏洞  
 网安百色   2026-03-04 10:37  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnum2WYRjcKn4Lup4yPyiciaOogPoztqTQmD4x90j1SkalPf4uw0fyd4Hia23YicYfpU8vENxfzICIUVfRGqGiclc5aibzENnpic6KRMYc/640?wx_fmt=jpeg&from=appmsg "")  
# Android 安全更新：修复 129 个漏洞并封堵一个正在被利用的零日漏洞  
  
Google 正式发布 2026 年 3 月 Android 安全公告（Android Security Bulletin），一次性修复了横跨 Android 生态系统的 129 个安全漏洞。这是近年来单月补丁数量最多的更新之一，反映出当前移动安全威胁态势的复杂性与严峻性。  
  
本次更新采用双补丁级别发布机制：2026-03-01 与 2026-03-05。该分级策略允许设备厂商优先修复核心 Android 平台漏洞，再逐步解决涉及硬件厂商的复杂组件问题，从而提升整体响应效率。  
## 正在被利用的零日漏洞：CVE-2026-21385  
  
此次更新的核心焦点是 CVE-2026-21385。这是一个位于 Qualcomm 开源显示组件（Qualcomm Display）中的高危零日漏洞。  
  
从技术层面分析，该漏洞源于整数溢出（Integer Overflow）或整数回绕问题，在内存分配对齐过程中触发内存损坏（Memory Corruption）。攻击者若成功利用该缺陷，可能突破系统安全边界，操控关键内存结构。  
  
**漏洞信息概览：**  
- CVE 编号：CVE-2026-21385  
  
- 严重等级：高危  
  
- 受影响组件：Qualcomm Display  
  
- 漏洞类型：整数溢出导致内存损坏  
  
- 潜在影响：系统不稳定、权限绕过、设备被攻陷  
  
- 修复状态：已于 2026 年 3 月补丁中修复  
  
- 利用情况：存在有限且定向的在野利用  
  
Google 与 Qualcomm 均确认，该漏洞已在有限的针对性攻击中被利用。由于漏洞位于硬件显示驱动层，其攻击面更接近底层系统，风险显著高于普通应用层漏洞。  
  
使用受影响 Qualcomm 芯片组的 Android 设备用户应立即安装安全更新，以降低被攻击风险。  
## 核心系统关键漏洞：无需用户交互即可利用  
  
在 2026-03-01 补丁级别中，Google 修复了多个无需用户交互即可触发的关键漏洞。  
  
其中最严重的是：  
### CVE-2026-0006 —— 远程代码执行（RCE）  
  
该漏洞存在于 Android 核心 System 组件中。攻击者可在无需额外执行权限的情况下远程运行恶意代码。一旦利用成功，可能直接获取系统级控制权。  
### CVE-2026-0047 —— 权限提升（EoP）  
  
该漏洞位于 Android Framework 组件中，属于严重级别的权限提升漏洞。  
  
权限提升漏洞在高级攻击中极具价值。攻击者常将其与 RCE 漏洞组合利用，从而实现：  
- 绕过应用沙箱机制  
  
- 获取系统级或管理员权限  
  
- 建立持久化控制  
  
这类漏洞往往是完整攻击链中的关键环节。  
## 厂商组件与硬件层漏洞风险  
  
2026-03-05 补丁级别主要针对第三方硬件组件漏洞，共修复 66 个问题，涉及闭源与开源组件。  
  
部分典型漏洞包括：  
- CVE-2025-48631 —— System 组件拒绝服务（DoS）  
  
- CVE-2024-43859 —— Kernel（F2FS）权限提升  
  
- CVE-2026-0037 —— Kernel（pKVM）权限提升  
  
Google 与多家芯片厂商合作修复漏洞，包括：  
- Arm  
  
- Imagination Technologies  
  
- MediaTek  
  
- Unisoc  
  
这些漏洞广泛存在于调制解调器（Modem）、GPU 驱动、虚拟机监控器（Hypervisor）等底层组件中，凸显移动设备供应链安全的复杂性。  
  
硬件层漏洞一旦被利用，往往更难检测与清除，也更容易绕过传统安全防护机制。  
## 安全防护建议  
### 1. 检查补丁级别  
  
用户应在“系统设置 → 关于手机 → Android 安全补丁级别”中确认设备是否运行 2026-03-05 补丁级别。  
  
达到 2026-03-05 的设备将获得：  
- 本次公告中全部 129 个漏洞的完整修复  
  
- 以及此前安全公告中的所有修复内容  
  
### 2. 关注 AOSP 更新  
  
Google 将在 48 小时内将相关补丁代码提交至 Android Open Source Project（AOSP）仓库，以确保生态系统长期稳定。  
### 3. 启用 Google Play Protect  
  
对于集成 Google Mobile Services 的设备，Google Play Protect 仍作为实时防御层运行，可持续检测并阻止试图利用新漏洞的恶意应用。  
## 总结：移动安全进入持续高强度对抗阶段  
  
本次 129 个漏洞的集中修复，以及零日漏洞已被在野利用的事实，表明移动安全威胁正在向更底层、更复杂的攻击链演进。  
  
本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1 "")  
  
