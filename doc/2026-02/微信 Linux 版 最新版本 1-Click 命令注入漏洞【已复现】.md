#  微信 Linux 版 最新版本 1-Click 命令注入漏洞【已复现】  
 湘安无事   2026-02-10 09:40  
  
01前言  
  
近日，看到有人发布这样的内容：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dwgmcibbDO5JAxzQg1Zb7Ysgk1z8aYibQeibic5gcfQ36vDMicic8YOiaI2LicBeSJYSwiaVkv6Sw49gEMlpLU2d1GB1cicOEOKibZc8ugJbTiaBtdrLiaa8/640?wx_fmt=png&from=appmsg "")  
  
02 漏洞描述  
  
其实就是程序在处理接收文件时，未对文件名中的特殊字符进行充分校验与过滤，攻击者可构造包含恶意命令的文件名并发送给目标用户。当受害者点击该文件后，程序在后续处理过程中触发命令注入，从而在受害者系统中执行任意命令。  
  
用人话讲就是  
微信 linux版本存在1click rce，只需要将文件名使用反引号包裹命令，目标点击文件即可执行。（引用某公众号的原话）  
  
03 漏洞复现  
  
文件名字可以弄长一点这样就可以不易发现下面我的名字就是（我以弹出计算器简单为例简单复现）：  
  
`中国工业软件行业发展研究报告：慢行业下需坚守长期主义之路-艾瑞咨询;kcalc`.txt  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dwgmcibbDO5JViak0VJbIAXVDwCd1ia0DvpguicLXGCXvPIePdiat9b4DCLCQdIMNCzwQd6U9C5PVMxCic2O2pn2cIH1O9aw3k8rKPib47uMLggIxQ/640?wx_fmt=png&from=appmsg "")  
  
04 修复建议  
  
 •  避免点击或打开文件名中包含异常特殊字符或可疑内容的文件。  
  
 •  临时使用微信网页版（https://web.wechat.com/）。  
  
  
 • 暂时不使用用微信liunx版本  
  
  
  
  
  
