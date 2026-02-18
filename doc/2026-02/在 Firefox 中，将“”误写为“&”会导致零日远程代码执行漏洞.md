#  在 Firefox 中，将“|”误写为“&”会导致零日远程代码执行漏洞  
原创 网络安全9527
                    网络安全9527  安全圈的那点事儿   2026-02-18 10:55  
  
Mozilla Firefox 中的一个严重远程代码执行 (RCE)漏洞是由 SpiderMonkey JavaScript 引擎的 WebAssembly 垃圾回收代码中的一个单字符拼写错误引起的，开发人员错误地输入了“&”（按位与）而不是“|”（按位或）。  
  
安全研究员 Erge 在研究 Firefox 149 Nightly 源代码以寻找 CTF 挑战的灵感时发现了这个漏洞，并成功利用该漏洞在 Firefox 渲染器进程中执行了代码。  
  
该漏洞是在重构文件中的 WebAssembly GC 数组元数据时，在提交 fcc2f20e35ec 中引入的。js/src/wasm/WasmGcObject.cpp 有问题的行读取的是，oolHeaderOld->word = uintptr_t(oolHeaderNew) & 1;而它应该是oolHeaderOld->word = uintptr_t(oolHeaderNew) | 1;。  
  
由于指针对齐的原因，与 1 进行按位与运算的结果始终为 0，导致代码存储零而不是存储预期的、最低有效位已设置的转发指针。  
  
这个单字符错误造成了内存损坏漏洞，因为它错误地将行外 (OOL) WebAssembly 数组标记为行内 (IL) 数组，导致垃圾回收器错误地处理内存引用。  
## Firefox RCE漏洞  
  
SpiderMonkey 的 WebAssembly GC 实现中存在一个 bug，该 bug 会具体影响WasmArrayObject::obj_moved()垃圾回收器在内存位置之间移动 Wasm 数组时调用的函数。  
  
当一个 OOL 数组被重定位时，垃圾回收器必须在旧缓冲区头部留下一个转发指针，以便 Ion（SpiderMonkey 的 JIT 编译器）能够找到数据的新位置。转发指针与普通头部的区别在于，它的最低有效位 (LSB) 设置为 1。  
  
该拼写错误导致转发指针被设置为 0，无意中满足了函数中将数组标识为内联数组的条件isDataInline()：return (headerWord & 1) == 0;。  
  
此漏洞只能在 Ion 优化的 WebAssembly 函数中触发，因为 Baseline 编译器中不存在此机制。  
  
研究人员 Erge 开发了一种概念验证漏洞利用程序，通过以下步骤实现了任意读/写原语和完全远程代码执行：  
1. 触发了一次小型垃圾回收，导致转发指针中存储了 0。  
1. wasm::Instance::updateFrameForMovingGC由于零转发指针，Ion 的函数错误地将数组识别为内联数组。  
1. 该函数返回了旧的数组地址而不是新的地址，从而阻止了栈帧的更新。  
1. 由于 Ion 继续使用已释放的阵列内存，因此产生了释放后使用 (UAF) 的情况。  
1. 使用类似这样的值执行堆喷射，0x41414141以回收已释放的内存  
1. 通过控制解释型 OOL 数组的基地址，实现了任意读/写操作。  
1. 通过喷射包含二进制相对指针的对象来绕过ASLR  
1. 覆盖虚函数表以劫持 RIP 并执行任意系统命令  
最终的漏洞利用/bin/sh通过调用 system() 函数成功生成了一个 shell ( )。  
## 披露和修补时间表  
  
漏洞披露过程十分迅速：  
  
<table><thead style="box-sizing: border-box;border-bottom-width: 3px;border-bottom-style: solid;border-bottom-color: currentcolor;"><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">事件</font></font></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">日期</font></font></th></tr></thead><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">漏洞由提交 fcc2f20e35ec 引入</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">2026年1月19日</font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">独立研究人员提交了漏洞报告</font></font><chrome_annotation data-index="0" data-data="8a2580e1-b376-4f48-af53-52729648310d" data-annotation="2013739" data-type="PHONE_NUMBER" role="link" style="box-sizing: border-box;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: rgb(34, 34, 34);"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">2013739</font></font></chrome_annotation></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">2026年2月3日（预计）</font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">Erge提交了bug报告</font></font><chrome_annotation data-index="1" data-data="5b69bf1e-a8c9-4108-924d-c8a55bc48b23" data-annotation="2014014" data-type="PHONE_NUMBER" role="link" style="box-sizing: border-box;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: rgb(34, 34, 34);"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">2014014</font></font></chrome_annotation><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">72小时内</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">2026年2月3日</font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">漏洞已通过提交 05ffcde 修复</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">2026年2月9日</font></font></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">安全赏金已发放并分配</font></font></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid;word-break: break-word;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;"><font dir="auto" style="box-sizing: border-box;vertical-align: inherit;">2026年2月11日</font></font></td></tr></tbody></table>  
该漏洞仅影响 Firefox 149 Nightly 版本，从未出现在任何正式版中，因此避免了被广泛利用。Mozilla 的安全团队迅速修复了该漏洞，两位独立发现该漏洞的安全研究人员平分了漏洞赏金。  
  
