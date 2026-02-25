#  Apache ActiveMQ漏洞遭利用，LockBit勒索软件批量入侵企业  
看雪学苑
                    看雪学苑  看雪学苑   2026-02-25 09:59  
  
近日，黑客  
利用Apache ActiveMQ服务器高危漏洞，入侵企业网络并部署LockBit勒索软件，  
从初始渗透到全面加密仅耗时约  
19天，  
风险极高。  
  
  
此次攻击的  
核心漏洞为Apache ActiveMQ的远程代码执行漏洞CVE-2023-46604。  
2024年2月中旬，黑客向公网可访问的ActiveMQ服务器发送特制命令，诱导其加载恶意配置文件，进而通过Windows CertUtil工具下载攻击程序。  
  
  
攻击程序执行后，立即与黑客控制的166.62.100[.]52服务器建立连接，仅40分钟就获取系统最高权限，并窃取跳板机的账户凭证。  
  
  
据The DFIR Report溯源，黑客虽在入侵次日被逐出，但漏洞服务器未打补丁，攻击路径仍开放。18天后，黑客利用相同漏洞、窃取的特权账户凭证，再次轻松入侵内网。  
  
  
重新入侵后，黑客确认域管理员权限，通过伪装扫描工具枚举内网主机，再通过RDP会话传入LB3.exe等LockBit勒索软件，分别在文件服务器和普通主机上执行加密。此次攻击为独立黑客利用泄露工具发起，勒索通知未指向LockBit官方。  
  
  
整个攻击周期达419小时（约19天），若未检测到初始入侵，黑客重新进入后不足90分钟即可启动加密，防御窗口极短。  
  
  
凭证窃取是关键，多种手段规避检测  
  
此次攻击中，黑客通过读取多台主机的LSASS进程内存窃取凭证，日志显示其采用注入代码方式，不留明显痕迹。被盗的特权账户凭证，成为二次入侵的关键。  
  
  
黑客还通过多重混淆处理攻击命令，采用内存注入方式执行恶意程序，规避终端检测——开启Microsoft Defender的主机成功拦截，未防护主机则被完全入侵。  
  
  
为掩盖痕迹，黑客安装AnyDesk留后门、开启RDP端口后立即删除相关文件、清空系统日志，并禁用Windows Defender。  
  
  
紧急防御建议  
  
企业需立即采取以下措施防范攻击：  
  
- 立即为ActiveMQ服务器打补丁，修复CVE-2023-46604漏洞；  
  
- 启用LSASS保护，防止账户凭证被窃取；  
  
- 监控日志清空行为，警惕异常操作；  
  
- 限制未授权远程访问工具（如AnyDesk）使用；  
  
- 怀疑入侵后，立即重置所有账户凭证。  
  
  
参考来源  
  
1. The DFIR Report（攻击细节原始来源）  
  
2. 公开网络安全漏洞库（CVE-2023-46604相关）  
  
3. 行业公开威胁分析报告（LockBit特征参考）  
  
  
  
﹀  
  
﹀  
  
﹀  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
