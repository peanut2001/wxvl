#  CentOS 9 新漏洞允许攻击者提升至 root 权限——PoC 发布  
原创 ZM
                    ZM  暗镜   2026-02-06 05:28  
  
Linux 内核的 sch_cake 队列规则 (Qdisc) 中存在一个严重的释放后使用 (UAF) 漏洞，该漏洞会影响 CentOS 9，允许本地用户获得 root 权限。  
  
安全公司 SSD Secure Disclosure 于 2026 年 2 月 5 日发布了详细信息，指出该漏洞在 TyphoonPWN 2025 的 Linux 类别中获得了第一名。  
  
问题出在 CAKE Qdisc 的 cake_enqueue 函数中，即使由于缓冲区限制而丢弃了数据包，该函数仍然返回 NET_XMIT_SUCCESS。  
  
这会误导父级有类队列（例如 HFSC），导致状态管理不当，并在数据包出队时引发 UAF（用户代理错误）。攻击者可以利用此漏洞在内核上下文中执行任意代码，从而实现本地权限提升（LPE）。  
  
当 buffer_used 超过 buffer_limit 时，cake_enqueue 会通过 cake_drop 丢弃数据包，但会发出成功信号。在堆叠架构（HFSC over CAKE）中，HFSC 入队时不进行错误检查，而是调用 init_ed 将类添加到其活动列表中。  
  
删除 HFSC 类会通过 qdisc_purge_queue 清除子 CAKE Qdisc，但由于 CAKE 为空，qlen_notify 会跳过从 HFSC 的活动列表中移除。  
  
这会留下一个悬空指针。在 hfsc_dequeue 期间，eltree_get_mindl 会选择已释放的类，而 qdisc_dequeue_peeked 会触发 cl->qdisc 上的 UAF。该漏洞利用此漏洞，通过喷洒带有 ROP 小工具的伪造 Qdisc 来实现 RIP 控制。  
  
cake_enqueue 函数的关键代码缺陷：  
```
if (q->buffer_used > q->buffer_limit) {
    // drops packets
}
return NET_XMIT_SUCCESS;  // Misleads parent

```  
## 利用详情  
  
该安全公告称，PoC 利用预取侧信道定时攻击绕过 KASLR，通过 sendmsg 发送带有精心构造的控制消息的伪造 Qdisc 。  
  
它使用类设置 HFSC (0x10000)，添加 CAKE 子进程，通过回环发送触发丢弃操作，删除类以创建 UAF，然后喷洒 ROP 链以覆盖 modprobe_path。最后，通过未处理的文件类型触发 modprobe 以获取 root shell。  
  
目前尚无 CVSS 评分，但影响巨大：本地攻击者可利用 CAKE 漏洞获取 CentOS 9 系统的 root 权限。  
  
红帽公司（CentOS 上游）在 90 多天前就已收到通知；回复是：“正在处理中，尚未发布。” 过去类似的 CAKE 漏洞（例如 CVE-2022-50452 空引用解引用）已通过内核更新修复。  
## 缓解措施  
- 避免使用 CAKE Qdisc：tc qdisc del dev lo root或者改用 HTB 等替代品。  
- 监控 tc 命令和异常 netlink 流量。  
- 打完补丁后更新内核；禁用不需要的 Qdisc 模块。  
- 对高风险工作负载使用命名空间/用户隔离。  
此 LPE 突出了内核流量控制风险；管理员应立即审核 Qdisc 使用情况。  
  
  
