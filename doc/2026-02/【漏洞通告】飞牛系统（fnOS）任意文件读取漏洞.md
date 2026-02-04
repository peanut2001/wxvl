#  【漏洞通告】飞牛系统（fnOS）任意文件读取漏洞  
原创 常行安服团队
                    常行安服团队  常行科技   2026-02-04 07:50  
  
    
  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/r8QjvJibulhRSzNZThCkQV1T2Fqy9a7EqkOROzD9uCia1RYiclgVHpdbuEypJDffRibFh1FQnpkuPQ7SC7yUf4bemw/640?wx_fmt=png&from=appmsg "")  
  
飞牛私有云（fnOS）是一款基于Linux内核（Debian发行版）深度开发的国产免费NAS系统,飞牛系统FnOS下app-center-static接口存在导致任意文件读取漏洞。  
  
  
  
  
  
<table><tbody><tr style="outline: 0px;visibility: visible;"><td colspan="4" data-colwidth="78,0,0,0" valign="middle" align="center" style="outline: 0px;word-break: break-all;hyphens: auto;background: rgb(70, 118, 217);visibility: visible;"><p style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 14px;color: rgb(255, 255, 255);visibility: visible;"><span leaf="">漏洞概述</span></span><span style="outline: 0px;font-size: 16px;color: white;font-family: 宋体;visibility: visible;"></span></p></td></tr><tr style="outline: 0px;visibility: visible;"><td data-colwidth="78" width="76.33333333333333" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><p style="outline: 0px;text-align: left;line-height: 16px;visibility: visible;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">漏洞名称</span></span></strong></p></td><td colspan="3" data-colwidth="461.3333333333333" width="461.3333333333333" style="border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;text-align: left;font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;text-wrap: wrap;background-color: rgb(255, 255, 255);"><section><span leaf="" style="color:rgb(0, 0, 0);font-size:13px;letter-spacing:1px;text-decoration:rgb(0, 0, 0);background-color:rgb(255, 255, 255);font-family:system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;">飞牛系统（fnOS）任意文件读取漏洞</span></section></td></tr><tr style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;text-align: left;font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;text-wrap: wrap;background-color: rgb(255, 255, 255);"><td data-colwidth="78" style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;text-align: left;font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;text-wrap: wrap;background-color: rgb(255, 255, 255);"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">漏洞编号</span></span></strong></td><td colspan="3"><p style="font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;text-wrap: wrap;background-color: rgb(255, 255, 255);outline: 0px;visibility: visible;"><span leaf="" style="color: rgb(0, 0, 0);font-size: 13px;letter-spacing: 1px;text-decoration: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;">暂无</span></p></td></tr><tr style="outline: 0px;text-align: left;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><td data-colwidth="78" width="109.33333333333333" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">公开时间</span></span></strong></p></td><td data-colwidth="164.33333333333334" width="164.33333333333334" style="border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;line-height: 16px;visibility: visible;"><span style="color: black;font-size: 13px;letter-spacing: 1px;"><span leaf="">2026-01-31</span></span></p></td><td data-colwidth="102.33333333333333" width="102.33333333333333" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">影响量级</span></span></strong></p></td><td data-colwidth="155.33333333333334" width="155.33333333333334" style="border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;line-height: 16px;visibility: visible;"><span style="outline: 0px;color: black;font-size: 13px;letter-spacing: 1px;text-decoration-style: solid;text-decoration-color: rgb(0, 0, 0);visibility: visible;"><span leaf="">万级</span></span></p></td></tr><tr style="outline: 0px;text-align: left;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><td data-colwidth="78" width="78" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">风险评级</span></span></strong></p></td><td data-colwidth="164.33333333333334" width="164.33333333333334" style="border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;color: red;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">高危</span></span></strong></p></td><td data-colwidth="107.33333333333333" width="107.33333333333333" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">CVSS 3.1分数</span></span></strong></p></td><td data-colwidth="155.33333333333334" width="155.33333333333334"><p style="font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;text-wrap: wrap;background-color: rgb(255, 255, 255);outline: 0px;visibility: visible;"><strong><span leaf="" style="color: rgb(0, 0, 0);font-size: 13px;letter-spacing: 1px;text-decoration: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;"><span textstyle="" style="font-weight: normal;">暂无</span></span></strong></p></td></tr><tr style="outline: 0px;text-align: left;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><td data-colwidth="78" width="78" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">威胁类型</span></span></strong></p></td><td data-colwidth="164.33333333333334" width="164.33333333333334"><p style="font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;text-wrap: wrap;background-color: rgb(255, 255, 255);outline: 0px;visibility: visible;"><span leaf="" style="color: rgb(0, 0, 0);font-size: 13px;letter-spacing: 1px;text-decoration: rgb(0, 0, 0);background-color: rgb(255, 255, 255);font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;">任意文件读取</span></p></td><td data-colwidth="107.33333333333333" width="107.33333333333333" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">利用可能性</span></span></strong></p></td><td data-colwidth="155.33333333333334" width="155.33333333333334" style="border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;line-height: 16px;visibility: visible;"><span style="color: rgb(255, 0, 0);"><strong><span style="color: rgb(255, 0, 0);outline: 0px;font-size: 13px;letter-spacing: 1px;text-decoration-style: solid;text-decoration-color: rgb(0, 0, 0);visibility: visible;"><span leaf="">高</span></span></strong></span></p></td></tr><tr style="outline: 0px;text-align: left;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><td data-colwidth="78" width="78" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">POC状态</span></span></strong></p></td><td data-colwidth="164.33333333333334" width="164.33333333333334" style="border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><strong style="outline: 0px;letter-spacing: 0.578px;visibility: visible;"><span style="outline: 0px;color: red;visibility: visible;"><span leaf="">已公开</span></span></strong></span></p></td><td data-colwidth="107.33333333333333" width="107.33333333333333" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">在野利用状态</span></span></strong></p></td><td data-colwidth="155.33333333333334" width="155.33333333333334" style="border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;line-height: 16px;visibility: visible;"><span style="outline: 0px;color: black;font-size: 13px;letter-spacing: 1px;text-decoration-style: solid;text-decoration-color: rgb(0, 0, 0);visibility: visible;"><span leaf="">暂未发现</span></span></p></td></tr><tr style="outline: 0px;text-align: left;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><td data-colwidth="78" width="78" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">EXP状态</span></span></strong></p></td><td data-colwidth="164.33333333333334" width="164.33333333333334"><p style="font-family: system-ui, -apple-system, &#34;system-ui&#34;, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;text-wrap: wrap;background-color: rgb(255, 255, 255);outline: 0px;line-height: 16px;visibility: visible;"><strong><span leaf="" style="font-size: 13px;font-family: 微软雅黑, sans-serif;font-weight: bold;letter-spacing: 0.578px;outline: 0px;color: red;visibility: visible;">已公开</span></strong></p></td><td data-colwidth="107.33333333333333" width="107.33333333333333" style="border-top-width: initial;border-top-style: none;outline: 0px;word-break: break-all;hyphens: auto;line-height: 16px;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;word-break: break-all;hyphens: auto;border-top-width: initial;border-top-style: none;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">技术细节状态</span></span></strong></p></td><td data-colwidth="155.33333333333334" width="155.33333333333334" style="border-top-width: initial;border-top-style: none;border-left-width: initial;border-left-style: none;outline: 0px;word-break: break-all;hyphens: auto;visibility: visible;"><p style="outline: 0px;line-height: 16px;visibility: visible;"><strong style="outline: 0px;visibility: visible;"><span style="outline: 0px;font-size: 13px;color: red;font-family: 微软雅黑, sans-serif;visibility: visible;"><span leaf="">已公开</span></span></strong></p></td></tr></tbody></table>  
  
**漏洞详情**  
  
   
Vulnerability Details  
   
  
  
  
**0x00**  
  
- **漏洞描述**  
  
  
飞牛系统（fnOS）是一款国产网络附加存储（NAS）操作系统。飞牛系统（fnOS）适合追求功能丰富、预算有限且对数据安全要求不高的用户，尤其适合闲置硬件改造和影视娱乐场景。攻击者通过构造恶意请求，利用路径遍历字符（如../）绕过系统路径限制，直接访问服务器文件系统中的任意文件。攻击者可尝试读取服务器上的/etc/passwd文件，若漏洞存在，服务器将返回文件内容  
。  
  
  
  
**受影响范围**  
  
   
Affected Version  
   
  
  
  
**0x01**  
  
版本1.1.15以下  
  
  
**修复方案**  
  
   
Solutions  
   
  
  
  
**0x02**  
  
  
  
- **解决方案**  
  
**1、立即升级至安全版本：**  
  
目前官方回应在x86版本的1.1.15版本已修复，请及时更新至最新版本  
  
**2、临时缓解措施：**  
  
在 NAS 设备开放公网访问权限时，优先采用安全访问方式（加密隧道 /2FA 验证 / 开启防火墙等），以进一步降低潜在安全风险  
  
  
**漏洞复现/验证**  
  
   
Reproduction  
   
  
  
  
**0x03**  
  
常行安服团队已成功复现  
飞牛系统（fnOS）任意文件读取漏洞  
，截图如下：  
  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/r8QjvJibulhRSzNZThCkQV1T2Fqy9a7EqLAK8qPhnsfN2OJ0aviaDDvKAhicljibvSBicGD5YsYG7lUjyZxKazGdLow/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5ibqUx1JicPMtpzBF9mpibjVeab8S0LPppgyJS90BEuqdO07WNt8kmenK1FGaoVBxTSgibfLdUL4SLKy7DCsaYdxxQ/640?wx_fmt=png "")  
  
**the end**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5ibqUx1JicPMtpzBF9mpibjVeab8S0LPppgQDn95A8w6k7yF4nOjPR3icYcLzQnF22HZl8g3o5VLvKMQJEo4gPS7wQ/640?wx_fmt=png "")  
  
  
  
常行科技是一家专注于**网络安全解决方案和运营服务**  
的“专精特新”企业，粤港澳专精特新标杆企业 TOP100，国家级高新技术企业，国家级科技型中小企业，广东省创新型中小企业，立志深耕于网络安全服务领域，是网络安全运营服务**PTM理论**  
的首创者。  
  
自建网络安全攻防实验室“**大圣·攻防实验室(DS-Lab)**  
”，专注于最新的网络攻防技术研究、安全人才培养、客户环境模拟、安全产品研发、应急演练模拟、安全技术培训等。与鹏城实验室深入合作，共建**鹏城靶场常行科技分靶场**  
。大圣·攻防实验室“行者战队”近年来多次参加国内外的实战攻防演练及比赛，并取得优秀战果。  
  
常行科技**三大服务体系、六大场景化解决方案**  
多维度为客户提供最适合自身需求的高性价比网络安全解决方案，**低成本、高质量**  
地帮助客户解决网络和数据安全相关问题。  
  
  
**有常行，更安全**  
  
****  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/r8QjvJibulhT9xicZgBkutnwqozGYfW20cxgUzbMVP117Px3xDtnafDiaeY2ToD2ibicnd3SaQE7qHuCMrL0X2ND0Qg/640?wx_fmt=jpeg "")  
  
常为而不置  
  
常行而不休  
  
了解更多咨询请关注公众号  
  
  
