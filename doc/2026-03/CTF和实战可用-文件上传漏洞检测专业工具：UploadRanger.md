#  CTF和实战可用-文件上传漏洞检测专业工具：UploadRanger  
原创 网安武器库
                    网安武器库  网安武器库   2026-03-13 16:25  
  
**更多干货  点击蓝字 关注我们**  
  
  
  
**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**  
  
**往期回顾**  
  
  
  
  
  
  
·[FlagHunter：CTF专用签到题Flag快速搜索工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486740&idx=1&sn=f3c6022d61fe9921c4259d639e63e7fe&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[SwordfishSuite：多平台抓包分析利器-现代化 Web 安全测试平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486734&idx=1&sn=4e5310b6adb0b5ee09c917b3bbf851d9&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[快速OpenClaw云部署教程：扣子平台接入飞书实现Ai自动办公](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486721&idx=1&sn=116249d6712546c4723075e095f75775&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[OpenClaw Exposure Watchboard：OpenClaw实例公网暴露安全监控面板](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486703&idx=1&sn=5434a2d90ceed9f066b1ae3f26228655&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[Trippy：一款高可视化的终端网络分析工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486690&idx=1&sn=6e39942109be30bf6914951fbf98840c&scene=21#wechat_redirect)  
  
  
  
  
  
  
·[GhostTrack：一站式搞定 IP / 手机号 / 用户名追踪](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486682&idx=1&sn=45ceeba3db95997dd71159bc80a9cb3c&scene=21#wechat_redirect)  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
**背景分析**  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicL4kaoMkjUPlhJm4jvZahzPzzd4Bt7GFtPqRIfpaX20QTLLR3uhiaflSYtF6ia7EXLVibnVibo3py6I1CVNmLicaiaQMslghB1hicXX4E/640?wx_fmt=png&from=appmsg "")  
  
  
    UploadRanger 是一款托管于 GitHub 平台（仓库地址：https://github.com/Gentle-bae/UploadRanger/tree/main）的开源工具类项目，其核心聚焦于文件上传场景下的功能实现与优化，旨在为开发者提供一套高效、可扩展的文件上传解决方案。该项目围绕文件上传的全流程进行技术架构设计，涵盖了上传请求处理、文件分片传输、数据校验、进度监控等关键环节的技术实现，能够适配多样化的应用场景与技术栈环境。  
  
      从技术特性来看，UploadRanger 注重代码的模块化与可复用性，通过规范化的代码组织与接口设计，降低了开发者集成文件上传功能的开发成本与维护复杂度，同时在性能层面针对大文件上传、网络波动适配等场景进行了针对性优化，具备一定的工程实践价值与技术参考意义，可为相关领域的软件开发与研究提供实践层面的借鉴。  
  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg "")  
  
安装及使用  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIJzdgIf0iaYPQvC4jia8fbvMssUwm3XQA3U4nFgEMxzXuasw2iaUEpzBNicLT8eIXAqckXS0vvqvrSGeTFaK6Y8hEDbdKNaSJ8YYM/640?wx_fmt=png&from=appmsg "")  
  
解压后是exe文件，直接双击打开即可  
  
智能扫描：自动检测上传点，分析响应内容 智能扫描界面  
  
![智能扫描界面](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJNXwOQ3nRDjiaTHLAeH1MXzqeyNPe2oMGSkaBSxucyCLuQa8LRCJ9taxb4XaD93LBW7VS9oYgKr9IrERrMvdqjycw15nVSWiaYk/640?wx_fmt=png&from=appmsg "")  
  
代理抓包：内置 HTTP/HTTPS 代理，支持拦 截、修改、重放 代理界面  
  
![代理界面](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicKMIyxlbClmPtFMCBCUe5RpAVNKichJVMiaTovEQrkKAjosU1gh3KFksFpqUPnyzZ7xdd90TfDnskLY5RgiavbfU9X9HfYiaMhlbgw/640?wx_fmt=png&from=appmsg "")  
  
Repeater：手动重放请求，调试绕过技术 Repeater界面 Repeater响应界面  
  
![Repeater界面](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJtUPaV4I0ib5Iic48ibJdUqgDyhDSUFuDpngkroia0xYt91ibWHjQvI35N20OWVpM5xdicZibVF9pOc02NBKic5ruOQicZloCwRSdFYPeU/640?wx_fmt=png&from=appmsg "")  
  
Intruder：自动化爆破，支持多种攻击模式 Intruder界面  
  
![Intruder界面](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIrOTFGWgNMUsWBAPicnYUiaufJoBfNXP03LBBNNG3gLh3ot6Ilthcc9zzuJBjkLbicdFsvAaISHdLbwYialWOLTSkCH2TicrKlYAPc/640?wx_fmt=png&from=appmsg "")  
  
263+ 绕过技术：支持各种文件类型绕过、Content-Type 绕过、WAF 绕过等 绕过技术  
  
![绕过技术](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIuvsmIKtVspBWMG4UmwLO8z9ny5xnFIrEo6yPc9MdjJicwGMR1ibYVQKMZoRUgmEIQObXxsWqrYZE3sM2dJFB9ZdGS69jmpGX5E/640?wx_fmt=png&from=appmsg "")  
  
Payload生成器：支持WebShell、Polyglot等多种载荷生成 Payload生成器  
  
![Payload生成器](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJG11NIGTVdBYiaY4gAAk4t6S5foFyjRia3M0RmaNl9fcmI3BnXZrhRliaVmLL6hqicE5sDLf2XNziam71ianGIvRmMH5HWneetTJQl4/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
github地址：  
```
https://github.com/Gentle-bae/UploadRanger/tree/main
```  
  
通过网盘分享的文件：  
  
UploadRanger.zip  
  
链接:   
  
https://pan.baidu.com/s/1R8R_rREhxyW8idUtJKHOiQ?pwd=e7k2   
  
提取码: e7k2   
  
--来自百度网盘超级会员v3的分享  
  
   
  我们  
新组建了交流群，如有感兴趣的师傅可以加入共同交流！！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicIZKNAMQPZwYT5gdofmTeFPBiaU6MJsjeOKX6aKUVOoONNQCich1t7wUFrAFkHmDve5dERdJ4gUOsk78Z2A8Wayn2v6Kx7oTL0DI/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=12 "")  
  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
