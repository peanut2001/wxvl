#  Chrome 浏览器漏洞利用 (一)：V8 引擎与 JavaScript 内部机制入门  
Jack Halon
                    Jack Halon  securitainment   2026-03-04 05:37  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://jhalon.github.io/chrome-browser-exploitation-1/</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">Jack Halon</span></section></td></tr></tbody></table>  
Web 浏览器——我们连接互联网的主要门户。如今浏览器在现代组织中扮演着举足轻重的角色，越来越多的软件应用以 Web 应用的形式通过浏览器交付给用户。你在互联网上所做的几乎一切都离不开浏览器，因此浏览器堪称全球使用率最高的面向消费者的软件产品之一。  
  
作为通往互联网的门户，浏览器也给个人计算设备的安全完整性带来了巨大风险。如今我们几乎每天都能看到类似的新闻——"Google Chrome Bug Actively Exploited as Zero-Day"，又或者 "Google Confirms Chrome's Fourth Zero-Day Exploit In 2022"。事实上，浏览器漏洞利用并非新鲜事，它们已经存在多年，已知最早的远程代码执行漏洞是 CVE-1999-0280。而首个被公开披露的在野浏览器漏洞利用，可能要数 2010 年 12 月影响了 Google 的 "Aurora" Internet Explorer 漏洞。  
  
我对 Web 浏览器的兴趣最早萌发于 2018 年，当时我的好友 Michael Weber 向我介绍了 Offensive Browser Extension Development，这让我大开眼界，认识到浏览器潜在的攻击面。之后我开始深入研究 Chrome 的内部机制，对浏览器漏洞利用产生了浓厚兴趣。坦白说，哪个 Red Team 不想要一个"单击"甚至"零点击"的浏览器漏洞利用呢？  
  
在安全研究领域，浏览器被公认为最令人瞩目的漏洞挖掘目标之一。遗憾的是，浏览器也是最复杂的研究对象之一——仅仅是入门浏览器内部机制所需的前置知识量，就让许多研究人员望而却步。  
  
尽管如此，我还是迈出了这一步，参加了 maxpl0it 出色的 "Introduction to Hard Target Internals" 培训课程，强烈推荐你也去学习！这门课程为我提供了大量关于 Chrome 和 Firefox 等浏览器内部工作原理的背景知识。此后，我便一头扎进去，阅读了从 Chromium 博客到 V8 开发文章的各种资料。  
  
我的学习方式偏向于"学一遍、教一遍、彻底掌握"，因此我发布了这个 "Chrome Browser Exploitation" 博客系列，旨在为你介绍浏览器内部机制，并深入探索 Windows 平台上的 Chrome 浏览器漏洞利用——同时我自己也在学习的过程中。  
  
你可能会问，为什么选择 Chrome，为什么选择 Windows？原因有二：  
1. Chrome 的市场份额约为 73%，是全球使用最广泛的浏览器。  
  
1. Windows 的市场份额约为 90%，也是全球使用最广泛的操作系统。  
  
通过学习攻击全球使用率最高的软件，作为 Red Team，我们发现漏洞、编写利用代码并在实际攻防中成功运用的可能性会大大提高。  
> **WARNING**  
由于浏览器、JavaScript 引擎和 JIT 编译器的巨大复杂性，这些博客文章的阅读量会非常、非常大。  
> 目前计划为三 (3) 篇博客系列。但根据涵盖内容的复杂程度和信息量，我可能会将材料拆分为更多篇文章。  
> 请注意——我是边学边写这些博客文章的。所以请多多包涵，后续文章的发布可能需要一些时间。  
> 话虽如此，如果你发现我的文章中有错误或对读者有误导，请随时联系我！此外，任何建议、建设性批评和反馈意见都非常欢迎！  
  
  
总体而言，在这个博客系列结束时，我们将涵盖开始研究和利用潜在 Chrome 漏洞所需的所有知识。在本系列的最后一篇文章中，我们将尝试利用 CVE-2018-17463——这是 Samuel Gross 发现的 Chrome V8 优化器 (TurboFan) 中的一个 JIT 编译器漏洞。  
  
那么废话不多说——让我们一头扎进浏览器漏洞利用的复杂世界吧！  
  
在今天的博客文章中，我们将介绍在深入研究之前需要充分理解的基本前置概念。将讨论以下主题：  
- JavaScript 引擎的工作流程  
  
- JavaScript 引擎编译管线  
  
- 栈机与寄存器机  
  
- JavaScript 与 V8 内部机制  
  
- 对象表示  
  
- HiddenClasses (Map)  
  
- Shape (Map) 转换  
  
- 属性  
  
- 元素与数组  
  
- 在内存中查看 Chrome 对象  
  
- 指针标记  
  
- 指针压缩  
  
不过在开始之前，请确保在 Windows 上编译好 v8  
和 d8  
以便跟随操作。你可以阅读我的 "Building Chrome V8 on Windows" gist 了解详细的编译步骤。  
## JavaScript 引擎的工作流程  
  
我们从理解 JavaScript 引擎是什么以及它们如何工作开始浏览器内部机制的探索之旅。JavaScript 引擎是系统上执行 JavaScript 代码不可或缺的组成部分。过去它们只是简单的解释器，但如今现代 JavaScript 引擎已经是包含众多性能提升组件 (如优化编译器和 Just-In-Time (JIT) 编译) 的复杂程序。  
  
目前有许多不同的 JS 引擎在使用，例如：  
- V8 - Google 的开源高性能 JavaScript 和 WebAssembly 引擎，用于 Chrome。  
  
- SpiderMonkey - Mozilla 的 JavaScript 和 WebAssembly 引擎，用于 Firefox。  
  
- Charka - Microsoft 开发的专有 JScript 引擎，用于 IE 和 Edge。  
  
- JavaScriptCore - Apple 内置的 JavaScript 引擎，用于 Safari 中的 WebKit。  
  
那么我们为什么需要这些 JavaScript 引擎及其全部的复杂性呢？  
  
众所周知，JavaScript 是一种轻量级、**解释型**  
的面向对象脚本语言。在解释型语言中，代码逐行执行，运行结果立即返回，因此我们不需要在浏览器运行代码之前将其编译为其他形式。但这通常会导致性能问题。这就是 Just-In-Time 编译等技术发挥作用的地方——JavaScript 代码被解析为字节码 (机器码的一种抽象)，然后由 JIT 进一步优化，使代码更加高效，也就是更"快"。  
  
虽然上述各 JavaScript 引擎可能有不同的编译器和优化器，但它们基本上都是基于 EcmaScript 标准 (也与 JavaScript 互换使用) 以相同的方式设计和实现的。EcmaScript 规范详细说明了浏览器应如何实现 JavaScript，以确保 JavaScript 程序在所有浏览器中运行的行为完全一致。  
  
那么当我们执行 JavaScript 代码后究竟发生了什么？为了详细说明，我在下面提供了一张图表，展示了 JavaScript 引擎的一般"流程" (也称为编译管线) 的高层概览。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjzh7kvP9JQOjKBrMmlIWqcsjv2ySUf3VFiclAicU9ibYO7iaUgNqPMibr05wFCXyIm3L71QdlichccEFYFTaEujgSibolu5rCickbFfTY/640?wx_fmt=png&from=appmsg "")  
  
初看可能有点混乱，但别担心——其实并不难理解。让我们逐步分解这个"流程"，解释每个组件的作用。  
1. **Parser (解析器)**  
: 执行 JavaScript 代码后，代码被传入 JavaScript 引擎，我们进入第一步——解析代码。解析器将代码转换为以下内容：  
  
1. 示例：使用上面的代码示例，其 AST 将如下所示：```
{  "type": "VariableDeclaration",  "start": 0,  "end": 13,  "declarations": [ {"type": "VariableDeclarator","start": 4,"end": 12,"id": {  "type": "Identifier",  "start": 4,  "end": 7,  "name": "num"},"init": {  "type": "Literal",  "start": 10,  "end": 12,  "value": 42,  "raw": "42"} }  ],  "kind": "var"}
```  
  
  
1. 示例：var num = 42  
被分解为 var,num,=,42  
，每个"token"或项目都会被标记其类型，在这种情况下就是 Keyword,Identifier,Operator,Number  
。  
  
1. **Tokens (词法单元)**  
: 代码首先被分解为"tokens"，如 Identifier、Number、String、Operator 等。这被称为"词法分析 (Lexical Analysis)"或"分词 (Tokenizing)"。  
  
1. **Abstract Syntax Tree (AST，抽象语法树)**  
: 代码被解析为 tokens 后，解析器会将这些 tokens 转换为 AST。这一步被称为"语法分析 (Syntax Analysis)"，顾名思义，它检查代码中是否存在语法错误。  
  
1. **Interpreter (解释器)**  
: 生成 AST 后，它被传入解释器。解释器遍历 AST 并生成字节码。字节码生成后会被执行，而 AST 则被删除。  
  
1. V8 的字节码列表可以在这里找到。  
  
1. var num = 42;  
的字节码示例如下：```
LdaConstant [0]Star1Mov <closure>, r2CallRuntime [DeclareGlobals], r1-r2LdaSmi [42]StaGlobal [1], [0]LdaUndefinedReturn
```  
  
  
1. **Compiler (编译器)**  
: 编译器通过使用一种称为"Profiler"的机制提前工作，Profiler 会监控和观察应该被优化的代码。如果存在所谓的"热函数 (hot function)"，编译器会获取该函数并生成优化的机器码来执行。否则，如果它发现一个已优化的"热函数"不再被使用，则会将其"反优化 (deoptimize)"回字节码。  
  
说到 Google 的 V8 JavaScript 引擎，其编译管线基本类似。不过 V8 包含一个额外的"非优化"编译器，这是在 2021 年新添加回来的。V8 的每个组件都有特定的名称，分别如下：  
- **Ignition**  
: V8 的快速底层基于寄存器的解释器，负责生成字节码。  
  
- **SparkPlug**  
: V8 的新非优化 JavaScript 编译器，从字节码编译，通过遍历字节码并为访问到的每条字节码指令生成机器码。  
  
- **TurboFan**  
: V8 的优化编译器，将字节码转译为机器码，具有更多数量和更复杂的代码优化。它还包含 JIT (Just-In-Time) 编译。  
  
将以上内容整合起来，V8 编译管线的高层概览如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjUrGZV1FnHc6mloglAjUo45qicA4DVlpIl0Sgg7wA9rduZVMNT4rospuialkeoHdzuL2xmHe7wvNnwjVvgSskNXZriaMJreUYspg/640?wx_fmt=png&from=appmsg "")  
  
如果当前还不理解编译器和优化等概念或特性，不用担心。在今天的文章中我们不需要完全理解整个编译管线，但应该对引擎整体工作方式有一个大致了解。我们将在本系列的第二篇文章中更深入地介绍 V8 管线及其组件。  
  
在此之前，如果你想了解更多关于管线的知识，建议观看 "JavaScript Engines: The Good Parts" 以获得更好的理解。  
  
目前你需要从这个编译管线中理解的唯一一点是：解释器是一个"栈机 (stack machine)"，本质上是一个执行字节码的 VM (虚拟机)。就 Ignition (V8 的解释器) 而言，它实际上是一个带有累加寄存器的"寄存器机"。Ignition 仍然使用栈，但它更倾向于将数据存储在寄存器中以加快速度。  
  
建议阅读 "Understanding V8's Bytecode" 和 "Firing up the Ignition Interpreter" 以更好地理解这些概念。  
## JavaScript 与 V8 内部机制  
  
现在我们已经对 JavaScript 引擎及其编译管线的结构有了一些基本了解，是时候更深入地探索 JavaScript 本身的内部机制，看看 V8 是如何在内存中存储和表示 JavaScript 对象及其值和属性的。  
  
这一节绝对是你想要利用 V8 (以及其他 JavaScript 引擎) 中的漏洞时 **最**  
需要理解的关键知识之一。因为事实证明，所有主流引擎都以类似的方式实现 JavaScript 对象模型。  
  
众所周知，JavaScript 是一种动态类型语言。这意味着类型信息与运行时的值相关联，而不是像 C++ 中那样与编译时的变量相关联。这意味着 JavaScript 中的任何对象都可以在运行时轻松修改其属性。JavaScript 的类型系统定义了 Undefined、Null、Boolean、String、Symbol、Number 和 Object (包括数组和函数) 等数据类型。  
  
简单来说，这意味着什么？基本上意味着 JavaScript 中的对象或 var  
等原始类型可以在运行时改变其数据类型，这与 C++ 不同。例如，让我们在 JavaScript 中创建一个名为 item  
的新变量并将其设置为 42  
。  
```
var item = 42;
```  
  
通过对 item  
变量使用 typeof 运算符，我们可以看到它返回了数据类型——即 Number  
。  
```
typeof item'number'
```  
  
那如果我们尝试将 item  
设置为字符串然后检查其数据类型，会发生什么呢？  
```
item = "Hello!";typeof item'string'
```  
  
看，item  
变量的数据类型现在变成了 String  
而不是 Number  
。这就是 JavaScript "动态"特性的体现。与此不同的是，在 C++ 中如果我们尝试创建一个 int  
或整数变量然后将其设置为字符串，则会失败——如下所示：  
```
int item = 3;item = "Hello!"; // error: invalid conversion from 'const char*' to 'int'//     ^~~~~~~~
```  
  
虽然 JavaScript 的这个特性很酷，但它确实给我们带来了一个问题。V8 和 Ignition 是用 C++ 编写的，因此解释器和编译器需要弄清楚 JavaScript 打算如何使用某些数据。这对于高效的代码编译至关重要，特别是因为在 C++ 中 int  
和 char  
等数据类型的内存大小是不同的。  
  
除了效率之外，这对安全性也至关重要——如果解释器和编译器"错误地解释"了 JavaScript 代码，使得我们得到的是字典对象而不是数组对象，那么我们就有了一个类型混淆 (Type Confusion) 漏洞。  
  
那么 V8 是如何存储每个运行时值的所有信息，同时保持引擎高效运行的呢？  
  
在 V8 中，这是通过使用一种名为 **Map**  
(不要与 Map Objects 混淆) 的专用信息类型对象来实现的，它也被称为"**Hidden Class**  
"。有时你可能听到 Map 被称为"**Shape**  
"，特别是在 Mozilla 的 SpiderMonkey JavaScript 引擎中。V8 还使用一种称为指针压缩 (pointer compression) 或指针标记 (pointer tagging) 的内存技术 (我们将在本文后面讨论) 来减少内存消耗，并允许 V8 将内存中的任何值表示为指向对象的指针。  
  
但在我们深入了解这些机制的工作原理之前，首先需要理解什么是 JavaScript 对象以及它们在 V8 中是如何表示的。  
## 对象表示  
  
在 JavaScript 中，对象本质上是以键值对形式存储的属性集合——这意味着对象的行为类似于字典。对象可以是 Arrays、Functions、Booleans、RegExp 等。  
  
JavaScript 中的每个对象都有与之关联的属性，可以简单地理解为帮助定义对象特征的变量。例如，一个新创建的 car  
对象可以有 make  
、model  
和 year  
等属性来定义 car  
对象是什么。你可以通过点号运算符 (如 objectName.propertyName  
) 或方括号表示法 (如 objectName['propertyName']  
) 来访问对象的属性。  
  
此外，每个对象的属性都映射到属性特性 (property attributes)，用于定义和描述对象属性的状态。JavaScript 对象中这些属性特性的示例如下图所示。  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6ibibxThEvFoKqOdCXyfXPcdT8rJgyvIxQlaNsE2ib86plu5wSFyibCWyKax8gs1vtIPqaT4UUamxINNuHtLCpgZlESOaeSicYHGgULJk1ZSMTVTQ/640?wx_fmt=svg&from=appmsg "")  
  
现在我们对对象有了初步了解，下一步是理解对象在内存中的结构以及它存储在哪里。  
  
每当创建对象时，V8 会创建一个新的 JSObject 并在堆上为其分配内存。对象的值是指向 JSObject  
的指针，其结构包含以下内容：  
- **Map**  
: 指向 **HiddenClass**  
对象的指针，描述对象的"**shape**  
"或结构。  
  
- **Properties**  
: 指向包含 **命名**  
属性的对象的指针。  
  
- **Elements**  
: 指向包含 **数字索引**  
属性的对象的指针。  
  
- **In-Object Properties**  
: 指向在对象初始化时定义的命名属性的指针。  
  
为了帮助你直观地理解，下图展示了一个基本 V8 JSObject 在内存中的结构。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaNX7WhOWQZ0kydRIq5nu0QqeCIUn5PAfuO7DDRWNvic7ZqJbib5NuD9N3Imk883EpPnYaI9DJniaZGPRGleiblxMGib7VD6Y507aZA/640?wx_fmt=png&from=appmsg "")  
  
观察 JSObject 结构，我们可以看到 Properties 和 Elements 存储在两个独立的 FixedArray  
数据结构中，这使得添加和访问属性或元素更加高效。Elements 结构主要存储非负整数或数组索引属性 (键)，通常称为元素。至于 Properties 结构，如果对象的属性键不是非负整数 (如字符串)，则该属性将作为 Inline-Object Property (稍后在本文中解释) 存储，或存储在 properties 结构中 (有时也称为对象的 properties backing store)。  
  
需要注意的是，虽然命名属性的存储方式与数组元素类似，但在属性访问方面它们并不相同。与元素不同，我们不能简单地使用键来找到命名属性在 properties 数组中的位置——我们需要一些额外的元数据。如前所述，V8 使用一个称为 HiddenClass  
或 Map  
的特殊对象与每个 JSObject 关联。这个 Map 存储了 JavaScript 对象的所有信息，从而使 V8 能够"动态"工作。  
  
因此，在进一步理解 JSObject 结构及其属性之前，我们首先需要了解这个 HiddenClass 在 V8 中是如何工作的。  
## HiddenClass (Map) 与 Shape 转换  
  
如前所述，我们知道 JavaScript 是一种动态类型语言。正因如此，JavaScript 中没有类的概念。在 C++ 中，如果你创建了一个类或对象，就不能像 JavaScript 那样动态地添加或删除方法和属性。在 C++ 和其他面向对象语言中，你可以将对象属性存储在固定的内存偏移处，因为给定类的实例的对象布局永远不会改变；但在 JavaScript 中它可以在运行时动态变化。为了解决这个问题，JavaScript 使用了一种称为"基于原型的继承 (prototype-based-inheritance)"的机制，其中每个对象都引用一个原型对象或"shape"，继承其属性。  
  
那么 V8 是如何存储对象的布局的呢？  
  
这就是 HiddenClass  
或 Map  
发挥作用的地方。Hidden classes 的工作方式类似于固定的对象布局——属性的值 (或指向这些属性的指针) 可以存储在特定的内存结构中，然后通过每个属性之间的 固定偏移量 (fixed-offset)  
来访问。这些偏移量由 Torque 生成，可以在 V8 的 /torque-generated/src/objects/*.tq.inc  
目录中找到。这基本上作为对象"shape"的标识符，进而允许 V8 更好地优化 JavaScript 代码并提高属性访问速度。  
  
如前面 JSObject  
示例中所示，Map 是对象中的另一个数据结构。该 Map 结构包含以下信息：  
- 对象的动态类型，如 String、JSArray、HeapNumber 等。  
  
- V8 中的对象类型列在 /src/objects/objects.h  
中  
  
- 对象的大小 (in-object properties 等)  
  
- 对象属性及其存储位置  
  
- 数组元素的类型  
  
- 对象的 Prototype 或 Shape (如果有的话)  
  
为了帮助直观理解 Map 对象在内存中的样子，我在下图中提供了一个相当详细的 V8 Map 结构。更多关于该结构的信息可以在 V8 的源代码中找到，位于 /src/objects/map.h  
和 /src/objects/descriptor-array.h  
源文件中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSh3maJAlxOqnw49s3eEwtVg3FUcGg32avjYeIG9UkYztGYfTBgOlqX95TJLicCMx4ibtgB0VVMNBclkV4gBA6cwzWicicBEfywOYmI/640?wx_fmt=png&from=appmsg "")  
  
现在我们理解了 Map 的布局，让我们解释一下不断提到的"shape"。如你所知，每个新创建的 JSObject  
都有自己的 hidden class，其中包含每个属性的内存偏移量。有趣的是：如果在任何时候对象的属性被动态创建、删除或更改，则会创建一个新的 hidden class。这个新的 hidden class 保留了现有属性的信息，并包含新属性的内存偏移量。需要注意，只有添加新的命名属性时才会创建新的 hidden class，添加数组索引属性不会创建新的 hidden class。  
  
那么在实践中是什么样的呢？让我们看下面这段代码：  
```
var obj1 = {};obj1.x = 1;obj1.y = 2;
```  
  
一开始我们创建了一个名为 obj1  
的新对象，它被创建并存储在 V8 的堆中。由于这是一个新创建的对象，我们 (显然) 需要创建一个 HiddenClass，即使此时还没有为这个对象定义任何属性。这个 HiddenClass 也被创建并存储在 V8 的堆中。在我们的示例中，我们将这个初始 hidden class 称为 "C0"。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjwdTCU4ddbZfR4EGZec3XCVu4FTGCcMOjic7CHft2rx7NuApHsm8heJjdMUbbFd0TBCZoxv80RKXyWhibY6sibJ2LToBxtP5G8rI/640?wx_fmt=png&from=appmsg "")  
  
当执行到下一行代码 obj1.x = 1  
时，V8 将创建一个基于 C0 的第二个 hidden class "C1"。C1 将是第一个描述属性 x  
在内存中位置的 HiddenClass。但它实际上存储的不是 x  
值的指针，而是 x  
的 **偏移量 (offset)**  
——偏移量为 0。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShrKsSbeTFn4VgpnrNBf11fonwHA6u1OBMdpZzR1ficwvDV3YgHCGmkjicic5A4nR2dlyiaLz7Iibh4dBU59l4QkdP0pacp4YRkZmmA/640?wx_fmt=png&from=appmsg "")  
  
好的，我知道此时你们中的一些人可能会问："为什么存储的是属性的偏移量而不是值的指针？"  
  
在 V8 中，这是一种优化技巧。就内存使用而言，Map 是相对昂贵的对象。如果我们在每个新创建的 JSObject  
中以字典格式存储属性的键值对，那将导致大量的计算开销，因为解析字典很慢。其次，如果创建了一个新对象 (如 obj2  
)，它与 obj1  
共享相同的属性 (如 x  
和 y  
)，会怎样？即使值可能不同，这两个对象实际上以相同的顺序共享相同的命名属性——或者我们所说的相同"**shape**  
"。在这种情况下，将同一属性名称存储在两个不同的位置是浪费的。  
  
这就是 V8 能够快速运行的原因——它经过优化，使 Map 在具有相似 shape 的对象之间尽可能地共享。由于属性名称在同一 shape 的所有对象中重复且顺序相同，我们可以让多个对象指向内存中的同一个 HiddenClass，使用属性偏移量而非值指针。这也便于垃圾回收，因为 Map 和 JSObject  
一样都是 HeapObject  
的分配。  
  
为了更好地解释这个概念，让我们暂时偏离上面的示例，看看 HiddenClass 中最重要的部分。HiddenClass 中使 Map 拥有其"shape"的两个最重要部分是 DescriptorArray 和 **第三位域 (third bit field)**  
。如果你回顾上面的 Map 结构，你会注意到第三位域存储了属性的数量，而 descriptor array 包含命名属性的信息，如名称本身、值的存储位置 (偏移量) 和属性特性。  
  
例如，假设我们创建一个新对象 var obj {x: 1}  
。x 属性将存储在 JavaScript 对象的 In-Object properties 或 Properties store 中。由于创建了新对象，也将创建一个新的 HiddenClass。在该 HiddenClass 中，descriptor array 和第三位域将被填充。第三位域将 numberOfOwnDescriptors  
设置为 1  
(因为我们只有一个属性)，然后 descriptor array 将使用与属性 x 相关的详细信息填充键、详情和值部分。该描述符的值将被设置为 0。为什么是 0？因为 In-Object properties 和 Properties store 就是一个数组。因此，通过将描述符的值设置为 0，V8 知道对于任何具有相同 shape 的对象，键的值位于该数组的偏移量 0 处。  
  
上面解释的可视化示例如下图所示。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSjSHKtLvxZ7ukBva1x3XL8xpbnoLqfmTjOtnscfdXcZymR3juRFdpdc7dcicBctvshkZdJ5wiaEXoSpEuoibY4xbtK4x1lrzlIQGQ/640?wx_fmt=png&from=appmsg "")  
  
让我们看看在 V8 中是什么样的。首先使用 --allow-natives-syntax  
参数启动 d8  
，然后执行以下 JavaScript 代码：  
```
d8> var obj1 = {a: 1, b: 2, c: 3}
```  
  
完成后，我们将对对象使用 %DebugPrint()  
命令来显示其属性、map 和其他信息 (如实例描述符)。执行后注意以下内容：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgiczW3Ishbnbzmmuk3icIJKY4NtS4jNibzuKFCic5TCIkEAQ4QeNFc9L4dhWCtyS1A6Ciau4yxMsnS81prnQYhSaiagc9O3OMgQdCJ8/640?wx_fmt=png&from=appmsg "")  
  
黄色部分是我们的对象 obj1  
。红色部分是指向 HiddenClass 或 Map 的指针。在该 HiddenClass 中，实例描述符指向 DescriptorArray  
。使用 %DebugPrintPtr()  
函数查看该数组的指针，我们可以看到该数组在内存中的更多细节，用蓝色高亮显示。  
  
请注意，我们有三个属性，与 map 的实例描述符部分中的描述符数量一致。在下方，我们可以看到 descriptor array 持有我们的属性键，而 const data field  
持有其在属性存储中关联值的偏移量。现在如果我们从偏移量向上追溯到对象，会发现偏移量确实匹配，每个属性都被分配了正确的值。  
  
另外请注意，在这些属性的右侧你可以看到每个属性的 **location**  
——正如我之前提到的，它们都是 **in-object**  
。这基本上证明了偏移量指向的是 In-Object 和 Properties store 中的属性。  
  
好了，现在我们理解了为什么使用偏移量，让我们回到之前的 HiddenClass 示例。如我们之前所说，通过向 obj1  
添加属性 x  
，我们将得到一个新创建的 HiddenClass "C1"，其中包含 x  
的偏移量。由于我们正在创建新的 HiddenClass，V8 将用一个"类转换 (class transition)"更新 C0，声明如果创建了一个具有属性 x  
的新对象，则 hidden class 应直接切换到 C1。  
  
当我们执行 obj1.y = 2  
时，这个过程重复进行。将创建一个新的 hidden class "C2"，并向 C1 添加一个类转换，声明对于任何具有属性 x  
的对象，如果添加了属性 y  
，则 hidden class 应转换为 C2。最终，所有这些类转换形成了所谓的"转换树 (transition tree)"。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSiaX7L8SibGLhSxkyvibUkdhzIAMiboBHAUlzv2qqwG6XHRrLU2vMKjLN0VH76mP4Aw1KfQkHCKlDQ7NHMof05Nwe2ZDpk7O9HGf9o/640?wx_fmt=png&from=appmsg "")  
  
另外需要注意，类转换取决于属性添加到对象的顺序。因此如果在 y 之后添加的是 z，那么"shape"将不再相同，也不会遵循从 C1 到 C2 的相同转换路径。相反，将创建一个新的 hidden class，并从 C1 添加一条新的转换路径来处理这个新属性，从而进一步扩展转换树。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiauubAQM0vtX0bzPCZNSDXGAwzaZuU1vVRFQ3AQTVEWzfQK05HE0zribf2IepuUV0Xib9Hllrysdwov3KTiczkX2MHVPico9LVqzgc/640?wx_fmt=png&from=appmsg "")  
  
现在我们理解了这些，让我们看看当两个具有相同 shape 的对象共享 Map 时，对象在内存中是什么样的。  
  
首先，再次使用 --allow-natives-syntax  
参数启动 d8  
，然后输入以下两行 JavaScript 代码：  
```
d8> var obj1 = {x: 1, y: 2};d8> var obj2 = {x: 2, y: 3};
```  
  
完成后，我们将再次对每个对象使用 %DebugPrint()  
命令来显示它们的属性、map 和其他信息。执行后注意以下内容：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShj8PP3zAB4UZrlRrrdO5bb4Mt8LY4TIjBl4TtE5bqBjLjYLyialBVLDporA9zDfzLLS6jvV55ZMojgb0thP16XsVTth3UB1ia6Y/640?wx_fmt=png&from=appmsg "")  
  
黄色部分可以看到我们的两个对象 obj1  
和 obj2  
。请注意每个对象都是一个 JS_OBJECT_TYPE  
，在堆中有不同的内存地址，因为它们显然是具有潜在不同属性值的独立对象。  
  
如我们所知，这两个对象共享相同的 shape，因为它们都以相同的顺序包含 x 和 y。在这种情况下，蓝色部分可以看到属性在同一个 FixedArray  
中，x 和 y 的偏移量分别为 0 和 1。原因是——正如我们已经知道的——具有相同 shape 的对象共享一个 HiddenClass (用红色表示)，它们拥有相同的 descriptor array。  
  
如你所见，大部分对象的属性和 Map 地址是相同的，都是因为这两个对象共享同一个 Map。  
  
现在让我们关注绿色高亮的 back_pointer  
。如果你回顾我们的 C0 到 C2 Map 转换示例，你会注意到我们提到了一个叫"转换树"的东西。这个转换树由 V8 在每次创建新 HiddenClass 时在后台创建，允许 V8 将新旧 HiddenClass 链接在一起。这个 back_pointer  
是转换树的一部分，它指回转换发生的父 map。这使得 V8 可以沿着 back pointer 链向上遍历，直到找到持有对象属性 (即其 shape) 的 map。  
  
让我们用 d8  
更深入地了解它是如何工作的。我们将再次使用 %DebugPrintPtr()  
命令来打印 V8 中地址指针的详细信息。在这里我们将查看 back_pointer  
地址的详情。完成后，你的输出应该类似于下图。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgHtQRGzLljEAyoBXY0QkU963ibEG6QoqOjbzNHPktvFZLl80JDMGBuLRcN2LxYuDuhVmOLFEZJekSj9QQmBAX59b7KQSgbA45w/640?wx_fmt=png&from=appmsg "")  
  
绿色部分可以看到 back_pointer  
解析为内存中的一个 JS_OBJECT_TYPE  
，而它实际上是一个 Map！这个 map 就是我们之前谈到的 C1 map。我们知道 Map 如何回溯到其前一个 Map，但当有属性被添加时，它如何知道应该转换到哪个 Map 呢？如果我们仔细观察该 Map 中的信息，会注意到在实例描述符指针下方有一个红色标注的"transitions"部分。这个 transitions 部分包含了 Map 结构中 Raw Transition Pointer 所指向的信息。  
  
在 V8 中，Map 转换使用一种称为 TransitionsAccessor 的辅助类。这个辅助类封装了对 Map 在 Map::kTransitionsOrPrototypeInfo  
字段 (也就是我们之前提到的 Raw Transition Pointer) 中存储到其他 map 的转换的各种访问方式。该指针指向一个 TransitionArray，同样是一个持有属性变更 map 转换的 FixedArray  
。  
  
回顾红色高亮部分，我们可以看到该 transition array 中只有一个转换。在该数组中，转换 [#1]()  
 描述了当 y 属性被添加到对象时的转换。如果 y 被添加，它告诉 map 使用存储在 0x007f00259735  
中的 map 更新自身——这正是我们当前的 map！如果存在另一个转换 (例如 z 被添加到 x 而不是 y)，那么 transition array 中将有两个项目，每个都指向其各自对象 shape 的 map。  
> **NOTE**  
: 如果你想要练习 Map 操作并获得 Map 转换的另一种可视化表示，推荐使用 V8 的 Indicium 工具。该工具是一个统一的 Web 界面，允许用户追踪、调试和分析 Map 在实际应用中被创建和修改的模式。  
  
  
如果我们删除一个属性，转换树会发生什么？在这种情况下，V8 每次删除属性时创建新 map 存在一些细微差别。如我们所知，map 在内存使用方面是相对昂贵的，因此在某个节点维护转换树的成本会越来越大且越来越慢。如果删除的是对象的最后一个属性，Map 只需将 back pointer 调整回其前一个 map，而不是创建新的。但如果我们删除的是对象中间的属性呢？在这种情况下，当添加了太多属性或删除了非末尾元素时，V8 将放弃维护转换树，转而切换到一种更慢的模式——字典模式 (dictionary mode)。  
  
那么什么是字典模式呢？既然我们已经知道了 V8 如何使用 HiddenClass 来追踪对象的 shape，现在可以回到起点，进一步理解 Properties 和 Elements 在 V8 中实际是如何存储和处理的。  
## 属性  
  
如前所述，我们知道 JavaScript 对象有两种基本类型的属性：命名属性和索引元素。我们先从命名属性开始。  
  
如果你回忆一下我们关于 Map 和 Descriptor Array 的讨论，我们提到命名属性要么存储为 In-Object，要么存储在 Property 数组中。那么我们所说的 In-Object Property 是什么？  
  
在 V8 中，这种模式是一种非常快速的属性存储方式——直接存储在对象上，因此可以无需任何间接寻址即可访问。虽然它们非常快，但也受限于对象的初始大小。如果添加的属性超出了对象的可用空间，则新属性会存储在 properties store 中——这增加了一级间接寻址。  
  
一般来说，JavaScript 引擎使用两种"模式"来存储属性：  
- **Fast Properties (快速属性)**  
: 通常用于定义存储在线性 properties store 中的属性。这些属性通过查阅 HiddenClass 中的 Descriptor Array，以索引方式在 properties store 中进行访问。  
  
- **Slow Properties (慢速属性)**  
: 也称为"字典模式 (dictionary mode)"，当属性的添加或删除过多——导致大量内存开销时使用。因此，具有 slow properties 的对象将有一个自包含的字典作为 properties store。所有属性元信息不再存储在 HiddenClass 的 Descriptor Array 中，而是直接存储在属性字典中。V8 将使用哈希表来访问这些属性。  
  
当 Map 转换为带有自包含字典的 slow properties 时的示例如下图所示。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShQiaicRL9TzqUI2PDib0AUOC6qwe9EXjRiacDe8icQFRj6lOhvX4H26uiaTddnydbibhZxkH7Bf3oPPV1j0wQyEC2LAFIXau3Wp7JxlM/640?wx_fmt=png&from=appmsg "")  
  
还有一点需要注意。Shape 转换只适用于 fast properties 而不适用于 slow properties，因为字典 shape 仅由单个对象使用，不能在不同对象之间共享，因此没有转换。  
## 元素  
  
好了，到目前为止我们已经基本涵盖了命名属性。现在让我们看看数组索引属性或元素。你可能会认为索引属性的处理不那么复杂......但这种假设是错误的。元素的处理并不比命名属性简单。尽管所有索引属性都保存在 elements store 中，V8 对每个数组包含的元素类型做出了非常精确的区分。实际上大约有 21 种不同的元素类型可以在该 store 中追踪！这使得 V8 能够专门针对该元素类型优化数组上的任何操作。  
  
这是什么意思？让我们看看这行代码：  
```
const array = [1,2,3];
```  
  
在 JavaScript 中，如果我们对这个数组执行 typeof 操作，它会说数组包含 numbers  
，因为 JavaScript 不区分整数、浮点数或双精度数。但 V8 做出了更精确的区分，会将这个数组分类为 PACKED_SMI_ELEMENTS  
，其中 SMI 指的是 Small Integers (小整数)。  
  
那么 SMI 是怎么回事？V8 会追踪每个数组包含的元素类型，然后利用这些信息优化该元素类型的数组操作。在 V8 中有三种我们需要了解的不同元素类型：  
- SMI_ELEMENTS  
- 用于表示包含小整数的数组，如 1、2、3 等。  
  
- DOUBLE_ELEMENTS  
- 用于表示包含浮点数的数组，如 4.5、5.5 等。  
  
- ELEMENTS  
- 用于表示包含字符串字面量元素或无法表示为 SMI 或 Double 的值的数组，如 'x'。  
  
那么 V8 如何使用这些元素类型？它们是针对数组设置的还是针对每个元素设置的？答案是：元素类型是针对数组设置的。我们需要记住的重要一点是，元素类型有一个只能单向进行的"转换"。我们可以从"自上而下"的方式查看这个转换树。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nShKVCHrjyZA4mXLea3zEZ0W04GiaansoKUazxQa73j5MbyLC7NiaA5cwc0vamQMEM9ic48xpcHPicgrHicAlAbV8SysGvLdSLQdoUQE/640?wx_fmt=png&from=appmsg "")  
  
例如，让我们看看之前的数组示例：  
```
const array = [1,2,3];// Elements Kind: PACKED_SMI_ELEMENTS
```  
  
如你所见，V8 将这个数组的元素类型追踪为 packed SMI (稍后我们会详细说明 packed 的含义)。如果我们添加一个浮点数，那么数组的元素类型将"转换"为 Double 元素类型：  
```
const array = [1,2,3];// Elements Kind: PACKED_SMI_ELEMENTSarray.push(3.337)// Elements Kind: PACKED_DOUBLE_ELEMENTS
```  
  
这种转换的原因很简单——操作优化。因为我们有一个浮点数，V8 需要能够对这些值执行优化，所以它向下转换一步到 DOUBLES  
，因为可以表示为 SMI  
的数字集合是可以表示为 double 的数字集合的子集。  
  
由于元素类型转换是单向的，一旦数组被标记为较低的元素类型 (如 PACKED_DOUBLES_ELEMENTS  
)，即使我们替换或删除了那个浮点数，它也不能再回到 PACKED_SMI_ELEMENTS  
。一般来说，创建数组时元素类型越具体，就能启用越精细的优化。元素类型越往下走，对该对象的操作可能就越慢。  
  
接下来，我们还需要理解 V8 在追踪元素 backing store 中索引被删除或为空时的第一个主要区分：  
- PACKED  
- 用于表示密集数组，即数组中所有可用元素都已被填充。  
  
- HOLEY  
- 用于表示有"空洞"的数组，例如当索引元素被删除或未定义时。这也被称为使数组变为"稀疏 (sparse)"的。  
  
让我们仔细看看。例如，来看以下两个数组：  
```
const packed_array = [1,2,3,5.5,'x'];// Elements Kind: PACKED_ELEMENTSconst holey_array = [1,2,,5,'x'];// Elements Kind: HOLEY_ELEMENTS
```  
  
如你所见，holey_array  
中有"空洞"，因为我们忘记在索引位置添加 3  
，直接留空或未定义。V8 做出这种区分的原因是对 packed 数组的操作可以比对 holey 数组的操作优化得更积极。如果你想了解更多，建议观看 Mathias Bynens 的演讲 "V8 internals for JavaScript Developers"，其中对此有很好的讲解。  
  
V8 还在 PACKED  
和 HOLEY  
数组上都实现了前面提到的元素类型转换，形成一个"格 (lattice)"。V8 博客中这些转换的简单可视化如下图所示。  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5IWeuib46jq9Cv52b5VqfDkvKLbprwLKBzJq0tXUYic8yZvBxDCaYadcTBsy2zg3NVBZEo8AInvEUXPGAVHV5a8Lyw4jjth3KHxs0xSBKdw14g/640?wx_fmt=svg&from=appmsg "")  
  
再次强调，我们必须记住元素类型在这个格中只有单向向下转换。例如向 SMI 数组中添加浮点数会将其标记为 double；类似地，一旦数组中出现空洞，它将永远被标记为 holey，即使你后来填充了它。  
  
V8 对元素还有第二个我们需要理解的主要区分。在元素 backing store 中，就像在 properties store 中一样，元素也可以是 fast 或 dictionary-mode (slow) 的。Fast elements 就是一个简单的数组，其中属性索引映射到 elements store 中项目的偏移量。至于 slow array，当存在大型稀疏数组且只有少数条目被占用时会出现这种情况。在这种情况下，数组 backing store 使用字典表示 (类似于我们在 properties store 中看到的) 以性能为代价来节省内存。该字典将在字典三元组值中存储键、值和元素属性。  
## 在内存中查看 Chrome 对象  
  
至此我们已经涵盖了大量关于 JavaScript 和 V8 内部机制的复杂主题。希望此时你对使 V8 在底层工作的一些概念有了比较好的理解。有了这些知识，是时候跳入实际观察，看看通过 WinDBG 观察时 V8 及其对象在内存中是什么样的，以及使用了什么类型的优化。  
  
我们使用 WinDBG 的原因是，当我们编写利用代码、调试 POC 等时，主要会结合使用 WinDBG 和 d8。因此能够掌握和理解 V8 内存结构的细微差别对我们来说很重要。如果你不熟悉 WinDBG，建议阅读 Microsoft 的 "Getting Started with WinDbg (User-Mode)" 博客文章；如果你之前使用过 GDB，还可以阅读 "GDB commands for WinDbg Users"。  
  
我知道我们已经查看过对象和 map 的内存结构，也玩过 d8——所以我们应该对什么指向什么、东西在内存中的位置有一个大致了解。但不要以为这会很简单。V8 中的所有东西一样，优化在让它快速高效方面起着重要作用，这同样适用于它在内存中处理和存储值的方式。  
  
这是什么意思？让我们使用 d8 和 WinDBG 快速看一下一个简单的 V8 对象结构。首先再次使用 --allow-natives-syntax  
选项启动 d8，并创建一个简单对象：  
```
d8> var obj = {x:1, y:2}
```  
  
完成后，让我们使用 %DebugPrint()  
函数来打印对象的信息。  
```
d8> var obj = {x:1, y:2};d8> %DebugPrint(obj)DebugPrint: 000002530010A509: [JS_OBJECT_TYPE] - map: 0x025300259735 <Map[20](HOLEY_ELEMENTS)> [FastProperties] - prototype: 0x025300244669 <Object map = 0000025300243D25> - elements: 0x025300002259 <FixedArray[0]> [HOLEY_ELEMENTS] - properties: 0x025300002259 <FixedArray[0]> - All own properties (excluding elements): {    00000253000041ED: [String] in ReadOnlySpace: #x: 1 (const data field 0), location: in-object    00000253000041FD: [String] in ReadOnlySpace: #y: 2 (const data field 1), location: in-object }0000025300259735: [Map] in OldSpace - type: JS_OBJECT_TYPE - instance size: 20 - inobject properties: 2 - elements kind: HOLEY_ELEMENTS - unused property fields: 0 - enum length: invalid - stable_map - back pointer: 0x0253002596ed <Map[20](HOLEY_ELEMENTS)> - prototype_validity cell: 0x0253002043cd <Cell value= 1> - instance descriptors (own) #2: 0x02530010a539 <DescriptorArray[2]> - prototype: 0x025300244669 <Object map = 0000025300243D25> - constructor: 0x02530024422d <JSFunction Object (sfi = 000002530021BA25)> - dependent code: 0x0253000021e1 <Other heap object (WEAK_ARRAY_LIST_TYPE)> - construction counter: 0
```  
  
之后，启动 WinDBG 并将其附加到 d8 进程。调试器连接后，我们将执行 dq 命令，后跟对象的内存地址 (0x0000020C0010A509  
) 来显示其内存内容。你的输出应该类似于下图。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSgBk5p4sPnTeJuIay22HqLG0THJUsRqDpyjz0DN58xc164amKngA0S9Rib0O6ED1R6eDBUMia4WInHp9xsfghx3T6eSmAv8qn6E8/640?wx_fmt=png&from=appmsg "")  
  
查看 WinDBG 的输出，我们可以看到使用了正确的对象内存地址。但当我们查看内存内容时，第一个地址 (如果你还记得我们的 JSObject 结构，它应该是指向 map 的指针) 似乎已损坏。普通人可能会认为它损坏了，更有经验的逆向工程师或漏洞利用开发者可能会认为存在偏移/对齐问题——你技术上接近了，但不完全正确。  
  
这再次是 V8 优化在起作用。你可以看到为什么我们需要讨论这些优化——因为对于未经训练的眼睛来说，你会对内存中发生了什么感到严重困惑。我们实际看到的是两件事——Pointer Compression (指针压缩) 和 Pointer Tagging (指针标记)。  
  
我们将首先理解 V8 中的 Pointer 或 Value tagging。  
## 指针标记  
  
那么什么是指针标记，我们为什么使用它？如我们所知，在 V8 中值被表示为对象并在堆上分配——无论它们是对象、数组、数字还是字符串。然而，许多 JavaScript 程序实际上对整数值执行计算，所以如果每次递增或修改值时我们都要在 JavaScript 中创建一个新的 Number()  
对象，那将导致创建对象、堆追踪的时间开销，并增加使用的内存空间，非常低效。  
  
在这种情况下，V8 会选择不每次都创建新对象，而是将一些值内联存储。虽然这样可行，但又引入了第二个问题——我们如何区分对象指针和内联值？这就是指针标记 (pointer tagging) 发挥作用的地方。  
  
指针标记技术基于这样一个观察：在 x32 和 x64 系统上，分配的数据必须位于字对齐 (4 字节) 的边界上。由于数据以这种方式对齐，最低有效位 (LSB) 将始终为零。标记将使用最低两位或最低有效位来区分堆对象指针和整数或 SMI。  
  
在 x64 架构上使用以下标记方案：  
```
            |----- 32 bits -----|----- 32 bits -------|Pointer:    |________________address______________(w1)|Smi:        |____int32_value____|000000000000000000(0)|
```  
  
从示例中可以看出，0 用于表示 SMI，1 用于表示指针。需要注意的一点是，当你查看内存中的 SMI 时，虽然它们是内联存储的，但实际上会被翻倍以避免指针标记冲突。因此如果原始值是 1，在内存中将是 2。  
  
在指针中，我们在第二个 LSB 还有一个 w  
位，用于区分强引用和弱引用。如果你不熟悉什么是强指针与弱指针，我来解释一下。简单来说，_强 (strong)_ 指针是指示所指对象必须保留在内存中的指针 (它代表一个对象)，而 弱 (weak)  
指针只是指向可能已被删除的数据的指针。当 GC (垃圾回收器) 删除对象时，它必须删除强指针，因为强指针持有引用计数。  
  
使用这种指针标记方案，对整数的算术或位运算可以忽略标记，因为低 32 位全部为零。但当需要解引用 HeapObject 时，V8 需要先掩码掉最低有效位，这通过一个专用的访问器来清除 LSB。  
  
了解了这些之后，让我们回到 WinDBG 中的示例，通过从地址减去 1 来清除 LSB。这应该能给我们提供有效的内存地址。完成后，你的输出应如下图所示。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nShria47lT5PKFgPEMs77ZKHuFgz1W61Cx0iaCFB8NBn2d6IoGBLASw1ahtIfqIEbkqpLANIKQpb2KenOyiazztB4uepb1iblAIpic9g/640?wx_fmt=png&from=appmsg "")  
  
如你所见，一旦我们清除了 LSB，内存中就有了有效的指针地址！具体来说我们有 map、properties、elements，然后是我们的内联对象。再次注意，SMI 是 **翻倍**  
的，所以持有 1 的 x 在内存中实际上是 2，2 同样变成了 4。  
  
眼尖的读者可能已经注意到，只有指针的一半实际指向内存中的对象。这是为什么？如果你的回答是"又一个优化"，那就对了。这就是所谓的 Pointer Compression (指针压缩)，我们接下来将讨论这个话题。  
## 指针压缩  
  
Chrome 和 V8 中的 Pointer Compression 利用了堆上对象的一个有趣特性——堆对象通常彼此靠近，因此指针的最高有效位很可能相同。在这种情况下，V8 只将指针的一半 (最低有效位) 保存到内存中，而将 V8 堆的最高有效位 (高 32 位，即 **isolate root**  
) 放入一个 **根寄存器 (root register)**  
(R13)。每当我们需要访问指针时，只需将寄存器和内存中的值相加，就能得到完整地址。该压缩方案的实现位于 V8 的 /src/common/ptr-compr-inl.h  
源文件中。  
  
基本上，V8 团队试图实现的目标是将两种标记值都压缩到 64 位架构上的 32 位中，特别是为了减少 V8 的开销，尽可能节省 x64 架构中浪费的 4 字节。  
## 结语  
  
以上就是我们对 JavaScript 和 V8 内部机制的深入探讨！希望你喜欢这篇文章，也真诚地希望它能帮助你们中的一些人了解 V8 的复杂性。  
  
我知道这涵盖了很多内容，说实话一开始确实非常复杂——所以请花时间仔细阅读，确保理解基本概念，因为在我们能够利用它之前，你需要理解所有这些底层工作原理。记住，要知道如何破坏某样东西，我们首先需要知道它是如何工作的。  
  
在本博客系列的第二部分，我们将进一步深入理解编译管线，解释 Ignition、Spark-Plug 和 TurboFan 的底层工作原理。我们还将更加关注 JIT 编译器、推测性保护 (speculative guards)、优化、假设等内容，这将帮助我们更好地理解常见的 JavaScript 引擎漏洞，如类型混淆 (type confusions)。  
## 致谢  
  
我衷心感谢 maxpl0it 和 Fletcher 在发布前为这篇博客文章进行校对、提供重要反馈并补充了一些关键细节。感谢你们花时间审查这篇文章的准确性和可读性，你们太棒了！  
## References  
- Attacking JavaScript Engines - A Case Study of JavaScriptCore and CVE-2016-4622  
  
- A Tale of Types, Classes, and Maps by Benedikt Meurer  
  
- A tour of V8: Object Representation  
  
- Exploiting Logic Bugs in JavaScript JIT Engines  
  
- Fast properties in V8  
  
- How is Data Stored in V8 JS Engine Memory  
  
- JavaScript Engine fundamentals: Shapes and Inline Caches  
  
- JavaScript Engines Hidden Classes  
  
- Javascript Hidden Classes and Inline Caching in V8  
  
- Juicing V8: A Primary Account for the Memory Forensics of the V8 JavaScript Engine  
  
- Learning V8  
  
- Mathias Bynens - V8 Internals for JavaScript Developers  
  
- Pointer Compression in V8  
  
- SMIs and Doubles  
  
- V8 / Chrome Architecture Reading List - For Vulnerability Researchers  
  
- V8 Dev Blog  
  
- V8 Engine JSObject Structure Analysis and Memory Optimization Ideas  
  
- V8 Hidden Class  
  
---  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
