#  历时数十年的漏洞与新堆损坏问题，Linux系统关键glibc漏洞曝光  
 FreeBuf   2026-01-19 10:32  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibofXkkXsibM0gxKLeZpLUxE3X2xpcA7HHU2yCSnn8wTB0uDQiavWUnQzj5icibJoWDs28VeaOoWEy3zA/640?wx_fmt=png&from=appmsg "")  
  
  
作为大多数Linux系统核心基础的GNU C库（glibc）维护团队披露了两个安全漏洞的详细信息，问题严重性从高危堆损坏到信息泄露不等。这些漏洞影响范围广泛，其中一个漏洞可追溯至glibc 2.0版本。  
  
  
**Part01**  
## 高危漏洞的技术特性  
  
  
虽然这两个漏洞都可能造成严重后果（如堆损坏和ASLR绕过），但其利用所需的技术门槛较高，可能限制了实际影响范围。  
  
  
其中更严重的是CVE-2026-0861漏洞，CVSS评分高达8.4分。该漏洞涉及库内存对齐函数（memalign、posix_memalign和aligned_alloc）中的整数溢出问题，影响glibc 2.30至2.42版本。攻击者若能控制应用程序传递特定参数组合，可导致堆损坏。  
  
  
要触发崩溃，攻击者必须同时控制大小和对齐参数。此外，大小参数必须接近PTRDIFF_MAX的极大值才能引发溢出。安全公告指出这是"非常见使用模式"，因为对齐参数通常是页面大小等固定值而非用户可控输入。  
  
  
**Part02**  
## 存在数十年的信息泄露漏洞  
  
  
第二个漏洞CVE-2026-0915是存在于库中数十年的信息泄露问题，影响2.0至2.42版本。该缺陷位于getnetbyaddr和getnetbyaddr_r函数中。当这些函数被调用来查询"零值网络"（即net == 0x0）且系统配置使用DNS后端时，函数可能意外将未修改的堆栈内容传递给DNS解析器。  
  
  
这种"堆栈内容泄露"会导致主机机密性受损。虽然数据泄露范围仅限于相邻堆栈，但理论上攻击者可利用泄露的指针值加速ASLR（地址空间布局随机化）绕过。与整数溢出漏洞类似，该漏洞利用门槛较高，要求攻击者能够"窥探应用程序与DNS服务器之间"的通信才能捕获泄露数据。  
  
  
**Part03**  
## 修复建议  
  
  
系统管理员应评估漏洞对其发行版的特定影响，并在可用时及时应用补丁。  
  
  
**参考来源：**  
  
Decades-Old Flaw & New Heap Corruption: Critical glibc Bugs Revealed  
  
https://securityonline.info/decades-old-flaw-new-heap-corruption-critical-glibc-bugs-revealed/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334067&idx=1&sn=817c2149a41e006fedbb453ec71f40ec&scene=21#wechat_redirect)  
###   
### 电台讨论  
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
