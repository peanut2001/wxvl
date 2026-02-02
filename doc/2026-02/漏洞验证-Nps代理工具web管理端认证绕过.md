#  漏洞验证-Nps代理工具web管理端认证绕过  
Domren
                    Domren  网安智界   2026-02-02 07:06  
  
一、漏洞描述  
  
nps是一款轻量级、高性能、功能强大的内网穿透代理服务器。目前支持tcp、udp流量转发，可支持任何tcp、udp上层协议，此外还支持内网http代理、内网socks5代理、p2p等，并带有功能强大的web管理端。Nps web管理端存在认证绕过漏洞，攻击者可任意添加代理，影响内网。  
  
二、验证POC  
  
https://github.com/Domren/POC/  
  
找了一圈，找不到，用DeepSeek写了一个POC和EXP，不过EXP有点问题，也能将就用，有能修改的大佬可以在评论区评论，或者在github 上评论，争取把这个EXP完善一下。  
  
这个验证POC太长了，就只能放这个github地址了。  
  
三、验证截图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/4GMSIbPibVJibpZJP6M1q8HD9wfic2CxlYpPPTvQRLe130UOlsmq0hBd7g9teTXWUuceSTpnuhUZq3uf3kotzaWicg/640?wx_fmt=png&from=appmsg "")  
  
  
四、整改建议  
  
去除配置文件中auth_key注释并设置随机值，同时注释掉auth_crypt_key  
  
