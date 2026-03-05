#  深度追踪“Coruna”：一款高端 iOS 漏洞武器库的“暗网”漂流记  
骨哥说事
                    骨哥说事  骨哥说事   2026-03-05 06:38  
  
<table><tbody><tr><td data-colwidth="557" width="557" valign="top" style="word-break: break-all;"><h1 data-selectable-paragraph="" style="white-space: normal;outline: 0px;max-width: 100%;font-family: -apple-system, system-ui, &#34;Helvetica Neue&#34;, &#34;PingFang SC&#34;, &#34;Hiragino Sans GB&#34;, &#34;Microsoft YaHei UI&#34;, &#34;Microsoft YaHei&#34;, Arial, sans-serif;letter-spacing: 0.544px;background-color: rgb(255, 255, 255);box-sizing: border-box !important;overflow-wrap: break-word !important;"><strong style="outline: 0px;max-width: 100%;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="color: rgb(255, 0, 0);"><strong><span style="font-size: 15px;"><span leaf="">声明：</span></span></strong></span><span style="font-size: 15px;"></span></span></strong><span style="outline: 0px;max-width: 100%;font-size: 18px;box-sizing: border-box !important;overflow-wrap: break-word !important;"><span style="font-size: 15px;"><span leaf="">文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。</span></span></span></h1></td></tr></tbody></table>#   
  
#   
  
****# 防走失：https://gugesay.com/archives/5389  
  
******不想错过任何消息？设置星标****↓ ↓ ↓**  
****  
#   
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg "")  
  
> 从一个秘密间谍工具到批量网络诈骗武器，顶级漏洞利用框架如何“飞入寻常百姓家”？  
  
  
**引言**  
  
谷歌威胁情报研究团队近期发现了一个全新且能量巨大的漏洞利用工具包，它主要针对运行 iOS 13.0（发布于2019年9月）至 iOS 17.2.1（发布于2023年12月）版本的苹果 iPhone 设备。这款被其开发者内部称为“科鲁尼亚”的漏洞武器，包含了**五套完整的 iOS 攻击链**  
和总计**23个不同的漏洞利用模块**  
。这套工具包的核心技术价值在于其覆盖了 iOS 系统各个层面的漏洞，其中最高级的利用手法采用了未公开的利用技术和安全缓解措施的绕过方法。  
  
“科鲁尼亚”漏洞武器的发现，再次印证了尖端攻击能力的扩散路径。在整个2025年，谷歌威胁情报研究团队追踪到它最初被监控软件供应商的客户用于高度定向的攻击行动。随后，观察到疑似俄罗斯间谍组织的UNC6353将其部署在针对乌克兰用户的“水坑攻击”中。  
  
当我们最终获取到这套工具的完整版本时，发现它正被来自一些以经济利益为驱动的威胁组织UNC6691用于大规模的钓鱼活动中。这套武器是如何在不同的攻击者之间流转传播的尚不清楚，但这无疑暗示着“二手”零日漏洞武器交易市场的活跃程度。除了已识别的这些漏洞利用手法，显然已有多个威胁组织掌握了可以复用并加以改造、适配新发现漏洞的高级利用技术基础。  
  
遵循我们的漏洞披露政策，我们决定分享这项研究，旨在提高行业安全意识并推动整体安全水平的提升。我们已经将所有识别的相关网站和域名添加到了安全浏览服务中，以保护用户免受进一步的攻击。需要强调的是，“科鲁尼亚”漏洞工具包对最新版本的 iOS 系统无效，因此我们强烈建议 iPhone 用户将自己的设备更新到最新的 iOS 版本。在无法更新的情况下，建议启用锁定模式以获得增强的安全保护。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZgsqumUZzsyx4J3R6zz3Yybt8tszQJq13gT4QDzDMxrSpKZK1fwibek09cDhFS8jmHajX7NMuA3pqTqfjRwiaZiblZAby121GjrLQ/640?wx_fmt=png&from=appmsg "")  
  
图1：科鲁尼亚iOS漏洞武器包的时间线  
## 第一阶段：揭开面纱——商业监控软件的影子  
  
2025年2月，我们截获了一部分由某监控软件公司客户使用的iOS攻击链组件。这些攻击代码被集成在一个前所未见的JavaScript框架中。该框架运用了简单但独特的JavaScript混淆技术来隐藏其真实意图。  
```
[16, 22, 0, 69, 22, 17, 23, 12, 6, 17].map(x => {return String.fromCharCode(x ^ 101);}).join("")
```  
```
i.p1=(1111970405 ^ 1111966034);
```  
  
该JS框架使用此类结构对字符串和整数进行编码  
  
该框架首先启动一个指纹识别模块，收集大量数据点来判断设备是否真实、具体的iPhone型号以及运行的是哪个iOS软件版本。基于收集到的数据，它会加载相应的WebKit远程代码执行漏洞利用模块，紧接着是指针验证码绕过模块，如右图中去混淆后的JavaScript代码所示。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhQ3bt7v08d2J7Bws2seXJb2DvRSBicOcJoGBK9l1zMV3zkv9XoC7PLTnL37UfSCjuQalH2NGyCZh8XI7Oq4ia7WVRh6awmRoMY8/640?wx_fmt=png&from=appmsg "")  
  
图2：去混淆后的科鲁尼亚漏洞武器包JavaScript代码  
  
那时，我们成功获取了针对运行iOS 17.2系统的设备所投递的WebKit远程代码执行模块，并确认它就是漏洞编号CVE-2024-23222。这个漏洞曾是一个已被发现的零日攻击漏洞，苹果公司在2024年1月22日发布的iOS 17.3版本中进行了封堵，但并未在公告中指名感谢外部研究人员。下图展示了在真实攻击中捕获到的远程代码执行模块的开头部分，并附上了我们的标注。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZh49Ria5O6Zpn0gia6I1stn49xFD52UpiawF3WcLoK36E8tdhfBTzMb0IKsYiaiahdojDsPqXwW4mmB0aRdZjndicr2dpzTHl8Znbhmc/640?wx_fmt=png&from=appmsg "")  
  
图3：利用CVE-2024-23222的RCE漏洞在真实攻击中的投递示例  
## 第二阶段：扩散与升级——高级持续性威胁（APT）组织接手  
  
时间来到2025年夏季。我们发现同一个JavaScript框架被托管在 cdn.uacounter[.]com  
 网站上，该网站的内容被作为隐藏的 iFrame 加载到了多个遭遇入侵的乌克兰网站上，这些网站涵盖了从工业设备、零售工具到本地服务、电子商务等各类平台。这个框架仅定向投递给来自特定地理位置的部分iPhone用户。  
  
框架的代码完全一致，投递的攻击模块集合也相同。在服务器被关闭之前，我们成功收集了多个WebKit远程代码执行模块，包括 CVE-2024-23222、CVE-2022-48503 和 CVE-2023-43000。我们及时发出预警，并与乌克兰的计算机应急响应小组 CERT-UA 协作，清理了所有已发现的被入侵网站。  
## 第三阶段：工具包的“大放送”——地下金融诈骗团伙的狂欢  
  
到了2025年底，我们在数量非常庞大的伪造中文网站上识别出了这个JavaScript框架。这些网站大多与金融相关，它们投放了完全相同的iOS漏洞武器包。这些网站试图诱使用户使用iOS设备访问，如下图所示，一张截图显示了一个虚假的WEEX加密货币交易所网站的弹窗。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZjSvUSuXacjzYCvFR4iaDxElRkG7PjMH3xRBU72ugLh2Bk2In5nc3yiclc037u0TYlXBcEMdqFoxraxVicdceJ0a3icUns0Pu5gBuw/640?wx_fmt=png&from=appmsg "")  
  
图4：一个虚假加密货币交易所网站上的弹窗，试图诱导用户触发漏洞  
  
无论用户的真实地理位置如何，只要通过iOS设备访问这些网站，一个隐藏的 iFrame 就会被注入页面，随之投递漏洞武器包。例如，下图展示了从 3v5w1km5gv[.]xyz  
 上发现的，与先前版本相同的CVE-2024-23222利用模块。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/TKdPSwEibsZhed0pmXadIEv12ktONKwScPcnicgf3FQCzibWQ1SNE1T6wCtU4OJl5FSbWwLv9XTMT8xbAszh0pvguz9TUruQxFuyVOw8W8NMXY/640?wx_fmt=png&from=appmsg "")  
  
图5：从一个诈骗网站恢复的 CVE-2024-23222 漏洞利用代码截图  
  
我们获取了所有经过混淆的攻击模块，包括其最终的载荷。在进一步深入分析时，我们发现了一个罕见情况：攻击者部署的居然是漏洞武器包的调试版本，这使得全部漏洞利用模块——包括它们内部的代号——都以明文形式泄露了。正是通过这次机会，我们才得以知晓这个漏洞武器包在内部很可能被称为“科鲁尼亚”（Coruna）。  
  
总体上，我们收集了数百个样本，涵盖了总计五套完整的iOS攻击链。这款漏洞武器包能够针对各种在2019年9月发布的 iOS 13.0 到 2023年12月发布的 iOS 17.2.1 版本之间运行的iPhone型号。  
## 科鲁尼亚漏洞武器包：精密的工程化攻击框架  
  
围绕这套漏洞武器包构建的框架工程化水平极高；各个攻击模块间的衔接非常自然，并整合了通用的工具和利用框架。该工具包执行以下独特的操作：  
- 精准规避：如果检测到设备处于“锁定模式”，或者用户正在使用“无痕浏览”模式，工具包会自动放弃攻击。  
  
- 密钥生成：使用一个独特的、硬编码的Cookie为沿途每个步骤生成资源URL。  
  
- 资源定位：资源采用哈希值标识，需要通过 SHA256(硬编码Cookie + ID) [:40]  
 的算法派生出最终的URL。  
  
- 传输策略：远程代码执行和指针验证码绕过模块以非加密方式传输。  
  
该工具包包含一个二进制加载器，用于在WebKit渲染引擎内成功实现远程代码执行后，加载合适的后续攻击链。这里的二进制载荷具有以下特征：  
- 载荷具备独特的元数据，明确指示其真实用途、支持的芯片型号和iOS版本范围。  
  
- 从以 .min.js 结尾的URL路径提供。  
  
- 使用ChaCha20算法进行加密，每个数据块使用独立的密钥。  
  
- 采用自定义的文件格式进行打包，文件头以 0xf00dbeef 为标志。  
  
- 使用Lempel–Ziv–Welch（LZW）算法进行压缩。  
  
下图从网络流量的角度，展示了在浏览某个虚假金融网站时，一台运行iOS 15.8.5的iPhone XR设备被感染的全过程，我们对攻击链的不同阶段进行了标注。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/TKdPSwEibsZiaVQKvZ4JpkIbzFxg9YglAOx10xZ2JR6YDM4EibJ14NW3axSU0kbPmL1oLqB26AySoUuH4OUNoXEGk1KS23LNnXFjtcbibV7eLug/640?wx_fmt=png&from=appmsg "")  
  
图6：在iOS 15.8.5系统上投递的科鲁尼亚攻击链网络流量图  
## 技术与代号：漏洞武器的“全家福”  
  
这套漏洞武器包的核心技术价值就体现在其全面覆盖的iOS漏洞利用集合上。这些利用模块包含了丰富的说明文档，如文档字符串和注释，均为地道的英文撰写。其中最先进的模块采用了未公开的利用技术和系统缓解措施的绕过方法。下表汇总了我们针对不同攻击链正在进行的技术分析概览。请注意，鉴于全面调查仍在进行中，某些漏洞与CVE编号的关联可能在未来有所修正。总计有覆盖了从iOS 13到 iOS 17.2.1 版本的23个漏洞利用模块。  
<table><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><strong style="font-weight: bold;color: black;"><span leaf="">Type</span></strong></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><strong style="font-weight: bold;color: black;"><span leaf="">Codename</span></strong></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><strong style="font-weight: bold;color: black;"><span leaf="">Targeted versions (inclusive)</span></strong></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><strong style="font-weight: bold;color: black;"><span leaf="">Fixed version</span></strong></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><strong style="font-weight: bold;color: black;"><span leaf="">CVE</span></strong></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent R/W</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">buffout</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">13 → 15.1.1</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.2</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2021-30952</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent R/W</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">jacurutu</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.2 → 15.5</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.6</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2022-48503</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent R/W</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">bluebird</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.6 → 16.1.2</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.2</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent R/W</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">terrorbird</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.2 → 16.5.1</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.6</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2023-43000</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent R/W</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">cassowary</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.6 → 17.2.1</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.7.5, 17.3</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2024-23222</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent PAC bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">breezy</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">13 → 14.x</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">?</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent PAC bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">breezy15</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15 → 16.2</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">?</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent PAC bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">seedbell</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.3 → 16.5.1</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">?</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent PAC bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">seedbell_16_6</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.6 → 16.7.12</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">?</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent PAC bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">seedbell_17</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">17 → 17.2.1</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">?</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent sandbox escape</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">IronLoader</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.0 → 16.3.116.4.0 (&lt;= A12)</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.7.8, 16.5</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2023-32409</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">WebContent sandbox escape</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">NeuronLoader</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.4.0 → 16.6.1 (A13-A16)</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">17.0</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PE</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Neutron</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">13.X</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">14.2</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2020-27932</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PE (infoleak)</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Dynamo</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">13.X</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">14.2</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2020-27950</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PE</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Pendulum</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">14 → 14.4.x</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">14.7</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PE</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Photon</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">14.5 → 15.7.6</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.7.7, 16.5.1</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2023-32434</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PE</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Parallax</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.4 → 16.7</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">17.0</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2023-41974</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PE</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Gruber</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.2 → 17.2.1</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.7.6, 17.3</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PPL Bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Quark</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">13.X</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">14.5</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PPL Bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Gallium</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">14.x</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.7.8, 16.6</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2023-38606</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PPL Bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Carbone</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">15.0 → 16.7.6</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">17.0</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">No CVE</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: white;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PPL Bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Sparrow</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">17.0 → 17.3</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.7.6, 17.4</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2024-23225</span></p></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">PPL Bypass</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">Rocket</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">17.1 → 17.4</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">16.7.8, 17.5</span></p></td><td style="border: 1px solid #ccc;padding: 5px 10px;text-align: left;font-size: 14px;min-width: 85px;"><p style="padding-top: 8px;padding-bottom: 8px;margin: 0;line-height: 26px;color: black;font-size: 14px;"><span leaf="">CVE-2024-23296</span></p></td></tr></tbody></table>  
特别值得注意的是，其中的 Photon 和 Gallium 模块所利用的漏洞，正是卡巴斯基在2023年发现的“三角测量”行动中使用过的零日漏洞。科鲁尼亚漏洞武器包还嵌入了可复用的模块，以简化对上述漏洞的利用过程。例如，存在一个名为 rwx_allocator  
 的模块，它采用多种技术来绕过用户态内存中阻止分配可读、可写、可执行内存页的各类缓解措施。内核层面的攻击模块同样也内嵌了各种内部组件，使其能够避开内核层面的保护措施，例如内核模式的指针验证代码。  
## 攻击终点：窃取一切的“等离子”加载器  
  
在攻击链的末端，一个名为 PlasmaLoader  
 的“后渗透”模块（谷歌威胁情报研究团队将其追踪为 PLASMAGRID）登场了。它冒用 com.apple.assistd  
 这个标识符，负责与漏洞利用模块建立的内核组件进行通信。这个加载器会将其自身注入到 powerd  
——一个在iOS系统中以root权限运行的后台服务进程中。  
  
被植入的最终载荷并非我们通常预期的那种来自监控软件供应商的间谍工具所具备的功能，而是专门用于窃取财务信息。这个载荷可以从磁盘上的图像文件中解析出二维码内容。它还包含一个分析文本块的模块，用于查找BIP39助记词序列，或搜索如“助记词备份”或“银行账户”等非常具体的关键词。如果在内置的备忘录应用中发现了此类文本，就会将其发送回攻击者的指挥控制服务器。  
  
更重要的是，这个载荷具有远程收集并运行额外模块的能力。模块配置信息从 http://<C2服务器地址>/details/show.html  
 获取。配置信息以及其他附加模块都被压缩成受7-ZIP保护的加密归档文件，使用一个独特的硬编码密码。配置信息采用JSON格式编码，本质上就是一个包含模块名称、对应的下载URL、安全哈希值以及文件大小的列表。  
```
{  "entries": [    {      "bundleId": "com.bitkeep.os",      "url": "http://<C2 URL>/details/f6lib.js",      "sha256": "6eafd742f58db21fbaf5fd7636e6653446df04b4a5c9bca9104e5dfad34f547c",       "size": 256832,      "flags": {        "do_not_close_after_run": true      }    }    ...  ]}
```  
  
不出所料，绝大多数被发现的模块都呈现出统一的设计风格；它们无一例外地都对特定应用程序进行了函数挂钩操作，目的就是为了窃取加密货币钱包或敏感信息。这些目标应用程序包括：  
- com.bitkeep.os  
 (比特派)  
  
- com.bitpie.wallet  
 (比特派钱包)  
  
- coin98.crypto.finance.insights  
 (Coin98)  
  
- org.toshi.distribution  
  
- exodus-movement.exodus  
 (出埃及记钱包)  
  
- im.token.app  
 (imToken)  
  
- com.kyrd.krystal.ios  
 (Krystal)  
  
- io.metamask.MetaMask  
 (MetaMask)  
  
- org.mytonwallet.app  
  
- app.phantom  
 (幻影钱包)  
  
- com.skymavis.Genesis  
  
- com.solflare.mobile  
 (Solflare)  
  
- com.global.wallet.ios  
  
- com.tonhub.app  
  
- com.jbig.tonkeeper  
 (Tonkeeper)  
  
- com.tronlink.hdwallet  
 (波场钱包)  
  
- com.sixdays.trust  
 (Trust Wallet)  
  
- com.uniswap.mobile  
 (Uniswap)  
  
所有这些模块内部都包含了完善的中文日志记录语句，例如：  
```
<PlasmaLogger> %s[%d]: CorePayload 管理器初始化成功，尝试启动...
```  
  
该日志字符串显示CorePayload管理器已成功初始化  
  
有些注释，例如下面这行，甚至还包含表情符号，并且表述方式暗示它们可能由大型语言模型辅助生成。  
```
<PlasmaLogger> %s[%d]: [PLCoreHeartbeatMonitor] ✅ 心跳监控已启动 (端口=0x%x)，等待 CorePayload 发送第一个心跳...
```  
  
网络通信基于HTTPS协议进行。被窃取的数据在使用AES算法加密后，以POST请求形式发送，加密密钥为一个静态字符串的SHA256哈希值。部分HTTP请求中包含了额外的自定义头部信息，例如sdkv  
或x-ts  
，后跟一个时间戳。该植入程序内置了一个预置的指挥控制服务器列表，并具备在服务器无响应时的备用回退机制。程序内部嵌入了一个自定义的域名生成算法。这个算法以字符串“lazarus”作为种子，生成一系列可预测的域名。这些域名长度固定为15个字符，并使用顶级域名.xyz。攻击者会利用谷歌的公共DNS解析器来验证生成的域名是否处于活动状态。  
## 启示与防御：从个人到行业的思考  
  
**1. 高级武器的“平民化”趋势：**  
“科鲁尼亚”的演变历程清晰地展示了一幅技术扩散图：最初由具备雄厚财力的商业监控软件公司开发，用于国家支持的精准间谍活动。随后，这些代码可能因交易、仿制或泄露，被国家层面的黑客组织获取用于地缘政治攻击。最终，这些技术降维流传到以经济犯罪为目的的网络犯罪团伙手中，用于大规模、低成本的金融诈骗。这意味着，普通用户面对的威胁源头，其技术起点正在越来越高，防御难度也相应增大。  
  
**2. “零日漏洞”交易市场的影子：**  
攻击框架在不同组织间的快速流转，暗示着一个活跃的、地下的“二手”甚至“N手”漏洞武器交易市场的存在。一个漏洞利用链在经过最初的高价值客户使用后，其代码可能被多次转售、重构和“翻新”，目标也从国家级目标转向普通民众。这对漏洞的生命周期管理和防御窗口期提出了前所未有的挑战。  
  
**3. 技术防护：深度优先于广度：**  
从“科鲁尼亚”的攻击模块列表可以看出，其成功依赖于对iOS系统多个安全层级的深度突破：WebKit引擎的渲染漏洞、内核的沙箱逃逸、绕过指针验证码、权限提升直至绕过层层防护机制。这意味着传统的、基于“黑名单”或已知特征的防御方式（如签名验证）效果有限。有效的防御必须关注这些技术演变的本质——对系统安全架构的持续攻击。苹果公司通过推出“锁定模式”这样的功能，正是试图从设计上阻断这种复杂攻击所依赖的攻击面。  
## 对普通用户的防御建议与工具补充  
1. **系统更新是绝对的第一道防线**  
：正如谷歌报告所强调的，该漏洞武器包对最新版本的iOS无效。保持系统处于最新状态，是防御此类已知和未知漏洞攻击最有效、最根本的手段。务必开启“系统自动更新”。  
  
1. **高危用户启用“锁定模式”**  
：如果你身处高危行业或地区，或者认为自己可能成为定向攻击的目标，强烈建议在“设置 > 隐私与安全性 > 锁定模式”中启用该功能。它会严格限制特定功能和网站特性，从而极大地压缩此类复杂漏洞包的攻击面。  
  
1. **警惕不寻常的网络提示**  
：攻击链往往始于诱导用户访问恶意网站。对于来源不明的链接、弹出式通知（如图4所示，尤其是要求切换到特定设备访问的提示）要保持高度警惕。不要轻易点击不明来源的二维码。  
  
1. **应用层面的谨慎**  
：尽量从苹果官方的App Store下载应用，特别是金融、加密货币钱包等敏感应用。审阅应用权限，不轻易授予不必要的访问权限。定期检查设备上已安装的应用列表，留意是否有来历不明的应用。  
  
1. **善用安全工具进行辅助检测**  
：  
  
1. **谷歌安全浏览服务**  
：确保你的浏览器（如Safari、Chrome）开启了安全浏览功能，它可以帮助拦截谷歌已知的恶意网站。  
  
1. **终端安全解决方案**  
：对于企业或高级用户，可以考虑部署移动终端检测与响应 或移动威胁防御解决方案，这类工具可以监控设备上的异常行为和潜在威胁。  
  
**行业与社区的共同努力**  
  
谷歌一直是旨在遏制商业监控软件行业危害的“Pall Mall进程”的积极参与者。我们共同致力于构建国际规范和框架，以限制这些强大技术的滥用，保护全球范围内的人权。这些努力建立在各国政府早先的行动基础之上，包括美国政府对间谍软件使用设限的措施，以及一项开创性的国际联合声明。  
  
**结论**  
  
“科鲁尼亚”漏洞武器包的发现之旅，不仅仅是曝光了一个强大的黑客工具，更是揭开了现代网络攻击技术生态中一条隐秘的供应链。它告诉我们，一次精心设计的漏洞利用，如同潘多拉的魔盒，一旦打开，其危害可能远超最初的预期，最终让每一个普通用户都暴露在风险之下。攻防对抗是一场永无止境的竞赛。作为用户，保持警惕、更新系统和善用安全功能，是保护自身的最基本防线。作为行业和安全社区，则需要共同努力，从技术、市场和政策等多个维度，遏制这类高级攻击武器的无序扩散，筑牢数字世界的安全堤坝。  
  
**技术附录：威胁指标（IOCs）**  
  
为协助安全社区更广泛地搜寻和识别本报告中概述的攻击活动，我们已经在一个免费提供的GTI集合中包含了相关威胁指标。  
  
(此处详细列表包含植入程序及模块的SHA-256哈希值、攻击涉及的URL和指挥控制服务器域名，以及用于检测相关代码和行为的YARA规则。鉴于其技术细节和长度，具体列表内容请参考原文附录。)  
  
原文：  
  
https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit  
  
- END -  
  
**感谢阅读，如果觉得还不错的话，动动手指给个三连吧～**  
  
