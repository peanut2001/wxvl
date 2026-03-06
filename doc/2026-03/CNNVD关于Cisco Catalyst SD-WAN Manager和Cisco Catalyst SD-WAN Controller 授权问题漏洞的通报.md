#  CNNVD关于Cisco Catalyst SD-WAN Manager和Cisco Catalyst SD-WAN Controller 授权问题漏洞的通报  
CNNVD
                    CNNVD  CNNVD安全动态   2026-03-06 03:54  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1JjlMnGl5z2XiaAQGZdFulYs0vsE3icB8RUiawPqDSb5lvm8G0drb7iaw7sQ/640?wx_fmt=gif&from=appmsg "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1Js3VkKswpUtkoDWibZ1YQl1lIdcctfqePCcSPEdc38SnhJGdqGJUFx9w/640?wx_fmt=gif&from=appmsg "")  
  
**点击蓝字 关注我们**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1Js3VkKswpUtkoDWibZ1YQl1lIdcctfqePCcSPEdc38SnhJGdqGJUFx9w/640?wx_fmt=gif&from=appmsg "")  
  
  
**漏洞情况**  
  
近日，国家信息安全漏洞库（CNNVD）收到关于Cisco Catalyst SD-WAN Manager和Cisco Catalyst SD-WAN Controller 授权问题漏洞（CNNVD-202602-4275、CVE-2026-20127）情况的报送。未经身份验证的攻击者可通过发送特制数据包，绕过验证机制并获取管理权限。思科产品多个版本均受此漏洞影响。目前，思科官方已发布更新修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。  
  
## 一漏洞介绍  
  
  
Cisco Catalyst SD-WAN Manager（Cisco SD-WAN vManage）和Cisco Catalyst SD-WAN Controller都是美国思科（Cisco）公司的产品。Cisco Catalyst SD-WAN Manager是一个高度可定制的仪表板，可简化和自动化 Cisco SD-WAN 的部署、配置、管理和操作。Cisco Catalyst SD-WAN Controller是一个安全策略控制面板。  
  
该漏洞源于对等身份验证机制存在问题，未经身份验证的攻击者可通过发送特制数据包，绕过验证机制并获取管理权限。  
  
****  
## 二危害影响  
  
  
Cisco Catalyst SD-WAN Manager 20.12.1版及之前版本、Cisco Catalyst SD-WAN Controller 20.12.1版及之前版本均受此漏洞影响。  
  
****  
## 三修复建议  
  
  
目前，思科官方已发布更新修复了该漏洞，建议用户及时确认产品版本，尽快采取修补措施。官方参考链接：  
  
https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa-EHchtZk  
  
本通报由CNNVD技术支撑单位——奇安信网神信息技术（北京）股份有限公司、中国银联股份有限公司、塞讯信息技术（上海）有限公司、北京网御星云信息技术有限公司、江苏骏安安全检测有限公司、信飛科技有限公司、西安秦易信息技术有限公司、广州纬安科技有限公司、北京国信城研科学技术研究院、清远职业技术学院、安徽信科共创信息安全测评有限公司等技术支撑单位提供支持。  
  
CNNVD将继续跟踪上述漏洞的相关情况，及时发布相关信息。如有需要，可与CNNVD联系。联系方式: cnnvd@itsec.gov.cn  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/g1thw9GoocfpeKv1eicF4icEx1vUX4LQ1JMd8aMOqNkic25xydKvYcCVEsHXvm506icfXiaFep4AfohjraUj3F2jMfg/640?wx_fmt=gif&from=appmsg "")  
  
  
