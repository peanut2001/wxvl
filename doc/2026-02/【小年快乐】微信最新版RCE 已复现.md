#  【小年快乐】微信最新版RCE 已复现  
原创 佚名
                    佚名  星宇Sec   2026-02-10 07:07  
  
图片来自朋友圈  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQpRm6qICekzX4FyalTVjSwoXRgtRpqL1uTiaHNJTYBtEJ5XEjNqVkD15rt0ss97N4ZK7FsZibjmbQ3w2ibdTmZXscEYJjPleq012s/640?wx_fmt=png&from=appmsg "")  
  
微信 for Linux 存在RCE漏洞  
- **影响版本：微信 for Linux v4.1（Deepin 版等）**  
- ****  
- **漏洞类型：命令注入（RCE）**  
- ****  
- **触发条件：****在文件名中嵌入反引号 ` 或 $()等 shell 元字符，微信在解析文件名时会直接执行其中的命令。**  
- ****  
- **危害等级：高，可导致任意命令执行，若微信以高权限运行则可实现权限提升**  
漏洞复现过程  
  
构造恶意文件名：  
创建包含命令的文件名，如 `ls && whoami`.pdf、 `lscpu && whoami`.pdf 或 $(id).pdf。  
  
文件传输：  
通过微信文件传输助手将该文件发送到目标设备。  
  
触发执行：  
在微信中点击打开该文件，微信在解析文件名时，会将其中的命令直接传递给 shell 执行。  
  
验证结果：  
通过 strace 跟踪微信进程，可在日志中清晰看到 id、lscpu、whoami 等命令被成功调用并输出结果。  
  
  
技术分析  
  
根本原因：  
微信 for Linux 在处理文件名时，未对用户可控的文件名进行充分的安全校验或转义，直接将其作为参数传递给了系统 shell 执行。  
  
执行环境：  
命令以微信进程的权限执行。在复现截图中，微信以 root 权限运行，导致命令直接以 root 身份执行，危害极大。  
  
证据：  
strace 日志显示，微信在处理文件名时调用了系统调用，并且输出了命令执行的结果，如 uid=0(root) gid=0(root)、CPU 信息等。  
  
  
修复建议  
  
用户侧：  
1. 立即升级微信 for Linux 到最新版本，等待官方补丁。  
  
1. 避免在微信中打开来源不明的文件，尤其是文件名包含特殊字符的文件。  
  
1. 不要以 root 权限运行微信等桌面应用程序。  
  
厂商侧：  
1. 对文件名等用户可控输入进行严格的白名单校验和转义处理。  
  
1. 避免直接将用户输入传递给 shell 执行，使用安全的 API 进行文件操作。  
  
复现：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQq6Hib7ib98oZA9vVeKJO0EBKG1HzdrnpBgWU9ib3eLKibcgcolDayVGSQJB9raJm1GEvVYLf7Et1tKyNCs23ibSU2ox30795ES1NVM/640?wx_fmt=png&from=appmsg "")  
  
   
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpgRq5fOx0hBYF74eCtcNv67Exrxn8GLPyR1w5QNZoS0SNJicpGIpMNtkoKR06Znz5W4zA0gjzIxia3shUAuoVWwibxQ9n4jOcicrg/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQqJxU4VKsjvPicBKZSPyyy2YPibwHoV1fdE5lSzg2VHWabUlqpuNWBlN2EX2HpvbiaGGOU8CTVx25Sia5hQibqCziav8jrfYFviciaibBUk/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQrib6guS7QhqruojCquJFVHW8nvXHyZltM97OccKlIgNqj4UqYicRdD6CAMvI3jLHNTJdszrtt5tzu2h42vYhXXUzeBIcDncRCYc/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQo6YkJX1ySPUszTpJqKlLJwcv63vrpG5NjK0omYFiam9E0ricQtIZpdKdSxbxicGRUJ3dgicZHrPO4rLk285bguat4JAb5dI9DU3mU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQq25JcVibabbTc26coaTFesJbGuFbMQaRGRQjLX2QSBgic21lg7PE63Gs2d08bb3b7m5XIsu14UnK3aOM6fXIWia30mZwcPYBkzck/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rapaL0gDxQqUz7bCj2zLx2bG3fE1EVOYExNyb9icraY6nNZarBuLlTHWv33AS7DKy4WDUhgI68QzJ791Via9xibTQwIaoDOxkKicZM2ExuiboJq8/640?wx_fmt=png&from=appmsg "")  
  
  
马上过年了，先是发现 Linux 版微信连个最基础的命令执行漏洞都有，利用起来简单到离谱，本来还觉得见怪不怪，毕竟 Linux 端微信本来就是后娘养的，用户少就彻底摆烂，更新维护全靠随缘，烂点也没人管。但是居然在信创系统上也能复现？这就真的离谱到家了  
  
说白了不就是仗着是非主力端、用户体量小，就彻底不管不顾、不更不修吗？办公用的 QQ TIM 更是一个德行，东西能用是能用，维护跟死了没区别，全靠自生自灭。更讽刺的是，利用方式简单到可笑，就往文件名里加个反引号就能搞定。  
  
  
免责声明：  
  
本文所有信息均已提交至相关机构备案  
，涉及内容已做严格脱敏处理。文章所提及的技术均为网络安全领域的常规测试方法，不包含任何框架 0day 漏洞、新型攻击手段及未公开的技术细节。  
  
请务必遵守国家法律法规及网络安全相关规定，  
严禁利用本文所述技术从事任何非法测试、攻击等危害网络安全的行为。因传播、使用本文信息而导致的任何直接或间接损失、法律责任，均由使用者自行承担，与文章作者及发布方无涉。  
  
  
  
