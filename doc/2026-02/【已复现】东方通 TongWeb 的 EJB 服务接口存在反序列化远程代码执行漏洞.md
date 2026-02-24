#  【已复现】东方通 TongWeb 的 EJB 服务接口存在反序列化远程代码执行漏洞  
蟑螂恶霸
                    蟑螂恶霸  momo安全   2026-02-24 03:49  
  
## 免责声明  
>   
> 本文仅用于技术学习和讨论。请勿使用本文所提供的内容及相关技术从事非法活动，由于传播、利用此文所提供的内容或工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果均与文章作者及本账号无关，本次测试仅供学习使用。如有内容争议或侵权，请及时私信我们！我们会立即删除并致歉。谢谢！  
  
### 一、漏洞描述  
  
东方通 TongWeb 的 EJB 服务接口存在反序列化远程代码执行漏洞。攻击者可通过向 /ejbserver/ejb  
 发送构造后的序列化数据触发命令执行，进而获取目标系统权限。  
### 二、影响版本  
  
东方通 TongWeb（具体受影响版本请以厂商官方公告为准）  
### 三、Fofa语法  
  
header="TongWeb Server" || banner="Server: TongWeb Server"  
### 四、漏洞复现  
  
nuclei 批量复现：  
```
nuclei -t tongweb-ejb-rce-multi.yaml -l urls.txt

```  
  
poc:  
```
访问www.momosec.cn 搜索**东方通** 获取 poc

```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zRdbbmqUZwuXicP4u15rqvicnPvryTYGibicHJTpAhaicxJgnxlUvib1n7u7mFVUNXUqwwozf2rl4mjLOq1BHAhyfyQ7tbURr2V3OWLnSk61uSbdA/640?wx_fmt=png&from=appmsg "")  
### 五、漏洞修复  
1. 关注 TongWeb 官方安全通告，及时升级到最新安全版本。  
  
1. 对 /ejbserver/ejb  
 接口进行访问控制，限制外网直接访问。  
  
1. 在边界设备启用 WAF/IPS，拦截异常序列化流量。  
  
1. 排查服务器日志，重点关注异常 application/octet-stream  
 请求和可疑命令执行痕迹。  
  
### 六、漏洞脚本下载  
  
访问  
www.momosec.cn  
 搜索**东方通**  
 获取 poc  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zRdbbmqUZwtLHWj9ib3GdAhGGibDXKSlicbHIYRNPn1ibv1LTtFEz5s72FZzZxP7Y5UOISp0TA5RdTHgN4KibibceqOosuM6LCtpDwxp1r3EEwuwo/640?wx_fmt=png&from=appmsg "")  
### 七、技术服务推广  
  
✅Cn*d🀄️高提交到个人账户上，CNNVD中高 漏洞及一般、重要情报 支撑单位均可协助获得  
  
✅CISP、PTE/PTS、CISP-DSG、IRE/IRS、NISP一二级、PMP、CCSK、CISSP/CCSP、CISAW各种类、CCSC、itil、软考中高级、CDSP各种类、CISA，oscp等等全网最低价。ISO27001、ITss服务项目经理报名等下证即可，可对公，可开专普票  
  
✅需要私聊联系~![](https://mmbiz.qpic.cn/sz_mmbiz_png/zRdbbmqUZwvNAByRd75QymcIyAv7JYfPv9PIqic2YnEagwGe1TzkmoPXU2SMNmtKHESCoEhd3vicBOxExDNQ8KpmxbmVZQ64OicUxH0Jfw0OEo/640?wx_fmt=png&from=appmsg "")  
  
  
  
