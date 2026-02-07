#  OSV-Scanner：一款专门于发现开源软件漏洞的扫描器  
星夜AI安全
                    星夜AI安全  星夜AI安全   2026-02-07 13:56  
  
📌各位可以将公众号设为星标⭐  
  
📌这样就不会错过每期的推荐内容啦~  
  
📌这对我真的很重要！  
  
![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")  
  
📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。  
  
📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。  
  
📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。  
- ![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIrnr1WD0X4Ol9q7eldrXmhgc1dliaRKiawhD7z12A7ro4LgQzXcfWDvG5Y7tIxe6XHDzhIYzvJ8YcTSFWkBu3yQRyxgC1l2vaIE/640?wx_fmt=png&from=appmsg "")  
  
OSV-Scanner 是一款基于 OSV.dev 漏洞数据库的工具，符合 SLSA3 标准。它通过解析 SBOM 和遍历依赖关系来实现对软件供应链中 CVE/OSV 漏洞的扫描，支持从锁文件、容器镜像等多种来源输入，并输出 CVSS 评分以及修复版本映射信息。  
  
该工具的核心功能包括递归扫描、离线同步漏洞数据库、生成可视化的 HTML 报告。它可以集成到 Pre-Commit 钩子中，以实现 CI/CD 流程中的前置风险拦截，并支持 npm、Go、Maven 等主流包管理生态系统。  
  
**安装**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLHibxdTnI3j80kj5DLHX1B89BPHc6udBd1e3xqcvGhKxzk4LmHTmy4ibMTSOUwNiayja4pEUAkhEm4r6ZwYj3106mIasxSVePVWc/640?wx_fmt=png&from=appmsg "")  
  
您可以跳转到文末链接访问 GitHub，在 Release 页面下载对应文件，也可以直接下载文末百度网盘分享的文件。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKMP6zkbHxQhTLKbnnVljdPMl8goByrHORjNSiadkXA7PTicbv24uibZicqg7Niap33dEWYBz270X96mID01UhJqcw9ic5qK2nBDydDU/640?wx_fmt=png&from=appmsg "")  
  
通常，在 Windows 系统上下载我框选的这个文件即可。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIkggzmRqUxaqU92KufgtJ4hzibMTmiclwRkdn423qk8SeiaiaplstytibIbJlh4PlRycomxFG38iaRNtVoYbPYZHMQUZ9tibXkib3WD4g/640?wx_fmt=png&from=appmsg "")  
  
下载后双击文件，它只会闪现一下，因为没有指定运行参数。  
  
我们需要将其添加到系统环境变量中，这样就可以在命令行中直接调用了。  
  
在系统设置中搜索并编辑系统环境变量，按照图示点击，并在 Path 变量中添加可执行文件所在的路径。例如，我的文件在 D:\wangan\OSVscanner  
，那么就添加 D:\wangan\OSVscanner  
。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLlspBicjzUmTMYw4FGDD508ibFfzKGTcWcvfyWcPtzEn30NEYrdFTYkDdGG85Lxcg7ibXxPwl3jRyLrhKMGL97nXJ6DhrYQN15OM/640?wx_fmt=png&from=appmsg "")  
  
保存设置后，您就可以在任意位置使用该工具了。  
  
打开任意命令行窗口，输入：  
```
osv-scanner_windows_amd64.exe --version
```  
  
结果如下图所示：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKDmC2ziaHs95Gz4uMiaQXLMibJgXHpjIaXcsibldpdR12q9l07S07Z6YJMiajbsGtobFHCRKRnGTFs2qicic8dZs3dLY67TUvrkMSNA4/640?wx_fmt=png&from=appmsg "")  
  
**使用**  
  
OSV-Scanner 的核心流程是「提取包信息 → 匹配漏洞库」，支持扫描源代码目录、锁文件、容器镜像等多种目标。  
  
**1. 基础扫描（源代码目录 / 锁文件）**  
  
扫描本地目录（递归扫描）：  
```
# 基础用法：扫描当前目录的所有依赖osv-scanner_windows_amd64.exe scan -r ./# 指定锁文件进行扫描（如 npm、Go、Maven 等）osv-scanner_windows_amd64.exe -L package-lock.json  # npmosv-scanner_windows_amd64.exe -L go.mod             # Goosv-scanner_windows_amd64.exe scan -L pom.xml       # Maven
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKNdE8QV5xXyOKlIcSdbzMwb47OWvsx0ZQyrNJgJI2fgD2yDib0ayU965poiaQeISmy9HMCQl8MVFaES55FofmQWcw258tf2oQHI/640?wx_fmt=png&from=appmsg "")  
  
在 Docker 容器内进行扫描：  
```
# 将当前目录挂载到容器的 /src，并扫描 go.moddocker run -v ${PWD}:/src ghcr.io/google/osv-scanner -L /src/go.mod
```  
  
**2. 容器镜像扫描**  
```
# 扫描本地 Docker 镜像（需要安装 Docker）osv-scanner_windows_amd64.exe scan image my-docker-img:latest# 使用 Docker 方式扫描容器镜像docker run ghcr.io/google/osv-scanner scan image my-docker-img:latest
```  
  
**3. 生成 HTML 报告并在本地预览**  
```
# 扫描锁文件并在 8000 端口启动 HTML 报告服务osv-scanner_windows_amd64.exe scan -L package-lock.json --serve
```  
  
然后，访问 http://localhost:8000[1]  
 即可查看可视化的漏洞报告。  
  
**修复指引（实验性功能）**  
  
扫描完成后，可以使用 fix  
 子命令获取修复建议：  
```
osv-scanner_windows_amd64.exe fix -M package.json -L package-lock.json
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKqJ4P7hdEfThSIPicdcAEUTRdzPE5HfuYyI2tREsWXgGLNX1x8qlc5TTDaXibu4dVZEZIo4vcmWmmKJQSu64FMFwFjxIX6hm0ok/640?wx_fmt=png&from=appmsg "")  
  
关注微信公众号后台回复“**20260207**  
 ”，即可获取项目下载地址   
  
关注微信公众号后台回复**入群**  
 即可加入星夜AI安全交流群  
  
  
  
圈子介绍  
  
现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。  
  
已产出的安全工具及成果包括：  
- 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护，无感知运行，突破多引擎联合检测）  
  
- XXByPassBehinder v1.1 冰蝎免杀生成器（定制化冰蝎免杀工具，绕过主流终端防护与EDR动态检测，支持自定义载荷）  
  
- 哥斯拉二开免杀定制版（二开优化，深度免杀，突破终端防护与EDR检测，适配多场景植入）  
  
- NeoCS4.9终极版（高级免杀加载工具，强化载荷注入与进程劫持，适配多系统版本，无兼容问题）  
  
- WinDump_免杀版（浏览器凭证窃取工具，支持Chrome/Edge/Firefox等主流浏览器，一键提取敏感数据，免杀过防护）_  
  
- _DumpBrowser_V1_免杀版（浏览器凭证窃取工具，专攻浏览器密码、Cookie、历史记录提取，免杀性能拉满）  
  
- fscan二开版（二开优化内网扫描工具，增强指纹精度、弱口令爆破与结果标准化输出，适配复杂内网）  
  
- RingQ加载器二开版（二开优化免杀加载器，支持Shellcode内存执行，绕过各类终端防护与EDR检测）  
  
- 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护，适配不同Web场景）  
  
- 免杀360专属加载器（支持Shellcode内存执行，针对性绕过360全系防护检测，无感知运行）  
  
- 一键Kill 火绒 defender 工具 **HDKiller**  
（包含源码）  
  
- win11 一键kill 360工具 **InjectKill**  
（包含源码）  
  
- win11 一键kill defender工具**win11_df-killer**  
（包含源码）  
  
后续将不断更新到内部圈子中 欢迎加入圈子 ![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lo4VYgFZveMP6cicgNY1qasdfdJ3seRZVv5nUsD4kpZ1pEAHxBE7tkkgIEULhQXZciaYanCribseulg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "image")  
![image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2nhghttp9mQhic3LJWsCj8Jb4QWibnjmRqic7M9W746srJZlLKQg6mmV7cKrwhWCOauLlJPzLzry0iaRQ/640?wx_fmt=jpeg&from=appmsg&watermark=1#imgIndex=7 "image")  
  
  
