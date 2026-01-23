#  Redis官方容器曝出RCE漏洞，研究人员详解"简单"栈溢出利用链  
 FreeBuf   2026-01-23 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icJZpTxpYYQtLW9fPVic9DLRhkibmgHIa6jNZC6qO7PzmqQWeUVBtG0icATY7B2Dn8BsIm94Awpu2M1A/640?wx_fmt=other&from=appmsg "")  
  
  
JFrog安全研究团队公开披露了Redis中一个高危漏洞的完整利用链，证明在2026年，"老派"的栈缓冲区溢出攻击依然活跃且危险。  
  
  
该漏洞编号为CVE-2025-62507，CVSS评分为8.8分，影响Redis 8.2.0至8.2.2版本。虽然官方公告已警告潜在风险，但JFrog团队决定进一步验证是否可实现完整的远程代码执行（RCE），并最终取得成功。  
  
  
**Part01**  
## 漏洞技术分析  
  
  
漏洞存在于XACKDEL命令中，这是Redis为优化流处理而引入的新功能。该命令允许用户在单个原子操作中确认并删除多条消息，但实现时未进行基本的边界检查。  
  
  
分析报告指出："核心问题在于代码未验证客户端提供的ID数量是否在该栈分配数组的边界范围内。"当用户提供的消息ID超过固定大小数组容量时，函数会盲目写入缓冲区末端之外。由于攻击者可控制这些ID，因此可覆盖关键栈内存（包括函数返回地址）。  
  
  
**Part02**  
## 官方镜像安全缺陷  
  
  
现代软件通常采用"栈金丝雀"机制防御此类攻击——通过在栈上放置秘密值来检测执行被劫持前的内存损坏。但研究人员在调查中发现，官方Redis Docker镜像存在惊人缺陷："令人惊讶的是，对EIP的直接控制表明官方Docker镜像中的Redis在编译时未启用栈金丝雀保护！"  
  
  
这一疏漏使得利用难度大幅降低。在没有金丝雀防护的情况下，研究人员能精确控制指令指针。他们构建了面向返回编程（ROP）链绕过NX（不可执行）保护，利用系统自身的mprotect函数将栈标记为可执行后运行自定义shellcode。  
  
  
**Part03**  
## 实际攻击演示  
  
  
JFrog通过发送特定命令序列成功演示了攻击：先发送XGROUP CREATE命令，再发送包含62个精心构造消息ID的XACKDEL命令，最终触发反向shell。  
  
  
**Part04**  
## 影响范围与风险  
  
  
该漏洞已在Redis 8.3.2版本中修复。但Shodan扫描显示仍有近3000台服务器明确运行受影响版本，主要分布在德国、美国和中国的服务器上。由于Redis默认不强制身份验证，该漏洞通常允许未经认证的远程代码执行，使其成为机会主义攻击者的主要目标。  
  
  
**参考来源：**  
  
Redis RCE Exposed: Researchers Detail Exploit for “Simple” Stack Overflow in Official Containers  
  
https://securityonline.info/redis-rce-exposed-researchers-detail-exploit-for-simple-stack-overflow-in-official-containers/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334067&idx=1&sn=817c2149a41e006fedbb453ec71f40ec&scene=21#wechat_redirect)  
  
### 电台讨论  
###   
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
