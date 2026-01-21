#  能注入 ≠ 理解漏洞：sqli-labs 第 29 关的真正考点  
原创 武文学网安
                        武文学网安  武文学网安   2026-01-21 18:44  
  
大家好，我是武文。  
今天来挑战 sqli-labs 第 29 关。  
  
第 29 关在官方描述中标注为：GET – Error based – Impedance mismatch – Having a WAF in front of web application  
  
这里的关键词并不是“WAF 本身”，而是 **Impedance Mismatch（解析不一致）**  
。  
  
前面的第28\28a  
关  
与27a关注入方式一致，仅闭合方式变为了单引号+括号，这里就不再重复演示了。让咱们快速进入下一个注入方式学习。  
## 一、现象：普通显错注入可以成功，sqlmap 也能跑通  
### 1.1 手工测试显错注入  
  
直接构造 payload：  
```
?id=1' and updatexml(1,concat(0x7e,database(),0x7e),1)--+

```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHpx0Qico5T8IAicRs5PUPR5hU9vBhcbicJWG8JPtpRm0Tuqkm3JvAakNT6qDMTQzzicrmt9NrLq45byA/640?wx_fmt=png&from=appmsg "")  
  
页面成功报错，并回显数据库名。  
  
这一步给人的直觉是：第 29 关不过是一个普通的显错注入关卡。  
### 1.2 手工测试UNION注入  
  
继续测试 UNION：  
：  
```
?id=-1'union select 1,2,3--+
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHpx0Qico5T8IAicRs5PUPR5h5yHyJibEQ5tiaNLQWPh40zPPBeFpRleaddKI107ZxSGVXt9ZIFyfrQYA/640?wx_fmt=png&from=appmsg "")  
  
发现普通的union注入也能实现。  
### 1.3 使用 sqlmap 测试  
  
在上述 payload 已经验证可行的前提下，使用 sqlmap：  
```
python sqlmap.py -u "http://192.168.1.9:8080/Less-29/?id=1" -p id --level=5 --risk=3 --dbms=mysql --batch

```  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVHpx0Qico5T8IAicRs5PUPR5hdIuLrEzBdicKvzP26eYgDm0ibwK7NPrM6LSgBwJN1tLdY4DjjsqMR8dQ/640?wx_fmt=gif&from=appmsg "")  
  
sqlmap 同样可以识别并利用注入点。到这里为止，一切看起来都“非常正常”。但问题也正是在这里。  
## 二、问题：如果只是普通显错注入，为什么要单独设计第 29 关？  
  
回顾 sqli-labs 的设计逻辑可以发现：  
- 26 / 26a：空格与关键字过滤  
  
- 27 / 27a/28/38a：大小写绕过  
  
如果第 29 关只是一个**没有新知识点的显错注入**  
，那它在整个关卡体系中是站不住脚的。  
  
这意味着：刚才成功的注入，很可能只是“解析顺序恰好成立”  
。  
## 三、第 29 关的真正考点：HTTP 参数污染（HPP）  
### 3.1 什么是 HTTP 参数污染  
  
HTTP 参数污染（HTTP Parameter Pollution）指的是：同一个参数名在请求中出现多次，但在不同处理阶段，被不同方式解析和使用。  
  
例如：  
```
?id=1&id=2
```  
  
在不同环境中，可能会出现：  
- 只取第一个值  
  
- 只取最后一个值  
  
- 多个值拼接  
  
- 不同位置分别取值  
  
### 3.2 第 29 关的关键点  
  
在第 29 关中：  
- id  
 参数 **被多次使用**  
  
- 且 **并不一定在同一位置取值**  
  
- Web 层和 SQL 层对参数的“理解”并不一致  
  
这正是 HTTP 参数污染能够成立的基础。  
## 四、为什么单参数注入能“碰巧成功”  
  
回到最开始的 payload：  
```
?id=1'and updatexml(...)
```  
  
这条语句之所以能成功，是因为：  
- 同一个 id  
 同时承担了：  
  
- SQL 语句闭合  
  
- 注入逻辑执行  
  
在某些情况下：  
- SQL 结构恰好成立  
  
- updatexml 被成功执行  
  
**但这是不稳定的。**  
  
实际上是在：用一个参数，强行完成两个阶段的任务  
## 五、参数污染的正确利用方式：拆分参数职责  
### 5.1 利用多个同名参数  
  
真正符合第 29 关设计思路的 payload 应该是：  
```
?id=1'&id=2' and updatexml(1,concat(0x7e,database(),0x7e),1) --+
?id=1'&id=-2' union select 1,2,3 --+
?id=1'&id=-2' union select 1,database(),version() --+
```  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVHpx0Qico5T8IAicRs5PUPR5hZsqOfWv6dMZPgepmua5BDYF2Pw38PSVhDicKZTCk8xBxpFwMeAo49sQ/640?wx_fmt=gif&from=appmsg "")  
### 5.2 这里发生了什么？  
#### 第一个 id=1'  
- 作用： 闭合原始 SQL  
  
- 目标：保证 SQL 语句结构合法  
  
#### 第二个 id=2' and updatexml(...)  
- 作用： 注入恶意逻辑  
  
- 目标：触发 XPATH 显错  
  
这时：  
- **参数被拆分**  
  
- **职责被分离**  
  
- 注入变得稳定、可复现  
  
## 六、为什么 sqlmap 在第 29 关“看起来能用，但并不理解本质”  
  
sqlmap 能在这里成功的原因是：  
- 单参数注入路径刚好成立  
  
- payload 没被破坏  
  
但它**并没有真正理解参数污染场景**  
：  
- sqlmap 默认假设：  
  
- 一个参数名 → 一个参数值  
  
- 而第 29 关：  
  
- 一个参数名 → 多次出现 → 多阶段消费  
  
这也是为什么：在真实环境中，  
HPP 漏洞往往需要人工构造，而不是完全依赖自动化工具。  
  
结语  
  
第 29 关表面上看是一个普通的显错注入，实际上应该考察的是 HTTP 层面的参数解析问题。  
  
单参数注入之所以能成功，只是解析顺序恰好成立。  
  
真正稳定、符合设计意图的利用方式，是通过  
HTTP 参数污染，将“闭合”和“注入”拆分到不同参数中完成。  
  
