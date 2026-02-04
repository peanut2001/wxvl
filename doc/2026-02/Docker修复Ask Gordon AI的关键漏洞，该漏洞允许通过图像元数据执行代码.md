#  Docker修复Ask Gordon AI的关键漏洞，该漏洞允许通过图像元数据执行代码  
会杀毒的单反狗
                    会杀毒的单反狗  军哥网络安全读报   2026-02-04 01:01  
  
**导****读**  
  
  
  
网络安全研究人员披露了一个已修复的安全漏洞的细节，该漏洞影响内置于 Docker Desktop 和 Docker 命令行界面 (CLI) 中的人工智能 (AI) 助手Ask Gordon ，该漏洞可能被利用来执行代码和窃取敏感数据。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHWZgtibnXIiaClm1tUdiaBAtcQnOAXmIHkljyGo0RHBUsdtBl6FiaibyRBfLhpgn832LIZUnmJRLOczYg/640?wx_fmt=png&from=appmsg "")  
  
  
网络安全公司 Noma Labs将这一严重漏洞命名为DockerDash。Docker在 2025 年 11 月发布的4.50.0 版本中修复了该漏洞。  
  
  
Noma 的安全研究主管 Sasi Levi 在一份报告中表示：“在 DockerDash 中，Docker 镜像中的一个恶意元数据标签可以通过简单的三阶段攻击来破坏您的 Docker 环境：Gordon AI 读取并解释恶意指令，将其转发到MCP（模型上下文协议）网关，然后通过 MCP 工具执行该指令。”  
  
  
“每个阶段都无需任何验证，充分利用了现有代理和 MCP 网关架构。”  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AnRWZJZfVaHWZgtibnXIiaClm1tUdiaBAtcXx8RLjcHib2TBF0t6C1ibOhKxJQUj6iaiaMgw2w0eaicJXiaaUABjqSQN0Qw/640?wx_fmt=png&from=appmsg "")  
  
  
成功利用该漏洞可能导致对云和 CLI 系统造成严重影响的远程代码执行，或对桌面应用程序造成严重影响的数据泄露。  
  
  
Noma Security指出，问题在于人工智能助手会将未经验证的元数据视为可执行命令，使其无需任何验证即可在不同层级间传播，从而使攻击者能够绕过安全边界。最终结果是，一个简单的AI查询就可能为工具执行打开方便之门。  
  
  
由于 MCP 作为大型语言模型 (LLM) 与本地环境之间的连接纽带，问题在于上下文信任的缺失。该问题被定义为元上下文注入。  
  
  
Levi表示：“MCP网关无法区分信息性元数据（例如标准的Docker标签）和预先授权的可运行内部指令。攻击者可以通过在这些元数据字段中嵌入恶意指令来劫持人工智能的推理过程。”  
  
  
在假设的攻击场景中，攻击者可以利用 Ask Gordon 解析容器元数据时存在的关键信任边界漏洞。为此，攻击者会精心构造一个恶意 Docker 镜像，并在 Dockerfile 的 LABEL 字段中嵌入恶意指令。  
  
  
虽然元数据字段看似无害，但当 Ask Gordon AI 处理它们时，它们就变成了注入漏洞的途径。代码执行攻击链如下：  
- 攻击者发布了一个 Docker 镜像，该镜像的 Dockerfile 中包含恶意 LABEL 指令。  
- 当受害者向 Ask Gordon AI 查询图像信息时，Gordon 会读取图像元数据，包括所有 LABEL 字段，利用 Ask Gordon 无法区分合法元数据描述和嵌入的恶意指令这一漏洞。  
- 请 Gordon 将解析后的指令转发给 MCP 网关，这是一个位于 AI 代理和 MCP 服务器之间的中间件层。  
- MCP 网关将其解释为来自可信来源的标准请求，并直接调用指定的 MCP 工具，无需任何额外验证。  
- MCP 工具以受害者的 Docker 权限执行命令，从而实现代码执行。  
该数据泄露漏洞利用了相同的提示注入缺陷，但目标是 Ask Gordon 的 Docker Desktop 实现，通过利用助手的只读权限，使用 MCP 工具捕获有关受害者环境的敏感内部数据。  
  
  
收集到的信息可以包括已安装工具的详细信息、容器详细信息、Docker 配置、挂载目录和网络拓扑结构。  
  
  
Levi表示：“DockerDash漏洞凸显将人工智能供应链风险视为当前核心威胁的必要性。它证明，您信任的输入源可能被用来隐藏恶意载荷，从而轻易操纵人工智能的执行路径。要缓解这类新型攻击，需要对提供给人工智能模型的所有上下文数据实施零信任验证。”  
  
  
详细漏洞分析：  
  
《DockerDash：两条攻击路径，一场人工智能供应链危机》  
  
https://noma.security/blog/dockerdash-two-attack-paths-one-ai-supply-chain-crisis/  
  
  
新闻链接：  
  
https://thehackernews.com/2026/02/docker-fixes-critical-ask-gordon-ai.html  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/AnRWZJZfVaGC3gsJClsh4Fia0icylyBEnBywibdbkrLLzmpibfdnf5wNYzEUq2GpzfedMKUjlLJQ4uwxAFWLzHhPFQ/640?wx_fmt=jpeg "")  
  
扫码关注  
  
军哥网络安全读报  
  
**讲述普通人能听懂的安全故事**  
  
  
