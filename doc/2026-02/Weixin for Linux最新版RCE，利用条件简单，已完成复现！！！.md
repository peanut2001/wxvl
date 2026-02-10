#  Weixin for Linux最新版RCE，利用条件简单，已完成复现！！！  
发呆
                    发呆  漏洞捕手日记   2026-02-10 07:19  
  
# 前言  
  
文中技术分析仅供交流讨论禁止用于商业或非法犯罪用途，poc仅供合法授权测试，用于企业自查，未授权测试造成任何后果由使用者承担！与本公众号以及发呆无关。  
# 正文  
  
今日，一位大佬在朋友圈发文：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/kW4GZt6YiapagAPby7R7KujkCFs2vs7Q6VtEIYYsXQuQzzG8SAez5DsnUqTtwRZzSD79zs1azZHWkOgXIGVonSicLU6VjUP63aXpubSmxcTvw/640?wx_fmt=png&from=appmsg "")  
  
简而言之，微信的Linux版本存在rce漏洞，只需要把文件名改为反引号引用命令就可触发，利用方式极为简单粗暴，目标只要点击文件就可触发，复现：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/kW4GZt6YiapYpHcmia7J3adqIQ73SBSA0kbp0QUXAia82T3N1WLLYNcUcn3llicxwA5JibC64eo8X06bdFWsWgtibiaeQjRR9yjeicXqIzyEviceicZbA/640?wx_fmt=png&from=appmsg "")  
  
根据一哥404所说信创系统也存在这个问题，危害范围还是很大的。  
  
