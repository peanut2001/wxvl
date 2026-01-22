#  漏洞挖掘实战系列（第18期）：高级Pwn技巧 ROP进阶+堆风水+格式化字符串漏洞  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-01-22 09:39  
  
在前17期内容中，我们覆盖了Web、移动端、物联网等多领域漏洞，而Pwn作为二进制安全的核心，是CTF竞赛的必争之地，也是真实渗透测试中突破系统边界的终极手段。多数人能掌握基础栈溢出，但面对NX、PIE等保护机制，或是堆漏洞、格式化字符串这类复杂场景时，往往陷入瓶颈。  
  
本期聚焦**高级Pwn三大核心技术**  
，全程基于Linux x86/x86_64架构，结合GDB、pwntools、IDA等工具实战，通过“原理拆解+调试步骤+可复现案例+正确Payload”的模式，逐一攻克难点。无论是CTF选手冲击中等难度Pwn题，还是渗透工程师挖掘二进制程序漏洞，这份内容都能直接落地复用，帮你突破Pwn进阶瓶颈。  
  
注：所有案例均关闭PIE保护（便于新手理解地址逻辑），开启NX保护（贴近实战场景），配套靶机环境与完整脚本，确保每一步都能复现成功。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralYCOWe0tQO4wnKRkJ5lynztELh3VeicL1ToMwpPHk3d9sRcCflTfhFohTyJm8iba1DbpjH8OazHfWSA/640?wx_fmt=png&from=appmsg "")  
## 一、ROP进阶：突破NX保护的核心方法论  
  
当程序开启NX（No-eXecute）保护时，栈与堆上的代码无法直接执行，基础栈溢出漏洞失效。ROP（Return-Oriented Programming，返回导向编程）通过拼接程序及依赖库（如libc）中已有的“gadget”（以ret结尾的短指令序列），构造攻击链实现函数调用、系统调用，是突破NX保护的唯一核心方案。  
### 1. 核心概念：gadget分类与识别  
  
gadget是二进制程序中天然存在的、以ret指令结尾的短指令片段，不同类型的gadget承担不同功能，组合后可实现完整攻击逻辑。  
#### 常用gadget类型及作用  
- **参数传递gadget**  
：用于给寄存器赋值（适配x86_64架构的寄存器传参规则），核心为“pop 寄存器; ret”。例如： pop rdi; ret（弹出栈中数据到rdi寄存器，x86_64下第一个函数参数存于rdi）； pop rsi; pop r15; ret（弹出数据到rsi、r15，适配第二个参数传递）。  
  
- **数据操作gadget**  
：用于寄存器间数据传递、运算，例如“mov rdi, rsi; ret”（将rsi值赋给rdi）、“add rdi, 0x10; ret”（rdi值加0x10）。  
  
- **系统调用gadget**  
：触发内核态系统调用，x86架构为“int 0x80”，x86_64架构为“syscall; ret”，需配合寄存器赋值构造系统调用参数。  
  
#### gadget识别工具与正确用法  
- **ROPgadget**  
：命令行工具，扫描二进制程序中的所有gadget，示例命令：ROPgadget --binary pwn --only "pop|ret"  # 仅筛选含pop和ret的gadgetROPgadget --binary pwn --string "/bin/sh"  # 查找程序中是否存在/bin/sh字符串  
。  
  
- **pwntools.ROP模块**  
：自动化查找gadget并构造ROP链，无需手动计算地址，大幅提升效率。  
  
- **IDA Pro+ROP Finder插件**  
：可视化标注gadget位置与功能，适合复杂程序（如大型二进制）的gadget分析。  
  
### 2. 实战案例：ROP链构造+libc泄露（x86_64）  
#### 漏洞场景  
  
目标程序（pwn18_rop）开启NX保护、关闭PIE保护，存在栈溢出漏洞（缓冲区大小0x80，可通过read函数控制返回地址）；程序依赖libc库，自身无system函数与/bin/sh字符串，需通过泄露libc地址，构造ROP链调用system("/bin/sh")。  
#### 利用逻辑  
1. 泄露libc地址：通过ROP链调用puts函数，打印puts@got（全局偏移表）的真实地址，结合libc版本计算system函数与/bin/sh字符串的地址；  
  
1. 二次构造ROP链：调用system函数，传递/bin/sh作为参数，实现getshell。  
  
#### 完整Payload与代码（pwntools实现）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralbolWr7ZOibTqEnRXJNXksL1Alico5Evu9ZumL7w9Viaibwl6I99lVvT3vKKMCxpVHDDn1xydBJqk0c1A/640?wx_fmt=png&from=appmsg "")  
  
#### 关键注意事项  
- x86_64架构函数参数传递规则：前6个参数依次存入rdi、rsi、rdx、rcx、r8、r9，多余参数存入栈，构造ROP链时需按顺序赋值寄存器。  
  
- libc版本必须匹配：若泄露地址计算后程序崩溃，大概率是libc版本不匹配，可通过libc.blukat.me查询对应版本（输入泄露的puts地址即可匹配）。  
  
- 栈对齐问题：部分程序（如编译时开启-O2优化）要求栈地址为16字节对齐，需插入额外的ret gadget调整栈指针，否则会触发程序崩溃。  
  
## 二、堆风水：堆漏洞利用的内存布局控制术  
  
堆漏洞（如UAF、Double Free、Use-After-Free）的核心难点在于“内存布局不可控”，堆风水（Heap Feng Shui）通过精心设计的“分配-释放-再分配”操作，调整堆块的位置、大小与状态，让恶意数据精准覆盖关键地址（如函数指针、堆块元数据），最终实现漏洞利用。  
### 1. 堆核心基础与堆风水原理  
#### 堆块结构（glibc malloc）  
  
glibc中的堆块分为“使用中堆块”与“空闲堆块”，核心结构如下（x86_64）：  
- 使用中堆块：prev_size（前一个堆块大小，仅前一个堆块空闲时有效）→ size（当前堆块大小，低3位为标志位）→ 数据区 → 堆块尾部footer（与size字段一致）。  
  
- 空闲堆块：在使用中堆块基础上，数据区增加fd（前向指针，指向链表中下一个空闲堆块）、bk（后向指针，指向链表中上一个空闲堆块），用于空闲堆块管理。  
  
#### 堆风水核心逻辑  
  
通过“填充堆块”“精准释放”控制空闲堆块的合并与分配，将恶意堆块布局到目标地址（如函数指针、GOT表）附近，当程序访问目标地址时，触发恶意数据执行。核心原则：避免空闲堆块合并，精准控制堆块分配顺序。  
### 2. 实战案例：Double Free漏洞+堆风水（x86）  
#### 漏洞场景  
  
目标程序（pwn18_heap）开启NX保护、关闭PIE保护，提供malloc（分配堆块）、free（释放堆块）、edit（修改堆块数据）功能；存在Double Free漏洞（允许重复释放同一堆块），堆块大小限制为0x80（属于fastbin范围，不触发空闲堆块合并）。  
#### 利用逻辑  
1. 分配3个大小为0x80的堆块，构造Double Free场景，让fastbin链表形成循环；  
  
1. 通过堆风水布局，将free@got（GOT表地址）写入堆块fd指针，实现堆块分配到GOT表地址；  
  
1. 修改该堆块数据，将free@got覆盖为system地址；  
  
1. 释放包含/bin/sh的堆块，触发free函数调用（实际执行system("/bin/sh")）。  
  
#### 完整Payload与代码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralbolWr7ZOibTqEnRXJNXksL1oZlHBV47oF1XZdbDtF0LomtLTlSWNfhXicCE4XDCqMCicSC6EQX8u7DQ/640?wx_fmt=png&from=appmsg "")  
  
#### 堆风水关键技巧  
- 利用fastbin特性：fastbin（0x10~0x80，x86）堆块释放后不合并，适合构造Double Free、UAF漏洞，避免空闲堆块合并干扰布局。  
  
- 填充堆块防合并：若堆块大小超出fastbin范围，需分配“填充堆块”（大小为0x10），隔开空闲堆块，防止合并。  
  
- 调试验证布局：用GDB+pwndbg插件，通过“heap”命令查看堆布局，“x/40xw 堆地址”查看堆块数据，确保布局符合预期。  
  
## 三、格式化字符串漏洞：精准读写内存的利器  
  
格式化字符串漏洞源于printf、sprintf、fprintf等函数的格式化参数可控，攻击者可通过构造恶意格式化字符串，实现内存读取（泄露敏感地址）、内存写入（修改函数指针），甚至直接getshell，是CTF中高频出现的Pwn漏洞类型。  
### 1. 漏洞原理与关键格式化符号  
#### 核心原理  
  
当格式化函数的第一个参数可控时（如printf(buf)，buf由用户输入控制），攻击者可通过格式化符号读取栈上数据，或利用%n系列符号将数据写入指定地址。例如：输入“%x%x%x”，printf会依次打印栈上3个4字节数据（x86架构）。  
#### 关键格式化符号（实战常用）  
<table><thead><tr><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">符号</span></section></th><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">功能</span></section></th><th style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(8, 155, 163);border: 1px solid rgb(8, 155, 163);vertical-align: top;font-weight: bold;background-color: rgba(122, 234, 240, 0.094);"><section><span leaf="">适用场景</span></section></th></tr></thead><tbody><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">%x</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">以十六进制打印4字节数据（x86）/8字节（x86_64）</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">内存读取、偏移定位</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">%s</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">打印字符串（需地址合法，指向可读内存）</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">泄露字符串、GOT表地址</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">%k$x</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">打印栈上第k个参数（精准定位数据）</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">偏移已知时快速读取</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">%n</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">将已打印字符数写入指定地址（4字节）</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">内存写入、修改函数指针</span></section></td></tr><tr><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">%hn</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">将已打印字符数写入指定地址（2字节）</span></section></td><td style="font-size: 10px;padding: 9px 12px;line-height: 22px;color: rgb(34, 34, 34);border: 1px solid rgb(8, 155, 163);vertical-align: top;"><section><span leaf="">分阶段写入大地址，避免溢出</span></section></td></tr></tbody></table>### 2. 实战案例：格式化字符串写入+GOT表劫持（x86）  
#### 漏洞场景  
  
目标程序（pwn18_fmt）开启NX保护、关闭PIE保护，存在printf(user_input)语句（格式化参数完全可控）；程序无system函数，需通过修改puts@got为system地址，触发system调用。  
#### 利用逻辑  
1. 定位偏移：构造测试字符串，确定格式化参数在栈上的偏移（即用户输入数据对应栈上第k个参数）；  
  
1. 泄露puts@got地址：通过%k$s读取puts@got对应的真实地址，计算system地址；  
  
1. 写入内存：利用%n符号，将system地址写入puts@got，覆盖原有地址；  
  
1. 触发调用：调用puts函数（实际执行system），传递/bin/sh参数getshell。  
  
#### 完整Payload与代码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralbolWr7ZOibTqEnRXJNXksL1xBxbH4vbiberFyXlwmttfSXlufOGbPr5buouADpRWiaT7H2rtHWavoZg/640?wx_fmt=png&from=appmsg "")  
#### 实战调试技巧  
- 偏移定位：用“%k$x”逐一代入k值（从1开始），观察泄露数据，若泄露数据与用户输入的地址一致，即为正确偏移。  
  
- 多字节写入：当写入地址（如system_addr）超过1字节时，用%hn/%hhn分阶段写入，避免单次写入数据过大导致程序崩溃，pwntools的fmtstr_payload会自动处理分阶段写入。  
  
- 地址对齐：x86架构地址为4字节对齐，x86_64为8字节对齐，构造Payload时需确保写入地址对齐，否则会触发内存访问错误。  
  
## 四、高级Pwn必备工具与实战建议  
### 1. 核心工具套装（必装）  
- **调试工具**  
：GDB+pwndbg（增强GDB功能，支持heap、rop等命令）、GDB+peda（适合指令跟踪与栈分析）。  
  
- **辅助工具**  
：pwntools（自动化Payload构造、进程交互）、ROPgadget（gadget扫描）、checksec（程序保护机制检测，命令：checksec --file 程序名）。  
  
- **逆向工具**  
：IDA Pro（二进制逆向分析、函数定位）、Ghidra（开源逆向工具，替代IDA入门使用）。  
  
### 2. 实战避坑与进阶建议  
1. **先查保护机制**  
：拿到程序后先用checksec分析保护机制，确定攻击方向（如开启NX用ROP，开启PIE需泄露基地址）。  
  
1. **多调试少盲测**  
：用GDB跟踪程序执行流程，观察栈、堆布局变化，定位漏洞触发点与gadget地址，避免盲目构造Payload。  
  
1. **积累利用链模板**  
：整理常见漏洞（ROP、Double Free、格式化字符串）的利用模板，遇到同类题目可快速复用、修改。  
  
1. **循序渐进刷题**  
：从CTF入门级Pwn题（CTFHub、Pwn.college）入手，逐步过渡到中等难度题，积累实战经验，避免直接挑战高难度题目打击信心。  
  
## 五、福利+互动  
  
高级Pwn技巧的核心是“精准控制”——控制寄存器构造ROP链、控制堆布局实现漏洞利用、控制格式化参数读写内存。掌握本期内容，你能突破Pwn进阶瓶颈，在CTF中稳定拿下Pwn题型分数，也能应对简单的二进制程序漏洞挖掘。  
  
**200节攻防教程，限时领！**  
  
想要的兄弟，**关注我+在后台发“想学”**  
，直接免费分享！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaLzURuoralYxsXugEKYCqnRibXVncWAias3Ey1j0vImVA0bl23vv2ibNurpqgp7jtOFxjNmeicV039fQOJPBBbeb8A/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17 "")  
  
咱学漏洞挖掘和CTF，光看文章不够，这套教程里全是**实战演示**  
——从工具配置到漏洞利用，每一步都手把手教，跟着练就能上手！  
  
（注：资源领取入口在公众号后台，关注后发“学习”自动弹链接）  
  
### 下期预告  
  
第19期将带来《Android高级漏洞：加固绕过+Frida高级Hook+内核漏洞入门》，拆解Android应用常见加固（360、爱加密）的绕过技巧、Frida Hook实战（脱壳、参数篡改）、内核漏洞挖掘基础，覆盖移动端安全核心进阶方向，助力突破移动端漏洞挖掘瓶颈！  
  
