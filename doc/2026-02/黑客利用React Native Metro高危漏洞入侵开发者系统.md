#  黑客利用React Native Metro高危漏洞入侵开发者系统  
胡金鱼
                    胡金鱼  嘶吼专业版   2026-02-13 06:00  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif "")  
  
黑客正针对开发者群体发起攻击，其手段是利用React Native框架Metro服务器中编号为CVE-2025-11953的高危漏洞，向Windows与Linux系统投放恶意载荷。  
  
在Windows系统环境下，未授权攻击者可借助该漏洞，通过发送POST请求执行任意操作系统命令；而在Linux和macOS系统中，该漏洞则可能导致攻击者在有限参数控制的前提下，运行任意可执行文件。  
  
Metro是React Native项目的默认JavaScript打包工具，是应用开发阶段构建和运行程序的核心组件。  
  
默认情况下，Metro会绑定外部网络接口，并开放仅供开发调试使用的HTTP端点（/open-url），以满足本地开发需求。   
  
研究人员发现了这一漏洞，并于去年11月初对外披露。漏洞公开后，多个概念验证（PoC）利用程序随即出现。  
  
据悉，该漏洞的根源在于Metro服务器的/open-url HTTP端点会接收POST请求中用户提交的URL参数，且该参数未经任何安全清理，便直接传递给系统的open()函数执行。  
  
该漏洞影响范围覆盖@react-native-community/cli-server-api工具的4.8.0至20.0.0-alpha.2版本，官方已在20.0.0及后续版本中完成漏洞修复。   
  
2025年12月21日，有威胁者开始利用这一漏洞发起攻击，该攻击活动被命名为Metro4Shell。此后在次年1月4日和21日，攻击者仍在通过该漏洞投放相同的恶意载荷。   
  
攻击者已通过该漏洞在Linux和Windows平台成功投递高级恶意载荷，这表明Metro4Shell已成为一种切实可行的跨平台初始访问手段。  
  
研究人员发现，在这三次攻击中，攻击者均将经过Base64编码的PowerShell恶意载荷隐藏在恶意请求的HTTP POST请求体中，发送至暴露在外的Metro服务器端点。  
  
这些载荷解码并启动后，会执行以下一系列恶意操作：  
  
1.禁用终端防护：调用Add-MpPreference命令，将当前工作目录和系统临时目录添加至微软 Defender 的排除路径，躲避查杀；  
  
2.获取后续载荷：与攻击者控制的服务器建立原始TCP连接，发送GET /windows请求以获取下一阶段的恶意程序；  
  
3.写入恶意文件：将接收的数据写入系统临时目录，保存为可执行文件；  
  
4.执行恶意程序：运行下载的二进制文件，并附带一段由攻击者指定的超长参数字符串。   
  
此次攻击中投放的Windows平台载荷，是一个基于Rust语言开发、经UPX加壳处理的二进制文件，内置基础反分析逻辑。攻击者控制的同一服务器中，还存放有对应的Linux平台恶意程序，可见该攻击活动同时覆盖两大主流操作系统。   
  
据扫描数据显示，目前暴露在公网环境中的React Native Metro服务器约有3500台。 尽管该漏洞已被攻击者持续利用超过一个月，但在漏洞利用预测评分系统中，其风险评分仍处于较低水平。  
  
研究人员强调：“企业切不可等待该漏洞被列入CISA已知被利用漏洞目录、厂商发布相关通报或行业形成广泛共识后，才采取防护措施。”  
  
参考及来源：  
https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-react-native-metro-bug-to-breach-dev-systems/  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fHEm7hZn9HKz9htsveHsW8hSSqNurYXc2Ysqclgt7WOTd3TU11miaxXoAiaMaiadBmayvFq4gJ6kAk8owHrZ4IRztph9cw5XGpxyDZCGjaemS4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fHEm7hZn9HLNxwbyQFS2r2icPa97KlnPaQVjloibG703mwF9GYzjOZeiacjIlTibmW9DwOB0s3Zde6GcIZ3n1S0wqxEtfNaZJ2ibsC6FK71w0d9U/640?wx_fmt=png&from=appmsg "")  
  
  
