#  不止于传马：将文件上传漏洞转化为持久性反向Shell通道  
aiki
                    aiki  W-L安全社   2026-02-03 09:09  
  
下午六点零一分，我按下指纹机。屏幕上跳出“17:01”的绿色字符时，我听见血管里传来冰面开裂的声音。  
  
这是我第一千三百二十七次打卡下班。  
  
地铁像一条钢铁盲肠，吞吐着面色相似的我们。车厢里，三十岁的男人们保持着一拳的安全距离，却共享着同一种疲惫的弧度——颈椎前倾，肩膀塌陷，手机屏幕的光映在无波的眼瞳里。西装是现代的甲胄，领带是优雅的绞索。我们被精心打造成社会齿轮，严丝合缝，连叹息都计算好了分贝。  
  
公寓楼下的便利店，店员永远在整理关东煮。我拿走第N份照烧鸡排饭，他头也不抬。微波炉“叮”的一声，是这座城市给我的、仅有的温热回音。  
  
改变始于一个荒诞的早晨。报告写到第三版，电脑屏幕右下角弹出新闻：本市最后一家古籍书店今日歇业。配图里，店主是个白发老者，坐在满地纸箱间，手里摩挲着一本《诗经》。标题是：“纸页的黄昏”。我心里某根弦，“啪”地断了。那些书页曾是一个少年整个世界的边界。  
  
递交辞呈时，上司像看一个故障零件：“三十了，玩这种情怀？”我没有解释。解释需要语言，而我的语言系统早已被KPI和PPT格式绑架。我只想找回自己的语法。  
  
我回了南方小镇。用所有积蓄，盘下巷口一家即将倒闭的花店。它旧得像一封寄错年代的信，木门推开时，铜铃的响声喑哑。  
  
第一个月，几乎没有客人。我在旧书市场淘来一堆泛黄的园艺书，对照着辨认每一种植物的脾性。薄荷需要光但不能直晒，绣球嗜水但怕涝根。给一盆奄奄一息的栀子换土时，我在板结的土块深处，触到它顽强挣扎的、雪白的根须。那一刻，手指传来细微的、搏动般的触感。我第一次感到，自己在“触摸”生命，而非屏幕或纸张。  
  
花店叫“野有蔓草”。一个老婆婆推门进来，看到招牌，轻声念出下一句：“零露漙兮。”她买了一小束茉莉，用方言说：“我老头子年轻时，总念这个。”她的皱纹里，藏着被诗句浸润过的光泽。那天黄昏，我坐在店门口，看夕阳把晾晒的蓝染布浸透。晚风路过，带来不远处中学的广播声，隐约是《蒹葭》的吟诵。空气里有尘土、植物汁液和旧时光的气味。我的感官，像是昏睡多年后骤然苏醒。  
  
我不再出售标准化花束。有人为病中的母亲而来，我配佛手、康乃馨与几枝带露的萱草，写“焉得谖草，言树之背”。有女孩将远行，我包一束柳枝与蒲公英，附上《古诗十九首》里“各在天一涯”的句子。花与诗，都成了渡人的舟楫。我的小店，成了小镇记忆的收容所。王婶来买给女儿出嫁的百合，会讲她当年一辆自行车嫁过来的事；李老师挑文竹，会聊起他那些“飞”到天涯海角的学生。  
  
一个闷热的午后，暴雨将至。我正将一批受潮的旧书搬出晾晒。风穿堂而过，翻动书页，也拂动悬垂的常春藤。墨香与草木清气缠绕上升。门外，收废品的老师傅摇着铜铃经过，巷子那头，传来孩童追逐的清脆笑声。我直起腰，汗水沿着脊沟滑下，却感到一种前所未有的、扎实的疲惫。这疲惫不同于格子间里被抽空的虚无，它结结实实地来自四肢百骸，让人清楚地感知到“我”存在于此刻此地。  
  
我终于懂得，所谓“找到自我”，并非掘出一个金光闪闪的内核，而是在与具体生活的摩擦与交融中，确认自己存在的形态与温度。如一块粗粝的卵石，在时光的溪流里，被冲刷出独属于自己的纹路与光泽。我不再是那个在钢铁森林里逐秒计时的幽魂。我是花店的守夜人，是植物与诗行的摆渡者。  
  
夜深了。我给新到的雀梅喷完水，准备打烊。玻璃门上，映出一张三十岁男人的脸。神情平和，指尖染着洗不掉的、青草汁液般的淡绿。门外，小镇沉入安眠；门内，无尽夏在暗处悄然结着花苞。  
  
花店永不眠。找到自我的人，也是。  
- 通过js+目录扫描发现后台的管理地址，是的；它是开源cms框架wordpress：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XN91DpbJN7aMS1R5T0ibjgxmFKHSfCTj27GsVKzWYTG0qudPEYaY9hLM4WITZSA0pQiamtxaiaOCibhntUbxXPJmcQ/640?wx_fmt=png&from=appmsg "")  
- 使用wpscan扫描探测，发现如下两个接口一个是注册；另一个是目录遍历：  
  
WPScan 是 Kali Linux 中默认集成的一款强大的漏洞扫描工具，专门用于检测 WordPress 网站的安全漏洞。它采用 Ruby 编写，支持扫描 WordPress 核心、插件和主题的漏洞，同时还能枚举用户名和进行暴力破解。  
  
注册接口：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XN91DpbJN7aMS1R5T0ibjgxmFKHSfCTj2mXOoJbtcTGK2qoO30DBM8TJsbo0ibCU5p8p7ltbjty247oD5AiaCsZwA/640?wx_fmt=png&from=appmsg "")  
  
目录遍历接口：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XN91DpbJN7aMS1R5T0ibjgxmFKHSfCTj2ZkoiaOTqib7zs0IR0vpdknwtiaPJaCDxBOLEQTOlo68OFSEYCvnia8q2nA/640?wx_fmt=png&from=appmsg "")  
- 突破口；注册登录后台后发现"Add Plugins"可上传文件，尝试文件上传：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XN91DpbJN7aMS1R5T0ibjgxmFKHSfCTj2Vv5Uy18Faoiazib5YqS8cqiaxfIibvLuUTcpPWibib2q2cktALlROhrROiadA/640?wx_fmt=png&from=appmsg "")  
  
上传反向 Shell ；**绕过入站防火墙限制 + 提供交互式 Shell：**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XN91DpbJN7aMS1R5T0ibjgxmFKHSfCTj29tPCj7axkTv4ngSia2lFWZ2S8B34rTicBfR0I9WXy6zVfsKwdC41fAhw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XN91DpbJN7aMS1R5T0ibjgxmFKHSfCTj2WX9K4uQR5kZfmsicEnzwuc2CWBSqJhBfM7oYiaPPUPyYPhkEhkHFj7qA/640?wx_fmt=png&from=appmsg "")  
  
通过wpscan扫描出来的目录遍历接口，上传成功可直接在/uploads目录下看到木马“php-reverse-shell.jsp”：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XN91DpbJN7aMS1R5T0ibjgxmFKHSfCTj2M6BibDUoiaHKJBse2uyvumTr6xJaOwhvj2tEuNALXkRXcjlEicY5qlFcw/640?wx_fmt=png&from=appmsg "")  
  
通过  
点击该文件即可触发shell反弹，成功拿到服务器权限：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/XN91DpbJN7aMS1R5T0ibjgxmFKHSfCTj2QOy2UOZryLXybqCibwLNkbl4KFH5ZNBSafq6ckoYOHv3wcdJWI2u2Zg/640?wx_fmt=png&from=appmsg "")  
  
  
免责声明  
：  
1. 本篇文章，仅用于读者学习网络安全知识，提醒大家防范恶意攻击。  
  
1. 如果读者利用本篇文章的知识，对目标进行恶意攻击，所造成的后果和损失，均由漏洞利用者负责，公众号“  
W-L  
安全  
社  
”及作者本人将不承担任何法律责任。  
  
