#  漏洞预警 | Fortinet身份认证绕过漏洞  
浅安
                    浅安  浅安安全   2026-02-11 00:01  
  
**0x00 漏洞编号**  
- # CVE-2026-24858  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
FortiOS是Fortinet公司推出的下一代防火墙操作系统，提供深度包检测、入侵防御、SSL解密、零信任网络访问等高级安全功能，广泛应用于企业边界防护。FortiManager是集中管理平台，用于统一配置和监控多台Fortinet安全设备。FortiAnalyzer则是日志收集与分析系统，支持安全事件关联、合规审计和威胁可视化。FortiProxy是安全Web网关解决方案，提供URL过滤、应用控制和恶意软件防护能力。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SU1ibQ8sYR4TvrgDEIO9AXibfKFIopibSrR0Mp0me9xDjXtCzSPic2IVCOY1hkEeBBglLO9zQyicL3N8BA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**CVE-2026-24858**  
  
**漏洞类型：**  
身份认证绕过  
  
**影响：**  
越权操作  
  
**简述：**  
Fortinet存在身份认证绕过漏洞，由于FortiCloud单点登录功能中的身份验证逻辑缺陷，当设备启用FortiCloud SSO认证时，攻击者可利用自身合法的FortiCloud账户及已注册设备，绕过正常身份认证机制，直接登录到其他用户账号下注册的设备。攻击者利用此漏洞可获取目标设备的管理员权限，执行下载设备配置文件、创建本地管理员账号等恶意操作，进而实现对内部网络的深度渗透。  
  
**0x04 影响版本**  
- 7.6.0 <= FortiAnalyzer <= 7.6.5  
  
- 7.4.0 <= FortiAnalyzer <= 7.4.9  
  
- 7.2.0 <= FortiAnalyzer <= 7.2.11  
  
- 7.0.0 <= FortiAnalyzer <= 7.0.15  
  
- 7.6.0 <= FortiManager <= 7.6.5  
  
- 7.4.0 <= FortiManager <= 7.4.9  
  
- 7.2.0 <= FortiManager <= 7.2.11  
  
- 7.0.0 <= FortiManager <= 7.0.15  
  
- 7.6.0 <= FortiOS <= 7.6.5  
  
- 7.4.0 <= FortiOS <= 7.4.10  
  
- 7.2.0 <= FortiOS <= 7.2.12  
  
- 7.0.0 <= FortiOS <= 7.0.18  
  
- 7.6.0 <= FortiProxy <= 7.6.4  
  
- 7.4.0 <= FortiProxy <= 7.4.12  
  
- FortiProxy 7.2  
  
- FortiProxy 7.0  
  
**0x05****POC状态**  
- 未公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.fortinet.com/  
  
  
  
