#  黑客利用 telnetd 身份验证绕过漏洞获取 root 权限  
原创 ZM
                    ZM  暗镜   2026-01-25 01:00  
  
已发现有针对 GNU InetUtils telnetd 服务器中存在 11 年之久的严重漏洞的协同攻击活动，该漏洞最近才被披露。  
  
该安全问题编号为 CVE-2026-24061，于 1 月 20 日报告。该漏洞很容易被利用，并且有多个漏洞利用示例已公开。  
  
该漏洞自 2015 年以来一直存在  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt89zcsSpzdKiaE0aj0Es7lWSP6Olb7rZ5OZcBtS3AvcdBPayAuIk3zAT2wibhCpGqddrbWazj2KEkww/640?wx_fmt=png&from=appmsg "")  
  
  
开源贡献者Simon Josefsson 解释说，GNU InetUtils 的 telnetd 组件存在远程身份验证绕过漏洞，这是由于在生成“/usr/bin/login”时未清理环境变量处理造成的。  
  
该漏洞的产生是因为 telnetd 会将用户控制的 USER 环境变量直接传递给 login(1) 函数，而没有进行任何清理。攻击者可以通过将 USER 设置为-f root并使用 telnet -a命令连接，从而绕过身份验证并获得 root 权限。  
  
该问题影响 GNU InetUtils 版本 1.9.3（2015 年发布）至 2.7，并在版本 2.8 中进行了修复。对于无法升级到安全版本的用户，缓解策略包括禁用 telnetd 服务或在所有防火墙上阻止 TCP 端口 23。  
  
GNU InetUtils是由 GNU 项目维护的一系列经典网络客户端和服务器工具（telnet/telnetd、ftp/ftpd、rsh/rshd、ping、traceroute），并在多个 Linux 发行版中使用。  
  
尽管 Telnet 是一种不安全的旧式组件，并且已被 SSH 基本取代，但许多 Linux 和 Unix 系统仍然保留它，以兼容其他系统或满足特殊用途的需求。由于其简单易用且开销低，Telnet 在工业领域尤其普遍。  
  
在传统设备和嵌入式设备上，它可以无需更新运行超过十年，这解释了它在物联网设备、摄像头、工业传感器和运营技术 (OT) 网络中的应用。  
  
Zerotak 是一家渗透测试和网络安全服务公司，其负责人Cristian Cornea告诉 BleepingComputer，在 OT/ICS 环境中，关键系统很难被替换。  
  
研究人员表示，有时这是不可能的，因为升级会伴随重启操作。“因此，我们仍然会遇到运行 Telnet 服务器的系统，即使尝试用更安全的协议（例如 SSH）替换它们，由于遗留系统仍在运行，这也不可行。”  
  
一些技术用户仍然依赖 Telnet 来完成某些项目：另一位用户证实，使用 telnet 连接到早已“停止支持”的旧款 Cisco 设备也存在同样的 SSH 问题。  
  
然而，在公共互联网上暴露的、仍然启用 Telnet 的设备很少，这促使许多研究人员认为 CVE-2026-24061 漏洞的严重性较低。  
  
威胁监控公司GreyNoise 报告称，已检测到利用 CVE-2026-24061 漏洞对少量易受攻击的终端进行实际攻击活动。  
  
记录于 1 月 21 日至 22 日期间的活动来自 18 个不同的攻击者 IP 地址，通过 60 个 Telnet 会话发起，所有会话均被认定为 100% 恶意，共发送了 1,525 个数据包，总计 101.6 KB。  
  
这些攻击利用 Telnet IAC 选项协商机制注入“USER=-f <user>”参数，从而在未经身份验证的情况下授予 shell 访问权限。GreyNoise 表示，大部分攻击活动似乎是自动化的，但也发现了一些“人工操作”的案例。  
  
攻击的终端速度、类型和 X11 DISPLAY 值各不相同，但在 83.3% 的情况下，它们的目标是“root”用户。  
  
在渗透后阶段，攻击者进行了自动化侦察，并试图持久化 SSH 密钥和部署 Python 恶意软件。GreyNoise 报告称，由于缺少二进制文件或目录，这些尝试在被观察到的系统中均告失败。  
  
虽然此次攻击活动的范围和成功程度似乎有限，但在攻击者优化其攻击链之前，应按照建议对可能受影响的系统进行修补或加固。  
  
  
  
  
