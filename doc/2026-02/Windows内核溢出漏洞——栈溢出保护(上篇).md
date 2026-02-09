#  Windows内核溢出漏洞——栈溢出保护(上篇)  
 众亦信安   2026-02-09 13:09  
  
## 前言  
  
上篇文章中介绍了利用Windows内核栈溢出进行提权，但是保护全关状态，本文介绍在打开SMEP和GS保护的情况下如何进行攻击。  
## Windows保护机制  
### GS栈保护机制  
#### security_cookie技术分析  
  
在Visual Studio 2005编译器中引入了GS保护，主要的作用是为了解决栈溢出的问题，对栈漏洞影响是在开启了GS后，无法在只有一个栈溢出漏洞的情况下，完成对栈的控制。开启方式如下图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rWfcL9Rh5WKEUpJiaRtFb2W1Uc3zocFpWHVDH3cfx3FPQtRd8rNPLQibQ/640?wx_fmt=png&from=appmsg "")  
  
  
在实际编译了代码中，每个函数都被加入了一段如下汇编  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rbhNYhQalicv7AgiccSJaibicbNDicEevkGzxggUxSU8alsJxNebZFkK4ZJA/640?wx_fmt=png&from=appmsg "")  
  
  
通过程序启动后创建一个固定的cookie，栈溢出的必须条件是覆盖栈到一定长度，这个cookie刚好被放到了需要被覆盖的栈帧上，如果被异或解密出的cookie和程序启动时创建的不符，那么就意味着栈产生错误。这时check_security_cookie()函数会让程序结束。使用这样的方式完成检查栈溢出。由此我们可以得出以下几点关键信息:  
1. security_cookie_init()是程序启动时被调用了，之后程序不会再调用  
  
1. security_cookie位于程序的.data段中，.data中的数据是可以被改写的  
  
1. security_init_cookie()对程序的SEH部分的代码并没有进行保护  
  
#### 绕过思路  
  
了解security_cookie的机制后，便有了针对的绕过机制。一种方法是，如果存在一个任意地址写入的漏洞，利用这个漏洞尝试重写  
security_cookie  
将这个值设置为我们固定的值，那么在接下来的栈溢出中，只需要得到RSP的值，将栈中的cookie的栈帧设置为程序所需要的cookie完成  
_security_check_cookie()  
的检查即可。  
  
另一种办法是针对异常处理的攻击手法，由于向程序的所有函数插入栈保护会降低程序的空间效率和时间效率，编译器并不是对所有函数插入保护，如下几种情况是不会添加栈保护的  
1. 函数不包含缓冲区  
  
1. 函数使用无保护的关键字标记  
  
1. 函数在第一个语句中包含内嵌汇编代码  
  
1. 缓冲区不是8字节类型且大小不大于4个字节等  
  
还有就是对S.E.H(异常处理)并不进行保护，并且对堆漏洞利用很难防护。通过大量字符先覆盖栈，然后触发异常处理(本文主要讲第一种技术)。  
### SMEP&SMAP  
#### 代码执行保护  
  
为提升操作系统内核的安全性，现代 x86/x64 处理器引入了多种硬件级防护机制，其中 SMEP（Supervisor Mode Execution Protection） 和 SMAP（Supervisor Mode Access Protection） 是两项重要特性。  
  
SMEP 用于防止内核模式下执行用户态代码。当 SMEP 启用后，若处理器处于内核模式（Ring 0）并尝试执行位于用户态地址空间的指令，CPU 将触发异常并终止该执行路径。该机制可以有效阻止攻击者通过劫持内核执行流，使其跳转到用户态代码，从而提升内核执行流的安全性。  
  
SMAP 用于防止内核模式下随意访问用户态数据。当 SMAP 启用后，内核在未显式授权的情况下访问用户态内存会触发异常。只有在内核临时设置允许标志后，才能安全地读写用户态数据。该机制主要用于防止内核漏洞被利用来非法读写用户空间内存。  
  
总体而言，SMEP 侧重于限制内核执行用户态代码，而 SMAP 侧重于限制内核访问用户态数据。两者通常同时启用，用于降低内核被利用的风险，增强系统整体安全性。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8r2HRlf8WHTMG8wWHa05Xy81CPdyicjxEIyw99licwjD3oNJLIeTNkyn5A/640?wx_fmt=png&from=appmsg "")  
  
#### 绕过思路  
  
本文主要讲解通过PTE复写技术绕过SMEP。通过观察内核地址和用户态地址的PTE页表属性即可发现，内存页被标记了内核内存和用户内存，通过任意地址写入漏洞或者通过ROP构造gadent直接把这个属性改为可以被内核执行的内存属性即可完成。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rw47g9WgIevEx6W6JvCkknx8QCtmoKgpJrqTBYxAXufnibUxIy74CtvQ/640?wx_fmt=png&from=appmsg "")  
  
## 漏洞利用  
  
漏洞的本质原理和上篇文章中所讲到的原理一致，因此不再过多赘述。通过前文的描述，想要成功利用这个漏洞，就需要2个数据，分别是漏洞函数的rsp值和记录pte页表属性的内存地址。  
### 漏洞函数rsp泄漏  
  
对GS保护机制了解后，我们只需按照GS的校验机制，在溢出时让数据和栈上的cookie抱持相同即可。那么这一步就需要泄露出rsp的数据。原因是为了计算出栈上用于校验的cookie。cookie是通过RSP和security_cookie异或计算后得到的，异或计算的一个特性就是可以被逆运算。因此得出RSP和security_cookie就可以计算出栈上的校验cookie。  
  
在HEVD中有存在任意内存读写漏洞，根据逆向分析可以得出security_cookie位置，由于security_cookie只会在程序加载的第一次才被初始化，因此只需要提取用读写漏洞读取出即可。在计算出HEVD的基址后，使用逆向得到的偏移即可拿到security_cookie的值，这个值在驱动卸载之前都不会变。内存读写漏洞函数为  
TriggerArbitraryWrite  
。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rvOlWpLjJkZI8zUib64Ac5OuYmobLbAEm297LJClT5XunllFDZfBhEJw/640?wx_fmt=png&from=appmsg "")  
  
  
与之相比，RSP 的获取过程相对复杂。可以通过调用  
NtQuerySystemInformation()  
，并将信息类参数设置为 57（SystemExtendedProcessInformation），获取系统中各进程的详细信息。  
**(注:此方法在Windows11高版本不再有效，文章环境为Windows 10 21H2)**  
  
返回的   
SYSTEM_EXTENDED_PROCESS_INFORMATION  
 结构体中包含了进程线程相关的数据，其中可用于推导线程栈的 起始地址和结束地址，从而确定线程栈的有效范围。  
  
由于在用户态调用   
DeviceIoControl()  
 进入内核时，执行流程必然会经过一系列内核函数（例如   
NtDeviceIoControlFile()  
），而这些函数的返回地址会被压入当前线程的内核栈中，因此可以利用这一特性进行定位。  
  
通过对   
ntoskrnl.exe  
 进行逆向分析，可以获得   
NtDeviceIoControlFile()  
 在内核镜像中的偏移。结合运行时获取的   
ntoskrnl  
 基地址，即可计算出该函数在内存中的实际地址。  
  
随后，在已知的内核栈地址范围内搜索该函数地址，即可定位到一个稳定存在于栈上的返回地址。在此基础上，通过调试分析确定该返回地址与漏洞函数使用的   
RSP  
 之间的固定偏移关系。  
  
最终，将定位到的栈地址加上该偏移，即可准确计算出漏洞函数执行时所使用的   
RSP  
 值。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rIjRUSCFMJMvRJ2LWztL1eWQKPbEPO07lpVpmbicn3xqagAsrdSqOFoA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rdCxbtibKPNJqJz3Ykm144KuEEgIP0SatQ4Gj4sFw0CiabKEib1YDYqmfg/640?wx_fmt=png&from=appmsg "")  
  
### 获取PTE页表属性  
  
在此之后，需要解决的问题是SMEP保护，在上篇文章中通过Windbg手动关闭SMEP保护，如果在多核情况下需要同时修改多个CPU的CR4寄存器。在漏洞利用中通过汇编完成CPU切换是不现实的。可以通过直接修改PTE的页表属性，将分配的shellcode的内存空间的页表属性改为可以被内核读取即可。在修改之后这个内存无法在用户态空间读取到。通过虚拟地址计算PTE地址的方式如下  
```
PT_index = (VirtualAddress >> 12) & 0x1FF;
PTE_address = PTE_BASE + (PT_index * 8);
```  
  
由此在利用时不得不先获取到PTE_BASE的地址，这个地址被  
ntoskrnl.exe  
导出为  
MmPteBase  
通过逆向分析拿到偏移即可，利用公式即可计算得出PTE_Address，再通过内核漏洞即可得到pfn。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rebaZDzO2smTOlA6JbWiceMLcu1QWuXhVaZIrQ1JuIlwyx6biaWxJOqUg/640?wx_fmt=png&from=appmsg "")  
  
  
有了pfn之后通过读写漏洞将原始数据读出，再通过如下计算即可得出允许内核执行的内存属性，再次通过读写漏洞写入即可。  
```
new_pfn = old_pfn& ~0x4
```  
  
如下图 用户态空间地址的页表属性被改为可以被内核执行的内存属性  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rkvEeSOmFOwNWiaOXmlRWxA2h5EoDETThL2Letx3UfXNlW2BTmMtEnGw/640?wx_fmt=png&from=appmsg "")  
  
通过以上方式修改内存页属性后，需要通过wbinvd指令刷新缓存，因此需要找到一个wbinvd gadent，这一步通过逆向分析即可得出。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rGKIaNtn6OJBlJ1T5xUj4kQw2cgXRQAY3vKfYzv3QklzXFthWGdCBPA/640?wx_fmt=png&from=appmsg "")  
### 恢复堆栈  
  
在之前的栈漏洞利用中，shellcode 通过修改当前内核栈内容，覆盖了一段栈空间，从而构造出一条  
**可控的安全返回路径**  
，使执行流能够正常退出内核并回到 3 环。  
  
然而，在本次利用场景中，由于执行路径中 额外引入了   
wbinvd  
 指令，破坏了下一个栈的数据，导致内核在返回过程中出现异常.。这一变化使得原先依赖“覆盖固定栈区域”的方式不再可靠：shellcode 在修改栈时会影响到后续使用的栈，从而破坏执行流程，无法再沿用之前的退出策略。  
  
基于上述限制，本次利用需要对 shellcode 进行改造，不再依赖覆盖栈空间来完成返回，而是主动恢复内核态→用户态切换所需的寄存器状态。具体思路是：  
1. 通过   
swapgs  
 切换 GS 基址，访问当前 CPU 的 KPCR；  
  
1. 从   
KPCR  
 中获取当前线程的   
KTHREAD  
；  
  
1. 进一步定位到   
ETHREAD.TrapFrame  
；  
  
1. 直接从   
TrapFrame  
 中恢复用户态所需的寄存器状态（RIP / RSP / RBP / EFLAGS）；  
  
1. 使用   
sysret  
 指令 绕过后续内核代码路径，直接返回到 3 环。  
  
这样可以完全跳过受影响的内核返回流程，避免栈被破坏的问题，实现稳定的安全退出。  
```
mov rax, [gs:0x188]  ;找到KThread地址
mov cx, [rax+0x1e4]	 ;修改KThread.KernelApcDisable
inc cx
mov [rax + 0x1e4], cx
mov rdx, [rax + 0x90]     ; ETHREAD.TrapFrame
mov rcx, [rdx + 0x168]    ; ETHREAD.TrapFrame.Rip
mov r11, [rdx + 0x178]    ; ETHREAD.TrapFrame.EFlags
mov rsp, [rdx + 0x180]    ; ETHREAD.TrapFrame.Rsp
mov rbp, [rdx + 0x158]    ; ETHREAD.TrapFrame.Rbp
xor eax,eax
swapgs
o64 sysret
```  
  
有一处细节在提权完成后不要直接关闭内核句柄，否则进程卡死。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/YO5l2I4CZNl6AH9LRKdEXvibONsqMrZ8rQX10GdKTjjVP07LpgFJQia6CqjqAw4ObaUFTdANkXqxqHaAGW5Xg7nA/640?wx_fmt=png&from=appmsg "")  
### 完整利用流程  
### 代码之后上传至Github  
## 文章引用  
  
代码参考:  
https://github.com/zoemurmure/HEVD-Exploit/  
  
感谢大佬！！！  
  
  
  
  
  
  
  
  
