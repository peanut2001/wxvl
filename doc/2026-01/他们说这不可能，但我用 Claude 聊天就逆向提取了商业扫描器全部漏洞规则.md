#  他们说这不可能，但我用 Claude 聊天就逆向提取了商业扫描器全部漏洞规则  
原创 AI安全工坊
                        AI安全工坊  AI安全工坊   2026-01-22 14:39  
  
# 他们说这不可能，但我用 Claude 聊天就逆向提取了商业扫描器全部漏洞规则  
> "  
> 不需要懂逆向，不需要会编程，只需要和 AI 对话。本文记录了一次完整的技术实验：通过与 AI 助手对话，从某商业漏洞扫描器中提取漏洞检测规则的全过程。  
  
  
**⚠️ 重要声明**  
  
本文内容仅用于**安全研究**  
和**技术教育**  
目的，旨在：  
1. 1. 探索 AI 在安全研究领域的应用边界  
  
1. 2. 帮助安全产品厂商了解潜在风险并改进防护  
  
1. 3. 促进安全社区的技术交流与进步  
  
**请勿将本文技术用于任何未经授权的场景。**  
 未经授权对商业软件进行逆向工程可能违反相关法律法规和用户协议。读者应自行承担因不当使用而产生的一切法律责任。  
## 0x00 背景  
  
在安全行业，漏洞扫描器的核心竞争力在于其**漏洞检测规则库**  
。这些规则库通常包含：  
- • 数千个 CVE 漏洞的检测逻辑  
  
- • 大量未公开的 0day 检测规则  
  
- • 针对国内软件的专属 POC  
  
- • 多年积累的检测经验  
  
对于安全研究人员来说，这些规则具有极高的学习价值。但厂商通常会采用各种手段保护这些核心资产：编译嵌入、压缩存储、加密保护…  
  
传统的提取方式需要深厚的逆向工程功底，可能需要数天甚至数周的时间。  
  
但这一次，我决定尝试一种不同的方式：**完全通过与 AI 对话来完成这个任务**  
。  
## 0x01 工具准备  
  
我使用的是 **Claude Code**  
，一个基于 Claude Opus 4 模型的终端 AI 助手。它可以：  
- • 在终端中与你对话  
  
- • 理解你的目标和上下文  
  
- • 生成并执行 shell 命令  
  
- • 根据命令输出调整策略  
  
- • 生成完整的脚本代码  
  
关键是：**你不需要知道具体怎么做，只需要描述你想要什么**  
。  
## 0x02 目标分析  
  
目标是一个 Docker 容器化部署的商业漏洞扫描器，架构如下：  
```
┌─────────────────────────────────────────────────────────┐│                    系统架构                              │├─────────────────────────────────────────────────────────┤│                                                         ││  ┌─────────────┐    gRPC     ┌─────────────────────┐   ││  │  Web 前端   │◄───────────►│    扫描引擎          │   ││  │  (Python)   │             │    (Go 语言)         │   ││  └──────┬──────┘             │                     │   ││         │                    │  核心二进制 150MB+   │   ││         ▼                    │  - POC 规则嵌入      │   ││  ┌─────────────┐             │  - 漏洞检测逻辑      │   ││  │  数据库     │             └─────────────────────┘   ││  │  (SQLite)   │                                       ││  └─────────────┘                                       ││                                                         │└─────────────────────────────────────────────────────────┘
```  
  
我的目标：**提取扫描引擎中嵌入的全部 POC 规则**  
。  
## 0x03 第一阶段：信息收集  
### 对话 1：确定规则存储位置  
  
**我**  
：我想从这个扫描器中提取漏洞检测规则，规则应该是 YAML 格式的 POC。帮我分析一下可能的存储位置。  
  
**AI**  
：好的，让我们先分析几种可能的存储方式：  
1. 1. **数据库存储**  
：规则可能在 SQLite/MySQL 中  
  
1. 2. **文件系统**  
：独立的 YAML 文件  
  
1. 3. **编译嵌入**  
：打包进 Go 二进制  
  
1. 4. **远程加载**  
：从服务器动态获取  
  
让我们逐一排查。先看数据库：  
```
docker exec web-container sqlite3 /data/db.sqlite3 ".tables"
```  
  
**执行结果**  
：  
```
sys_plugin          vuln_category       scan_taskuser_plugin         ...
```  
  
**AI**  
：有 sys_plugin  
 表，让我们看看里面有什么：  
```
docker exec web-container sqlite3 /data/db.sqlite3 \"SELECT COUNT(*) FROM sys_plugin;"
```  
  
**执行结果**  
：  
```
5500
```  
  
**AI**  
：有 5500 条插件记录！让我们看看表结构：  
```
docker exec web-container sqlite3 /data/db.sqlite3 \"PRAGMA table_info(sys_plugin);"
```  
  
**执行结果**  
：  
```
0|id|INTEGER|1||11|plugin_key|VARCHAR(255)|1||02|name|VARCHAR(255)|1||03|category|VARCHAR(50)|1||04|version|VARCHAR(36)|0||0
```  
  
**AI**  
：只有元数据（key、name、type），没有 POC 内容字段。规则不在数据库中。  
### 对话 2：检查文件系统  
  
**我**  
：那看看文件系统里有没有。  
  
**AI**  
：  
```
docker exec scanner-engine find / -name "*.yml" -o -name "*.yaml" 2>/dev/null | head -20
```  
  
**执行结果**  
：  
```
（空）
```  
  
**AI**  
：没有独立的 YAML 文件。让我们检查二进制：  
```
docker exec scanner-engine ls -lh /app/scanner
```  
  
**执行结果**  
：  
```
-rwxr-xr-x 1 root root 156M Dec 30 06:10 /app/scanner
```  
  
**AI**  
：156MB 的 Go 二进制，很可能规则就嵌入在里面。让我们验证：  
```
docker exec scanner-engine strings /app/scanner | grep -i "poc\|rule\|yaml" | head -20
```  
  
**执行结果**  
：  
```
plugins/pocs/plugins/pocs/cve-2021-44228.ymlplugins/pocs/cve-2022-22965.yml...
```  
  
**AI**  
：确认了！规则以 yml 文件的形式嵌入在二进制中。让我们统计数量：  
```
docker exec scanner-engine strings /app/scanner | \  grep -oE "plugins/pocs/[a-zA-Z0-9_-]+\.yml" | \sort -u | wc -l
```  
  
**执行结果**  
：  
```
5200
```  
  
**结论**  
：5200 个 POC 文件嵌入在二进制中，但只能看到文件名，看不到内容（因为是压缩存储的）。  
## 0x04 第二阶段：尝试直接提取（失败）  
### 尝试 1：binwalk 分析  
  
**我**  
：能不能用 binwalk 把这些文件提取出来？  
  
**AI**  
：可以试试。先把二进制复制出来：  
```
docker cp scanner-engine:/app/scanner /tmp/scannerbinwalk /tmp/scanner | head -50
```  
  
**执行结果**  
：  
```
DECIMAL       HEXADECIMAL     DESCRIPTION--------------------------------------------------------------------------------0             0x0             ELF, 64-bit LSB executable, AMD x86-644243407       0x40BFCF        gzip compressed data30590113      0x1D2C4A1       LZ4 compressed data, legacy30590270      0x1D2C53E       LZ4 compressed data, legacy...92520048      0x583BE70       End of Zip archive
```  
  
**AI**  
：发现了 gzip、LZ4、Zip 等压缩数据。尝试提取：  
```
binwalk -e /tmp/scanner -C /tmp/extracted/ls /tmp/extracted/
```  
  
**执行结果**  
：  
```
_scanner.extracted/
```  
```
ls /tmp/extracted/_scanner.extracted/
```  
  
**执行结果**  
：  
```
40BFCF.gz  583BE70.zip  ...
```  
  
**AI**  
：让我们看看提取出了什么：  
```
file /tmp/extracted/_scanner.extracted/*
```  
  
**执行结果**  
：  
```
40BFCF.gz: gzip compressed data583BE70.zip: Zip archive data (时区数据)...
```  
  
**我**  
：解压看看有没有 POC？  
  
**AI**  
：  
```
zcat /tmp/extracted/_scanner.extracted/40BFCF.gz | strings | grep -i "name:\|rules:" | head -10
```  
  
**执行结果**  
：  
```
（空）
```  
  
**结论**  
：❌ binwalk 提取的都是时区数据、图片等资源，不是 POC。  
### 尝试 2：搜索原始 YAML 内容  
  
**我**  
：直接在二进制里搜索 YAML 内容呢？  
  
**AI**  
：  
```
strings /tmp/scanner | grep -E "^name:\s*poc-" | head -10
```  
  
**执行结果**  
：  
```
（空）
```  
  
**AI**  
：没有找到。说明 POC 内容确实是压缩存储的。让我们搜索一些 YAML 特征：  
```
python3 << 'EOF'with open('/tmp/scanner', 'rb') as f:    data = f.read()patterns = [b'name: poc-', b'rules:', b'requests:']for p in patterns:    idx = data.find(p)if idx > 0:print(f"Found '{p.decode()}' at offset {idx}")print(data[idx:idx+200].decode('utf-8', errors='ignore'))EOF
```  
  
**执行结果**  
：  
```
Found 'rules:' at offset 85829887rules:  braces:    level: error    max-spaces-inside: 1  brackets:    level: error...
```  
  
**AI**  
：这是 YAML lint 的配置规则，不是 POC。POC 内容确实被压缩了。  
  
**结论**  
：❌ 无法直接从二进制中提取 POC 内容。  
### 尝试 3：zstd 解压  
  
**我**  
：binwalk 显示有 zstd 压缩块，试试解压？  
  
**AI**  
：  
```
# 找 zstd 块python3 << 'EOF'with open('/tmp/scanner', 'rb') as f:    data = f.read()zstd_magic = b'\x28\xb5\x2f\xfd'idx = 0blocks = []while True:    idx = data.find(zstd_magic, idx)if idx == -1:break    blocks.append(idx)    idx += 1print(f"Found {len(blocks)} zstd blocks at: {blocks}")EOF
```  
  
**执行结果**  
：  
```
Found 5 zstd blocks at: [16555387, 16651237, 16654105, 49156610, 184577972]
```  
  
**AI**  
：尝试解压：  
```
ddif=/tmp/scanner bs=1 skip=49156610 count=5000000 of=/tmp/zstd_block.zstzstd -d /tmp/zstd_block.zst -o /tmp/zstd_out.bin
```  
  
**执行结果**  
：  
```
zstd: /tmp/zstd_block.zst : Decoding error (36) : Unsupported frame parameter
```  
  
**结论**  
：❌ zstd 块不是标准格式，可能是自定义压缩或加密。  
### 尝试 4：gRPC 接口  
  
**我**  
：有没有 gRPC 接口可以获取 POC？  
  
**AI**  
：让我们看看扫描引擎暴露了哪些端口：  
```
docker exec scanner-engine netstat -tlnp
```  
  
**执行结果**  
：  
```
tcp  0  0  10.0.0.2:9090  0.0.0.0:*  LISTEN  -
```  
  
**AI**  
：9090 端口是 gRPC 服务。安装 grpcurl 测试：  
```
# 下载 grpcurlcurl -sLO https://github.com/fullstorydev/grpcurl/releases/download/v1.8.9/grpcurl_1.8.9_linux_x86_64.tar.gztar xzf grpcurl_1.8.9_linux_x86_64.tar.gzdocker cp grpcurl scanner-engine:/tmp/# 列出服务docker exec scanner-engine /tmp/grpcurl -plaintext 10.0.0.2:9090 list
```  
  
**执行结果**  
：  
```
Failed to list services: server does not support the reflection API
```  
  
**AI**  
：服务端没有启用反射。我们需要 proto 文件。从反编译的代码中找到了接口定义：  
```
service VulnScanner {rpc Scan(ScanRequest) returns (ScanResult);rpc GetTaskStatus(TaskRequest) returns (TaskStatus);// 没有获取 POC 列表的接口！}
```  
  
**结论**  
：❌ gRPC 接口没有提供获取 POC 内容的方法。  
## 0x05 第三阶段：内存提取（成功）  
  
经过前面的失败尝试，AI 提出了一个关键洞察：  
  
**AI**  
：我们换个思路。无论 POC 如何存储，在执行扫描时必须解压到内存中。我们可以从运行时内存中提取。  
### 分析进程内存  
  
**我**  
：怎么做？  
  
**AI**  
：先找到进程：  
```
docker exec scanner-engine pgrep -f scanner
```  
  
**执行结果**  
：  
```
1
```  
  
**AI**  
：PID 是 1（容器内主进程）。看看内存布局：  
```
docker exec scanner-engine cat /proc/1/maps | head -30
```  
  
**执行结果**  
：  
```
00400000-00402000 r--p 00000000 00:91 12345  /app/scanner00402000-04000000 r-xp 00002000 00:91 12345  /app/scanner04000000-0a000000 r--p 03d66000 00:91 12345  /app/scanner0a000000-0a001000 r--p 0aeb3000 00:91 12345  /app/scanner0a001000-0b000000 rw-p 0aeb4000 00:91 12345  /app/scanner0b000000-0c000000 rw-p 00000000 00:00 0 0e000000-0e100000 rw-p 00000000 00:00 0      [heap]c000000000-c020000000 rw-p 00000000 00:00 0  # <-- Go 堆！
```  
  
**AI**  
：关键发现！c000000000-c020000000  
 是 Go 的堆内存区域，大约 512MB。这是 Go 运行时管理的内存，解压后的 POC 应该在这里。  
### 首次提取尝试  
  
**AI**  
：让我们搜索一下：  
```
docker exec scanner-engine python3 << 'PYEOF'pid = 1with open(f"/proc/{pid}/mem", "rb") as f:    f.seek(0xc000000000)    data = f.read(0x20000000)  # 512MBprint(f"Read {len(data)} bytes")# 搜索 POC 特征count = 0for pattern in [b"id:", b"name:", b"requests:", b"matchers:", b"severity:"]:    idx = 0while True:        idx = data.find(pattern, idx)if idx == -1:break        count += 1        idx += 1print(f"Found {count} potential POC markers")PYEOF
```  
  
**执行结果**  
：  
```
Read 536870912 bytesFound 12000 potential POC markers
```  
  
**AI**  
：找到了大量潜在的 POC 标记！现在让我们提取完整的 POC 内容。  
### 提取完整 POC  
  
**AI**  
：我来写一个提取脚本：  
```
#!/usr/bin/env python3"""从进程内存中提取 POC 规则"""import ospid = 1# 主进程 PIDoutput_dir = "/tmp/pocs"os.makedirs(output_dir, exist_ok=True)# 读取 Go 堆内存withopen(f"/proc/{pid}/mem", "rb") as f:    f.seek(0xc000000000)    data = f.read(0x20000000)  # 512MBprint(f"Read {len(data)} bytes from Go heap")# 搜索 POC 特征模式# 不同产品需要调整这些特征patterns = [b"id:",           # Nuclei 风格b"requests:",     # Nuclei 风格  b"matchers:",     # 匹配规则b"severity:",     # 危害等级]extracted = set()idx = 0whileTrue:# 找到任意一个特征    positions = []for p in patterns:        pos = data.find(p, idx)if pos != -1:            positions.append(pos)ifnot positions:break    pos = min(positions)# 向前搜索规则起始位置（通常是 id: 或 name:）    search_start = max(0, pos - 500)    chunk = data[search_start:pos]# 找 id: 或 name: 作为起始    start_markers = [b"id:", b"name:"]    start_pos = -1for marker in start_markers:        p = chunk.rfind(marker)if p != -1and (start_pos == -1or p > start_pos):            start_pos = pif start_pos == -1:        idx = pos + 1continue    rule_start = search_start + start_pos# 向后搜索规则结束位置    rule_end = pos + 50while rule_end < min(len(data), pos + 10000):# 边界检测：下一个规则开始或空字节        next_chunk = data[rule_end:rule_end+10]ifany(next_chunk.startswith(m) for m in start_markers):if data[rule_end-1:rule_end] in [b"\n", b"\x00"]:breakif data[rule_end:rule_end+4] == b"\x00\x00\x00\x00":break        rule_end += 1# 提取规则内容    rule_content = data[rule_start:rule_end].rstrip(b"\x00").strip()# 验证规则有效性（至少包含一个关键字段）ifany(kw in rule_content for kw in [b"requests:", b"matchers:", b"rules:", b"http:"]):# 从规则中提取名称作为文件名        first_line = rule_content.split(b"\n")[0]ifb":"in first_line:            rule_name = first_line.split(b":")[1].strip()            rule_name = rule_name.decode("utf-8", errors="ignore")            rule_name = rule_name.replace("/", "_").replace(" ", "_")[:80]            filename = f"{rule_name}.yaml"else:            filename = f"rule_{len(extracted):04d}.yaml"if filename notin extracted:            filepath = os.path.join(output_dir, filename)withopen(filepath, "wb") as out:                out.write(rule_content)            extracted.add(filename)    idx = rule_endprint(f"Extracted {len(extracted)} rules to {output_dir}")
```  
  
**执行结果**  
：  
```
Read 536870912 bytes from Go heapExtracted 4200 rules to /tmp/pocs
```  
  
**我**  
：只有 4200 个，应该还有更多吧？  
  
**AI**  
：很多规则可能还没加载到内存。扫描器通常采用**懒加载**  
策略，只有在需要时才加载规则。你需要触发一次扫描任务，让引擎加载更多规则。  
### 触发规则加载  
  
**我**  
：我在 Web 界面创建了一个漏洞扫描任务，选择了全部插件（大约 6600 个），目标填的 127.0.0.1。  
  
**AI**  
：很好！等任务开始运行后，规则就会加载到内存。现在重新提取：  
```
docker exec scanner-engine python3 /tmp/extract.py
```  
  
**执行结果**  
：  
```
Read 536870912 bytes from Go heapExtracted 6500 rules to /tmp/pocs
```  
  
**我**  
：6500 个了！还能更多吗？  
  
**AI**  
：可以尝试扩大内存搜索范围，或者多创建几个不同类型的扫描任务：  
```
# 扩大到 1GBwithopen(f"/proc/{pid}/mem", "rb") as f:    f.seek(0xc000000000)    data = f.read(0x40000000)  # 1GB
```  
  
**执行结果**  
：  
```
Read 1073741824 bytes from Go heapExtracted 7000+ rules to /tmp/pocs
```  
  
**我**  
：超过预期了！  
  
**AI**  
：太好了！多出来的可能是一些内部规则或者不同版本的规则。让我们打包下载：  
```
docker cp scanner-engine:/tmp/pocs /tmp/extracted_pocscd /tmp && tar czf pocs.tar.gz extracted_pocs/ls -lh pocs.tar.gz
```  
  
**执行结果**  
：  
```
-rw-r--r-- 1 root root 18M Jan 22 21:21 pocs.tar.gz
```  
## 0x06 提取结果分析  
### POC 格式示例  
  
提取出的 POC 是标准的 YAML 格式：  
```
id:CVE-2021-44228-log4j-rceinfo:name:ApacheLog4jRCEauthor:security-teamseverity:criticaldescription:|    Apache Log4j2 远程代码执行漏洞reference:-https://nvd.nist.gov/vuln/detail/CVE-2021-44228tags:cve,cve2021,rce,log4jrequests:-method:GETpath:-"{{BaseURL}}/api"headers:X-Api-Version:"${jndi:ldap://{{interactsh-url}}}"matchers-condition:andmatchers:-type:wordpart:interactsh_protocolwords:-"dns"-"http"-type:regexpart:interactsh_requestregex:-'([a-zA-Z0-9\.\-]+)\.([a-z0-9]+)\.([a-z0-9]+)\.\w+'
```  
### 统计信息  
<table><thead><tr><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));"><section><span leaf="">指标</span></section></th><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));color: #05d4cd;"><section><span leaf="">数值</span></section></th></tr></thead><tbody><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">提取 POC 总数</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">7000+</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">压缩包大小</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">18MB</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">提取耗时</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">~30秒</span></section></td></tr></tbody></table>### 漏洞类型分布（示例）  
```
Web 漏洞          3000+  (40%)网络设备          1500+  (20%)中间件            1000+  (15%)数据库            500+   (7%)其他              1000+  (18%)
```  
## 0x07 技术原理深度解析  
### 为什么内存提取有效？  
```
┌─────────────────────────────────────────────────────────────┐│                    POC 生命周期                              │├─────────────────────────────────────────────────────────────┤│                                                             ││  [编译时]        [启动时]        [扫描时]        [执行时]    ││                                                             ││  源文件 ──压缩──► 二进制 ──加载──► 索引 ──解压──► 内存      ││  .yaml          .bin           元数据        明文 POC ✓    ││                                                             ││  可读            不可读          部分可读      完全可读      ││                                                             │└─────────────────────────────────────────────────────────────┘
```  
  
关键点：**无论如何保护，POC 在执行检测时必须以明文形式存在于内存中**  
。  
### Go 程序内存布局  
```
地址范围                    用途────────────────────────────────────────────────0x00400000-0x04000000      代码段 (.text)0x04000000-0x0a000000      只读数据段 (.rodata)0x0a001000-0x0b000000      数据段 (.data/.bss)0x0e000000-0x0e100000      传统堆 [heap]0xc000000000-0xc020000000  Go 堆 (runtime heap) ← POC 在这里
```  
  
Go 使用自己的内存管理器，堆内存位于 0xc000000000  
 开头的高地址区域。这是一个固定的特征，适用于所有 Go 程序。  
### 懒加载机制  
  
大多数扫描器不会在启动时加载所有规则，而是采用懒加载：  
```
启动扫描器    │    ▼加载规则索引（文件名、元数据）    │    ▼等待扫描任务    │    ▼创建扫描任务 ◄─── 触发点    │    ▼根据目标匹配规则    │    ▼解压并加载匹配的规则到内存 ◄─── 提取时机    │    ▼执行漏洞检测
```  
  
这就是为什么需要先创建扫描任务，才能提取到更多规则。  
## 0x08 AI 在过程中的关键作用  
  
回顾整个过程，AI 的作用不仅仅是"执行命令"：  
### 1. 方向指引  
  
当我不知道从哪里开始时，AI 提供了系统性的分析框架：  
- • 先排查数据库  
  
- • 再检查文件系统  
  
- • 然后分析二进制  
  
- • 最后考虑内存提取  
  
### 2. 失败处理  
  
每次尝试失败后，AI 都能快速调整策略：  
- • binwalk 失败 → 尝试直接搜索  
  
- • 直接搜索失败 → 尝试 zstd 解压  
  
- • zstd 失败 → 尝试 gRPC 接口  
  
- • gRPC 失败 → 转向内存提取  
  
### 3. 代码生成  
  
AI 生成的代码不是简单的模板，而是根据实际情况定制的：  
- • 根据内存布局确定搜索范围  
  
- • 根据 POC 格式设计特征模式  
  
- • 根据提取结果优化边界检测  
  
### 4. 问题诊断  
  
当提取数量不够时，AI 准确诊断出原因（懒加载）并给出解决方案（触发扫描任务）。  
### 5. 持续优化  
  
从 4200 → 6500 → 7000+，AI 不断优化提取策略，最终超额完成目标。  
## 0x09 通用性分析  
  
这种方法不仅适用于某一个产品，理论上适用于所有满足以下条件的扫描器：  
### 适用条件  
<table><thead><tr><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));color: #05d4cd;"><section><span leaf="">条件</span></section></th><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));"><section><span leaf="">说明</span></section></th></tr></thead><tbody><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">✅ 规则是文本格式</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">YAML/JSON/XML 等</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">✅ 运行时需要解压</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">压缩存储的规则</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">✅ 有特征模式</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">可识别的字段名</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">✅ 有系统权限</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">root 或同用户</span></section></td></tr></tbody></table>### 适用场景分析  
<table><thead><tr><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));"><section><span leaf="">产品类型</span></section></th><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));color: #05d4cd;"><section><span leaf="">开发语言</span></section></th><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));"><section><span leaf="">规则格式</span></section></th><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));color: #05d4cd;"><section><span leaf="">可行性</span></section></th></tr></thead><tbody><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">Go 语言扫描器</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">Go</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">YAML/JSON</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">✅ 高</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">Java 扫描器</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">Java</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">YAML/JSON/XML</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">✅ 高</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">Python 扫描器</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">Python</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">YAML/JSON</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">✅ 高</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">C/C++ 扫描器</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">C/C++</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">自定义格式</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">⚠️ 中</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">脚本类扫描器</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">各种</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">明文脚本</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">✅ 高</span></section></td></tr></tbody></table>> "  
> 注：本表仅从技术角度分析不同类型产品的内存提取可行性，不针对任何具体产品。  
  
### 不同语言的适配  
  
**Python 产品**  
：  
```
# 搜索 Python 堆patterns = [b"def check(", b"class Poc", b"vuln_id"]
```  
  
**Java 产品**  
：  
```
# 使用 jmap 导出堆jmap -dump:format=b,file=heap.bin <pid>strings heap.bin | grep -A 10 "vuln_name"
```  
  
**C/C++ 产品**  
：  
```
# 使用 GDBgdb -p <pid>(gdb) dump memory /tmp/heap.bin 0x08000000 0x10000000
```  
## 0x0A 防护建议  
  
作为安全产品开发者，如何防护这种攻击？  
### 1. 内存保护  
```
// 使用后立即清零funcexecuteRule(rule []byte) {deferfunc() {for i := range rule {            rule[i] = 0        }        runtime.GC() // 强制垃圾回收    }()// 执行规则...}
```  
### 2. 规则分片  
  
不要一次性加载所有规则：  
```
funcscanTarget(target string) {for _, ruleID := range getMatchingRules(target) {        rule := loadRule(ruleID)   // 按需加载        result := executeRule(rule)        unloadRule(rule)           // 立即释放        clearMemory(rule)          // 清零内存    }}
```  
### 3. 格式混淆  
  
避免使用明显的特征字段：  
```
# Bad: 容易被搜索id:CVE-2021-44228name:Log4jRCEseverity:critical# Better: 混淆字段名_i:a1b2c3d4_n:encrypted_base64_string_s:4
```  
### 4. 反调试检测  
```
funccheckDebugger()bool {    data, _ := ioutil.ReadFile("/proc/self/status")return !strings.Contains(string(data), "TracerPid:\t0")}funccheckMemoryAccess()bool {// 检测 /proc/self/mem 是否被其他进程访问// ...}
```  
### 5. 运行时加密  
```
// 规则在内存中保持加密状态// 只在执行的瞬间解密funcexecuteRule(encryptedRule []byte) {    rule := decrypt(encryptedRule)defer encrypt(rule) // 执行后重新加密// 执行...}
```  
  
**但说实话，这些都只能增加难度，无法完全防护。**  
 只要规则需要执行，就必须在某个时刻以明文存在。  
## 0x0B 法律与道德边界  
  
在进行此类研究前，必须认真考虑以下问题：  
### 法律风险  
<table><thead><tr><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));"><section><span leaf="">行为</span></section></th><th style="padding: 12px 16px;text-align: left;font-weight: 600;color: #1677ff;border-bottom: 1px solid rgba(5,212,205,0.1);background: linear-gradient(to right, rgba(22,119,255,0.05), rgba(5,212,205,0.05));color: #05d4cd;"><section><span leaf="">可能涉及的法律</span></section></th></tr></thead><tbody><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">未授权逆向商业软件</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">《计算机软件保护条例》</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">绕过技术保护措施</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">《著作权法》</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">传播提取的规则</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;"><section><span leaf="">《反不正当竞争法》</span></section></td></tr><tr><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">用于攻击他人系统</span></section></td><td style="padding: 10px 16px;border-bottom: 1px solid rgba(0,0,0,0.05);color: #4e5969;background: rgba(247,248,250,0.7);"><section><span leaf="">《刑法》第285/286条</span></section></td></tr></tbody></table>### 合规建议  
1. 1. **获取授权**  
：在进行安全研究前，尽可能获得厂商的书面授权  
  
1. 2. **限定范围**  
：仅在授权范围内进行测试  
  
1. 3. **负责任披露**  
：发现安全问题后，通过正规渠道向厂商报告  
  
1. 4. **不传播**  
：提取的规则仅供个人学习，不公开传播  
  
1. 5. **不商用**  
：不将提取的规则用于商业目的  
  
### 本文的定位  
  
本文是一次**技术探索实验**  
，目的是：  
- • 研究 AI 在安全领域的应用潜力  
  
- • 帮助厂商了解潜在的安全风险  
  
- • 推动行业对规则保护的重视  
  
**本文不鼓励任何未经授权的逆向行为。**  
## 0x0C 总结与思考  
### 技术总结  
1. 1. **核心原理**  
：规则执行时必须以明文存在于内存中  
  
1. 2. **关键步骤**  
：定位进程 → 分析内存布局 → 触发规则加载 → 搜索特征提取  
  
1. 3. **成功要素**  
：正确的内存区域 + 准确的特征模式 + 触发加载机制  
  
### AI 的价值  
  
这次实验让我深刻感受到 AI 在安全研究中的价值：  
1. 1. **降低门槛**  
：不需要精通逆向，也能完成复杂任务  
  
1. 2. **提高效率**  
：2 小时完成可能需要数天的工作  
  
1. 3. **交互式探索**  
：根据实时反馈调整策略  
  
1. 4. **知识整合**  
：AI 整合了多个领域的知识  
  
### 更深的思考  
> "  
> 在 AI 时代，**提出正确的问题**  
比**掌握具体的技术**  
更重要。  
  
  
因为技术可以让 AI 帮你实现，但问题需要你自己去发现。  
  
同时，这也给安全产品厂商敲响了警钟：**传统的保护手段在 AI 面前可能不堪一击**  
。当攻击者可以通过自然语言对话来完成复杂的逆向任务时，防护的难度将大大增加。  
## 附录：通用提取脚本参考  
  
以下脚本仅供学习参考，展示内存提取的基本原理：  
```
#!/bin/bash# 通用扫描器规则内存提取脚本（仅供学习）# 实际使用需根据目标调整参数CONTAINER="scanner-engine"# 容器名称PROCESS="scanner"# 进程名称OUTPUT_DIR="/tmp/rules"# 输出目录echo"=========================================="echo"扫描器规则内存提取工具"echo"=========================================="# 获取 PIDPID=$(docker exec$CONTAINER pgrep -f $PROCESS | head -1)echo"[*] Process PID: $PID"# 提取规则docker exec$CONTAINER python3 << PYEOFimport ospid = $PIDoutput_dir = "$OUTPUT_DIR"os.makedirs(output_dir, exist_ok=True)with open(f"/proc/{pid}/mem", "rb") as f:    f.seek(0xc000000000)    data = f.read(0x20000000)print(f"[*] Read {len(data)//1024//1024}MB from memory")# 根据目标产品调整特征patterns = [b"id:", b"name:", b"requests:", b"matchers:"]extracted = set()# ... 提取逻辑 ...print(f"[+] Extracted {len(extracted)} rules")PYEOF# 打包docker cp$CONTAINER:$OUTPUT_DIR /tmp/extracted_rulestar czf rules.tar.gz -C /tmp extracted_rulesecho"[+] Saved to rules.tar.gz"
```  
## 写在最后  
  
**致安全厂商**  
：本文的目的不是攻击，而是提醒。在 AI 时代，传统的软件保护手段面临新的挑战。希望本文能帮助厂商重新审视规则保护策略，推动行业安全水平的整体提升。  
  
**致安全研究者**  
：技术是中立的，但使用技术的人需要有底线。请在合法合规的前提下进行安全研究，尊重他人的知识产权。  
  
**致读者**  
：如果你从本文中学到了东西，希望你能将这些知识用于正当的安全研究和防护工作，而不是用于破坏。  
  
**工具信息**  
：  
- • Claude Code：终端 AI 助手  
  
- • 模型：Claude Opus 4  
  
**免责声明**  
：本文所述技术仅供安全研究和教育目的。作者不对任何人因阅读本文后采取的行动承担责任。在进行任何安全测试前，请确保已获得适当授权。  
  
如果觉得本文有价值，欢迎点赞、在看、转发！  
  
关注公众号，获取更多 AI + 安全的技术分享。  
  
  
  
## AI安全工坊内部社群  
  
  
  
**🔥 AI安全工坊社群 · 6大核心价值 🔥**  
  
****1. **AI安全实战**  
→ AI渗透测试 | 模型加固 | 数据防护 | 模型测评  
  
1. **开发全栈指南**  
→ 大模型应用 | Agent开发 | 行业解决方案 | AI安全工具 | AI产品开发  
  
1. **商业落地加速**  
→ 案例拆解 | ROI优化 | 合规指南  
  
1. **专属学习支持**  
→ 文档库 | 答疑 | 代码示例 | 1v1 解答  
  
1. **独家资源网络**  
→ 工具包 | 漏洞库 | 行业报告 | AI视频课程 | AI多模态资源  
  
1. **高质量AI社群**  
→ 技术交流 | 内推机会 | 项目合作  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRAicHn7IC6WXiaPEfumEvmO15U6l7p2efUz1oia0ugSlK5FwtEbMNcUMoGOt3hoSNfibSmiaNtFu80V138g/640?wx_fmt=png&from=appmsg "")  
  
  
## AI安全工坊-AISecKit安全工具资源平台  
  
  
  
**网站地址：https://aiseckit.com/**  
  
**网站介绍：AISecKit 提供了一个专注于 AI 安全工具和大型语言模型安全资源的平台，为专注于 AI 安全和网络安全专业人士提供了一系列的工具和资源。**  
  
****  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/BibeFvVBkRA8OoawLw7oR4iaTVrY2q4h0ictEjkEkjf68kicX0Yyb4Dpnriay22UDxnIWTClicVKia16yicNEZYjIUaibJw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
## 福利赠送  
  
  
  
🎁 **立即获取福利，在公众号后台私信发送下方关键词，即可免费领取专属工具和教程：**  
<table><tbody><tr><td data-colwidth="268" width="268" valign="top" style="word-break: break-all;"><section><span leaf="">关键词</span><span style="display: none;line-height: 0px;"><span leaf="">‍</span></span><span style="display: none;line-height: 0px;"><span leaf="">‍</span></span></section></td></tr><tr><td data-colwidth="268" width="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">AI大模型安全评估标准和指南</span></span></td></tr><tr><td data-colwidth="268" width="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">智擎 - AI业务场景提示词生成器</span></span></td></tr><tr><td data-colwidth="268" width="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">AI医疗助手-AI安全工坊</span><span style="display: none;line-height: 0px;"><span leaf="">‍</span></span></span></td></tr><tr><td data-colwidth="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">AI 智能体商业应用全景图</span></span></td></tr><tr><td data-colwidth="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">DeepSeek离线部署资源包</span></span></td></tr><tr><td data-colwidth="268" valign="top" style="word-break: break-all;"><span style="color: rgb(26, 27, 28);font-family: -apple-system, system-ui, &#34;system-ui&#34;, &#34;PingFang SC&#34;, &#34;SF Pro Text&#34;, &#34;Helvetica Neue&#34;, Helvetica, &#34;Hiragino Sans GB&#34;, &#34;Heiti SC&#34;, Arial, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, sans-serif;font-size: 14px;letter-spacing: normal;text-align: left;background-color: rgb(255, 255, 255);"><span leaf="">AIPOC</span></span></td></tr></tbody></table>- 免责声明  
  
   
  
  
  
  
