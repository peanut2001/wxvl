#  【工具箱梳理】nday利用篇-第一期  
xxxh
                    xxxh  安全驾驶舱   2026-03-13 05:09  
  
**背景**  
  
  
  
    
    
继上期的工具分  
享，本  
期主要介绍一些nday漏洞利用的的工具  
。  
  
**工具清单**  
  
  
  
  
1. W/L-Fscan  
  
2. W-Goby  
  
3. Jar-I-Wanna-Get-All  
  
4. Jar-JNDIExploit  
  
5. Py-CrackJWTKey  
  
6. Jar-ShiroAttack2  
  
7. Jar-ThinkPHPGUI  
  
8. Jar-YongYouNCTool/Yongyou-Unserialize  
  
9. Jar-FrChannel  
  
**主题总结**  
  
  
  
  
1、nday漏洞综合利用的工具箱  
  
2、部分框架的nday漏洞利用工具  
  
**使用介绍/案例**  
  
  
  
  
**01 Fscan**  
  
    品种：       扫描工具  
  
    主要功能： IP探活、端口探活、nday漏洞扫描、弱口令扫描  
  
    命令分享：  
```
线程5禁探活弱口令探测，指定输出文件
fscan.exe -hf ip.txt -np -nopoc -num 5 -m vnc -o xb2504vnc.txt
C段漏洞扫描，后台静默执行，输出结果文件result.txt
nohup fscan -h 127.0.0.0/24 -num 5
```  
  
    链接：  
```
https://github.com/shadow1ng/fscan
```  
  
    ps: 经典的万金油扫描器，体积小，作用大。  
  
**02 Goby**  
  
    品种：        扫描工具  
  
    主要功能： IP探活、端口探活、漏洞扫描、POC扫描；  
带UI的Window扫描工具，解压即用、可自定义POC  
  
    链接：  
```
https://github.com/goby-lang/goby
```  
  
    ps：免费版的可用来进行网段探活、时效漏洞排查等，新版的UI响应流畅度比旧版本要好很多。  
  
**03 I-Wanna-Get-All**  
  
    品种：       漏洞利用工具箱  
  
    主要功能：用友、泛微等多组件nday探测，heapdump数据提取  
  
    链接：  
```
https://github.com/R4gd0ll/I-Wanna-Get-All
```  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdppGaXianRUj9X7qNfA6nicaqIUwGRxv3gzfos4XEauD6RibTUyVYNKetlpAsSfm9Yzia5TRgLVeFJtuQic08F546grkKRlbnefuVGC8/640?wx_fmt=png&from=appmsg "")  
  
    ps: heapdump解析能获取到heapdump_tool不同的信息，且同一个配置的信息会在同一个标签下，提取的数据比heapdump_tool更易读。  
  
**04 JNDIExploit**  
  
    品种：     JNDI辅助工具-LDAP服务启动  
  
    主要功能：启动LDAP服务，提供多种远程加载的shell类，协助weblogic等反序列化漏洞利用  
  
    命令分享：  
```
java -jar INDIExploit.jar -i IP
（虚拟机外的本机IP/虚拟机需设置虚拟网络编辑器->NAT设置->端口转发）
```  
  
      
链接：  
```
https://github.com/0x727/JNDIExploit
```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/ySlic3yZpdprM9CVV1FIkxRiabUCaT4klX7PwAGyBOlCuGkFG9Xn4B8HtyblNY6Iht91Y0IaNvWV4VHHRXn6cvfaME0hPanwzeyaAyibukun2g/640?wx_fmt=png&from=appmsg "")  
  
    ps: 内网系统的log4j2等反序列化漏洞验证方便，且支持通过多种中间件加载命令回显。  
  
**05 CrackJWTKey**  
  
      
品种：       JWT密钥爆破  
  
    主要功能： 破解JWT密钥，支持HS256、HS512等（需手动改一下解密方式）  
  
    链接：  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpr6IHmwTRFomRQBDuZ9icRap3PNSjGIFLOiaqqK1FaLW8YytMpo2PB0U2oibMMiby60xic3P6LfMSc3ictLFKJyoQpHeeXalaaAMia91g/640?wx_fmt=png&from=appmsg "")  
  
      
ps: 支持自定义字典，代码开源小体量易读易修改。  
  
**06 ShiroAttack2**  
  
      
品种：     shiro弱密钥反序列化可视化利用工具  
  
    主要功能：爆破shiro密钥，爆破回显利用链，命令行交互  
  
    链接：  
```
https://github.com/SummerSec/ShiroAttack2
```  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpqbl8rPHClibmd2mSBP2Pyty457n2EfQ4vPA8AUuibd1SRMCvPEV8pCtgZib8tXqfqvWyVJpHK682m7Jyg6kibibfgKibzVVUpnVibutg/640?wx_fmt=png&from=appmsg "")  
  
      
ps：对于探测shiro若密钥反序列化很方便，爆破密钥与回显方式一条龙获取shell。可以配合上期的HaE，HaE写规则确定是否是shiro，ShiroAttack2确认  
shiro  
系统部署后是否有更改密钥。  
  
**07 ThinkPHPGUI**  
  
    品种：      ThinkPHP利用工具  
  
    主要功能：ThinkPHP5.0的RCE漏洞，ThinkPHP多版本的日志泄露  
  
    链接：  
```
https://github.com/Lotus6/ThinkphpGUI
```  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdppZBRtBaLqYRBoEo8xVKu4QdKPAD5h6yjIYiaFJFmLNz0BRLib7ZJ1VEVVjFqGKEhSmkzicMb0ajfgl2uvwNNCyk9icQibJWFrkRyibY/640?wx_fmt=png&from=appmsg "")  
  
      
  
**08 YongYouNCTool/Yongyou-Unserialize-plus**  
  
    品种：           用友NC利用工具  
  
    主要功能：    用友NCnday检测、利用  
  
    链接：  
```
https://github.com/wgpsec/YongYouNcTool
https://github.com/bmth666/Yongyou-Unserialize-plus
```  
  
![image.png](https://mmbiz.qpic.cn/mmbiz_png/ySlic3yZpdprrUzoObbv21L1Ip6Wib58MzSAEa9XEZ5LoZAibnHSeDapDdBicMibPw31fZKh8Sg2xFfPrM3eOicM2E72AP4oWeJQfxVAFm4ZAaSGQ/640?wx_fmt=png&from=appmsg "")  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdppwYT4s1uo4pjz7rvASVc5C0eFAVpY53iaeKvriaFSFwQ9xvbGEMZkHJom1BFQwrq5hKq89uM8oBhtktvzzov742l60fXVU2ksuY/640?wx_fmt=png&from=appmsg "")  
  
  
**09 FrChannel**  
  
    品种：      帆软channel反序列化利用工具  
  
    主要功能：帆软channel检测、利用  
  
    链接：  
```
https://github.com/7wkajk/Frchannel
```  
  
![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/ySlic3yZpdpoC4I00gTKUHFaoDdrib6GFYLEw61SRocyBqiaDpia9habMiagxhYyMFIdrs0HzXGkAly19ibX78HmHfj7Yz2OicMTr20Ck9SZru8RX4/640?wx_fmt=png&from=appmsg "")  
  
  
**正文内容**  
  
  
  
  
  
**END**  
  
  
  
  
  
  
  
