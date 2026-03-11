#  小程序 wx.cloud 操作文档型数据库的漏洞挖掘点  
原创 进击的HACK
                    进击的HACK  进击的HACK   2026-03-11 10:24  
  
   
  
> 字数 474，阅读大约需 3 分钟  
  
## 前言  
  
对上一篇文章的补充 [原创 | 小程序中云函数越权的探索](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247489796&idx=1&sn=cf50ea7a6fd13bb64ccb23a7e9d6401b&scene=21#wechat_redirect)  
。  
  
今天来说 cloudbase 中的文档型数据库的权限问题。  
前言文档型数据库权限说明文档型数据库操作演示小结防御## 文档型数据库权限说明  
  
腾讯云 cloudbase 中位置：  
  
![78a3ea8036d9e7dda55d48ebb2c04391.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlJA4JvrZdtqUdtBmIWRb1Q1aUVLwH7ghPQejdIstQ9RvRTZFvybVMz18qTqT8Kx947JmJfE8BibNoicueXhy4VngZRsb1T6Dhus/640?from=appmsg "null")  
  
78a3ea8036d9e7dda55d48ebb2c04391.png  
> 官方文档：https://docs.cloudbase.net/database/data-permission  
  
  
![a3117a3bdefebfd8d15c1556378cff93.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmdOicTcKcUm2ibvCOiawXMsxYHdnVgqpoeoP8ibSuqia4tXsrzJ8iaGmzy2jic9D7LeHLicFOXkiaHPZlQBs0I3DFgpeJSfcyR9vVXvJvA/640?from=appmsg "null")  
  
a3117a3bdefebfd8d15c1556378cff93.png  
## 文档型数据库操作演示  
  
我在写小程序的时候，发现大模型会在云函数和小程序 js 文件里使用  
```
const db = wx.cloud.database();// 先获取总数const countResult = await db.collection('articles').count();const total = countResult.total;// 获取分页数据const result = await db.collection('articles').orderBy('createTime', 'desc').skip((page - 1) * pageSize).limit(pageSize).get();const newArticles = result.data;
```  
  
云函数和小程序都是调用的 wx cloud 的 sdk。这两种都执行成了。  
  
那小程序可以直接db.collection('articles')  
直接配置查询哪个数据表。这里好像并没有限制不能查看其他数据库哦。  
  
在 console 中调用  
  
![84962631212994c355fd91d92d932f35.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl6EAY6FJhVEbmLBSUQdAeNXiczRH3XYL45b4RPZ2rbiaySS0pa5OGuY4P4a573dUJibrSHvCJKBkj046wHp22xS6kGBvfjFXzYhk/640?from=appmsg "null")  
  
84962631212994c355fd91d92d932f35.png  
```
const db = wx.cloud.database();let countResult = await db.collection('articles').count();let total = countResult.total;console.log('总条数：', total);
```  
  
我的云文档数据库里的表有：  
- • articles  
  
- • articles_tag  
  
- • interview_questions  
  
- • interview_tag  
  
如果数据表不存在：  
  
![ebbf8bae834b5625025c4a710f723efc.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkXOqdia514xHibHZSIMN8XuIGVFrx8bm5XUxtYsBJWwf8D6oMN5CvUIpOVy2gXqcHiaibcMTNV27qpML02gTzyfLblDLhofeMuUqg/640?from=appmsg "null")  
  
ebbf8bae834b5625025c4a710f723efc.png  
  
读取 articles_tag  
```
let countResult = await db.collection('articles_tag').count();let total = countResult.total;console.log('总条数：', total);
```  
**无权限[ADMINONLY]**  
  
![3ed7b7de11790f25e1cc50363ae3b611.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkomICuVSPTgc0hUvg0ic1dyibtd2ZKdkBicqfRr55X4ezdNA2lk8wc5D4gsH88o1zqUgOZaKSBFkJXEv17Cvgho3Cibxd2WOP3jhE/640?from=appmsg "null")  
  
3ed7b7de11790f25e1cc50363ae3b611.png  
  
提示无权限  
  
![39ea5bec2a94a30c715447b80f3226e0.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkqDrxPn4zAQ9wD6J6oRETicXFVcGVdyx6R3h9QYPhHiaVolsc5550JaAibQ3BVWibYk2Ss025nC7bjlfRTbuUrgfeYMsCWia8Mk0E0/640?from=appmsg "null")  
  
39ea5bec2a94a30c715447b80f3226e0.png  
**读取全部数据，不可修改数据[ADMINWRITE]**  
  
![b6d296e971eb6e891d18da8d837962d4.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVm7AiaxKaUABm7xdVXNAeVpMClkesGzTCSNXy8lhTdc27YgRY7Fmk5gCJibLoiaNoibSWkicibnalgvIw3seEGqM2kciaY0kw7icIwl7lo/640?from=appmsg "null")  
  
b6d296e971eb6e891d18da8d837962d4.png  
**读取和修改本人数据[PRIVATE]**  
  
![0f78a87d7ad972253a2ec310d5efea7d.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl1s768DpAQcJznwTx24UeglTGFg6w2rY0RYR8Zr1HeJyuWqI7HBN37sVnyAk3xSTjEbnicBTHKTfKh7ibnpQOvouHF6MqbA6gJ4/640?from=appmsg "null")  
  
0f78a87d7ad972253a2ec310d5efea7d.png  
### 小结  
  
可以看到，如果没有配置**无权限[ADMINONLY]**  
，那么我们能通过 wx.cloud.database 直接对数据库进行查看，如果给了满权限，还能增删改查。  
## 防御  
  
当小程序需要对云文档数据库进行操作时，可以通过云函数进行操作。即时数据库配置**无权限[ADMINONLY]**  
，云函数依然可以访问，进行完整的增删改查。  
  
![e894e2bc7480497e8c020a03b8986e33.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmvsHLiaz7yic6hWP9WYvWrhmM1HxOr1jFMnOsOibiaryrOStz3d92ZxEAIu5EviciceOTYSNgHMM3BtwiaA4ibbcwXicF3vNBhIm657glk/640?from=appmsg "null")  
  
e894e2bc7480497e8c020a03b8986e33.png  
  
也因此，通过云函数操作时，就要考虑上一篇文章对云函数的权限限制。  
  
通过云函数访问时：  
  
![2c746ecfb4ba3b5289a3bbac1a7e41f5.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnRSzFfwgzrd3V0phvzPww7WicrERuj1X6dn7gkrea8VXUqyRuCJmsu84VQBcZOviciap1Y6DvS6bh4UDwYKy1XXTtLmSCmTDGA3I/640?from=appmsg "null")  
  
2c746ecfb4ba3b5289a3bbac1a7e41f5.png  
  
小程序直接 db.collection 访问时  
  
![92deeecf0b414c8d34c1493e92933ad2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlXyrwuZPsHUV4ZSlbQ1GEUPdria7evQegA5RztbicIYEx5c27dwJJsIOKUElth5kAOUlbkTJObqkrC20ibL5K0IdIVFcK4B0HbDs/640?from=appmsg "null")  
  
92deeecf0b414c8d34c1493e92933ad2.png  
  
   
  
  
