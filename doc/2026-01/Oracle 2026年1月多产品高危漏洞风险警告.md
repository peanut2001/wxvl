#  Oracle 2026年1月多产品高危漏洞风险警告  
安融技术
                    安融技术  安融技术   2026-01-22 03:28  
  
Oracle  
公司发布了  
2026  
年  
1  
月关键补丁更新（  
Critical Patch Update, CPU  
），修复了其全线产品中存在的多个高危安全漏洞。本次安全更新涵盖了数据库、中间件、应用系统等多个核心产品线，其中多个漏洞的  
CVSS v3.1  
评分达到  
10.0  
分（最高危级别），对企业信息系统安全构成严重威胁。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCCKJJhicxaIzjVtMY2GAVH5CTvtibdNKbVmIhXrYmJFiaY0GFlNg63bkmX55rJDY4WDke3zoWHKanic8A/640?wx_fmt=jpeg&from=appmsg "")  
  
  
一、高危漏洞分布概况  
  
本次更新涉及多家产品线，部分关键漏洞详情如下：  
  
1. Oracle Communications（通信产品线）  
  
漏洞数量：  
56  
个新安全补丁  
  
远程利用：  
34  
个漏洞可在无需认证情况下远程利用  
  
最高风险评分：  
10.0  
分（超危级别）  
  
受影响产品：包括  
Oracle Cloud Native Session Border Controller  
、  
Oracle Communications Billing and Revenue Management  
、  
Oracle Session Border Controller  
等多个核心通信系统。  
  
2. Oracle Fusion Middleware（融合中间件）  
  
最高风险评分：  
10.0  
分  
  
核心受影响组件：  
  
Oracle WebLogic Server  
（版本  
12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0  
）  
  
Oracle Access Manager  
  
Oracle HTTP Server  
  
Oracle Coherence  
  
风险特点：多个组件存在远程代码执行风险。  
  
3. Oracle MySQL数据库  
  
漏洞数量：  
20  
个新安全补丁  
  
远程利用：  
7  
个漏洞可在无需认证情况下远程利用  
  
最高风险评分：  
9.8  
分  
  
受影响范围：涵盖  
MySQL Server 8.0/8.4/9.0  
系列、  
MySQL Cluster  
、  
MySQL Connectors  
等全系列产品。  
  
4. Oracle Commerce（商务平台）  
  
漏洞数量：  
7  
个新安全补丁  
  
远程利用：  
6  
个漏洞可在无需认证情况下远程利用  
  
最高风险评分：  
10.0  
分  
  
受影响产品：  
Oracle Commerce Guided Search  
、  
Oracle Commerce Platform  
（版本  
11.4.0  
）。  
  
5. Oracle Supply Chain（供应链系统）  
  
漏洞数量：  
10  
个新安全补丁  
  
远程利用：  
8  
个漏洞可在无需认证情况下远程利用  
  
最高风险评分：  
9.8  
分  
  
受影响产品：  
Oracle Agile PLM  
、  
Oracle Autovue  
等关键供应链管理系统。  
  
6. 关键安全补丁集合（CPU）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f0KlQiaibhCCCKJJhicxaIzjVtMY2GAVH5CAiale6wY7SQzZxLryD1mAb1X8d8l22C72GBo24OFOIz7fQpUyZUib7pQ/640?wx_fmt=jpeg&from=appmsg "")  
  
  
特别提醒：目前多个Oracle WebLogic Server版本已停止维护，详情如下：  
  
10.3.6.0、11.1.1.9版本最终CPU截止至2021年10月；  
  
12.1.3.0版本最终CPU截止至2022年01月。  
  
二、重点关注的超危漏洞  
  
CVE-2026-21535：Oracle WebLogic Server远程命令执行漏洞  
  
影响组件：  
WebLogic Server  
核心组件（  
T3/IIOP  
协议）  
  
CVSS  
评分：  
10.0  
  
利用特点：无需认证即可远程利用，攻击者可执行任意系统命令  
  
影响版本：  
12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0  
  
CVE-2026-21556：Oracle Agile PLM框架接管漏洞  
  
风险等级：  
CVSS  
评分  
9.9  
  
攻击方式：通过  
HTTP  
协议低权限访问即可实现系统接管  
  
历史关联：该系列产品在  
2025  
年  
11  
月曾出现被积极利用的漏洞（  
CVE-2025-21287  
）  
  
三、其他关键产品线风险  
  
Oracle Database Server  
  
7  
个新补丁，  
2  
个可远程利用  
  
最高  
CVSS  
评分  
7.4  
  
影响版本：  
19c  
、  
21c  
、  
23c  
全系列。  
  
Oracle Java SE  
  
11  
个漏洞全部可远程利用  
  
最高  
CVSS  
评分  
7.5  
  
影响范围：  
Java SE 8/11/17/21/25  
及  
GraalVM  
等版本。  
  
Oracle GoldenGate  
  
5  
个新补丁，  
3  
个可远程利用  
  
最高  
CVSS  
评分  
8.1  
  
影响数据同步与集成环境。  
  
四、安全建议  
  
1.   
立即评估影响范围：各单位需紧急排查所使用的  
Oracle  
产品线及版本是否在本次漏洞影响范围内。  
  
2.   
优先修复超危漏洞：对  
CVSS  
评分  
10.0  
和  
9.8  
的超危漏洞，应在  
24-48  
小时内完成补丁测试与部署。  
  
3.   
加强网络隔离：在补丁部署前，建议对受影响的系统实施网络访问控制，限制非授权访问。  
  
4.   
启用安全监测：加强对  
WebLogic Server  
、  
MySQL  
数据库等关键组件的网络流量监控，及时发现异常利用行为。  
  
5.   
制定应急计划：针对可能的攻击场景，提前准备系统恢复与应急处置方案。  
  
