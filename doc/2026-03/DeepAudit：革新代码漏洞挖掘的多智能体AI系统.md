#  DeepAudit：革新代码漏洞挖掘的多智能体AI系统  
原创 子午猫
                        子午猫  网络侦查研究院   2026-03-12 00:11  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2bujwd3M0M1ICStsbhAHWtth8dQwoBBFoNDafDAzGbm1sCA8bqVWIjs40A8lu9rtuD4yeOOwDNadg/640?wx_fmt=png "")  
  
  
在当今数字化时代，代码安全至关重要，而高效准确的代码漏洞挖掘工具更是保障软件安全的关键。DeepAudit作为一款基于Multi - Agent协作架构的下一代代码安全审计平台，正凭借其创新的理念和强大的功能，在代码漏洞挖掘领域崭露头角。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0pcA9efn4EM50xHNVDBkRib3sw6z3z8FPXHhEwCZPl65leCULpuC0RLWib8sQKtf30wibdfVdwAgh1ibXz4lT5BDWqpSib5lvCkQtKM/640?wx_fmt=png&from=appmsg "")  
## 0x00项目背景与核心理念  
  
DeepAudit的项目地址为https://github.com/lintsinghua/DeepAudit ，它是国内首个开源的代码漏洞挖掘多智能体系统，已成功在16个知名开源项目中发现48个CVE漏洞，成绩斐然。其核心理念是“让AI像黑客一样攻击，像专家一样防御”，旨在通过模拟安全专家的思维方式，有效解决传统SAST（静态应用安全测试）工具长期存在的三大痛点。  
  
传统SAST工具常常面临高误报率的问题，这主要是因为它们缺乏对代码语义的深入理解。在分析代码时，往往只是机械地匹配规则，而无法真正理解代码的含义，导致大量误报，增加了安全人员的工作负担。同时，传统工具存在业务逻辑盲点，难以理解跨文件调用的复杂关系。在大型项目中，代码分散在多个文件中，文件之间的调用关系错综复杂，传统工具很难全面把握这些关系，从而遗漏一些隐藏在跨文件调用中的漏洞。此外，传统工具还缺乏有效的验证手段，无法确认所发现的漏洞是否具有可利用性，这使得安全人员难以判断漏洞的实际风险。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0qSEL3sJzUfCohDZHWEbcj72pcricuOl17S6HQwgcHwnx2NfxMamtvuFZ7TnNNSRGdEM8uiaWk8yQjiauOpueWTMrJGoVfgw3s7wU/640?wx_fmt=png&from=appmsg "")  
## 0x01核心架构探秘  
  
DeepAudit采用微服务架构，由Multi - Agent引擎驱动，其架构设计精巧，各部分协同工作，实现高效的代码漏洞挖掘。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mQFl6fQOc0oP7UvhbWkAIPtaZZ3aemWliabMib3dFaWdQBQcBZibGy1NtPtMHvJcicpJ7B9YEDdgusariaicydzXu8B5yUm5nINI6JAMLalR17cs0/640?wx_fmt=png&from=appmsg "")  
### 0x0101用户界面层  
  
用户界面基于React + TypeScript构建，为用户提供了一个直观且交互性良好的操作界面。这一设计使得用户能够轻松地与平台进行交互，无论是发起审计任务、查看审计结果还是进行项目管理，都能在这个界面上便捷地完成。例如，用户可以通过简洁明了的菜单和按钮，快速选择要审计的项目，查看实时的审计进度和详细的报告。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mQFl6fQOc0oqEcDwGu2S2eUtb4dv3kRG0IIr2uQ8rMEbwOia6hJ3WEZIygJbjjw2YACtvic3Xj5aAG5bwm8fpP6qmhcyRWlKaDZNQmP6gwwvs/640?wx_fmt=png&from=appmsg "")  
### 0x0102后端服务层  
1. **FastAPI后端框架**  
：后端以Python的FastAPI + Uvicorn为框架，提供了高性能的服务接口。FastAPI以其快速、简洁的特点，能够高效地处理各种请求，确保平台的响应速度。Uvicorn则作为ASGI服务器，进一步优化了后端的性能，使得系统能够稳定地处理大量并发请求。  
  
1. **Multi - Agent系统**  
：核心的Multi - Agent系统由LangGraph + LangChain驱动，包含四个专用智能体，分别在不同阶段发挥关键作用。  
  
1. **Orchestrator Agent**  
：负责策略规划。它首先分析项目类型，根据项目的特点制定详细的审计计划，然后将任务合理地分发给其他智能体。例如，对于一个Java项目和一个Python项目，它会根据不同语言的特性和常见漏洞类型，制定不同的审计策略。  
  
1. **Recon Agent**  
：承担信息收集的重任。它扫描项目结构，识别项目所使用的技术栈，并提取可能的攻击面。比如，它可以确定项目是否使用了特定的Web框架，以及框架版本是否存在已知漏洞，从而为后续的漏洞挖掘提供基础信息。  
  
1. **Analysis Agent**  
：结合RAG（检索增强生成）知识库与AST（抽象语法树）分析，对代码进行深度审查。RAG知识库存储了丰富的CWE（常见弱点枚举）和CVE（公共漏洞和暴露）知识，Analysis Agent利用这些知识以及AST分析代码的结构和语义，更准确地挖掘潜在漏洞。例如，在分析一段代码时，它可以通过AST理解代码的逻辑结构，同时借助RAG知识库判断代码是否存在特定类型的漏洞。  
  
1. **Verification Agent**  
：负责编写并执行PoC（概念验证）脚本，在Docker沙箱环境中验证漏洞的存在性。它会根据Analysis Agent发现的潜在漏洞，生成相应的PoC脚本，并在沙箱中执行，以确认漏洞是否真实可利用。如果验证失败，它还会自动修正PoC并重试，最多可达3次。  
  
1. **向量数据库与相关技术**  
：向量数据库采用ChromaDB作为RAG知识库，用于存储和检索代码语义相关的信息。AST解析使用Tree - sitter，它支持10多种语言，能够准确地将代码解析为抽象语法树，为Analysis Agent的深度审查提供基础。任务队列由Celery + Redis组成，负责管理和调度各种任务，确保系统的高效运行。数据库则选用PostgreSQL 15+，用于存储项目信息、审计结果等重要数据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0o8HQ2HSFvVQMd48ibvOXyoxfibhdfpopicYhxMLIqnbDB4iawoiavrME1iadJbNrgO040iaqwYyPIiazdedUpBK4teFgTdoj99ibIeeHBo/640?wx_fmt=png&from=appmsg "")  
### 0x0103Docker沙箱环境层  
  
这一层提供了一个隔离的Docker沙箱环境，主要用于自动化的PoC测试与验证。每个PoC在独立的Docker容器中运行，通过资源限制（如CPU、Memory配额限制）、网络隔离（沙箱内禁止外网访问，除了SSRF测试）以及文件系统只读挂载等策略，确保测试过程的安全性，防止潜在的逃逸风险。在验证流程中，Verification Agent生成PoC脚本后，沙箱会动态构建目标应用环境，然后在这个隔离环境中执行攻击脚本，捕获响应或异常，以此验证漏洞的存在性。  
## 0x02Multi - Agent工作流详解  
1. **策略规划阶段**  
：Orchestrator Agent首先对项目类型进行深入分析，例如判断项目是Web应用、移动应用还是桌面应用，以及使用的编程语言和框架等。基于这些分析，它制定详细的审计计划，明确各个阶段的任务和目标，并将任务分发给相应的Recon Agent、Analysis Agent和Verification Agent。比如，对于一个基于Django框架的Python Web项目，它可能会安排Recon Agent重点扫描与Django相关的配置文件和视图函数，Analysis Agent针对常见的Django漏洞类型进行分析。  
  
1. **信息收集阶段**  
：Recon Agent接到任务后，开始扫描项目结构。它会遍历项目的文件和目录，识别项目所使用的技术栈，如编程语言、框架、数据库等。同时，提取可能的攻击面，例如Web应用中的URL路径、表单输入点等。以一个Java Spring Boot项目为例，Recon Agent可以确定项目使用的Spring Boot版本，以及项目中暴露的RESTful API端点，这些都可能成为潜在的攻击面。  
  
1. **漏洞挖掘阶段**  
：Analysis Agent结合RAG知识库与AST分析来深度审查代码。它首先通过AST分析代码的语法和逻辑结构，理解代码的功能和执行流程。然后，利用RAG知识库中的CWE和CVE知识，对代码进行比对和分析，查找潜在的漏洞。例如，在分析一段SQL查询代码时，通过AST分析确定代码的查询逻辑，再结合RAG知识库中关于SQL注入的知识，判断是否存在SQL注入漏洞。  
  
1. **PoC验证阶段**  
：Verification Agent根据Analysis Agent发现的潜在漏洞，编写PoC脚本。然后，在Docker沙箱环境中动态构建目标应用环境，将PoC脚本在这个隔离环境中执行。它会捕获执行过程中的响应或异常，如果能够成功触发漏洞相关的行为，如SQL注入成功获取到数据库敏感信息，就可以确认漏洞的存在性。如果验证失败，Verification Agent会自动修正PoC脚本并重试，最多重试3次，以确保验证结果的准确性。  
  
1. **报告生成阶段**  
：Orchestrator Agent汇总各个阶段的结果，对结果进行进一步处理，剔除误报信息。然后，生成专业的审计报告，报告内容包括漏洞详情、危害等级、修复建议等。例如，报告中会详细说明某个SQL注入漏洞的具体位置、可能导致的数据泄露风险，以及如何修改代码来修复该漏洞。  
  
## 0x03技术栈全面解析  
### 0x0301后端技术栈  
1. **框架选择**  
：选用Python FastAPI + Uvicorn作为后端框架，FastAPI的快速开发特性和高效性能，以及Uvicorn的ASGI服务器优势，使得后端能够快速响应各种请求，满足平台在处理大量项目审计任务时的性能需求。  
  
1. **Multi - Agent技术**  
：LangGraph + LangChain为Multi - Agent系统提供了强大的支持。LangGraph负责管理智能体之间的状态转换和协作流程，确保各个智能体按照预定的工作流协同工作。LangChain则提供了丰富的工具和接口，用于与各种语言模型进行交互，使得智能体能够利用语言模型的能力进行代码分析和决策。  
  
1. **向量数据库与AST解析**  
：ChromaDB作为向量数据库，用于存储和检索与代码语义相关的信息，为RAG知识库提供支持。Tree - sitter的多语言支持能力，使得它能够准确地将不同编程语言的代码解析为抽象语法树，为Analysis Agent进行深度代码审查提供了有力的工具。  
  
1. **任务队列与数据库**  
：Celery + Redis组成的任务队列，有效地管理和调度各种任务，确保任务的有序执行。PostgreSQL 15+数据库则用于存储项目的各种信息，包括项目的基本信息、审计结果、用户配置等，为平台的稳定运行提供数据支持。  
  
### 0x0302前端技术栈  
1. **框架与构建工具**  
：前端基于React 18 + TypeScript框架，结合Vite构建工具，提供了高效的开发和构建流程。React的组件化开发模式使得前端界面的开发和维护更加便捷，TypeScript的强类型特性则提高了代码的可读性和可维护性。Vite的快速热重载功能，大大提升了前端开发的效率。  
  
1. **样式与状态管理**  
：采用TailwindCSS + shadcn/ui进行样式设计，提供了简洁美观的界面风格。Zustand用于状态管理，使得前端组件之间能够方便地共享和管理状态。例如，在显示审计进度时，不同的前端组件可以通过Zustand获取和更新进度状态。  
  
1. **图表展示**  
：使用Recharts进行图表展示，能够直观地呈现审计结果中的各种数据，如漏洞数量统计、风险等级分布等，帮助用户更清晰地理解审计结果。  
  
### 0x0303部署技术  
1. **容器化与沙箱**  
：通过Docker + Compose实现容器化部署，将各个服务封装在独立的容器中，便于管理和部署。Docker沙箱环境为PoC测试提供了安全隔离的空间，确保测试过程不会对外部环境造成影响。  
  
1. **镜像仓库**  
：采用GitHub Container Registry (ghcr.io)作为镜像仓库，方便存储和管理项目的Docker镜像，同时也便于在不同环境中进行部署。  
  
## 0x04支持的漏洞类型  
  
DeepAudit支持多种常见且危害较大的漏洞类型，涵盖了从严重到中等危害等级。  
1. **严重危害漏洞**  
：如sql_injection（SQL注入）、command_injection（命令注入）、ssrf（服务端请求伪造）、xxe（XML外部实体注入）、insecure_deserialization（不安全反序列化）、authentication_bypass（认证绕过）、authorization_bypass（授权绕过）等。这些漏洞一旦被利用，可能导致数据库泄露、服务器被控制、敏感信息泄露等严重后果。例如，SQL注入漏洞可能让攻击者获取数据库中的所有用户信息，对企业造成巨大的损失。  
  
1. **中等危害漏洞**  
：包括xss（跨站脚本攻击）、path_traversal（路径遍历）、hardcoded_secret（硬编码密钥）、weak_crypto（弱加密算法）、idor（不安全直接对象引用）等。虽然这些漏洞的危害程度相对较低，但也可能导致用户数据泄露、权限提升等问题。比如，XSS漏洞可能被用于窃取用户的会话 cookie，从而获取用户的登录权限。  
  
## 0x05LLM平台支持  
  
DeepAudit支持多种国际和国内的LLM（大语言模型）平台，同时也支持本地部署。  
1. **国际平台**  
：支持OpenAI的GPT - 4o / GPT - 4 / GPT - 3.5，Anthropic的Claude 3.5 Sonnet / Opus，以及Google的Gemini Pro。这些国际知名的LLM平台具有强大的语言理解和生成能力，能够为代码分析提供有力的支持。例如，GPT - 4在处理复杂的代码语义理解和漏洞分析时表现出色。  
  
1. **国内平台**  
：涵盖阿里的通义千问Qwen、智谱的GLM - 4、月之暗面的Kimi、百度的文心一言、字节的豆包等。国内的LLM平台在中文语境和对国内技术栈的理解上可能具有独特的优势，能够更好地服务于国内用户。  
  
1. **本地部署**  
：支持本地部署多种模型，如Llama3(8B/70B)、Qwen2.5(7B/14B/32B)、DeepSeek - Coder(6.7B/33B)、CodeLlama(7B/13B)等。同时，还支持自定义API Base URL，以解决网络访问限制问题，使得用户可以根据自己的需求选择合适的模型进行本地部署和使用。  
  
## 0x06部署方案详析  
### 0x0601生产环境一键部署（推荐）  
1. **标准部署**  
：用户只需执行命令curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker - compose.prod.yml | docker compose -f - up -d  
，即可完成生产环境的快速部署。这种方式简单快捷，适合对部署流程要求不高，希望快速搭建平台的用户。它会自动从指定的URL下载Docker Compose配置文件，并启动相应的容器，完成平台的部署。  
  
1. **国内加速（南京大学镜像站）**  
：对于国内用户，可能会面临网络访问国外资源缓慢的问题。为此，DeepAudit提供了国内加速方案，通过执行curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker - compose.prod.cn.yml | docker compose -f - up -d  
，从南京大学镜像站下载配置文件进行部署，大大提高了部署速度。部署完成后，用户可以通过http://localhost:3000  
访问平台。  
  
### 0x0602源码开发部署  
1. **克隆代码**  
：首先使用git clone https://github.com/lintsinghua/DeepAudit.git && cd DeepAudit  
命令克隆项目代码到本地，获取平台的源代码。  
  
1. **配置环境变量**  
：复制backend/env.example  
为backend/.env  
，然后编辑.env  
文件，配置LLM API Key等环境变量。LLM API Key的配置决定了平台使用的LLM服务，用户需要根据自己选择的LLM平台获取相应的API Key并进行配置。  
  
1. **启动服务**  
：执行docker compose up -d  
命令启动服务，Docker Compose会根据配置文件启动各个服务容器，完成平台的部署。  
  
### 0x0603源码本地开发  
1. **环境要求**  
：需要Python 3.11+、Node.js 20+、PostgreSQL 15+以及Docker（用于沙箱）。这些环境是平台运行和开发的基础，确保各个组件能够正常工作。  
  
1. **启动步骤**  
：  
  
1. **启动数据库**  
：通过docker compose up -d redis db adminer  
命令启动Redis、PostgreSQL数据库以及Adminer（用于数据库管理）。  
  
1. **后端开发**  
：进入backend  
目录，执行uvsync  
，然后激活虚拟环境source.venv/bin/activate  
，最后使用uvicorn app.main:app --reload  
启动后端服务，并开启热重载功能，方便开发过程中的代码修改和调试。  
  
1. **前端开发**  
：切换到frontend  
目录，执行pnpm install  
安装前端依赖，再使用pnpm dev  
启动前端开发服务器。  
  
1. **沙箱镜像**  
：通过docker pull ghcr.io/lintsinghua/deepaudit - sandbox:latest  
拉取最新的沙箱镜像，为PoC验证提供环境支持。  
  
## 0x07核心功能矩阵解读  
1. **Multi - Agent审计**  
：基于LangGraph状态机实现，能够自主编排审计策略，实现智能体之间的高效协作。不同的智能体在不同阶段发挥作用，共同完成代码审计任务，提高审计的准确性和效率。例如，在面对一个复杂的项目时，各个智能体可以根据项目特点和自身职责，协同完成从信息收集到漏洞验证的全过程。  
  
1. **RAG知识增强**  
：借助ChromaDB和Embeddings技术，实现代码语义理解和CWE/CVE知识检索。ChromaDB存储的向量数据与Embeddings技术相结合，使得平台能够更准确地理解代码的含义，并从知识库中检索相关的漏洞知识，提高漏洞挖掘的准确性。比如，在分析一段代码时，能够准确判断代码的功能，并与知识库中的漏洞模式进行匹配。  
  
1. **沙箱PoC验证**  
：利用Docker隔离和动态执行技术，自动生成并执行攻击脚本。在隔离的Docker沙箱环境中执行PoC脚本，确保验证过程的安全性和可靠性，同时提高了验证的效率。例如，对于发现的潜在SQL注入漏洞，能够在沙箱中模拟攻击过程，验证漏洞是否真实存在。  
  
1. **项目管理**  
：支持通过Git/API/ZIP导入项目，方便用户将GitHub、GitLab、Gitea等平台上的项目导入到DeepAudit进行审计。这种灵活性使得用户可以轻松对不同来源的项目进行安全审计，扩大了平台的适用范围。  
  
1. **即时分析**  
：提供代码片段快速扫描功能，用户只需粘贴代码，即可在秒级时间内得到分析结果。这对于快速检测小段代码的安全性非常有用，例如在开发过程中，开发人员可以随时使用该功能检查自己编写的代码片段是否存在安全隐患。  
  
1. **五维检测**  
：通过规则引擎和AI相结合，实现对Bug、安全、性能、风格、可维护性的全面检测。这种全方位的检测能够帮助用户不仅发现代码中的安全漏洞，还能优化代码的性能、风格和可维护性，提高代码质量。例如，规则引擎可以检查代码是否符合特定的编码规范，AI则可以分析代码中的潜在逻辑问题。  
  
1. **What - Why - How**  
：借助LLM生成解释，实现漏洞定位、原因分析以及修复建议。当发现漏洞时，LLM能够详细指出漏洞在代码中的具体位置，分析漏洞产生的原因，并且给出针对性的修复建议。例如，对于一个SQL注入漏洞，它可以指出具体的SQL语句位置，分析是由于输入验证不当导致的，同时提供正确的输入验证代码示例用于修复。  
  
1. **报告导出**  
：支持一键生成PDF、Markdown、JSON等格式的专业审计报告。不同格式的报告适用于不同的场景，PDF报告适合正式的文档提交和打印，Markdown报告便于在技术社区分享和交流，JSON报告则方便与其他系统进行数据交互。例如，企业在向客户提交安全审计报告时，可以选择PDF格式；开发团队内部交流时，Markdown格式更为便捷。  
  
1. **运行时配置**  
：通过Web UI实现动态配置，用户无需重启服务即可切换LLM。这使得用户可以根据实际需求，灵活选择不同的LLM服务，以适应不同的项目需求和成本预算。比如，在处理对准确性要求极高的项目时，选择功能强大但成本较高的LLM；在日常测试项目中，选择成本较低的LLM。  
  
## 0x08配置说明  
### 0x0801环境变量配置 (backend/.env)  
1. **LLM API配置**  
：OPENAI_API_KEY=sk - xxx  
、ANTHROPIC_API_KEY=sk - ant - xxx  
、DEEPSEEK_API_KEY=sk - xxx  
 等，用户需要根据所使用的LLM平台获取相应的API Key，并填写在此处。这些API Key是平台与LLM服务进行交互的凭证，确保平台能够调用LLM的强大功能进行代码分析。  
  
1. **数据库配置**  
：DATABASE_URL=postgresql://user:pass@localhost:5432/deepaudit  
，此配置指定了PostgreSQL数据库的连接信息，包括用户名、密码、主机地址和端口号，以及数据库名称。平台通过此配置与数据库建立连接，存储和读取项目信息、审计结果等数据。  
  
1. **沙箱配置**  
：SANDBOX_IMAGE=ghcr.io/lintsinghua/deepaudit - sandbox:latest  
指定了用于PoC验证的沙箱镜像，SANDBOX_TIMEOUT=300  
设置了沙箱内执行任务的超时时间为300秒。合适的沙箱镜像和超时设置能够保证PoC验证过程的顺利进行，同时避免因长时间运行任务而导致的资源浪费。  
  
1. **RAG配置**  
：CHROMA_PERSIST_DIR=./chroma_db  
指定了ChromaDB向量数据库的持久化存储目录，EMBEDDINGS_MODEL=text - embedding - 3 - small  
设置了用于生成嵌入的模型。这些配置影响着RAG知识库的存储和使用，确保平台能够有效地存储和检索代码语义相关的信息。  
  
### 0x0802前端配置 (frontend/.env)  
1. **VITE_API_URL=http://localhost:3000**  
：此配置指定了前端与后端进行通信的API地址，前端通过该地址向后端发送请求，获取项目信息、审计结果等数据。如果后端服务的地址或端口发生变化，需要相应地修改此配置。  
  
1. **VITE_WS_URL=ws://localhost:3000**  
：设置了WebSocket实时通信的地址，用于实现审计日志的实时推送。前端通过WebSocket连接到该地址，接收后端发送的实时审计日志信息，使用户能够实时了解审计任务的执行情况。  
  
## 0x09API接口参考  
### 0x0901核心REST API端点  
1. **项目管理**  
：  
  
1. **POST /api/projects**  
：用于创建项目，用户可以通过此接口向平台提交项目相关信息，如项目名称、描述、代码仓库地址等，平台将根据这些信息创建一个新的审计项目。  
  
1. **GET /api/projects/{id}**  
：通过项目ID获取项目详情，包括项目的基本信息、审计状态、漏洞数量等。用户可以根据项目ID查看特定项目的详细情况，方便对项目进行管理和跟踪。  
  
1. **POST /api/projects/{id}/scan**  
：启动指定项目的审计任务，当用户确认项目准备好进行审计时，通过此接口触发审计流程，平台将按照预定的审计策略对项目进行漏洞挖掘。  
  
1. **Agent审计**  
：  
  
1. **POST /api/agent/audit**  
：启动Multi - Agent审计，该接口触发Multi - Agent系统开始执行审计任务，各个智能体将按照工作流协同完成审计工作。  
  
1. **GET /api/agent/status/{task_id}**  
：根据任务ID获取审计状态，用户可以通过此接口实时了解审计任务的执行进度，如正在进行信息收集、漏洞挖掘或PoC验证等阶段。  
  
1. **GET /api/agent/logs/{task_id}**  
：获取审计日志，此接口返回指定任务的详细审计日志，包括各个智能体的操作记录、发现的潜在问题等信息，方便用户进行问题排查和分析。  
  
1. **即时分析**  
：  
  
1. **POST /api/analysis/code**  
：用于代码片段分析，用户可以将代码片段通过此接口提交给平台，平台将快速对代码片段进行安全分析，并返回分析结果。  
  
1. **POST /api/analysis/file**  
：支持文件上传分析，用户可以上传整个代码文件，平台将对文件内容进行全面的安全检测，相比代码片段分析，更适用于对完整代码文件的审查。  
  
1. **报告**  
：  
  
1. **GET /api/reports/{project_id}**  
：获取指定项目的审计报告，平台将返回该项目的详细审计报告，包括漏洞列表、危害等级、修复建议等内容。  
  
1. **POST /api/reports/export**  
：导出报告（PDF/MD/JSON），用户可以通过此接口选择将审计报告导出为PDF、Markdown或JSON格式，满足不同的使用场景需求。  
  
### 0x0902WebSocket实时通信  
  
通过const ws = new WebSocket('ws://localhost:8000/ws/agent/{task_id}');  
建立WebSocket连接，用于实时接收审计日志推送。当后端有新的审计日志产生时，会通过此WebSocket连接将日志信息发送给前端。前端通过ws.onmessage = (event) => { const log = JSON.parse(event.data); console.log(  
[  
  
{log.message}); };  
解析和处理接收到的日志信息，在控制台打印出每个智能体的操作日志，方便用户实时监控审计任务的执行情况。  
## 0x10沙箱安全机制  
### 0x1001隔离策略  
1. **Docker容器隔离**  
：每个PoC在独立的Docker容器中运行，这种隔离方式确保了各个PoC之间以及PoC与外部环境之间的独立性。即使某个PoC在执行过程中出现问题，也不会影响其他PoC的运行以及整个系统的稳定性。例如，一个PoC尝试进行恶意的系统调用，由于其运行在独立容器中，不会对宿主机或其他容器造成影响。  
  
1. **资源限制**  
：对Docker容器进行CPU和Memory配额限制，防止PoC在执行过程中占用过多的系统资源，导致系统性能下降。例如，为每个容器分配一定的CPU核心数和内存大小，确保多个PoC可以同时运行而不会相互干扰。  
  
1. **网络隔离**  
：沙箱内默认禁止外网访问，除了专门用于SSRF测试的情况。这有效防止了PoC在执行过程中与外部恶意服务器进行通信，避免数据泄露或成为攻击跳板的风险。  
  
1. **文件系统**  
：采用只读挂载的方式，将容器内的文件系统设置为只读，防止PoC通过修改文件系统来逃逸沙箱环境，进一步增强了沙箱的安全性。  
  
### 0x1002验证流程  
1. **PoC脚本生成**  
：Verification Agent根据Analysis Agent发现的潜在漏洞，生成相应的PoC脚本。这些脚本模拟攻击者的行为，尝试触发漏洞。例如，对于一个潜在的SQL注入漏洞，Verification Agent会生成包含恶意SQL语句的PoC脚本。  
  
1. **环境构建**  
：沙箱动态构建目标应用环境，根据项目的技术栈和依赖关系，在容器内搭建与目标应用相似的运行环境。这确保了PoC脚本在一个与实际应用相近的环境中执行，提高验证的准确性。  
  
1. **脚本执行与验证**  
：在隔离环境中执行攻击脚本，捕获脚本执行过程中的响应或异常。如果成功触发了与漏洞相关的响应，如获取到数据库的敏感信息或引发了特定的错误，就可以确认漏洞的存在性。如果验证失败，Verification Agent会自动分析失败原因，修正PoC脚本并重试，最多重试3次。例如，如果PoC脚本由于环境配置问题导致执行失败，Verification Agent会调整脚本中的相关配置信息后再次尝试执行。  
  
## 0x11性能指标分析  
1. **并发审计**  
：DeepAudit支持多项目并行扫描，这意味着平台能够同时处理多个项目的审计任务，大大提高了审计效率。在企业级应用中，可能需要同时对多个项目进行安全审计，并发审计功能使得平台能够快速响应这种需求，缩短整体审计周期。  
  
1. **响应时间**  
：代码片段分析能够在 < 5秒内完成，这对于开发人员在编写代码过程中即时检测代码安全性非常关键。快速的响应时间使得开发人员能够及时得到反馈，及时修复潜在的安全问题，提高开发效率。  
  
1. **Agent循环**  
：平均3 - 5轮完成深度审计，这表明Multi - Agent系统能够在相对较少的循环次数内，全面且深入地审查代码，挖掘出潜在的漏洞。相比传统的审计方式，减少了审计所需的时间和资源消耗。  
  
1. **PoC成功率**  
：对于常见漏洞类型，PoC成功率 > 85%，这说明平台在验证漏洞存在性方面具有较高的准确性。较高的PoC成功率意味着平台发现的漏洞大多数是真实可利用的，减少了安全人员对漏洞真实性的额外验证工作。  
  
1. **误报率**  
：误报率 < 15%，相比传统SAST降低了60%。低误报率使得安全人员能够专注于真正的安全问题，避免在大量误报信息中浪费时间和精力，提高了安全审计工作的效率和质量。  
  
  
  
**END**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2bujwd3M0M1ICStsbhAHWtt0VVqCfFLOVnpmeNJ3R59doWtI0AmqLn4Qkic8aAS06l0pATjcYx10zw/640?wx_fmt=png "")  
  
  
