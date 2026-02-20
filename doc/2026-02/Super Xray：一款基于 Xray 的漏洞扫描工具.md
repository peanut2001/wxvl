#  Super Xray：一款基于 Xray 的漏洞扫描工具  
原创 网安武器库
                    网安武器库  网安武器库   2026-02-19 05:43  
  
**更多干货  点击蓝字 关注我们**  
  
  
  
**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**  
  
**往期回顾**  
  
  
  
  
  
  
·  
Havoc：现代化后渗透命令与控制(C2)工具  
  
  
  
  
  
·  
URLFinder：一款高效网页内部隐藏链接挖掘工具  
  
  
  
  
  
·  
PCHunter：一款深度检测隐藏恶意代码的扫描工具（兼容win11）  
  
  
  
  
  
·  
Web-SurvivalScan：用于快速验证资产存活的轻量化渗透测试扫描工具  
  
  
  
  
  
·【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat  
  
  
  
  
  
·  
xss_scanner_mix：一款自动化深度XSS漏洞扫描工具  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**介绍**  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicL8QWLTkyUqAcIL85D5ZJ6sP7QC9ibicpSURXLVJ5T4QBSMsejNXoRjfER95nvGZdYI31yIUQG9wvBGQUTgh81icKSKFjAoswvlu4/640?wx_fmt=png&from=appmsg "")  
  
    Super Xray 是一款基于 Xray 漏洞扫描工具的 GUI 启动器，旨在简化 Xray 的使用流程并提供更友好的用户界面。Xray 本身是一款功能强大的安全评估工具，支持主动和被动扫描，能够检测多种类型的漏洞。然而，Xray 只有命令行版本，对于新手来说可能不太容易上手，因此 Super Xray 提供了一个图形化界面，使得用户可以更快速、更直观地进行漏洞扫描。  
  
    Super Xray 基于 Java 8 构建，确保了广泛的跨平台兼容性。它不仅简化了 Xray 的使用流程，还引入了一些增强功能，如内置的下载面板以获取最新的 Xray 和RAD工具。此外，Super Xray 还支持通过 config.yaml 配置文件启动，使得用户可以根据自己的需求进行灵活配置。  
  
    Super Xray 的使用前提包括本地有 JRE/JDK 8+ 环境（如果使用内置JRE的exe版本无需Java环境）。它提供了两种方式的exe文件，system版使用系统的JRE，另一种内置了JRE 8。Super Xray 还提供了一个简单的 GUI 界面，帮助用户更快速地使用 Xray。  
  
    总的来说，Super Xray 是一个旨在帮助新手更容易使用 Xray 进行漏洞扫描的工具，它通过图形化界面简化了操作流程，同时保持了 Xray 的强大功能。  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**安装介绍**  
  
  
  
      
下载地址：  
```
https://github.com/4ra1n/super-xray/releases/tag/1.7
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJxq3UbdnOUia486iarSL80RnrNDibxSk6UToBEHT6B9yUIK2QKvP8qlDBzJwzYYyLicTic668Ll8ZFhQB2oeuicx0tlbAaYcgjrVYeM/640?wx_fmt=png&from=appmsg "")  
  
    可以看到三种下载方式：  
  
1.super-xray-1.7-jre-exe.zip  
  
2.super-xray-1.7.jar  
  
3.super-xray-1.7-system-jre.exe  
  
    第一种  
内置了JRE，无需额外安装Java环境，解压后直接运行exe。  
  
    第二种  
需要系统已安装 JRE/JDK 8+ 环境，通过 java -jar 启动  
  
    第三种  
使用系统JRE，需要系统已安装Java环境，直接运行exe  
  
  
    如果下载  
super-xray-1.7.jar包，需要  
通过 java -jar 启动  
，终端运行：  
```
java -jar super-xray-1.7.jar
```  
  
    如果下载  
super-xray-1.7-jre-exe.zip，则压缩后直接点击.exe文件执行：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicK6KDicEEnwtt0Wu5kqyVm8Kog8KDOAr4Xfk8kibNnsqibichUDdaLr4NicS7IVH6ba6D0ECoEougAIvjoictrQYqVlJvKluJNHkLvZk/640?wx_fmt=png&from=appmsg "")  
  
    点击.exe文件后仍要执行，即可打开界面：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKVhtvOicsIROfyCItJKhcwRibjD8HH0hnnsEic7SGdiar42ejZsRWIFInDmPM00DN1JLD2fNY21icwYXACrXJYCYicFQtJTQO2UvKuA/640?wx_fmt=png&from=appmsg "")  
  
    即可开始使用。  
  
  
注意：  
  
1.请使用 1080P 及以上分辨率，在 720P 及以下分辨率可能无法完全显示  
  
2.请使用最新版xray（目前是1.9.4版本，本工具未兼容老版本xray）  
  
3.支持两种方式的exe文件，system版使用系统的JRE，另一种内置了JRE 8  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**功能介绍**  
  
  
  
    根据GUI界面图，可以看到工具的功能如下：  
  
1.选择xray可执行文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLXBddibbOwzL3gKBYfrsA8aEIW2Hw3rNmYCRiaH463xDb2qlgdHcCb8B41TiamEeUHmrbS2mvOsTXHuOoNJ5DyicDnYVN7Z188vzI/640?wx_fmt=png&from=appmsg "")  
  
    点击按钮选择xray扫描对象。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJSicP8N7KichUM9WoJhSqs0rFKtBicxYEciaIGib0MAcl3YdsiakAcuILkxZEEVIweLr9rDTwulHxG3rbDFN1W38XR7oeliceFAImtZw/640?wx_fmt=png&from=appmsg "")  
  
    下面的命令行输出结果会根据操作进行输出。  
  
  
2.poc模块  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLKcPJzkQ6fVQ4mU5AU975YsAGRQSdciasesEmAyXqjsSl2ercj9QSjF7uXCLYasWwE2icl25sfNIk3KxksSiblavDxialthEBK5sk/640?wx_fmt=png&from=appmsg "")  
  
    点击  
同步PoCket数据库可以获取所有可用的PoC。  
  
    点击  
查看所有PoC可以方便的搜索需要的PoC，如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJ95KyTzReUTZ3ZLAzjFktnm81wgAkxbBFIicjgFhf9g3jeasUswZ99hW7Cib8p0o2IvcicOJUA00ykSO1ibfTmpgPZU0nmibW6DZhE/640?wx_fmt=png&from=appmsg "")  
  
    搜索选择并复制后输入到输入框中，按照一行一个PoC的原则，然后指定PoC。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIia5LXf6NCtMzQqTJFz5k7IDJjeEGnQhEVW7opEJTNzcWWRZSoicfKwPdibxBiclsuroUrKcBerkGMVhmgCn8X2LxkaJURgKFSaicE/640?wx_fmt=png&from=appmsg "")  
  
      
除此这外还可以  
设置等级，  
选择本地的PoC，  
在线生成PoC和  
清除PoC设置。  
  
  
3.扫描插件  
  
      
这是工具的核心功能区域，列出了 Xray 支持的所有主动扫描插件，用户可以自由勾选需要启用的检测模块。  
  
    同时在指定PoC后，会自动调整扫描插件配置，选择PoC指定的扫描插件。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJndR7NDLibibFVCl3qkT0LBoSVVmZqsSrg7ZckLjhWKocrLOl6XibzT4dnUV2fD7jibj5SaaApHA0shxfEf9qiaQzdicFEl83mMg2KU/640?wx_fmt=png&from=appmsg "")  
  
    可以进入  
高级配置进行进一步设置：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJibF68iaXbJC9rSAVJzIAFnCvOAsRDARJAD69j6NYy65ekqOUx7jblB1PM38lu7FymyO9JBD16D5oAAib9egA4u8rVVAbwvH802Y/640?wx_fmt=png&from=appmsg "")  
  
  
4.反连平台  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIsiaeCPpDo6ASOZfk5WAHM6Kb4iaTRgkFS78OTt0afZeiaAS0ByuxeUMFNHcqBicNyAHSR1WXRibIJ9ceq8flGeVLUzS7HD604hCpo/640?wx_fmt=png&from=appmsg "")  
  
      
Xray反连平台是Xray漏洞扫描工具的一个辅助功能，它主要用于解决在漏洞检测过程中，由于目标系统没有直接反馈（即没有回显），导致难以确认漏洞是否存在的情况。通过配置反连平台，可以让目标系统执行特定的命令（如ping、curl等），这些命令会触发目标系统对反连平台发起网络请求。反连平台接收到这些请求后，可以确认命令已被触发，从而间接证明漏洞的存在。  
  
      
反连平台的配置涉及到多个方面，包括数据库文件位置、认证Token、HTTP和DNS的监听设置等。例如，可以配置反连平台的HTTP服务，使其监听特定的IP和端口，同时指定用于获取客户端IP的HTTP头部信息。对于DNS反连，可以配置域名和静态解析规则，以及是否将域名的NS记录指向反连平台。  
  
      
Xray反连平台是一个强大的工具，它通过接收目标系统的网络请求来辅助确认漏洞的存在，尤其适用于那些没有直接反馈的漏洞检测场景。  
  
  
5.子域名扫描  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKfYfdH8qG5IskWwWDweYHuVtpkHxNwcGLSpytDRhKY34ZabQzhO3HrOL6gwibJqYADoRacuW99Gyh20DlJGxoFTZHlaSE7QDek/640?wx_fmt=png&from=appmsg "")  
  
    设置目标子域名并点击  
随机文件名后，点击  
开始扫描，即可对子域进行扫描，点击  
打开输出文件可以看到扫描详细情况。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLiaLCu7z7SalGdObuJnGN1sDziblhPOFjZoEPia59JzPBL0gORpsvVnmhhtqtlg0icBBSlpuzeTVuI8QeaGO45Yu6fA2PrPDl0AdA/640?wx_fmt=png&from=appmsg "")  
  
  
6.下载面板  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIAF8OBG31SNMLQVPuBTwKEsk0hlYAPaIxodbKLVUTxUSTOzNpvuy3mibMz4Lj5icicY8meWM3Xee9EDRHHH5vyp2ApTvtzz9dPxg/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJozu3UIhXEfV85P8CTXOVhO3hUOF40x8VX6c8bOIsLN6QibI0IfQW70vT6uiagfRxepAHzvL2Ll74hpMv8Run6ibL0VTpNY91ems/640?wx_fmt=png&from=appmsg "")  
  
    在1.0版本以后新增下载面板，一键下载最新版xray和rad工具。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
