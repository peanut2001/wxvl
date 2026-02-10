#  【已复现】微信Linux版本存在1click远程代码执行漏洞  
安恒研究院
                    安恒研究院  安恒信息CERT   2026-02-10 11:24  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/JAzzLj4nXevmL5H6C1I6nWLYOHeic25ZZq3Sju5Xs1LnOckux8PBqG1qYrBly0Nicx4verjADnLorl5g1ImeuTeg/640?wx_fmt=jpeg&from=appmsg&wx_&wx_#imgIndex=0 "")  
  
<table><tbody><tr style="-webkit-tap-highlight-color:transparent;"><td colspan="4" data-colwidth="100.0000%" width="100.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;background-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;color:rgb(255, 255, 255);box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:center;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">漏洞概述</span></strong></p></section></section></td></tr><tr style="-webkit-tap-highlight-color:transparent;"><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">漏洞名称</span></strong></p></section></section></td><td colspan="3" data-colwidth="75.0000%" width="75.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p><span style="letter-spacing:0.544px;"><span leaf="">微信Linux版本存在1click远程代码执行漏洞</span></span></p></section></section></td></tr><tr style="-webkit-tap-highlight-color:transparent;"><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">CVE编号</span></strong></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><span style="font-size:14px;letter-spacing:0.544px;line-height:22.4px;"><span leaf="">未分配</span></span><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;overflow:hidden;line-height:0;box-sizing:border-box;"><span leaf="" style="-webkit-tap-highlight-color:transparent;"><br/></span></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">CNVD编号</span></strong></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><span leaf="" style="-webkit-tap-highlight-color:transparent;">未分配</span></p></section></section></td></tr><tr style="-webkit-tap-highlight-color:transparent;"><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">CNNVD编号</span></strong></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><span leaf="">未分配</span></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">安恒CERT编号</span></strong></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><span leaf="">WM-202602-000002</span></section></section></td></tr><tr style="-webkit-tap-highlight-color:transparent;"><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">POC情况</span></strong></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;"><span leaf="" style="-webkit-tap-highlight-color:transparent;">已发现</span></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">EXP情况</span></strong></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;"><span leaf="" style="-webkit-tap-highlight-color:transparent;">已发现</span></p></section></section></td></tr><tr style="-webkit-tap-highlight-color:transparent;"><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">在野利用</span></strong></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;"><span leaf="" style="-webkit-tap-highlight-color:transparent;">未发现</span></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">研究情况</span></strong></p></section></section></td><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;"><span leaf="" style="-webkit-tap-highlight-color:transparent;">已复现</span></p></section></section></td></tr><tr style="-webkit-tap-highlight-color:transparent;"><td data-colwidth="25.0000%" width="25.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;box-sizing:border-box;"><p style="-webkit-tap-highlight-color:transparent;text-align:left;"><strong style="-webkit-tap-highlight-color:transparent;"><span leaf="">危害描述</span></strong></p></section></section></td><td colspan="3" data-colwidth="75.0000%" width="75.0000%" style="-webkit-tap-highlight-color:transparent;word-break:break-all;hyphens:auto;border-color:#4577da;"><section style="-webkit-tap-highlight-color:transparent;margin:5px 0px;"><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;overflow:hidden;line-height:0;box-sizing:border-box;"><span leaf="" style="-webkit-tap-highlight-color:transparent;"><br/></span></section><p><span style="font-size:14px;letter-spacing:0.544px;"><span leaf="">微信Linux版本存在1click远程代码执行漏洞，用户在微信中接收到包含恶意命令文件名的文件，下载并打开会导致远程代码执行。</span></span></p><section style="-webkit-tap-highlight-color:transparent;margin-top:0px;margin-right:0px;margin-bottom:unset;margin-left:0px;padding:0px 5px;font-size:14px;overflow:hidden;line-height:0;box-sizing:border-box;"><span leaf=""><br/></span></section></section></td></tr></tbody></table>  
  
**该产品主要使用客户行业分布广泛，漏洞危害性极高，建议客户尽快做好自查及防护。**  
  
**安恒研究院卫兵实验室已复现此漏洞。**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/P5dz00jGoyRUrJ0ocEWcicdw22SJ1HmvH0Yu4ByoGWjYg738Bg1ic2jWCHCHzhcdw5vibRicCOfotlwSIFY9gJJ7iaFEPPMfAiaxNPCSGIYZtDmdk/640?wx_fmt=jpeg "")  
  
复现截图  
  
  
  
**漏洞信息**  
  
  
  
  
微信Linux版，一款跨平台的通讯工具。支持单人、多人参与。通过网络发送语音、图片、视频和文字。  
  
  
**漏洞描述**  
  
**漏洞危害等级：**  
严重  
  
**漏洞类型：**  
远程代码执行  
  
  
**影响范围**  
  
**影响版本：**  
  
微信Linux版 <= 4.1.0.13  
  
  
  
  
  
**修复方案**  
  
  
  
  
**官方修复方案：**  
  
微信Linux版官方尚未发布针对该问题的修复版本。建议用户密切关注微信官方渠道的版本更新通知，并及时升级至安全版本。在此期间，请注意防范风险，避免打开文件名中包含异常特殊字符、命名可疑或来源不明的文件，以保护设备与个人信息安全。  
  
https://linux.weixin.qq.com  
  
  
  
**参考资料**  
  
  
  
  
  
https://linux.weixin.qq.com  
  
  
  
  
  
**技术支持**  
  
  
  
  
如有漏洞相关需求支持请联系400-6059-110获取相关能力支撑。  
  
  
