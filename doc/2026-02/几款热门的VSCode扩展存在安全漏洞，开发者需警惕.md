#  几款热门的VSCode扩展存在安全漏洞，开发者需警惕  
 幻泉之洲   2026-02-27 01:43  
  
> 几款累计下载量超过1.28亿次的热门VSCode扩展被曝存在高危漏洞，攻击者可能借此窃取本地文件甚至远程执行代码。安全研究人员自去年6月起试图联系维护者却未获回应，建议开发者检查并卸载不必要的扩展。  
  
  
几款在Visual Studio Code里相当受欢迎的扩展出了安全问题，有些漏洞评级挺高。它们加起来被下载了超过1.28亿次，这些漏洞可能让坏蛋偷走你电脑里的文件，或者在远程直接运行恶意代码。  
  
出问题的扩展包括Code Runner、Markdown预览增强版，还有微软自家的Live Preview。发现这些问题的是应用安全公司Ox Security的研究人员，他们从2025年6月就开始想办法联系这些扩展的维护者来报告漏洞，但据他们说，一直没人搭理。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdzqU2wkILLYmBY1wzKj9TibW6dicShlyDe84iaPzyTgr3TFdqYiacia7kqOT1ZAh0Vs5gpQIase71FkRqnbuftP82mqwgFrfV1hoh8/640?wx_fmt=jpeg&from=appmsg "")  
## 开发工具里的危险“后门”  
  
VSCode扩展其实就是给这个微软的代码编辑器增加功能的插件，比如支持新的编程语言、加个调试工具、换换界面主题什么的。正因为要给编辑器“赋能”，这些扩展通常拥有很高的权限，能接触到你的本地文件、终端命令和网络资源。  
  
Ox Security针对每个漏洞都发了详细报告。他们警告说，如果在公司环境里还留着这些有问题的扩展，可能会把整个内网都暴露在风险之下。攻击者可以借此在内部网络里横着走，偷数据，甚至完全控制你的系统。  
  
具体来看，其中几个漏洞挺吓人的：  
- Live Server扩展有个严重漏洞。这个扩展有超过7200万次安装，攻击者可以诱导你访问一个恶意网页，然后利用这个漏洞把你电脑里的本地文件偷走。相关报告[1]  
  
- Code Runner扩展的漏洞允许远程执行代码。它有3700万次下载。攻击方法有点“社会工程学”——骗你在一个叫settings.json  
的全局配置文件里，粘贴或者应用一段动过手脚的配置代码。相关报告[2]  
  
- Markdown预览增强版扩展的漏洞评分为8.8分（满分10分），属于高危。它有850万次下载。问题出在它能通过一个精心构造的Markdown文件来执行JavaScript代码。相关报告[3]  
  
- Microsoft Live Preview扩展在0.4.16版本之前存在一个“一键触发”的跨站脚本漏洞。这个扩展安装了1100多万次，攻击者可以利用这个漏洞访问开发者电脑上的敏感文件。相关报告[4]  
  
需要特别注意的是，这些安全问题不光影响VSCode本身。因为Cursor和Windsurf这两个新兴的、主打AI编程助手的代码编辑器，本质上跟VSCode是兼容的，所以用这两个编辑器的人，如果装了同样的扩展，也一样有风险。  
## 普通开发者现在该做些什么？  
  
研究人员报告里提了一些挺实际的建议。老实说，有些习惯我们自己可能也没太注意。  
  
首先，尽量不要随便运行本地主机服务器（localhost server）。如果非跑不可，那就别在浏览器里打开那些你信不过的HTML页面。其次，别轻易把来路不明的配置代码片段，往settings.json  
文件里粘贴。这个操作风险比想象中大。  
  
最直接的应对办法，就是去检查一下你的VSCode（或者Cursor/Windsurf）都装了哪些扩展。把那些用不着的、或者不咋更新的扩展给卸载了。安装新扩展时，尽量选那些信誉好的发布者。平时也多留个心眼，看看编辑器设置有没有自己“变”出什么奇怪的东西。  
  
报告里也说了，攻击者利用这些漏洞，不光能偷文件，还可能顺走你的API密钥、数据库配置文件这类更敏感的东西，然后在你的网络里找机会干更多坏事。  
  
到现在，这些漏洞的维护者还没做出公开回应和修复。所以，如果你在用上面提到的这几款扩展，最好自己先采取行动，别干等着。  
### 参考资料  
  
[1]   
https://www.ox.security/blog/cve-2025-65717-live-server-vscode-vulnerability/  
  
[2]   
https://www.ox.security/blog/cve-2025-65715-code-runner-vscode-rce/  
  
[3]   
https://www.ox.security/blog/cve-2025-65716-markdown-preview-enhanced-vscode-vulnerability/  
  
[4]   
https://www.ox.security/blog/xssinlivepreview/  
  
[5]   
https://www.bleepingcomputer.com/news/security/flaws-in-popular-vscode-extensions-expose-developers-to-attacks/  
  
