#  【复现】泛微 E-cology10 远程代码执行漏洞风险通告  
 赛博昆仑CERT   2026-03-16 09:17  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/iaZ7t7b9Dodvib7ddpGMC6vx4COAy4sBoGbGCkwVUIJSHBPI0z1Utrp1h5ys6ygT3albl3PgjejJcRRRiaDFFbMBA/640?wx_fmt=gif "")  
  
  
-  
赛博昆仑漏洞  
安全风险通告  
-  
  
泛微 E-cology10 远程代码执行漏洞风险通告  
  
![](https://mmbiz.qpic.cn/mmbiz_svg/7j1UQofaR9fsNXgsOXHVKZMJ1PCicm8s4RHQVjCJEjX63AsNibMx3So4wSMAvubEOoU2vLqYY7hIibIJbkEaPIDs5A4ianh5jibxw/640?wx_fmt=svg "")  
  
  
  
  
**漏洞描****述**  
  
    泛微Ecology是由上海泛微网络科技股份有限公司开发的一套企业级协同管理与办公自动化(OA)平台，其中Ecology10是其新一代协同管理平台产品，广泛应用于政府机关、企事业单位等场景，用于流程审批、知识管理、门户建设及移动办公等业务。  
          
  
   近日，赛博昆仑CERT监测Ecology10存在远程代码执行漏洞。未经过身份的攻击者可以利用该漏洞在Ecology10服务器上执行任意代码，获取系统权限，窃取或篡改业务数据，进一步控制整个OA平台，严重威胁企业核心业务安全  
。  
<table><tbody><tr style="height:39px;"><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;word-break: break-all;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">漏洞名称</span></strong></span></p></td><td colspan="3" data-colwidth="144,144,144"><section><span leaf="" style="color: rgb(0, 122, 170);"><span textstyle="" style="font-size: 14px;">泛微 E-cology10 远程代码执行漏洞</span></span></section></td></tr><tr style="height:39px;"><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">漏洞公开编号</span></strong></span></p></td><td colspan="3" data-colwidth="144,144,144"><p><span leaf="" style="color: rgb(0, 122, 170);"><span textstyle="" style="font-size: 14px;">暂无</span></span></p></td></tr><tr style="height:39px;"><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">昆仑漏洞库编号</span></strong></span></p></td><td colspan="3" data-colwidth="144,144,144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><span leaf="">CYKL-2026-031151</span></span></p></td></tr><tr style="height:39px;"><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">漏洞类型</span></strong></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><span leaf="">代码执行</span><span leaf=""><br/></span></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">公开时间</span></strong></span></p></td><td data-colwidth="144" width="144"><p><span leaf="" style="color: rgb(0, 122, 170);"><span textstyle="" style="font-size: 14px;">2026-3-12</span></span></p></td></tr><tr style="height:39px;"><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">漏洞等级</span></strong></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><span leaf="">高危</span></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">评分</span></strong></span></p></td><td data-colwidth="144" width="144"><p><span leaf="" style="color: rgb(0, 122, 170);"><span textstyle="" style="font-size: 14px;">9</span></span><span leaf="" style="color: rgb(0, 122, 170);"><span textstyle="" style="font-size: 14px;">.8</span></span></p></td></tr><tr style="height:39px;"><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">漏洞所需权限</span></strong></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><span leaf="">无权限要求</span></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">漏洞利用难度</span></strong></span></p></td><td data-colwidth="144" width="144"><p><span leaf="" style="color: rgb(0, 122, 170);"><span textstyle="" style="font-size: 14px;">低</span></span></p></td></tr><tr style="height:39px;"><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">PoC</span></strong><strong><span leaf="">状态</span></strong></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><span leaf="">未知</span></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">EXP</span></strong><strong><span leaf="">状态</span></strong></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><span leaf="">未知</span></span></p></td></tr><tr style="height:39px;"><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">漏洞细节</span></strong></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><span leaf="">未知</span></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><strong><span leaf="">在野利用</span></strong></span></p></td><td data-colwidth="144" width="144" style="font-size: 10pt;text-align: left;"><p><span style="color: rgb(0, 122, 170);"><span leaf="">未知</span></span></p></td></tr></tbody></table>  
  
**影响范围**  
  
泛微  
 Ecology10  
   
< v20260312安全补丁之前的版本  
  
  
**漏洞复现**  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/n8iag6r4WbSbrwZtO7rOIk6gaSNp8kZXfo9JsRpKsb479aSZmygFrJA2gYoGic6ZKjclFBwk9MbZNMHfUxuNdJltfibWjfpvM6UPvt8HWrw7qE/640?wx_fmt=png&from=appmsg "")  
  
  
****  
**防护措施**  
- **修复建议**  
  
目前，官方已发布修复建议，建议受影响的用户尽快联系厂商下载更新补丁。  
  
- **技术业务咨询**  
  
  
  
赛博昆仑支持对用户提供轻量级的检测规则或热补方式，可提供定制化服务适配多种产品及规则，帮助用户进行漏洞检测和修复。  
  
赛博昆仑CERT已开启年订阅服务，付费客户(可申请试用)将获取更多技术详情，并支持适配客户的需求。  
  
联系邮箱：  
cert@cyberkl.com  
  
公众号：赛博昆仑CERT  
  
  
****  
**时间线**  
  
    2026年3月12日，官方发布补丁  
  
    2026年3月16日，赛博昆仑CERT发布漏洞风险通告  
  
  
**技术业务咨询**  
  
邮箱：cert@cyberkl.com  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/iaZ7t7b9Dodvib7ddpGMC6vx4COAy4sBoGLJ1DKwHPSc2JX7FQat3De8XiaajuAHkJzOY9ic9bnaHiaLJqVHIe0E2wg/640?wx_fmt=gif "")  
  
  
  
  
  
  
  
  
  
  
  
  
