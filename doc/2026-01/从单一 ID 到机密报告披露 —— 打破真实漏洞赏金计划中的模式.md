#  从单一 ID 到机密报告披露 —— 打破真实漏洞赏金计划中的模式  
haidragon
                    haidragon  安全狗的自我修养   2026-01-22 06:47  
  
##   
# 官网：http://securitytech.cc  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQEREDjrR3AQgTV2E82iaD0yUkkfRVozWIwWhvv7oqhQgpdDMZzNSH9iacnzoJObzr60RSJXcJu3kI4uPA/640?wx_fmt=png&from=appmsg "")  
##   
  
这是我的第二篇博文。  
  
这次的方法不同了。  
  
没有花哨的攻击手段，也没有明显的漏洞。只有耐心、模式识别和大量的深夜好奇心。  
## 了解应用程序流程  
  
在深入研究实际漏洞之前，了解此应用程序如何处理漏洞报告非常重要。  
  
当研究人员通过电子邮件报告漏洞时，团队会在其 Web 应用程序中创建一个内部问题——本质上是一个工单系统。每个报告都会被分配一个问题 ID，并生成一个专门的页面来跟踪该报告的整个生命周期。  
  
本问题页面维护着：  
- 完整的通信历史记录  
  
- 状态更新  
  
- 上传的证据文件，例如屏幕截图、文本文件和 PDF 文件  
  
每期内容都可以通过类似这样的 URL 访问：  
  
/common/issue-tracking.php?id=228  
  
之后，所有相关的证据文件都会从内部端点动态加载。这种流程旨在集中报告并简化协作，但如果访问控制处理不当，它也会成为一个严重的攻击面。  
  
了解了这个工作流程之后，我开始研究这些报告资源的保护程度。  
## 从简单的 ID 到更强大的功能  
  
首先吸引我注意的是 id 参数的解码是多么容易。  
  
乍一看，这个值似乎很复杂——一个很长的十六进制字符串——但当在 Burp Suite 中解码为 ASCII 十六进制时，它立即变成了可读字符。  
  
不是哈希值，  
  
也不是随机字节，  
  
只是结构化文本。  
  
光是这一点就足以让我放慢脚步，仔细观察。  
## 值得再次考察的目标  
  
我之前就研究过这个目标。  
  
早期的报告包括存储型跨站脚本攻击（XSS）和双因素身份验证（2FA）配置错误等问题。过了一段时间后，我决定以全新的视角重新审视它。  
  
夜已深——正是在这种时候，你不再匆忙，开始注意到别人忽略的事物。  
  
该应用程序的报告流程非常简单：  
  
如果您通过电子邮件报告漏洞，团队会在他们的 Web 应用程序中创建一个内部问题。每个报告都会生成一个类似工单的页面，其中包含完整的沟通记录以及上传的证据。  
  
这些报告可通过类似这样的 URL 访问：  
  
/common/issue-tracking.php?id=228  
  
当然，我首先检查的就是这个端点是否存在经典的 IDOR 漏洞。经过充分测试后，很明显简单的 ID 操作不起作用，不存在直接的 IDOR 漏洞。我没有继续深入研究，而是回到我**之前的报告**  
，查看了原始邮件往来，其中提到了相同的问题跟踪 URL。  
  
那时我决定深入挖掘——不是横向挖掘，而是纵向挖掘。  
## 证据档案改变了一切  
  
在报告页面中，我注意到所有上传的证据文件——图片、文本文件、PDF——都是从不同的端点加载的：  
  
/common/admin/issue-tracking/file.php?id=585b243672692442373b4d4d2b33327c707b737428517b6c73266d3423747d6f364d3823255d3a  
  
这里的参数 id  
 看起来像是经过编码的，而不是随机的。  
  
我直接把它复制到 Burp Decoder 中，并将其解码为 ASCII 十六进制。  
  
结果：  
  
X  
$6ri$B7;MM+32|p{st(Q{ls&m4[#t]()  
}o6M8#%  
:  
  
乍一看，它显得很杂乱——大写字母、小写字母、数字、特殊字符——所有东西都混杂在一起。  
  
但我并没有就此止步。  
  
按回车键或点击查看完整尺寸的图片  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQEREDjrR3AQgTV2E82iaD0yUkkZxia4xZfDGKJKaOlFAqnGe0cfBEuVqvC1hokd1NLYyG7AyPFvcFhv8w/640?wx_fmt=png&from=appmsg "")  
  
解码为 ASCII 十六进制  
## 模式开始显现  
  
我查看了同一份报告中的另一个证据文件 URL：  
  
/common/admin/issue-tracking/file.php?id=565b243672692442373b4d4b2b33327c707b737428517b6c73266d3423747d6f364d3823255d36  
  
解码：  
  
V  
$6ri$B7;MK+32|p{st(Q{ls&m4[#t]()  
}o6M8#%  
6  
  
现在事情开始变得有趣起来了。  
  
比较两个解码值，只有**四个部分发生了变化**  
：  
- 首字母大写变化  
  
- 中间两个大写字母变化  
  
- 最后一个字符变化  
  
- 其余保持不变  
  
那不是随机性，  
  
那是结构。  
  
为了确保万无一失，我又查阅了一份证据文件：  
  
/common/admin/issue-tracking/file.php?id=545b243672692442373b4d492b33327c707b737428517b6c73266d3423747d6f364d3823255d32  
  
解码：  
  
T  
$6ri$B7;MI+32|p{st(Q{ls&m4[#t]()  
}o6M8#%  
2  
  
至此，这种模式已无可辩驳。  
  
按回车键或点击查看完整尺寸的图片  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQEREDjrR3AQgTV2E82iaD0yUkk6mntN8uHg8KeJ8YE1V1bic3uv0FNLmyTibI8SO8BwRq7sYVy5AgczPVQ/640?wx_fmt=png&from=appmsg "")  
  
模式理解  
## 自动化好奇心  
  
一旦规律明确，手动测试就失去了意义。  
  
我编写了一个 Python 脚本：  
1. 只暴力四个变量位  
  
1. 重新编码为 ASCII 十六进制  
  
1. 自动请求端点  
  
1. 记录有效响应  
  
这不是盲目蛮力，而是**结构驱动的约束枚举**  
。  
  
于是我让脚本运行了。  
  
按回车键或点击查看完整尺寸的图片  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQEREDjrR3AQgTV2E82iaD0yUkkereAjKc4tIjhdjBf66IicJLaDFlMreMPm2f4bibgKveTObNPACdszsvg/640?wx_fmt=png&from=appmsg "")  
  
成功获取了一些其他有效 ID  
## 当剧本开始反驳  
  
脚本开始返回有效响应。  
  
当我手动访问这些网址时……  
  
我看到了**其他研究人员的报告**  
。  
  
完整 PDF，  
  
截图，  
  
内部漏洞细节。  
  
无需认证，  
  
无需授权。  
  
那一刻问题变得严肃起来。  
  
按回车键或点击查看完整尺寸的图片  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQEREDjrR3AQgTV2E82iaD0yUkkONwBibFCHsgI0jliaCf3Jlv6WBqibibRpkunhP99BCpZk5P8srnbwmqWVw/640?wx_fmt=png&from=appmsg "")  
  
已成功下载其他用户报告  
## 为什么这很重要  
  
这不是破解加密，  
  
也不是暴力破解。  
  
而是发现：**看似复杂，其实可预测。**  
  
机密漏洞报告是平台最敏感的资产之一。  
## 最后想说的话  
  
无论看到什么编码值，都不要默认它是安全的。  
  
尝试解码它。  
  
大多数漏洞并非隐藏，  
  
而是就在眼前。  
- 公众号:安全狗的自我修养  
  
- vx:2207344074  
  
- http://  
gitee.com/haidragon  
  
- http://  
github.com/haidragon  
  
- bilibili:haidragonx  
  
##   
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vBZcZNVQERG9naV4nCia8QSsm3ONq58k2yzaqYLp6ricjrGYBwSNib1S0xaB1AC15CqSSado8Ng7EAmibVQRHX4TpA/640?wxfrom=5&wx_fmt=jpg&watermark=1&wx_lazy=1&tp=webp#imgIndex=1 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5 "")  
  
****- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5 "")  
  
##   
  
  
