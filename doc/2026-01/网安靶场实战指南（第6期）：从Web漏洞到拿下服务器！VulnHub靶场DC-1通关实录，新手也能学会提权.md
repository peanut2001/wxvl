#  网安靶场实战指南（第6期）：从Web漏洞到拿下服务器！VulnHub靶场DC-1通关实录，新手也能学会提权  
原创 点击关注👉
                    点击关注👉  网络安全学习室   2026-01-31 02:49  
  
很多人刷完DVWA、Juice Shop，总觉得“不过瘾”——这些靶场要么只练Web漏洞，要么没有真实服务器环境。但真实渗透中，**拿下Web权限只是第一步，提权、横向移动才是拿高权限的关键**  
！  
  
今天就带大家玩VulnHub最经典的靶场镜像DC-1——这是一个模拟真实Linux服务器的靶场，从“Web漏洞getshell”到“Linux提权”再到“拿下最终flag”，全程手把手教你走通完整渗透流程。学会这套思路，你才算真正入门实战渗透，再也不是只会刷Web漏洞的“小白”！  
## 一、 准备工作：5分钟搞定靶场环境搭建  
  
VulnHub的靶场都是虚拟机镜像，新手别慌，跟着步骤来，零门槛搭建！  
### 1. 下载镜像+准备工具  
- 靶场下载：去VulnHub官网搜“DC-1”，下载镜像文件（格式是.ova，很小，几百MB）  
  
- 工具准备：VMware或VirtualBox（虚拟机软件）、kali Linux（攻击机，自带所有渗透工具）  
  
### 2. 虚拟机配置（核心！避免踩坑）  
1. 打开VMware，点击“打开虚拟机”，选择下载好的DC-1.ova文件，导入虚拟机  
  
1. 网络设置：把DC-1和你的kali攻击机都设置为**仅主机模式**  
（确保两台机器在同一网段，能互相访问）  
  
1. 启动靶场：先开kali，再开DC-1，DC-1启动后会显示一个Linux登录界面，不用管它  
  
### 3. 找到靶场IP（第一步必做！）  
  
攻击前先确定目标IP，在kali里打开终端，执行命令扫描网段：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt8ia3iauBryVuicGOqzJJECWyKMFTLKLKrsKK2Y0CWGepDuPrqXnTRFK1icw/640?wx_fmt=png&from=appmsg "")  
  
扫描完成后，找到“DC-1”对应的IP（比如我的是192.168.137.130），记下来！  
## 二、 第一步：信息收集——找到靶场的“突破口”  
  
渗透的核心是“知己知彼”，先扫描靶场开放了哪些端口、有哪些服务：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt8tZD0yTVONIXYZfnMbyaIVqJf8nI4vJ6zOFVcpXLWThd2RSLgprcy1w/640?wx_fmt=png&from=appmsg "")  
### 扫描结果解读（重点看这两个！）  
1. **80端口开放**  
：运行Apache服务，说明有Web网站（突破口来了！）  
  
1. **22端口开放**  
：运行SSH服务，后续拿到账号密码可以直接登录服务器  
  
## 三、 第二步：Web漏洞突破——拿下第一个shell  
  
访问靶场IP（192.168.137.130），看到一个用Drupal搭建的CMS网站——Drupal是老牌CMS，低版本有很多漏洞，DC-1用的正好是有漏洞的版本！  
### 1. 漏洞扫描：找到可利用的漏洞  
  
用kali自带的工具扫描Drupal版本和漏洞：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt8kmwUZic2x9y7jygTAOTwpzjfic4ZFDJK5ibmicBUL7YULN95zr2JYC2abg/640?wx_fmt=png&from=appmsg "")  
  
搜索结果里会看到“Drupal 7.x - 'Drupalgeddon2' Remote Code Execution”——这个漏洞可以直接远程执行命令，拿下shell！  
### 2. 利用漏洞：一键getshell  
1. 复制漏洞对应的exp路径（比如exploit/unix/webapps/44449.rb  
）  
  
1. 执行exp，获取shell：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt8wPJv2bhwWfUSJpocl5r9LxicpcCl46VRCv6PYaiapTrVPuicXuMJkvgbA/640?wx_fmt=png&from=appmsg "")  
  
1. 看到id  
命令返回结果，说明**成功拿到低权限shell**  
！（当前用户是www-data，权限很低）  
  
## 四、 第三步：Linux提权——从低权限到root（核心难点！）  
  
拿到www-data权限后，我们只能操作Web目录，要想控制整个服务器，必须提权到root——这是真实渗透中最关键的一步！  
### 1. 先找靶场的flag文件（明确目标）  
  
DC-1有5个flag，找到所有flag才算通关。在shell里执行命令找flag：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt8v78x7NCgY0SFS1Im1ZNj7IuFPXyh2DglByxBuiav5ibibX0jdrGlxmSzg/640?wx_fmt=png&from=appmsg "")  
  
找到第一个flag，里面提示“看看/etc/passwd文件”——这是关键线索！  
### 2. 查看/etc/passwd，发现新用户  
  
执行命令查看系统用户列表：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt88icRBxKXnSQIVIyBYFv4KwwMbktWlCCmxuGib0DzCSrPPa09Vj1TNloQ/640?wx_fmt=png&from=appmsg "")  
  
会发现一个叫flag4  
的用户——这是靶场留的第二个突破口！  
### 3. 提权关键：利用SUID权限文件  
  
SUID是Linux的特殊权限，拥有SUID权限的文件，能以文件所有者的权限执行——我们要找root用户拥有的SUID文件：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt8dIcGS6mAUOd4uvcrUJl0sFNowVqUjZS76ueRFEx32NBTMfrmVpV4aA/640?wx_fmt=png&from=appmsg "")  
  
搜索结果里会有/usr/bin/find  
——这个命令可以用来提权！  
### 4. 用find命令提权到root（终极技巧！）  
  
find命令是root用户所有，且有SUID权限，执行下面的命令：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt8CDmamqRqCndZQCV6ia105iap32MAdch5kgRI61Zw9QQBqvKhibllibwozg/640?wx_fmt=png&from=appmsg "")  
  
执行后，输入id  
命令，看到uid=0(root)  
——**成功提权到root**  
！  
## 五、 第四步：拿下所有flag，完成通关  
  
提权到root后，整个服务器都归你管了！再次执行find命令找所有flag：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralaGKacpkFnqgmhGMrSpsRt84MHyMjMlweicQbkaHQhEwibo0VJQOUgYK2y696QuczicVbXkYdoOibA5Cg/640?wx_fmt=png&from=appmsg "")  
  
找到最后一个flag（在root目录下），里面写着“恭喜通关”——至此，DC-1靶场全部搞定！  
## 六、 实战总结：真实渗透的核心思路  
  
DC-1靶场完美还原了真实渗透流程，总结下来就3步：  
1. **信息收集**  
：扫端口、找服务、确定突破口（80端口Web服务）  
  
1. **Web突破**  
：利用CMS漏洞拿到低权限shell  
  
1. **提权横向移动**  
：找SUID文件提权到root，控制整个服务器  
  
这就是真实企业渗透的完整逻辑——不是只会找Web漏洞，而是从“突破”到“提权”的全流程操作！  
## 七、 互动与下期预告  
  
你在提权的时候有没有卡壳？比如找不到SUID文件，或者提权命令执行失败？评论区留言，我帮你拆解问题！  
  
下一期我们继续玩VulnHub靶场DC-2，教你**利用SSH密钥登录+crontab定时任务提权**  
，这套技巧在真实SRC里经常用到，关注不迷路！  
  
点击文末  
阅读原文  
领取200节攻防教程  
  
  
