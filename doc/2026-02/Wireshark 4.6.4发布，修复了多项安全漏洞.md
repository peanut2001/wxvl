#  Wireshark 4.6.4发布，修复了多项安全漏洞  
sec随谈
                    sec随谈  sec随谈   2026-02-27 01:08  
  
Wireshark基金会已正式发布Wireshark 4.6.4版本，这是全球  
最受欢迎的网络协议分析仪  
的重要维护更新。  
  
本版本修复了多个安全漏洞，并解决了可能影响稳定性和性能的各种功能缺陷。  
  
网络管理员、安全分析师和开发者依赖Wireshark进行故障排除和教育。  
  
此次更新尤为关键，因为它修复了可能通过特定协议解体器暴露于  
拒绝服务（DoS）攻击  
的漏洞。  
  
4.6.4版本解决了之前版本中发现的三个具体安全问题。这些漏洞涉及协议剖析器中的内存耗尽和崩溃循环，这些组件是Wireshark用来  
解码网络流量的组件。  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">脆弱/问题</span></span></section></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">描述</span></span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong msttexthash="35769383" msthash="55" style="box-sizing: border-box;font-weight: bold;"><span leaf=""><span textstyle="" style="font-size: 15px;">USB HID 剖析器内存耗尽</span></span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">错误的USB HID数据包可能导致内存过度占用，导致崩溃或不稳定。</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong msttexthash="24916840" msthash="57" style="box-sizing: border-box;font-weight: bold;"><span leaf=""><span textstyle="" style="font-size: 15px;">NTS-KE解剖器坠毁</span></span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">特定的网络时间安全密钥建立流量模式可能导致分析器崩溃。</span></span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong msttexthash="52217776" msthash="59" style="box-sizing: border-box;font-weight: bold;"><span leaf=""><span textstyle="" style="font-size: 15px;">RF4CE 配置文件拆除器崩溃</span></span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">稳定性问题已修复，以防止在分析RF4CE（消费电子射频）流量时发生崩溃。</span></span></section></td></tr></tbody></table>## 关键漏洞修复与性能提升  
  
除了安全补丁，Wireshark 4.6.4 还提供了重要的稳定性修复。  
  
而显著变慢。  
  
**其他技术修复包括：**  
  
<table><thead><tr style="box-sizing: border-box;"><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">类别</span></span></section></th><th style="box-sizing: border-box;padding: 2px 8px;text-align: left;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">修复/改进</span></span></section></th></tr></thead><tbody><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong msttexthash="14428700" msthash="68" style="box-sizing: border-box;font-weight: bold;"><span leaf=""><span textstyle="" style="font-size: 15px;">TShark 稳定性</span></span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">当输出格式设置为BLF时，修复了TShark和editcap中的分段错误。</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong msttexthash="23052497" msthash="70" style="box-sizing: border-box;font-weight: bold;"><span leaf=""><span textstyle="" style="font-size: 15px;">捕获文件完整性</span></span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">纠正了无效的PCAPNG达尔文选项块和自定义字符串选项的窃听写入问题。</span></span></section></td></tr><tr style="box-sizing: border-box;background-color: rgb(240, 240, 240);"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong msttexthash="11372205" msthash="72" style="box-sizing: border-box;font-weight: bold;"><span leaf=""><span textstyle="" style="font-size: 15px;">解剖修正</span></span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">解决了 Art-Net PollReply 解体器中 TDS 非同步问题并修复了 RDM 状态解码。</span></span></section></td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><strong msttexthash="15448810" msthash="74" style="box-sizing: border-box;font-weight: bold;"><span leaf=""><span textstyle="" style="font-size: 15px;">杂音撞击声</span></span></strong></td><td style="box-sizing: border-box;padding: 2px 8px;border: 1px solid rgba(0, 0, 0, 0);word-break: break-word;"><section><span leaf=""><span textstyle="" style="font-size: 15px;">在Zigbee直接隧道模糊测试中发现了修复的崩溃。</span></span></section></td></tr></tbody></table>  
虽然本次版本未引入新协议，但已更新对多种现有协议的支持，以确保解码准确。  
  
更新协议包括 Art-Net、BGP、IEEE 802.11、IPv6、MySQL、NAS-5GS 和 Socks。BLF和pcapng格式的捕获文件支持也得到了改进。  
  
建议用户立即更新到 Wireshark 4.6.4  
，以确保其分析环境的安全稳定。最新版本可直接从Wireshark基金会网站下载。  
  
参考链接：  
  
https://www.wireshark.org/docs/relnotes/wireshark-4.6.4.html  
  
