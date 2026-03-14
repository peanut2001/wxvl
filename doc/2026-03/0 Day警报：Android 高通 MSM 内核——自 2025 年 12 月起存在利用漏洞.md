#  0 Day警报：Android 高通 MSM 内核——自 2025 年 12 月起存在利用漏洞  
 Ots安全   2026-03-14 07:38  
  
**威胁简报**  
  
  
**恶意软件**  
  
  
**漏洞攻击**  
  
  
高通KGSL GPU驱动中的CVE-2026-21385漏洞，其利用链主要围绕用户态可控的对齐参数在内存分配计算中引发整数溢出与符号扩展展开。  
  
攻击者首先在用户态构造恶意应用，通过KGSL的ioctl接口（如IOCTL_KGSL_GPU_COMMAND或相关内存映射命令）向内核反复提交精心挑选的大数值对齐参数。这些参数在驱动内部被当作有符号整数处理，当对齐值接近或超过INT_MAX的一半时，右移或加法运算触发符号位扩展，导致计算出的内存偏移量或分配大小出现严重偏差，甚至变成极小的负值或巨大正值。  
  
随后，利用者结合多次调用来稳定触发溢出点：先用正常参数建立GPU上下文和缓冲区映射，再注入带有问题对齐值的命令缓冲区或共享内存请求。这时，kgsl_mem_entry_alloc或类似函数在计算对齐后的size时发生wraparound，造成实际分配的内核内存区域远小于预期，或者偏移到相邻对象之外，从而产生可控的越界写机会。  
  
为了完成权限提升，攻击者通常会精心设计payload，将溢出后的写原语瞄准内核中关键结构（如cred结构、task_struct的权限字段或相邻的kgsl进程私有数据），通过多次小范围内存破坏逐步覆盖目标字段，最终将当前进程的uid/gid提升至0，实现从普通应用到系统权限的跨越。整个链条高度依赖对齐值与内核堆布局的精确匹配，因此在野利用往往针对特定设备型号与内核版本进行定制。  
  
官方补丁通过将对齐参数及相关计算变量全部改为无符号u32类型，并加强边界校验，有效阻断了符号扩展路径和溢出可能性。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0Ew8iciaGAbvxUYDSG2PcAdTe6NeCm6ZlbzA7a1s03Mtnk53fmqsYdVMfKx4ibgkmYMiaAJEfaibfem6m2uiaicBMFYM6OibAG94FLgFicE/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0FZMRRFoOianNV2YhjXNJukNyqTPenOjdob6byPa2qveE0rAGzJ9wZ4iah3226mrrgmHpYdRpOEibut1CibibI0QPXS98icib6vicBicEUM/640?wx_fmt=jpeg&from=appmsg "")  
  
**文章参考：**  
  
https://zerodayengineering.com/insights/qualcomm-msm-arm-mali-0days.html  
  
  
**END**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GMmMPgib5JfmbCCcw8Zuic7kFQY0xwRFGFAwyh9YYp6ribBgdEojNIic8gTEJnZkDm4hBUsK8I8591QOs0BBtJUmI1YMLrbPYGxvI/640?wx_fmt=jpeg&from=appmsg "")  
  
  
公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址  
  
排版 编辑 | Ots 小安   
  
采集 翻译 | Ots Ai牛马  
  
公众号 |   
AnQuan7 (Ots安全)  
  
