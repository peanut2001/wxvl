#  紧急提醒！立即备份自己的VPS数据 大量VPS提供商面临勒索软件攻击|国产飞牛系统fnOS疑似出现重大安全漏洞 官方已修复但没有发布安全公告  
 黑白之道   2026-02-02 01:19  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif "")  
  
**关键词**  
  
  
  
勒索软件  
  
  
![紧急安全提醒！请立即备份自己的VPS数据 大量VPS提供商面临勒索软件攻击](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaRuMkW4S00udFPnia9JibPrEIUQm2JPulJJHFRyFK0QmaqXPSxYhvvvx5Xff7ibzgz1cic3CacMNTEaQ/640?wx_fmt=jpeg "")  
  
美国廉价虚拟服务器提供商 **CloudCone**  
 已确认，其部分节点遭遇严重安全事件，**用户数据无法恢复**  
。  
  
  
CloudCone 表示，公司位于**洛杉矶机房的部分宿主节点（母机）遭到黑客入侵**  
，攻击者直接覆写了虚拟机的引导磁盘信息，导致多台 VPS 数据彻底损坏。事件发生后，CloudCone 对受影响节点进行了重装处理，并重新部署系统，但明确指出：**用户数据需自行依赖本地或异地备份恢复，公司无法提供数据找回服务**  
。  
  
### 攻击源头指向 Virtualizor 管理面板  
  
  
从目前披露的信息来看，此次事件的真正安全隐患并不在底层硬件，而是指向 **虚拟机管理面板 Virtualizor**  
。CloudCone 在官方回应中暗示，攻击行为很可能源自 Virtualizor 存在的安全漏洞，被攻击者成功利用。  
  
  
在 **LET（LowEndTalk）等核心主机社区**  
的讨论中，有多名用户指出，攻击者疑似利用了 **Virtualizor 与计费面板 WHMCS 的集成插件漏洞**  
。该漏洞一旦被利用，攻击者可能直接获得管理员权限，从而在管理面板或宿主节点层面对虚拟机执行高权限操作，包括磁盘覆写、系统破坏等。  
  
### 受影响的不止 CloudCone  
  
  
值得注意的是，**CloudCone 并非唯一受影响的服务商**  
。  
  
- **ColoCrossing 旗下 ColoCloud**  
 于 1 月 30 日对 Virtualizor 管理端进行了临时维护  
  
- 多名用户反馈收到 CCS 发出的**安全维护与平台加固通知**  
  
- **HostSlick**  
 公开表示，其 **超过 25% 的服务器遭到感染**  
  
- **OuiHeberg**  
 也被列入疑似受攻击服务商名单  
  
HostSlick 方面称，其已就漏洞问题与 Virtualizor 开发商沟通，但**开发方拒绝承认漏洞存在**  
。  
  
### 多家使用 Virtualizor 的服务商处于高风险状态  
  
  
目前已知仍在使用 **Virtualizor + WHMCS 插件**  
架构的虚拟服务器提供商包括但不限于：  
- ColoCloud  
  
- Virtono  
  
- SolidSEOVPS  
  
- Naranjatech  
  
- LittleCreek  
  
- DediRock  
  
- Chunkserv  
  
- RareCloud  
  
上述服务商由于管理架构相似，**理论上均处于潜在高风险状态**  
。  
###   
### 官方建议  
  
  
截至目前，Virtualizor 官方尚未发布明确的漏洞通告或补丁说明。鉴于攻击范围正在扩大，**建议正在使用相关 VPS 的用户立即完成完整数据备份**  
，并密切关注服务商后续安全公告，以防类似风险进一步扩大。  
  
  
**关键词**  
  
  
  
漏洞  
  
  
据 V2EX 与飞牛官方论坛多名网友反馈，**飞牛系统（fnOS）疑似存在严重安全漏洞**  
，已有多台部署该系统的设备遭到黑客攻击，目前尚无法确认是否发生数据泄露。  
  
部分用户表示，即便已启用 **HTTPS、强密码及 2FA**  
，设备仍被植入恶意程序，说明问题并非源于用户配置不当，而是系统层面可能存在漏洞。  
  
另有飞牛论坛网友指出，fnOS 曾存在**路径穿越漏洞**  
，攻击者可借此访问整个 NAS 的文件系统，包括用户数据和敏感配置文件，该漏洞据称已在 **1.1.15 版本**  
中修复。  
  
需要注意的是，如设备出现**卡顿、卡死、网络异常、连接数异常或无法连接飞牛服务器**  
等情况，可能意味着设备已遭入侵，用户应立即进行排查。  
  
![国产飞牛系统fnOS疑似出现重大安全漏洞 官方已修复但没有发布安全公告](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliah0k6RfNmQeeTqZ1E6WkozTibibrfjsibgmCSna7ia2lZF2AlqtaqhDKLBWwrRAPNkTicJ1pBDu9J2mtQ/640?wx_fmt=png&from=appmsg "")  
  
令人困惑的是，面对如此严重的安全问题，**飞牛官方并未发布任何正式安全公告**  
，目前相关信息仅来源于论坛与用户自行披露。若仍在使用旧版本 fnOS，设备可能正处于高风险状态。  
  
因此，飞牛官方有必要：  
- 强制推送安全更新或启用自动更新机制  
  
- 通过短信、邮件等方式主动通知用户  
  
- 对已受影响设备进行取证分析，明确是否存在数据泄露，并发布相应安全通告  
  
在安全事件中保持沉默或回避披露，短期或许能减少舆论影响，但长期来看，**只会进一步削弱用户对飞牛系统的信任**  
。  
  
> **文章来源 ：安全圈**  
  
  
**精彩推荐**  
  
  
  
  
# 乘风破浪|华盟信安线下网络安全就业班招生中！  
  
  
[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650575781&idx=2&sn=ea0334807d87faa0c2b30770b0fa710d&chksm=83bdf641b4ca7f5774129396e8e916645b7aa7e2e2744984d724ca0019e913b491107e1d6e29&scene=21#wechat_redirect)  
  
  
# 【Web精英班·开班】HW加油站，快来充电！  
  
  
‍[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650594891&idx=1&sn=b2c5659bb6bce6703f282e8acce3d7cb&chksm=83bdbbafb4ca32b9044716aec713576156968a5753fd3a3d6913951a8e2a7e968715adea1ddc&scene=21#wechat_redirect)  
  
  
‍  
# 始于猎艳，终于诈骗！带你了解“约炮”APP  
  
[](http://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650575222&idx=1&sn=ce9ab9d633804f2a0862f1771172c26a&chksm=83bdf492b4ca7d843d508982b4550e289055c3181708d9f02bf3c797821cc1d0d8652a0d5535&scene=21#wechat_redirect)  
  
**‍**  
  
