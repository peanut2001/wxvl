#  【红队必备】Shiro漏洞内存马注入与回显探测综合漏洞利用工具  
原创 0xSecDebug
                    0xSecDebug  0xSecDebug   2026-02-11 05:13  
  
# ShiroEXP  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
> **项目地址在文章底部哦**  
  
  
  
Shiro漏洞综合利用工具  
## 环境  
```
JDK 8u431` | `Intellij 2025
```  
> ⚠️ 使用其他JDK版本可能出现未知的错误  
  
## Features  
- 爆破rememberMe  
  
- 漏洞探测(Shiro550、Shiro721)  
  
- 探测回显链  
  
- 探测依赖（FindClassByURLDNS、FindClassByBomb）  
  
- 命令执行  
  
- 注入内存马  
  
- 全局代理  
  
## 工具使用  
### Shiro550  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODwRhSxn4KQ5D8TzMwnrQdUQAjaDsCRHRGG7Q7gIx5vFj20Z7VCGic1On0CiaQQeicZe323dBn8EsPKicSHsgNiavVPblAiaILdk37QCM/640?wx_fmt=png&from=appmsg "")  
### Shiro721  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODyRZUpQXNqZpuP8NOXeRt3PUQRuX635B9m9R06FF2ydYkOj2O1O6SEpbSs2J53nbHcj7hUiaVvkkGHegNuRXJGn3yTpRLRG32XU/640?wx_fmt=png&from=appmsg "")  
### FindClassByURLDNS  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzKuQPM7CEiaWz1iblmefWrJ4jkOxYWJtuEYepGufTgLofT0r6GOMkNEyDNSMiaNCC1q3ela2zEr6Wnib4iaAl9LQkhdib3L7362VZbU/640?wx_fmt=png&from=appmsg "")  
### 自定义探测类  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODzY4rQppF5s6PB528asnnZ44OyIibFxJsxfaK5SAA13bgUf5gUmYe5sEACGy6r7vnmOssSaicXyMMN6qozfCcicPiagwlDHmVib8zCM/640?wx_fmt=png&from=appmsg "")  
### FindClassByBomb  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwCNbVsm7lPWm1YUKF0FQ74ZW9kicBNOVhzoBB9Idib6x3sWClr1lKJKBYkIib8ficWMutQTFa48vrhHiaoLytl6oDElLBHB3gS5PcE/640?wx_fmt=png&from=appmsg "")  
### 命令执行  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODw0IPxjopxeyYyvEEJ2rQCfnbQByKaD9pliacuPtUIx73epQNsiaEvQkjvsPmYl2iaF8tB26ypjU2UXSSFy3Jc5YPAPK2Z2rBJbwU/640?wx_fmt=png&from=appmsg "")  
### 内存马注入  
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyQLlfz0Vz4Rr78qCrPn3gtnwm0mHlq8CDZvqrGEQvURw7IibGByjyHMDwd6aLOb7EvfamFSxUv6hXj0SgZia4HvwEYyffRlib7Jw/640?wx_fmt=png&from=appmsg "")  
### 自定义内存马  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODz7ZvQxY3icEiaicllvRnaqicxSavJvrtVdEc1JMfZZiaFbpzV7IAtJKIzCfVDAddV8QibTRzJuXffW16VJ3rtpyQrsqAGtdyhgSxfxg/640?wx_fmt=png&from=appmsg "")  
## 工具构建  
  
自行编译打jar包时，可能会遇到**找不到或无法加载主类**  
的问题，经排查是因为bcprov包中的签名文件，打包后删除*.DSA、*.SF文件即可   
  
![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODyKrY9N8LK0t4JDlxfR2pNYQaIMrSfsXQqtXTQqxy4mmwDdb1crxDtVmqzX00ftcuYyMlIYc1tQPpBF0nZUzJOP2PVxdhF9dUk/640?wx_fmt=png&from=appmsg "")  
  
📖 项目地址  
```
https://github.com/Y5neKO/ShiroEXP
```  
  
💻 威胁情报推送群  
>   如果师傅们想要第一时间获取到**最新的威胁情报**  
，可以添加下面我创建的  
**钉钉漏洞威胁情报群**  
，便于师傅们可以及时获取最新的  
**IOC**  
。  
>  如果师傅们想要获取  
**网络安全相关知识内容**  
，可以添加下面我创建的  
**网络安全全栈知识库**  
，便于师傅们的学习和使用：  
  
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**  
。  
  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg "")  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg "")  
  
**点分享**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg "")  
  
**点收藏**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg "")  
  
**点在看**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg "")  
  
**点点赞**  
  
