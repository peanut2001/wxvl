#  通过补丁对比分析 N-day 漏洞  
c0w5lip
                    c0w5lip  securitainment   2026-02-09 13:31  
  
<table><thead><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">原文链接</span></section></th><th style="font-weight: bold;border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">作者</span></section></th></tr></thead><tbody><tr style="border-top-width: 1px;border-top-style: solid;border-top-color: rgb(204, 204, 204);background-color: white;margin: 0px;padding: 0px;"><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">https://c0w5lip.github.io/posts/2026-01-25-patch-diffing-introduction/</span></section></td><td style="border: 1px solid rgb(204, 204, 204);text-align: left;margin: 0px;padding: 6px 13px;"><section><span leaf="">c0w5lip</span></section></td></tr></tbody></table>## 介绍  
  
本文旨在快速入门"补丁对比"（Patch Diffing）技术，并通过 CVE-2023-38831 这一影响 WinRAR 的真实漏洞案例进行深入剖析。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/h4gtbB74nSjg0SqVrSPIReiaDqpI6n2Ltrnd8bhdjAny5SuP4TmEhfAmf3p05PYuZ9QxEZNQBJILnIrGiaZk6Hib8yu67QCHMFn4A0HBea5jLg/640?wx_fmt=gif&from=appmsg "")  
### 什么是补丁对比？  
  
补丁对比是一种比较两个二进制版本差异的过程，分别为应用补丁前后的二进制文件。通过对这两个版本进行逐段对比，可以识别出修复过程中的所有代码变化。  
### 为什么要进行补丁对比？  
  
（非详尽列表）：  
1. **一日漏洞利用**  
：供应商通常在修补漏洞时不提供任何细节，甚至不提及漏洞的存在。补丁对比允许研究人员反向工程出漏洞，从而开发仍然有效的利用代码。  
  
1. **绕过补丁**  
：应用于漏洞的补丁可能存在缺陷。因此可以尝试绕过补丁来利用相同的漏洞，或甚至发现由补丁修改衍生出的新漏洞。  
  
### 如何进行补丁对比？  
1. 使用 Diaphora 或 BinDiff 等工具将二进制文件导出到数据库中。  
  
1. 对数据库进行对比  
  
1. 筛选和审查对比结果  
  
1. 发现有趣的代码变化  
  
1. 从这些变化中识别潜在的可利用内容  
  
### 个人看法  
  
我一直以来主要从事逆向工程工作，因此对二进制对比这项技术感到得心应手，因为它本质上仍然是逆向工程的延伸。我认为通过对比学习来识别漏洞而不被大量代码所淹没，是一项很好的训练。  
## 案例研究：WinRAR  
  
我们存例分析两个连续版本的著名压缩工具 WinRAR。  
  
为了演示目的，我们假设最新版本是 6.23，之前的版本为数月前发布的 6.22。  
### 获取二进制文件  
  
如果想追上补丁对比学习，你可能需要浮事 curated 的、安全的羗件下载库来获取旧版本羗件。我们选择了 Filepuma。  
### 分析过程  
  
下仪将应用了补丁的 WinRAR.exe  
可执行文件在 IDA Pro 9.2 中打开，並使用 Diaphora 将它导出到 SQLite 数据库中。正式引用时，应确保【不勾选】微代码生成选项，因为它不是必需的，且会显著低下处理效率。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSg2G1o6eAkljn3hfKnKwWhia2j9Fmk7DlB0jWogNApWVY1kMcpwCLWhuLlf3DGiaGM9LStWs56BJnrkygbFLS6lK2bdCjE2GOHFk/640?wx_fmt=png&from=appmsg "")  
  
一旦处理完成，我们可以打开来自同一二进制的**未补丁**  
版本，然后与已补丁的数据库进行导出和对比。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/h4gtbB74nSgeC3u85qECicWboGKQX4g1xGBcUlWB3ibQ1SNJItmzHpYNvc9ge8pqYlKkvGCozjAIribXVpGpbxIvxhNd4V4XAVEtSlniaa2P7Bc/640?wx_fmt=png&from=appmsg "")  
  
最终，各种对比结果视图会出现，其中我们重点关注**部分匹配**  
（Partial Matches）这一项。  
  
因为存在数量相当多的函数，我们可以根据两个条件来缩小候选范围：**新增基本块的数量**  
和**相似度比率**  
。为漏洞添加一个简单的 if  
语句作为补丁会导致控制流图中增加数个基本块，这为我们提供了一个关于新增基本块数量的粗略估计。  
  
(1) **相似度比率**  
简单地表示两个函数之间的差异程度（相同函数为 1.0）。我们可以过滤掉相似度过高的函数（如 0.99...），因为它们往往只是汇编层面的微小变化，而不是真正的补丁。  
  
类似的筛选技巧很有用，可以帮助我们节省时间，但整个遍历过程仍然需要发挥直觉、常识和大量深入挖掘。  
  
在查看了几个伪代码对比后，有一个特别引人注目的函数吸引了我们的目光**（第 31 行）**  
。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/h4gtbB74nSiaX3CdzL6BYfT2Qs28xnZQYiaJ4bUBhH8j4KZeZMiakqJlAibWBz5iaHqzOwNwO42QzWq4phia2GR3kv9wYOicdia4jowlFn8tyNxziaW8/640?wx_fmt=png&from=appmsg "")  
  
这段代码实际上会在你在 WinRAR GUI 中打开存档后，双击其中一个文件时执行。  
### 漏洞分析  
  
该代码导致了 CVE-2023-38831。  
  
不过多深入细节，大致过程如下：  
- 为 SHELLEXECUTEINFOW 结构体实例 (pExecInfo  
) 设置参数  
  
- WinRAR 尝试执行用户点击的文件 (v12 = ShellExecuteExW(&pExecInfo);  
)  
  
问题在于 ShellExecuteExW() 在遇到模糊路径时具有特殊的行为。  
  
结构体的一个字段是 lpVerb  
，它"指定要执行的操作"。出于**任何失败原因**  
，WinRAR 在首次调用失败后会重试执行，并设置 lpVerb = 0  
：  
```
v12 = ShellExecuteExW(&pExecInfo);if (!v12) # ShellExecuteExW 失败{    ...if (pExecInfo.lpVerb) # lpVerb 已设置？    {        pExecInfo.lpVerb = 0; # lpVerb 被清空        v12 = ShellExecuteExW(&pExecInfo); # 使用清空的 lpVerb 重新尝试执行函数    }}
```  
  
当 pExecInfo.lpVerb = 0  
时，观察到的 Windows Shell 行为表现出更宽松的路径解析启发式。  
  
如果我们创建一个名为 evil.pdf  
的文件（带有尾随空格）和一个同名文件夹，其中包含名为 evil.pdf .cmd  
的脚本，尾随空格会暗中使 PDF 扩展名失效（Windows 找不到打开该文件的应用程序）。这会导致 ShellExecuteExW()  
失败。  
  
然而，我们已经评估过这个失败会导致 lpVerb  
被清空，并使用新参数再次调用 ShellExecuteExW()  
（尽管失败与 lpVerb  
无关！）。在这种情况下，Windows Shell 会表现出以下行为：它会查找同名的文件夹（evil.pdf /  
），并自动执行该目录中的任何脚本文件（即 evil.pdf .cmd  
）。  
### 补丁方案  
  
添加了一项检查（if (GetLastError() != 1155)  
）来防止在首次尝试返回**ERROR_NO_ASSOCIATION**  
（1155）时再次执行 ShellExecuteExW()  
。  
  
因此，补丁的焦点在于修复逻辑而非清理输入。  
### 漏洞利用？  
  
我编写了自己的漏洞利用代码，但考虑到法律问题，决定在此篇中删除这部分。利用这一漏洞弹出计算器只需 Python 的 4 行代码，你可以自己尝试。  
```
CVE-2023-38831.zip├── evil .pdf  （带有尾随空格的文件）└── evil .pdf  （文件夹）    └── evil.pdf .cmd （有效载荷）
```  
### 动态分析 vs 静态理论  
  
我们刚才的评估认为有效载荷是在第二次调用 ShellExecuteExW()  
（重试）时执行的。然而，如果你调试 WinRAR，你会发现有效载荷实际上是在首次调用时执行的。这表明 Windows Shell API 的行为比之前想象的更"激进"：它直接注意到了模糊路径，并在函数返回错误之前就已经搜索了我们的目录。  
## 总结  
### 开场  
  
我的朋友 nasm 转发给我一篇关于 AI 辅助补丁对比分析的文章，如果你觉得本文有趣，定会喜欢那篇。  
### 补充资源  
- https://diffing.quarkslab.com/exporter/binexport.html  
  
- https://www.orangecyberdefense.com/be/blog/introduction-to-binary-diffing-part-3  
  
本文仅用于教育和防御性研究目的。请勿在未获得明确授权的系统上尝试复现漏洞利用代码。用户应更新 WinRAR 至 6.23 或更高版本以缓解本文所述的问题。  
  
---  
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。  
  
  
  
