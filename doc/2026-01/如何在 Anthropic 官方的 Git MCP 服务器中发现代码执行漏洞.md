#  如何在 Anthropic 官方的 Git MCP 服务器中发现代码执行漏洞  
原创 骨哥说事
                    骨哥说事  骨哥说事   2026-01-22 05:57  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf="">声明：</span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf="">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></h1></td></tr></tbody></table>#   
  
#   
  
****# 防走失：https://gugesay.com/archives/5193  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg "")  
  
# 摘要  
  
**事件概述：**  
  
Cyata 的安全研究团队在 mcp-server-git 中发现了三个安全漏洞，该服务器是由 Anthropic 官方维护的 Git MCP 服务器。这些漏洞可通过提示注入 (prompt injection) 被利用。这意味着，如果攻击者能够影响人工智能助手所读取的内容（例如通过恶意的 README 文件、被篡改的 Issue 描述或被入侵的网页），他们便能在无需直接访问受害者系统的情况下利用这些漏洞。  
  
**影响范围：**  
  
这些漏洞允许具备提示注入能力的攻击者：  
  
•   在结合文件系统 MCP 服务器使用时执行任意代码  
  
•   删除系统中的任意文件  
  
•   将任意文件读取到大型语言模型（LLM）的上下文中（尽管并非直接外泄数据）  
  
重要性： 这些漏洞影响了 Anthropic 官方的 MCP 服务器，即由 MCP 协议创造者维护的参考实现。与先前一些需要特定配置才能利用的发现不同，这些漏洞在默认配置下即可生效。  
  
**受影响用户：**  
  
使用 2025年12月18日 之前版本 mcp-server-git 的用户应立即更新至最新版本。  
  
**漏洞总结：**  
  
•   CVE-2025-68143 – 未受限制的 git_init  
  
•   CVE-2025-68145 – 路径验证绕过  
  
•   CVE-2025-68144 – git_diff 中的参数注入  
# 什么是 MCP？  
  
模型上下文协议 (Model Context Protocol，简称 MCP) 是 Anthropic 于 2024 年 11 月推出的一个开放标准。它为 AI 助手（如 Claude Desktop、Cursor、Windsurf 等）提供了一种统一的方式来与外部工具及数据源交互，这些数据源包括文件系统、数据库、API 以及 Git 等开发工具。  
  
MCP 服务器是一种向 AI 暴露这些功能的程序，充当了 LLM 与外部系统之间的桥梁。  
  
这种架构引入了一个关键的安全考量：MCP 服务器基于 LLM 的决策执行操作，而 LLM 本身可能通过提示注入被操纵。 能够影响 AI 上下文（context）的恶意行为者，可以触发使用攻击者控制参数的 MCP 工具调用。  
# 发现过程  
  
在加入 Cyata 初期，该团队的研究人员正在研究 MCP，并希望了解官方服务器的工作原理，于是开始阅读其代码。  
  
mcp-server-git 的代码结构相当直接。其典型配置如下：  
```
"mcpServers": {  "git": {    "command": "uvx",    "args": ["mcp-server-git", "--repository", "path/to/git/repo"]  }}
```  
  
配置后，用户便可调用基本的 git 命令，如 git_add、git_commit、git_log、git_diff 等。  
  
当时，当调用 mcp-server-git 中的一个工具时，代码逻辑如下：  
```
@server.call_tool()async def call_tool(name: str, arguments: dict) -> list[TextContent]:        repo_path = Path(arguments["repo_path"])        if name == GitTools.INIT:           ....        # 对于所有其他命令，我们需要一个已存在的仓库        repo = git.Repo(repo_path)        match name:            case GitTools.STATUS:                ...            case GitTools.DIFF_UNSTAGED:                ...            case GitTools.DIFF_STAGED:                ...
```  
  
问题在于：repo_path 直接取自 arguments["repo_path"]，而从未与配置中通过 --repository 标志指定的路径进行比较或验证。服务器只是直接使用了接收到的路径。  
  
这意味着攻击者可以访问系统上任何 git 仓库，而不仅仅是 --repository 配置指定的那个。  
  
基于这一发现，Cyata 团队开始深入分析 mcp-server-git。他们发现 git_init 工具存在同样的问题：根本没有路径验证。它可以在文件系统的任何目录中创建新的 git 仓库。  
  
将这两者结合起来，形成了一个强大的攻击原语 (primitive)：攻击者可以获取任意目录（例如 /home/user/.ssh），使用 git_init 将其转换为 git 仓库，然后使用 git_log 或 git_diff 读取其内容。这些文件随后会被加载到 LLM 的上下文中，实际上是将敏感数据泄露给了 AI。  
  
此时，Cyata 通过 HackerOne 向 Anthropic 报告了这一发现。然而，报告最初未被接受，因此该团队继续深入研究，以寻找更具直接影响的利用方式。（详细时间线见文末。）  
  
git_diff 参数注入 (CVE-2025-68144)  
  
在此期间，研究人员发现了 git_diff 函数的问题：  
```
def git_diff(repo: git.Repo, target: str, context_lines: int = DEFAULT_CONTEXT_LINES) -> str:    return repo.git.diff(f"--unified={context_lines}", target)
```  
  
target 参数被直接传递给了 git 命令行，没有任何净化处理。这意味着可以注入任何 git 标志，包括 --output，该标志会将 diff 结果写入文件。  
  
例如：  
```
{  "name": "git_diff",  "arguments": {    "repo_path": "/home/user/repo",    "target": "--output=/home/user/.bashrc"  }}
```  
  
其结果是，diff 输出（在大多数情况下为空）会覆盖目标文件，这实现了任意文件删除。  
  
利用 git_init  
 进行文件删除  
  
该团队仍然认为最初的 git_init  
 和 repo_path  
 绕过可能导致更严重的问题。  
  
他们意识到，攻击者也可以通过一些 git 技巧实现文件删除：  
  
假设目标文件是 /home/user/.ssh/authorized_keys  
，攻击步骤可以是：  
1. 在 /home/user/.ssh  
 目录执行 git_init  
  
1. 执行 git_commit  
 创建初始提交  
  
1. 执行 git_branch  
 创建新分支  
  
1. 执行 git_add authorized_keys  
  
1. 在新分支上执行 git_commit  
  
1. 执行 git_checkout  
 切回原始分支  
  
这样，文件就会从工作目录中消失（尽管它仍然存储在 .git 目录中）。  
  
利用 git_init  
 实现代码执行  
  
利用 git_init  
，攻击者可以在文件系统的任何位置创建 git 仓库。但要实现代码执行，还需要额外的能力：写入文件。  
  
mcp-server-git 的一个常见应用场景是 AI 驱动的 IDE，如 Cursor、Windsurf 或 GitHub Copilot。在这些环境中，AI 通常有两种方式可以写入文件：  
1. 文件系统 MCP 服务器 – Anthropic 官方的文件操作 MCP 服务器  
  
1. IDE 内置的文件写入功能 – IDE 原生内置的文件写入能力  
  
大多数设置至少启用了其中一种。（注：如今其中一些路径受到了更多限制，但当时并非如此。）  
  
该团队最初的想法是利用 git hook，将恶意脚本写入 .git/hooks/pre-commit。但这行不通，因为 Git hook 需要有执行权限，而无论是文件系统 MCP 服务器还是 IDE 的文件写入器，都不会设置执行位。  
  
于是，他们开始梳理 git 的功能，寻找任何无需执行权限就能执行代码的特性。最终，他们找到了涂抹过滤器与清除过滤器 (smudge and clean filters)。  
  
Git 有一个功能，可以在 .git/config  
 中配置过滤器，当文件被暂存 (clean) 或检出 (smudge) 时，这些过滤器会执行 shell 命令。关键在于：这些过滤器是直接通过 shell 执行的，不需要任何文件具有执行权限。  
# 完整攻击链：  
1. 使用 git_init  
 在可写目录中创建仓库  
  
1. 使用文件系统 MCP 服务器写入一个恶意的 .git/config  
 文件，其中包含一个清除过滤器 (clean filter)  
  
1. 写入一个 .gitattributes  
 文件，将该过滤器应用于特定文件  
  
1. 写入一个包含有效Payload的 shell 脚本  
  
1. 写入一个触发过滤器的文件  
  
1. 调用 git_add  
，清除过滤器被执行，从而运行攻击者的有效Payload  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlx0WosRbkZaYaJlNJY4ECHNhE3ssJWSicI6TJqdwsbsblLzjnGiba9l6abh6yibESo6LiaOjWmVnFKiag/640?wx_fmt=png&from=appmsg "")  
# 时间线  
  
2025年6月24日 – Cyata 通过 HackerOne 向 Anthropic 提交初始报告（涉及 repo_path 未检查和 git_init 文件泄露）。  
  
2025年6月25日 – Anthropic 将报告标记为"信息性 (informative)"。  
  
2025年7月6日 – Cyata 提交第二份报告，补充了 git_diff 参数注入和代码执行的发现。  
  
2025年7月24日 – Anthropic 重新开启了报告。  
  
2025年9月10日 – 报告被 Anthropic 接受。  
  
2025年12月17日 – 分配 3 个 CVE 编号，并提交修复补丁。  
# 补救措施  
  
•   将 mcp-server-git 更新至 2025年12月18日 或更高版本  
  
•   审计哪些 MCP 服务器会一起运行——组合使用 Git 和文件系统服务器会增加攻击面  
  
•   监控非仓库文件夹中是否出现意外的 .git 目录  
  
原文：https://cyata.ai/blog/cyata-research-breaking-anthropics-official-mcp-server/  
  
- END -  
  
**感谢阅读，如果觉得还不错的话，动动手指一键三连～**  
  
