#  严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听  
胡金鱼
                    胡金鱼  嘶吼专业版   2026-01-22 06:02  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif "")  
  
安全研究人员在 Google 的Fast Pair（快速配对）协议中发现了一个严重漏洞，攻击者可利用该漏洞劫持蓝牙音频配件、追踪用户位置并窃听对话。   
  
该漏洞编号为 CVE-2025-36911，被命名为WhisperPair，影响数亿支持 Google Fast Pair 功能的无线耳机、耳塞和音箱。由于漏洞存在于配件本身，无论用户使用何种智能手机操作系统均会受到影响，这意味着使用易受攻击蓝牙设备的 iPhone 用户也面临同等风险。  
  
发现该漏洞的研究人员解释称，该漏洞源于许多旗舰音频配件对 Fast Pair 协议的不当实现。  
  
尽管 Fast Pair 规范规定蓝牙设备在非配对模式下应忽略配对请求，但许多厂商并未在产品中强制实施此检查，从而允许未授权设备在用户不知情或未同意的情况下发起配对。   
  
为启动 Fast Pair 流程，搜索者（手机）会向提供者（配件）发送一条表示想要配对的消息。Fast Pair 规范指出，如果配件未处于配对模式，则应忽略此类消息。 然而，许多设备在实际操作中并未强制实施此检查，允许未授权设备启动配对流程。在收到易受攻击设备的回复后，攻击者可以通过建立常规蓝牙配对来完成 Fast Pair 过程。  
  
攻击者可利用任何具备蓝牙功能的设备，在14米范围内，于数秒内强制与受影响的音频配件配对，且无需用户交互或物理接触。  
  
受影响的品牌包括 Google、Jabra、JBL、Logitech、Marshall、Nothing、OnePlus、Sony、Soundcore 等。   
  
配对成功后，攻击者将获得对音频设备的完全控制权，能够以高音量播放音频，或通过设备的麦克风窃听用户对话。   
  
如果该配件从未与 Android 设备配对过，攻击者还可通过将其添加到自己的 Google 账户中，利用 Google 的 查找设备网络来追踪受害者的位置。   
  
“受害者可能会在数小时或数天后看到一条不想要的追踪通知，但该通知显示的是他们自己的设备，”研究人员说道。“这可能导致用户将该警告误认为是系统 Bug 而忽略，从而使攻击者能够在较长一段时间内持续追踪受害者。”   
  
随后，Google 向研究人员颁发了最高额度15,000 美元的赏金，并在 150 天的披露期内与厂商合作发布了安全补丁。不过，他们指出，针对所有受影响设备的安全更新可能尚未全部推送。  
  
特别提醒，防御此类攻击的唯一方法是安装设备厂商提供的固件更新。在 Android 手机上禁用 Fast Pair 无法防止攻击，因为该功能无法在配件端被关闭。  
  
参考及来  
源：  
https://www.bleepingcomputer.com/news/security/critical-whisperpair-flaw-lets-hackers-track-eavesdrop-via-bluetooth-audio-devices/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib9obXIwF1RXaR0k8M8jbccdpWAicgrXc3RNlicqT1r3JnV6GtprWyLS85NpT9HhFQcAGuCR6HTBLaQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib9obXIwF1RXaR0k8M8jbccKJLNMnYSQoBMc5op5F5MuUbWL4d8jlJha6uiazcDEROaGfORrWUWicyg/640?wx_fmt=png&from=appmsg "")  
  
  
