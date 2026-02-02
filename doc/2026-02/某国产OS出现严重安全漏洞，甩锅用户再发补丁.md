#  某国产OS出现严重安全漏洞，甩锅用户再发补丁  
原创 安全透视镜
                    安全透视镜  网络安全透视镜   2026-02-02 01:20  
  
![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS7YafeBGloytAJNxzDmkpmF9QCyReUxCNIoQQTRerbRAkQ4ZcWNX1FW6Pt4Y03Jlu5fNq3KeT2pcQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS7YafeBGloytAJNxzDmkpmFcicHTVRalOxq9Kq6MQjfMBberVqVEZkjic0V3lrH51wFQkFFbdyqK2Mg/640?wx_fmt=png&from=appmsg "")  
- 未登录的情况下可以直接历遍目录：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS7YafeBGloytAJNxzDmkpmFPu9UuruzegMosxwsCWu69wESmfVrvD1I9UPzFiaBrRr7sOHcSYqhUPA/640?wx_fmt=png&from=appmsg "")  
  
  
官方人员也并未做出预警，而是一句 “别走 http 明文方式访问设备” 轻描淡写带过（说是最新版本 v1.1.15 已经修复）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS7YafeBGloytAJNxzDmkpmFyx1o1nYuE5dv25qkLmRXSiaoNbzne03noVrMHQbzw7YIs5iaIQeeUyTA/640?wx_fmt=png&from=appmsg "")  
  
虽然官方说最新版本 v1.1.15 已经修复了历遍问题，但部分已受影响的用户，依然存在严重问题：  
- 异常的连接数：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS7YafeBGloytAJNxzDmkpmFauK0gdJGeD6dylibWrnfSlXlJ9QDDWkgs9uZdkcOfSCsICSJq8TAOkQ/640?wx_fmt=png&from=appmsg "")  
  
网传POC  
  
![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS7YafeBGloytAJNxzDmkpmFxBx4cViaWX3kEIXVw8WQjKKXalnAoFq4YWdykWPuvvj9bSS0Vvn1hnQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
