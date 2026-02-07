#  豆包ai 命令执行？  
原创 数字幽灵安全团队
                    数字幽灵安全团队  数字幽灵安全团队   2026-02-07 09:17  
  
#### 免责申明：本文内容为学习笔记分享，仅供技术学习参考，请勿用作违法用途，任何个人和组织利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责，与作者无关！！！  
  
最近用豆包ai比较多，问问题问着出现了端倪！！！  
  
让它执行命令他竟然执行了  
  
![Pasted image 20260207170157.png](https://mmbiz.qpic.cn/mmbiz_png/njzTo1lbicaicIg3ERgiaWE5yUg8SR5PjiaNDxES9HJkbAtkD8Z2fxKnseR4eTwCdTA0MlYwleQiaAeSEmdoyJdPAUSyDwCLXmcibrRUnE89DxBTw/640?wx_fmt=png&from=appmsg "")  
  
于是我验证是否是模型出现的幻觉，以前某书也是出现了评论区执行命令的情况，听说是模型幻觉，于是我尝试多次，发现他在自己执行python 代码的时候确实是执行了，但是如果他没有出现  
已生成代码并执行的就跟小红书类似 豆包自己生成  
  
![Pasted image 20260207170045.png](https://mmbiz.qpic.cn/mmbiz_png/njzTo1lbica9XS89Xz47m6p9Wys7BWjS4KRvMxictRE1VKVnN7PyEtfGicLcIcJgSplIb37gickAQbiabso5zmVgdawPMGpumRKKtEicSVBLvZX78/640?wx_fmt=png&from=appmsg "")  
  
最后跟字节审核人员沟通，第一点应该是我刚说的第二点情况，第二点就是我第一点的情况；最终确定应该是执行命令了，但是这是业务方故意这么做的。其他的ai我也尝试发现能通过python执行命令，但是应该都是这种情况，到此结束。  
发出来给大家避雷，不然也兴致勃勃随意一问以为拿下了。  
![Pasted image 20260207170547.png](https://mmbiz.qpic.cn/mmbiz_png/njzTo1lbicaicZt8FGsVHloboM1RWibC2m6IoGKzIktc06qhicAp0WtGJx79z7euyyPcsUjWTuRLyY5wEfDGr1iaY89euibfEQiaZ0QFQrH5UDdPGs/640?wx_fmt=png&from=appmsg "")  
  
  
  
