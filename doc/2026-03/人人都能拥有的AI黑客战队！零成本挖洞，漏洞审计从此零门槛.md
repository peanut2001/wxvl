#  人人都能拥有的AI黑客战队！零成本挖洞，漏洞审计从此零门槛  
lintsinghua
                    lintsinghua  鹏组安全   2026-03-06 17:24  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0YvAy5BgkyNJe4vC6qtyDX3vcGgiameZcOwiaYlDgwuutJUicHD1ZWicn2T6WTuuiaLvsAcnHBq2a4f6LkwqGtGOuxw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0 "")  
  
想做漏洞挖掘却苦于没有专业团队？传统代码审计更是痛点缠身：误报堆成山、人工排查耗时长，啃不透业务逻辑满是盲区，漏洞难验证、源码不敢上云合规难，硬生生把高效挖洞变成了少数人的“专属技能”。  
  
3分钟本地部署、全程零成本，全自动挖洞+沙箱PoC验证双buff拉满，彻底打破技术壁垒，让专业级漏洞挖掘触手可及，轻松干翻传统审计模式！  
  
![Agent审计入口](https://mmbiz.qpic.cn/mmbiz_png/gL9yql6ibrhIUp1EtYlURPSxxSUT2523OtEprYiaT0OibiaWHXS3F1ShjeM2Oy7Z2ic05LOVicGN2o1xMbaSYuvxhTaRia5raibialORYgQ2THvaLelA/640?wx_fmt=png&from=appmsg "")  
## ⚡ 10秒极速部署，一行命令直达体验  
  
摒弃繁琐的环境搭建、依赖配置流程，不管是新手还是资深安全工程师，复制对应命令直接执行，即可快速启动AI审计服务，真正实现零门槛上手：  
### 国际线路（海外部署首选，稳定流畅）  
```
curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.yml | docker compose -f - up -d国内加速线路（南京大学镜像站，极速拉取无卡顿）
curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.yml | docker compose -f - up -d
```  
```
curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.cn.yml | docker compose -f - up -d
curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.cn.yml | docker compose -f - up -d
```  
## 🎯 硬核优势拉满，精准破解传统审计顽疾  
  
DeepAudit依托AI多智能体架构+本地化部署能力，直击传统审计核心短板，用技术实力解决安全审计的各类痛点，各项优势对比清晰可见：  
<table><thead><tr style="height:39px;"><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">传统审计核心痛点</span></p></th><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">DeepAudit 专属解决方案</span></p></th></tr></thead><tbody><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">误报堆积如山，人工清洗效率极低</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><strong><span leaf="">RAG检索增强+语义理解</span></strong><span leaf="">双重赋能，漏洞误报率直降80%，大幅减少无效排查工作</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">无法吃透业务逻辑，跨文件漏洞存盲区</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><strong><span leaf="">Multi-Agent多智能体协同作业</span></strong><span leaf="">，自动梳理代码调用链路，全维度覆盖业务无死角</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">漏洞真伪难辨，手动验证耗时耗力</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><strong><span leaf="">Docker沙箱PoC验证</span></strong><span leaf="">，只有可实际利用的漏洞才会上报，彻底杜绝虚假漏洞干扰</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">源码涉密不敢上云，合规审核难通过</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><strong><span leaf="">Ollama本地化部署</span></strong><span leaf="">，核心源码与数据全程不出内网，兼顾数据安全与合规要求</span></p></td></tr></tbody></table>## 🔄 5步全自动化审计流程，解放双手不费心  
  
DeepAudit实现从审计规划到结果输出的全流程自动化，无需人工值守干预，既能提升审计效率，又能保障漏洞挖掘的精准度，完整流程如下：  
1. **策略编排**  
：Orchestrator智能模块定制专属审计策略，贴合不同业务场景需求  
  
1. **信息侦察**  
：Recon Agent自动识别技术框架、定位代码入口点，夯实审计基础  
  
1. **漏洞挖掘**  
：Analysis Agent结合RAG知识增强，深度扫描剖析代码，精准定位潜在漏洞  
  
1. **验证修正**  
：Verification Agent自动编写PoC，接入沙箱执行验证，验证失败即刻自我迭代修正  
  
1. **报告生成**  
：自动过滤无效误报，支持PDF、Markdown、JSON多格式标准化输出  
  
![审计流日志](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhLh1FVDZkNhEHHAH9sQUryX9XMY4nTepVCpAxHnqvAQLY9gzibk6DwNQfdzBypVUle2qE7tMRicVVoEKQZDH9v7biccJqZ2hG36sY/640?wx_fmt=png&from=appmsg "")  
## 🏗️ 先进系统架构，微服务+沙箱兼顾性能与安全  
  
DeepAudit采用成熟的微服务+隔离沙箱架构，兼具扩展性、稳定性与安全性，支持按需弹性扩容，适配各类规模的审计需求，核心架构链路清晰：  
  
Vue3 Web前端界面 ─▶ Go-Zero API网关 ─▶ MongoDB数据存储  
  
▼  
  
Redis任务队列  
  
┌───────┼───────┐  
  
▼       ▼       ▼  
  
Worker1 Worker2 WorkerN（支持任意弹性扩容，适配大流量审计）  
  
▼  
  
Docker隔离沙箱 – 自动拉取镜像、执行PoC验证、实时回传审计结果，安全无外泄  
## 🧪 全品类漏洞覆盖，支持类型持续迭代更新  
  
DeepAudit覆盖当下主流高危、中危漏洞类型，满足日常代码安全审计、漏洞排查的核心需求，后续还会持续扩充覆盖范围，具体分类如下：  
<table><thead><tr style="height:39px;"><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">漏洞类别</span></p></th><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">典型漏洞示例</span></p></th></tr></thead><tbody><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">注入类漏洞</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">SQL注入、命令注入、XXE、SSRF</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">业务逻辑类</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">认证/授权绕过、IDOR、硬编码密钥</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">加密安全类</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">弱加密算法、不安全反序列化</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">信息泄露类</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">敏感信息泄露、目录遍历漏洞</span></p></td></tr></tbody></table>## 🤖 全场景LLM适配，国际+国内+本地全覆盖  
  
DeepAudit支持多款主流大语言模型，兼顾海外、国内不同使用场景，更有本地化模型方案，满足涉密场景数据不出内网的严苛要求：  
- **国际主流模型**  
：GPT-4o、Claude-3.5、Gemini Pro  
  
- **国内主流模型**  
：通义千问、GLM-4、Kimi、豆包  
  
- **本地私有化模型（Ollama）**  
：Llama3、Qwen2.5、DeepSeek-Coder，全程本地化运行，数据零外泄  
  
## 🎯 双模式功能矩阵，兼顾深度审计与快速扫描  
  
DeepAudit搭载Agent深度审计、即时分析两种模式，针对不同审计需求灵活切换，既满足精细化漏洞排查，也适配快速代码片段检测，核心功能对比清晰：  
<table><thead><tr style="height:39px;"><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">核心功能</span></p></th><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">Agent模式（深度审计）</span></p></th><th style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;font-weight:500;background-color:rgb(242, 243, 245);text-align:left;"><p><span leaf="">即时分析模式（快速扫描）</span></p></th></tr></thead><tbody><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">Multi-Agent协同审计</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">❌ 不支持</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">RAG知识增强分析</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">沙箱PoC漏洞验证</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">❌ 不支持</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">代码片段秒级扫描</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">❌ 不支持</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">多格式报告导出</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td></tr><tr style="height:39px;"><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">运行时动态切换LLM</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td><td style="border:1px solid rgb(222, 224, 227);font-size:10pt;padding:8px;vertical-align:top;"><p><span leaf="">✅ 支持</span></p></td></tr></tbody></table>## 📊 实战报告示例，漏洞结果清晰可落地  
  
Agent深度审计模式下，输出的报告条理分明，不仅标注漏洞等级，还附带验证结果与修复建议，直接落地整改：  
- **高危漏洞**  
：SSRF漏洞 ➜ 可窃取AWS元数据 ➜ 沙箱PoC验证成功，回显清晰  
  
- **中危漏洞**  
：硬编码JWT密钥 ➜ 配套专属解密脚本，快速排查风险  
  
- **低危漏洞**  
：弱加密算法使用 ➜ 提供可直接复用的修复代码（AES-256-GCM）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gL9yql6ibrhKsSeNl9P20srRGlgDLy3qIVrE2AAibF50L4eZyZe4EFVicxkLMYmLM9mlhwBltQMViaUljFfLByUnaHbvzwHibWARO18AAYWzl400/640?wx_fmt=png&from=appmsg "")  
## 🦖 未来6个月路线图，功能持续迭代升级  
  
DeepAudit并未止步于现有功能，后续将围绕自动化、定制化、全场景化持续优化，未来6个月核心规划如下：  
- v3.1 增量PR审计：无缝对接CI/CD流程，审计结果自动评论至代码PR  
  
- v3.2 Auto-Fix自动修复：AI Agent直接编写修复代码，自动提交修复PR  
  
- v3.3 自定义知识库：支持上传企业内部安全规范，RAG即刻适配专属审计标准  
  
- v4.0 二进制逆向审计：新增ELF/PE格式文件支持，覆盖二进制程序漏洞挖掘  
  
**小贴士**  
：本地部署全程零成本，数据安全有保障，不管是个人安全练习、企业内部代码审计，都能轻松适配，赶紧部署体验AI赋能的高效审计吧！  
  
github:  
https://github.com/lintsinghua/DeepAudit  
  
[鹏组安全社区站：您身边的安全专家-情报 | 攻防 | 渗透 | 线索 | 资源社区](https://mp.weixin.qq.com/s?__biz=Mzg5NDU3NDA3OQ==&mid=2247491205&idx=1&sn=b212739965f6617c84c89726cc85d50c&scene=21#wechat_redirect)  
  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyNHF1CWPJ9XSApBFhIGwF5Jh0zD2ySOcHvBkYgicU4xZsqvR3XEjUEnfGKH7ya8TgqCibHpYZKcibDBQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=28 "")  
  
**扫码关注**  
  
**社区**  
  
鹏组安全社区：  
comm.pgpsec.cn  
  
  
专注网络技术与骇客的一个综合性技术性交流与资源分享社区  
  
  
老用户续费88折扣  
![图片](https://mmbiz.qpic.cn/mmbiz_png/gL9yql6ibrhJModYspO6q4T19tQX0a9tvOqAcmblIoKGQmpmXW1AwbEIE4ibBWpicp0wLRlSWxf6T89qM9GwutmMa0bmdrqB2NJxCIRB9ScEcY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3 "")  
  
  
社区首页  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0YvAy5BgkyN92OtiagxgUpDAeq8RbcPacH8L82CwLzHtvucDrP1RrgfzeUYY8cS4WHk8niap3jKZzys9wK5oHB9w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=29 "")  
  
免责声明  
  
由于传播、利用本公众号鹏组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号鹏组安全及作者不为  
此  
承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！  
  
好文分享收藏赞一下最美点在看哦  
  
