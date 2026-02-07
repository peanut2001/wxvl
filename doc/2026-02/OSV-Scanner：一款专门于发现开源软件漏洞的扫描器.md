#  OSV-Scanner：一款专门于发现开源软件漏洞的扫描器  
 sec0nd安全   2026-02-07 12:15  
  
**更多干货  点击蓝字 关注我们**  
  
  
  
**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**  
  
**往期回顾**  
  
  
  
  
  
  
·[LingOps（灵控）：AWD/AWDP 竞赛自动化平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486227&idx=1&sn=c7183a4926281db23003d3e02010fd8f&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[融合AI引擎的日志应急响应溯源工具SSLogs--详细配置教程与使用方法](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486211&idx=1&sn=b6893a457752881cbef64eb8f685e0fb&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[AWD-H1M：AWD攻防竞赛自动化工具箱](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486193&idx=1&sn=0d299367f73c1a711d810af55196a275&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[DumpGuard：首个公开绕过Windows Credential Guard的凭据提取工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486180&idx=1&sn=c8e5f47564ce29bf0435b6bba13828a1&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[FingerprintHub：识别网站和网络服务背后使用的技术栈](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486175&idx=1&sn=ff7c227b167f27367150e9f9d481be57&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[data-cve-poc：近两年的漏洞CVE-POC合集](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486159&idx=1&sn=d4788941d37418ed052eefd317ae631c&scene=21#wechat_redirect)  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**介绍**  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIrnr1WD0X4Ol9q7eldrXmhgc1dliaRKiawhD7z12A7ro4LgQzXcfWDvG5Y7tIxe6XHDzhIYzvJ8YcTSFWkBu3yQRyxgC1l2vaIE/640?wx_fmt=png&from=appmsg "")  
  
  
     OSV-Scanner 是基于 OSV.dev 漏洞库的 SLSA3 合规工具，通过 SBOM 解析、依赖遍历实现软件供应链的 CVE/OSV 漏洞扫描，支持锁文件、容器镜像等多源输入，输出 CVSS 评分与修复版本映射。  
  
       其核心能力包括递归扫描、离线漏洞库同步、HTML 报告可视化，可集成 Pre-Commit 钩子实现 CI/CD 前置风险拦截，覆盖 npm/Go/Maven 等主流包管理生态。  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**安装**  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLHibxdTnI3j80kj5DLHX1B89BPHc6udBd1e3xqcvGhKxzk4LmHTmy4ibMTSOUwNiayja4pEUAkhEm4r6ZwYj3106mIasxSVePVWc/640?wx_fmt=png&from=appmsg "")  
  
文末链接跳转github,在release界面下载对应文件，也可以直接下载文末百度网盘分享的文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKMP6zkbHxQhTLKbnnVljdPMl8goByrHORjNSiadkXA7PTicbv24uibZicqg7Niap33dEWYBz270X96mID01UhJqcw9ic5qK2nBDydDU/640?wx_fmt=png&from=appmsg "")  
  
一般来说windows上下载我框选的这个就可以  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIkggzmRqUxaqU92KufgtJ4hzibMTmiclwRkdn423qk8SeiaiaplstytibIbJlh4PlRycomxFG38iaRNtVoYbPYZHMQUZ9tibXkib3WD4g/640?wx_fmt=png&from=appmsg "")  
  
下载以后双击只会闪一下，因为没有指定参数。  
  
我们需要把它添加进环境变量，这样就可以直接在命令行调用了  
  
设置搜索编辑系统环境变量，按照图示点击并在path中添加exe文件所在路径，比如说我的是  
D:\wangan\OSVscanner  
  
，那我就填  
D:\wangan\OSVscanner  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLlspBicjzUmTMYw4FGDD508ibFfzKGTcWcvfyWcPtzEn30NEYrdFTYkDdGG85Lxcg7ibXxPwl3jRyLrhKMGL97nXJ6DhrYQN15OM/640?wx_fmt=png&from=appmsg "")  
  
保存以后就可以在全局使用了  
  
随便打开一个命令行窗口输入  
```
osv-scanner_windows_amd64.exe --version
```  
  
如下所示  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKDmC2ziaHs95Gz4uMiaQXLMibJgXHpjIaXcsibldpdR12q9l07S07Z6YJMiajbsGtobFHCRKRnGTFs2qicic8dZs3dLY67TUvrkMSNA4/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**使用**  
  
  
  
OSV-Scanner 核心流程是「提取包信息 → 匹配漏洞库」，支持扫描源码目录、锁文件、容器镜像等。  
  
1. 基础扫描（源码 / 锁文件）  
  
扫描本地目录（递归）  
```
# 基础用法：扫描当前目录所有依赖
osv-scanner_windows_amd64.exe scan -r ./
# 指定锁文件扫描（如 npm、Go、Maven 等）
osv-scanner_windows_amd64.exe -L package-lock.json  # npm
osv-scanner_windows_amd64.exe -L go.mod            # Go
osv-scanner_windows_amd64.exe scan -L pom.xml           # Maven
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKNdE8QV5xXyOKlIcSdbzMwb47OWvsx0ZQyrNJgJI2fgD2yDib0ayU965poiaQeISmy9HMCQl8MVFaES55FofmQWcw258tf2oQHI/640?wx_fmt=png&from=appmsg "")  
  
  
Docker 容器内扫描  
```
# 挂载当前目录到容器 /src，扫描 go.mod
docker run -v ${PWD}:/src ghcr.io/google/osv-scanner -L /src/go.mod
```  
  
2. 容器镜像扫描  
```
# 扫描本地 Docker 镜像（需安装 Docker）
osv-scanner_windows_amd64.exe scan image my-docker-img:latest
# Docker 方式扫描容器镜像
docker run ghcr.io/google/osv-scanner scan image my-docker-img:latest
```  
  
3. 生成 HTML 报告并本地预览  
```
# 扫描锁文件并在 8000 端口启动 HTML 报告服务
osv-scanner_windows_amd64.exe scan -L package-lock.json --serve
```  
  
访问 http://localhost:8000 即可查看可视化漏洞报告。  
  
 修复指引（实验性）  
  
扫描后可通过 fix 子命令获取修复建议：  
```
osv-scanner_windows_amd64.exe fix -M package.json -L package-lock.json
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKqJ4P7hdEfThSIPicdcAEUTRdzPE5HfuYyI2tREsWXgGLNX1x8qlc5TTDaXibu4dVZEZIo4vcmWmmKJQSu64FMFwFjxIX6hm0ok/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
github链接  
```
https://github.com/google/osv-scanner
```  
  
通过网盘分享的文件：  
  
osv-scanner_windows_amd64.exe  
  
链接:   
  
https://pan.baidu.com/s/12xASVgZZZMidlHZ7VBojWg?pwd=dcvn 提取码: dcvn   
  
--来自百度网盘超级会员v3的分享  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
