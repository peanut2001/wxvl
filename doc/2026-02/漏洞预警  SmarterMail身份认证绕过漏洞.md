#  漏洞预警 | SmarterMail身份认证绕过漏洞  
浅安
                    浅安  浅安安全   2026-02-02 00:01  
  
**0x00 漏洞编号**  
- # QVD-2026-4572  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
SmarterMail是SmarterTools公司推出的一款基于Windows平台的邮件服务器软件，支持SMTP、POP3、IMAP及WebMail等核心邮件功能，广泛应用于中小企业和自建邮件系统场景。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SWMH7URGvicoyl4Cvkc3uYgLb4moyaeBMugRStF77v5iclpOHl48y0DuxOeAKZ6FXyXm2PnNnlwGQBw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
**0x03 漏洞详情**  
###   
  
**QVD-2026-4572**  
  
**漏洞类型：**  
身份认证绕过****  
  
**影响：**  
重置系统管理员账户密码  
  
  
****  
  
**简述：**  
SmarterMail存在身份认证绕过漏洞，由于系统管理员的密码重置路径未验证OldPassword字段的有效性，仅依赖用户输入的Username和NewPassword即可直接修改系统管理员账户密码。远程攻击者可通过构造特定请求，重置任意已知用户名的系统管理员账户密码，进而执行任意操作系统命令，最终实现远程代码执行。  
  
**0x04 影响版本**  
- SmarterMail < Build 9511  
  
**0x05****POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.smartertools.com/  
  
  
  
