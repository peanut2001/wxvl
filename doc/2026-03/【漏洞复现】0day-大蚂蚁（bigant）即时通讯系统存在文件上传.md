#  【漏洞复现】0day-大蚂蚁（bigant）即时通讯系统存在文件上传  
什么安全
                    什么安全  什么安全   2026-03-11 07:25  
  
  请勿利用  
文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接  
或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。本次测试仅供学习使用，如若非法他用，与平台和本文作者无关，需自行负责  
！    
## 产品描述  
  
  大蚂蚁即时  
通讯系统是一款企业办公  
通讯软件，通过本地化服务器部署为政企单位提供安全可控的协同办公服务。  
## 漏洞描述  
  
  
  
   
   
未经身份验证的远程攻击者通过未授权接口上传恶意文件可以  
执行恶意代码，实现服务器的远程控制。  
## Poc  
  
```
GET 未公开
```  
  
## 漏洞复现  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/XY4NEU6nZJBLSicGmkKNtMc5iah6GFicicDiax0OoT2pZbteWGj43BicPHCrolqeAae7ahBy3DMibI6W7rsVxAriaKdAJDhEKrdWqogwAdHJnTv4ydU/640?wx_fmt=png&from=appmsg "")  
  
  
小  
知  
识  
  
  
  
  
**依据《刑法》第285条第3款的规定，犯提供非法侵入或者控制计算机信息罪的，处3年以下有期徒刑或者****拘役****，并处或者单处****罚金****;情节特别严重的，处3年以上7年以下有期徒刑，并处罚金。**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/Gn0JbCnxttRbj4Mib3fcSfwr0tP4UxXtjf47HFwaZcgwWStzGNLNMlGKQJz902fHTT8PCfOwHedLqarXh0eC9KQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1 "")  
  
声  
明  
  
  
  
**本文提供的技术参数仅供学习或运维人员对内部系统进行测试提供参考，未经授权请勿用本文提供的技术进行破坏性测试，利用此文提供的信息造成的直接或间接损失，由使用者承担。**  
  
  
