#  攻击者利用Apache ActiveMQ漏洞获取RDP权限并部署LockBit勒索软件  
 FreeBuf   2026-02-26 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2AdUcQhbZXZvkVzr3Vx14f84XL7ETHtnHf00j4FBSPeia0apQbbMyoFCeBUbRDNYguO4Bq79D1PSaicVEBEUaGzWYDJEnqicjxUs/640?wx_fmt=jpeg&from=appmsg "")  
##   
  
Apache ActiveMQ 存在一个已被攻击者积极利用的高危漏洞，导致企业网络全面感染 LockBit 勒索软件。攻击者利用 ActiveMQ 消息代理中的远程代码执行漏洞（CVE-2023-46604）入侵暴露在外的 Windows 服务器，最终通过远程桌面协议（RDP）加密系统——从初始入侵到完全加密历时约 19 天。  
##   
  
**Part01**  
## 攻击过程分析  
  
  
2024 年 2 月中旬，攻击者向公开可访问的 Apache ActiveMQ 服务器发送特制的 OpenWire 命令。该漏洞利用导致服务器加载远程 Java Spring XML 配置文件，指示受感染主机使用 Windows CertUtil 实用程序下载 Metasploit 攻击载荷。执行后，攻击载荷在 IP 地址 166.62.100[.]52 的攻击者控制服务器上建立了命令与控制通道。  
  
  
获得初始立足点后 40 分钟内，攻击者已将权限提升至 SYSTEM 级别，并开始从桥头堡主机的 LSASS 进程内存中转储凭据。数字取证与事件响应（DFIR）报告分析人员发现，攻击者在入侵第二天曾被驱逐出环境，但由于易受攻击的 ActiveMQ 服务器从未打补丁，相同的利用途径仍然开放。  
  
  
首次入侵 18 天后，攻击者使用相同的 CVE-2023-46604 技术卷土重来——仅更改了漏洞利用后下载的文件名。由于在第一次入侵期间从 LSASS 内存中窃取了特权服务账户凭据，攻击者获得了直接重返网络的现成路径。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0hN0rfDGzYpiaEIcBsChA1REDoOzoYZ1ibAkPOW37ZVgnjUrNb0wot9eMk9Zr0sQlYeqfkg2slhwjoMjLkliaTjuLWMbvWiaDlzIY/640?wx_fmt=png&from=appmsg "")  
  
  
**Part02**  
## 横向移动与勒索软件部署  
  
  
攻击者重返网络后，确认了域管理员访问权限，随后运行伪装成 SoftPerfect Network Scanner 的网络扫描工具 Advanced IP Scanner，枚举环境中的活动主机。接着通过 RDP 会话将 LockBit 勒索软件可执行文件（LB3.exe 和 LB3_pass.exe）转移到服务器和工作站。  
  
  
在文件和备份服务器上，勒索软件通过特定路径和密码参数执行，而在其他主机上则通过 Windows 资源管理器界面简单双击运行。勒索说明引导受害者使用 Session 私密消息应用而非官方 LockBit 基础设施，表明这是使用泄露的 LockBit Black 构建器制作勒索软件的独立攻击者。  
  
  
从首次漏洞利用到完全加密的总时间为 419 小时（约 19 天）。如果防御者未检测到初始入侵阶段，攻击者从重返网络到勒索软件开始执行只需不到 90 分钟。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2BTcRPsXO81KQhJXFDFG9YtdtrCe0a3IIUx0OG44VctWSGicuoDh5zF0ib1rg6OE7nnDNZ5rrukgEtk414CJNLL2VpNzCQSroWg/640?wx_fmt=png&from=appmsg "")  
  
  
**Part03**  
## 凭据窃取推动横向移动  
  
  
在获得 SYSTEM 级别访问权限后，Metasploit 进程在第一轮入侵期间访问了四台主机的 LSASS 进程内存。Sysmon 日志捕获了 GrantedAccess 值为 0x1010（授予虚拟内存读取权限）以及 CallTrace UNKNOWN 条目——这是注入代码执行转储而不留下标准进程痕迹的可靠指标。  
  
  
其中一台目标主机运行着与特权服务账户关联的生产应用程序，该账户成为 18 天后攻击者重返网络的桥梁。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2dtTNoJCyybibwx30kUu95WDhKaCma3pwdM64ZRfWkywTMLooicvdfGeiabWkJhrmdhfQkjyUloO7AWHIykRDOGbsAbXyo9dEFiaE/640?wx_fmt=jpeg&from=appmsg "")  
  
  
攻击者在第 18 天重返时，使用窃取的服务账户在域控制器和多台服务器上远程创建服务并运行 Metasploit 载荷。这些载荷通过字符串连接、Base64 编码和 gzip 压缩层层混淆。解码后，shellcode 使用 VirtualAlloc 分配内存区域，通过 VirtualProtect 更改保护属性为可执行，然后生成线程执行内存中注入的载荷——这是避免触发基于签名的终端检测的常用方法。  
  
  
**Part04**  
## 痕迹清楚与持久化  
  
  
为掩盖行踪并维持立足点，攻击者在桥头堡主机上静默安装 AnyDesk，将其设置为自动启动服务。名为 rdp.bat 的批处理文件打开防火墙 3389 端口允许 RDP 连接，执行约六分钟后被删除。桥头堡主机上的 Windows 系统、应用程序和安全事件日志全部被清除，攻击者还在 Exchange 服务器上滥用 LOLBIN SystemSettingsAdminFlows.exe 禁用 Windows Defender。  
  
  
![AnyDesk 静默安装及与 166.62.100[.]52 的 C2 连接（来源：The DFIR Report）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0Mf80Me2cAX0AdnKLMdf7pI9EjdxlVCDN5LVKkZxibZZ718tCubkKXzrXibwTp6gUicDcGnNw1jtrQ6By1eNgiaPFTnOf4cZ8oRUY/640?wx_fmt=jpeg&from=appmsg "")  
  
  
**Part05**  
## 入侵指标（IOC）  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1eYOeCj58ahibp4UhYw2QFwQnfdbJs2fDjuJPEKEZvDvFcqfaRHKhpQA6ZcCibGyw0CibawrxkNSTOu3Sqj7HER9Js5bWCTObDB4/640?wx_fmt=png&from=appmsg "")  
  
  
企业应立即修补 Apache ActiveMQ 以解决 CVE-2023-46604 漏洞，通过 Credential Guard 加强 LSASS 保护，监控事件日志清除活动，限制未经授权的远程访问工具安装，并在任何可疑入侵后重置所有凭据以防止通过被盗账户重新入侵。  
  
  
**参考来源：**  
  
Threat Actors Exploit Apache ActiveMQ Server Vulnerability to Gain RDP Access and Deploy LockBit Ransomware  
  
https://cybersecuritynews.com/threat-actors-exploit-apache-activemq-server-vulnerability/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335325&idx=1&sn=9ed0ec9935e791c0508c4ec1526dbf72&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
