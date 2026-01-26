#  免费，够强！实战使用MonkeyCode审计0day&安全开发  
MonkeyCode
                    MonkeyCode  听风安全   2026-01-26 01:00  
  
 序言  
  
2026年了，应该没有人不用AI了吧。第一次直观的感受到AI的强大还得是三年之前刚用cursor的时候，记得当时是在逆向  
一  
个web站点的加密算法，把源码丢给cursor就直接秒掉了。最近又接二连三出来了很多工具比如  
Antigravity、  
Windsurf、kiro等等。虽然能用但是限制越来越多，也是一直在寻找一个能平替的工具。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQuZpsicWeIeuRMvV9b77HF8ank4aUfiaKow9xsb6E0kpFBT3XLldoQjvw/640?wx_fmt=jpeg&from=appmsg "")  
  
正好看到CT在宣传的  
这  
个  
MonkeyCode，试了试代码审计和工具二开效果都还蛮不错的，本篇文章会着重针对这两点进行详细讲解我是怎么通过  
MonkeyCode审计到0day和轻松实现工具二开的。  
  
先来了解一下  
MonkeyCode是什么？  
  
MonkeyCode 是由长亭科技推出的企业级 AI 开发平台，致力于为开发者提供更专业、更可靠、更可扩展的 AI Coding 体验，地址如下：  
  
https://monkeycode-ai.com/  
  
MonkeyCode有三个模式分别是：开发、设计、审查  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQl2aBXzv1GtT4OeHSfZdANLk13eibAhXuEWT9J46kACKZNBWVHdq2YzA/640?wx_fmt=png&from=appmsg "")  
  
再具体的使用可以去查看官方文档了解  
  
https://monkeycode.docs.baizhi.cloud/  
  
MonkeyCode   
代码审计  
  
用  
MonkeyCode做代码审计也非常简单，只需要把代码压缩包上传即可或者选择GitHub的地址，它会自动下载。这里要选择审查模式。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQxxIq8HiahVxia7IodMYkPMkoUZSPF3PZyexdB39z1uk5xwBnss7aTP3A/640?wx_fmt=png&from=appmsg "")  
  
上传源码压缩包，告诉它要做的事情就行了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQaO45mcrG5DCdgYBXqy5cYrWSyE5eibFiaHkOYJDgKtffN2K9fC6icENJQ/640?wx_fmt=png&from=appmsg "")  
  
MonkeyCode支持  
完全免费使用  
，当然也可以使用付费的模型，这里我就使用Claude code进行测试。使用  
Claude code需要耗费对应的点数，不过可以邀请用户获得点数，实现左脚踩右脚上天。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQ3HVCoibiazn0UXdjAPb7tsEhBTdvicZwUT45NpJX9Zhr0Kjan88zXHNpA/640?wx_fmt=png&from=appmsg "")  
  
接下来会自动创建一个开发环境，这个也就相当于是开了一个临时的vps，非常方便  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQkbwDciaaIRvOMIbdqKImH823RXCoGPvAEywsd9pvACs8TrmJULh3l2w/640?wx_fmt=png&from=appmsg "")  
  
结果也是很给力，光说不练假把式，来验证几个看看漏洞是否真实存在  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQcRrMnNXSqPlzklGGdXUsibBzNY4YeERwSuX4B3K3CR731oOwtOOOkuA/640?wx_fmt=png&from=appmsg "")  
  
这里挑了两个严重进行了验证都是存在的，路径遍历和文件上传  
  
先来看一下权限绕过这个漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQOZoEftJ5EbibGrmk1AH6Hr3DApPccnw9eXCKTbxJ1ib8VkPXRnLrwPYQ/640?wx_fmt=png&from=appmsg "")  
  
/api/file/下的接口都无需认证可实现未授权访问，而  
路径遍历和文件上传的路径正好都在这个接口下。  
  
可跨目录未授权文件读取，不过这里有点鸡肋的是只能读xlsx格式的文件因为代码中写死了，代码这里就不贴出来了，只作为测试验证漏洞确实存在。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQfrqHXzeXm8TsfaPzcGEa7NvF2FdusM7JZW5C5YeBzfUicYb6cyyqyeg/640?wx_fmt=png&from=appmsg "")  
  
如果你是安全人员，可以通过  
MonkeyCode大大提升效率，助你更快挖到0day或者辅助进行代码审计，如果你是开发人员同样可以使用  
MonkeyCode检查你的代码是否安全  
是  
否规范。  
  
MonkeyCode   
工具二开  
  
这里对gogo进行二开，对代码进行混淆然后加上一个输入密码才能使用的功能。  
  
这里就选择开发模式，然后复制GitHub地址就行了，再输入提示词就可以开始干活了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQpNaC0KYVtetodcxxLSriclCpOyxaiaM2ys7pltzxLRpqTo7kbBIl0xvQ/640?wx_fmt=png&from=appmsg "")  
  
MonkeyCode每执行一个任务都会起一个临时的虚拟环境，也就意外着可以直接在平台进行编译，省去了在本地下载配置各种环境报错的麻烦。属于是即开即用，很方便。  
  
等几分钟之后，ai就工作完毕  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQfrr0sO0wghpK1v3YMty9Q7tHxsO6gycEsHo1qibSIVrnWMyRic5V7bng/640?wx_fmt=png&from=appmsg "")  
  
然后来测试一下看看，效果也是嘎嘎好  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQVlfO20nuEoJkONPA1sUayZ9PZaAUsn9cePbicp7qnKoSYtwRKBcQebw/640?wx_fmt=png&from=appmsg "")  
  
也可以根据自己的需求手动修改代码，或者配置环境  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQCicTXoBrSQhPVB37k9hUhCNxBhvSYLffyucTg1B1qaUzaOwdUJ9wANg/640?wx_fmt=png&from=appmsg "")  
  
这里只是提供一个开发模式的使用思路，大家可以用来做更多的事情甚至开发一个新的工具。  
  
结尾  
  
上面代码审计的时候提到了使用  
Claude code需要耗费对应的点数，这里就教给大家怎么白嫖点数，首先新注册的用户可以直接获得价值200元也就是20000点。同时，  
邀请1个好友就可以活动2000点数，而且是不设上限的！  
  
注册方式：  
  
https://monkeycode-ai.com/?ic=019bd617-f10d-7e6f-b8e1-5481d98c8a42  
  
扫描下方二维码可加入官方群聊，群内不定时发放点数，有什么相关问题也可以反馈  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Tp9VOk1IaycpX8pojk9pe80mVibwv1fAQIOkpppv2fo0noMIlYnde7OSZt2M0P3o1E0SGbw1KRlPibxugWF81wuw/640?wx_fmt=png&from=appmsg "")  
  
快来体验体验吧~  
  
