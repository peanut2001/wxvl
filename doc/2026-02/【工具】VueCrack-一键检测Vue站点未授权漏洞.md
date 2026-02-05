#  【工具】VueCrack-一键检测Vue站点未授权漏洞  
原创 track
                    track  泷羽Sec-track   2026-02-05 05:09  
  
>   
> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！  
  
  
**往期推荐：**  
  
**【工具】Burp插件DouSql，自动化检测sql注入**  
  
**隧道代理攻防技术战争手册**  
  
**【工具】Hikvision海康威视综合漏洞利用工具**  
  
**【好靶场】云安全专场-WP**  
  
**【工具】Shiro反序列化利用工具**  
  
**【工具】Sqlmap中文汉化版**  
  
**公众号：**  
  
  
公众号后台回复**vuecrack**  
即可获取工具  
# VueCrack  
  
这是一个专为红队人员开发的浏览器插件，用于分析Vue框架网站的路由结构，并绕过路由守卫，从而发现站点的**隐藏资产**  
与**未授权访问漏洞**  
。  
```
https://github.com/Ad1euDa1e/VueCrack

```  
  
![image-20260205130109693](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbzIlOlJicWWWdmicv3ibphRpqWbnb6W1ib49VNN6yriaxCTQCtNibuicJ85uRN5KbzISpQvLtUCrYgapxUp6iaNQsx2vibUvcd7pIg9M1GU/640?wx_fmt=png&from=appmsg "")  
  
image-20260205130109693  
## 📝核心功能  
- **自动检测Vue框架**  
：快速识别目标站点是否使用Vue.js  
  
- **绕过路由守卫**  
：自动清除路由守卫，允许访问受保护路由  
  
- **修改鉴权字段**  
：自动修改路由元信息中的auth字段，绕过前端权限检查  
  
- **路由结构分析**  
：提取所有路由路径，包括可能隐藏的管理页面  
  
- **批量操作**  
：支持一键复制和访问所有发现的路由  
  
  
  
## 📄技术实现  
- **多重检测引擎**  
：使用多种策略检测Vue及Router实例  
  
- **守卫清除机制**  
：通过修改Router原型方法清除beforeEach等路由守卫  
  
- **权限标志修改**  
：递归遍历路由树，修改所有auth相关字段  
  
- **内存路由提取**  
：直接从内存中获取完整路由表，包括隐藏路由  
  
## 配置方法  
  
首先下载插件的压缩包，后台回复**vuecrack**  
即可获取  
```
通过网盘分享的文件：VueCrack.V.1.3.zip
链接: https://pan.baidu.com/s/1AFC1H0ZtcZKdXPa04Ufj2A?pwd=xnqy 提取码: xnqy

```  
  
![image-20260205125037716](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbyAjFnQOibGYGJuWaOm0Oc1KDOoFLDf87lduX5DeUMzyWO4WUhw0FiaWwlwWMwGDJE8rg1er8sO1XM2ICeGeX368ZKw9TAVEkBWw/640?wx_fmt=png&from=appmsg "")  
  
image-20260205125037716  
  
打开google或者微软浏览器的开发者模式  
  
![image-20260205125420976](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbwv3Z5jl8DQ71cvu8VbhHnoXxiaccMibc11libkic0PP9fDckoYp5JHPFZJo3f4Y3ILWJGpeiamfuzVxe21lgxyiafwiafiaI2HAmYD1Lw/640?wx_fmt=png&from=appmsg "")  
  
image-20260205125420976  
  
解压缩下载的文件，直接脱进来即可，建议固定在工具栏  
  
![image-20260205125516122](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJby7uIqfNpHIrHh1n2p0FEciaFfgeCt2YQNICLyYQnWbLM030qpIHNAqfgPzCC2pzfXWz8mXAJ2KAYNQ5Tr14s0iajNGXE1yyEaLE/640?wx_fmt=png&from=appmsg "")  
  
image-20260205125516122  
## 使用案例  
  
该插件通常是用来测未授权的，使用的话可以先看看网站指纹特征  
  
![image-20260205125724452](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbxW1libpyu8wP1TV3jI9VOlBMaFecMZHBld5qVXQ2FXVltlaolF3L6zKqCX4TZOQmb1uJaPMibS8Yv9HuIITnXYz8YoBWzgoh5hU/640?wx_fmt=png&from=appmsg "")  
  
image-20260205125724452  
  
另外一点就是通常VUE框架的路由会存在特殊的**[#号]()  
**  
  
![image-20260205125819786](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbzuJ7sY0UmauKAPjaibMqr32Y3bmp9lpJRZunDg8APjgPfn4ic12XRFgOGvMNnLKZ7fTVjKpUpibMAxNy4vyzUIPYXaxiaHI3EmT7k/640?wx_fmt=png&from=appmsg "")  
  
image-20260205125819786  
  
  
直接打开插件，就能看到提取出的路由，省去了一个个去找的时间  
  
![image-20260205125909852](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbxLBd8ghI6BAsUfSholUOQk82icnj6B7JsYm7HTxzPQcPSCj2ah4XzjcZYfCbA3j6o7oia015T1PEiarA8yzxUL9sdkLQMkghD6c0/640?wx_fmt=png&from=appmsg "")  
  
image-20260205125909852  
  
如果存在未授权，那么在访问之后会直接进入后台  
  
![image-20260205130020385](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbx2ejdhrgAKj1r1wqSVxC0YgvDZaCC4nJNjnGyMXiauY4GjiabGWibb8WnH2BPia4JqDXE5BIHF2n3nSTevOkqqsVoHHibUmHruTa1c/640?wx_fmt=png&from=appmsg "")  
  
image-20260205130020385  
## 知识星球  
  
**可以加入我们的知识星球，包含cs二开，甲壳虫，渗透工具，SRC案例分享，POC工具等，还有很多src挖掘资料包**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbw1CZibA2ToSpTiaiaDHibUqWiah8SITsneTaRM2xQLTSbfoCibDQZZzM90PDOCwemsTQUH3CTmj0gRX9HiaBybaXfAcYbJaScL35e9w0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbwXu8u0jRBhrPk6xib1elaibsmJu75tYWdx8VGezzd6Ixkl6q0P3FMDaibBma8hJDMFh6Aica9RgXGMD44rRJiclr2VahfIyZcn2Tso/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vOORdxuIJbzjMAVUyiczFR1yG9h2peomD7JHu6zNehqae1CdJ9DqbtkcibQbBnNcnP86ZibQS4AibFaw0TibO7mqJqoRsEAHp7icicrianf5nNZibibs0/640?wx_fmt=jpeg&from=appmsg "")  
  
  
  
