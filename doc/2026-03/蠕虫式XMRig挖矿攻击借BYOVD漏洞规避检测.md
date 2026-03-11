#  蠕虫式XMRig挖矿攻击借BYOVD漏洞规避检测  
胡金鱼
                    胡金鱼  嘶吼专业版   2026-03-11 06:03  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif "")  
  
一场具备蠕虫传播能力的加密货币劫持攻击，正通过盗版软件进行传播，利用BYOVD漏洞部署定制版XMRig挖矿程序。  
  
研究人员发现，该攻击通过捆绑盗版软件传播，投放定制化XMRig挖矿木马。攻击借助BYOVD漏洞利用时间触发逻辑炸弹实现规避检测、最大化挖矿收益。其多阶段感染链以提升加密货币算力为核心，过程中常导致受感染系统运行不稳定。  
  
该攻击通过盗版“付费”软件安装程序传播，释放基于XMRig的复杂挖矿木马。其核心是名为Explorer.exe的控制程序，该程序以持久化状态机形式运行，可通过命令行参数切换角色：安装器、守护程序、主动感染、清理程序。  
  
据了解，Explorer.exe是整个感染流程的核心调度节点。在传统恶意软件设计中，功能通常被拆分为线性执行流程：下载器下载载荷、运行、退出。而Explorer.exe控制程序则以持久化状态机运行。  
  
它根据运行时传入的命令行参数决定行为模式，使单个文件在感染生命周期中承担多种不同角色：安装程序、守护程序、载荷管理器、清理程序。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fHEm7hZn9HIrSvOVSNyDbmbUjpmqAWd62gyTibfLyTU6ajXuJmorBeA77DkctQgIasibFCug6bdbFXjKDawoe82wZKA3BH22kXIicNydNnpHPc/640?wx_fmt=png&from=appmsg "")  
  
该恶意软件将控制逻辑（“大脑”）与载荷（“执行体”）分离，后者包括挖矿程序、守护程序以及用于获取内核权限的漏洞驱动（BYOVD）。  
  
恶意软件滥用一款名为WinRing0x64.sys的合法但存在漏洞的驱动，该技术被称为BYOVD（自带漏洞驱动）。它无需创建恶意驱动，只需加载此老旧但已签名的驱动，即可获得内核级（Ring 0）权限。  
  
获取权限后，它会修改特定 CPU 配置（型号专用寄存器），禁用干扰门罗币RandomX挖矿算法的硬件预取器。由于RandomX依赖随机内存访问，关闭这些功能可减少缓存冲突，将挖矿性能提升15%～50%。   
  
各类载荷被内嵌在程序资源段中，经解压后以隐藏系统文件形式写入磁盘，并伪装成合法软件。  
  
一套环形守护机制确保组件被终止后会互相重启，强行恢复挖矿，甚至会杀死正常的Windows资源管理器进程干扰用户操作。   
  
该恶意软件内置时间触发自杀开关，截止时间为2025年12月23日，到期后将执行可控清理逻辑。   
  
研究人员在sub_14000D180函数中发现了一个硬编码时间检测逻辑，充当“自杀开关”或“时间炸弹”。该机制获取系统本地时间，并与预设截止日期2025年12月23日对比：   
  
**·**  
活跃阶段（2025年12月23日之前）：执行标准感染流程，安装持久化模块并启动挖矿。  
  
**·**  
过期阶段（2025年12月23日之后）：表明该攻击并非长期持续运营，而是“发射后不管”的生命周期。时间点可能与租用的C2基础设施到期、加密货币市场预期变动（特别是门罗币难度调整），或计划切换新版本恶意软件有关。  
  
该XMRig变种还包含蠕虫模块，可通过U盘传播，而非仅依靠手动下载。它通过Windows系统通知静默监听新插入的可移动设备，而非持续轮询扫描。  
  
当U盘插入时，恶意软件会将自身explorer.exe复制到设备中，隐藏在文件夹内，并创建伪装成磁盘图标的恶意快捷方式。当该U盘在其他电脑上打开时，快捷方式即可执行恶意程序，实现进一步扩散。  
  
恶意分子似乎先在小范围系统中测试感染链与持久化功能（包括名为“Barusu”的自杀开关），随后再扩大规模。  
  
根据相关数据显示，曾有一个活跃节点以中等算力运行，2025年11月活动零星，12月8日起出现明显增长，表明新一轮投放或新感染节点被激活。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fHEm7hZn9HJV99DCT5p3Lt6n0do45r8zYvvIdSpJJydIM0dDiac7AcE9Okic1llVuOM55CGicUMlv2RwnFpQRapgR0E8BA1Hwm1e1MgvaQiceVM/640?wx_fmt=png&from=appmsg "")  
  
该攻击事件的发生正提醒人们，常规恶意软件仍在持续进化。攻击者将社会工程、伪装合法软件、蠕虫式传播、内核级漏洞利用结合，打造出高抗性、高效率的僵尸网络。尤其是BYOVD技术的使用，凸显出现代操作系统安全模型中的一个关键弱点：对已签名驱动的过度信任。  
  
参考及来源：  
https://securityaffairs.com/188388/malware/wormable-xmrig-campaign-leverages-byovd-and-timed-kill-switch-for-stealth.html  
  
![](https://mmbiz.qpic.cn/mmbiz_png/fHEm7hZn9HJ5ggbLMeo50BxxwRHMtarQTV1ia4CVndlwuxaXkqYaiaiaITzBYYDR107oKicFdGe2hbniaIA896dl9UA3yWv6tQwHGku4ic8Em9MaU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fHEm7hZn9HJHY90h1tFbqYeDpXkOlrQ97e3e62xT9AjlqWNWXdcX7Kn7hkQPsVkj0ZF6l2HMMV3pVMeRv5icMHu4kcKFvDZx2Qf5Q1xFfRQY/640?wx_fmt=png&from=appmsg "")  
  
  
