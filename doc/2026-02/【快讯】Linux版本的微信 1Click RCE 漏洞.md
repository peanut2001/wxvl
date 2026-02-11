#  【快讯】Linux版本的微信 1Click RCE 漏洞  
原创 joe1sn
                        joe1sn  不止Sec   2026-02-10 16:54  
  
360已经收录：  
[https://mp.weixin.qq.com/s/HcHuxvYb1sZjFNJNAfyLtA](https://mp.weixin.qq.com/s?__biz=Mzk0ODM3NTU5MA==&mid=2247496292&idx=1&sn=cc7adcbd050bffde0144714aee3243d0&scene=21#wechat_redirect)  
  
  
安装linux wechat  
  
https://linux.weixin.qq.com/en  
```
```  
  
![image-20260211003007299](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuibFFVlDmwusMvFddu7iaxzC5ROIpWYiaSg6N4zDgSeraTibcOrY8adcHHkmc30ibqCibzUFOPfp8PEsicxx6TYpq9B4QoeeU74SLTndQ/640?wx_fmt=png&from=appmsg "")  
  
安装完成后中断输入  
wechat  
打开引用  
# PoC  
  
发送包含特殊字符的文件，双击打开文件即可RCE  
  
![](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuicnRokMzbbbuuS6D8pbIwicgOqD1ZVSPSudnk0NSHeaTkyUicCAFbj0KQtjsAAB5NaBRspWhUIic1ibxrnib79aH4ZhvI6PfeELmbjA/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
