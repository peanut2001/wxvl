#  针对 Windows 错误报告的 ALPC 权限提升漏洞利用程序已发布  
原创 网络安全9527
                    网络安全9527  安全圈的那点事儿   2026-03-03 04:17  
  
最近，随着概念验证 (PoC) 漏洞利用程序的公开发布，一个影响 Microsoft Windows 的严重本地权限提升 (LPE) 漏洞被曝光。  
  
该安全漏洞编号为 CVE-2026-20817，存在于 Windows 错误报告 (WER) 服务中。  
  
该漏洞允许具有低权限的已认证用户以完整的 SYSTEM 权限执行任意恶意代码。  
  
详细的研究和相应的 C++ PoC 漏洞利用程序由安全研究员 @oxfemale（在 X/Twitter 上也称为 @bytecodevm）发布在 GitHub 上。  
  
此次发布凸显了Windows进程间通信错误报告机制中存在的重大安全漏洞。  
  
该漏洞的核心在于高级本地过程调用（ALPC）协议。  
  
WER 服务公开了一个名为 \WindowsErrorReportingService 的特定 ALPC 端口，以便与其他进程进行通信。  
  
根据研究人员的发现，该缺陷具体存在于 SvcElevatedLaunch 方法中，具体方法编号为 0x0D。WER 服务完全无法正确验证调用用户的权限。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7NCX0eiaHBQQ12icfia4UsWxP1FwEClrkFLuSpWBBIB5XubCKBBHn9LeCvQibC9GQUghq6s0xkqrIHvcjKMl7qSoQu7yeYVrRRHlIY/640?wx_fmt=png&from=appmsg "")  
  
因此，攻击者可以 使用从共享内存块提供的自定义命令行参数强制服务启动 WerFault.exe 。  
## 漏洞利用执行步骤  
  
要成功触发漏洞，攻击者只需遵循以下一系列简单的操作：  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf="">动作</span></section></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">描述</span></font></font></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">创建共享内存</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">创建一个包含任意恶意命令行信息的共享内存块。</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">连接至 WR ALPC 端口</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">建立与 Windows 错误报告 (WER) ALPC 端口的本地连接。</span></font></font></td></tr><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">发送 ALPC 消息（方法 0x0D）</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">使用方法 0x0D 发送 ALPC 消息，包括客户端进程 ID、共享内存句柄和确切的命令行长度。</span></font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong style="box-sizing: border-box;font-weight: bold;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">触发命令执行</span></font></font></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><span leaf="">WER 服务复制句柄并使用提供的命令行启动 WerFault.exe。</span></font></font></td></tr></tbody></table>  
由于 WER 服务以高权限级别运行，因此新生成的进程继承了 SYSTEM 令牌。  
  
此令牌包含危险权限，例如 SeDebugPrivilege（允许调试任何进程）和 SeImpersonatePrivilege（允许模拟任何用户）。  
  
虽然SeTcbPrivilege并未被授予作为操作系统一部分的权限，但所获得的权限仍然提供了完整的系统访问权限。  
  
该漏洞影响范围广泛，包括2026年1月之前的所有Windows 10和Windows 11版本，以及运行Windows Server 2019和Windows Server 2022的企业服务器环境。  
  
微软在2026 年 1 月的安全更新中正式解决了这个漏洞。  
  
根据 GitHub 上发布的 PoC，强烈建议组织和系统管理员立即应用最新的安全补丁来保护其网络安全。  
  
