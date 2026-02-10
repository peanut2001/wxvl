#  【附POC及复现环境】Linux版微信 1-click任意命令执行漏洞复现  
原创 a1batr0ss
                    a1batr0ss  天翁安全   2026-02-10 09:05  
  
**免责声明：**  
本公众号所发布的全部内容，包括但不限于技术文章、POC脚本、漏洞利用工具及相关测试环境，均仅限于合法的网络安全学习、研究和教学用途。所有人在使用上述内容时，应严格遵守中华人民共和国相关法律法规以及道德伦理要求。未经明确的官方书面授权，严禁将公众号内的任何内容用于未经授权的渗透测试、漏洞利用或攻击行为。 所有人仅可在自己合法拥有或管理的系统环境中进行本地漏洞复现与安全测试，或用于具有明确授权的合法渗透测试项目。所有人不得以任何形式利用公众号内提供的内容从事非法、侵权或其他不当活动。 如因违反上述规定或不当使用本公众号提供的任何内容，造成的一切法律责任、经济损失、纠纷及其他任何形式的不利后果，均由相关成员自行承担，与本公众号无任何关联。  
## 不错过最新的漏洞POC  
  
为保证您可以在第一时间接收到本公众号分享的**漏洞复现及POC**  
信息，建议您在公众号“天翁安全”主页界面将“天翁安全”设为**星标**  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xDGMcPEtbiaibn0KTwElo7LyJAgMEZHNdhXRsGib9bh9yXMfXQAmJD5RyZsTDf3S3akZAicLjgyAkWOvhJmXgVGY6XY8a0dPojYNfoh4DAY35ZQ/640?wx_fmt=png&from=appmsg "")  
## 漏洞介绍  
  
该漏洞源于微信 Linux 客户端在处理文件名时缺乏严格的合法性校验与转义机制，攻击者可构造包含恶意命令的特制文件名并诱导用户打开，从而在客户端解析文件名过程中触发命令注入，最终导致任意命令执行并获取系统权限。  
  
**该漏洞需要1-click，且只存在于Linux版的微信中。**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xDGMcPEtbiaibevYomeLNSkNyiakAOpH5sibCtAZYNgudqcRRem0kDYsQQ9aarLkf33YMghqu1XmG4oS6WKtIyttd9ZaYgtNPZnHSoPGXY5smj8/640?wx_fmt=png&from=appmsg "")  
## 漏洞影响版本  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;margin: 0px;padding: 0.5rem 1rem;font-style: normal;font-weight: bold;text-align: left;border: 1px solid rgb(233, 235, 236);"><section><span leaf="">产品版本</span></section></th><th style="box-sizing: border-box;margin: 0px;padding: 0.5rem 1rem;font-style: normal;font-weight: bold;text-align: left;border: 1px solid rgb(233, 235, 236);"><section><span leaf="">版本</span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;margin: 0px;padding: 0.5rem 1rem;border: 1px solid rgb(233, 235, 236);"><section><span leaf="">微信 Linux 版</span></section></td><td style="box-sizing: border-box;margin: 0px;padding: 0.5rem 1rem;border: 1px solid rgb(233, 235, 236);"><section><span leaf="">截止发稿前最新版本（4.1.0.13）也存在该漏洞</span></section></td></tr></tbody></table>## 环境部署  
  
这里以Ubuntu环境为例，执行以下命令安装微信Linux版（4.1.0.13）  
```
sudo apt install ./WeChatLinux_x86_64.deb
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xDGMcPEtbiaibnKdwx0HnXycD6Cx68T8IJ16JNZDV93Dn7mowSVzBGNWJHQBSEouJk3rssOYxET52LcibMkoJ7Jf46buz1pHudBc9eibgD8N99Q/640?wx_fmt=png&from=appmsg "")  
## 漏洞复现  
  
攻击者构造包含反引号、 $()  
等的文件名发送给受害者，受害者点击后即可出发命令执行（这里执行kcalc命令打开计算器做漏洞验证）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/xDGMcPEtbia9hIfNX1aBfiaOeG1pwAO9zdtfKr8dCVkp11ECkiaXFqgczwwXsffBRhph69VKYppUkT4UxBgfF9ic5b1sH9mUibKM6Sg31qTHqvfI/640?wx_fmt=png&from=appmsg "")  
## 知识星球  
  
**“微信Linux版命令执行漏洞POC”、“Wechat Linux版4.1.0.13环境”、“微信Linux版RCE漏洞复现”**  
现已全部发布至知识星球，大家可在知识星球内获取，自行学习复现。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xDGMcPEtbiaibAdO1x0mvwm9WtRLicG5tbicKmhnzGBviaO66gJf4r4gtybT2rWuicfHmp9Q4xsh80VTDU6nDWsx7Y02iaChxIy5ncV59lQDe0oheg/640?wx_fmt=png&from=appmsg "")  
> 星球加入方式见文章底部二维码，欢迎加入交流和学习  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/xDGMcPEtbiaibMQxLFCydvMtReDSiaVGGoTdsggMg3haQpMibfSag6L2E2MoG615qL3T3x0EiceORSDRYFtkU4XdFticQKEn0CmibWM6aHJaPchicLE/640?wx_fmt=png&from=appmsg "")  
  
