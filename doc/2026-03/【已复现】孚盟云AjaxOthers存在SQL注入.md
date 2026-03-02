#  【已复现】孚盟云AjaxOthers存在SQL注入  
原创 蟑螂恶霸
                    蟑螂恶霸  momo安全   2026-03-02 00:53  
  
## 免责声明  
>   
> 本文仅用于技术学习和讨论。请勿使用本文所提供的内容及相关技术从事非法活动，由于传播、利用此文所提供的内容或工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果均与文章作者及本账号无关，本次测试仅供学习使用。如有内容争议或侵权，请及时私信我们！我们会立即删除并致歉。谢谢！  
  
### 一、漏洞描述  
  
孚盟云AjaxOthers存在SQL注入。攻击者可通过构造恶意参数触发 SQL 注入，导致数据库信息泄露或业务数据被篡改。  
### 二、影响版本  
  
孚盟云AjaxOthers存在SQL注入（具体受影响版本请以厂商官方公告为准）  
### 三、Fofa语法  
  
app="孚盟软件-孚盟云"  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zRdbbmqUZwsDZIL8Wb4nhSPrB924Lqte7LkjXQP5wsMXibmJJpkdBGArctia36nJxRnCSVCnG62XTWNpM21VlJ6wfBFaUrJlgsQZykHxKPIicE/640?wx_fmt=png&from=appmsg "")  
  
### 四、漏洞复现  
  
poc:   
  
访问  
www.momosec.cn 搜索  
浮**盟云**  
 获取 poc  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zRdbbmqUZwv2wjh9lxg8Q6AOcwibaaNriaOp6e7rER5OZcsbPQVJpJ3UG3L7duP0hQoKwntoBhAFiclKmdrC1TKgLoor5PNibdtP802BTa3ckT8/640?wx_fmt=png&from=appmsg "")  
### 五、漏洞修复  
1. 对所有用户输入进行严格白名单校验，使用参数化查询/预编译语句。  
  
1. 为数据库账号配置最小权限，禁止高危系统权限。  
  
1. 在应用和网关侧部署 WAF 规则，拦截常见注入载荷。  
  
1. 对相关接口进行安全审计，及时修复并更新版本。  
  
### 六、漏洞脚本下载  
  
访问www.momosec.cn  
  
 搜索**浮盟云**  
 获取 poc  
  
![](https://mmbiz.qpic.cn/mmbiz_png/zRdbbmqUZwsiaZQ6z7N9PhzMb8Hdib00wYicUoxyRjLBh20UDKhC6ySa6UTINicL65SYoIJNVxcV8iaudEFU6tNR0hbuVku4Lc8FMdxUe0EQxAXY/640?wx_fmt=png&from=appmsg "")  
### 七、技术服务推广  
  
✅Cn*d️高提交到个人账户上，CNNVD中高 漏洞及一般、重要情报 支撑单位均可协助获得  
  
✅CISP、PTE/PTS、CISP-DSG、IRE/IRS、NISP一二级、PMP、CCSK、CISSP/CCSP、CISAW各种类、CCSC、itil、软考中高级、CDSP各种类、CISA，oscp等等全网最低价。ISO27001、ITss服务项目经理报名等下证即可，可对公，可开专普票  
  
✅需要私聊联系~  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zRdbbmqUZwtuFiavQEObr3uz0E6yDrlrhMv0hMe2ls69dEw7rpct1SxQibIgummScibPQAB2A9m4iccwmA26xTQH6pPyl9ib6MqymN7nE1NWQf04/640?wx_fmt=png&from=appmsg "")  
  
  
  
