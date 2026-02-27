#  【已复现】深科特LEAN MES系统的MesATEApi.asmx接口存在任意文件上传漏洞  
原创 蟑螂恶霸
                    蟑螂恶霸  momo安全   2026-02-27 00:51  
  
## 免责声明  
>   
> 本文仅用于技术学习和讨论。请勿使用本文所提供的内容及相关技术从事非法活动，由于传播、利用此文所提供的内容或工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果均与文章作者及本账号无关，本次测试仅供学习使用。如有内容争议或侵权，请及时私信我们！我们会立即删除并致歉。谢谢！  
  
### 一、漏洞描述  
  
深科特LEAN MES系统的MesATEApi.asmx接口存在任意文件上传致远程代码执行（RCE）漏洞，该漏洞因接口未对用户上传文件进行严格校验与过滤，使得攻击者可绕过安全机制上传含恶意代码的文件（如恶意脚本）。  
### 二、影响版本  
  
深科特LEAN MES系统  
### 三、Fofa语法  
  
app="SKTMAX-LEAN-MES"  
### 四、漏洞复现  
  
nuclei.exe -l urls.txt -t 深科特rce.yaml  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zRdbbmqUZwuX6JXCJibJEQbEQeSV5Ooo7EoibNvtHNHoOYHxM75Zpf6HBOnUgibKV7Xh3DrOp5rllM72xFiby2L7eCnFthibXcaXHiahyyeMWicgag/640?wx_fmt=png&from=appmsg "")  
### 五、漏洞修复  
  
关注厂商动态，及时升级至安全版本  
### 六、漏洞脚本下载  
  
poc:   
  
访问  
www.momosec.cn 搜索**深科特**  
 获取 poc  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zRdbbmqUZwut38rXd3BD2MqsGWC7DmZu3Es1SE7INJFkr3AXkdZIicmOY9mDZF7vF5dSwFTny1Q1vbYbhGiaH6x8mymQboHmoXKxobLxW5l54/640?wx_fmt=png&from=appmsg "")  
### 七、技术服务推广  
  
✅Cn*d🀄️高提交到个人账户上，CNNVD中高 漏洞及一般、重要情报 支撑单位均可协助获得  
  
✅CISP、PTE/PTS、CISP-DSG、IRE/IRS、NISP一二级、PMP、CCSK、CISSP/CCSP、CISAW各种类、CCSC、itil、软考中高级、CDSP各种类、CISA，oscp等等全网最低价。ISO27001、ITss服务项目经理报名等下证即可，可对公，可开专普票  
  
✅需要私聊联系~  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zRdbbmqUZwvAzGY0HgPuIzIcW29tB7QFibX7jYQhNA3KtmUT2uQf9TVRNaoNBmmIx7uzZSWXOed1ZC0QMzm2XowgYn9d3DnSYFgLfteU1jbM/640?wx_fmt=png&from=appmsg "")  
  
  
  
