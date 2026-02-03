#  漏洞预警 | 飞牛-私有云fnOS文件读取漏洞  
永恒之锋实验室
                    永恒之锋实验室  Eonian Sharp   2026-02-03 07:38  
  
## fnOS-myapp-file  
### 漏洞介绍  
  
飞牛私有云fnOS是一款基于Debian Linux内核深度开发的国产、正版免费NAS操作系统。因其免费和程序资源丰富，吸引了很多的用户。fnOS出现严重  
0day漏洞  
，可以访问nas上任意文件（包括系统配置文件，用户存储文件）。  
### 漏洞原理  
  
该漏洞源于app-center-static接口（用于提供应用静态资源），后端处理参数时仅做简单字符串拼接，未校验路径跳转符，攻击者构造特殊请求即可遍历全目录读取核心配置及用户数据，特定条件下还可演变为远程命令执行（RCE），实现对设备的完全控制。该漏洞拥有无需认证、无需交互、无明显异常提示的特征，具备隐蔽性强、破坏力大的漏洞特征。鉴于目前PoC已在互联网公开传播，并已发现在野利用，建议尽快安排处置。  
### 影响版本  
```
/ -
```  
### 修复建议  
  
在 NAS 设备开放公网访问权限时，优先采用安全访问方式（加密隧道 /2FA 验证 / 开启防火墙等），以进一步降低潜在安全风险。  
### ES::Portscan 批量验证  
  
espscan可进行端口扫描后批量验证该漏洞。 快速帮助企业排查风险问题。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hvMQKkLOqzOOIsdj1GyAmub4C3IKykdFCD3n6deTE13LxTiaxrOhMibwVl5x1KeG4Jav8SNlL1qGswQVEYlJqMpQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hvMQKkLOqzOOIsdj1GyAmub4C3IKykdFs3CfY0Ttsbyfohuiagq2PFtzW7BU6libmkLCTu2xN89YGpsaCWMjMP9g/640?wx_fmt=png&from=appmsg "")  
  
  
