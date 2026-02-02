#  三菱电机 SCADA 系统曝漏洞，恐引发工业生产中断  
HackerNews
                    HackerNews  安全威胁纵横   2026-02-02 10:08  
  
高危漏洞    
  
紧急修复指南    
  
RCE Patch    
  
Iconics Suite SCADA 系统存在一项中危漏洞，攻击者可利用该漏洞在关键工业控制系统上触发拒绝服务状态。  
  
推测e  
  
  
该漏洞编号为 CVE-2025-0921，广泛部署于  
汽车、能源及制造业  
的监控与数据采集（SCADA）基础设施。  
**1**  
  
  
**漏洞详情**  
  
CVE-2025-0921 源于三菱电机 Iconics Digital Solutions 的 GENESIS64 软件中，**多个服务存在“以不必要权限执行”的安全缺陷**  
。  
  
  
该漏洞 CVSS 评分为 6.5 分，评级为中危。攻击者成功利用该漏洞后，  
可**滥用特权文件系统操作提升权限、破坏核心系统二进制文件，最终导致系统完整性与可用性受损**  
。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AYVicr6OzRAH1otBhA90uqrMemhtDETHdK6nW1sRIibN9a5UQIzX0TqibIu5GgM1FZRgAkSZAjf0QVqUYTtHkeYSA/640?wx_fmt=png&from=appmsg "")  
  
  
此漏洞由 Unit 42 的研究员 Asher Davila 和 Malav Vyas 在 2024 年初的一次全面安全评估中发现。这是在微软 Windows 平台的 Iconics Suite 10.97.2 及更早版本中发现的 6 项漏洞之一。此前研究人员已披露该 SCADA 平台存在的 5 项相关漏洞，CVE-2025-0921 是后续调查中发现的  
新增威胁  
。  
  
  
根据三菱电机的安全公告，该漏洞影响 GENESIS64、MC Works64 的所有版本以及 GENESIS 11.00 版本。Iconics Suite 在**全球超过 100 个国家拥有数十万安装实例**  
，遍布**政府设施、军事基地、水处理厂、公共事业及能源供应商**  
等关键基础设施领域。  
  
  
  
**0****2**  
  
  
**技术原理与利用途径**  
  
该漏洞存在于工业流程监控告警管理系统 AlarmWorX64 MMX 的 Pager Agent 组件中。  
  
具备本地访问权限的攻击者，可通过篡改 C:\ProgramData\ICONICS 目录下 IcoSetup64.ini 文件中存储的 SMSLogFile 路径配置来利用该漏洞。攻击链流程包括：将日志文件存储路径创建为指向目标系统二进制文件的符号链接。当管理员发送测试消息或系统自动触发告警时，  
日志信息会沿符号链接覆盖核心驱动文件  
（如为 Windows 系统组件提供加密服务的 cng.sys）。  
  
系统重启后，被破坏的驱动会导致启动失败，设备陷入无限修复循环，最终使工业控制（OT）工程工作站无法运行。  
  
研究人员证实，该漏洞与 CVE-2024-7587 漏洞结合后利用难度会大幅降低；CVE-2024-7587 是此前披露的 GenBroker32 安装程序漏洞，会给 C:\ProgramData\ICONICS 目录赋予过高权限，  
允许任意本地用户修改核心配置文件  
。但即便单独利用该漏洞，若日志文件因配置不当、其他漏洞或社会工程学攻击具备可写权限，攻击者仍可成功触发漏洞。  
  
三菱电机已为 GENESIS 11.01 及后续版本发布修复补丁，客户可从 Iconics 社区资源中心下载。针对 GENESIS64 用户，修复版本正在开发中，将于近期发布。厂商明确表示暂无 MC Works64 版本补丁发布计划，相关客户需在此期间落实漏洞缓解措施。  
  
转载请注明出处@安全威胁纵横，封面来源于网络；  
  
消息来源：https://cybersecuritynews.com/scada-vulnerability-triggers-dos/  
  
  
  
  
  
  
  
更多网络安全视频，请关注视频号“知道创宇404实验室”  
  
  
  
  
  
  
  
  
  
