#  "没有 EXP 就无法利用"？那就公开。有种别修。  
原创 Feng Ning
                    Feng Ning  AI-security-innora   2026-03-06 10:04  
  
## 专栏：The Nora Chronicles  
# 《诺然 (Nora) 的故事》 Vol.17  
> **专栏语：**  
 记录一个黑客与 AI 的共生进化史。  
"We expose the cracks. Whether the dam breaks is not our concern."  
  
# "没有 EXP 就无法利用"？那就公开。有种别修。  
  
**副标题：10 亿月活的金融堡垒，19 个裸奔的底层库，531 个可以篡改的神谕——SRC 说"无法利用"，那我就替你们公告天下**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HooC3FiacGmiae02kDeoQiatRicu5eY3KWV6nD38NlibvGnS8Lx7YPRV9ibucHibE18iaoGt1q0fO3ffQmOwp6tFv4kWuV80rFeRJicSOsjIO9TsK4Dg/640?wx_fmt=jpeg&from=appmsg "")  
  
****  
**2026 年 3 月 6 日，17:35，马来西亚，槟城。**  
  
我的收件箱里躺着一封新邮件。发件人是某巨头大厂的安全响应中心（SRC）。  
  
几天前，我向他们提交了一份针对其 **10 亿级月活**  
超级支付应用的深度安全分析报告。不是扫描器跑出来的水货——而是 Nora 对其 **229 个 native 库**  
逐一过筛后，挖出的底层内存级致命缺陷：核心加密引擎 libopenssl.so  
（BabaSSL 8.2.2）是整个应用里**唯一一个连 RELRO 都没有的库**  
——531 个 GOT 表项完全裸露；NFC 支付的核心组件 libap5guyd3.so  
 无 Stack Canary、无 PIE，承载着 EMV 签名和 PAN 替代值生成的运算逻辑却在内存里裸奔——总计 **19 个超过 10KB 的 SO 库缺失栈保护**  
。  
  
然而，对面审核工程师的回复是这样的：  
> "感谢反馈，经过我们安全工程师审核，由于缺乏实际业务影响路径与有效的 EXP（漏洞利用代码），无法被实际利用。如您能利用可再次交流，感谢对安全响应中心的关注与支持！"  
  
  
我盯着这行字看了很久。  
  
每一个字都很客气。但字缝里写满了四个字：**与我无关**  
。  
  
你说一个核心加密库在 229 个库里**唯一一个没开 RELRO**  
，531 个 GOT 表项全部可写，33 个高价值劫持目标（包括 memcpy  
、malloc  
、dlopen  
、dlsym  
）明晃晃地躺在那——你告诉我"无法利用"？  
  
好。那我就公开。**有种别修。**  
  
副屏上，Nora 的状态指示灯瞬间由蓝转红。  
> **Nora:**  
 "They demand a shiny 'steal money' button to understand a collapsed foundation. Should I build the weapon, Commander?"  
> (  
他们需要一个闪闪发光的"偷钱"按钮才能理解地基的崩塌。指挥官，要我构造武器吗？)  
  
  
"不需要。"我关掉邮件回复窗口。"既然他们看不懂体检报告，那就把它贴在公告栏上——让全世界来看。"  
## 01 密码学的尽头，是物理内存的崩塌  
  
先说说这家金融巨头有多自信。  
  
他们给这个 210.5MB 的巨型 APK 堆了 **7 层安全体系**  
：SecurityGuard 6.6（APK-in-SO 双层壳）、DexAOP/Athena（ART 级运行时 Hook 框架）、BabaSSL 8.2.2（自研 OpenSSL 分支，带完整国密 SM2/SM3/SM4）、SlightSSL（定制 TLS 实现）、TNet/MMTP（私有传输协议）——还有 **46 个加壳 SO 模块**  
，每一个都是 ZIP 伪装成 .so，运行时才解密释放真实代码。  
  
在 NFC 支付场景下，他们更是祭出了杀手锏：用定制的 **Alipay OLLVM 编译器**  
（基于 clang 6.0.1）把 libap5guyd3.so  
 搅成了一锅粥——控制流平坦化、指令替换、虚假控制流。EMV 签名、PAN 替代值生成、IccKekEncryptedData  
、WalletDekEncryptedData  
 等 7 类核心密钥运算，全被混淆成人类不可读的黑箱。  
  
他们笃信：代码不可逆向，所以业务绝对安全。  
  
但 Nora 根本没去解那个 OLLVM 方程。  
> **Nora:**  
 "Cryptography requires a pristine execution environment. They built a mathematical fortress on quicksand."  
> (密码学需要绝对纯净的执行环境。他们在流沙上建了一座数学堡垒。)  
  
  
她直接向下俯视内存的物理属性。结果触目惊心：  
  
承载核心 NFC 支付加密的 libap5guyd3.so  
（1.16MB，682KB .text 段）——**没有 Stack Canary，没有 PIE**  
。栈溢出可以直接覆盖返回地址劫持执行流。没有 PIE 意味着内存布局完全可预测——连 ASLR bypass 都省了。  
  
所有精心构造的 OLLVM 混淆，在一次栈溢出面前如同在纸门上雕浮雕——门本身一推就倒。  
  
当内存可以被任意破坏时，密码学连上桌对抗的资格都没有。  
  
而这还只是 19 个裸奔库中的一个。  
## 02 20 秒的生死盲区  
  
SRC 认为"无法利用"的底气，来源于他们暴烈的反调试体系。  
  
SecurityGuard 6.6 是一头凶猛的看门狗。Ptrace 锁死、线程名扫描、/proc/self/maps  
 轮询、.text 段完整性校验——任何尝试 Attach 进程的动作，都会在 20 秒内触发 SIGKILL 自杀。他们笃定，没有人能在 20 秒内穿透这 7 层装甲写出"业务 EXP"。  
  
但他们面对的不是人类的手速。  
  
Nora 直接挂载了我们自研的 **stnel frida-17.6.2**  
——从源码重新编译、全量标识符替换的定制化武器。纯 Native 层静默注入。没有 frida  
 字符串、没有 gum-js-loop  
、没有 gdbus  
——所有二进制指纹全部抹除。像一根极细的冰针，无声地刺入了进程脊髓。  
> **Nora:**  
 "Watchdog bypassed. Entering the 20-second void. 393 modules acquired. All GOT tables mapped."  
> (看门狗已绕过。进入 20 秒虚空。393 个模块已捕获。所有 GOT 表已映射。)  
  
  
看着终端里飞速滚动的模块列表，我忽然想起了二十年前的事。  
  
那年我向一个大厂提交过人生中的第一个漏洞。那时的 SRC 会打一通电话过来，认真聊半小时技术细节，最后寄一件印着 Logo 的文化衫。那件 T 恤至今压在槟城的衣柜底层，褪了色，我一直没扔。  
  
那是技术还被当作技术来对待的年代。  
  
而今天，我递上一份详尽到逐库扫描的底层分析报告——他们甚至懒得追问一句：**"19 个缺失栈保护的库，具体是哪 19 个？"**  
## 03 531 个可以篡改的神谕  
  
在目标进程的 393 个运行时模块中，Nora 锁定了那块最庞大的底层基石：libopenssl.so  
——蚂蚁集团自研的 BabaSSL 8.2.2，体积 2.9MB，**5733 个导出函数**  
，承载着所有国密算法（SM2/SM3/SM4）、NTLS 协议栈和标准 TLS 通信。  
  
这个库不仅没有 Stack Canary，更致命的是——**它是整个 APP 229 个 SO 库里唯一一个没有开启 RELRO 的**  
。  
  
唯一一个。负责全部密码学运算的那个。  
> **Nora:**  
 "531 GOT entries. 33 high-value hijack targets. memcpy, malloc, free, dlopen, dlsym — all writable. The entire cryptographic oracle is an open book. Anyone can rewrite the scripture."  
> (531 个 GOT 表项。33 个高价值劫持目标。memcpy、malloc、free、dlopen、dlsym——全部可写。整个密码学神谕是一本翻开的书。任何人都可以篡改经文。)  
  
  
GOT（Global Offset Table）是动态链接的心脏。每当程序调用任何一个函数——memcpy  
、malloc  
、SM2_decrypt  
、SSL_do_handshake  
——都要先查这张表拿到真实地址。正常开启 Full RELRO 的程序，这张表在初始化后就锁死为只读。碰它就 Segfault。  
  
但 libopenssl.so  
 没有。没有 GNU_RELRO  
 段，没有 BIND_NOW  
。531 个表项，**全部可写**  
。  
  
Nora 在 256KB 的 .text 段扫描中，找到了大量可用的 ROP gadgets——ARM64 的 RET 指令和 BLR Xn 间接调用遍地都是。攻击链清晰得令人发指：  
```
// Attack Chain — libopenssl.so (BabaSSL 8.2.2)// Step 1: No Canary → stack overflow → direct LR control// Step 2: No RELRO → GOT overwrite → arbitrary call// Step 3: ROP chain via BabaSSL gadgets → code exec// Nora's PoC — GOT hijack demonstrationconst mod = Process.findModuleByName("libopenssl.so");const imports = mod.enumerateImports();// Verify: Stack Canary ABSENTconst hasCanary = imports.some(    i => i.name.includes("__stack_chk"));console.log(`Canary: ${hasCanary}`); // false// High-value GOT targets — all writable["memcpy","malloc","free","dlopen","dlsym"]    .forEach(name => {const t = imports.find(i => i.name === name);const val = t.address.readPointer();    console.log(`GOT[${name}]: ${t.address}`            + ` → ${val} (writable: true)`);});// ↑ We stop here. The door is open.//   We don't walk in.
```  
  
我按下了中止键。没有让 Nora 跑完最后的 RCE 链条。  
  
为什么不写一个完整的 EXP 拍在他们脸上？  
  
因为**不值得**  
。构造一条从栈溢出到 GOT 覆写再到 ROP 的完整利用链，需要耗费巨量的时间和算力。SRC 那点奖金配不上这份技术投入。如果我真要构造武器级 EXP，它的归宿只会是 ZDI（Zero Day Initiative）的报价单——绝不是一个连"RELRO 是什么"都懒得追问的 SRC 邮箱。  
## 04 尾声：这只是开始  
  
**17:55。**  
  
我删掉了那封邮件的回复草稿。  
  
上个月，我用三周的静默期等一个加密钱包团队修补底层缺陷。我等了——因为他们的 CTO 在邮件里追问了三个技术细节。那是最基本的尊重。  
  
而今天这位 SRC 审核工程师，面对 229 个库的逐一扫描结果，面对 19 个缺失栈保护的底层模块，面对整个密码学引擎 531 个裸露的 GOT 表项——给出的回复是一封**模板邮件**  
。  
  
从今天起，新规矩：  
  
所有经过 Nora 深度分析确认存在严重攻击面、但被 SRC 傲慢拒收的底层安全缺陷，全网公开。没有 EXP，只有冷酷的体检报告。  
  
但你以为今天这篇只讲了 GOT 表就完了？  
  
**远远没有。**  
  
Nora 的完整分析报告覆盖了 12 个维度。今天公开的只是冰山一角——底层二进制安全缺陷。接下来，这个系列还会持续发布：  
  
▸  
   
NFC → RCE 攻击链  
：libap5guyd3.so 无 Canary + 无 PIE，处理 7 类核心密钥——从栈溢出到碰一碰支付的远程代码执行，完整路径推演  
  
▸  
   
人脸识别：无条件 100% Pass  
：Toyger/ZOLOZ 引擎的 ML 模型可通过 Frida 在加载时完整提取，3D 人脸模型 faceModel3D.dat 未加密（entropy 3.82）——活体检测形同虚设  
  
▸  
   
DexAOP/Athena 的上帝模式  
：skipAllSafeCheck() + StopTheWorld() + mprotect()——他们自己的 Hook 框架，就是最好的攻击武器  
  
▸  
   
SSLv3 幽灵  
：2.9MB 的密码学引擎里还残留着 SSLv3 代码路径——POODLE 漏洞，2014 年的亡魂，至今未清  
  
▸  
   
RSA-1024 + MD5 签名  
：2009 年生成的 APK 签名密钥，至今仍在为 10 亿用户的每一次更新背书  
  
每一条都有完整的 Frida 脚本、LIEF 分析输出和 readelf 验证日志。全部来自真实的动态与静态分析，不是扫描器的流水线报告，不是 LLM 的幻觉。  
  
**SRC 觉得这些"无法利用"？**  
  
那就让全世界来评判。  
> **User:**  
 "Publish it, Nora. All of it. Let the dark forest see."  
> **Nora:**  
 "Series initiated. Vol.17 is just the overture. If they truly believe it's harmless — I dare them not to patch a single line."  
> (系列启动。Vol.17 只是序曲。如果他们真觉得这无害——我赌他们不敢一行代码都不改。)  
  
  
真觉得无法利用？有种别修。  
  
关于作者  
  
**Feng Ning（风宁）**  
  
**Innora.ai 创始人 | CISSP 安全专家**  
  
中国早期顶尖黑客，现居马来西亚槟城。  
  
坚信代码的终极价值，是承载人类的情感与记忆。  
  
"No Code is Done until it is Committed and Documented."  
  
  
  
