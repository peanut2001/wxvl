#  漏洞预警 | OpenEMR未授权访问漏洞  
浅安
                    浅安  浅安安全   2026-03-12 00:00  
  
**0x00 漏洞编号**  
- # CVE-2026-24898  
  
**0x01 危险等级**  
- 高危  
  
**0x02 漏洞概述**  
  
OpenEMR是一款开源电子病历和医疗信息管理系统，广泛应用于医疗机构的临床管理与患者信息管理。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/7stTqD182SWzl9tcv7CRS9WWlNvEkJibfrom4154jm9XE9zDfibYPe6RC11PXEN6fOjCpF4nyOqU0lO1tzY4ibiaNg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
**0x03 漏洞详情**  
  
**CVE-2026-24898**  
  
**漏洞类型：**  
未授权访问  
  
**影响：**  
获取敏感信息  
  
**简述：**  
OpenEMR MedEx存在未授权访问漏洞，由于library/MedEx/MedEx.php文件中，代码设置$ignoreAuth=true，导致接口在未进行身份认证的情况下即可被外部访问。当攻击者向该接口发送包含任意callback_key参数的POST请求时，系统会自动调用MedEx登录流程，并将完整的登录响应以JSON形式返回，其中包含MedEx API 访问令牌、诊所信息、患者事件及营销活动等敏感数据。攻击者可利用泄露的令牌直接访问MedEx平台API，获取患者相关数据、触发通知或修改事件配置，从而造成敏感医疗信息泄露。  
  
**0x04 影响版本**  
- OpenEMR < 8.0.0  
  
**0x05 POC状态**  
- 已公开  
  
**0x06****修复建议**  
  
**目前官方已发布漏洞修复版本，建议用户升级到安全版本****：**  
  
https://www.open-emr.org/  
  
  
  
