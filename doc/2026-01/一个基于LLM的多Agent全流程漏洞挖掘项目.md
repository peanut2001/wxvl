#  一个基于LLM的多Agent全流程漏洞挖掘项目  
qqliushiyu
                    qqliushiyu  贝雷帽SEC   2026-01-29 16:01  
  
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
  
  
一个基于LLM的多Agent全流程漏洞挖掘项目，支持PHP、Java、Python、Go、Node.js等多种语言项目环境搭建、漏洞分析、漏洞验证、报告产出。支持多Agent并发高效率完成漏洞挖掘任务，下个版本将会大更新。  
## 核心能力  
  
- **多 Agent 智能协作**  
：Ops / Analyze / Verifier / Report 四类 Agent 分工协作，通过 SharedContext 共享关键信息  
  
- **Docker 沙箱隔离**  
：所有代码执行、PoC 验证均在隔离容器中进行，支持 PHP/Java/Node.js/Python/Go 多语言环境  
  
- **端到端自动化**  
：从源码上传到漏洞报告生成，全流程自动化，无需人工干预  
  
- **实时可观测**  
：WebSocket 推送实时事件，支持漏洞发现/验证状态跟踪  
  
### 核心模块  
  
模块职责关键文件Web/HTTP API + WebSocket 推送 + Swagger 文档Route.go, Server.go, WebSocketImp.goProjectManager/项目级编排、AgentGroup 调度、多种调度模式ProjectManager.go, Start.goagents/Agent 接口定义与实现（Decision/Ops/Analyze/Verifier/Report）base.go, AgentCore.go, *Agent.gollm/记忆体管理、LLM 缓存、分层记忆ContextManager.go, SharedContext.go, Cache.go, TieredMemory.gotoolCalling/LLM 工具调用框架与 40+ 工具实现ToolManager.go, *Tool.godockerManager/Docker 容器操作封装 + 连接池core.go, pool.go, service.gotaskManager/任务/沙箱/漏洞/碎片/攻击链/检查点管理Task.go, VulnManager.go, FragmentManager.go, ChainManager.gotaskQueue/优先级任务队列、Worker 池、队列持久化Queue.go, Worker.go, Persistence.godatabase/SQLite 数据持久化、JSON 迁移工具database.go, schema.go, *_repo.go  
  
  
                                              
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
**工具使用**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
```
前置条件
Go 1.24+（与 
go.mod 保持一致）
Docker 已安装并启动
已构建依赖的 Docker 镜像：
aisandbox、
java_env
1. 构建 Docker 镜像
docker build -t aisandbox -f dockerfile/dockerfile.aisandbox/Dockerfile dockerfile/dockerfile.aisandbox
docker build -t java_env -f dockerfile/dockerfile.java_env/Dockerfile dockerfile/dockerfile.java_env
2. 配置
复制并编辑配置文件：
cp config.ini.example config.ini
# 编辑 config.ini，填入你的 API Key 等配置
3. 运行
go run .
默认监听：
0.0.0.0:9999
4. 访问 API 文档
启动后访问 Swagger UI 查看交互式 API 文档：
http://localhost:9999/swagger/index.html
5. 前端 UI（可选）
本仓库不提供前端 UI。如需可视化交互，请启动前端仓库：
https://github.com/qqliushiyu/AIxVuln_Web
6. 运行（二进制）
你也可以直接从 GitHub Releases 下载已编译的二进制文件运行。
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCA0DicOyY9MCiafw3EUvjfr9E0wEmadHaqQx5eXbWiaVTumUAeSGktuRvQAwnVuVnfKHxQQ7K3NRjgVg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCA0DicOyY9MCiafw3EUvjfr9EVEn1hegDKhvvVnpBmt7Z7hIOFpyBshQkzK8O4J68RHViclHiaibzXxVVA/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
**下载链接**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
  
```
https://github.com/qqliushiyu/AIxVuln_Web
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
  
                                                   
  
      
  
  
  
