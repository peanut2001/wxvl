#  【漏洞预警】麒麟操作系统V11 KysecScene D-Bus 服务本地提权漏洞  
 松杨网络安全资料库   2026-03-05 09:37  
  
漏洞概述：  
  
该漏洞存在于麒麟操作系统的D-Bus系统服务 **com.kylin.KysecScene**  
 中。该服务以 root 权限运行，但其 D-Bus 访问控制策略配置不当，未对调用主体进行有效的权限校验，导致任意本地普通用户均可直接调用其对外暴露的敏感接口。  
  
此外，服务提供的LoadJson与SaveJson方法在处理用户传入的文件路径时，未进行严格的访问控制判断与路径合法性校验，从而引发任意文件读写风险。  
  
上述问题相互叠加，可构成完整的本地权限提升攻击链。低权限用户可借此获取 root 权限，进而实现对系统的完全控制，安全风险极高。  
  
系统版本  
```
V11
```  
  
漏洞原因  
  
**1.KysecScene进程服务权限是root权限。**  
  
**2.D-Bus默认向本地用户开放。**  
  
**3.LoadJson和SaveJson方法可对任意路径进行操作，且未对其方法进行任何限制。**  
  
漏洞复现  
  
1.读取高敏感系统文件（如/etc/shadow  
）  
  
普通用户查看/etc/shadow  
，无法查看，如图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2xCpgJcagf8o1lniccBDL6ZGcicviazGhE3TicQMWg2YqtibbqjYlqT81Hn248QAYQQeKCVVicupJWSodonmp4ibKrBQKfXtcwBfIKMISxHXrriam0o/640?wx_fmt=png&from=appmsg "")  
  
使用漏洞查看/etc/shadow  
，如图  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2xCpgJcagf9jQliaib3aX64cTV1NOnNK3rKicDo7aEFYVHrDS0MoTgnMxKYFIl31YSZR1hCtSDfu99XnYama47AElDY41q38meorsF1q5mLVC4/640?wx_fmt=png&from=appmsg "")  
  
2.以 root 身份向任意文件路径写入文件  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2xCpgJcagfibHUpQzMiaqXswqBBc2eia6B5WoW7X0rSguLwJ64zY1TJUVuvoHRGXqBR7ZqP6mFaicZIG4xzgudF2Gia7OauAgJOOMeIkBn6iaf7AU/640?wx_fmt=png&from=appmsg "")  
  
文件成功写入  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2xCpgJcagf8JXBnT0f9QJmcgsw3P54T49q7n08HBooune0pGZAHib9c89aiacFvPicGOibIicXg31VXZWp5icH0Y63OhtJt6d5ppibdmibbRk6dqxLk/640?wx_fmt=png&from=appmsg "")  
  
文件权限，显示root用户编写  
  
![](https://mmbiz.qpic.cn/mmbiz_png/2xCpgJcagf8Gbh38Fet75FpggpV8MXHCYAhjia0n5viboz2Eic43vd4j4wpJrvEZ8ibOb5M5ATJ4vFGTZoRfemKKeR7GK8RTEyqhIO66RaTls8k/640?wx_fmt=png&from=appmsg "")  
  
漏洞影响  
  
1.本地权限提升至root：  
  
任意本地地权限用户可利用该漏洞获取root权限，实现完全控制。  
  
2.敏感信息泄露：  
  
攻击者可读取/etc/shadow  
、系统配置文件、数据库配置文件等敏感数据，导致密码泄露、凭证失窃，扩大攻击面。  
  
3.系统文件篡改及植入后门：  
  
向/etc/passwd  
、/etc/sudoers  
、计划任务等关键路径写入恶意内容，实现添加后门账户、提权维持权限、持久化控制等操作。  
  
4.横向移动风险增加：  
  
若系统处于内网环境中，攻击者可利用获取的 root 权限作为跳板，进行内网横向渗透，扩大入侵范围。  
  
临时修复建议  
  
1.**D-Bus策略限制：**  
  
**D-Bus策略文件路径如下：/usr/share/dbus-1/system.d/com.kylin.KyescScene.conf修改后的配置如下：**  
  
**在配置文件com.kylin.KyescScene.conf中，对KysecScene服务的访问策略进行限制，仅允许特定用户或用户组调用该服务，禁止普通用户直接访问。2.对敏感方法进行身份校验：**  
  
**开发确认是否有在调用LoadJson和SaveJson方法执行的操作，操作时进行身份校验，仅允许 root 或特定管理用户执行敏感操作。**  
  
**3.持续关注官网信息，及时下载更新补丁程序。**  
  
