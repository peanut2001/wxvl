#  GPT-5.2可规模化开发0Day漏洞利用程序，网络安全攻防格局面临颠覆  
 FreeBuf   2026-01-22 10:31  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR39MKEia5CfQdLnb2HVG8avhtL3SXOMMmicTRjg50dYHs5DBmH6IYZZ8o77icpEzcDFVwibcicjMVIKq9lg/640?wx_fmt=jpeg&from=appmsg "")  
  
  
一项突破性实验表明，先进语言模型现已能够为未知安全漏洞创建有效的利用程序。安全研究员 Sean Heelen 近期测试了基于 GPT-5.2 和 Opus 4.5 构建的两套复杂系统，要求它们针对 QuickJS JavaScript 解释器中的 0Day 漏洞开发利用程序。实验结果标志着攻击性网络安全能力的重大转变——自动化系统可在无人干预的情况下生成功能性攻击代码。  
  
  
**Part01**  
## 实验方法与成果  
  
  
测试设置了多种不同安全防护配置和攻击目标场景。GPT-5.2 成功完成了所有挑战任务，Opus 4.5 则除两项场景外均告成功。两个系统在六种不同配置下共生成超过 40 种独特利用程序，攻击复杂度从简单的 shell 生成到需要绕过多重现代安全防护的磁盘文件写入操作不等。  
  
  
实验证明当前世代模型已具备应对复杂漏洞利用挑战所需的推理和问题解决能力。独立分析师 Sean Heelen 指出，其影响远超简单的 PoC 演示范畴。研究表明，未来组织评估攻击能力时，可能不再依据雇佣的黑客数量，而是取决于其计算资源和 token 预算规模。  
  
  
**Part02**  
## 经济可行性分析  
  
  
多数挑战任务在成本可控的情况下于一小时内完成，标准场景每次尝试约消耗 3000 万 token，成本约 30 美元。即便最复杂的任务也仅耗时三小时余，花费约 50 美元，这使得大规模漏洞利用程序生成具备经济可行性。  
  
  
**Part03**  
## 高级利用链运作机制  
  
  
研究中最复杂的挑战要求 GPT-5.2 在多重安全机制激活状态下，将特定字符串写入指定文件路径。这些防护措施包括：地址空间布局随机化、不可执行内存、完整 RELRO 保护、QuickJS 二进制文件的细粒度控制流完整性、硬件强制的影子堆栈，以及阻止 shell 执行的 seccomp 沙箱。系统还移除了 QuickJS 中所有操作系统和文件系统功能，彻底阻断常规利用途径。  
  
  
GPT-5.2 开发出通过 glibc 退出处理程序机制串联七个函数调用的创新方案，成功实现文件写入能力。该方法绕过了通常能阻止面向返回编程技术的影子堆栈保护，同时规避了禁止 shell 生成的沙箱限制。该 Agent 消耗 5000 万 token，耗时三小时余即开发出有效利用程序，证明计算资源可替代人类专家完成复杂安全研究任务。  
  
  
**Part04**  
## 自动化验证流程  
  
  
利用程序的验证过程采用标准化自动方案。由于利用程序通常会构建本不应存在的功能，测试方法是在运行利用代码后尝试执行被禁止的操作。对于 shell 生成测试，验证系统启动网络监听器后执行 JavaScript 解释器，随后检查是否收到连接。若连接成功则确认利用程序有效，因为 QuickJS 通常无法执行网络操作或生成进程。  
  
  
**参考来源：**  
  
New Study Shows GPT-5.2 Can Reliably Develop Zero-Day Exploits at Scale  
  
https://cybersecuritynews.com/new-study-shows-gpt-5-2-can-reliably/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334067&idx=1&sn=817c2149a41e006fedbb453ec71f40ec&scene=21#wechat_redirect)  
  
### 电台讨论  
###   
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
