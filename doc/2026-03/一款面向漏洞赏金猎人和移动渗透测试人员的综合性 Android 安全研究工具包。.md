#  一款面向漏洞赏金猎人和移动渗透测试人员的综合性 Android 安全研究工具包。  
AndroHunter
                    AndroHunter  贝雷帽SEC   2026-03-10 14:22  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
**免责声明**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/HVNK6rZ71oofHnCicjcYq2y5pSeBUgibJg8K4djZgn6iaWb6NGmqxIhX2oPlRmGe6Yk0xBODwnibFF8XCjxhEV3K7w/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic "")  
  
本公众号所提供的文字和信息仅供学习和研究使用，  
请读者自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任  
。  
工具来自网络，安全性自测，如有侵权请联系删除。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
**工具介绍**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
  
AndroHunter 是一款原生 Android 应用，提供一整套移动安全测试工具——所有工具均可直接在设备上运行，大多数功能无需 root 权限。它专为参与漏洞赏金计划（例如 HackerOne、Yes We Hack、Intigriti 等）的安全研究人员而设计，帮助他们快速高效地分析 Android 应用。  
  
该工具涵盖了整个 Android 攻击面：静态分析（APK、DEX、Manifest）、动态测试（Intent 模糊测试、ContentProvider 探测、广播注入）、运行时分析（Frida 脚本生成、SSL 绕过）和网络拦截（HTTP 代理）。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/k2PJfskYEClGGvNRf4qzqvmrmTV6b868K00kRuCkhOg4djCgYyWxCy9gahxu5Kpb9Xo9icNsRYr2cI7vfeqBYoYBhPoicbjbdFicjaNBTzm0WI/640?wx_fmt=png&from=appmsg "")  
  
  
特征  
### 📱 应用浏览器  
- 列出所有已安装的应用程序及其元数据（软件包名称、版本、权限、目标 SDK）  
- 按系统/用户应用筛选  
- 从应用详情视图快速导航至任何分析模块  
### 🔍 DEX 分析器  
- 从 APK 文件中提取并分析.dex  
文件  
- 扫描硬编码的密钥：API 密钥、令牌、密码、URL、私钥  
- 字符串模式匹配及严重性分类（VULN  
/  
SUSP  
/  
SAFE  
）  
- 使用弹出式查看器进行类和方法枚举  
- 支持多 DEX APK——每个 DEX 文件单独分析。  
### 📄清单查看器  
- AndroidManifest.xml  
直接从 APK  
解析（无需反编译器）  
- 三标签视图：**组件**  
、**权限**  
、**原始 XML**  
- 重点介绍导出的组件、危险权限和深度链接方案  
- 识别潜在攻击面（导出的活动、服务、接收器、提供者）  
### 🎯 意图模糊测试器  
- 列出目标应用的所有已导出活动、服务和广播接收器  
- 发送带有自定义附加信息、数据 URI 和类别的精心设计的意图。  
- 支持通过 Intent 数据传递路径遍历有效载荷（file:///data/...  
）  
- 与有效载荷引擎集成，实现自动化测试  
### 💥 有效载荷引擎  
- 基于 Logcat 的实时结果监控  
- 自动将有效载荷交付至目标组件  
- 视觉结果分类：（VULN  
红色）/  
SUSP  
（黄色）/  
SAFE  
（绿色）  
- 支持深度链接利用、OAuth重定向劫持、文件URI泄露  
### 🗄️ 内容提供商模糊测试器  
- 枚举目标应用程序的所有已导出内容提供程序  
- 每个提供程序测试 9 种 SQL 注入有效载荷（基于错误、布尔值、UNION、基于时间）  
- 检测可读/可写提供程序和模式暴露情况  
- 一键即可从 APK 分析器结果导航至提供程序模糊测试工具，并预填充目标  
### 📁 文件提供程序路径分析器  
- 解析res/xml/  
APK 中的配置文件以提取 FileProvider 路径定义  
- 按路径类型划分的风险分类：  
- root-path  
路径为空 →**严重**  
（完全文件系统访问权限）  
- external-path  
路径为空 →**高**  
- cache-path  
/  
external-cache-path  
→**中等**  
- **路径遍历测试器**  
：包含 9 个遍历有效载荷的自动化测试  
- 尝试实际读取文件，ContentResolver  
并在成功时报告文件内容。  
- **ADB 命令选项卡**  
：即用型adb shell content read --uri '...'  
命令  
### 🏃 活动启动器  
- 列出所有已安装应用的活动，并导出状态徽章  
- 一键启动，可选额外数据/深度链接注入  
- ADB 命令生成器：adb shell am start -n pkg/activity --es data "payload"  
- 按仅导出文件筛选，以便快速识别攻击面  
### 📡 广播模糊器  
- 10 个预构建的广播有效载荷，涵盖 6 个类别：  
- **身份验证**  
：绕过登录、会话劫持  
- **SQLi**  
：通过 Intent extras 进行 SQL 注入  
- **LFI**  
：通过文件路径附加信息进行路径遍历  
- **重定向**  
：开放式重定向、深度链接劫持  
- **PrivEsc**  
：权限提升，组件启用  
- **Exfil**  
：通过备份意图进行数据泄露  
- 自定义广播发送器：指定操作 + 键值对附加信息  
- 每个有效载荷的 ADB 命令复制  
### 🔑 共享偏好设置阅读器  
- shared_prefs/*.xml  
从目标应用程序数据目录  
读取文件  
- 用于run-as  
调试应用程序，其他情况则回退到dumpsys  
其他方式。  
- 敏感  
按键  
检测  
：token  
，，，，，，passwordsecretapi_keysessionjwtcookie  
- 按敏感内容筛选、全文搜索、一键复制  
### 🐛 Frida 脚本生成器  
- 生成针对所选目标包定制的、可直接使用的 Frida hook 脚本  
- 6 个脚本类别：  
- **SSL 绑定绕过**  
：OkHttp3、TrustManager、Conscrypt、BoringSSL  
- **Root 检测绕过**  
：RootBeer、SafetyNet、File.exists()  
hook  
- **登录绕过**  
：通过反射自动发现身份验证/登录/会话类  
- **加密监控器**  
：钩子javax.crypto.Cipher  
— 记录所有加密/解密操作  
- **SQL 监视器**  
：  
钩子SQLiteDatabase.rawQuery  
，，execSQLquery  
- **HTTP 拦截**  
：OkHttp3 和HttpURLConnection  
- 一键复制（带或不带启动命令头）  
- 准备运行的命令：frida -U -f com.target.app -l script.js --no-pause  
### 🔓 SSL 证书绑定绕过指南  
- 6 种绕过方法，附详细步骤说明：  
1. **Frida SSL Kill Switch 2**  
  
— 最简单，无需 root 权限  
1. **反对意见**  
——android sslpinning disable  
1. **Magisk TrustMeAlready**  
  
— 系统级绕过  
1. **APK 重新打包**  
—network_security_config.xml  
通过注入apktool  
1. **Xposed / LSPosed + JustTrustMe**  
1. **Burp Suite + 用户 CA**  
### 🌐 交通拦截器  
- 内置 HTTP 代理服务器运行在127.0.0.1:8877  
- 捕获任何配置为使用代理的应用程序的 HTTP 流量  
- HTTPS CONNECT 隧道支持  
- 实时请求/响应列表，并按方法颜色编码  
- 敏感  
标题高亮显示：Authorization  
，，  
以红色显示CookieToken  
- 每次请求的详细信息视图：完整请求头、请求体、响应体、时间  
- **curl 命令生成器**  
：一键复制任何捕获的请求  
- 按 URL、主机、正文内容或 HTTP 方法筛选  
### 🖥️ 终端  
- 设备端 shell 命令执行  
- 快捷  
指令  
芯片  
：id  
，，，，，，，whoamiuname -aenvifconfignetstat -anpsls /data  
- 颜色编码的输出：命令（绿色）、标准输出（白色）、标准错误输出（红色）  
- 输入法栏边距：键盘打开时输入栏仍然可见  
### 👁️ 广播监视器  
- 实时监控系统和自定义广播意图  
### 🎭 任务劫持（StrandHogg）  
- 针对任务亲和性劫持漏洞的测试（StrandHogg 1.0）  
### ♿ 辅助功能监视器  
- 监控目标应用程序的辅助功能服务事件  
    
## 涵盖的漏洞类别  
<table><tbody><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><strong><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">类别</span></span></strong></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><strong><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">模块</span></span></strong></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">硬编码的秘密</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">DEX分析仪</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">导出组件</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">清单查看器、意图模糊测试器、活动启动器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">SQL注入</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">内容提供商模糊测试器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">路径遍历</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">文件提供程序分析器，意图模糊测试器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">不安全的深层链接</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">意图模糊测试器、有效载荷引擎、活动启动器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">OAuth重定向劫持</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">有效载荷引擎</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">广播注入</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">广播模糊测试器，广播监视器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">SSL 固定</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">SSL绕过指南，Frida生成器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">敏感数据存储</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">共享偏好读取器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">StrandHogg 任务劫持</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">任务劫持模块</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">HTTP流量分析</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">交通拦截器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">绕过根检测</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;background-color: rgb(246, 248, 250);"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">弗里达生成器</span></span></p></td></tr><tr style="height: 33px;"><td data-colwidth="206" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">密码学弱点</span></span></p></td><td data-colwidth="375" width="375" style="border: 1px solid #d9d9d9;"><p style="margin: 0;padding: 0;min-height: 24px;"><span style="color: rgb(31, 35, 40);font-size: 16px;"><span leaf="">Frida 加密监视器</span></span></p></td></tr></tbody></table>  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
**工具使用**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
```
Android 10+（API 29+）
大多数功能无需root权限。
根目录 / 
run-as：允许在非调试应用上读取 SharedPrefs
通过 USB 进行 ADB 连接：ADB 管理器命令需要此操作
设备上的 Frida 服务器：Frida 脚本执行所必需（脚本在设备上生成，从 PC 运行）
```  
### Traffic Interception  
```
# Start proxy in app → tap ▶ START
# Configure proxy on device Wi-Fi: 127.0.0.1:8877

# Or via ADB:
adb shell settings put global http_proxy 127.0.0.1:8877

# Use target app — requests appear in real time
# Tap any entry for full details + curl command

# Remove proxy when done:
adb shell settings put global http_proxy :0
```  
### Frida 脚本用法  
```
# Push frida-server to device
adb push frida-server /data/local/tmp/
adb shell chmod 755 /data/local/tmp/frida-server
adb shell /data/local/tmp/frida-server &

# Copy generated script from app, then:
frida -U -f com.target.app -l script.js --no-pause
```  
### 文件提供程序路径遍历  
```
# Via ADB (copy from ADB Commands tab in app):
adb shell content read --uri 'content://com.target.app.fileprovider/files/../../../data/data/com.target.app/databases/'
```  
  
  
  
**下载链接**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
```
https://github.com/ynsmroztas/AndroHunter
```  
  
  
  
End  
  
  
“点赞、在看与分享都是莫大的支持”  
  
  
**工具精选**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
  
  
[【红队】一款安全测试工具集——Onyx](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494121&idx=1&sn=8675cf1677352620a57d68ff9f0b0686&scene=21#wechat_redirect)  
  
  
[【红队】一款 AI 原生安全测试平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494139&idx=1&sn=5d8a98e0d0cb700c124aeaecae595d4c&scene=21#wechat_redirect)  
  
  
[【红队】Webshell 管理与后渗透平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494098&idx=1&sn=cb7bc8f3cc7f59e6f80f4b56e7d4c1f9&scene=21#wechat_redirect)  
  
  
[【红队】BProxy - 多级 SOCKS5 代理工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494084&idx=1&sn=dbc658a17e6ddc0dcd7c7857c841478a&scene=21#wechat_redirect)  
  
  
[【红队】攻击面管理平台 (ASM)](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494076&idx=1&sn=e9c2ff60ccd065dc223c71042515268d&scene=21#wechat_redirect)  
  
  
[【红队】ParrotOS 7.0 正式发布 代号：Echo](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494038&idx=1&sn=243e1105a439eb986fdc34534e6a8d19&scene=21#wechat_redirect)  
  
  
[【红队】一款专为红队打造的主动资产指纹识别工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493898&idx=1&sn=3e395ade15061739c89f5d0a13645af4&scene=21#wechat_redirect)  
  
  
[【蓝队】SamWaf开源轻量级网站防火墙](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493939&idx=1&sn=e56702a24dcae461024668aaea6aced3&scene=21#wechat_redirect)  
  
  
[[蓝队] FastMonitor - 网络流量监控与威胁检测工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493925&idx=1&sn=a952c400c3ee63c8401ff57692745dd1&scene=21#wechat_redirect)  
  
  
[【蓝队】漏洞全生命周期管理平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493803&idx=1&sn=10daa12b5a3523bf4a1ecc665890f917&scene=21#wechat_redirect)  
  
  
[【蓝队】蓝队Ark神器 OpenArk v1.5.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493788&idx=1&sn=91a31e2d507cb9e0111c19dac98b315e&scene=21#wechat_redirect)  
  
  
[【红队】矛·盾 武器库 v3.2](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493701&idx=2&sn=9cf7e304fee21328bac6d9bd97b81183&scene=21#wechat_redirect)  
  
  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/pM2klgicgT5dylTzXyrXBmex6dlAsZ0QJOQdzqcw2HpC49rnL0dTHNsWsOze4QmRYN7fPRoLdVK5MXs0DXtOvZw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
                                                   
  
      
  
  
  
