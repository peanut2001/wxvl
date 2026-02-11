#  【已复现】CentOS Stream 9 ROOT 提权漏洞（TyphoonPWN 2025比赛漏洞）  
原创 360漏洞研究院
                    360漏洞研究院  360漏洞研究院   2026-02-11 07:10  
  
“扫描下方二维码，进入公众号粉丝交流群。更多一手网安资讯、漏洞预警、技术干货和技术交流等您参与！”  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/5nNKGRl7pFgrNicMticDTWVCUWbOwRuWcrYSpAlwDRibKNLbe3KialEfR0Y2PlPAvS4MN50asXETicAviaRy1gRicI2Dw/640?wx_fmt=gif&from=appmsg "")  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td colspan="4" data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;background-color: rgb(100, 130, 228);box-sizing: border-box;padding: 0px;"><section style="text-align: center;color: rgb(255, 255, 255);box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞概述</span></strong></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞名称</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">CentOS Stream 9 CAKE Qdisc Use-After-Free漏洞</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞编号</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">LDYVUL-2026-00023143</span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">公开时间</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="box-sizing: border-box;"><span leaf="">2026-02-05</span></span></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span style="color: rgb(0, 0, 0);box-sizing: border-box;"><span leaf="">POC状态</span></span></strong></p></section></td><td data-colwidth="20.0000%" width="20.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;color: rgb(100, 130, 228);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">已公开</span></strong></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">漏洞类型</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">权限提升</span></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">EXP状态</span></strong></p></section></td><td data-colwidth="20.0000%" width="20.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;color: rgb(100, 130, 228);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">已公开</span></strong></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span style="color: rgb(0, 0, 0);box-sizing: border-box;"><span leaf="">利用可能性</span></span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">高</span></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;color: rgb(0, 0, 0);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">技术细节状态</span></strong></p></section></td><td data-colwidth="20.0000%" width="20.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;color: rgb(100, 130, 228);box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">已公开</span></strong></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">CVSS 3.1</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">7.0</span></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf="">在野利用状态</span></strong></p></section></td><td data-colwidth="20.0000%" width="20.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;"><p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf="">未发现</span></p></section></td></tr></tbody></table>  
  
  
**01**  
  
影响组件  
  
  
  
Linux是一种免费开源的类Unix操作系统，广泛应用于服务器、嵌入式设备及云计算领域。  
  
Qdisc（Queueing Discipline，排队规则）是Linux内核网络流量控制（TC）子系统的核心组件，负责管理网络接口的数据包排队、调度和拥塞控制逻辑。它通过定义数据包在网络设备发送队列中的处理顺序和优先级，实现带宽分配、延迟控制、流量整形（Shaping）和拥塞避免等功能。  
  
CAKE（Common Applications Kept Enhanced）是一种结合了调度器和流量整形器的Linux内核Qdisc模块，核心功能是有效缓解网络中的缓冲区膨胀（Bufferbloat）问题。  
  
  
**02**  
  
**漏洞描述**  
  
  
  
近日，CentOS Stream 9 中 CAKE Qdisc 组件的 Use-After-Free（UAF）权限提升漏洞细节被公开。该漏洞源于 cake_enqueue 函数在数据包丢弃时错误地返回了 NET_XMIT_SUCCESS 状态，导致父级 HFSC Qdisc 误认为入队成功并将其加入活跃列表；当该 class 被释放后，由于计数器未触发更新，其指针仍保留在活跃列表中，最终在出队操作时触发 UAF，攻击者可借此实现 root 提权。该漏洞的利用在 TyphoonPWN 2025 比赛的 Linux 类别中使用。  
```
static s32 cake_enqueue(struct sk_buff *skb, struct Qdisc *sch,
            struct sk_buff **to_free)
{
    ...
if (q->buffer_used > q->buffer_max_used)
        q->buffer_max_used = q->buffer_used;
if (q->buffer_used > q->buffer_limit) {                 // [1]
        u32 dropped = 0;
while (q->buffer_used > q->buffer_limit) {
            dropped++;
            cake_drop(sch, to_free);                        // [2]
        }
        b->drop_overlimit += dropped;
    }
return NET_XMIT_SUCCESS;
}
```  
  
当 buffer_used 大于 Qdisc 中设置的 buffer_limit 时 （代码[1]处），cake_enqueue 会调用 cake_drop （代码[2]处），从 Qdisc 中选择一个数据包并丢弃。  
  
如果将 buffer_limit 设置为一个很小的值（例如 1），即使只发送一个数据包，也会被丢弃。  
```
static int
hfsc_enqueue(struct sk_buff *skb, struct Qdisc *sch, struct sk_buff **to_free)
{
    unsigned int len = qdisc_pkt_len(skb);
    struct hfsc_class *cl;
    int err;
    bool first;
    cl = hfsc_classify(skb, sch, &err);
    if (cl == NULL) {
        if (err & __NET_XMIT_BYPASS)
            qdisc_qstats_drop(sch);
        __qdisc_drop(skb, to_free);
        return err;
    }
    first = !cl->qdisc->q.qlen;
    err = qdisc_enqueue(skb, cl->qdisc, to_free);
    if (unlikely(err != NET_XMIT_SUCCESS)) {                // [3]
        if (net_xmit_drop_count(err)) {
            cl->qstats.drops++;
            qdisc_qstats_drop(sch);
        }
        return err;
    }
    if (first) {
        if (cl->cl_flags & HFSC_RSC)
            init_ed(cl, len);                               // [4]
        if (cl->cl_flags & HFSC_FSC)
            init_vf(cl, len);
        if (cl->cl_flags & HFSC_RSC)
            cl->qdisc->ops->peek(cl->qdisc);
    }
    sch->qstats.backlog += len;
    sch->q.qlen++;
    return NET_XMIT_SUCCESS;
}
```  
  
在函数hfsc_enqueue中，由于 CAKE Qdisc 的 enqueue() 返回了 NET_XMIT_SUCCESS（代码[3]处），HFSC Qdisc 会认为 enqueue 过程正常完成，因此不会进行异常处理。如果这是某个 HFSC class 第一次入队数据包，就会调用 init_ed 将该 class 添加到 HFSC Qdisc 的 active list（活跃列表） 中（ 代码[4]处）。  
  
随后删除该 HFSC Qdisc class 时，class 被释放，但并没有从 HFSC 的 active list 中移除，从而留下一个 悬空指针。  
```
static int
hfsc_delete_class(struct Qdisc *sch, unsignedlong arg,
          struct netlink_ext_ack *extack)
{
    struct hfsc_sched *q = qdisc_priv(sch);
    struct hfsc_class *cl = (struct hfsc_class *)arg;
    if (cl->level > 0 || qdisc_class_in_use(&cl->cl_common) ||
        cl == &q->root) {
        NL_SET_ERR_MSG(extack, "HFSC class in use");
        return -EBUSY;
    }
    sch_tree_lock(sch);
    list_del(&cl->siblings);
    hfsc_adjust_levels(cl->cl_parent);
    qdisc_purge_queue(cl->qdisc);                           // [5]
    qdisc_class_hash_remove(&q->clhash, &cl->cl_common);
    sch_tree_unlock(sch);
    hfsc_destroy_class(sch, cl);
    return0;
}
```  
  
hfsc_delete_class 调用了 qdisc_purge_queue来清空子 Qdisc（即 CAKE Qdisc）（代码[5]处）。  
```
static inline void qdisc_purge_queue(struct Qdisc *sch)
{
    __u32 qlen, backlog;
    qdisc_qstats_qlen_backlog(sch, &qlen, &backlog);
    qdisc_reset(sch);
    qdisc_tree_reduce_backlog(sch, qlen, backlog);          // [6]
}
```  
  
qdisc_purge_queue 调用了 qdisc_tree_reduce_backlog （代码[6]处）。  
```
void qdisc_tree_reduce_backlog(struct Qdisc *sch, int n, int len)
{
    ...
    if (n == 0 && len == 0)                                 // [7]
        return;
    ...
        if (notify && cops->qlen_notify) {
            cl = cops->find(sch, parentid);
            cops->qlen_notify(sch, cl);                     // [8]
        }
    ...
}
```  
  
由于此时 CAKE Qdisc 中 不存在任何数据包，qlen 和 backlog 均为 0。  
  
由于 n == 0 && len == 0（代码[7]处）, qlen_notify 并不会被调用，导致 CAKE Qdisc 的父 class 无法从 HFSC 的 active list 中被移除（ 代码[8]处）。  
```
static struct sk_buff *
hfsc_dequeue(struct Qdisc *sch)
{
    ...
    cl = eltree_get_mindl(q, cur_time);                     // [9]
    ...
    skb = qdisc_dequeue_peeked(cl->qdisc);                 // [10]
    ...
}
```  
  
由于 HFSC Qdisc 的 active list 中仍然保留着这个已经被释放的 class 指针，在 hfsc_dequeue 中使用该 class 会触发 UAF。  
```
static inline struct sk_buff *qdisc_dequeue_peeked(struct Qdisc *sch)
{
struct sk_buff *skb = skb_peek(&sch->gso_skb);
if (skb) {                                              // [11]
        ...
    } else {
        skb = sch->dequeue(sch);                            // [12]
    }
return skb;
}
```  
  
UAF 发生在 hfsc_dequeue 中访问已经被释放的 cl->qdisc 时。 由于 qdisc_dequeue_peeked 会调用 sch->dequeue（代码[12]处）， 而 sch是被释放的对象，在此处可以实现控制流劫持。  
  
  
**03**  
  
**漏洞复现******  
  
  
  
360 漏洞研究院已成功复现该漏洞。复现过程基于官方 kernel-5.14.0-1.el9 分支代码，通过开启 KASAN（Kernel Address Sanitizer）检测机制编译内核，并在 QEMU 模拟器中运行 PoC 程序，捕获内核崩溃日志。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dZ7ia5iaWFzzibzxGfVa2jCnZsohR1Xdy8vP7MWYibH8b3Vx7ZMGLMEW14gLFXERsoaBlzVtAtjbk84lYAZiaNvwo5oY2YD4cg6uELRlbTcYSsUE/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dZ7ia5iaWFzz9CI0ObVbZyxH81HfzOzAYNwApOP5BPsS1cGGriaIbuvrIDVgRQLyMcV9Im4jX43tx9EYXZAHEJBZkvsp8pxhpj7PyqUDicPicW80/640?wx_fmt=png&from=appmsg "")  
  
CentOS Stream 9 CAKE Qdisc Use-After-Free漏洞复现  
  
  
**04**  
  
**漏洞影响范围******  
  
  
  
受影响软件版本：  
  
官方尚未公开，已知受影响分支：kernel-5.14.0-1.el9。  
  
  
**05**  
  
**修复建议******  
  
  
  
**正式防护方案：**  
  
目前官方尚未发布正式的安全补丁通告，建议受影响用户关注内核版本更新，并升级至 5.14.0-669.el9 或更高版本。  
  
查看官方内核源代码发现，在当前最新版本对应代码分支5.14.0-669.el9上，函数qdisc_tree_reduce_backlog中，以下代码被去掉。  
```
if (n == 0 && len == 0)                                 // [7]
return;
```  
  
从而使得函数qdisc_tree_reduce_backlog中不再会略过把class从active list 中移除的操作。问题将不会被触发。  
```
void qdisc_tree_reduce_backlog(struct Qdisc *sch, int n, int len)
{
    ...
   
    ...
        if (notify && cops->qlen_notify) {
            cl = cops->find(sch, parentid);
            cops->qlen_notify(sch, cl);                     // [8]
        }
    ...
}
```  
  
  
**06**  
  
**时间线**  
  
  
  
2026年2月11日，360漏洞研究院发布本安全风险通告。  
  
  
**07**  
  
参考链接  
  
  
  
https://ssd-disclosure.com/linux-kernel-net-sched-cake-qdisc-use-after-free-lpe/  
  
  
08  
  
更多漏洞情报  
  
  
  
建议您订阅360数字安全-漏洞情报服务，获取更多漏洞情报详情以及处置建议，让您的企业远离漏洞威胁。  
  
  
邮箱：360VRI@360.cn  
  
网址：https://vi.loudongyun.360.net  
  
  
  
“洞”悉网络威胁，守护数字安全  
  
  
**关于我们**  
  
  
360 漏洞研究院，隶属于360数字安全集团。其成员常年入选谷歌、微软、华为等厂商的安全精英排行榜, 并获得谷歌、微软、苹果史上最高漏洞奖励。研究院是中国首个荣膺Pwnie Awards“史诗级成就奖”，并获得多个Pwnie Awards提名的组织。累计发现并协助修复谷歌、苹果、微软、华为、高通等全球顶级厂商CVE漏洞3000多个，收获诸多官方公开致谢。研究院也屡次受邀在BlackHat，Usenix Security，Defcon等极具影响力的工业安全峰会和顶级学术会议上分享研究成果，并多次斩获信创挑战赛、天府杯等顶级黑客大赛总冠军和单项冠军。研究院将凭借其在漏洞挖掘和安全攻防方面的强大技术实力，帮助各大企业厂商不断完善系统安全，为数字安全保驾护航，筑造数字时代的安全堡垒。  
  
  
