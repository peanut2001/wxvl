#  什么是自带漏洞驱动 (BYOVD) 攻击?  
Umut Bayram
                    Umut Bayram  securitainment   2026-03-03 05:38  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://www.picussecurity.com/resource/blog/what-are-bring-your-own-vulnerable-driver-byovd-attacks</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Umut Bayram</span></section></td></tr></tbody></table>  
**BYOVD (Bring Your Own Vulnerable Driver) 攻击**  
是一种 Windows 内核利用技术，攻击者将合法且经过数字签名、但存在已知漏洞的驱动程序加载到目标系统中，随后利用该驱动的漏洞获得任意内核模式 (Ring 0) 执行权限——这是 Windows 中的最高特权级别。  
  
借助内核级访问权限，攻击者能够终止 EDR 进程、禁用安全工具、篡改内核回调并绕过终端防护措施。由于所加载的驱动程序本身是受信任且已签名的，BYOVD 实质上是在滥用 Microsoft 的驱动信任模型来规避安全防御。  
  
在 MITRE ATT&CK 框架中，BYOVD 对应 **T1068 - 利用漏洞进行权限提升**  
，并常与 **T1562.001 - 削弱防御：禁用或修改工具**  
存在交叉。该技术已成为勒索软件组织和 APT 组织实现隐蔽提权与防御规避的常用手段。  
## BYOVD 攻击的工作原理：技术流程逐步解析  
  
在 **BYOVD 攻击**  
中，拥有管理员权限的威胁行为者会将一个合法且经过数字签名、但包含已知漏洞的驱动程序安装到目标系统上。攻击者通过利用这些驱动漏洞，获取关键的**内核级访问权限**  
，从而绕过或禁用 EDR 和杀毒软件等终端安全控制措施。  
  
以下是典型 BYOVD 攻击的完整流程：  
  
![从初始访问到载荷部署的攻击链流程](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSggeuILeJAFxfoZJftDk0hMBMk00adGibmX4PZVM4FUSicSiauFZOiakrhsXF1GJ4ARczNH7616xc4uGYJdZoj5dKyN1t0w5Hl2TVY/640?wx_fmt=png&from=appmsg "")  
  
从初始访问到载荷部署的攻击链流程  
  
从初始访问到载荷部署的攻击链流程  
### 步骤 1: 攻击者在执行 BYOVD 之前获取管理员权限  
  
BYOVD 并非初始访问技术，它要求攻击者已经拥有目标系统的**本地管理员权限**  
。这些权限通常通过**钓鱼攻击**  
、利用**面向公网的应用程序**  
漏洞或从**初始访问代理商**  
处购买等方式获得。  
### 步骤 2: 将漏洞驱动文件释放到磁盘  
  
攻击者将 **.sys 文件**  
(漏洞驱动) 放置在可写目录中，例如 **C:WindowsTemp**  
或 **C:UsersPublic**  
。该驱动通常是合法软件，往往直接来源于**厂商自身的安装程序**  
，因此更难被检测发现。  
### 步骤 3: 在 Windows 中注册并加载漏洞驱动  
  
攻击者通过 **Windows 服务控制管理器**  
注册并加载漏洞驱动，使用的命令如下：  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf=""><br/></span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">sc.exe create vuln_driver type= kernel binPath= C:\Windows\Temp\vulnerable_driver.sys </span><br style="margin-top: 0px;margin-bottom: 0px;"/><span leaf="">sc.exe start vuln_driver</span></section></td></tr></tbody></table>  
或通过 **NtLoadDriver**  
API 以编程方式完成。  
### 步骤 4: 通过构造 IOCTL 请求利用驱动漏洞  
  
驱动加载完成后，攻击者通过 **DeviceIoControl**  
调用与其进行交互，向驱动发送特定的 **I/O 控制码**  
以触发漏洞。  
  
例如，**RTCore64.sys**  
暴露的 IOCTL 代码可实现对物理内存和虚拟内存的任意**读/写**  
操作。  
### 步骤 5: 利用内核权限禁用终端安全工具  
  
凭借**内核访问权限**  
，攻击者使用**读/写原语**  
逐一枚举并移除系统中注册的所有 **EDR 回调**  
，随后终止 **EDR 的用户模式进程**  
，使终端彻底失去防御能力。  
### 步骤 6: 绕过防御后部署主载荷  
  
成功绕过安全防御后，攻击者在已无防护的系统上部署**勒索软件**  
、**数据窃取工具**  
或其他**持久化机制**  
，整个过程不受任何安全措施干扰。  
## 真实 BYOVD 攻击案例：Genshin Impact 驱动滥用事件  
  
某勒索软件攻击者利用了热门角色扮演游戏 Genshin Impact (原神) 中存在漏洞的反作弊驱动 **mhyprot2.sys**  
1  
。  
  
攻击者通过**远程桌面协议**  
(**RDP**  
) 使用被入侵的**管理员账户**  
连接到域控制器，并向系统桌面传输了两个关键文件：第一个是 **mhyprot2.sys**  
，一个合法且经过数字签名的 Genshin Impact 反作弊驱动; 第二个是名为 **kill_svc.exe**  
的恶意可执行文件。  
  
攻击者运行 **kill_svc.exe**  
启动绕过流程。该文件将漏洞驱动 **mhyprot2.sys**  
安装为名为 **mhyprot2**  
的服务。  
  
驱动激活后，**kill_svc.exe**  
扫描系统中特定的杀毒进程列表，如 **uiWatchDog.exe**  
和 **TmWSCSvc.exe**  
，并通过 **DeviceIoControl**  
函数将目标列表传递给漏洞驱动。在此步骤中，该可执行文件向驱动发送了控制码 **0x81034000**  
。  
  
控制码 **0x81034000**  
指示 **mhyprot2.sys**  
驱动终止指定进程。由于该驱动以 Ring 0 内核权限运行，它成功调用 **ZwTerminateProcess**  
函数终止了杀毒软件，绕过了标准的用户模式防护。  
  
终端防护被完全禁用后，攻击者启动了名为 **svchost.exe**  
的勒索软件载荷，随即开始加密文件。  
## 为什么 BYOVD 攻击能如此有效地规避防御？  
  
BYOVD 之所以有效，是因为它利用了 Windows 建立内核代码信任机制中的结构性缺陷。  
### 数字签名问题  
  
要理解攻击者如何利用驱动信任机制，需要先了解 Microsoft 如何保护 Windows 内核。自 Windows 10 起，Microsoft 要求所有新的内核模式驱动必须通过 Dev Portal 提交，以获得 Microsoft 的直接数字签名。  
  
此前，开发者可以使用第三方 "cross-certificates" (交叉证书) 自行签署驱动，无需 Microsoft 显式签名。为避免破坏数百万依赖旧版签名的遗留设备，Windows 无法全面拒绝这些驱动。  
  
如果系统满足以下任一条件，Windows 将继续允许加载交叉签名的驱动：  
- **旧版证书：**  
驱动使用 2015 年 7 月 29 日之前签发的终端实体证书进行签名 (前提是该证书链回到经批准的交叉签名证书颁发机构)。  
  
- **Secure Boot 已禁用：**  
计算机 BIOS 已配置为关闭 Secure Boot。  
  
- **升级系统：**  
机器运行的是 Windows 10 1607 版本，但该版本是通过从旧版 Windows 升级而来，而非全新安装。  
  
这些向后兼容性例外恰恰创造了 BYOVD 攻击所利用的漏洞。由于 Windows 仍然信任这些旧的、有效签名的驱动，威胁行为者无需伪造或窃取新的 Microsoft 签名即可获得内核级访问权限。  
### 为什么 Microsoft 的漏洞驱动阻止列表无法阻止 BYOVD 攻击  
  
任何阻止列表最根本的缺陷在于它是被动式的。驱动只有在漏洞被发现、上报之后——往往是在野外已被利用之后——才会被加入列表。攻击者深知这一点，并持续搜寻新的、冷门的或被遗忘的驱动。  
  
要使阻止列表能有效应对快速转换策略的威胁行为者，就必须持续更新。然而，Microsoft 的漏洞驱动阻止列表通常随 Windows 操作系统主要版本一同更新 (通常每年仅 1-2 次)。  
### 为什么 EDR 自我保护机制不够充分  
  
大多数 EDR 供应商都实现了防篡改保护，以防止其进程和驱动被终止。但防篡改保护与攻击者加载的漏洞驱动运行在同一特权级别 (Ring 0)。如果**基于虚拟化的安全**  
(**VBS**  
) 等缓解措施被禁用，一旦攻击者获得任意内核读/写权限，他们可以：  
- 在内存中修补防篡改保护检查  
  
- 在 **PspNotifyEnableMask**  
和**回调数组**  
处移除 EDR 的回调注册  
  
- 直接操纵 **EPROCESS**  
结构以隐藏自身进程  
  
## 如何预防和检测 BYOVD 攻击 (缓解策略)  
  
防御 BYOVD 需要采用纵深防御策略，因为没有任何单一措施能够独立应对。以下是一份实用且按优先级排序的防御方案。  
### 启用受 Hypervisor 保护的代码完整性 (HVCI)  
  
HVCI (Hypervisor-Protected Code Integrity) 利用 Windows 虚拟化技术来强制实施内核代码完整性。它将代码完整性检查转移到主操作系统内核无法访问或修改的安全隔离环境中。这意味着即使攻击者获得了内核级访问权限，也无法篡改代码完整性的执行过程本身。  
  
任何驱动或内核模块在运行前都必须经过签名验证。未签名或签名无效的代码在执行前即被阻止。Hypervisor 作为位于操作系统之下的守门人，仅仅攻破操作系统并不足以绕过它。  
  
即使攻击者拥有合法但存在漏洞的签名驱动，HVCI 的内存保护机制也能阻止未授权进程对内核内存的写入，从而限制该驱动可被利用的范围。  
#### 如何启用 HVCI?  
  
**通过组策略：**  
Computer Configuration > Administrative Templates > System > Device Guard > Turn On Virtualization Based Security > Virtualization Based Protection of Code Integrity: **Enabled with UEFI lock.**  
  
**通过注册表：**  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf=""><br/></span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">reg add &#34;HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard&#34; /v &#34;EnableVirtualizationBasedSecurity&#34; /t REG_DWORD /d 1 /f </span><br style="margin-top: 0px;"/><span leaf="">reg add &#34;HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard&#34; /v &#34;RequirePlatformSecurityFeatures&#34; /t REG_DWORD /d 1 /f </span><br/><span leaf="">reg add &#34;HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard&#34; /v &#34;Locked&#34; /t REG_DWORD /d 0 /f </span><br/><span leaf="">reg add &#34;HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity&#34; /v &#34;Enabled&#34; /t REG_DWORD /d 1 /f </span><br style="margin-bottom: 0px;"/><span leaf="">reg add &#34;HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity&#34; /v &#34;Locked&#34; /t REG_DWORD /d 0 /f</span></section></td></tr></tbody></table>  
**通过 PowerShell 验证状态：**  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf=""><br/></span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard \| Select-Object VirtualizationBasedSecurityStatus, SecurityServicesRunning</span></section></td></tr></tbody></table>  
**VirtualizationBasedSecurityStatus**  
的值为 "**2**  
" 表示**基于虚拟化的安全**  
(**VBS**  
) 已启用并正在运行。  
  
**SecurityServicesRunning**  
的值为 "**{2}**  
" 表示 **HVCI**  
正在运行。  
### 通过特定事件 ID 监控驱动加载事件  
  
以下是需要收集和告警的关键事件：  
- **Sysmon 事件 ID 6 (驱动加载):**  
记录每次驱动加载的哈希值、签名状态和路径。这是检测 BYOVD 最重要的单一事件。  
  
- **系统事件 ID 7045 (服务安装):**  
记录新服务 (包括通过 **sc.exe**  
注册的内核驱动) 的安装。  
  
- **Sysmon 事件 ID 1 (进程创建):**  
捕获用于注册驱动的 **sc.exe create**  
命令行。  
  
可使用以下 Sysmon 配置片段来排除可信驱动加载：  
```
<Sysmonschemaversion="4.90">
<EventFiltering>
<DriverLoadonmatch="exclude">
<!-- Exclude known-good Microsoft drivers if needed to reduce noise -->
</DriverLoad>  
</EventFiltering>  
</Sysmon>
```  
### 加固管理员权限  
  
BYOVD 需要本地管理员权限。减少拥有管理员访问权限的账户数量是最具影响力的控制措施之一。  
## 要点总结  
- BYOVD 是一种 Windows 内核利用技术，攻击者通过加载合法且经过数字签名、但存在漏洞的驱动来获得 Ring 0 (内核级) 访问权限。  
  
- 获得内核访问权限后，攻击者可以禁用 EDR、篡改安全回调、终止杀毒进程并绕过终端防护。  
  
- BYOVD 并非初始访问技术，它需要攻击者已具备管理员权限。  
  
- 该技术对应 MITRE ATT&CK T1068 (利用漏洞进行权限提升)，并常与 T1562.001 (削弱防御：禁用或修改工具) 存在交叉。  
  
- 攻击者利用 Windows 驱动信任和数字签名执行模型中的弱点，包括遗留签名驱动和阻止列表的缺口。  
  
- 有效防御需要纵深防御策略，包括：  
  
- 受 Hypervisor 保护的代码完整性 (HVCI)  
  
- 监控驱动加载事件 (如 Sysmon 事件 ID 6)  
  
- 特权访问加固  
  
- 组织不应假设防护措施正在有效运行，必须针对 BYOVD 等真实攻击技术持续验证安全控制措施。  
  
- 安全控制验证由攻击和入侵模拟提供支持，使团队能够安全地测试预防和检测控制措施、发现缺口，并在攻击者利用之前应用可操作的缓解指导。  
  
## 参考文献  
  
1  
"Ransomware Actor Abuses Genshin Impact Anti-Cheat Driver to Kill Antivirus," Trend Micro. Accessed: Feb. 17, 2026. [Online]. Available: https://www.trendmicro.com/en_us/research/22/h/ransomware-actor-abuses-genshin-impact-anti-cheat-driver-to-kill-antivirus.html  
  
---  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
