#  Firefox 0Day漏洞：单字符错误引发RCE风险，攻击者可劫持系统  
 FreeBuf   2026-02-19 10:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3CyiaaEBVIu1q6vz9ncwgN3XIX9nhiaXzTWXvGl9h6hNiamKkQbHyMQkCp3jq3LuaViaLSqx9Y6u3DoicOxRNErIWSFyqybFzhDicBM/640?wx_fmt=jpeg&from=appmsg "")  
  
  
Mozilla Firefox 中存在一个严重的远程代码执行（RCE）漏洞，该漏洞源于 SpiderMonkey JavaScript 引擎 WebAssembly 垃圾回收代码中的一个单字符输入错误——开发者误将 "|"（按位或）写成了 "&"（按位与）。  
  
  
安全研究员 Erge 在检查 Firefox 149 Nightly 源代码以获取 CTF 挑战灵感时发现了这一缺陷，并成功利用该漏洞在 Firefox 渲染器进程中执行代码。  
##    
  
**Part01**  
## 漏洞分析  
  
  
该漏洞是在文件 js/src/wasm/WasmGcObject.cpp 中重构 WebAssembly GC 数组元数据时，通过提交 fcc2f20e35ec 引入的。问题代码行为 oolHeaderOld->word = uintptr_t(oolHeaderNew) & 1;，而正确写法应为 oolHeaderOld->word = uintptr_t(oolHeaderNew) | 1;。  
  
  
由于指针对齐，与 1 进行按位与运算的结果始终为 0，导致代码存储了 0 而非预期的设置了最低有效位的转发指针。这个单字符错误通过将 WebAssembly 的 out-of-line（OOL）数组错误标记为 inline（IL）数组，造成了内存损坏漏洞，导致垃圾回收器错误处理内存引用。  
  
  
**Part02**  
## Firefox RCE漏洞详情  
  
  
该漏洞存在于 SpiderMonkey 的 WebAssembly GC 实现中，具体影响 WasmArrayObject::obj_moved() 函数，该函数在垃圾回收器将 Wasm 数组移动到不同内存位置时被调用。  
  
  
当 OOL 数组被重新定位时，垃圾回收器必须在旧缓冲区头部留下转发指针，以便 Ion（SpiderMonkey 的 JIT 编译器）能够找到数据的新位置。转发指针通过将其最低有效位（LSB）设置为 1 来与普通头部区分。  
  
输入错误导致转发指针被设置为 0，这无意中满足了 isDataInline() 函数中将数组识别为内联的条件：return (headerWord & 1) == 0;。该漏洞仅在由 Ion 优化的 WebAssembly 函数中可触发，因为 Baseline 编译器中不存在此机制。  
  
  
**Part03**  
## 漏洞利用过程  
  
  
研究员 Erge 开发了一个概念验证（PoC）漏洞利用程序，通过以下步骤实现了任意读写原语和完整的 RCE：  
  
1. 触发小型垃圾回收，导致 0 被存储在转发指针中  
  
1. Ion 的 wasm::Instance::updateFrameForMovingGC 函数由于零转发指针错误地将数组识别为内联  
  
1. 该函数返回旧数组地址而非新地址，阻止了堆栈帧更新  
  
1. 创建了释放后使用（UAF）条件，因为 Ion 继续使用已释放的数组内存  
  
1. 使用 0x41414141 等值进行堆喷射以回收释放的内存  
  
1. 通过控制解释的 OOL 数组基地址实现任意读写  
  
1. 通过喷射包含二进制相对指针的对象绕过 ASLR  
  
1. 覆盖虚表以劫持 RIP 并执行任意系统命令  
  
最终，该漏洞利用程序通过调用 system() 函数成功生成了一个 shell（/bin/sh）。  
  
  
**Part04**  
## 漏洞披露与修复时间线  
  
  
漏洞披露遵循了快速响应时间线：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yHHJXegyn4jfEHZMSKohgTcSuYlI7TdeMYq2aWTTFJ9pW4IqPP0qV7vsKobR2Vf1WHswnpIYXh6HMglSClFkv5SAzGOcF6IA/640?wx_fmt=png&from=appmsg "")  
  
  
该漏洞仅影响 Firefox 149 Nightly 版本，从未进入任何正式发布版本，因此避免了大规模利用。Mozilla 安全团队迅速响应并修复了该漏洞，两位独立发现该漏洞的安全研究员均获得了分配的赏金奖励。  
  
  
**参考来源：**  
  
Single-Character Typo of “&” Instead of “|” Leads to 0-Day RCE in Firefox  
  
https://cybersecuritynews.com/firefox-0-day-rce/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
