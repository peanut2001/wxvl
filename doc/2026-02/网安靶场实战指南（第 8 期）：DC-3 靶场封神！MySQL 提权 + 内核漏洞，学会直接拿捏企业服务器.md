#  网安靶场实战指南（第 8 期）：DC-3 靶场封神！MySQL 提权 + 内核漏洞，学会直接拿捏企业服务器  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-02-02 02:59  
  
上一期DC-2的定时任务提权让大家直呼过瘾！但真实渗透中，服务器防护只会更严——没有明显的定时任务漏洞，也没有弱口令给你破解，该怎么办？  
  
今天的DC-3靶场就是为解决这个问题而生！它完全模拟真实企业服务器环境：**藏得极深的MySQL数据库漏洞、需要精准利用的Linux内核提权、全程无弱口令可破**  
，堪称“提权技巧天花板”。学会这套“数据库突破→内核提权”的组合拳，你才算真正掌握了高权限渗透的核心逻辑，挖洞赏金直接翻倍！  
## 一、环境搭建&信息收集：开局就给新手下马威  
  
DC-3和前两期不一样，开局就设坑！新手如果没做好信息收集，直接卡到怀疑人生。  
### 1. 靶场部署（避坑版）  
- 下载镜像：VulnHub搜“DC-3”，注意！它只有一个flag，通关目标就是拿下root权限找到这个flag  
  
- 网络配置：老规矩！Kali和DC-3都设为**仅主机模式**  
，这步错了后面全白搭  
  
- 启动靶场：DC-3启动后不会显示IP，别慌，按老方法扫  
  
### 2. 信息收集：全网段扫描，只找到一个突破口  
  
执行命令扫网段找靶场IP（示例网段192.168.137.0/24，按自己的改）：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0StwWYb06VyqvibdPCj12NsY9dtFCNhViaO81oJrRHWBudNo5ppLDIae2obw/640?wx_fmt=png&from=appmsg "")  
  
找到靶场IP（比如192.168.137.132）后，直接全端口扫描：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0StwWgFajcHUbpqcoPGNicUhludgjM8tFIiciaftTUf1QVNPPXy7UunXXnc7g/640?wx_fmt=png&from=appmsg "")  
  
**扫描结果让人大吃一惊**  
：  
- 只开放了**80端口**  
！SSH 22端口直接关了，定时任务、SUID文件这些常规提权路径全被堵死  
  
- 80端口跑的是**Joomla CMS**  
（和Drupal、WordPress齐名的老牌CMS），版本是3.7.0——这就是唯一的突破口！  
  
## 二、Joomla漏洞挖掘：从版本泄露到数据库拿下  
  
DC-3的核心就是“靠Joomla漏洞打穿数据库”，没有弱口令，纯靠技术突破！  
### 1. 一招确定Joomla版本，找到致命漏洞  
  
Joomla的版本信息藏在页面源码里：  
- 访问靶场IP，右键“查看页面源码”，搜索generator  
，看到Joomla! 3.7.0  
  
- 立刻打开Kali，用searchsploit  
搜漏洞：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0Stwhl3TyAH5uHmPYNWmRJia3qTdumu6NzNlBe3gLBmACmGYMtyvC0fNn7A/640?wx_fmt=png&from=appmsg "")  
  
搜索结果直接炸出**致命漏洞**  
：Joomla! 3.7.0 - SQL Injection (42033.txt)  
——这个漏洞能直接读取数据库所有数据！  
  
### 2. 利用SQL注入漏洞，导出管理员账号密码  
  
这个漏洞有现成的POC，不用自己写代码，新手也能轻松用：  
1. 复制POC路径：exploit/unix/webapps/42033.txt  
，查看POC内容：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0Stwa9qcEjKfkPJ4978YIHjicIGPnR9CrSy26icomico7woXR2QpwWbYuFE6A/640?wx_fmt=png&from=appmsg "")  
  
1. 找到核心Payload：POC里给了一个直接读取管理员表的URL，复制下来，把[target]  
换成靶场IP：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0StwrqvFHxKa1YCUgdzKZqeU1auNRsj4aXE4RzjRVfM5t2nnkDXxdOibwiaw/640?wx_fmt=png&from=appmsg "")  
  
1. 浏览器访问这个URL，页面直接报错，泄露数据库用户和数据库名：root@localhost  
+joomladb  
  
1. 用SQLMap批量导出数据（终极懒人法）：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0StwaIlkhgiczFS1OsKYZ7m8Qsib1ibhbKzwA2AUQnhBib8ecAcVicZvZWnM5Rg/640?wx_fmt=png&from=appmsg "")  
  
重点导出joomladb  
数据库里的#__users  
表（Joomla管理员表），拿到管理员账号：  
  
1. 用户名：admin  
  
1. 密码哈希值：$2y$10$DpfpYjADpejngxNh9GnmCeyIHCWpL97CVRnGeZsVJwR0kWFlfB1Zu  
  
### 3. 密码破解：用John the Ripper秒解哈希值  
  
拿到密码哈希别慌，Kali自带的John工具就是哈希破解神器：  
1. 新建文件dc3_hash.txt  
，把哈希值粘贴进去  
  
1. 执行破解命令，用rockyou.txt字典怼：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0StwaSyHqKROW2A3ibia6iblSiaFPZ7peJ8V8hINtWTmukmphHNy3EPpKPdbrw/640?wx_fmt=png&from=appmsg "")  
  
**30秒不到，密码出！**  
：snoopy  
——这个密码比DC-2的复杂多了，还好John够给力！  
  
### 4. 登录Joomla后台，上传木马拿shell  
  
拿到admin密码，直接冲Joomla后台：  
1. 访问后台地址：http://192.168.137.132/administrator  
，输入账号admin，密码snoopy，成功登录！  
  
1. 上传木马：Joomla后台可以直接编辑模板文件，找到“模板管理”→“Templates”→“Protostar”→“Edit HTML”  
  
1. 植入PHP一句话木马：把模板里的任意一行代码替换成：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0StwmgaXe76iavSnBYsnELcQN9a5mYB9iaSicf48xobveIKZS9nQGcKV6mUXA/640?wx_fmt=png&from=appmsg "")  
  
1. 连接木马：打开蚁剑，添加数据，地址填http://192.168.137.132/templates/protostar/index.php  
，密码填cmd  
，**成功拿到低权限shell**  
（当前用户www-data）！  
  
## 三、终极提权：Linux内核漏洞一击必杀（最关键的一步）  
  
拿到www-data权限后，常规提权方法全失效——没有SUID文件，没有定时任务，没有可写脚本！这时候就要祭出终极杀招：**Linux内核漏洞提权**  
！  
### 1. 信息收集：确定内核版本，找可利用漏洞  
  
内核提权的核心是“找对应版本的漏洞EXP”，先查服务器内核信息：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0StwysCvRLobA3Q0ZicgF1xZAAVnK4Rm4oAvsbmVBQH6HwtsPJC1Xp6yNHA/640?wx_fmt=png&from=appmsg "")  
  
返回结果：Linux dc-3 4.4.0-21-generic #37-Ubuntu SMP Mon Apr 18 18:33:37 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux  
  
关键信息：**内核版本4.4.0-21-generic、Ubuntu 16.04系统、64位**  
### 2. 搜索内核漏洞EXP，精准匹配  
  
用searchsploit  
搜对应内核版本的提权EXP：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0StwsD5sOsK9y3FLzic9ef0NBQVrunpNAjvL5DOpNHhPZn10gMezMHKPh0g/640?wx_fmt=png&from=appmsg "")  
  
一眼锁定**完美匹配的EXP**  
：Linux Kernel 4.4.0 < 4.11.8 - netfilter xt_u32 Privilege Escalation (44298.c)  
——这个EXP专门针对Ubuntu 16.04的4.4.0内核，成功率100%！  
### 3. 上传EXP，编译执行，秒提root  
  
这步是最爽的，新手跟着做就行：  
1. 在Kali里找到EXP文件：/usr/share/exploitdb/exploits/linux/local/44298.c  
  
1. 把EXP上传到靶场服务器：用蚁剑的“文件管理”功能，把44298.c上传到靶场的/tmp  
目录（权限足够）  
  
1. 靶场shell里编译EXP：gcc 44298.c -o dc3_exp  
（如果提示gcc没装，先执行apt-get install gcc  
安装）  
  
1. 给EXP加执行权限：chmod +x dc3_exp  
  
1. 执行EXP：./dc3_exp  
  
屏幕一闪，再输入id  
命令——**uid=0(root)！成功提权root！**  
## 四、拿下最终flag，通关总结（真实渗透必记）  
  
提权root后，找flag就是手到擒来：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0Stw6YKosTEmxNHbuRt0ykxu2ftUUBZol2H4mcrIatS8YFq7pGYAvNQwOw/640?wx_fmt=png&from=appmsg "")  
  
在/root/flag.txt  
找到最终flag！打开一看，短短一句话：“权限不是一切，但没有权限，你什么都不是”——这就是渗透的精髓！  
### 核心技巧总结（拿去直接挖洞）  
1. **CMS版本是突破口**  
：Joomla、WordPress这类CMS，版本泄露=漏洞泄露，一定要先查版本  
  
1. **内核提权是终极杀招**  
：当常规提权方法失效时，查内核版本找EXP，一击必杀  
  
1. **SQLMap是懒人神器**  
：遇到SQL注入，不用手动构造Payload，SQLMap直接导出数据  
  
## 五、互动&下期预告  
  
你在编译内核EXP时有没有遇到gcc安装失败的问题？或者内核版本不匹配的情况？评论区甩问题，我帮你拆解！  
  
下一期咱们告别DC系列，挑战**更贴近企业内网的靶场——Hack The Box（HTB）入门**  
，教你外网打点、内网横向移动、域控渗透的核心思路，关注别迷路！  
  
点击文末  
阅读原文  
领取200节攻防教程  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralY7kYI6yBEAYn0aorAz0Stwib7j2hhq8EV0WDDO7I8L51LibzVRhP4BoYIoiaaZrelldCwnyI7s5HYkA/640?wx_fmt=png&from=appmsg "")  
  
  
