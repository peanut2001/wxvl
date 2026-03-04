#  谷歌紧急修复Android 129个漏洞，含正遭利用的0Day  
 FreeBuf   2026-03-04 10:06  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1CKKdvlEN8LlSA7VynOoicdAicTHWnhu2xKw1fl7GUvMzZ6gpSEgpicrV1YFNHhhAIvvdGygzfayCGYtibl4GQ487pZkibMRhMpY04/640?wx_fmt=jpeg&from=appmsg "")  
##   
  
Google 已发布备受期待的 2026 年 3 月 Android 安全公告，为整个 Android 生态系统的 129 个安全漏洞提供关键修复。此次大规模更新是近年来单月发布补丁数量最多的一次。  
  
  
更新部署采用两个独立的安全补丁级别（2026-03-01 和 2026-03-05），使设备制造商能够先快速修复核心 Android 平台缺陷，再处理复杂的硬件特定问题。  
  
  
本次公告解决的最严重威胁是一个正遭有限针对性攻击利用的高危 0Day 漏洞。  
##   
  
**Part01**  
## 正遭利用的0Day：  
## CVE-2026-21385  
  
  
3月更新的焦点是开源 Qualcomm Display 组件中的高危 0Day 漏洞（CVE-2026-21385）。技术分析表明，该问题源于内存分配对齐过程中因整数溢出或回绕错误导致的内存损坏。  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0iafeyU2GFYkBUn9xfGzCm3dHTn6BzoUsItl2xdibs6GaUUQ8RibJ07XHBfUb9BMF3BlzwZneLSsCicmy7g7gXawLvg5g6FHVyqgA/640?wx_fmt=png&from=appmsg "")  
  
  
Google 和高通均已确认该漏洞在野遭到有限针对性利用。由于此内存损坏漏洞存在于硬件显示驱动中，攻击者成功利用后可绕过严格安全边界并操控关键内存结构。  
  
  
使用受影响高通芯片组 Android 设备的用户面临更高风险，必须优先立即应用此补丁。  
  
  
除 0Day 外，2026-03-01 补丁级别还修复了多个无需用户交互即可被攻击者利用的关键平台漏洞。其中最危险的是核心 System 组件中的远程代码执行（RCE）漏洞（CVE-2026-0006），远程攻击者成功利用后无需额外执行权限即可运行恶意代码。  
  
  
此外，Android Framework 组件修复了关键权限提升（EoP）漏洞（CVE-2026-0047）。网络犯罪分子常将此类漏洞与初始 RCE 攻击串联使用，使恶意应用获得对受控设备的高级管理权限。  
  
  
**Part02**  
## 供应商特定组件漏洞  
  
  
次要的 2026-03-05 补丁级别专门修复闭源和开源第三方硬件组件中的 66 个漏洞：  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0AhwfibXQA92kp4VzMBXXDabFcALyrHmtax4YvE51UaVILk0fLc2AGbycEJ9JtuvaUB3G5nqAlSm7ossLI0EWKOoo4LtVa98ic4/640?wx_fmt=png&from=appmsg "")  
  
  
Google 与主要供应商合作修复了影响 Arm、Imagination Technologies、联发科和紫光展锐硬件的严重漏洞。这些修复涉及设备调制解调器、虚拟机监控程序和 GPU 驱动中深埋的众多权限提升和信息泄露漏洞。  
  
  
面对高级持续性威胁（APT），这份庞大的硬件级补丁清单突显了保护复杂移动供应链的持续挑战。用户应通过系统设置验证设备的安全补丁级别——运行 2026-03-05 补丁级别的设备可完全防御本公告所述 129 个漏洞及以往安全更新修复的问题。  
  
  
Google 将在 48 小时内向 Android 开源项目（AOSP）代码库发布相应源代码补丁，确保更广泛生态系统的长期平台稳定性。同时，Google Play Protect 将继续为使用 Google 移动服务的用户提供主动防御，持续监控并阻止试图利用这些新披露漏洞的潜在有害应用。  
  
  
**参考来源：**  
  
Android Security Update – Patch for 129 Vulnerabilities and Actively Exploited Zero-Day  
  
https://cybersecuritynews.com/android-security-update-march/  
  
  
###   
###   
###   
  
**推荐阅读**  
  
[](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)  
  
  
### 电台讨论  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg "")  
  
****  
  
  
  
  
