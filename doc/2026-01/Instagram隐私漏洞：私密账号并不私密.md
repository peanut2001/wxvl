#  Instagram隐私漏洞：私密账号并不私密  
原创 OwlSec
                    OwlSec  猫头鹰OSINT   2026-01-26 03:50  
  
最近国外一名安全研究人员披露了一个  
 Instagram 严重漏洞：在特定条件下，未登录、未关注的任何人，都可以直接访问本应“仅限好友可见”的私人帖子内容。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/biarWYvQqiaDicccXs2xa1wmKSUqmAs2hXXwHBbbibmywsShgcr5RibydClao9KcZfYJn3E8ibvDrgzpVFoDyebaWZYQ/640?wx_fmt=png&from=appmsg "")  
  
作者在开发一个与  
 Instagram 网页端相关的自动化工具时，注意到一个异常现象：  
  
当访问某些私密账号的页面时，返回的  
HTML源码中，竟然  
包含了完整的帖子数据。更关键的是  
——  
访问者  
不需要登录，也不需要任何权限。  
  
起初，作者以为只是  
 CDN 缓存异常或显示错误，但在反复测试了多个自己可控的私密账号后，他确认了一点：这不是前端显示问题，而是后端已经把“不该给你看的数据”，直接塞进了响应里。  
## 漏洞原理  
  
利用漏洞的方法很简单：  
  
1.  
向  
 `instagram.com/<private_username>` 发送未经身份验证的 GET 请求，并带有特定的移动设备请求头。  
  
2.  
服务器返回包含嵌入式  
 JSON 的 HTML，其中包含 `polaris_timeline_connection`  
  
3.  
从  
 `edges` 数组中提取 CDN 链接  
  
4.  
直接访问带有说明文字的私人照片  
  
整个过程没有任何鉴权校验。也就是说，所谓  
“私密”，只是在正常访问流程中成立，但在某些边缘请求路径下，权限判断被直接绕过。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/biarWYvQqiaDicccXs2xa1wmKSUqmAs2hXXWYosVgOVQpdBgczyGAiaEuhWjgsHBHC733PmBxvLW2wrXttHaCZSncw/640?wx_fmt=png&from=appmsg "")  
  
Poc脚本暴露了  
Instagram私密  
帖子  
## 非“全量失效”，而是“条件性漏洞”  
  
这个漏洞，并不是对所有私密账号都生效。作者测试的多个账号中，只有一部分账号出现了内容泄露，另一部分则完全正常。  
  
这类漏洞在安全领域有一个典型特征：不稳定  
、  
不易复现  
、  
极易被官方低估风险  
。  
  
但从攻击者角度看，这恰恰是最理想的漏洞形态：不容易被监控发现，却可能长期存在。  
## 向 Meta 报告后的真实经历  
  
发现问题后，作者第一时间走了正规漏洞披露流程，向  
 Meta 的漏洞赏金平台提交了报告：  
- 提供了详细的技术分析  
  
- 提供了  
 PoC 脚本  
  
- 提供了视频和时间戳证据  
  
结果却并不理想。  
  
第一次回应  
  
Meta 认为这是 CDN 缓存问题，直接关闭了报告。  
  
再次提交  
  
作者重新强调这是服务器端授权失败，并提供了更清晰的复现路径。  
  
Meta 要求在官方测试账号中复现，但由于漏洞具备“条件性”，首次测试失败。  
  
直到作者提供了一个已确认可触发问题的账号，  
Meta 才承认异常存在。  
  
在确认问题后，大约  
48小时内，漏洞被悄然修复。  
  
信息来源：  
  
https://medium.com/@jatin.b.rx3/i-found-a-bug-that-exposed-private-instagram-posts-to-anyone-eebb7923f7e3  
  
