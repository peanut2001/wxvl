#  Juniper Networks PTX 系列产品的关键漏洞允许完全控制路由器  
Rhinoer
                    Rhinoer  犀牛安全   2026-03-12 16:00  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vO1zY1O9p8Lic67bfibHqRmovEFIZkUE0MDcbGtK6dicH9s7cE6xvZrrDjceKeh747V9aLLN5qXiaQ6H8VcjuWWUE9wDG02aoIGUMDhcn8GIxtM/640?wx_fmt=png&from=appmsg "")  
  
Juniper Networks PTX 系列路由器上运行的 Junos OS Evolved 网络操作系统存在一个严重漏洞，可能允许未经身份验证的攻击者以 root 权限远程执行代码。  
  
PTX系列路由器是高性能核心路由器和对等路由器，专为高吞吐量、低延迟和可扩展性而设计。它们通常用于互联网服务提供商、电信服务提供商和云网络应用。  
  
该安全问题被识别为 CVE-2026-21902  ，是由“On-Box 异常检测”框架中不正确的权限分配引起的，该框架应该只通过内部路由接口向内部进程公开。  
  
然而，Juniper Networks 在一份安全公告中解释说，该漏洞允许通过外部暴露的端口访问该框架。  
  
由于该服务以 root 用户身份运行且默认启用，因此成功利用该漏洞将允许已在网络上的攻击者在未经身份验证的情况下完全控制该设备。  
  
该问题影响 PTX 系列路由器上 25.4R1-S1-EVO 和 25.4R2-EVO 之前的 Junos OS Evolved 版本。更早的版本也可能受到影响，但供应商不会评估已达到工程终止或生命周期终止 (EoL) 阶段的版本。  
  
25.4R1-EVO 之前的版本以及标准（非演进版）Junos OS 版本不受 CVE-2026-21902 的影响。Juniper Networks 已在产品版本 25.4R1-S1-EVO、25.4R2-EVO 和 26.2R1-EVO 中提供了修复程序。  
  
Juniper 的安全事件响应团队 (SIRT) 表示，在发布安全公告时，他们并不知道该漏洞已被恶意利用。  
  
如果无法立即进行修补，供应商建议使用防火墙过滤器或访问控制列表 (ACL) 将对易受攻击端点的访问限制在受信任的网络范围内。或者，管理员可以使用以下方法完全禁用易受攻击的服务：  
  
'request pfe anomalies disable'  
  
由于 Juniper Networks 的网络设备被云数据中心和大型企业等需要高带宽的服务提供商使用，因此它通常是高级黑客的理想目标。  
  
2025 年 3 月，有消息透露，某国网络间谍活动者在已停用的 Junos OS MX 路由器上部署定制后门，以投放一系列“TinyShell”后门变种。  
  
2025 年 1 月，一场名为“J-magic”的恶意软件活动以半导体、能源、制造和 IT 行业使用的 Juniper VPN 网关为目标，部署了网络嗅探恶意软件，该恶意软件在收到“魔法数据包”时会激活。  
  
2024 年 12 月，Juniper Networks 智能路由器成为Mirai 僵尸网络攻击的目标，被纳入分布式拒绝服务 (DDoS) 攻击群中。  
  
  
信息来源：  
BleepingComputer  
  
