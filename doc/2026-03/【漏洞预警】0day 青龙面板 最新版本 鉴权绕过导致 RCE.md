#  【漏洞预警】0day 青龙面板 最新版本 鉴权绕过导致 RCE  
原创 安全探索者
                        安全探索者  安全探索者   2026-03-03 07:12  
  
↑点击关注，获取更多漏洞预警，技术分享  
  
0x01 组件介绍  
  
        青龙面板是一款支持 Python3、JavaScript、Shell、Typescript 的定时任务管理平台。  
  
fofa语法：  
product="青龙-定时任务管理面板"  
  
0x02 漏洞描述  
  
     
2026年2月，互联网上披露其存在权限绕过漏洞，攻击者可构造恶意请求绕过相关权限认证，攻击者可通过大小写变形路径（如 /API/...  
）绕过鉴权并命中 /api/...  
 实际路由，最终形成未授权远程命令执行（RCE）  
  
<table><tbody><tr><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf="">漏洞分类</span></section></td><td colspan="3" data-colwidth="143,143,143" width="143,143,143" style="border-color:#0080ff;"><p style="margin-bottom: 0px;"><span leaf="" style="color: rgb(52, 58, 64);font-family: -apple-system, BlinkMacSystemFont, &#34;Segoe UI&#34;, Roboto, &#34;Helvetica Neue&#34;, Arial, sans-serif, &#34;Apple Color Emoji&#34;, &#34;Segoe UI Emoji&#34;, &#34;Segoe UI Symbol&#34;;font-size: 16px;font-style: normal;font-variant-ligatures: normal;font-variant-caps: normal;font-weight: 400;letter-spacing: normal;orphans: 2;text-align: left;text-indent: 0px;text-transform: none;widows: 2;word-spacing: 0px;-webkit-text-stroke-width: 0px;background-color: rgb(255, 255, 255);text-decoration-thickness: initial;text-decoration-style: initial;text-decoration-color: initial;float: none;display: inline !important;" data-pm-slice="1 1 [&#34;para&#34;,{&#34;tagName&#34;:&#34;p&#34;,&#34;attributes&#34;:{&#34;style&#34;:&#34;margin-bottom: 0px;&#34;},&#34;namespaceURI&#34;:&#34;http://www.w3.org/1999/xhtml&#34;}]">未授权远程命令执行</span></p></td></tr><tr><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf="" data-pm-slice="1 1 [&#34;table&#34;,{&#34;interlaced&#34;:null,&#34;align&#34;:null,&#34;class&#34;:null,&#34;style&#34;:null},&#34;table_body&#34;,{},&#34;table_row&#34;,{&#34;class&#34;:null,&#34;style&#34;:null},&#34;table_cell&#34;,{&#34;colspan&#34;:1,&#34;rowspan&#34;:1,&#34;colwidth&#34;:[143],&#34;width&#34;:null,&#34;valign&#34;:null,&#34;align&#34;:null,&#34;style&#34;:null},&#34;para&#34;,null]">CVSS 3.1分数</span></section></td><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf=""><span textstyle="" style="color: rgb(255, 0, 0);">9.6</span></span></section></td><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf="">漏洞等级</span></section></td><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf=""><span textstyle="" style="color: rgb(255, 0, 0);">严重</span></span></section></td></tr><tr><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf="">POC/EXP</span></section></td><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf=""> </span><span leaf=""><span textstyle="" style="color: rgb(255, 0, 0);">已公开</span></span></section></td><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf="">可利用性</span></section></td><td data-colwidth="143" width="143" style="border-color:#0080ff;"><section><span leaf=""><span textstyle="" style="color: rgb(255, 0, 0);">高</span></span></section></td></tr></tbody></table>  
  
0x03 影响版本  
  
青龙面板 2.20.1(其余版本未明确受影响）  
<table><tbody><tr style="-webkit-tap-highlight-color: transparent;outline: 0px;visibility: visible;"></tr></tbody></table>  
  
0x04 漏洞验证  
  
目前POC/EXP已经公开（后台留言：青龙面板，获取测试paylaod）  
  
概念性验证，  
发送数据包，出现下面的即可证明漏洞存在  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibWiaLKz39tdCrWlia8XFELB0u165ic96ybmrXdNWPPN8N5QmjxOPA1ZftfjO9FtQ883yVS8lS6g59o9NicjehCIsM7FsPVbvo8UzVc2FibNGC1hI/640?wx_fmt=png&from=appmsg "")  
  
随机测试了目前公开的大部分版本，大部分都未受影响  
  
0x05 漏洞影响  
  
由于该漏洞影响范围较广，危害较大。通过以上复现过程，我们可以知道该漏洞的利用过程比较简单，且能造成的危害是高危的，可以执行命令，获取服务器权限，企业应该尽快排查是否有使用该组件，并尽快做出对应措施  
  
  
0x06 修复建议  
  
  
1.利用安全组设置其仅对可信地址开放  
  
2.参考官方修复方式进行修复  
  
https://github.com/whyour/qinglong/issues/2934  
  
0X07 参考链接  
  
https://github.com/whyour/qinglong/issues/2934  
  
  
0x08 免责声明  
  
> 本文所涉及的任何技术、信息或工具，仅供学习和参考之用。  
  
> 请勿利用本文提供的信息从事任何违法活动或不当行为。任何因使用本文所提供的信息或工具而导致的损失、后果或不良影响，均由使用者个人承担责任，与本文作者无关。  
  
> 作者不对任何因使用本文信息或工具而产生的损失或后果承担任何责任。使用本文所提供的信息或工具即视为同意本免责声明，并承诺遵守相关法律法规和道德规范。  
  
  
  
