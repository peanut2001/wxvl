#  新型变种木马 XWorm 7.2 攻击链深度拆解：Excel漏洞 + 图片隐写 + 进程镂空  
原创 ZKAFKA
                    ZKAFKA  网络安全研究站   2026-02-24 07:46  
  
![](https://mmbiz.qpic.cn/mmbiz_png/HmaGibWBicEElcawyVVdhmkZX52foQX6TibC9NtQu5GSjjjJhQ28n1BDqdkUB5p92dricMyia9wSUZaWiauIMRjCHSUj7ichLGdgzKe6le0u6xaV6Q/640?wx_fmt=png&from=appmsg "")  
# 近日，Fortinet 旗下 FortiGuard Labs 的最新调查披露了一起高度复杂的钓鱼攻击活动：攻击者通过精心构造的邮件传播最新变种的 XWorm 7.2 远程访问木马（RAT），不仅利用了经典的 Excel 公式编辑器漏洞（CVE-2018-0802），还结合了图片隐写术、进程镂空等技术，实现了对 Windows 系统的完全控制。以下是该攻击链的完整技术拆解及防御建议。  
#   
  
01  
  
  
攻击路径详细拆解  
  
**1. 钓鱼邮件投递：多主题诱饵，恶意 Excel 附件**  
  
攻击者发送大量钓鱼邮件，伪装  
成**付款请求、采购订单、银行单据**  
等商务主题，邮件正文诱导收件人打开附件。附件为 **Excel 加载项文件（.XLAM）**  
，  
这是本次攻击的初始载体。  
  
![XWorm 活动中使用的钓鱼邮件示例](https://mmbiz.qpic.cn/mmbiz_png/HmaGibWBicEEmZF9wrDxG0DibticMMod5UU6VDUEJVtfpCGqVucEXiaK6a0DLXPKtic27ric9PboAZnC1zX27tL10BzQjT7ojDH3cRLxbmiaXvy3NJ0/640?wx_fmt=png&from=appmsg "")  
  
****  
**2. Excel 漏洞利用（CVE-2018-0802）**  
  
附件中的 Excel 文件包含一个精心构  
造的 **OLE 对象**  
（嵌入在 sheet1.xml 中，且 autoLoad=true  
）。当用户打开文件时，Microsoft 公式编辑器（EQNEDT32.EXE）会自动解析该对象，触发 **CVE-2018-0802**  
 远程代码执行漏洞。该漏洞自2018年曝光以来仍被广泛利用，许多未及时修补的系统因  
此中招。  
> CVE-2018-0802 是一个存在于 Microsoft Office 公式编辑器组件 EQNEDT32.EXE 中的栈溢出漏洞。该组件在解析包含特殊字体名称记录的 OLE 对象时，由于未能对用户输入的数据进行正确的长度检查，导致在处理过程中将一段超长的数据拷贝到堆栈中。当拷贝操作发生时，超长数据会覆盖堆栈上的返回地址或异常处理结构，从而劫持程序执行流程。攻击者通过构造恶意文档并诱导用户打开，即可利用此漏洞在目标系统上以当前用户的权限执行任意代码。  
  
  
![利用CVE-2018-0802的故障型OLE对象流](https://mmbiz.qpic.cn/sz_mmbiz_png/HmaGibWBicEEkLC1gEE1ibNmjUUu3414Swv6CcwC3wtX6MZzZMEl04bU39oU8fkmicrUa0MRequabfODibK7gS3ZaFHFqh8GibGRG6Tvt3Aibzia7e4/640?wx_fmt=png&from=appmsg "")  
  
  
漏洞利用代码在内存中解密并执行，其核心功能是从远程服务器  
 **retrodayaengineering[.]icu/HGG.hta**  
   
下载一个   
HTA 文件  
，并保存为 %APPDATA%\VA5.hta  
，随后通过 ShellExecuteExW()  
 执行该文件。  
  
****  
****  
**3. HTA 文件执行：混淆脚本暗藏 PowerShell**  
  
下载的 HTA 文件经过重度混淆，插入大量垃圾数据以规避检测。实际执行的是  
 **JScript 代码**  
，该代码解码并运行一段 **Base64 编码的 PowerShell 命令**  
。PowerShell 命令负责下一步的关键操作：下载一张看似无害的  
 **JPEG 图片**  
（托管于 res[.]cloudinary[.]com  
），并从中提取隐藏的恶意代码。  
  
![去混淆的HTA文件，显示嵌入脚本逻辑](https://mmbiz.qpic.cn/mmbiz_png/HmaGibWBicEEm35un5N6iaZmC0OGS7vCvoaKiavVib60QWAUEJHYwc1Cibgz9AYJCsLr9CtpKIzzv9peAcicibR8G60BTwiamWtsDpTsRIU1dTKcCCWw/640?wx_fmt=png&from=appmsg "")  
  
  
**4. 图片隐写术：藏匿于像素间的 .NET 模块**  
  
这张 JPEG 图片并非普通图片。攻击者将一段 Base64 编码的 **.NET 模块**  
 附加在图片文件尾部，并用 BaseStart  
 和 -BaseEnd  
 标记。PowerShell 脚本下载图片后，提取标记之间的数据，解码并直接加载到 **PowerShell.exe 进程的内存中**  
，整个过程无文件写入磁盘，绕过了传统杀毒软件的文件扫描。  
  
该 .NET 模块伪装成合法的 Microsoft.Win32.TaskScheduler  
（任务计划程序相关模块），实际上是 **XWorm 的下载器和加载器**  
。这种伪装手法旨在迷惑分析师和终端防护。  
  
![嵌入在 JPEG 文件中 BaseStart 和 BaseEnd 标记之间的 Base64 编码的 .NET 模块。](https://mmbiz.qpic.cn/mmbiz_png/HmaGibWBicEElgEzYVXHUELhsRsxRUzNXR64u62YGnhsWkFLOF7DDNhHBUYb6IRDfdmAOjqYASsJNdt4cX0Zz6dYChmrVH04AN9iadD9xU5QOw/640?wx_fmt=png&from=appmsg "")  
  
****  
**5. 下载最终载荷：另一层 Base64 编码的 XWorm**  
  
.NET 模块执行后，首先反转并解码第一个参数（一个 Base64 字符串），得到真正的下载地址：hxxp://pub-3bc1de741f8149f49bdbafa703067f24[.]r2[.]dev/wwa.txt  
。该地址返回一个文本文件，内容为另一  
段 **Base64 字符串**  
。解码后，内存中即还原出 **XWorm 的 PE 可执行文件**  
。  
  
![从解码的URL下载文件](https://mmbiz.qpic.cn/sz_mmbiz_png/HmaGibWBicEEmJJfpBysFNY4icmgPdeYGqcedfODoAjX4HpLe8Sk0NHCic8tXibP59glSVrEL4eBHWBRm7MPR4I0jMvjranGuonoJArlw1QFhucA/640?wx_fmt=png&from=appmsg "")  
  
  
**6. 进程镂空：注入 Msbuild.exe 实现隐身执行**  
  
由于 XWorm 基于 .NET 框架，需要 .NET 运行时环境才能执行。攻击者选择了 Msbuild.exe  
——微软的官方构建工具，通常被列入白名单。.NET 模块调用 CreateProcessA()  
 创建 **挂起状态**  
 的 Msbuild.exe  
 进程，然后通过 VirtualAllocEx  
、WriteProcessMemory  
 等 API 将 XWorm 载荷写入该进程内存，最后修改线程上下文并恢复执行。这样，XWorm 便在 Msbuild.exe  
 的上下文中悄然运行，而该进程往往是安全监控的盲区。  
  
![活动中涉及的进程树。](https://mmbiz.qpic.cn/sz_mmbiz_png/HmaGibWBicEEm6IkHxBb13jIBrThulDqEdqKk2I7czBegWgYrRU3gg5AnAujD3K602F4ruHibmvGL4aibVoiaUaPIapvkjHL3iaefWyRJbC2OEJZU/640?wx_fmt=png&from=appmsg "")  
  
至此，攻击者通过 Msbuild.exe  
 进程完全控制受害者主机，整个过程未在磁盘留下任何恶意文件。  
  
![XWorm 网络钓鱼活动感染链概述](https://mmbiz.qpic.cn/sz_mmbiz_png/HmaGibWBicEEn3y2CnvSNs2hzCgibEdCGbNu71dpUvReZX4MSasEbM1Z7j5RQO2tunuTIK2qmKBgRGbWppxDPm5BZsHBcqM4DJuWJvGwJyib5mU/640?wx_fmt=png&from=appmsg "")  
####   
  
02  
  
  
XWorm 7.2 深度解析  
  
#### 本次捕获的 XWorm 版本为 7.2（客户端标识 UD_XWormClient 7.2），编译于 2025 年底至 2026 年初，使用 DeepSea 混淆器保护。其核心特性如下：  
##### 1. 加密通信与 C2 协议  
- 所有网络流量均使用 **AES 算法加密**  
，数据包格式为：[数据包大小（十进制字符串）] + [AES加密数据]  
。  
  
- 连接 C2 服务器（例如 berlin101[.]com:6000  
）后，XWorm 发送注册包，包含受害者 ID、用户名、系统版本、管理员权限、杀毒软件等信息，使用 <Xwormmm>  
 作为字段分隔符。  
  
##### 2. 丰富的控制命令  
##### XWorm 支持数十种远程控制命令，涵盖系统控制、数据窃取、攻击发起等功能。部分高危命令示例：  
<table><thead><tr><th data-colwidth="196" style="border-bottom: 0.666667px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px 10px 0px;text-align: left;"><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;font-weight: bold;">命令</span></span></section></th><th style="border-bottom: 0.666667px solid rgba(0, 0, 0, 0.12);font: 500 15px / 25px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, Oxygen, Ubuntu, Cantarell, &#34;Open Sans&#34;, &#34;Helvetica Neue&#34;, sans-serif;border-top: none;padding: 10px 16px;text-align: left;"><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;font-weight: bold;">功能</span></span></section></th></tr></thead><tbody><tr><td data-colwidth="196"><code><span leaf=""><span textstyle="" style="font-size: 12px;">Urlopen</span></span></code></td><td><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;">在受害者默认浏览器中打开指定网页（可见）</span></span></section></td></tr><tr><td data-colwidth="196"><code><span leaf=""><span textstyle="" style="font-size: 12px;">Urlhide</span></span></code></td><td><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;">在后台隐藏访问网页</span></span></section></td></tr><tr><td data-colwidth="196"><code><span leaf=""><span textstyle="" style="font-size: 12px;">RunShell</span></span></code></td><td><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;">远程执行 Windows 命令</span></span></section></td></tr><tr><td data-colwidth="196"><code><span leaf=""><span textstyle="" style="font-size: 12px;">StartDDos</span></span></code></td><td><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;">发起 DDoS 攻击（持续发送 POST 请求）</span></span></section></td></tr><tr><td data-colwidth="196"><code><span leaf=""><span textstyle="" style="font-size: 12px;">DW</span></span></code></td><td><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;">上传并执行任意文件（PowerShell、BAT、EXE 等）</span></span></section></td></tr><tr><td data-colwidth="196"><code><span leaf=""><span textstyle="" style="font-size: 12px;">FM</span></span></code></td><td><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;">在内存中运行无文件模块</span></span></section></td></tr><tr><td data-colwidth="196"><code><span leaf=""><span textstyle="" style="font-size: 12px;">PCShutdown/</span></span><code><span leaf=""><span textstyle="" style="font-size: 12px;">PCRestart</span></span></code></code></td><td><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;">远程关机 / 重启</span></span></section></td></tr><tr><td data-colwidth="196"><code><span leaf=""><span textstyle="" style="font-size: 12px;">plugin/</span></span><code><span leaf=""><span textstyle="" style="font-size: 12px;">savePlugin</span></span></code></code></td><td><section style="margin-left: 8px;margin-right: 8px;"><span leaf=""><span textstyle="" style="font-size: 12px;">加载或保存插件模块</span></span></section></td></tr></tbody></table>##### 3. 插件架构：功能无限扩展  
  
XWorm 7.2 Pro 版提供超过  
 **50 个插件**  
，以 .NET DLL 形式实现，动态加载至内存。插件可独立与 C2 通信，并存储在注册表 HKCU\SOFTWARE\{victim ID}  
 下。这使得攻击者能按需定制功能，例如：  
- **HVNC（隐形虚拟网络计算）**  
：创建隐藏桌面，窃取数据而不被用户察觉。  
  
- **勒索模块**  
：一键加密磁盘文件。  
  
- **剪贴板劫持**  
：实时替换虚拟货币地址。  
  
- **摄像头/麦克风控制**  
、键盘记录、屏幕截图、密码窃取等。  
  
####   
  
03  
  
  
攻击技术亮点：为何传统防御失效？  
1. **隐写术绕过文件扫描**  
  
恶意 .NET 模块隐藏在 JPEG 图片的尾部，仅通过像素分析无法发现。多数安全产品对图片文件仅做轻量扫描，导致载荷顺利进入内存。  
  
1. **全程无文件执行**  
  
HTA 文件虽短暂写入磁盘，但核心 PowerShell 脚本、.NET 模块和最终 XWorm 载荷均在内存中运行，规避了基于文件的查杀。  
  
1. **利用可信进程 Msbuild.exe**  
Msbuild.exe  
 是微软官方构建工具，常被列入白名单。攻击者将其作为傀儡进程，使恶意行为更难被端点检测产品识别。  
  
1. **老旧漏洞的新生**  
  
CVE-2018-0802 是 2018 年曝光的公式编辑器漏洞，但许多企业仍未彻底修补，成为本次攻击的突破口。  
  
####   
  
04  
  
  
企业防御建议  
#### 面对此类“新老结合”的复合攻击，建议企业采取以下措施：  
1. **修补已知漏洞**  
  
立即为 Office 套件安装补丁，重点修复 **CVE-2018-0802**  
 和 **CVE-2017-11882**  
 等公式编辑器漏洞。  
  
1. **强化 Office 宏策略**  
  
通过组策略全局禁用来自互联网的宏，并启用 Office 的“阻止宏运行”功能。  
  
1. **监控异常进程行为**  
  
1. 启用 PowerShell 脚本块日志，监控从非标准进程发起的下载与反射加载。  
  
1. 关注 Msbuild.exe  
、regsvr32.exe  
 等白名单进程的异常创建（如由 Office 或脚本启动）。  
  
1. **实施内容消除与重构（CDR）**  
  
对通过邮件和 Web 下载的文件（包括图片、文档）进行“消毒”，剥离隐藏代码，只保留纯净内容。  
  
1. **加强员工安全意识**  
  
教育员工警惕  
异常发件人  
的邮件，尤其涉及“启用宏”或“查看图片”的请求，即使附件看似常见文档或图片  
。  
  
在威胁追踪与响应过程中，以下入侵指标（IOC）可帮助识别本次攻击活动的痕迹：  
  
**URLs（恶意载荷下载地址）**  
- hxxps://retrodayaengineering[.]icu/HGG.hta  
  
- hxxps://res[.]cloudinary[.]com/dbjtzqp4q/image/upload/v1767455040/optimized_MSI_lpsd9p.jpg  
  
- hxxp://pub-3bc1de741f8149f49bdbafa703067f24[.]r2[.]dev/wwa.txt  
  
**C2 服务器**  
- berlin101[.]com:6000  
  
**相关样本 SHA-256 哈希值**  
- SNEV_VEND_026011406440.xlam  
: EE663D016894D44C69B1FDC9D2A5BE02F028A56FC22B694FF7C1DACB2BBBCC6D  
  
- optimized_MSI_lpsd9p.jpg  
: 3F4C3C16F63FB90D1FD64B031D8A9803035F3CB18332E198850896881FB42FE5  
  
- HGG.hta  
 / VA5.hta  
: FD9BA9E6BD4886EDC1123D4074D0EAC363DF61162364530B1303390AA621140B  
  
- XWorm RAT payload  
: EACD8E95EAD3FFE2C225768EF6F85672C4BFDF61655ED697B97F598203EF2CF6  
  
####   
  
  
  
本站致力于做最深度、专业、前沿的网络安全知识分享平台，  
欢迎  
点赞、关注、推荐，为您持续更新深度好文。  
  
