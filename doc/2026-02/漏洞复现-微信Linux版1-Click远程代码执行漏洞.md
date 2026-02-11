#  漏洞复现-微信Linux版1-Click远程代码执行漏洞  
 松杨网络安全资料库   2026-02-11 01:09  
  
漏洞概述：  
  
微信Linux版本存在1click远程代码执行漏洞，用户在微信中接收到包含恶意命令文件名的文件，下载并打开会导致远程代码执行。该产品主要使用客户行业分布广泛，漏洞危害性极高，建议客户尽快做好自查及防护。  
  
漏洞影响版本：  
  
微信Linux<=4.1.0.13  
  
复现截图及过程如下：  
  
发送文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2xCpgJcagf8BYx0rhPNwibCicMFiawXVmQ3KqvFOfgGyvk7uic4u4cvjcTOtiaowg661OkicOJEPsdYRWFdfOuH9qgkE5wy1Wwm5K9NCXzUxN275k/640?wx_fmt=png&from=appmsg "")  
  
点击文件后效果  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2xCpgJcagf8DhmkGT1Feufb2icrE1VicWDhvDv4ktGF8d6kLA9Ygf9H6icWhMes1mEC0uF2IqjnwfdODbQPWiageQxHAsS2oSPTzywASQ6Uib3hg/640?wx_fmt=png&from=appmsg "")  
  
修复方案：  
  
微信Linux版官方尚未发布针对该问题的修复版本。建议用户密切关注微信官方渠道的版本更新通知，并及时升级至安全版本。在此期间，请注意防范风险，避免打开文件名中包含异常特殊字符、命名可疑或来源不明的文件，以保护设备与个人信息安全。  
  
微信官方linux版本下载链接：  
  
https://linux.weixin.qq.com  
  
