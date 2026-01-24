#  StackWarp漏洞为什么不能影响海光C86  
原创 安全赛博
                        安全赛博  安全赛博   2026-01-24 16:15  
  
SPARC  
（Scalable Processor Architecture，可扩展处理器架构）是一种基于 RISC  
（精简指令集计算机）原则的指令集架构（ISA）。  
  
它最初由 Sun Microsystems  
在 1980 年代中期开发，因其在工作站和高性能服务器（尤其是运行 Solaris 系统的服务器）中的卓越表现而闻名。虽然现在在个人电脑领域很少见，但在一些关键任务、航空航天（如欧洲空间局的 LEON 处理器）以及老牌企业的后端系统中依然存在。  
### SPARC 的核心技术特征  
  
SPARC 之所以独特（也是为什么它会产生像 StackWarp  
这样漏洞的原因），主要源于以下几个设计理念：  
#### 1. 寄存器窗口 (Register Windows) —— 最具代表性的设计  
  
这是 SPARC 的“杀手锏”也是它的“阿克琉斯之踵”。  
- 概念：  
传统处理器（如 x86）在调用函数时，需要显式地把寄存器里的数据存入堆栈（Push）。SPARC 则是直接在硬件内部维护一大堆寄存器，并将其划分为多个“窗口”。  
  
- 操作：  
当函数调用发生时，硬件只需通过一个 save  
指令“滑动”一下窗口，函数就能立刻得到一组全新的寄存器，而无需访问慢速的内存内存。  
  
- 问题：  
当嵌套调用太深，硬件寄存器用完时，就会触发 Window Spill（窗口溢出）  
，迫使内核将寄存器内容写回内存堆栈。StackWarp 漏洞正是利用了这种硬件自动管理内存时的逻辑缺陷。  
  
#### 2. 延迟分支 (Delayed Branching)  
  
为了保持流水线不间断，SPARC 在执行跳转指令（如 jmp  
）时，会紧接着执行跳转指令之后的下一条指令（称为“延迟槽”）。这种设计在早期可以压榨硬件性能，但也增加了编译器编写和代码分析的复杂度。  
#### 3. 严格的 RISC 原则  
- 定长指令：  
所有指令长度固定（通常为 32 位），简化了解码过程。  
  
- 加载/存储架构：  
只有专门的 Load  
和 Store  
指令可以访问内存，所有计算必须在寄存器之间进行。  
  
SPARC 与海光 C86 (x86) 的现状对比  
<table><thead><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><strong style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;margin-bottom: 0px !important;"><span leaf="">特性</span></strong></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><strong style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;margin-bottom: 0px !important;"><span leaf="">SPARC</span></strong></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><strong style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;margin-bottom: 0px !important;"><span leaf="">海光 C86 / x86</span></strong></td></tr></thead><tbody><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,1,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="15,1,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">设计哲学</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,1,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">极简指令，依赖硬件技巧（窗口化）</span></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,1,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">复杂指令（CISC），依赖微码转换</span></span></td></tr><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,2,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="15,2,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">寄存器处理</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,2,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="15,2,1,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">硬件自动滑动窗口</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,2,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="15,2,2,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">软件手动推栈 (Push/Pop)</span></b></span></td></tr><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,3,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="15,3,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">主要用途</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,3,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">关键任务服务器、航天、UNIX 终端</span></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,3,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">桌面电脑、云计算、国产通用服务器</span></span></td></tr><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,4,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="15,4,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">安全性</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,4,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">逻辑漏洞（如 StackWarp）风险高</span></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="15,4,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">侧信道攻击（如 Spectre）风险高</span></span></td></tr></tbody></table>### 核心：谁在搬运数据？  
- SPARC (受影响)：  
硬件在后台自动“偷偷”搬运数据。  
  
- 海光 C86 (不受影响)：  
软件在代码里“显式”搬运数据。  
  
### 1. 代码层面直观对比  
  
我们可以通过一段伪汇编代码，看看同一个函数调用在两个架构下是如何处理寄存器的。  
#### SPARC 架构：硬件自动溢出（StackWarp 的温床）  
  
在 SPARC 中，你只需要执行 save  
指令，硬件就会自动滑动“寄存器窗口”。如果窗口满了，硬件会自动触发一个 Trap（陷阱）  
，由内核把旧数据写到堆栈里。  
```
! SPARC 代码示例
_my_function:
    save %sp, -112, %sp    ! 重点：硬件自动处理寄存器窗口滑动
                           ! 如果此时寄存器窗口已满，硬件会自动将旧寄存器
                           ! “溢出（Spill）”到内存堆栈中。
                           ! StackWarp 攻击的就是这个硬件自动写入的过程。
    ... 执行函数逻辑 ...
    ret                    ! 返回
    restore                ! 硬件自动恢复上一个窗口
```  
  
海光 C86 (x86-64) 架构：软件手动入栈（完全免疫）  
  
在海光 C86 上，没有“寄存器窗口”的概念。如果你想保存寄存器状态，编译器必须生成明确的 push  
指令。  
```
; 海光 C86 (x86-64) 代码示例
_my_function:
    push rbp               ; 显式：由软件指令把寄存器存入堆栈
    mov rbp, rsp
    sub rsp, 32            ; 显式：手动分配栈空间

    ; 此时，除非你代码里写了越界写入漏洞（如 Buffer Overflow），
    ; 否则硬件绝对不会在后台自动往这块内存里写任何东西。

    ... 执行函数逻辑 ...

    add rsp, 32
    pop rbp                ; 显式：由软件指令恢复寄存器
    ret                    ; 显式：跳转回返回地址
```  
  
### 2. 为什么海光 C86 免疫？  
#### ① 缺少“影子写回”机制  
  
StackWarp 攻击的是 SPARC 硬件在 Window Spill  
（窗口溢出）时产生的逻辑缺陷。海光 C86 采用的是寄存器重命名  
技术，寄存器之间的切换是在 CPU 内部的物理寄存器堆（PRF）中完成的，不涉及自动写回内存的操作  
。  
#### ② 权限边界清晰  
- SPARC：  
硬件自动溢出寄存器时，可能会在特权级切换的瞬间产生竞态条件（Race Condition），让攻击者有机会在内核写入前“掉包”堆栈指针。  
  
- 海光 C86：  
寄存器存取完全由指令流控制。CPU 执行 push  
就是用户态权限，执行内核代码就是内核态权限。没有这种“半自动、半特权”的灰色地带。  
  
#### ③ 现代架构的“栈引擎”优化  
  
虽然海光 C86 也有内部的“栈引擎（Stack Engine）”来优化 push/pop  
，但它只是为了加速指针计算。即使发生错误，它也只会导致程序崩溃，而不会像 StackWarp 那样允许攻击者通过“滑动窗口”逻辑来重定向控制流。  
  
3. 架构差异总结表  
<table><thead><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><strong style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;margin-bottom: 0px !important;"><span leaf="">特性</span></strong></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><strong style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;margin-bottom: 0px !important;"><span leaf="">SPARC (StackWarp 受害者)</span></strong></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><strong style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;margin-bottom: 0px !important;"><span leaf="">海光 C86 (x86-64)</span></strong></td></tr></thead><tbody><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,1,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="22,1,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">寄存器架构</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,1,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">寄存器窗口 (Windowed)</span></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,1,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">通用寄存器 (Flat/Renamed)</span></span></td></tr><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,2,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="22,2,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">溢出行为</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,2,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="22,2,1,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">硬件自动触发</span></b><span leaf="">(不可见)</span></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,2,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="22,2,2,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">软件指令驱动</span></b><span leaf="">(显式)</span></span></td></tr><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,3,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="22,3,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">内存访问</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,3,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">硬件在 Trap 时读写堆栈</span></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,3,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">只有 </span><code data-path-to-node="22,3,2,0" data-index-in-node="3" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">mov/push/pop</span></code><span leaf="">指令读写堆栈</span></span></td></tr><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,4,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="22,4,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">攻击面</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,4,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">硬件自动同步的逻辑缺陷</span></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,4,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">缓冲区溢出等软件漏洞</span></span></td></tr><tr style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,5,0,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="22,5,0,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">防护重点</span></b></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,5,1,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">修复硬件 Trap 处理逻辑</span></span></td><td style="border: 1px solid;font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span data-path-to-node="22,5,2,0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><b data-path-to-node="22,5,2,0" data-index-in-node="0" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">CET (影子栈)</span></b><span leaf="">、</span><b data-path-to-node="22,5,2,0" data-index-in-node="10" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">ASLR</span></b><span leaf="">、</span><b data-path-to-node="22,5,2,0" data-index-in-node="15" style="font-family: &#34;Google Sans Text&#34;, sans-serif !important;line-height: 1.15 !important;margin-top: 0px !important;"><span leaf="">Canary</span></b></span></td></tr></tbody></table>  
StackWarp 是一场属于 SPARC 架构的“特定灾难”。  
海光 C86 作为现代 x86 架构的代表，从地基阶段就采用了完全不同的设计哲学，因此该漏洞在海光处理器上根本没有触发的物理基础。  
  
免疫的核心就四个字  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/HI8NQuzWg1uW0jpiaVKWpoA0rMJ5cJCH7LXwe7eOxY8NxI4ZgZYeaIJ90icWooUExEJsoXVF1kqCwq8qt3s2QofA/640?wx_fmt=jpeg&from=appmsg "")  
  
完全自主  
  
