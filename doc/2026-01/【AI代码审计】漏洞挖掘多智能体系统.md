#  【AI代码审计】漏洞挖掘多智能体系统  
 网络安全透视镜   2026-01-22 01:05  
  
## 项目概述  
  
**DeepAudit**  
 是一个基于 **Multi-Agent 协作架构**  
的下一代代码安全审计平台。它不仅仅是一个静态扫描工具，而是模拟安全专家的思维模式，通过多个智能体（**Orchestrator**  
, **Recon**  
, **Analysis**  
, **Verification**  
）的自主协作，实现对代码的深度理解、漏洞挖掘和 **自动化沙箱 PoC 验证**  
。  
  
我们致力于解决传统 SAST 工具的三大痛点：  
- **误报率高**  
 — 缺乏语义理解，大量误报消耗人力  
  
- **业务逻辑盲点**  
 — 无法理解跨文件调用和复杂逻辑  
  
- **缺乏验证手段**  
 — 不知道漏洞是否真实可利用  
  
用户只需导入项目，DeepAudit 便全自动开始工作：识别技术栈 → 分析潜在风险 → 生成脚本 → 沙箱验证 → 生成报告，最终输出一份专业审计报告。  
##   
## 界面预览  
### Agent 审计入口  
  
  
**页快速进入 Multi-Agent 深度审计**  
  
**审计流日志**  
  
****  
**智能仪表盘**  
  
****  
**即时分析**  
  
****  
**项目管理**  
  
****  
**GitHub/GitLab/Gitea 导入，多项目协同管理**  
### 专业报告  
###   
## CVE 漏洞发现  
### DeepAudit 已成功发现并获得 48 个 CVE 编号，涉及 16 个知名开源项目  
  
![](https://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS6MXib5oByxu4Z68ribhnQn67xtYGic3VEJsTD24pk3IdGE5qctbBXkicChzDkr907BxhFGMf2ZnSuaEw/640?wx_fmt=png&from=appmsg "")  
###   
##  快速开始  
### 使用预构建的 Docker 镜像，无需克隆代码，一行命令即可启动：  
```
curl -fsSL https://raw.githubusercontent.com/lintsinghua/DeepAudit/v3.0.0/docker-compose.prod.yml | docker compose -f - up -d

```  
  
### 方式二：克隆代码部署  
### 适合需要自定义配置或二次开发的用户：  
```
# 1. 克隆项目
git clone https://github.com/lintsinghua/DeepAudit.git && cd DeepAudit

# 2. 配置环境变量
cp backend/env.example backend/.env
# 编辑 backend/.env 填入你的 LLM API Key

# 3. 一键启动
docker compose up -d
```  
  
****  
**项目地址：**  
```
https://github.com/lintsinghua/DeepAudit
```  
  
****  
