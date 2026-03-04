#  Chrome 浏览器漏洞利用 (二): Ignition 解释器、Sparkplug 编译器与 TurboFan JIT 优化详解  
Jack Halon
                    Jack Halon  securitainment   2026-03-04 05:37  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://jhalon.github.io/chrome-browser-exploitation-2/</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Jack Halon</span></section></td></tr></tbody></table>  
在我的上一篇文章 "Chrome Browser Exploitation, Part 1: Introduction to V8 and JavaScript Internals" 中，我们首次深入浏览器漏洞利用的世界，涵盖了若干构成基础知识的复杂主题。我们主要探讨了 JavaScript 和 V8 的底层工作原理，包括对象、Map 与 Shape 的概念、对象在内存中的结构布局，以及指针标记 (Pointer Tagging) 和指针压缩 (Pointer Compression) 等基础内存优化技术。此外，我们还简要介绍了编译器流水线、字节码解释器和代码优化。  
  
如果你还没有阅读过上一篇文章，我 **强烈**  
建议你先去阅读。否则，你可能会对本文中的部分内容感到陌生，因为本文是在 Part 1 的知识基础上进一步展开和深入的。  
  
在今天这篇博客中，我们将重新回到编译器流水线，进一步深入之前提到的一些概念，包括 V8 的字节码、代码编译和代码优化。整体而言，本文将深入剖析 Ignition、Sparkplug 和 TurboFan 的底层机制，理解它们对于我们分析某些"特性"如何转化为可利用漏洞至关重要。  
  
本文将讨论以下主题：  
- Chrome 安全模型  
  
- 多进程沙箱架构  
  
- V8 的 Isolate 与 Context  
  
- Ignition 解释器  
  
- 理解 V8 的字节码  
  
- 理解基于寄存器的虚拟机  
  
- Sparkplug  
  
- 1:1 映射  
  
- TurboFan  
  
- 即时编译 (JIT)  
  
- 推测性优化与类型守卫  
  
- 反馈格 (Feedback Lattice)  
  
- "Sea of Nodes" 中间表示 (IR)  
  
- 常见优化  
  
- Typer  
  
- 范围分析  
  
- 边界检查消除 (BCE)  
  
- 冗余消除  
  
- 其他优化  
  
- 控制流优化  
  
- 别名分析与全局值编号  
  
- 死代码消除 (DCE)  
  
- 常见 JIT 编译器漏洞  
  
好了，列完这个冗长而令人生畏的复杂主题清单之后，让我们深吸一口气，直接进入正题！  
> 另外，请花些时间阅读代码中的注释。Chromium 源代码虽然复杂，但其中不乏优秀的注释，能帮助你理解相关代码的功能和作用。  
  
# Chrome 安全模型  
  
在深入编译器流水线的复杂性、其优化方式以及漏洞可能出现的位置之前，我们首先需要退后一步，审视全局。虽然编译器流水线在 JavaScript 执行中扮演着重要角色，但它只是整个浏览器架构拼图中的一块。  
  
如前所述，V8 可以作为独立应用程序运行，但对于整个浏览器而言，V8 实际上是被嵌入到 Chrome 中，然后通过 bindings 被另一个引擎调用。因此，我们需要了解应用程序中的 JavaScript 代码是如何被处理的，其中存在一些细微差别和特定含义，这些信息对于我们理解浏览器中的安全问题至关重要。  
  
为了看到这个"全局"，将拼图的所有碎片拼在一起，我们需要从理解 Chrome 安全模型开始。毕竟，这个系列博客是一段探索浏览器内部机制与漏洞利用的旅程。因此，为了更好地理解为什么某些漏洞比其他漏洞更容易利用，以及为什么仅利用一个漏洞可能无法直接实现远程代码执行，我们需要理解 Chromium 的架构。  
  
众所周知，JavaScript 引擎是系统上执行 JavaScript 代码不可或缺的一部分。虽然它们在使浏览器快速高效方面发挥着重要作用，但同时也可能导致浏览器崩溃、应用程序挂起甚至安全风险。然而，JavaScript 引擎并不是浏览器中唯一可能存在问题或漏洞的组件。其他许多组件，如 API 或正在使用的 HTML 和 CSS 渲染引擎，同样可能存在稳定性问题和可被利用的漏洞——无论是有意还是无意。  
  
构建一个永远不会崩溃的 JavaScript 或渲染引擎几乎是不可能的。同样，构建这类引擎使其免受漏洞和安全问题的侵害也几乎不可能——尤其是因为这些组件大多使用静态类型语言 C++ 编写，而 C++ 需要处理 Web 应用程序的动态特性。  
  
那么 Chrome 是如何应对这个"不可能"的任务——既要保持浏览器高效运行，又要保障浏览器、系统及其用户安全的呢？答案是两种方式：使用多进程架构和沙箱机制。  
## 多进程沙箱架构  
  
Chromium 的多进程架构顾名思义，是一种使用多个进程来保护浏览器免受 JavaScript 引擎、渲染引擎或其他组件可能引发的不稳定性问题和漏洞的架构。Chromium 还通过仅允许特定进程之间相互通信来限制各进程之间的访问。这种架构可以被视为在应用程序中引入了内存保护和访问控制。  
  
一般来说，浏览器有一个主进程负责运行 UI 并管理所有其他进程——这被称为"**浏览器进程 (browser process)**  
"或简称"browser"。名字确实很独特。处理网页内容的进程被称为"**渲染进程 (renderer processes)**  
"或"renderers"。这些渲染进程使用一个叫做 Blink 的开源渲染引擎。Blink 实现了许多辅助库来帮助其运行，例如开源 2D 图形库 Skia，当然还有用于 JavaScript 的 V8。  
  
接下来事情会变得有点复杂。在 Chrome 中，每个新窗口或标签页都会在一个 **新进程**  
中打开——通常是一个新的渲染进程。这个新的渲染进程有一个全局 RenderProcess  
对象，负责管理与父浏览器进程的通信，并维护该窗口或标签页中网页或应用程序的全局状态。相应地，主浏览器进程会为每个渲染器维护一个对应的 RenderProcessHost  
对象，用于管理渲染器的浏览器状态和通信。  
  
在这些进程之间进行通信时，Chromium 使用传统 IPC 系统或 Mojo。我不会深入讨论它们的工作原理，因为说实话，Chrome 的架构和通信方案本身就可以写成一篇单独的博客文章。我将留给读者自行查阅链接并做研究。  
  
总之，纸上谈兵是廉价的，而计算能力是昂贵的。为了帮助更好地可视化我们刚才解释的内容，下面来自 Chromium 开发团队的图片将为我们提供多进程架构的高层概览。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSjDj7Y4KUGxlLoqns6bIuyDZBictFicfjsAdhI670oV7HHOZG4giaWx33B7TrdBhibOFCGmuw9MzP6l6XLq242RRSNfo5s4DIDQibLU/640?wx_fmt=png&from=appmsg "")  
  
除了让每个渲染器运行在自己的进程中之外，Chrome 还利用沙箱来限制进程对系统资源的访问。通过沙箱化每个进程，Chrome 可以确保渲染器访问网络资源的唯一途径是通过主进程中运行的网络服务调度器。此外，沙箱还可以限制进程对文件系统以及用户显示、Cookie 和输入的访问。  
  
总的来说，这限制了攻击者在渲染进程中获得远程代码执行后能做的事情。本质上，如果不利用或串联另一个漏洞来逃出沙箱，他们将无法对计算机进行持久性更改，也无法访问其他窗口和标签页中的用户输入和 Cookie 等信息。  
  
在此我不会再深入更多细节，因为那会偏离本文的当前主题。但我 **强烈建议**  
你深入阅读 "Chromium Windows Sandbox Architecture" 文档，不仅是为了理解设计原则，更是为了更好地理解 broker 和 target 进程的通信方案。  
  
那么在实践中这是什么样子的呢？我们可以通过启动 Chrome、打开两个标签页并启动 Process Monitor 来看一个实际示例。一开始我们应该能看到 Chrome 有一个父进程即"browser"进程，以及若干子进程，如下所示。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSj3JibRpe7tLnCLicCwicnViaJUOthYTPuUdXbrJm9iaGicIsM5taiax2A4YcQANmHCA465gibRAtWgiaziaiba4aRZK4ZSf34ngnr6gGwLlk/640?wx_fmt=png&from=appmsg "")  
  
如果我们查看主父进程，并将其与子进程进行比较，会注意到其他进程运行着不同的命令行参数。在这个例子中，我们可以看到子进程 (右侧) 是渲染器类型，并且匹配其父浏览器进程 (左侧)。很酷，对吧？  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiafZ8GfrOic8CiarHrdLiah5dc71nFria2ku3B6dOvPWKk5IfKZDFRZo58AZ5y6krUuWG2t2fvO8d8ichhEDXZyBEUz4CJ93XU4T5Ik/640?wx_fmt=png&from=appmsg "")  
  
好了，在介绍完所有这些之后，我知道你可能会问这一切和 V8 以及 JavaScript 有什么关系？如果你一直认真在看，那你应该已经注意到了我提到 Chrome 渲染引擎 Blink 时的一个关键点——它实现了 V8。  
  
如果你作为一个好学生花时间阅读了一些 Blink 的文档，那你应该对 Blink 有了一些了解。文档中指出，Blink 在每个渲染进程中运行，并且有一个主线程来处理 JavaScript、DOM、CSS、样式和布局计算。此外，Blink 还可以创建多个"worker"线程来运行额外的脚本、扩展等。  
  
一般来说，每个 Blink 线程都运行自己的 V8 实例。为什么？因为如你所知，在一个单独的浏览器窗口或标签页中，可能有大量 JavaScript 代码在运行，不仅是页面本身的，还有不同 iframe 中的广告、按钮等。归根结底，每个脚本和 iframe 都有各自独立的 JavaScript 上下文，必须有一种方式来防止一个脚本操纵另一个脚本中的对象。  
  
为了帮助将一个脚本的上下文与另一个"隔离"开来，V8 实现了一种称为 Isolate 和 Context 的机制，接下来我们将详细讨论。  
## V8 的 Isolate 与 Context  
  
在 V8 中，**Isolate**  
是一个实例或"虚拟机"的概念，代表一个 JavaScript 执行环境，包括堆管理器、垃圾回收器等。在 Blink 中，Isolate 和线程具有 1:1  
的关系，即一个 Isolate 关联主线程，一个 Isolate 关联一个 worker 线程。  
  
**Context**  
对应一个全局根对象，它持有虚拟机的状态，用于在单个 V8 实例中编译和执行脚本。粗略地说，一个 window 对象对应一个 Context，由于每个 frame 都有一个 window 对象，因此一个渲染进程中可能存在多个 Context。在与 Isolate 的关系方面，Isolate 和 Context 在 Isolate 的生命周期内具有 1:N  
的关系——即特定的 Isolate 或实例将解释和编译多个 Context。  
  
这意味着每次需要执行 JavaScript 时，我们都需要通过 GetCurrentContext() 验证我们是否在正确的 Context 中，否则最终可能会泄漏 JavaScript 对象或覆盖它们，进而可能导致安全问题。  
  
在 Chrome 中，运行时对象 v8::Isolate  
实现在 v8/include/v8-isolate.h 中，v8::Context  
对象实现在 v8/include/v8-context.h 中。利用我们所学的知识，从高层视角来看，我们可以将 Chrome 中的运行时和 Context 层级关系可视化如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaBDxdUS1eD5lvLPTjEFWn1zSw5viarAZYUNo0GRXS7EcrZB9ABK3TiaqoETxsDHjKvGpweXLObYwXnzGzJcZ6PU1xFaED8ATdTg/640?wx_fmt=png&from=appmsg "")  
  
如果你想更深入地了解 Isolate 和 Context 的工作原理，建议阅读 "Design of V8 Bindings" 和 "Getting Started with Embedding V8"。  
# Ignition 解释器  
  
现在我们已经对 Chromium 的架构有了大致了解，并且知道了并非所有 JavaScript 代码都在同一个 V8 引擎实例中执行，我们终于可以回到编译器流水线中继续深入探讨了。  
  
我们将从更深入地理解 V8 的解释器 Ignition 开始。  
  
作为 Part 1 的回顾，让我们再看一下 V8 编译流水线的高层概览，以便了解我们在流水线中的当前位置。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShXjXgOvFI3EyqK0VlvVn7tRrkjtpHJaHib0bQul90QaemX3JhCnwk6BH69573cGVDvujEiaFW8dbd7zfwQA1GrYDB5rc5iaaiankg/640?wx_fmt=png&from=appmsg "")  
  
我们在 Part 1 中已经介绍了 Token 和抽象语法树 (AST)，并简要说明了 AST 是如何被解析并在解释器中转换为字节码的。现在我想要深入讲解 V8 的字节码，因为解释器生成的字节码是构成任何 JavaScript 功能的关键构建块。此外，当 Ignition 编译字节码时，它还会在每次运行 JavaScript 函数时收集性能分析和反馈数据。这些反馈数据随后被 TurboFan 用于生成 JIT 优化的机器码。  
  
但是，在开始理解字节码的结构之前，我们首先需要理解 Ignition 是如何实现其"寄存器机"的。原因在于每条字节码都将其输入和输出指定为寄存器操作数，因此我们需要知道这些输入和输出在栈上的位置。这也将帮助我们进一步可视化和理解 V8 中生成的栈帧。  
## 理解基于寄存器的虚拟机  
  
如我们所知，Ignition 解释器是一个带有累加器寄存器的基于寄存器的解释器。这些"寄存器"并不是人们通常认为的传统机器寄存器。相反，它们是寄存器文件中的特定 **槽位 (slot)**  
，作为函数栈帧的一部分进行分配——本质上它们是"虚拟"寄存器。正如我们稍后将看到的，字节码可以指定这些输入和输出寄存器，其参数将在这些寄存器上进行操作。  
  
Ignition 由一组 **字节码处理器 (bytecode handler)**  
组成，这些处理器使用高级的、与机器无关的汇编代码编写。这些处理器由 CodeStubAssembler  
类实现，并在浏览器编译时通过 TurboFan 的后端进行编译。总体而言，每个处理器"处理"一个特定的字节码，然后调度到下一个字节码的相应处理器。  
  
v8/src/interpreter/interpreter-generator.cc  
中 LdaZero  
即"将零加载到累加器"的字节码处理器示例如下。  
```
// LdaZero
// Load literal '0' into the accumulator.
IGNITION_HANDLER(LdaZero, InterpreterAssembler)
{
  TNode<Number> zero_value = NumberConstant(0.0);
  SetAccumulator(zero_value);
  Dispatch();
}
```  
  
当 V8 创建新的 Isolate 时，它会从构建时创建的快照文件中加载处理器。Isolate 还将包含一个全局解释器调度表，该表保存指向每个字节码处理器的代码对象指针，按字节码值进行索引。一般来说，这个调度表只是一个 enum。  
  
为了让 Ignition 运行字节码，JavaScript 函数首先通过 BytecodeGenerator  
从其 AST 转换为字节码。这个生成器遍历 AST，并通过调用 GenerateBytecode  
函数为每个 AST 节点发出相应的字节码。  
  
随后，该字节码与函数 (即 JSFunction 对象) 通过一个名为 SharedFunctionInfo  
的属性字段关联。之后，JavaScript 函数的 code_entry_point  
被设置为 InterpreterEntryTrampoline  
内建桩 (built-in stub)。  
  
当 JavaScript 函数被调用时，会进入 InterpreterEntryTrampoline  
桩，它负责设置适当的解释器栈帧，同时调度到该函数第一条字节码的解释器字节码处理器。然后开始由 Ignition 执行或"解释"该函数，这一过程在 v8/src/builtins/x64/builtins-x64.cc  
源文件中处理。  
  
具体来说，在 builtins-x64.cc  
的第 1255-1387 行，Builtins::Generate_InterpreterPushArgsThenCallImpl  
和 Builtins::Generate_InterpreterPushArgsThenConstructImpl  
函数负责通过将参数和函数状态压入栈来进一步构建解释器栈帧。  
  
关于字节码生成器我不会再深入太多，但如果你想扩展知识，建议阅读 "Ignition Design Documentation: Bytecode Generation" 部分，以更好地理解其底层工作原理。本节我想重点关注的是函数的寄存器分配和栈帧创建。  
  
那么这个栈帧是如何生成的呢？  
  
在字节码生成过程中，BytecodeGenerator  
还会在函数的寄存器文件中为局部变量、Context 对象指针以及表达式求值所需的临时值分配寄存器。  
  
InterpreterEntryTrampoline  
桩处理栈帧的初始构建，然后在栈帧中为寄存器文件分配空间。该桩还会将 undefined  
写入寄存器文件中的所有寄存器，以便垃圾回收器 (GC) 在遍历栈时不会看到任何无效的 (即非标记的) 指针。  
  
字节码通过在其操作数中指定寄存器来对它们进行操作，Ignition 随后从与该寄存器关联的特定栈槽中加载或存储数据。由于寄存器索引直接映射到函数栈帧槽，Ignition 可以直接访问栈上的其他槽，例如 Context 和随函数传入的参数。  
  
函数栈帧的示例如下 (由 Chromium 团队提供)。请注意 "Interpreter Stack Frame"——这是由 InterpreterEntryTrampoline  
构建的栈帧。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiagDjFKNZTYNQEUiat2hSL1icWwOatQepJfY4aanPjl0ib5tcKbXpwKp5R2EaFIYBM1yAfLqq7cIwMkubSzyBeBwNVze7NSYMu7Ik/640?wx_fmt=png&from=appmsg "")  
  
如你所见，红色部分是函数的参数，绿色部分是局部变量和用于表达式求值的临时变量。  
  
浅绿色部分包含 Isolate 当前的 Context 对象、调用者指针计数器，以及指向 JSFunction  
对象的指针。这个指向 JSFunction  
的指针也称为 **闭包 (closure)**  
，它链接到函数的 Context、SharedFunctionInfo  
对象以及其他访问器如 FeedbackVector  
。这个 JSFunction  
在内存中的示例如下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjIZKS20Vv2p9lB7niaxd8CYCPibKZXzMIHkKVicDnKzf196YpMZJkO8wjYEy6wQGYxFRFG6LFibdxEefUgCdO4YKPVPRHg5tVaWo8/640?wx_fmt=png&from=appmsg "")  
  
你可能还注意到栈帧中没有累加器寄存器。原因是累加器寄存器在函数调用过程中会不断变化，因此它作为状态寄存器保存在解释器中。这个状态寄存器由 **帧指针 (Frame Pointer, FP)**  
指向，帧指针还持有栈指针和帧计数器。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShyrUBqLRJAvj566EQquRUuLUSBg2vm7A9d9aic7Z0IhR2f04oIwSxfO5fqVFy6jkqaKiaAcYNSX52FmOHdvv3bQGHMFzRNohW1U/640?wx_fmt=png&from=appmsg "")  
  
回到之前的栈帧示例，你还会注意到有一个 **Bytecode Array**  
指针。这个 BytecodeArray  
表示栈帧中特定函数的一系列解释器字节码。最初每条字节码都是一个 enum  
，字节码的索引存储对应的处理器——如前所述。  
  
这个 BytecodeArray  
的示例可以在 v8/src/objects/code.h  
中看到，下面是该代码的片段。  
```
// BytecodeArray represents a sequence of interpreter bytecodes.
class BytecodeArray
    : public TorqueGeneratedBytecodeArray<BytecodeArray, FixedArrayBase> {
 public:
  static constexpr int SizeFor(int length) {
    return OBJECT_POINTER_ALIGN(kHeaderSize + length);
  }

  inline byte get(int index) const;
  inline void set(int index, byte value);

  inline Address GetFirstBytecodeAddress();

  inline int32_t frame_size() const;
  inline void set_frame_size(int32_t frame_size);
```  
  
如你所见，GetFirstBytecodeAddress()  
函数负责获取数组中第一条字节码的地址。那么它是如何找到该地址的呢？  
  
让我们快速看一下为 var num = 42  
生成的字节码。  
```
d8> var num = 42;
[generated bytecode for function:  (0x03650025a599 <SharedFunctionInfo>)]
Bytecode length: 18
Parameter count 1
Register count 3
Frame size 24
Bytecode age: 0
         000003650025A61E @    0 : 13 00             LdaConstant [0]
         000003650025A620 @    2 : c4                Star1
         000003650025A621 @    3 : 19 fe f8          Mov <closure>, r2
         000003650025A624 @    6 : 66 5f 01 f9 02    CallRuntime [DeclareGlobals], r1-r2
         000003650025A629 @   11 : 0d 2a             LdaSmi [42]
         000003650025A62B @   13 : 23 01 00          StaGlobal [1], [0]
         000003650025A62E @   16 : 0e                LdaUndefined
         000003650025A62F @   17 : aa                Return
```  
  
先不用担心这些字节码各自的含义，我们稍后会解释。看一下字节码数组中的第 1 行，它存储了 LdaConstant  
。在它左边我们看到 13 00  
。十六进制数 0x13  
是字节码枚举器，表示该字节码处理器所在的位置。  
  
一旦接收到该值，就会调用 SetBytecodeHandler()  
并传入字节码、操作数及其处理器枚举。该函数位于 v8/src/interpreter/interpreter.cc  
文件中; 其示例如下。  
```
void Interpreter::SetBytecodeHandler(Bytecode bytecode,
                                     OperandScale operand_scale,
                                     CodeT handler) {
  DCHECK(handler.is_off_heap_trampoline());
  DCHECK(handler.kind() == CodeKind::BYTECODE_HANDLER);
  size_t index = GetDispatchTableIndex(bytecode, operand_scale);
  dispatch_table_[index] = handler.InstructionStart();
}

size_t Interpreter::GetDispatchTableIndex(Bytecode bytecode,
                                          OperandScale operand_scale) {
  static const size_t kEntriesPerOperandScale = 1u << kBitsPerByte;
  size_t index = static_cast<size_t>(bytecode);
  return index + BytecodeOperands::OperandScaleAsIndex(operand_scale) *
                     kEntriesPerOperandScale;
}
```  
  
如你所见，dispatch_table_[index]  
将从存储在物理寄存器中的调度表计算字节码的索引，最终这将启动或完成 Dispatch()  
函数来执行字节码。  
  
字节码数组还包含一个叫做"**常量池指针 (Constant Pool Pointer)**  
"的东西，它存储在生成的字节码中被引用为常量的堆对象，例如字符串和整数。常量池是一个指向堆对象的指针 FixedArray  
。这个 BytecodeArray  
指针及其堆对象常量池的示例如下。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgXs8veV6h6aIvCeB1poaP9I34MYv9U7FbsPAUmFicbFB1Nfx246nwuWVZU4NYsEe2tLAp2sbX7IRwoCjXQKWbI8EibDxXG8R9Q8/640?wx_fmt=png&from=appmsg "")  
  
在继续之前，我还想提一件事：InterpreterEntryTrampoline  
桩有一些 Ignition 使用的固定机器寄存器。这些寄存器位于 v8/src/codegen/x64/register-x64.h  
文件中。  
  
下面是这些寄存器的示例，感兴趣的寄存器已添加了注释。  
```
// Define {RegisterName} methods for the register types.
DEFINE_REGISTER_NAMES(Register, GENERAL_REGISTERS)
DEFINE_REGISTER_NAMES(XMMRegister, DOUBLE_REGISTERS)
DEFINE_REGISTER_NAMES(YMMRegister, YMM_REGISTERS)

// Give alias names to registers for calling conventions.
constexpr Register kReturnRegister0 = rax;
constexpr Register kReturnRegister1 = rdx;
constexpr Register kReturnRegister2 = r8;
constexpr Register kJSFunctionRegister = rdi;
// Points to the current context object
constexpr Register kContextRegister = rsi;
constexpr Register kAllocateSizeRegister = rdx;
// Stores the implicit accumulator interpreter register
constexpr Register kInterpreterAccumulatorRegister = rax;
// The current offset of execution in the BytecodeArray
constexpr Register kInterpreterBytecodeOffsetRegister = r9;
// Points the the start of the BytecodeArray object which is being interpreted
constexpr Register kInterpreterBytecodeArrayRegister = r12;
// Points to the interpreter's dispatch table, used to dispatch to the next bytecode handler
constexpr Register kInterpreterDispatchTableRegister = r15;
```  
  
现在我们理解了这些，是时候深入了解 V8 字节码的样子以及字节码操作数如何与寄存器文件交互了。  
## 理解 V8 的字节码  
  
如 Part 1 所述，V8 中有数百种字节码，它们都定义在 v8/src/interpreter/bytecodes.h  
头文件中。正如我们稍后将看到的，每条字节码都将其输入和输出操作数指定为寄存器文件中的寄存器。此外，许多操作码的名称以 Lda  
或 Sta  
开头，其中 a  
代表 **累加器 (accumulator)**  
。  
  
例如，让我们跟踪 LdaSmi  
的字节码定义：  
```
V(LdaSmi, ImplicitRegisterUse::kWriteAccumulator, OperandType::kImm)
```  
  
如你所见，LdaSmi  
将"加载" (即名称中的 Ld  
) 一个值到累加器寄存器中。在这种情况下，它将加载一个 kImm  
操作数，即一个有符号字节，这与字节码名称中的 Smi  
即小整数 (Small Integer) 相对应。总结来说，这条字节码将一个小整数加载到累加器寄存器中。  
  
请注意，操作数及其类型的列表定义在 v8/src/interpreter/bytecode-operands.h  
头文件中。  
  
有了这些基本信息，让我们看看一个实际 JavaScript 函数的字节码。首先，让我们使用 --print-bytecode  
标志启动 d8  
，这样我们就能看到字节码。启动后，随便输入一些 JavaScript 代码并按几次回车。原因是 V8 是一个"惰性"引擎，所以它不会编译不需要的东西。但因为我们是第一次使用字符串和数字，它会编译像 Stringify  
这样的库，这会导致一开始有大量输出。  
  
完成后，让我们创建一个名为 incX  
的简单 JavaScript 函数，它将对象的属性 x  
加一并返回给我们。函数应如下所示。  
```
function incX(obj) { return 1 + obj.x; }
```  
  
这会生成一些字节码，但我们先不管它。现在有了这个函数，让我们用一个具有属性 x 赋值的对象来调用它，并查看生成的字节码。  
```
d8> incX({x:13});
...
[generated bytecode for function: incX (0x026c0025ab65 <SharedFunctionInfo incX>)]
Bytecode length: 11
Parameter count 2
Register count 1
Frame size 8
Bytecode age: 0
         0000026C0025ACC6 @    0 : 0d 01             LdaSmi [1]
         0000026C0025ACC8 @    2 : c5                Star0
         0000026C0025ACC9 @    3 : 2d 03 00 01       GetNamedProperty a0, [0], [1]
         0000026C0025ACCD @    7 : 39 fa 00          Add r0, [0]
         0000026C0025ACD0 @   10 : aa                Return
Constant pool (size = 1)
0000026C0025AC99: [FixedArray] in OldSpace
 - map: 0x026c00002231 <Map(FIXED_ARRAY_TYPE)>
 - length: 1
           0: 0x026c000041ed <String[1]: #x>
Handler Table (size = 0)
Source Position Table (size = 0)
14
```  
  
我们将忽略大部分输出，只关注字节码部分。但在此之前，请注意这段字节码位于 SharedFunctionInfo  
对象中，这与我们之前的解释一致！首先我们看到调用了 LdaSmi  
将一个小整数加载到累加器寄存器中，值为 1。  
  
接下来，我们调用 Star0  
，它会将累加器中的值存储 (即 st  
) 到寄存器 r0  
中 (即 a  
代表累加器)。所以在这里我们将 1 移动到 r0  
。  
  
GetNameProperty  
字节码从 a0  
获取命名属性并存储到累加器中，即值 13。a0  
指的是函数的第 i  
个参数。所以如果我们传入 a,b,x  
，想要加载 x  
，字节码操作数将显示 a2  
，因为我们是函数中的第 2 个参数 (请记住这是一个参数数组)。在这种情况下，a0  
将在表中查找命名属性，其中索引 0  
映射到 x  
。  
```
 - length: 1
           0: 0x026c000041ed <String[1]: #x>
```  
  
简而言之，这就是加载 obj.x  
的字节码。另一个 [0]  
操作数被称为 **反馈向量 (feedback vector)**  
，它包含运行时信息和对象 Shape 数据，供 TurboFan 用于优化。  
  
接下来，我们将寄存器 r0  
中的值与累加器相 Add  
，结果值为 14。最后，我们调用 Return  
返回累加器的值，然后退出函数。  
  
为了帮助你在栈帧上可视化这个过程，我提供了一个 GIF 动画，展示了每条字节码指令在简化栈上的执行过程。  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/h4gtbB74nShIqMcVoQmeXoPCnv31Nt5IslfibCa1R77BeVAKs2mF9vvBnOwBtiap2V4R7Xn1xanDSz0aEJneXj3fYxUDnPvxDxHHA9qvB8L0c/640?wx_fmt=gif&from=appmsg "")  
  
如你所见，虽然字节码一开始看起来有些晦涩，但一旦我们掌握了每条字节码的作用，就很容易理解和跟踪了。如果你想了解更多关于 V8 字节码的内容，建议阅读 "JavaScript Bytecode - v8 Ignition Instructions"，其中涵盖了大量不同的操作。  
# Sparkplug  
  
现在我们已经对 Ignition 如何生成和执行 JavaScript 代码字节码有了不错的理解，是时候开始研究 V8 编译器流水线中的编译部分了。我们从 Sparkplug 开始，因为它相对容易理解，只对已生成的字节码和栈做一些小的修改以进行优化。  
  
如 Part 1 所述，Sparkplug 是 V8 的超快非优化编译器，位于 Ignition 和 TurboFan 之间。本质上，Sparkplug 并不是真正的编译器，更像是一个转译器，将 Ignition 的字节码转换为机器码以便原生运行。同时，作为非优化编译器，它不会进行非常特定的优化，因为那是 TurboFan 的工作。  
  
那么是什么让 Sparkplug 如此之快呢？Sparkplug 之所以快，是因为它"作弊"。它编译的函数已经被编译为字节码，而且 Ignition 已经完成了变量解析、控制流等繁重工作。因此，Sparkplug 是从字节码而不是从 JavaScript 源代码进行编译。  
  
其次，Sparkplug 不产生任何中间表示 (IR)，这与大多数编译器不同 (我们稍后会详细介绍)。Sparkplug 在字节码上进行单次线性遍历，直接编译为机器码。这通常被称为 1:1  
映射。  
  
有趣的是，Sparkplug 本质上就是一个 for  
循环内的 switch  
语句，它调度到固定的字节码然后生成机器码。我们可以在 v8/src/baseline/baseline-compiler.cc  
源文件中看到这个实现。  
  
Sparkplug 的机器码生成函数示例如下。  
```
switch (iterator().current_bytecode()) {
#define BYTECODE_CASE(name, ...)       \
  case interpreter::Bytecode::k##name: \
    Visit##name();                     \
    break;
    BYTECODE_LIST(BYTECODE_CASE)
#undef BYTECODE_CASE
  }
```  
  
那么 Sparkplug 是如何生成机器码的呢？当然是再次"作弊"。Sparkplug 几乎不生成自己的代码，而是直接调用通常由 InterpreterEntryTrampoline  
进入的字节码内建函数，然后在 v8/src/builtins/x64/builtins-x64.cc  
中处理。  
  
如果你还记得我们在讨论 Ignition 时提到的 JSFunction  
对象，你会记得闭包链接到了"优化后的代码"。本质上，Sparkplug 会将字节码的内建函数存储在那里，当函数被执行时，我们不再调度到字节码，而是直接调用内建函数。  
  
此时你可能会认为 Sparkplug 本质上就是一个美化版的解释器，这么说也没错。Sparkplug 基本上只是通过调用相同的内建函数来序列化解释器的执行。但这使得 JavaScript 函数变得更快，因为这样做可以避免解释器的开销，如操作码解码和字节码调度查找——使我们能够从模拟引擎转向原生执行，从而降低 CPU 使用率。  
  
要了解更多关于这些内建函数的工作原理，建议阅读 "Short Builtin Calls"。  
## 1:1 映射  
  
Sparkplug 的 1:1  
映射不仅仅涉及它如何将 Ignition 的字节码编译为机器码变体；它还涉及栈帧。如我们所知，编译器流水线的每个部分都需要存储函数状态。正如我们在 V8 中已经看到的，JavaScript 函数状态存储在 Ignition 的栈帧中，包括当前被调用的函数、调用它的 Context、传入的参数数量、指向字节码数组的指针等等。  
  
现在，如我们所知，Ignition 是一个基于寄存器的解释器，其虚拟寄存器用于函数参数以及作为字节码操作数的输入和输出。为了提高速度并避免自己做任何寄存器分配，Sparkplug 复用了 Ignition 的寄存器帧，这反过来又使 Sparkplug 能够镜像解释器的行为和栈。这使得 Sparkplug 不需要在两个帧之间进行任何映射——使这些栈帧几乎 1:1  
兼容。  
  
请注意我说的是"几乎 1:1  
兼容"，Ignition 和 Sparkplug 栈帧之间有一个小区别。区别在于 Sparkplug 不需要在寄存器文件中保留字节码偏移槽，因为 Sparkplug 的代码是直接从字节码发出的。取而代之的是，它将其替换为缓存的反馈向量。  
  
这两个栈帧的对比示例如下图所示——来自 Ignition 文档。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSheJ4bGzia4icuHtDSayHIwqypF4D9m7xWyDxzAPhqQemOOQPiaeImXjblJ1XJDyUavZ11skOMia2jwXyvAl7UGLvhuiaicdvbgUUXoI/640?wx_fmt=png&from=appmsg "")  
  
那么为什么 Sparkplug 需要创建和维护与 Ignition 相似的栈帧布局呢？一个原因，也是 Sparkplug 和 TurboFan 工作方式的核心原因，就是通过一种叫做栈上替换 (on-stack replacement, OSR) 的技术。OSR 是在运行时将当前正在执行的代码替换为不同版本的能力。在这种情况下，当 Ignition 发现某个 JavaScript 函数被大量使用时，它会将其发送给 Sparkplug 来加速。  
  
一旦 Sparkplug 将字节码序列化为其内建函数，它就会替换该特定函数的解释器栈帧。当栈被遍历和执行时，代码将直接跳转到 Sparkplug 而不是在 Ignition 的模拟栈上执行。由于帧是"镜像"的，这在技术上允许 V8 在解释器和 Sparkplug 代码之间几乎零帧转换开销地切换。  
  
在继续之前，我想指出 Sparkplug 的安全方面。一般来说，生成的代码本身不太可能存在安全问题。Sparkplug 更大的安全风险在于 Ignition 栈帧布局的解释方式，这可能导致类型混淆或栈上的代码执行。  
  
一个例子是 Issue 1179595，这是由于无效的寄存器计数检查导致的潜在 RCE。还有一个关于 Sparkplug 进行 RX/WX 位翻转方式的担忧——但我不会深入讨论，因为这真的不太重要，这类漏洞在整个系列中不起重要作用。  
  
好了，我们现在理解了 Ignition 和 Sparkplug 的工作方式。现在是时候更深入地进入编译器流水线，理解优化编译器 TurboFan 了。  
# TurboFan  
  
TurboFan 是 V8 的即时编译 (JIT) 编译器，它结合了一种被称为 "Sea of Nodes" 的有趣中间表示概念，以及多层翻译和优化流水线，帮助 TurboFan 从字节码生成更高质量的机器码。对于那些认真阅读代码和文档的读者来说，你会知道 TurboFan 远不止是一个编译器。  
  
TurboFan 实际上还负责解释器的字节码处理器、内建函数、代码桩和内联缓存系统——这些都通过它的宏汇编器实现！所以当我说 TurboFan 是编译器流水线中最重要的部分时，这绝非夸张。  
  
那么，像 TurboFan 这样的优化编译器是如何工作的呢？  
  
优化编译器通过一种叫做"分析器 (profiler)"的东西来工作——我们在 Part 1 中简要提到过。本质上，这个分析器通过提前观察应该被优化的代码来工作 (我们将这类代码或 JavaScript 函数称为"**热 (hot)**  
"代码)。它通过查看内联缓存和反馈向量收集的信息，从 JavaScript 函数和栈中收集元数据和"样本"。  
  
然后编译器构建一个中间表示 (IR) 数据结构，用于生成优化后的代码。这整个观察代码然后编译机器码的过程被称为即时编译或 JIT 编译。  
## 即时编译 (JIT)  
  
如我们所知，在解释器虚拟机中执行字节码比在原生机器上执行汇编要慢。原因是 JavaScript 是动态的，属性查找、对象和值的检查等操作有大量开销，而且我们还是在模拟栈上运行。  
  
当然，Map 和内联缓存 (IC) 通过加速属性、对象和值的动态查找来帮助解决部分开销——但它们仍然无法提供峰值性能。原因是每个 IC 独立运作，它不了解也不关心其邻近操作的情况。  
  
以 Map 为例，如果我们向一个已知 Shape 添加属性，仍然需要遍历转换表并查找或添加额外的 Shape。如果对于特定函数或对象需要反复进行多次这样的操作，即使 Shape 已知，我们基本上是在一次又一次地浪费计算周期。  
  
因此，当一个 JavaScript 函数被执行了很多次时，可能值得花时间将该函数传入编译器并编译为机器码，从而使其执行速度大幅提升。  
  
例如，让我们看这段代码：  
```
function hot_function(obj) {
 return obj.x;
}

for (let i=0; i < 10000; i++) {
 hot_function({x:i});
}
```  
  
hot_function  
简单地接收一个对象并返回属性 x  
的值。接下来，我们执行该函数大约 10k 次，每次传入的对象都为属性 x  
赋一个新的整数值。在这种情况下，因为该函数被大量使用且对象的总体 Shape 没有变化，V8 可能会决定将其向上传递到流水线中 (称为 "tier-up") 进行编译，以使其执行更快。  
  
我们可以通过 d8  
中的 --trace-opt  
标志来跟踪优化过程。那就让我们这么做，同时加上 --allow-natives-syntax  
命令，这样我们就可以查看函数在优化前后的代码。  
  
我们先启动 d8  
然后设置函数。之后，对 hot_function  
使用 %DisassembleFunction  
来查看其类型。你应该会得到类似的输出。  
```
d8> function hot_function(obj) {return obj.x;}
d8> %DisassembleFunction(hot_function)
0000027B0020B31D: [CodeDataContainer] in OldSpace
 - map: 0x027b00002a71 <Map[32](CODE_DATA_CONTAINER_TYPE)>
 - kind: BUILTIN
 - builtin: InterpreterEntryTrampoline
 - is_off_heap_trampoline: 1
 - code: 0
 - code_entry_point: 00007FFCFF5875C0
 - kind_specific_flags: 0
```  
  
如你所见，最初这个代码对象将由 Ignition 执行，因为它是一个 BUILTIN  
并且将由我们熟知的 InterpreterEntryTrampoline  
处理。现在，如果我们执行这个函数 10k 次，我们将看到它被 TurboFan 优化。  
```
d8> for (let i=0; i < 10000; i++) {hot_function({x:i});}
[marking 0x027b0025aa4d <JSFunction (sfi = 0000027B0025A979)> for optimization to TURBOFAN, ConcurrencyMode::kConcurrent, reason: small function]
[compiling method 0x027b0025aa4d <JSFunction (sfi = 0000027B0025A979)> (target TURBOFAN) OSR, mode: ConcurrencyMode::kConcurrent]
[completed compiling 0x027b0025aa4d <JSFunction (sfi = 0000027B0025A979)> (target TURBOFAN) OSR - took 1.691, 81.595, 2.983 ms]
[completed optimizing 0x027b0025aa4d <JSFunction (sfi = 0000027B0025A979)> (target TURBOFAN) OSR]
9999
```  
  
如你所见，TurboFan 启动并开始编译函数进行优化。请注意优化跟踪中的几个关键点。如第一行所示，我们正在标记 JSFunction  
的 SFI  
即 SharedFunctionInfo  
进行优化。  
  
如果你还记得我们对 Ignition 的深入讲解，你会记得 SFI 包含了我们函数的字节码。TurboFan 将使用该字节码来生成 IR，然后将其优化为机器码。  
  
接下来，再往下看，你会看到提到了 OSR  
即栈上替换。TurboFan 在优化字节码时做的事情和 Sparkplug 基本相同。它会用一个真正的 JIT 或系统栈帧替换原来的栈帧，该帧在运行时指向优化后的代码。这使得函数下次被调用时可以直接执行优化后的代码，而不是在 Ignition 的模拟栈中执行。  
  
如果我们再次对 hot_function  
运行 %DisassembleFunction  
，我们应该看到它现在已被优化，SharedFunctionInfo  
中的代码入口点将指向优化后的机器码。  
```
d8> %DisassembleFunction(hot_function)
0000027B0025B2B5: [CodeDataContainer] in OldSpace
 - map: 0x027b00002a71 <Map[32](CODE_DATA_CONTAINER_TYPE)>
 - kind: TURBOFAN
 - is_off_heap_trampoline: 0
 - code: 0x7ffce0004241 <Code TURBOFAN>
 - code_entry_point: 00007FFCE0004280
 - kind_specific_flags: 4
```  
  
对于眼尖的人来说，你可能在跟踪函数优化时注意到了一些有趣的事情。如果你仔细观察，会发现 TurboFan 并没有立即启动，而是在几秒钟后——或者说在循环迭代了几千次之后才启动。这是为什么？  
  
原因是 TurboFan 会等待代码"预热"。如果你还记得我们对 Ignition 和 Sparkplug 的讨论，我们简要提到过反馈向量 (feedback vector)。这个向量存储对象运行时数据以及来自内联缓存的信息，并收集所谓的 **类型反馈 (type feedback)**  
。  
  
这对 TurboFan 至关重要，因为如我们所知，JavaScript 是动态的，我们无法存储静态类型信息。其次，在运行时之前我们不知道值的类型。JIT 编译器实际上必须对其编译的代码的使用方式和行为做出 **有根据的猜测**  
，例如函数类型是什么、传入的变量类型是什么等等。本质上，编译器做了大量的假设或"**推测 (speculation)**  
"。  
  
这就是为什么优化编译器会查看内联缓存收集的信息，并使用反馈向量来帮助做出明智的决策，以确定需要对代码进行什么样的处理才能使其变快。这就是所谓的推测性优化 (Speculative Optimization)。  
## 推测性优化与类型守卫  
  
那么推测性优化是如何帮助我们将 JavaScript 代码转化为高度优化的机器码的呢？为了帮助解释这一点，让我们从一个例子开始。  
  
假设我们有一个名为 add  
的函数的简单求值表达式，如 return 1 + i  
。这里我们通过将 1  
加到 i  
来返回一个值。在不知道 i  
的类型的情况下，我们需要遵循 ECMAScript 标准中 EvaluateStringOrNumericBinaryExpression 的运行时语义实现。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiacAoBVPDq5YjB4o7BiaVnuWYZWLg8ulzyvh1wvYxDuEofQQlOjAWLDtFw7JHGYiagdxjLvA2yAicn1MWfaLTQDZtUVLY0LEiaghCI/640?wx_fmt=png&from=appmsg "")  
  
如你所见，一旦我们对操作数的左右引用进行求值，并对左右值调用 GetValue，我们接下来需要遵循 ECMAScript 标准执行 ApplyStringOrNumericBinaryOperator 来返回我们的值。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShibDvictrRwAib473O5Y3kfVFupX55LFEk32mJjapZvwbprZuaGMBDibJiaK2hbzJWCicbEyCddd70U7gGibngibQTJVvFX66QQKaG2ias/640?wx_fmt=png&from=appmsg "")  
  
如果这对你来说还不够明显的话，在不知道变量 i  
的类型 (无论是整数还是字符串) 的情况下，我们无法仅用几条机器指令来实现整个求值过程，更不用说让它快速运行了。  
  
这就是推测性优化发挥作用的地方，TurboFan 将依赖反馈向量来对 i  
的可能类型做出假设。  
  
例如，如果在几百次运行后我们查看 Add  
字节码的反馈向量，知道 i  
是一个数字，那么我们就不需要处理 ToString 甚至 ToPrimitive 求值。在这种情况下，优化器可以获取一条 IR 指令并声称 i  
和返回值只是数字，直接按数字方式加载。这大大减少了我们需要生成的机器指令数量。  
  
那么在我们的函数中，这些反馈向量看起来是什么样的呢？  
  
如果你还记得之前提到的 JSFunction  
对象或闭包，你会记得闭包还链接到了反馈向量槽以及 SharedFunctionInfo  
。在反馈向量中，有一个有趣的槽叫做 BinaryOp  
槽，它记录了二元运算 (如 +  
、-  
、*  
等) 的输入和输出反馈。  
  
我们可以通过对 add  
函数运行 %DebugPrint  
来查看反馈向量中的内容并看到这个特定的槽。你的输出应该与下面类似。  
```
d8> function add(i) {return 1 + i;}
d8> for (let i=0; i<100; i++) {add(i);}
d8> %DebugPrint(add)
DebugPrint: 0000019A002596F1: [Function] in OldSpace
 - map: 0x019a00243fa1 <Map[32](HOLEY_ELEMENTS)> [FastProperties]
 - prototype: 0x019a00243ec9 <JSFunction (sfi = 0000019A0020AA45)>
 - elements: 0x019a00002259 <FixedArray[0]> [HOLEY_ELEMENTS]
 - function prototype:
 - initial_map:
 - shared_info: 0x019a0025962d <SharedFunctionInfo add>
 - name: 0x019a00005809 <String[3]: #add>
 - builtin: InterpreterEntryTrampoline
 - formal_parameter_count: 1
 - kind: NormalFunction
 - context: 0x019a00243881 <NativeContext[273]>
 - code: 0x019a0020b31d <CodeDataContainer BUILTIN InterpreterEntryTrampoline>
 - interpreted
 - bytecode: 0x019a0025a89d <BytecodeArray[9]>
 - source code: (i) {return 1 + i;}
 - properties: 0x019a00002259 <FixedArray[0]>
   ...
 - feedback vector: 0000019A0025B759: [FeedbackVector] in OldSpace
 - map: 0x019a0000273d <Map(FEEDBACK_VECTOR_TYPE)>
 - length: 1
 - shared function info: 0x019a0025962d <SharedFunctionInfo add>
 - no optimized code
 - tiering state: TieringState::kNone
 - maybe has maglev code: 0
 - maybe has turbofan code: 0
 - invocation count: 97
 - profiler ticks: 0
 - closure feedback cell array: 0000019A00003511: [ClosureFeedbackCellArray] in ReadOnlySpace
 - map: 0x019a00002981 <Map(CLOSURE_FEEDBACK_CELL_ARRAY_TYPE)>
 - length: 0

 - slot #0 BinaryOp BinaryOp:SignedSmall {
     [0]: 1
  }
   ...
```  
  
这里有一些有趣的信息。调用计数 (Invocation count) 显示了我们运行 add  
函数的次数，如果我们查看反馈向量，会看到恰好有一个槽，就是我们提到的 BinaryOp  
。查看该槽内部，我们看到它包含当前反馈类型 SignedSmall  
，本质上就是指 SMI。  
  
请记住，这些反馈信息不是由 V8 解释的，而是由 TurboFan 解释的，如我们所知，SMI 是一个有符号 32 位值，这在本系列 Part 1 的指针标记部分已经解释过。  
  
总的来说，这些通过反馈向量进行的推测在通过消除不同类型的不必要机器指令来加速代码方面非常有效。不幸的是，仅仅将针对一种类型的指令应用于动态对象是相当不安全的。  
  
那么，如果在优化后的函数执行到一半时我们传入一个字符串而不是数字会怎样？本质上，如果发生这种情况，我们就会面临一个类型混淆漏洞。为了防止可能错误的假设，TurboFan 在特定指令执行之前预置了一个叫做 **类型守卫 (type guard)**  
的东西。  
  
这个类型守卫检查确保我们传入的对象的 Shape 是正确的类型。这在对象到达我们的优化操作之前完成。如果对象不匹配预期的 Shape，那么优化代码的执行就 **无法继续**  
。在这种情况下，我们将从汇编代码中"退出"(bail out)，跳回解释器中未优化的字节码并在那里继续执行。这被称为"**去优化 (deoptimization)**  
"。  
  
优化后的汇编代码中类型守卫和跳转到去优化的示例如下。  
```
REX.W movq rcx,[rbp-0x38]       ; Move i to rcx
testb rcx,0x1                   ; Check if rcx is an SMI
jnz 00007FFB0000422A  <+0x1ea>  ; If check fails, bailout
```  
  
类型守卫触发的去优化不仅限于检查对象类型是否不匹配。它们同样作用于算术运算和边界检查。  
  
例如，如果我们的优化代码是针对 32 位整数的算术运算进行优化的，而发生了溢出，我们可以去优化并让 Ignition 来处理计算——从而保护我们免受机器上潜在的安全问题。这类可能导致去优化的问题被称为"副作用 (side-effects)"(我们稍后会更详细地介绍)。  
  
与优化过程一样，我们也可以在 d8  
中使用 --trace-deopt  
标志来观察去优化的实际过程。完成后，让我们重新添加 add  
函数并运行以下循环。  
```
for (let i=0; i<10000; i++) {
 if (i<7000) {
  add(i);
 } else {
  add("string");
 }
}
```  
  
这段代码简单地让函数先针对数字进行优化，然后在 7k 次迭代后，我们开始传入字符串——这应该会触发退出。你的输出应该与下面类似。  
```
d8> function add(i) {return 1 + i;}
d8> for (let i=0; i<10000; i++) {if (i<7000) {add(i);} else {add("string");}}
[marking 0x03e20025ac55 <JSFunction (sfi = 000003E20025AB5D)> for optimization to TURBOFAN, ConcurrencyMode::kConcurrent, reason: small function]
[compiling method 0x03e20025ac55 <JSFunction (sfi = 000003E20025AB5D)> (target TURBOFAN) OSR, mode: ConcurrencyMode::kConcurrent]
[completed compiling 0x03e20025ac55 <JSFunction (sfi = 000003E20025AB5D)> (target TURBOFAN) OSR - took 1.987, 70.704, 2.731 ms]
[completed optimizing 0x03e20025ac55 <JSFunction (sfi = 000003E20025AB5D)> (target TURBOFAN) OSR]
[bailout (kind: deopt-eager, reason: Insufficient type feedback for call): begin. deoptimizing 0x03e20025ac55 <JSFunction (sfi = 000003E20025AB5D)>, 0x7ffb00004001 <Code TURBOFAN>, opt id 0, node id 63, bytecode offset 40, deopt exit 3, FP to SP delta 96, caller SP 0x00ea459fe250, pc 0x7ffb00004274]
[compiling method 0x03e20025ac55 <JSFunction (sfi = 000003E20025AB5D)> (target TURBOFAN) OSR, mode: ConcurrencyMode::kConcurrent]
[completed compiling 0x03e20025ac55 <JSFunction (sfi = 000003E20025AB5D)> (target TURBOFAN) OSR - took 0.325, 121.591, 1.425 ms]
[completed optimizing 0x03e20025ac55 <JSFunction (sfi = 000003E20025AB5D)> (target TURBOFAN) OSR]
"1string"
```  
  
如你所见，函数被优化了，后来我们触发了退出。由于调用时类型不足，代码被去优化回字节码。然后，有趣的事情发生了——函数再次被优化。为什么？  
  
因为这个函数仍然是"热"的，还有几千次迭代要执行。TurboFan 所做的是，既然它现在已经在类型反馈中收集了数字和字符串两种类型，它会再次优化代码。但这次它会添加允许字符串求值的代码。在这种情况下，将添加第二个类型守卫——所以第二次运行的代码现在同时针对数字 **和**  
字符串进行了优化！  
  
关于这一点，一个很好的示例和解释可以在视频 "Inside V8: The choreography of Ignition and TurboFan" 中看到。  
  
我们还可以通过对 add  
函数运行 %DebugPrint  
命令来查看 BinaryOp  
槽中更新后的反馈。你应该会看到类似下面的内容。  
```
d8> %DebugPrint(add)
DebugPrint: 000003E20025970D: [Function] in OldSpace
 - map: 0x03e200243fa1 <Map[32](HOLEY_ELEMENTS)> [FastProperties]
 - prototype: 0x03e200243ec9 <JSFunction (sfi = 000003E20020AA45)>
 - elements: 0x03e200002259 <FixedArray[0]> [HOLEY_ELEMENTS]
 - function prototype:
 - initial_map:
 - shared_info: 0x03e20025962d <SharedFunctionInfo add>
 - name: 0x03e200005809 <String[3]: #add>
 - builtin: InterpreterEntryTrampoline
 - formal_parameter_count: 1
 - kind: NormalFunction
 - context: 0x03e200243881 <NativeContext[273]>
 - code: 0x03e20020b31d <CodeDataContainer BUILTIN InterpreterEntryTrampoline>
 - interpreted
 - bytecode: 0x03e20025aca5 <BytecodeArray[9]>
 - source code: (i) {return 1 + i;}
 - properties: 0x03e200002259 <FixedArray[0]>
   ...
 - feedback vector: 000003E20025ACF1: [FeedbackVector] in OldSpace
 - map: 0x03e20000273d <Map(FEEDBACK_VECTOR_TYPE)>
 - length: 1
 - shared function info: 0x03e20025962d <SharedFunctionInfo add>
 - no optimized code
 - tiering state: TieringState::kNone
 - maybe has maglev code: 0
 - maybe has turbofan code: 0
 - invocation count: 5623
 - profiler ticks: 0
 - closure feedback cell array: 000003E200003511: [ClosureFeedbackCellArray] in ReadOnlySpace
 - map: 0x03e200002981 <Map(CLOSURE_FEEDBACK_CELL_ARRAY_TYPE)>
 - length: 0

 - slot #0 BinaryOp BinaryOp:Any {
     [0]: 127
  }
```  
  
如你所见，BinaryOp  
现在存储的反馈类型是 Any  
，而不是 SignedSmall  
和 String  
。为什么？这是由于一种叫做反馈格 (Feedback Lattice) 的东西。  
## 反馈格 (Feedback Lattice)  
  
反馈格存储了操作的所有可能反馈状态。它从 None  
开始，表示尚未看到任何内容，然后向下走到 Any  
状态，表示它已经看到了输入和输出的组合。Any  
状态表示该函数应被视为多态的 (polymorphic)，相比之下，任何其他状态都表示该函数是单态的 (monomorphic)——因为它只产生了某种特定的值。  
  
如果你想了解更多关于单态和多态代码之间的区别，强烈建议阅读 "What's up with Monomorphism?" 这篇精彩文章。  
  
下面我提供了反馈格大致样子的可视化示例。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSg1ohyJzIO6ePvBko9w0ia91AicDbMFYGeakonGns7OwpsGHSGmfp02dMSRmo6LIPxhLsanVpu0LdXAbYKfQAciahVJZU0zh9sos4/640?wx_fmt=png&from=appmsg "")  
  
就像 Part 1 中的数组格一样，这个格的工作方式相同。反馈只能在格中向下推进。一旦我们从 Number 变为 Any，就永远无法回退。如果由于某种奇妙的原因我们确实回退了，那么我们就有可能进入所谓的 _去优化循环_，优化编译器会消耗无效的反馈并持续从优化后的代码中退出。  
  
你可以在 v8/src/compiler/use-info.h  
文件中查看更多关于类型检查的信息。此外，如果你想了解更多关于 V8 的反馈系统和内联缓存，建议观看 "V8 and How It Listens to You - Michael Stanton"。  
## "Sea of Nodes" 中间表示 (IR)  
  
现在我们知道了 TurboFan 如何收集类型反馈来做出推测性假设，让我们看看 TurboFan 如何根据这些反馈构建其特化的 IR。生成 IR 的原因在于这种数据结构抽象了代码复杂性，从而使执行编译器优化变得更加容易。  
  
TurboFan 的 "Sea of Nodes" IR 基于静态单赋值 (Static Single Assignment, SSA) 形式，SSA 是 IR 的一个属性，要求每个变量只被赋值一次且在使用之前定义。这对于冗余消除等优化非常有用。  
  
以我们上面示例中的 add  
函数为例，其 SSA 形式如下。  
```
// function add(i) {return 1 + i;}
var i1 = argument
var r1 = 1 + i1
return r1
```  
  
然后这种 SSA 形式被转换为图格式，类似于控制流图 (control-flow graph, CFG)，其中使用节点和边来表示代码及计算之间的依赖关系。这种图格式使 TurboFan 能够将其同时用于数据流分析和机器码生成。  
  
那么，让我们看看这个 Sea of Nodes 是什么样子的。我们将使用 hot_function  
示例。首先创建一个新的 JavaScript 文件，并添加以下内容。  
```
function hot_function(obj) {
 return obj.x;
}

for (let i=0; i < 10000; i++) {
 hot_function({x:i});
}
```  
  
完成后，我们将通过 d8  
使用 --trace-turbo  
标志运行这个脚本，该标志允许我们跟踪和保存 TurboFan JIT 生成的 IR。你的输出应该与下面类似。运行结束时，它应该会生成一个命名格式为 turbo-*.json  
的 JSON 文件。  
```
C:\dev\v8\v8\out\x64.debug>d8 --trace-turbo hot_function.js
Concurrent recompilation has been disabled for tracing.
---------------------------------------------------
Begin compiling method add using TurboFan
---------------------------------------------------
Finished compiling method add using TurboFan
```  
  
完成后，在浏览器中打开 Turbolizer，按 CTRL + L  
并加载你的 JSON 文件。这个工具将帮助我们可视化 TurboFan 生成的 Sea of Nodes 图。  
  
你看到的图应该与我的基本一致。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaey9nwiczEH2lEwyqTRYmC48UklbvdiaplOPRpIhaiaib6TicZxxA9tRSkbU0xmmiaKA5Wfl44Bmn7eI82zpbKHMeaP27sLC1XngAeI/640?wx_fmt=png&from=appmsg "")  
  
在 Turbolizer 中，左侧是你的源代码，右侧 (图中未显示) 是 TurboFan 生成的优化后的机器码。中间是 Sea of Nodes 图。  
  
目前有很多节点被隐藏了，只显示控制节点，这是默认行为。如果你点击"refresh"符号右边的 "Show All Nodes" 复选框，就能看到所有节点。  
  
在 Turbolizer 中浏览图时，你会注意到有五种不同颜色的节点，它们代表以下含义：  
- **黄色**  
: 这些节点代表控制节点，即任何可以改变脚本"流程"的东西——例如 if/else 语句。  
  
- **浅蓝色**  
: 这些节点代表某个节点可以拥有或返回的值，例如堆常量或内联值。  
  
- **红色**  
: 代表 JavaScript 重载运算符的语义，即在 JavaScript 层面执行的任何操作，如 JSCall  
、JSAdd  
等。这些类似于字节码操作。  
  
- **蓝色**  
: 表示虚拟机级别的操作，如分配、边界检查、从栈加载数据等。这有助于跟踪 TurboFan 消耗的反馈。  
  
- **绿色**  
: 对应单条机器级别的指令。  
  
如我们所见，Sea of Nodes 中的每个节点可以代表算术运算、加载、存储、调用、常量等。然后有三种边 (由节点之间的箭头表示) 需要了解，它们表达了依赖关系。这些边是：  
- **控制 (Control)**  
: 就像在 CFG 中一样，这些边实现分支和循环。  
  
- **值 (Value)**  
: 就像在数据流图中一样，这些边显示值的依赖关系和输出。  
  
- **效果 (Effect)**  
: 详细说明读取或写入状态等操作的顺序。  
  
有了这些知识，让我们稍微展开图并查看其他一些节点，以理解执行流程。请注意，我隐藏了一些不太重要的节点。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaOMFgia7ReIm41aQfPRqAWW1zKAl7Sn2pXr2M4xiaLBln0iba95xnQhM3IecdjGIIA99wFYqHNGxyzn3PIicEzsBbLQ4gDksGaAe0/640?wx_fmt=png&from=appmsg "")  
  
如我们所见，黄色节点是管理函数流程的控制节点。首先我们有 Loop  
节点，告诉我们正在进入一个循环。从那里，控制边指向 Branch  
和 LoopExit  
节点。Branch  
就是字面意思，它将循环"分支"为一个 True/False 语句。  
  
如果我们沿着 Branch  
节点向上看，会看到一个 SpeculativeNumberLessThan  
节点，它有一条值边指向值为 10000  
的 NumberConstant  
。这与我们的函数一致，因为我们循环了 10k 次。由于这个节点是绿色的，它是一条机器指令，代表我们循环的 **类型守卫**  
。  
  
从 SpeculativeNumberLessThan  
节点可以看到有一条效果边指向 LoopExitEffect  
，这意味着如果数字超过 10k，我们就退出循环，因为我们刚刚打破了假设。  
  
当值小于 10k 且 SpeculativeNumberLessThan  
为 true 时，我们将加载对象，并调用 JSDefineNamedOwnProperty  
来获取对象到属性 x  
的偏移量。然后调用 JSCall  
将 1 加到属性值并返回该值。从该节点还有一条效果边指向 SpeculativeSafeIntegerAdd  
。这个节点有一条值边指向值为 1 的 NumberConstant  
节点，这是我们在返回值时进行的数学加法。  
  
再次注意，我们有一个 SpeculativeSafeIntegerAdd  
节点来检查确保我们进行的加法运算确实是在添加一个 SMI 而不是其他东西，否则它会触发类型守卫并去优化。  
  
对于那些可能好奇 Phi  
节点是什么的人，它基本上是一个 SSA 节点，合并了由不同分支计算出的某个值的两种 (或多种) 可能性。在这种情况下，它合并了两个潜在的整数推测。  
  
如你所见，一旦理解了基础知识，理解这些图并不太复杂。  
  
现在，如果你查看 Sea of Nodes 窗口的左上角，会看到我们处于 V8.TFBytecodeGraphBuilder  
选项。这个选项展示了从字节码生成的 IR，没有应用任何优化。从下拉菜单中，我们可以选择此代码经历的其他不同优化阶段来查看相关的 IR。  
# 常见优化  
  
好了，现在我们已经介绍了 TurboFan 的 Sea of Nodes，对如何导航和理解生成的 IR 至少有了基本的了解。从这里开始，我们可以深入理解 TurboFan 的一些常见优化。这些优化本质上是在从字节码产生的原始图上进行操作。  
  
由于生成的图现在具有来自类型守卫的静态类型信息，优化以更经典的提前编译方式进行，以提高代码的执行速度或减小内存占用。之后，一旦图被优化完成，生成的图会被降低为机器码 (称为"降低/lowering")，然后写入 V8 的可执行内存区域，以便在编译后的函数被调用时执行。  
  
需要注意的是，降低可以分多个阶段进行，中间还有进一步的优化，这使得编译器流水线相当灵活。  
  
了解了这些之后，让我们看看其中一些常见的优化。  
## Typer  
  
最早的优化阶段之一叫做 TyperPhase  
，由 OptimizeGraph  
函数运行。该阶段遍历代码，从堆对象中识别操作的结果类型，例如 Int32 + Int32 = Int32。  
  
当 Typer  
运行时，它会访问图中的每个节点，并尝试通过简化操作逻辑来"化简"它们。然后它会调用节点关联的 typer 调用来将一个 Type  
与之关联。  
  
例如，在我们的案例中，循环和返回算术中的常量整数将被 Typer::Visitor::TypeNumberConstant  
访问，它将返回一个 Range  
类型——如下面来自 v8/src/compiler/types.cc  
的代码示例所示。  
```
Type Type::Constant(double value, Zone* zone) {
  if (RangeType::IsInteger(value)) {
    return Range(value, value, zone);
  } else if (IsMinusZero(value)) {
    return Type::MinusZero();
  } else if (std::isnan(value)) {
    return Type::NaN();
  }
```  
  
那么我们的推测节点呢？  
  
对于这些节点，它们由 OperationTyper  
处理。在我们的案例中，返回值的算术推测将调用 OperationTyper::SpeculativeSafeIntegerAdd  
，它将类型设置为"安全整数"范围，例如 Int64  
。该类型会被检查，如果在执行过程中它不是 Int64  
，我们就去优化。这本质上允许算术运算具有正负返回值，并防止潜在的上溢/下溢问题。  
  
了解了这些，让我们查看 V8.TFTyper  
优化阶段的图及其节点关联的类型。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShBrRIe1JicawhZpdlHtrZ8kwvicjXce7WjbVMmS9BXJVNqrjJicEIcqo0gL5h3kj8dDzkuDOWmmkBic8icbpLYhvWrzFZOjcBfJRCs/640?wx_fmt=png&from=appmsg "")  
## 范围分析  
  
在 Typer  
优化过程中，编译器遍历代码，识别操作的范围并计算结果值的边界。这就是所谓的范围分析 (Range Analysis)。  
  
如果你注意到了上图中的 Range  
类型，特别是 SpeculativeSafeIntegerAdd  
节点具有 Int64  
变量的范围。之所以这样做，是因为范围分析优化器计算了加法或返回值的最小值和最大值。  
  
在我们的案例中，我们返回的是对象属性 x  
的值 i  
加 1。类型反馈只能知道返回值是一个整数，仅此而已，它无法确定值的范围。因此，为了安全起见，它决定给出尽可能大的值范围以防止问题。  
  
那么，让我们通过以下代码来再看看范围分析：  
```
function hot_function(obj) {
 let values = [0,13,1337]
 let a = 1;
 if (obj == "leet")
  a = 2;
 return values[a];
}
```  
  
如我们所见，根据传入的 obj  
参数的类型，如果 obj  
是一个等于 "leet" 的字符串，那么 a  
将等于 1337，否则等于 13。代码的这部分将经过 SSA 处理并合并到一个 Phi  
节点中，该节点包含 a  
的可能范围。常量将其范围设置为各自的硬编码值，但这些常量也会由于算术计算而影响我们的推测范围。  
  
如果我们查看范围分析后该代码生成的图，应该能看到以下内容。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShaqmGwM9PsSQ5VYDmIEuILMNeqa73OYAbePbY1wlMnADFW5fdTYAR8XCpoL7BvIOjU9NN7Kwaz8R6WuCl0tZibMOsNfsJ9qlas/640?wx_fmt=png&from=appmsg "")  
  
如你所见，由于 SSA 我们有了 Phi  
节点。在范围分析期间，typer 访问 TypePhi  
节点函数，并创建操作数 13 和 1337 的联合，从而得到 a  
的可能范围。  
  
对于推测节点，OperationTyper  
调用 AddRanger  
函数来计算 Range  
类型的最小和最大边界。在这种情况下，你可以看到 typer 为 a  
在两种可能的迭代值下算术运算后的返回值计算了范围。  
  
有了这些，如果范围分析失败且我们获得了编译器不期望的值，我们就去优化。非常简单易懂！  
## Bounds Checking Elimination (BCE)  
  
在简化降低 (simplified lowering) 阶段，Typer  
还会执行另一项常见优化——CheckBounds  
操作，该操作作用于 CheckBound  
推测节点。当范围分析证实数组索引处于数组边界范围内时，这种优化通常会应用于数组访问操作。  
  
之所以使用"**曾经**  
"这个措辞，是因为 Chromium 团队已决定禁用此优化，以 加固 TurboFan 的边界检查能力，抵御 typer 缺陷。确实存在一些可绕过该加固措施的"缺陷"，但这里不做展开。如果你想深入了解，建议阅读 "Circumventing Chrome's Hardening of Typer Bugs"。  
  
无论如何，我们以下面的代码为例，演示一下这种优化原本是如何工作的：  
```
function hot_function(obj) {
 let values = [0,13,1337]
 let a = 1;
 if (obj == "leet")
  a = 2;
 return values[a];
}
```  
  
可以看到，这段代码与范围分析中使用的代码十分相似。我们同样为 hot_function  
接收一个参数，当对象匹配字符串 "leet" 时将 a  
设为 2 并返回 1337，否则将 a  
设为 1 并返回 13。  
  
需要特别注意的是，a  
永远不等于 0，因此我们永远——或至少理论上不应该——返回 0。这在查看图时会产生一个有趣的场景。下面来看 IR 的逃逸分析 (escape analysis) 部分，观察图的形态。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaa5OHIUsTe6lXnZgOLbXs7Z1icMkhVDZxg6RiaCYIiaLnE8mRQaArMSUKpecXGRC6BTLvtLyTU4hlA5NibwfImoCWPeP7yOCKcQqE/640?wx_fmt=png&from=appmsg "")  
  
可以看到，这里又出现了一个 Phi  
节点来合并 a  
的可能取值，接着有一个 CheckBounds  
节点用于检查数组边界。若索引在 1 或 2 的范围内，则调用 LoadElement  
从数组中加载元素；否则将触发 bailout，因为边界检查不接受索引 0。  
  
如果你已经注意到了，可能会好奇为什么 LoadElement  
的类型是 Signed31  
而非 Signed32  
。原因很简单：Signed31  
表示第一位用于标记符号位。也就是说，对于 32 位有符号整数，实际可用的值位只有 31 位而非 32 位。此外可以看到，LoadElement  
的输入是一个长度为 3 的 FixedArray HeapConstant  
，即我们的 values  
数组。  
  
逃逸分析完成后，流程进入简化降低 (simplified lowering) 阶段。这个降低阶段的作用——简单来说 (一语双关)——是将所有值表示转换为机器操作符所要求的正确机器表示。该阶段的代码位于 v8/src/compiler/simplified-lowering.cc  
中，边界检查消除 (Bounds Checking Elimination) 正是在此阶段进行的。  
  
那么，编译器是如何判定一个 CheckBounds  
节点为冗余的呢？  
  
对于每个 CheckBounds  
节点，编译器都会调用 VisitCheckBounds  
函数。该函数负责验证索引的最小范围是否大于等于零、最大范围是否不超过数组长度。若验证通过，则触发 DeferReplacement  
，将该节点标记为待移除。  
  
下面展示的是加固提交 7bb6dc0e06fa158df508bc8997f0fce4e33512a5 之前的 VisitCheckBounds  
函数示例。  
```
  void VisitCheckBounds(Node* node, SimplifiedLowering* lowering) {
    CheckParameters const& p = CheckParametersOf(node->op());
    Type const index_type = TypeOf(node->InputAt(0));
    Type const length_type = TypeOf(node->InputAt(1));
    if (length_type.Is(Type::Unsigned31())) {
      if (index_type.Is(Type::Integral32OrMinusZero())) {
        // Map -0 to 0, and the values in the [-2^31,-1] range to the
        // [2^31,2^32-1] range, which will be considered out-of-bounds
        // as well, because the {length_type} is limited to Unsigned31.
        VisitBinop(node, UseInfo::TruncatingWord32(),
                   MachineRepresentation::kWord32);
        if (lower()) {
          if (lowering->poisoning_level_ ==
                  PoisoningMitigationLevel::kDontPoison &&
              (index_type.IsNone() || length_type.IsNone() ||
               (index_type.Min() >= 0.0 &&
                index_type.Max() < length_type.Min()))) {
            // The bounds check is redundant if we already know that
            // the index is within the bounds of [0.0, length[.
            DeferReplacement(node, node->InputAt(0)); // <= Removes Nodes
          } else {
            NodeProperties::ChangeOp(
                node, simplified()->CheckedUint32Bounds(p.feedback()));
          }
        }
      ...
  }
```  
  
可以看到，我们的 CheckBound  
范围会进入 if  
分支，其中 Range(1,2).Min() >= 0  
且 Range(1,2).Max() < 3  
。在这种情况下，上图中的节点 [#46]()  
 将被判定为冗余并移除。  
  
现在再看提交之后更新的代码，会发现一个细微的变化：DeferReplacement  
调用已被移除，取而代之的是将该节点替换为 CheckedUint32Bounds  
节点。若检查失败，TurboFan 会调用 kAbortOnOutOfBounds  
，直接中止边界检查并触发崩溃，而非执行去优化。  
  
新代码如下：  
```
  void VisitCheckBounds(Node* node, SimplifiedLowering* lowering) {
    CheckBoundsParameters const& p = CheckBoundsParametersOf(node->op());
    FeedbackSource const& feedback = p.check_parameters().feedback();
    Type const index_type = TypeOf(node->InputAt(0));
    Type const length_type = TypeOf(node->InputAt(1));

    // Conversions, if requested and needed, will be handled by the
    // representation changer, not by the lower-level Checked*Bounds operators.
    CheckBoundsFlags new_flags =
        p.flags().without(CheckBoundsFlag::kConvertStringAndMinusZero);

    if (length_type.Is(Type::Unsigned31())) {
      if (index_type.Is(Type::Integral32()) ||
          (index_type.Is(Type::Integral32OrMinusZero()) &&
           p.flags() & CheckBoundsFlag::kConvertStringAndMinusZero)) {
        // Map the values in the [-2^31,-1] range to the [2^31,2^32-1] range,
        // which will be considered out-of-bounds because the {length_type} is
        // limited to Unsigned31. This also converts -0 to 0.
        VisitBinop<T>(node, UseInfo::TruncatingWord32(),
                      MachineRepresentation::kWord32);
        if (lower<T>()) {
          if (index_type.IsNone() || length_type.IsNone() ||
              (index_type.Min() >= 0.0 &&
               index_type.Max() < length_type.Min())) {
            // The bounds check is redundant if we already know that
            // the index is within the bounds of [0.0, length[.
            // TODO(neis): Move this into TypedOptimization?
            new_flags |= CheckBoundsFlag::kAbortOnOutOfBounds; // <= Abort & Crash
          }
          ChangeOp(node,
                   simplified()->CheckedUint32Bounds(feedback, new_flags)); // <= Replace Node
        }
      ...
  }
```  
  
查看图的简化降低部分，可以确认 CheckBounds  
节点确实已按代码逻辑被替换为 CheckedUint32Bounds  
节点，其余所有节点的值也已"降低"为机器码表示。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShsaGkJVCEia0eBHhrRqAjiac0rnrSw6jLLoQfaqvS5U7G6O2iauL3kyeFqTVibMl8YFJpheWtKN0LgLOD1dIUribbrA934IiaHswevY/640?wx_fmt=png&from=appmsg "")  
## Redundancy Elimination  
  
另一类与 BCE 相似的常见优化是冗余消除 (Redundancy Elimination)。其代码位于 v8/src/compiler/redundancy-elimination.cc  
，负责移除冗余的类型检查。RedundancyElimination  
类本质上是一个图归约器 (graph reducer)，它会尝试移除或合并效果链中的冗余检查。  
  
效果链 (effect chain) 本质上是 load 和 store 函数之间效果边 (effect edges) 的操作顺序。例如，如果我们尝试从一个对象加载属性并对其执行加法运算，比如 obj[x] = obj[x] + 1  
，那么效果链将是 JSLoadNamed => SpeculativeSafeIntegerAdd => JSStoreNamed  
。TurboFan 必须确保这些节点的外部效果不被重排，否则可能导致守卫 (guards) 位置不当。  
  
归约器 (reducer) 的定义详见 v8/src/compiler/graph-reducer.h  
，它根据节点的操作符和输入尝试对其进行简化。归约器有多种类型，例如 常量折叠 (constant folding)——如果两个常量相加，就会将它们折叠为一个节点，即 3 + 5  
变为单个值为 8  
的常量节点；还有强度降低 (strength reduction)——如果一个无副作用的节点被加上某个值，就只保留单个节点，即 x + 0  
只保留节点 x  
。  
  
我们可以通过 --trace_turbo_reduction  
标志来追踪这些归约过程。如果用该标志再次运行前面的 hot_function  
，你应该会看到类似如下的输出。  
```
C:\dev\v8\v8\out\x64.debug>d8 --trace_turbo_reduction hot_function.js
- Replacement of #12: Parameter[-1, debug name: %closure](0) with #41: HeapConstant[0x00c800259781 <JSFunction hot_function (sfi = 000000C800259679)>] by reducer JSContextSpecialization
- Replacement of #34: JSLoadProperty[sloppy, FeedbackSource(#2)](14, 30, 5, 4, 35, 31, 26) with #47: LoadElement[tagged base, 8, Signed31, kRepTaggedSigned|kTypeInt32, FullWriteBarrier](44, 46, 46, 26) by reducer JSNativeContextSpecialization
- Replacement of #42: Checkpoint(33, 31, 26) with #31: Checkpoint(33, 21, 26) by reducer CheckpointElimination
- In-place update of #36: NumberConstant[0] by reducer Typer
... snip ...
- In-place update of #26: Merge(24, 27) by reducer BranchElimination
- In-place update of #43: CheckMaps[None, 0x00c80024dcb9 <Map[16](PACKED_SMI_ELEMENTS)>, FeedbackSource(INVALID)](61, 62, 26) by reducer RedundancyElimination
- Replacement of #43: CheckMaps[None, 0x00c80024dcb9 <Map[16](PACKED_SMI_ELEMENTS)>, FeedbackSource(INVALID)](61, 62, 26) with #62: CheckInternalizedString(2, 18, 8) by reducer LoadElimination
- In-place update of #44: LoadField[JSObjectElements, tagged base, 8, Internal, kRepTaggedPointer|kTypeAny, PointerWriteBarrier, mutable](61, 62, 26) by reducer RedundancyElimination
- Replacement of #44: LoadField[JSObjectElements, tagged base, 8, Internal, kRepTaggedPointer|kTypeAny, PointerWriteBarrier, mutable](61, 62, 26) with #50: HeapConstant[0x00c800259811 <FixedArray[3]>] by reducer LoadElimination
- In-place update of #45: LoadField[JSArrayLength, tagged base, 12, Range(0, 134217725), kRepTaggedSigned|kTypeInt32, NoWriteBarrier, mutable](61, 62, 26) by reducer RedundancyElimination
- Replacement of #45: LoadField[JSArrayLength, tagged base, 12, Range(0, 134217725), kRepTaggedSigned|kTypeInt32, NoWriteBarrier, mutable](61, 62, 26) with #59: NumberConstant[3] by reducer LoadElimination
... snip ...
```  
  
该标志会产生大量有趣的输出，如你所见，有许多不同的归约器和消除操作在执行。我们稍后会简要介绍其中一部分，但这里我想让你仔细看其中几条归约记录。  
  
例如这条：  
```
In-place update of #43: CheckMaps[None, 0x00c80024dcb9 <Map[16](PACKED_SMI_ELEMENTS)>, FeedbackSource(INVALID)](61, 62, 26) by reducer RedundancyElimination
```  
  
没错，你没看错——CheckMaps  
被 RedundancyElimination  
归约器更新并随后替换了。原因是冗余消除检测到 CheckMaps  
调用是一个冗余检查，于是移除了同一控制流路径中除第一个之外的所有 CheckMaps  
。  
  
此时你们中一些人可能在想："这难道不是一个安全漏洞吗？"答案是"有可能"并且"要看具体情况"。  
  
在我详细解释之前，让我们先看下面的代码示例：  
```
function hot_function(obj) {
 return obj.a + obj.b;
}
```  
  
可以看到，这段代码很简单：接收一个对象，返回其属性 a  
和属性 b  
的值之和。查看 Typer 优化图，我们会看到如下结构。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShUdvAuMCEiaDvozu8qC3FhgPs6ick3gQe0NdjicrCfXuwAF8CEJCryXmPsBEgEoJib89uYEibHicwDY94vMUgDWUrn2Af9VoQsEqXUA/640?wx_fmt=png&from=appmsg "")  
  
可以看到，进入函数后首先调用 CheckMaps  
来验证传入对象的 map 是否包含 a  
和 b  
两个属性。若检查通过，随即调用 LoadField  
从 Parameter  
常量的偏移 12  
处加载数据，即传入的 obj  
对象的 a  
属性。  
  
紧接着，再次调用 CheckMaps  
验证 map，然后加载属性 b  
。完成后调用 JSAdd  
函数对数字、字符串或两者执行加法运算。  
  
这里的问题在于冗余的 CheckMaps  
调用——因为在两次 CheckMap  
操作之间，传入对象的 map 不可能发生变化。因此，第二次调用将被移除。  
  
我们可以在图的简化降低阶段看到这种冗余消除的结果。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaG55fgl9ficOCmOVgPDVYJ5bBtyFRT56GvJZfia0Hs49e9an5hkvM78Kw6c1Kp4iceXCUHDNu6ymTwckJocAQ9wAYzJ5lXtFXUc4/640?wx_fmt=png&from=appmsg "")  
  
可以清楚地看到，第二个 CheckMaps  
节点已被移除，在第一次检查之后直接依次加载两个属性——从而加速了代码执行。此外，由于简化降低的作用，JSAdd  
调用已被降低为机器码变体，以按照 ECMAScript 标准验证整数和字符串表达式。  
  
回到之前的问题：这是否构成安全漏洞？如前所述，"要看具体情况"。原因在于，某些操作会对上下文的可观察执行产生副作用 (side-effects)——这正是副作用链存在的意义。如果 TurboFan 因某种原因遗漏了某个副作用而未将其写入副作用链，那么对象的 Map 就可能在执行期间发生改变，例如另一个用户函数调用修改了对象或添加了属性。  
  
V8 中每个中间表示操作都有与之关联的各种标志。JavaScript 操作符的部分标志示例可以在 v8/src/compiler/js-operator.cc  
中看到，其中一些标志附带特定的假设。  
  
例如，V(ToString, Operator::kNoProperties, 1, 1)  
假设 String  
不应有属性。另一个如 V(LoadMessage, Operator::kNoThrow | Operator::kNoWrite, 0, 1)  
通过 kNoWrite  
标志假设 LoadMessage  
操作不会产生可观察的副作用。kNoWrite  
标志意味着该操作实际上不会写入效果链。  
  
由此可见，如果我们能让编译器为一个看似无副作用的操作移除冗余检查，那么只要能在编译代码执行期间修改对象或属性，就获得了一个潜在可利用的缺陷。  
  
关于冗余消除与副作用的话题，本可以进一步展开讨论这些消除检查中的缺陷如何导致可利用的漏洞。但在此之前，让我们先快速概览一些其他常见优化。  
## 其他优化  
  
从 --trace_turbo_reduction  
标志的输出中可以看到，TurboFan 中还有许多我们尚未讨论的优化。前面我尽量覆盖了与我们将在 Part 3 中利用的缺陷最相关的优化，但仍然想快速介绍一些其他优化，让你至少对它们有个大致概念。  
  
TurboFan 中其他常见的优化包括：  
- **控制流优化 (Control Optimization)**  
：定义在 v8/src/compiler/control-flow-optimizer.cc  
中，该优化主要针对图的控制流进行优化，将某些分支链转换为 switch 语句。  
  
- **别名分析 (Alias Analysis) 与全局值编号 (Global Value Numbering)**  
：别名分析识别 Store  
和 Load  
节点之间的依赖关系。因此，如果两个 load 操作依赖于同一个操作，它们必须等到第一个操作完成后才能执行，例如 x = 2; y = x + 2; z = x + 2  
。GVN (Global Value Numbering) 在此基础上进一步移除冗余的 Store  
和 Load  
操作，即 z = x + 2  
可以被移除，z  
直接设为 y  
的值，因为该操作是冗余的。  
  
- **死代码消除 (Dead Code Elimination, DCE)**  
：死代码消除正如其名。它遍历所有节点，移除不会被执行的代码。例如，如果 True/False 语句中的 x  
和 y  
始终为 true，则 false 路径将被视为"死代码"并移除。  
  
如果你想进一步了解不同的优化以及 Sea of Nodes 的更多内容，建议阅读 "TurboFan JIT Design" 和 "Introduction to TurboFan"。  
# 常见 JIT 编译器漏洞  
  
在理解了完整的 V8 管线和编译器优化之后，我们现在可以开始审视和理解浏览器中存在哪些类型的漏洞类别。众所周知，JavaScript 引擎及其所有组件 (包括编译器) 都是用 C++ 实现的。  
  
因此，该管线首先容易受到常见的内存和类型安全违规影响，例如整数上溢和下溢、偏差一 (off-by-one) 错误、越界读写 (out-of-bound reads and writes)、缓冲区溢出 (buffer overflows)、堆溢出 (heap overflows)，当然还有释放后使用 (use-after-free) 缺陷等。  
  
除了常见的 C++ 缺陷外，由于推测性假设的本质，在优化阶段还可能出现逻辑缺陷和机器码生成缺陷。这类逻辑缺陷可能源于对操作可能对对象或属性产生的副作用的错误假设，或源于移除关键类型守卫的不当优化 pass。  
  
这类问题通常被称为"类型混淆 (type-confusion)"漏洞——编译器未能验证传入对象的类型或形状 (shape)，导致编译器盲目使用该对象。CVE-2018-17463 正是这种情况，我们将在本系列 Part 3 中尝试分析和利用该漏洞。  
  
写到这里时，我曾考虑深入分析几个缺陷并展示易受攻击代码的示例。最终我决定不这样做。为什么？因为到了这个阶段，你应该已经对浏览器内部机制和 V8 有了足够的理解，能够自行阅读 Chromium 代码并理解相关缺陷报告。  
  
所以，给读者留一些作业。下面提供一系列与浏览器漏洞利用相关的视频和缺陷报告链接。请花时间阅读其中一些报告，理解这些缺陷是如何产生的，以及是什么使它们可以被利用。  
  
需要注意的是，其中一些缺陷存在于其他 JavaScript 引擎中，但无论如何，它们展示了所有 JavaScript 引擎中可能出现的漏洞类型。  
  
推荐阅读以下内容：  
- 35C3 - From Zero to Zero Day: ChakraCore Type Confusion due to Invalid Side-Effects  
  
- Browser Security Beyond Sandboxing - CVE-2017-5121  
  
- Issue 765433: V8 JIT Escape Analysis Bug  
  
- Chrome TurboFan Remote Code Execution via Type Confusion  
  
- CVE-2015-0817 - Incorrect asm.js Bounds Checking Elimination  
  
- CVE-2016-1669 - Use After Free in RegExp  
  
- CVE-2016-1677 - Type Confusion Leads to Info Leak in decodeURI  
  
- CVE-2016-5129 - V8 Out of Bound Read in GC with Array Object  
  
- CVE-2017-2547 - WebKit: Invalid Bounds Check leads to OOB Access  
  
- CVE-2017-5040 - Information Leak in Array indexOf  
  
- CVE-2018-0758 - Chakra: JIT: Missing Integer Overflow Check  
  
- CVE-2018-0769 - Chakra JIT: Incorrect Bounds Calculation  
  
- CVE-2018-4192 - Race Condition in Garbage Collection for array.reverse()  
  
- CVE-2018-6065 - V8 Integer Overflow in Object Allocation Size  
  
- CVE-2018-6106 - V8 AwaitedPromise Incorrect State  
  
- CVE-2018-6136 - Crash with JavaScript RegExp Subclassing  
  
- CVE-2018-6142 - Information Leak in Map Constructor  
  
- CVE-2019-5782 - Improper Side-Effect in Lowering Leads to OOB via Check Bounds Elimination  
  
- CVE-2019-13764 - Invalid NaN Type Check via Typer Optimizer  
  
- CVE-2021-21220 - Improper JIT OpCode Leads to RCE  
  
- Exploiting Chrome V8: Krautflare (35C3 CTF 2018)  
  
- Exploiting the Math.expm1 Typing Bug in V8  
  
- Exploiting TurboFan Through Bound Check Elimination  
  
- Issue: 762847 - Off By One in Range Optimization of String.indexOf  
  
- Patch Gapping Chrome - Properties Backing Store Type Confusion  
  
- JavaScript Vulnerability Database  
  
- ZDI Advisories Page  
  
# 结语  
  
本篇文章到此结束！感谢你坚持读到最后，因为这里涵盖了大量复杂的内容。我自己在学习这些知识的过程中，不知道回头修改了多少次博客初稿。  
  
希望这里呈现的大部分内容都容易理解。如果有些地方不太清楚，那么就像第一篇文章中说的一样——花时间反复阅读，并善用文中和参考文献部分的链接来帮助你理解不清楚的概念。  
  
说实话，对我帮助最大的是阅读和调试 V8 代码。这能让你更好地了解底层发生了什么、哪些函数在什么时候被调用。如果你想审查代码寻找缺陷，这也有助于你更加熟悉代码库。  
  
总之，在我们所涵盖的所有内容中，优化部分对下一篇文章最为重要。在本系列的 Part 3 中，我们将运用所学知识来分析和理解 CVE-2018-17463。之后，我们将深入了解浏览器漏洞利用原语 (exploitation primitives) 的基础知识，然后实际利用该缺陷实现远程代码执行。  
  
话虽如此，感谢阅读，我们下篇见！  
# 致谢  
  
我要衷心感谢 maxpl0it 对本文进行了细致的技术审查，在发布前提供了关键反馈并补充了若干重要细节。  
  
同时感谢 Connor McGarr 和 V3ded 抽出时间对本文的准确性和可读性进行了校对。谢谢你们！  
  
最后，向 Jeremy Fetiveau 致敬，感谢他在 Chrome 漏洞利用领域所做的出色工作，以及为 Diary of a Reverse Engineer 撰写的详尽博文。这些文章对理解 Chrome 和 V8 中的许多细微之处帮助极大。  
# 参考文献  
- An Introduction to Speculative Optimization in V8  
  
- Circumventing Chrome's Hardening of Typer Bugs  
  
- Compiler Design: Static Single Assignment  
  
- Deoptimization in V8  
  
- Digging into the TurboFan JIT  
  
- Exploiting TurboFan Through Bounds Check Elimination  
  
- Firing up the Ignition interpreter  
  
- Franziska Hinkelmann: JavaScript engines - how do they even?  
  
- Getting Around the Chromium Source Code Directory Structure  
  
- How To Start JIT-ting  
  
- Ignition and TurboFan Compiler Pipeline  
  
- Ignition Design Docs  
  
- Ignition: Register Equivalence Optimization  
  
- Intro to Chrome's V8 from an Exploit Development Angle  
  
- Introduction to TurboFan  
  
- JavaScript engine fundamentals: optimizing prototypes  
  
- JavaScript Engine Fundamentals: Shapes and Inline Caches  
  
- Modern attacks on the Chrome browser : optimizations and deoptimizations  
  
- Sea of Nodes  
  
- Sigurd Scheider: Inside V8: The choreography of Ignition and TurboFan  
  
- Sparkplug Design Documentation  
  
- The Chromium Super (Inline Cache) Type Confusion  
  
- TurboFan IR  
  
- TurboFan JIT Design  
  
- Understanding V8's Bytecode  
  
- V8 and How It Listens To You - Michael Stanton  
  
- V8 release v6.8  
  
- V8: Hooking up the Ignition to the TurboFan  
  
- What's up with Monomorphism?  
  
---  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
