#  vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码  
胡金鱼
                    胡金鱼  嘶吼专业版   2026-02-02 06:00  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif "")  
  
近日，Node.js沙箱库vm2曝出一个高危漏洞（CVE-2026-22709），攻击者可利用该漏洞突破沙箱限制，在底层主机系统上执行任意代码。  
  
这款开源的vm2库能够创建安全执行环境，支持用户运行不受信任的JavaScript代码，且限制其访问文件系统，是实现代码隔离执行的常用工具。  
  
vm2历来被广泛应用于支持用户脚本执行的SaaS平台、在线代码运行工具、聊天机器人及各类开源项目中，仅在GitHub平台上，使用该库的项目就超20万个。不过因沙箱逃逸漏洞频发，该项目曾在2023年停止维护，且被判定为不适用于运行不受信任的代码。   
  
去年10月，项目维护者决定重启vm2项目，并发布3.10.0版本，该版本修复了当时已知的所有漏洞，同时保持“向下兼容至Node 6版本”的特性。  
  
目前该库在npm平台上依旧拥有极高的人气，过去一年间，其周下载量稳定在100万次左右。  
# 漏洞根源：数据清理机制存在疏漏  
  
此次曝出的最新漏洞，根源在于vm2库未能对处理异步操作的Promise组件实现完善的沙箱隔离，导致无法确保代码始终在独立的隔离环境中执行。   
  
vm2虽会对其自身内置Promise实现所绑定的回调函数做数据清理处理，但异步函数返回的是全局Promise对象，该对象的.then()和.catch()回调函数并未得到妥善的清理校验。  
  
项目维护者表示：“在vm2 3.10.0版本中，Promise.prototype.then和Promise.prototype.catch的回调函数清理机制可被绕过”，而这一漏洞“会让攻击者得以突破沙箱限制，运行任意代码”。   
  
据开发者介绍，vm2 3.10.1版本已对该CVE-2026-22709沙箱逃逸漏洞做出部分修复，后续推出的3.10.2版本则进一步强化了修复措施，避免漏洞被再次绕过。  
  
同时开发者还公开了相关演示代码，展示了攻击者如何在vm2沙箱中触发该漏洞、实现沙箱逃逸，并在主机系统上执行命令。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2972qMRgbUrUbVOl5bzGH11r4AOPUKIat7AFU9uem6Oib0xicTTCcAMokgajNnWxJGfSjGLOJzG8vjg/640?wx_fmt=png&from=appmsg "")  
  
已发布的漏洞利用片段  
  
鉴于在受影响的vm2版本中，CVE-2026-22709漏洞的利用方式极为简易，官方建议所有用户尽快将库版本升级至最新版。   
# 历史漏洞：沙箱逃逸问题屡发  
  
vm2此前也曾多次曝出高危沙箱逃逸漏洞，其中包括被披露的CVE-2022-36067，攻击者利用该漏洞可突破隔离环境，在主机系统上执行命令。   
  
2023年4月，研究人员发现另一同类漏洞（CVE-2023-29017），且相关利用程序随即被公开；同月晚些时候，研究人员又发布了CVE-2023-30547漏洞的利用程序，这也是影响vm2的又一个高危沙箱逃逸漏洞。   
  
其开发  
者表示，  
目前vm2的最新版本为3.10.3，所有已披露的漏洞均在该版本中得到妥善修复。  
  
参考及来源：  
https://www.bleepingcomputer.com/news/security/critical-sandbox-escape-flaw-discovered-in-popular-vm2-nodejs-library/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2972qMRgbUrUbVOl5bzGH11CxMdF2oG4AKLC04kicC2q67JQ2OOWhOAQKQ0Hza1w63h7r6ZAUxiaK5g/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2972qMRgbUrUbVOl5bzGH11gYIQ56TINXpx7zgIU4Mbzpx1ibED02J1hVK0OaGIIH3I8ibIAqicyTMqw/640?wx_fmt=png&from=appmsg "")  
  
  
