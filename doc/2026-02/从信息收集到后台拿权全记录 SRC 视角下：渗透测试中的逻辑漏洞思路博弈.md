#  从信息收集到后台拿权全记录 SRC 视角下：渗透测试中的逻辑漏洞思路博弈  
一天要喝八杯水
                    一天要喝八杯水  渗透安全HackTwo   2026-02-23 16:01  
  
**0x01 前言**  
  
**最近挖到的中高危漏洞，既没靠 `0day` 这种 "王炸"，也没搞复杂利用链 "炫技"，纯靠瞪大眼睛当 "人肉扫描器"，连标点符号都不放过地逐行比对参数和响应。直到某个昏昏欲睡的下午，随手改了个藏在 `JSON` 数据深处的小参数，系统突然像短路反馈了全新的信息，反常的响应直接暴露未授权访问的 "马脚"。当时激动得差点把咖啡泼到键盘上，看着满地咖啡渍才顿悟 —— 原来倒掉的咖啡，比直接喝咖啡提神一百倍。******  
  
****  
渗透测试人员堪称代码世界的 "超级侦探"，手握 Burp Suite  
 这把 "神奇放大镜"，进入甲方的资产海洋遨游,在其中对着页面疯狂改参数、发请求，却总被系统用平淡入手的响应打发，如同在广阔的太平洋掷入一枚石子,不泛起一丝涟漪; 要么直接拦截请求让人气的砸电脑。开局登录框更是 "经典打卡圣地"，测 API  
 接口这边要扮成研究正常逻辑的好学生，那边得秒变设计注入 Payload  
 的 脑洞大师,还得时刻提防 WAF  
悄无声息送你一张404  
飞机票✈️, 漏洞挖掘本就是逆天而行,挖不到才是正常的  
  
  
最近挖到的中高危漏洞，既没靠 0day  
 这种 "王炸"，也没搞复杂利用链 "炫技"，纯靠瞪大眼睛当 "人肉扫描器"，连标点符号都不放过地逐行比对参数和响应。直到某个昏昏欲睡的下午，随手改了个藏在 JSON  
 数据深处的小参数，系统突然像短路反馈了全新的信息，反常的响应直接暴露未授权访问的 "马脚"。当时激动得差点把咖啡泼到键盘上，看着满地咖啡渍才顿悟 —— 原来倒掉的咖啡，比直接喝咖啡提神一百倍  
  
现在只对常读和星标的公众号才展示大图推送，建议大家把**渗透安全HackTwo“设为星标”，否则可能就看不到了啦！**  
  
参考文章  
：  
  
```
https://forum.butian.net/share/4441
https://www.hacktwohub.com/
```  
  
  
**末尾可领取挖洞资料/加圈子 #渗透安全HackTwo**  
  
**0x02 漏洞详情**  
  
**无限抽奖币**  
  
新的功能点往往被常规功能点所裹挟,黑盒测试的我们只能点点点,当坚持到隐秘功能点出现的那一刻,漏洞已经是呼之欲出了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXGPDCYndEJTAg57R69KAsccujW5dn2oic6IbbiawKOib4R5ApYcPOURjNN3ge1B8UcQxet4HXuXuTdAjKazic9X0N6Yrjic4UxmFf0/640?wx_fmt=png&from=appmsg "null")  
  
微信搜索厂商资产找到一处不起眼的资产,20  
币一次并且可得实物  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWyGvzpXtMlxTk5kd0kiaK0mfybjYEV4vXoEQfybTlUUVvl73F96ibzUPmJNNn1kSoCcg7iccIWld76AJbgYZHSRHLQ04nia37u2vw/640?wx_fmt=png&from=appmsg "null")  
  
初始币是100  
当我小心翼翼的尝试投币点进行一些,自定投币数量,修改返回包控制所得物品,并发签到等操作时,结果洞还没挖到我的游戏币就已经快测没了,真的是天塌了  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAX3LD6tvGHBrox6KBE8Ibo81HoQlAOfHqESGfYOveWSdYIC8rUJsqUfd1iaOPtNDHlzck4XsfKkxPtFcT8KaY2Phfh5RxfKnp0I/640?wx_fmt=png&from=appmsg "null")  
  
当时已经非常晚了到了12点,当我最后一次爪子进行抓娃娃的时候,修改请求包发现还是一无所获,悬着的心最终还是死了,已经准备win+x+u u  
 光速下播,但游戏币消失的时候又出现了新的功能点,这让我死去的心又再次燃烧起来  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWdicyJpGqrukQsn20VxfGANib5RTRQOc9enGQDBRc1DCcpYQTNlt0ctlvoaNZNmv5Y9ZKFbrtYfibndQSsIoib9LIKdRAfj2HS99g/640?wx_fmt=png&from=appmsg "null")  
  
分享赚币,点击后BP  
记录接口,在历史记录逐个对数据包进行查看,最终凭借经验锁定/app/point/doll/share  
接口就是关键的数值包,它的值所控制的就是所得金币数量  
```
points=15
```  
  
思路都理清了那还说啥,直接重发狠狠的输入最大数值  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUFLYSt3PHu0XYG6CBKqcPibuvTiahAT5KRhiaic5kuynOTAOUrCtcPtwHEDCIErFy7ngr6gEAzsQuzHSsJZQX21wia2yb1SO6sEtgI/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUKHSWLCRUdM6xHYmEJWTv1F5EehnKmqxIOic78ZMmG56AwibMU54hW1cITDs8HnG0Z7mhOMwJO1aWR1ygT42vEhet0LjUBFicVpE/640?wx_fmt=png&from=appmsg "null")  
  
不出意外成功,爽吃一中,又可以多买几个馒头恰了,这次渗透告诉我,不测试完所有功能点就绝对不轻言放弃,不要自己跟自己说丧气话,因为大多数人在一个站比如测试越权发现有鉴权,就下定义觉得这个站已经没有越权了,这是万万不行的,作为白帽子最后是把所有思路穷尽才算是一次完整的渗透测试,细心再细心,虽然这样很枯燥但是长此以往相信肯定会有所收获  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVzf3XfpwnSY8FzRXLsEPVkDCSkhEpFjd48NJ706FJkuLTjhjIcnhJ8ljcN5C4JMJQf0k4gkrPVeWo56gmicM4ecOtao7crBSwk/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWDrvk2zbojNzRTA6zSnvr8808HFdw7Qyly9E0FqSCMcKKhAibLib5RIv9ZiatibZR5h4uu6AzwwVt6QvnHe2yibzlTbFbZb0nWvYjg/640?wx_fmt=png&from=appmsg "null")  
## 可控所得优惠卷  
  
功能点购入某些物品系统会赠送一部分优惠卷,但大多是一些小额优惠卷,除非购买昂贵的服务才会赠送价格不菲的优惠卷,利用低级服务所得优惠卷,通过手法找到高等级优惠卷对应token  
，替换后造成刷优惠卷效果  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXia9srlfushG8eIqlZ3u8SJl33wYe00eFbbENl7zpTictbCEnJI0ULYHTLprred1be8q9aN8sTk0R1LZWicricYl88HSIMH1uShzo/640?wx_fmt=png&from=appmsg "null")  
  
站点特征较明显,省略一些前期发现步骤,快进到数据包分析,选择一个商品服务进行下单,BP  
记录所有流量,通过逐个分析定位到此接口为关键的创建订单包,将其测试发送到重发起等待进一步测试  
```
https://xxxxx/restapi/soa2/19691/orderCreate?_fxpcqlnired
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUc4ZePOKUZtVceXlVrF7wpFXfQXjQmQibHNQbPeTz8l73o6Sj9OhwWvOiaV1sjrbY4cDN1UbXqI1gr7RDNrVUIQByVqPGD68dmY/640?wx_fmt=png&from=appmsg "null")  
  
进行小程序看先前创建的订单,看有没有可以操作的业务,观察到订单创建后成功支付会相对应的赠送优惠卷  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWoUNjXKqibFnSJQpshl5Via5xZ1fCRkqc8vSKibhHMJ3hR1wxEhlTtemMt8uRHcnfXmXqiab2TakZMgcuWmTamZ4n0t92Aheu4XTg/640?wx_fmt=png&from=appmsg "null")  
  
都是一些不起眼的小福利卷,跟QQ  
空间兰博基尼5  
元代金券不能说没有区别只能说一模一样  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAW51CCDKEYX7icn0a0c8AUUAVhZryj15GPtXnjiaVRJvufbg48XtnRrbTiaZB7hDcAia6wvR8D8VYfiaXX5jzudQdibtA4vpQDia7Cdy8/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAU3vZfgdolD4Ugxn6icwtczDbEC2XGibvT6WOQL4vyXW5RaNEgAcU1eibda38xo8N8pmFguLK5XpnHMAeRibw7r8SyRhKUic2DkvX7Y/640?wx_fmt=png&from=appmsg "null")  
  
将创建订单接口发送到重发器后,观察数据包,这种涉及多个流程的业务数据包一般都很多参数,有的是关键参数,有的是多余参数用于迷惑,通过"人肉扫描器"一段段观察,定位到data  
 数据体记录了优惠卷对应的token  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWvIicezPSGkniao2XfOhU6yiccHZdb3TjnZvfN7FNB1ziawzOtgE98jlkxwwny45vt8mL8e1okpSIP0ZZt434xwd1tkK6KXECslgs/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWicIOiazgLs40OrClibKvwicTYlC5fnELSlg9XuNKl1IjJ8MMKa93labwzgzvTcWuJRW2Esicad1Da85BW6N7Tgy3xLTH9smk723XQ/640?wx_fmt=png&from=appmsg "null")  
  
通过一系列手法,找到了其他优惠卷的token  
,然后对先前的三处优惠卷token  
进行替换.并且全是一模一样的,意味着我可以通过低级服务自定义所得优惠卷,并且叠加  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXk0rFtsicjxKgJWuNMCic5ROYwH3qKIxCQO4p7rtD95toTflKNvRxIiaPgkOMg3cibTQdbSsFoNiawv2lXicbvia8A8yP2Osqu9xNMLs/640?wx_fmt=png&from=appmsg "null")  
  
当前替换后再次创建新订单,先前的三张低级优惠卷已经被替换为了三张豪车打车减免卷,并且只需要我知道任意卷的token  
,就可以得到对应券,还可以叠加字段进行复用  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWogQibZKSaOEpwU8snpcaSYIEUvqwmlDcoptB9O3oLh5GHPUOPfUhfQYCuQJoUXb7HZ0gerc1DjfRa9Lfl3lPbsyauHV4pbcAo/640?wx_fmt=png&from=appmsg "null")  
## 普通的CSRF  
  
如今各种逻辑漏洞,云攻防,Top10  
 为主流的今天,最基础的CSRF  
往往是同其他漏洞结合利用,但忽略了单个CSRF  
所能造成的影响,我理解的是只要功能涉及到主观操作场景,如修改信息,增加收货地址,发送邮件...等等需要主观意愿才能进行,并且请求中并没有发现token  
或其他校验字段均可以尝试CSRF  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAX4QnjEpbVz72LVY0tbTRiaoRicCUGicRmVXqdaelFDeQ0TKiajaxJ8qntX4W5iavicnNll1d1s0VVBOgk6JMuBVCTtiaAYjuN43On0Ck/640?wx_fmt=png&from=appmsg "null")  
  
正常用户修改绑定的邮箱需要输入交易密码才可以修改，但是功能点的个人信息接口可以直接修改绑定的邮箱,制作post  
请求的csrf  
数据包发送受害者点击, 就会自动修改绑定邮箱及个人信息为我们所设置的  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWSHciaZy5fQglhM9VOmhJSDLMmESQaeEvoZLRdJg91QibP9sV3ibhqr4aULLlWgQlyB6pOm4uMk8yhibV70Q5VfyrwkPPIhTNefSI/640?wx_fmt=png&from=appmsg "null")  
  
为不影响业务,实名认证后准备两个小号相互测试  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAXRushwK9YCRSxqn1HlNdTmZBEYSAluuXydFcj6cDgYWmZjAblhoGb8vPqQ8hc7XjwbgzR7ZlwfVNqBZUrUowiaN0hYKcxGeTL8/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVJE1OcjF0315V3SgicfpLZHYN242ysKqgs0CyOO7FiaerD9ibegWSicdcRluKIO38Ey5oCfXjdBhYWY94UzPuGa8YEQpLf0ywF4icQ/640?wx_fmt=png&from=appmsg "null")  
  
对个人信息进行修改,BP  
记录所有的流量,此接口为更新信息  
```
/fund/apl/postUserinfo
```  
  
观察更新个人信息功能第一是携带了邮箱更新,如上所示,正常我们单独修改关键的邮箱是需要交易密码的, 因为站点是一处涉及基金交易,但是普通的修改个人信息却是可以直接修改邮箱,跳过交易密码,第二是请求包没有token  
等其他涉及状态码字段,那么是不是可以尝试一下CSRF  
呢  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWcs26raqaV0WmsyFs83hlsgoMDNyD5GHnFWzlx7W6Giac3XGB3Q8kiaMIagc5Y0KicPzcJ3k42TVzcGm8H6SnQ7vH4NV7Ylib4rvk/640?wx_fmt=png&from=appmsg "null")  
  
将更新POST  
请求右键制作为CSRFPOC  
 把生成的代码拷贝一下随意改一下信息为自定义的,然后本地作为html  
文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUC2IXDI7O1wngS9qIZ9nTh6SGwOAN6fkiaBrsRWVcwA5C5q0BJ8UeYNWeIkMkHj4umPHsje6gTU2327TWxQwibI57Fh4hNztvOQ/640?wx_fmt=png&from=appmsg "null")  
  
poc.html  
 用当前小号登录的浏览器去打开,点击后返回修改成功  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAV7QVbt8Ytzkbx56tFZkWBckQxqswCUSqCiaYGhQsviciaxBjYQyQJAahLLAP1EQLjnC60n2GaqIzgvdvuh8gt5LIjrRdhMaxic2yg/640?wx_fmt=png&from=appmsg "null")  
  
刷新站点,当前的个人信息包括邮箱已经是我们所设置的,CSRF  
 攻击成功  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUy3rqy0pVThnHC6CTuwYllhzIZXdWbZ6vEOLvDLkiaqQRVvy40ibibGbuNWruxUKmMDFW3pobSQJUreRzpzzykdEBWnjFIWSG3UY/640?wx_fmt=png&from=appmsg "null")  
## 网站泄露导致接管  
  
写多了企业SRC  
报告,现如今刚刚初入社会投身于工作当中,下班后再去花精力挖掘SRC  
可能是越来越少,还是怀念大学的时光没有压力,别管挖没挖到洞,你只管去挖剩下的交给时间,现在如果下班没有产出其实还是挺浪费时间的,因为本来是可以利用这个时间再去学习一些新知识,提高自己技术....分享一个在近期在公司渗透测试一个单位的过程,最终也是拿下网站超级管理员  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUgVV2ELF8tJI6vzM1uLavvGt9ZqJ2QqaJ94RkFM8JiaibvkvxXJVZYWTVVPQvgHGtM7ZOfhlwPMzsAZQ4gadAqOCVtzvXtb0r14/640?wx_fmt=png&from=appmsg "null")  
  
企业SRC  
大多目标较少,且会给出具体的域名范围,工作渗透项目因为是会有地区网信办授权,所以给我某一地区庞大的单位,从中进行渗透,海量的资产梳理不是一件简单的事情  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAU0I8LEIb2Ux7LyuW1QO1hYYRb3HsiaFeq3DSQfbia36X41JYY7UgLDhEKahFPg5bqSY0G69LL8LHwoxWHK8Isu0IP3JI7kVkicVQ/640?wx_fmt=png&from=appmsg "null")  
### 测绘资产处理  
  
众多单位名有些是存在备案网址的,这些才是有效资产可以进行渗透,那么无备案的单位如果排除呢？测绘网站hunter  
可以很好的做到这一点，它支持企业备案名称进行查询,这是其他fofa 360  
 都没有的,所有在攻防项目还是企业渗透开局海量单位名hunter  
是最佳的选择,唯一缺点这个打法比较吃积分  
  
```
icp.name="xxx"
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXmNGS0I85nbwzzAyiaZsHSEBPwFFmlW7k7580JCciaC5OFmVpQ92ws1fiawibOE8Anx9QcfWc0a0nrG81WmjUU4OEFE1EVKjOgfgE/640?wx_fmt=png&from=appmsg "null")  
  
既然知道hunter  
可以根据备案名查询,那么写一个批量脚本,填入API  
进行调用语法即可  
```
import requests
import base64
import time
import json
import pandas as pd
# 鹰图平台的 API 地址
BASE_URL = "https://hunter.qianxin.com"
SEARCH_ENDPOINT = "/openApi/search"
# 你的 API Key（从鹰图平台获取）
API_KEY = ""  # 替换为实际的 API Key
# 字段翻译映射表
FIELD_TRANSLATION = {
    "code": "状态码",
    "message": "错误信息",
    "data": "数据部分",
    "total": "资产总数",
    "time": "时间",
    "arr": "资产列表",
    "is_risk": "风险资产",
    "url": "URL地址",
    "ip": "IP地址",
    "port": "端口号",
    "web_title": "网站标题",
    "domain": "域名",
    "is_risk_protocol": "高危协议",
    "protocol": "协议类型",
    "base_protocol": "通讯协议",
    "status_code": "网站状态码",
    "component": "应用组件/版本",
    "os": "操作系统",
    "company": "备案单位",
    "number": "备案号",
    "icp_exception": "备案异常",
    "country": "国家",
    "province": "省份",
    "city": "市区",
    "ip_tag": "IP标签",
    "asset_tag": "资产标签",
    "vul_list": "历史漏洞",
    "updated_at": "探查时间",
    "is_web": "Web资产",
    "name": "组件名称",
    "version": "组件版本",
    "as_org": "注册机构",
    "isp": "运营商信息",
    "banner": "服务标识信息",
    "header": "HTTP响应头",
    "sha256": "证书签名哈希算法(SHA256)",
    "consume_quota": "消耗积分",
    "rest_quota": "今日剩余积分"
}
# 从 txt 文件读取公司名称列表
def load_company_names(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            companies = [line.strip() for line in f.readlines() if line.strip()]
        return companies
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return []
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return []
# 公司名称文件路径
COMPANY_FILE = "dz.txt"
# 加载公司名称列表
company_names = load_company_names(COMPANY_FILE)
if not company_names:
    print("没有可用的公司名称，请检查 gs.txt 文件内容")
    exit()
# 请求参数
page_size = 10  # 每页资产条数
# 存储所有检索结果
results = []
no_data_companies = []
for company_name in company_names:
    print(f"\n正在查询公司: {company_name}")
    page = 1
    total_pages = 1
    has_data = False
    while page <= total_pages:
        search_query = f'icp.name="{company_name}"'
        search_encoded = base64.urlsafe_b64encode(search_query.encode("utf-8")).decode("utf-8")
        params = {
            "api-key": API_KEY,
            "search": search_encoded,
            "page": page,
            "page_size": page_size
        }
        try:
            response = requests.get(
                f"{BASE_URL}{SEARCH_ENDPOINT}",
                params=params,
                timeout=15
            )
            response.raise_for_status()
            data = response.json()
            # 转换状态码为是/否
            if "code" in data:
                data["status"] = "是" if data["code"] == 200 else "否"
            if data.get("code") == 429:
                print(f"公司 {company_name} 请求过多，等待15秒后重试...")
                time.sleep(15)
                continue
            if data.get("code") != 200:
                print(f"公司 {company_name} 检索失败: {data.get('message')}")
                break
            total = data.get("data", {}).get("total", 0)
            total_pages = (total + page_size - 1) // page_size
            if data.get("data", {}).get("arr"):
                has_data = True
                # 移除banner字段
                for item in data["data"]["arr"]:
                    if "banner" in item:
                        del item["banner"]
                results.append({
                    "company_name": company_name,
                    "page": page,
                    "data": data
                })
            print(f"公司 {company_name} 第 {page}/{total_pages} 页检索完成，共 {total} 条结果")
            page += 1
            time.sleep(1.5)
        except requests.exceptions.RequestException as e:
            print(f"公司 {company_name} 请求失败: {e}")
            break
    if not has_data:
        no_data_companies.append(company_name)
# 统计结果
total_companies = len(company_names)
no_data_count = len(no_data_companies)
print(f"\n总共查询了 {total_companies} 个公司，其中 {no_data_count} 个未查询到数据。")
# 保存原始JSON结果
timestamp = time.strftime("%Y%m%d_%H%M%S")
filename = f"search_results_{timestamp}.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
# 保存无数据公司名单
no_data_filename = f"no_data_companies_{timestamp}.txt"
with open(no_data_filename, "w", encoding="utf-8") as f:
    f.write("\n".join(no_data_companies))
# 准备Excel数据
excel_data = []
for result in results:
    company_name = result["company_name"]
    status = result["data"].get("status", "否")  # 获取状态码转换结果
    for item in result["data"]["data"]["arr"]:
        row = {"公司名称": company_name, "请求状态": status}
        # 添加所有字段到行数据
        for field, translation in FIELD_TRANSLATION.items():
            if field in item:
                row[translation] = item[field]
            elif field in result["data"]:
                row[translation] = result["data"][field]
        excel_data.append(row)
# 创建DataFrame
df = pd.DataFrame(excel_data)
# 保存为Excel文件
excel_filename = f"search_results_{timestamp}.xlsx"
df.to_excel(excel_filename, index=False)
print(f"\n所有公司检索完成，结果已保存到 {filename}")
print(f"查询不到的公司名称已保存到 {no_data_filename}")
print(f"Excel表格已保存到 {excel_filename}")
```  
  
填入公司名在dz.txt  
 结束好后会生成json  
 格式文件和xlsh  
 文件  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUaZcry6jibXqAyAe75ncrVJpCqNDficia1vjKGAMhbJVK3fJ6tZgp85TjIuoH5HicYicx1fPHZEKcPN2qJyliaGJuYKBicdVvTq4zNI8/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWAtJrDHwJaG25avlib2CvduoGCUtV7VdIicuWhwg544vaVWydNz7smhpBkggqRerZ7JLX71bLkSibpSQ7wP3NVXy4iauSibBuMK5ibo/640?wx_fmt=png&from=appmsg "null")  
  
通过这个步骤收集到的域名资产我一般是保留200  
状态码,之后便会开始nuclei  
和afrog  
同步进行扫描,收取漏洞标准没有限制所以在手工测试前,配置好的自动化工具就会帮我们找好一些swagger  
泄露 ,目录遍历,以及一些CVE  
 和高危的端口服务,可以再进行弱口令的爆破等等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVNC7J9J9ib1OoUgpn7aGpJ3pTkqEuRia7PtordMwBQIdd4FCffroicEVdhavBMveCbwzDbo50sQ3VxOTzrZ1Z2umZdOYIpCUEGNc/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWjVfYdDdG93PZPVQ8jgNYC51Neqn0fCAteEHVDlDgeHc8fMicgYM0h41sUGTKHID3CE0ChAU07AicicgztR7HAtIib8AjjdGdetLk/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUGjHLXDOSlUIomntqfHDdcypcOTeWt13VFfVKd0cMZy4He2C5fkBbSfS4Jia70f5Zibw7pvbibHWttzqyuVvhv5icxOiaZCBtnc4k4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAUuwTBoWe1HoyW3icz1w52Ykz0bd43YYbjF7PLXD2siaicETWRW9GicOxssExh90eYfMt4oPTT71zeCXNRXE61Nu5J0npiaZVSqslIY/640?wx_fmt=png&from=appmsg "null")  
### 渗透实战  
  
当资产在被扫描器轮番测试时，这个时间就开始逐一对资产进行手工测试,开局一个首页,看起来确实没什么功能点,现在可以选择的测试是目录扫描和接口未授权  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXRPStC0kNk8h7sqyJEG5n3NKjEz9bHFnvvFegOgLFSDlqnhX5Ya0L81Snc3HLQq1dXZus4aJOftcIickIOvibCic6bSZ0Psd24PA/640?wx_fmt=png&from=appmsg "null")  
  
打开我的dirsearch  
为了应对不同的目标架构还有需求,需要在多个不同的命令行参数间转换,各位白帽师傅可以让ai  
 辅助写一个bat  
 脚本去调用工具不同的参数从而在单个目标 多个目标,递归目标间迅速切换  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUKicN0xF8UZTsVgQatqericHJ613mbVm3MkCVU6ljutSWJv4CMNTs2lMGYAldyJEvbJnZ0f3uCRX8X5fF1c0hX84GsDQf4A9NR4/640?wx_fmt=png&from=appmsg "null")  
  
相信大家都发现了出现了一个Admin  
目录大概率是网站管理后台  
```
http://xxxxx.com/Admin/
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVTyZ4O5RtbapOH7Y3wgUwJyTRGsosbIibkyQ7KlEicyicibeFsuk3UjuYYRNUnOqZMv4ia5PSWBYUKZx1F0pNxWkEtLoulibPYQHaIY/640?wx_fmt=png&from=appmsg "null")  
  
提示超时,那么应该是进行鉴权 了,状态码301  
调整到了网站管理登录页面  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWG3yT1ZbbUysBFiazu7vo1BsRAzg03TZZibXlLCAzXkGicbP11FnKT2F0wcCYLYp1icRE6XyY8hHdFrg9eyWIsiadke3H1TJ54qLVA/640?wx_fmt=png&from=appmsg "null")  
  
登录框先尝试了简单的弱口令admin admin  
 几个经典账号密码,均失败,注意到网站标题是xx  
网络,这个时候我在想这个会不会是个框架呢,遂寻找是否有相关文章  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVygbPTIib2jpvicbPR9dOciby8hwlichMtchNsfiawFKnLPS0AP2ommgshGEwX1B2ypqnBlnlXYcrnMibcSBH1JXuLKaqJIWm8ibQZv4/640?wx_fmt=png&from=appmsg "null")  
  
查询到了对应的服务商企业,但却十分小众,并没有公开的漏洞,开始测试接口看着能不能信息泄露,但是接口同样少的可怜,此时常规思路已经穷尽,站点还是没有拿下,哈基W 还是办不到吗。。。  
  
此时只剩下两个选择,继续尝试突破登录框,虽然有验证码但是开启验证码插件还是可以继续爆破的不过完全是听天由命,二是继续在目录处做操作,既然一开始就可以爆破出登录框,证明站点防护并不是特别好,第一层目录就是admin  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXxxVTVfjLgLYywVOsh3KpS4kky1cuwN9cSPG84wqCxWneDWYPR1F92oMjfj4hfOvw6ia2ZXJ72lhmhXLBpVTe3xSiaerX0D41LE/640?wx_fmt=png&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAXP46szoMYZnWXlepd9COBkWia9NdAlpDardnc8uPrAM7uG2O659iaic66zrgKNgQuR8KqCvcJwSiaMjVj1ibOFocKV6lMBaEDvF0jQ/640?wx_fmt=png&from=appmsg "null")  
  
回到第一步查看dirsearch  
 结果,我擦看我发现了什么,朴实无华的password.txt  
 不会吧不会把 不会真有人把密码写进目录然后没有删掉吧,开什么玩笑啊 居然这么简单吗  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVp59umOCnrjibIBquocfb2dyN3HM4zPUd6zgAEia3Tjdm732icxwNy3KiaNevOV9ynJ10EJQ6O4NdUYWar3qkM5kQ7eNzxFMPnbhk/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWoAqDCWNDFJHkBTkW3SdtmepCtZzolY5ePicB6aNEa15MicXvVBZrdgRva5TFU6rOZycQibzdZDhqIYO1dkcDPiap6jZf6oibyRR8k/640?wx_fmt=png&from=appmsg "null")  
  
一气呵成,拿下后台,点到为止  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAWOEwJ1XFgYwDiaDZNZMdPJjvd8am33OuGvkF4GsicDBzBRM7YwILxeWIGricTXHibEylGUZFfnIXe2fc44dsY76mWwLibmzEyWp7zY/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVsmwSM9hkwic9icZvcsOIHyWocTwZWMvOz8jMf2ZDjRh2N337ZibpMmicOuAZgu9Hr78ewPqsfp0CVuHvWTFicGGicQLibMz31g7heZA/640?wx_fmt=png&from=appmsg "null")  
  
  
**0x03总结**  
  
没有华而不实的屠龙术只有重复99个数据包,仅有第100个数据包产生了惊喜,唯有点滴的付出,你坚持的东西总有一天会反过来拥抱你; 之前文章觉得过于死板加入一些诙谐幽默的叙事方法,让各位读者阅读我的文章不像是一本正经的聊技术,更是像一位朋友一般分享着我的挖掘经历以及心态转换过程,看的开心又能学到技术;欢迎学习交流。愿各位师傅在后续挖洞之路中，精准定位漏洞、高效挖掘，天天出高危、次次有收获，挖洞顺利、不踩坑、多拿奖励，共同提升支付业务安全测试能力！🔥  
喜欢这类文章或挖掘SRC技巧文章师傅可以点赞转发支持一下谢谢！  
  
  
**内部星球VIP介绍V1.4（更多未公开挖洞技术欢迎加入星球）**  
  
  
**如果你想学习更多另类渗透SRC挖洞技术/攻防/免杀/应急溯源/赏金赚取/工作内推，欢迎加入我们内部星球可获得内部工具字典和享受内部资源/内部群🔥**  
  
🚀  
1.每周更新1day/0day漏洞刷分上分，目前已更新至5294+;  
  
🧰  
2.包含网上的各种付费工具/各种Burp  
漏洞检测插件  
/  
fuzz字典  
等等;  
  
🧩  
3.Fofa/Ctfshow/360Quake/Shadon/零零信安/Zoomeye各种账号高级VIP会员共享等等;  
  
🎥  
4.最新SRC挖掘/红队/代审/免杀/逆向视频资源等等;  
  
🧪  
5.内部自动化漏扫赚赏金捡洞工具，免杀CS/Webshell工具等等;  
  
🎯  
6.最新0Day1Day漏洞POC/EXP分享地址（同步更新）;  
  
https://t.zsxq.com/KcKlh  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq7cpyLKdrg9g0QRpvkvBaQicGaNoLjesB2YZuPd6RMJOmxdwV8BBcEX8hjsT3OL6DuGpSedCkl2Mhw/640?wx_fmt=png&from=appmsg "")  
  
🔥  
7.详情直接点击下方链接进入了解，后台回复"   
星球  
 "获取优惠先到先得！后续资源会更丰富在加入还是低价！（即将涨价）以上仅介绍部分内容还没完！**点击下方地址全面了解👇🏻**  
  
  
**👉****点击了解加入-->>2026内部VIP星球福利介绍V1.5版本-1day/0day漏洞库及内部资源更新**  
  
  
结尾  
  
# 免责声明  
  
  
# 获取方法  
  
  
回复“**app**  
" 获取  app渗透和app抓包教程  
  
回复“**渗透字典**  
" 获取 一些字典已重新划分处理**（需要内部专属fuzz字典可加入星球获取，内部字典多年积累整理好用！持续整理中！）**  
  
回复“**书籍**  
" 获取 网络安全相关经典书籍电子版pdf  
  
# 最后必看  
  
  
      
文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如  
用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。  
本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。  
如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请在24小时内删除，请勿用于商业行为，自行查验是否具有后门，切勿相信软件内的广告！  
  
  
  
  
  
# 往期推荐  
  
  
**1.内部VIP知识星球福利介绍V1.5版本0day推送**  
  
**2.最新Nessus2026.2.9版本下载**  
  
**3.最新BurpSuite2026.1.1专业版下载**  
  
**4.最新xray1.9.11高级版下载Windows/Linux**  
  
**5.最新HCL AppScan_Standard_10.9.1下载**  
  
渗透安全HackTwo  
  
微信号：关注公众号获取  
  
后台回复星球加入：  
知识星球  
  
扫码关注 了解更多  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RjOvISzUFq6qFFAxdkV2tgPPqL76yNTw38UJ9vr5QJQE48ff1I4Gichw7adAcHQx8ePBPmwvouAhs4ArJFVdKkw/640?wx_fmt=png "二维码")  
  
  
上一篇文章：  
[Nacos配置文件攻防思路总结|揭秘Nacos被低估的攻击面](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247492839&idx=1&sn=b6f091114fbd8e8922153a996c8f4f1c&scene=21#wechat_redirect)  
  
  
喜欢的师傅可以点赞转发支持一下  
  
