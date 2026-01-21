#  [0day]某erp系统存在任意文件上传漏洞  
原创 zyxa
                    zyxa  众亦信安   2026-01-21 04:45  
  
**声明：**  
文中涉及到的技术和工具，仅供学习使用，禁止从事任何非法活动，如因此造成的直接或间接损失，均由使用者自行承担责任。  
  
**众亦信安，中意你啊！**  
  
  
****  
**温馨提示：当前公众号推送机制调整，仅常读及星标账号可展示大图推送。建议各位将众亦信安团队设为“星标“，以便及时接收我们的最新内容与技术分享。**  
  
****  
****  
  
****  
漏洞介绍：  
  
某erp系统任意文件上传，可解析  
  
****  
**fofa:**  
```
Images/login/login_bg_pic.jpg
```  
  
poc:  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDkbSToe4erMnBhSBMkR8wBKzo94meF7S71yfr1mtttqevpUhdlkcUV99TNy0iblGVntr4zEHXXnZw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaDkbSToe4erMnBhSBMkR8wBv6ZAqznr4raWiaqthZaPk809dPftRRmQibhicJYpp3pGRNJqtVpNm3iaCg/640?wx_fmt=png&from=appmsg "")  
  
poc已更新至圈子  
  
tips：  
  
  
圈子专注于  
渗透测试、漏洞挖掘、免杀对抗、逆向分析  
四大核心方向，同时提供各类实战工具、0day 情报与长期更新的技术资源。目前已更新包括 suo5 二开（含流量修改及客户端工具）、哥斯拉特战版二开（持续维护）、以及 0day 披露等内容。  
  
  
未来还将陆续上线自研 webshell 管理工具、CS 远控定制版本、内网漏洞批量检测工具（fscan 二开 web 界面）、src 与 edu 高赏金积分报告（脱敏）、以及历年 hw 实战案例复盘等深度内容，致力于打造一个真正能提升技术、辅助实战的高质量交流圈。  
  
  
目前定价 129 / 年，前 30 名入圈师傅可享 85 折优惠，欢迎各位热爱技术的师傅加入，一起交流、一起进步。  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_jpg/rl85Sib8ZkaBrDvy8TKfP3pmENHPYQRvnoUJruepz5RIakgWW15WoZlx0GwZl7t32HZLbGzw6Es3o0LNVcicrUdA/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "")  
  
  
  
  
盒子  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzYAmqmVyLA140bY25X4CBspqHHIdchuvl5bTtXqjEZWH6oEdricIUiaNw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzrJoCPp65LU8vOvfiaZ9azEZaiacT4HWN9BjAQibgve4Jwhp2S6H91vYbw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzIc7ibNTL1yqTC9icFDaMaHUtRiccsy6Arnq9KZwBJVhHtIpoibz12VEvgA/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uz4VYVzN5xicYdBt62M6vo2icO8NjQlCaKibkMu15obIz9EnXe0alwSkm1A/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8 "")  
  
携程  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzQm262GVX0fMUqBQP3hZ3kFNO3EnrRdlYU6ODSQhfsac4fXu0DggE7w/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9 "")  
  
  
小红书总榜第二第三  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzyynyEXxX43C2Dn95nqZVLt0ElQb0eb9jqT1HRO8W3VQiaibpXkzNlI7w/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uz6sT5VB2NhebTS27LRTg6rqcJcPCV35ictQMWD5qqxEKvG4BK6UXoNrw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11 "")  
  
  
攻防  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzR87BIcxwa5feaKA3IWcibefB5pkNUGy4q8HKTucczg1MAk1CFdpyBKg/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12 "")  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzMbWx5FD5Sia3vMfoCBDC4gs3avOaeKP7xUkwNcOUMiardqEm7roQsMxg/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzpAONs33icjw7rDANxt444wAfEZNQLVia0Qs7Fxpmb0ExFOMQfsKIbrZQ/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaCOHZticLo6kZuTsH2czn9uzudOB49nibPxwwcInGibS06Dd24s3PGLWYZ51jaicDYxBXfvUrM9kxX6bQ/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaBrDvy8TKfP3pmENHPYQRvnxX6pJGD61jba1mLFcdJ16Lg0AW9WmsEBAnFgaTAWeytqPKQXiaLX2Kw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaBrDvy8TKfP3pmENHPYQRvn4BF5iap2jTibQeibicg5Spuhze3QZtVwNrKvriaJqz9l677mRGwVluW2tBg/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17 "")  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaBrDvy8TKfP3pmENHPYQRvnicicINnJpHaw3QXY8shF3mmTOxnfGIyKVJCqXZuhN8OpUiafqrBLOKoAA/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18 "")  
  
  
  
往这里看  
  
  
  
  
点点关注不迷路，不定时持续分享各种干货。  
可关注公众号回复"进群"，也可添加管理微信拉你入群。  
  
项目交流，src/众测挖掘，重大节日保障，攻防均可联系海哥微信。  
  
入了小圈的朋友联系海哥进内部交流群。  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/rl85Sib8ZkaALhRNp0ic9JdTb3u3x0wr8NEKVpvibCaGWymICEcwUbmO3icFAJwSvxbszDKv7OXQwoDjtrmVRvN91Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=10 "")  
  
  
  
  
  
  
  
  
  
  
