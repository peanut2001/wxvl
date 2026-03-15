#  Linux AppArmor模块曝九大漏洞，可致提权及绕过容器隔离  
 FreeBuf   2026-03-15 10:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3BB6j7icvOXhefrIlHgQA6iaqU3FMrEookkkd8ibib4j4Nw05eNpYnr5kiaXQib4miaw5yNUBicd08t8cqb48Fe5tOKvvKg5bhQlzoxE0/640?wx_fmt=png&from=appmsg "")  
##   
## 网络安全研究人员披露了 Linux 内核 AppArmor 模块中的多个安全漏洞，非特权用户可利用这些漏洞绕过内核保护机制、提升至 root 权限并破坏容器隔离保障。  
  
  
Qualys 威胁研究部门（TRU）将这九个混淆代理漏洞统称为 "**CrackArmor"**  
。该网络安全公司表示，该问题自 2017 年起就已存在。目前这些漏洞尚未分配 CVE 编号。  
  
  
AppArmor 是 Linux 的安全模块，提供强制访问控制（MAC），通过防止已知和未知应用程序漏洞被利用来保护操作系统免受外部或内部威胁。自 Linux 内核 2.6.36 版本起，AppArmor 已被纳入主线内核。  
##   
  
**Part01**  
## 漏洞技术细节  
  
  
Qualys TRU 高级经理 Saeed Abbasi 表示：此次 'CrackArmor' 公告披露了一个混淆代理漏洞，允许非特权用户通过伪文件操纵安全配置文件、绕过用户命名空间限制，并在内核中执行任意代码。  
  
  
这些漏洞通过与 Sudo 和 Postfix 等工具的复杂交互，促成本地提权至 root；同时还能通过堆栈耗尽发起拒绝服务攻击，以及通过越界读取绕过内核地址空间布局随机化（KASLR）。  
  
  
混淆代理漏洞是指特权程序被未经授权的用户胁迫滥用其权限执行非预期的恶意操作。该问题本质上利用了高权限工具的信任关系来执行导致权限提升的命令。  
  
  
**Part02**  
## 潜在攻击影响  
  
  
Qualys 指出，不具备执行某项操作权限的实体可以操纵 AppArmor 配置文件来禁用关键服务保护或强制执行全拒绝策略，在此过程中触发拒绝服务（DoS）攻击。  
  
  
结合配置文件解析过程中固有的内核级缺陷，攻击者可绕过用户命名空间限制，实现本地提权（LPE）至完整 root 权限。  
  
策略操纵会危及整个主机，而命名空间绕过则有助于实现高级内核利用，例如任意内存泄露。DoS 和 LPE 能力会导致服务中断、通过无密码 root（例如修改 /etc/passwd）进行凭据篡改，或泄露 KASLR 信息，从而为进一步的远程利用链创造条件。  
  
更糟糕的是，CrackArmor 允许非特权用户创建具备完整能力的用户命名空间，有效绕过 Ubuntu 通过 AppArmor 实现的用户命名空间限制，并破坏容器隔离、最小权限执行和服务强化等关键安全保障。  
  
  
**Part03**  
## 修复建议  
  
  
该网络安全公司表示，暂不发布针对已识别漏洞的概念验证（PoC）利用代码，以便为用户留出时间优先打补丁并减少暴露风险。  
  
  
此问题影响所有自 4.11 版本起的 Linux 内核，只要发行版集成了 AppArmor 就会受到影响。由于 Ubuntu、Debian 和 SUSE 等多个主要发行版默认启用了 AppArmor，运行中的企业 Linux 实例超过 1260 万台，建议立即打内核补丁以缓解这些漏洞。  
  
  
Abbasi 强调："立即打内核补丁仍然是解决这些关键漏洞不可妥协的首要任务，因为临时缓解措施无法提供与恢复供应商修复代码路径相同级别的安全保障。"  
  
  
**参考来源：**  
  
Nine CrackArmor Flaws in Linux AppArmor Enable Root Escalation, Bypass Container Isolation  
  
https://thehackernews.com/2026/03/nine-crackarmor-flaws-in-linux-apparmor.html  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)  
  
  
### 电报讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
