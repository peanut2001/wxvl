#  【40万POC？？？】小场面，看纽克如何拿捏海量POC场景  
 WDCIA   2026-01-19 10:31  
  
#   
> ★  
> 更现代化的 POC 管理方案 | 颠覆 Nuclei 使用体验  
  
## 免责声明  
  
本文所涉及的技术、工具及相关内容仅供网络安全从业人员在已获得合法授权的目标上进行安全测试、研究和学习使用。严禁将其用于  未经授权的渗透测试、非法入侵或任何违反法律法规的行为。使用者应确保其行为符合《网络安全法》等相关法律规定。因使用本文内容所产生的任何直接或间接后果及法律责任，均由使用者本人承担，与作者及发布平台无关。  
## 用户反馈  
  
上周五收到同学的反馈，纽克1.3.2版本在扫描任务目标较多的场景下数据包解析速度缓慢、大量POC场景导入缓慢而且可能启动异常。  
  
**数据解析缓慢**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tntfgFdYwsSwibXEQQXiaLPQbuu3icyRaQY6iblM0S0Z0GcfrRaXCf9nyL8k60DBzxdY3vCMl84xberUSlBX4INVUA/640?wx_fmt=jpeg&from=appmsg "")  
  
**数据导入缓慢**  
，甚至导入后无法启动程序，启动崩溃  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tntfgFdYwsSwibXEQQXiaLPQbuu3icyRaQY0nhvcia7gNV46WxRDhKM7VOBnzGibqyhOxoAbPia0egZ24xMvRGmBPUDw/640?wx_fmt=jpeg&from=appmsg "")  
  
想到可能有大量POC的场景（2-5万），但是没想到竟有如此之多。  
  
不能忍😤，纽克的设计哲学就是简捷、快速、稳定，失去了速度一切都没有意义。必须安排。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/tntfgFdYwsSwibXEQQXiaLPQbuu3icyRaQYeYFWZJzZxxdCAvlTD5YASic7jXx2vtMe1KRW2PTQiac9Hz7ZeSJb4NqA/640?wx_fmt=png&from=appmsg "")  
## 处理过程  
  
周末开启加班模式，通过详细日志定位整个数据解析和数据导入逻辑，对关键瓶颈字符串操作进行优化和压缩，减少流程，增加缓存机制。同时对于POC编写、POC管理、扫描任务标签进行重构，引入Pinia状态管理，三端共享POC数据，减少内存压力。压缩冗余开销，对于空间占比最大的POC内容部分转移到后端查询。进一步减小内存占用。在这个过程中最重要的问题是如何兼顾搜索响应能力和内存压力。既要又要还要，全都要。  
## 优化完成后的效果  
  
连续更新发版到1.3.5版本，轻松拿捏40W POC导入场景，继续多维度管理，搜索、编辑、扫描全覆盖。继续起飞🚀🚀🚀  
  
优化完成后的效果（Windows平台测试）：  
  
<table><thead><tr><th style="color: rgb(0, 0, 0);font-size: 15px;line-height: 1.5em;letter-spacing: 0em;text-align: left;font-weight: bold;background: none left top / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;"><section><span leaf="">场景</span></section></th><th style="color: rgb(0, 0, 0);font-size: 15px;line-height: 1.5em;letter-spacing: 0em;text-align: left;font-weight: bold;background: none left top / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;"><section><span leaf="">优化前</span></section></th><th style="color: rgb(0, 0, 0);font-size: 15px;line-height: 1.5em;letter-spacing: 0em;text-align: left;font-weight: bold;background: none left top / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;"><section><span leaf="">优化后🚀</span></section></th></tr></thead><tbody><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(255, 255, 255);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">2千条数据包解析</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">25s</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">1s</span></section></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(248, 248, 248);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">1万条数据包解析</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">-</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">7s</span></section></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(255, 255, 255);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">1万POC导入</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">10min</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">16s</span></section></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(248, 248, 248);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">20万POC导入</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">4h</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">11min</span></section></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(255, 255, 255);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">40万POC导入</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">-</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">36min</span></section></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(248, 248, 248);background-image: none;background-origin: padding-box;background-position-x: left;background-position-y: top;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">40万POC导出</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">-</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">11min</span></section></td></tr></tbody></table>  
  
【2千数据包解析】  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/tntfgFdYwsSwibXEQQXiaLPQbuu3icyRaQYvuB9iaBhPgu1cJun9ScJX5OSmkfKC4SqDNXQRYk6MoIJ0omo9jqGHVw/640?wx_fmt=gif&from=appmsg "")  
  
  
【1万数据包解析】  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/tntfgFdYwsSwibXEQQXiaLPQbuu3icyRaQYNqq3xepyVmeueEfL57rAQRD6QicD7BHwOzqricopWdeWFR24wM6jy9JQ/640?wx_fmt=gif&from=appmsg "")  
  
### 40W POC导入演示  
  
  
###   
  
**那么MacOS平台是什么情况？**  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tntfgFdYwsSwibXEQQXiaLPQbuu3icyRaQYcw2HnluPMS58n8iaIrrlsJVKzb8foFrFkIayNib9njreyweSqQdibuWFw/640?wx_fmt=jpeg&from=appmsg "")  
  
留下了没有实力的泪水😭![](https://mmbiz.qpic.cn/mmbiz_png/tntfgFdYwsSwibXEQQXiaLPQbuu3icyRaQYxaJeDa14oqGSaEqYNyhj1cCOYRU4eRtAUsKE4wRySpAWN0CHzZjiabQ/640?wx_fmt=png&from=appmsg "")  
  
## MacOS机器码稳定性修复  
  
本次更新同时修复了MacOS机器码生成过程中的bug，可能导致在特殊情况下机器码发生变化。受到影响的同学随时联系客服重新导入授权或者申请重新试用。  
## 核心基础功能全免费  
  
重要的事情说三遍：  
  
POC编写、POC管理、APP管理、历史目标、蜜罐记录全免费！！！  
  
POC编写、POC管理、APP管理、历史目标、蜜罐记录全免费！！！  
  
POC编写、POC管理、APP管理、历史目标、蜜罐记录全免费！！！  
  
只有以下**原生高级模块需要授权**  
（14天试用期）：  
  
Resender - HTTP 请求重放工具  
  
网空数据管理 - FOFA/Hunter/Quake 数据获取  
  
扫描任务 - Nuclei POC 批量扫描  
  
  
永久授权现在只要￥99！！！  
  
## 产品优化  
  
使用过程中有任何问题、优化建议请随时联系客服或公众号留言，当然更建议在github提issue。正在进行活跃更新，多个功能正在添加中。（如果项目帮助到你，欢迎留个star 😊）  
  
官网链接:  
  
https://www.nucssist.top  
  
github:  
  
https://github.com/nucssistdev/nucssist  
  
客服二维码：  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/tntfgFdYwsSwibXEQQXiaLPQbuu3icyRaQYicOpibT7m1VonVfGOiasIB5FNbTrhA9M6fABichQnEkVnY4unOwDR2AzUA/640?wx_fmt=jpeg&from=appmsg "")  
  
有些小伙伴可能不知道40W POC仓库地址，公众号私信回复  40  
  获取下载地址。  
  
  
