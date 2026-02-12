#  【已验证】Windows 记事本应用程序远程代码执行漏洞  
Hedysx
                    Hedysx  安全微焦点   2026-02-12 06:35  
  
    Microsoft Windows 记事本是一款预装于 Windows 系统的轻量级文本编辑器，广泛用于日常文档处理。漏洞影响其 Markdown 渲染引擎的实现，具体版本为 11.0.0 至 11.2510 之前的版本。  
  
    近日，Microsoft 安全响应中心（MSRC）披露了 Windows 记事本应用存在一个高危命令注入漏洞（CVE-2026-20841）。该漏洞源于应用未能正确处理命令中的特殊字符（CWE-77），导致攻击者可通过构造恶意文本文件，诱使用户在联网状态下打开文件，从而触发远程代码执行（RCE）。  
  
    记事本在解析 Markdown 中的 file:/// 链接时，未对 URL 中的特殊字符（如 @ 端口、UNC 路径）进行充分过滤，导致攻击者可嵌入指向远程 WebDAV/SMB 共享的恶意路径。当用户点击链接且系统已关联可执行扩展名（如 .py、.jar）时，记事本将直接调用 ShellExecute 打开该远程文件，造成任意代码执行。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RjNQtLicCeVArPR4WQtM4hhwK5UMIq6JAMVJ6rdpYQezQzGjYWCgZLppcrxAEmGictoBibMOyJlAEVCQKYsovBQ43APUWtT8qybLb9HgR6BE20/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RjNQtLicCeVBb3mL803b8Xyo3ZTUVSZrguBjI4WHo9v7WkpwoMfm7NCY5Lr8SlkvfzWGibRfC0j3TibR7RQ9AgRHP7IibecwmXnjicrvicTw80l6Y/640?wx_fmt=png&from=appmsg "")  
  
  
