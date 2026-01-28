#  攻击者利用React2Shell漏洞针对IT行业发起攻击  
 FreeBuf   2026-01-28 10:31  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38JdicabhF81Im3gEDpQN7BF29iaeO6XzlibDY7VMQHsOumdXZX9a1LxW0yoIia8ZD9vTIYic7dicFNXXCA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
威胁行为者正通过一个被追踪为CVE-2025-55182的关键漏洞（俗称React2Shell）针对保险、电子商务和IT行业的公司发起攻击。该漏洞存在于处理React Server Components客户端-服务器通信的Flight协议中，允许攻击者在易受攻击的服务器上执行未经授权的代码。  
  
  
该漏洞源于不安全的反序列化过程，服务器在未经验证的情况下接受了客户端数据。攻击主要投放XMRig加密货币挖矿程序，同时伴有多个危险的僵尸网络和远程访问工具。  
  
  
**Part01**  
## 攻击活动特点  
  
  
这些利用活动展现出惊人的速度和复杂性。BI.ZONE分析师指出，攻击者能够在漏洞披露后数小时内将其武器化，尽管许多此类安全漏洞在实际场景中从未被广泛利用。针对俄罗斯实体的攻击专门部署了RustoBot和Kaiji僵尸网络，而针对其他地区的攻击活动则分发了更广泛的恶意软件，包括CrossC2植入程序、Tactical RMM、VShell后门和EtherRAT木马。  
  
  
React2Shell影响多个版本的React Server Component软件包，包括react-server-dom-webpack、react-server-dom-parcel和react-server-dom-turbopack的19.0、19.1.0、19.1.1和19.2.0版本。补丁已在19.0.1、19.1.2和19.2.1版本中发布。BI.ZONE研究人员发现，仅修复漏洞是不够的，组织还必须评估其系统是否存在成功利用和利用后活动的迹象，因为这些攻击通常涉及多种恶意操作。  
  
  
**Part02**  
## 防护建议  
  
  
除了打补丁外，开发人员还应验证其Next.js版本和依赖项，更新后重新构建项目，并检查锁定文件以确认已删除易受攻击的软件包版本。专家建议在生产环境中限制使用实验性React Server Components功能，除非当前安全补丁已覆盖这些功能。  
  
  
**Part03**  
## 感染机制与恶意软件部署  
  
  
攻击链始于威胁行为者利用React2Shell在受感染容器内执行命令。获得初始访问权限后，攻击者从远程服务器下载并执行Bash脚本来部署恶意负载。例如，wocaosinm.sh脚本会下载被识别为Kaiji僵尸网络的架构特定ELF可执行文件，该僵尸网络通过systemd服务、crontab任务和修改后的系统工具执行DDoS攻击并建立持久性。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38JdicabhF81Im3gEDpQN7BFFhvzcQf3OnvUuZSMyHQKp20bjLfaQG7JQQFM1UTzhGm4iaaCJEU20TQ/640?wx_fmt=png&from=appmsg "")  
  
  
另一种部署方法涉及setup2.sh脚本，该脚本通过下载包含挖矿程序配置和可执行文件的压缩包来安装XMRig 6.24.0版本。随后，alive.sh脚本会终止任何CPU占用超过40%的进程，但XMRig挖矿程序本身和其他白名单进程除外。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38JdicabhF81Im3gEDpQN7BFrT48UMDVUvhsLibewVB6sb3m5bcqryHv54d6YIeNy4dK3fWmTmdkxgQ/640?wx_fmt=png&from=appmsg "")  
  
  
攻击者还通过nslookup等工具使用DNS隧道技术，利用编码的子域名查询将命令执行结果外泄到外部域。  
  
  
**Part04**  
## 高级攻击向量  
  
  
用于Cobalt Strike的CrossC2框架负载代表了另一种复杂的攻击向量。这些UPX打包的可执行文件包含嵌入在文件末尾的加密配置，使用AES-128-CBC算法解密。  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38JdicabhF81Im3gEDpQN7BF9ZVj8DJxYjsbfaKdr1piaffwSGcaSU8IDUqiahCBLicEsBEMDlHF92jLA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
check.sh脚本将这些负载保存为rsyslo，并创建一个systemd服务以实现持久性，将恶意软件伪装成"Rsyslo AV Agent Service"以避免检测。  
  
  
EtherRAT恶意软件通过建立五种不同的方法展示了卓越的持久性能力：systemd服务、XDG Autostart条目、crontab任务、.bashrc修改和.profile修改。这款基于JavaScript的恶意软件从以太坊智能合约中获取其命令和控制服务器地址，使得传统拦截方法效果不佳。  
  
  
**参考来源：**  
  
Attackers Exploiting React2Shell Vulnerability to Attack IT Sectors  
  
https://cybersecuritynews.com/attackers-exploiting-react2shell-vulnerability/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334254&idx=1&sn=60c1a1f106cdbab728bc207a35262d08&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
