#  一行错误函数调用引发的 OpenSSH 预认证漏洞  
原创 🅼🅰🆈
                    🅼🅰🆈  独眼情报   2026-03-13 06:06  
  
![](https://mmbiz.qpic.cn/mmbiz_png/cBGhzWwhSAiaVGx4umtG5FDCPOr0YRqQFT7pHbFqI9ytfhQGev4eEgYWSFqJu6MiburMtjfkIst7UsdxWAicHxKmf39EgYveHOOwjE1T47UL8k/640?wx_fmt=png&from=appmsg "")  
## 一、背景：这不是 OpenSSH 的 Bug，是发行版补丁的 Bug  
  
2026年3月12日，Canonical 安全工程师 Marc Deslauriers 在 oss-sec 邮件列表发布了一份披露通告，描述了安全研究员 Jeremy Brown 在 GSSAPI 密钥交换补丁中发现的严重安全缺陷，编号为 CVE-2026-3497。  
  
这一缺陷存在于众多发行版在官方 OpenSSH 软件包之上额外附加的 GSSAPI 密钥交换补丁中，而非 OpenBSD 官方维护的 OpenSSH 上游代码本身。这个细节至关重要：官方 OpenSSH 项目不受此漏洞影响，风险完全来自下游发行版对官方代码库的修改。  
  
GSSAPI 密钥交换功能（由 GSSAPIKeyExchange yes  
 配置项启用）允许在 SSH 握手阶段直接通过 Kerberos 等 GSSAPI 机制完成认证，常见于企业内网和高校环境中。由于这项功能不属于 OpenSSH 官方支持的范畴，各发行版长期以来各自维护着版本不尽相同的社区补丁，CVE-2026-3497 的根源正在于此。  
## 二、技术细节：一个函数名之差，安全边界全线崩溃  
### 核心缺陷  
  
该补丁中存在一处代码缺陷：在 GSSAPI 密钥交换服务端循环的错误处理分支中，使用了 sshpkt_disconnect()  
（该函数仅将断开消息加入队列后返回，不会终止进程），而原本意图应该调用的是 ssh_packet_disconnect()  
（该函数会直接终止进程）。这两个函数名极为相似，但行为天差地别。  
  
换言之，这个错误使得原本应该终止进程的错误处理路径变成了一个「会继续往下执行」的路径。  
### 未初始化变量泄漏  
  
错误处理的 default:  
 分支执行后没有终止，程序继续向下执行，进入了操作未初始化栈变量 recv_tok  
 的代码区域。recv_tok  
 的内容随即通过进程间通信被发送至拥有更高权限的 monitor 进程，随后传递给 gss_release_buffer()  
，后者可能对一个垃圾指针调用 free()  
，从而触发堆内存破坏。  
  
这一过程涉及两个经典漏洞类型：CWE-824（未初始化指针解引用）和 CWE-908（使用未初始化的内存）。  
### 特权分离边界被穿透  
  
OpenSSH 的权限分离架构本是一道重要防线：网络侧进程以低权限运行，通过 IPC 与高权限的 monitor 进程通信。然而此次漏洞直接打穿了这道边界——在特定编译条件下（GCC -O2 加上 -fno-stack-protector），recv_tok.value  
 可能指向一个有效的堆地址，长度值为 127344 字节，意味着最多可将约 127KB 的堆数据通过 IPC 传递给 root 级别的 monitor 进程。  
### 编译器相关性  
  
漏洞的危害程度与编译器选项密切相关，这是此漏洞的一个独特之处：不同编译器产生的栈残留数据存在本质差异。Clang -O0 编译下，recv_tok.value  
 的值为 0xfffbe600  
，长度为 4；GCC -O2 并关闭栈保护的情况下，则是一个有效的堆地址，长度达到 127344 字节。这意味着在不同发行版的不同构建配置下，攻击效果从拒绝服务到潜在的任意代码执行之间存在显著差异。  
## 三、攻击向量：门槛极低  
  
触发条件极为简单：发送一个约 300 字节的特制 SSH 数据包即可，无需任何身份凭证，攻击完全发生在认证流程之前。这是预认证漏洞中最危险的一类——攻击者不需要账号，不需要密码，只要目标端口可访问就可以发起攻击。  
  
经验证的直接影响包括：在 x86_64 架构上触发 SIGABRT（信号6）和 SIGSEGV（信号11），导致子进程崩溃并触发 90 秒的 SSH 连接封锁，且子进程崩溃率为 100%。  
## 四、受影响范围  
  
此漏洞仅影响满足以下两个条件的系统：  
  
第一，系统为 Ubuntu 或 Debian（以及其衍生版本），使用了携带 GSSAPI 密钥交换补丁的 OpenSSH 软件包。第二，SSH 服务端配置文件中明确设置了 GSSAPIKeyExchange yes  
。Ubuntu 官方确认，受影响版本包括 Ubuntu 22.04 LTS、24.04 LTS 及 25.10。  
  
值得注意的是，GSSAPIKeyExchange  
 并非默认启用项，**因此大多数普通 Ubuntu/Debian 服务器实际上并不受影响**  
。但在对接企业 Kerberos/Active Directory 认证的生产环境中，这一选项往往是刻意开启的，而这类环境恰恰是攻击者最有价值的目标。  
  
Red Hat、Fedora、SUSE 等其他主流发行版均有各自版本的 GSSAPI 补丁，是否受影响需要独立核实——Marc Deslauriers 在原始披露中也明确指出，不同发行版携带的补丁版本存在差异，核心缺陷是共性的，但具体影响有所不同。目前尚无公开信息证实这些发行版已确认受到波及，**此处需保持审慎，不宜直接断言其受影响**  
。  
## 五、修复措施  
### 官方补丁  
  
Ubuntu 于3月12日发布了安全公告 USN-8090-1，随后又发布 USN-8090-2 以覆盖 Ubuntu 20.04 LTS。修复版本如下：Ubuntu 22.04 LTS 对应 1:8.9p1-3ubuntu0.14  
，Ubuntu 24.04 LTS 对应 1:9.6p1-3ubuntu13.15  
，Ubuntu 25.10 对应 1:10.0p1-5ubuntu5.1  
。  
  
执行以下命令即可完成修复：  
```
sudo apt update && sudo apt upgrade openssh-server

```  
  
修复方案的技术核心非常简单——将 kexgsss.c  
 中服务端三处调用 sshpkt_disconnect()  
 的位置全部替换为 ssh_packet_disconnect()  
。改动量极小，却修复了一个存在多年的重大安全隐患。  
### 临时缓解  
  
如果暂时无法立即升级，可在 /etc/ssh/sshd_config  
 中将以下配置项更改为 no  
，然后重启 SSH 服务：  
```
GSSAPIKeyExchange no

```  
  
但需注意，这会导致依赖 GSSAPI 密钥交换的 Kerberos 认证流程失效。  
  
参考： https://seclists.org/oss-sec/2026/q1/299  
  
  
