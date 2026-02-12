#  React2Shell漏洞突袭：漏洞深度剖析与企业防御实践  
原创 安全知不道
                    安全知不道  安全知不道   2026-02-12 09:04  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8rhSLTdQtf0euby3FKCQZicvUIKQiczWhPtherqWO1SnC0z6SicYw5VdZTLvn62dOSavnEvSfBY7iaRP3fJSqsrDOmdEBHicJhIPibaU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8oqqKD4288fdZ474ktQAV3ibX66iagN7JdFAjmIEmNH4pD7941YqYPuB3QaSFOgxTNHS9uKqFvWHXc3YkRdVesKKWNOmeET4ichz4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8paKticgWpkdEa0qoywFdMH1qhnBYb7Yakjd7Ep554j8R10Wm9GQ1PAOaq7FtibBr0j9X0LUibOU88aaFuibtKwE7uEXS7m5r5jzW0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8o2hHAdZpHeSSt1dTjfgibzdiajSu9hKsqWeOyLurzBxcBlnUd4P2gPAT6I1OCJv0kC2wVE3bNcSxpSlNw7W8oekaicViafmD2Zciak/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8rf4QsxcONENHp6ZS5yXib5TACXNwVVobOgGeEq7GELaLoUqrVPyO2iaIiatfdx3mfcqGProOpDuIx1TVFYHbQicmHiar1eSLS0vyl4/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8ohtjy1iaoPWnBgmoibNSMKM6m5eQYfnNEsGAiafXiaIN1POeQprMPlpx0d4bKML7Fq23yWUgBiaa0uFuUPvBGyibseODhcufGAAeu8s/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8rWfQEWGSZNpEBGjiauEbn8ODRq4mFlM9qI2k2ibicKvic4O1nIkb8olPsucvys8nK5Y9wczUc3xNkrJeoE8rQpEDKvHHISVgVnaU0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8qGh1HYFEribXcic8RJD0XwlwM73nGf0dIhvLSXCWSXKFKeW8r5wHibG89Cv5fibRmuJfD9xANmZA2GhA5s8tsPgpvicYnghichwia8Lw/640?wx_fmt=png&from=appmsg "")  
  
**React2Shell漏洞**  
  
突袭：漏洞深度剖析与企业防御实践  
  
  
  
近期互联网存在大量针对React2Shell漏洞（CVE-2025-55182）的扫描探测与攻击尝试，经验证该漏洞可在业务场景中实现远程代码执行，存在极大的安全风险。深入分析漏洞根因、利用方式以及防护思路，既是防范安全风险的关键路径，也是企业履行安全责任的必要举措。在此背景下，我们第一时间展开漏洞排查、整改和治理工作，并梳理该漏洞的全流程解析与企业防护思路，为后续开展安全防护工作提供技术参考。  
  
CVE-2025-55182是React Server Components存在的严重安全漏洞，由于未对原型链敏感属性进行过滤或限制，该漏洞允许攻击者在无需身份验证的情况下执行任意系统命令。影响范围包括Next.js 14.3.0-canary.77至16.0.6版本、React 19.0.0至19.2.0版本以及其他依赖该组件的软件。  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8r4X3cDVk5fUNpIsUPoRaA3jfZCtbQHwu0hPUxyOg771PhneeNHbKhJKBLLpF8d0ujIwturYpYDJibwHOzlm6hLW2V8KuReib6Po/640?wx_fmt=png&from=appmsg "")  
  
**漏洞原理**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8qete2pdQspUcs7zmJsKpS9Fd4KpAicmQFNOSjAJumAzO8HAAnN98mpUZcyAENrlpXTUPOvYByhMg5EYx8yxDSehs5MwqBOwrGw/640?wx_fmt=png&from=appmsg "")  
  
  
  
React Server Components是React推出的服务端渲染组件模型，通过Flight协议将生成的特殊序列化数据流式传输至客户端。攻击者可构造恶意请求数据污染原型链，通过隐式原型（__proto__）层层向上查找，导致所有继承该原型的属性/方法被注入恶意代码，最终实现远程代码执行（RCE）。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8q5b8pq3BPficr6HBg2xBDPVyEAXnaYOunElvneIOWNlJ8BZG5dnf8icMYHV42bbGSTJIueBibmZmbPtUYLgt02oiaJgDTdPDCYGuY/640?wx_fmt=png&from=appmsg "")  
  
图1 React2Shell漏洞利用原理  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8rViaI6ZtRnjWAyrt6zzxwpmxaq1cSuKzeXLX5pMfBcXA5M0QAyFKxT7uYrBWibG8KtYGcV2jm5lPznic8QBozicGhnfBBAwtNcAZM/640?wx_fmt=png&from=appmsg "")  
  
阶段一：恶意请求载荷构造  
  
首先构造恶意的请求数据，以Vulhub提供的CVE-2025-55182复现Payload为例，关键片段是Chunk0和Chunk1数据。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8qTwCSSN2PBHeIReBfZE8g2hDrXsStib09ulVF0yb338RLdRr5rQlXABV9USR3BOBI4jhv5leH6MlLzp7bXtjFOyibPfSB8CdHUY/640?wx_fmt=png&from=appmsg "")  
  
图2 Chunk0  
  
解析：  
-  "then": "$1:__proto__:then"的作用是让Chunk0成为Thenable对象，并赋值为Chunk1 的隐式原型的then方法。  
  
-  "status": "resolved_model"的作用是将Chunk0伪造为已解析的状态。  
  
-  "value": "{"then":"$B1337"}"的作用是触发Blob类型的解析逻辑，进而调用_response._formData.get。  
  
- "get": "$1:constructor:constructor"的作用将FormData对象的get方法替换为Function构造函数，即_response._formData.get=Chunk1. constructor. constructor = Function。  
  
Chunk1："$@0"  
  
解析：$@0代表着Chunk1引用Chunk0，表示Chunk1需依赖Chunk0的解析结果。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8oOEOc2RgZuMFtQLsGjDXo5ib2ic8oTvKhUYqC7M6hTQE9DzRQpcHx4RleGYRc9shfOq7ZXcqChax3SehH3lOlfaLN2t9MqFVEz8/640?wx_fmt=png&from=appmsg "")  
  
阶段二：恶意回调注册  
  
服务端解析数据字段并将数据反序列化为实际对象。解析Chunk0的$1:__proto__:then，识别到此处Chunk0引用了Chunk1，此时Chunk1的状态为PENDING，因此注册恶意的回调函数。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8qeppfwHUC7cC2eASSZRibP59icVFPFAHWxoaDk1oCibzx7NzvMuaicpef7Xk4BYy07NRXhL9j9ibMrmF9jbEZTXnc1dzX0ZN5py310/640?wx_fmt=png&from=appmsg "")  
  
阶段三：原型链污染实现  
  
解析Chunk1并完成数据处理，将Chunk1状态更新为INITIALIZED。状态变更触发Chunk1回调队列中污染回调函数的执行，回调函数内部利用原型链路径遍历完成then、get等核心方法替换。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8rV8g3BM3sS7Bx25rR3ksfvibluyfhRMYDic000TnmfSTRs2N1Ugo2b2FLQ3NOJysrAH0qNogqtDbFBD2VjtOoaTCsqaw3XGWkz4/640?wx_fmt=png&from=appmsg "")  
  
阶段四：实现远程代码执行  
  
服务端基于await机制自动调用Chunk0的then方法，执行Blob分支逻辑并拼接恶意代码生成blobKey。然后通过调用_response._formData.get方法生成恶意的Function函数，Function函数被赋值回then属性。基于Thenable对象的链式执行特性，由于返回值仍是Thenable对象，JS的await机制再次调用then方法，最终实现远程代码执行。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8pp24qV6ouslx7ib69ib0RIicn4FPKY7mxqnu2LFvmAUsvzR3KNBWy9vgqic2NHOog0BycPfz2yhTicUcLqaic85SHXce9lpjDDVpdGM/640?wx_fmt=png&from=appmsg "")  
  
**漏洞环境搭建**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8qkN1NBcorKejRSkgez1iasqKzG3xNuexYjo2jNhl7ibwzHE7Oex5YAFkMvhyIGoAWAmXesNU6oiapxOxP9nqW9ujoZw7QiaROyVmY/640?wx_fmt=png&from=appmsg "")  
  
  
  
我们采用vulhub搭建Next.js React远程命令执行漏洞环境，利用docker容器建立Next.js服务端，用于复现CVE-2025-55182漏洞。服务端操作系统为kali-linux-2023.1，客户端操作系统为Windows。  
  
在服务端拉取Docker镜像建立Next.js环境，过程如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8obBNQZqnbbicyQSPncuAuB1RhCaOI5mdjU7usibVCicvdicpXxm6VjGgcpxYRDCV9fLuF855SP1lXiaZctiaOuDoXIFKyah1hNWSH9Y/640?wx_fmt=png&from=appmsg "")  
  
图3 漏洞环境搭建过程  
  
在客户端访问3000端口，Next.js环境页面如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8oWic5s52HUUlYklIdickHZDS6DkiavF2oDBpoqZHxfVQmvDpx8s8W3VltKricmNK396EKybcIbicyRzoh3ea7jTibsKf1rvQdvHsFiaw/640?wx_fmt=png&from=appmsg "")  
  
图4 Next.js界面  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8rsMVAUZV6KhBHwLgXDGzqElpfCjYx5b0PsSIciaenf4uA6UBiaBKuOXEIHicHfLQoQKcY1ADRrSfhOFxDefDTxhxPYsdbtjCeoeg/640?wx_fmt=png&from=appmsg "")  
  
**漏洞基本利用**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8qMKNa80knlFAfs8qibY07c3SSgyKKA8GRc0gRmcpVE8svZfDjBibwySBJCSqkLGoOfoOz7Vxy383JDKPjBHSy4vCb903Iia47umQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8pb38LAYX60fXTIrsaibF9qviaueqibMcCveykicLziaumPW5vzQK7G0lZQaTYu9wnCjxib8J8ibgfXspz8vv3FdXmt0bq0nwjORPibdr8/640?wx_fmt=png&from=appmsg "")  
  
任意命令执行  
  
参照Vulhub的示例Payload，我们可以完整地复现该漏洞，实现任意命令执行的效果。运用Burpsuite工具手动构建并发送恶意请求，尝试注入命令"whoami"，响应体返回命令执行结果"root"，可以看到命令结果显示在响应头x-action-redirect。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8rVxkAj3tkswic2tXT3KllLJibLBs3rKqeoTMgluoT4sSGJneAib6P5bFDDs72icx0wkvPdELWaV19RATUwNYoUJM9hVA09N7z3lX0/640?wx_fmt=png&from=appmsg "")  
  
图5 任意命令执行效果  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8rC4lUxqlH7etckp88PzPrju9Jkcm5CBQl7YnAQWR7iaoGhl1B81HokL6QrAZAjiasIyMM4iasfIqibYxEFOojMSrXJ3YNYOHPl9Fk/640?wx_fmt=png&from=appmsg "")  
  
WEB内存马  
  
进一步地，我们可以利用该漏洞向Next.js服务端写入WEB内存马，通过构建恶意的Webshell，实现在浏览器端执行任意命令的效果。内存马脚本如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8p5lWV8mPp739mwqEiaSia9HzjUT3ozmVsyEiaYULsFNVC6DXibTxSWFIatksOA0k6YR2ibmeTymDhSFWvddM1yaLe0OZdCojHThCdc/640?wx_fmt=png&from=appmsg "")  
  
图6 内存马脚本  
  
Web内存马以无落地文件的形式植入恶意后门，具有隐蔽性、持久性和无感知的特性。这段代码的核心思路是劫持Node.js HTTP核心模块的emit方法，采用自定义函数重写emit逻辑，在恶意Payload执行完毕后再返回至原来的emit方法，实现完整的路径闭环，避免服务出现异常。这段代码的最终效果是，浏览器可访问/deep路径，通过发送带有恶意命令的request请求来实现任意系统命令执行。效果如下图所示，可以执行不同的命令（id、env、uname -a），浏览器直接返回敏感信息。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8qLZoeUtk9nkaIZfzQcSfe5RU6sjAnLNVjcbgibMcgU5lusXuM3IBxD4LzoHRFWU4B8XQkNASspzuT4H4oj0nTYMykz2j95bkic4/640?wx_fmt=png&from=appmsg "")  
  
图7 Webshell实现RCE效果-1  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8r8tRboW0FpFoh0SibNPC6eVicU49EiaDib7SP6D7TvrKykEicOTVnjbZZHQI7NQn0QyRLibk5pseZ56EJI23QwTg5SmAdicFHp6F0Jog/640?wx_fmt=png&from=appmsg "")  
  
图8 Webshell实现RCE效果-2  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8okjWguqB2VN5VPHgAM4QTSEDdiciaeyyKMwMkBbpUF6lKLmOhmKT17yoYSRibf7Au3NqT4VJSxfib2SLgyn1OKw2k67Uibx5ZZZqRs/640?wx_fmt=png&from=appmsg "")  
  
图9 Webshell实现RCE效果-3  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8reoCz4KJibuIPQdJmEkZX9ySlJYyUPv9uCmDhia7BaicA7K2AGhU5uky4oa5hcwuiaq9lDMiaice9TwkH1fAjIzLpntpvEYf29CnfWk/640?wx_fmt=png&from=appmsg "")  
  
**漏洞高阶利用**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8oPWp3X0T1ILjDCrUR6IkNicTdWdmRTFSdks6moaI69YRgPZPn3qfwbtCDb7C2LRPGIP09BBtLJ9TjFTniaicJYSn8uxqFf0ckTG8/640?wx_fmt=png&from=appmsg "")  
  
  
  
前面介绍了漏洞的基础利用方法，该高危漏洞可以被攻击者利用并注入后门，使得攻击者可以获取各种敏感信息并执行恶意操作。从报文分析，我们可以看到报文传输均采用明文的方式，WAF、防火墙等主流防御手段能基于漏洞特征和恶意命令检测并拦截恶意行为。“冰蝎”（Behinder）现已经历了四代升级，利用通信流量的强加密性，大幅增加了防御难度。结合加密手段，我们也可以利用Next.js React漏洞以隐蔽的方式注入恶意后门，实现漏洞的高阶利用。加密Webshell代码如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8oUAbvnfvVM7ic5bDwvrXogiabtxdyfQ8J9zeu2tdqYgDejRSUY2qvPqnexRoSficxj0NZGEoT7ogicoCXwDY7U4pX7fPB0Kh7704k/640?wx_fmt=png&from=appmsg "")  
  
图10 加密Webshell代码  
  
该段代码增加了AES-256-CBC加密的逻辑，使得服务端回显内容以密文形式返回，可以规避一些基于敏感回显的检测规则。加密算法使用随机的IV和key，即使浏览器发送相同的命令，服务端返回的密文也不一样。效果如下所示，客户端接连发送相同的命令cmd=cat /etc/*-release，页面返回的密文不同，解密之后的明文相同。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8oqCUIDRUREEY5HfHiarsutg4KZSDvaImwLunTVYkhZTOPIaptGM090HJNUw8AnITm5icIW4rdKQ0HevZvkUOxDPWDAiabmjk1gps/640?wx_fmt=png&from=appmsg "")  
  
图11 加密Webshell实现RCE效果-1  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8pAIPC2dUygqDiaaTu6uDcTC3FGzzoJ8fbG9DwSH9ww57icULwGl8M06CzPJw0xAcONiaGfMVN52lGKRePE3sD6R2uOx3METYOQLQ/640?wx_fmt=png&from=appmsg "")  
  
图12 AES解密结果-1  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8pg2OVVGT1qUK4F7O1Ylic5XoWvhUam4dsgL4sKic8hG1Qicnrx72puaZCnDYJhmYJodDtSd9Fq1xSBnf8T63Sx8vl0QyoLtiaibtLA/640?wx_fmt=png&from=appmsg "")  
  
图13 加密Webshell实现RCE效果-2  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8qx7RSrsRMYgq881GmibT0dDWVlwwmjB27qzAPBiaUDmn5bCjEN2cQr5d1paodElkibCVR8KdFoyOm76zOWg2raj1lVn4MZAxPhbk/640?wx_fmt=png&from=appmsg "")  
  
图14 AES解密结果-2  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8rqfEoYFPYZmNJmgN4U8aicwhlfp4HMAHiaqbkuic32QTN8EN74VV8hfib5cma8aPokziaVWLqhcaKw4uD7mibwRVLP8YgYae1icAh0bE/640?wx_fmt=png&from=appmsg "")  
  
**分析研判思路**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8pgibrdciboZpa3vRuIJeRxKY9N8l6EufCEvick5646q1r4eksC3UKRm1n4Vh08oUuxCw6aF5VwuNh82pVChciakeYsHqodthdibyHI/640?wx_fmt=png&from=appmsg "")  
  
  
  
针对此类复杂的高危威胁，我们可以从以下方面进行流量特征分析：  
  
**1、关注特殊的关键字**  
  
如果流量中出现了形如"__proto__"、"constructor"、"then"的关键字及其混淆变体，则可能存在原型链污染和恶意代码注入的风险行为。  
  
**2、关注模块劫持**  
  
若发现一些核心方法不是原生代码，如http.Server.prototype.emit被劫持和修改，可以基本判定为存在内存马注入行为。  
  
**3、关注非常规路径**  
  
内存马通常不挂载在正常的路由表中，如果日志中出现多个不存在的、非业务应用的路径，需高度警惕，攻击者常利用这些路径注入恶意后门。另外，合法的请求报文通常在逻辑上具备关联性，而攻击者利用的路径与前后的业务流量没有明显关联，因此也需要关注不具备业务语义的孤立路径。  
  
**4、关注异常序列化**  
  
异常的序列化JSON字符串中包含多个转义符或嵌套的函数体代码，即使返回值不是200，恶意代码依然可以生效。  
  
**5、关注异常数据负载**  
  
若请求体中出现大量密文、编码或者不规律的字符串，或是出现探测扫描、访问敏感信息、执行高危操作的可疑命令，分析人员需高度关注此类情形，对攻击源进行进一步的溯源分析。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8pKgI6PJPYicfNjjOwlQaPYbnGHiazGvicJffaXhYoEZg9DLEdeKyiaylhrmy3icAXURLOyn5oIMickRDiadCmcEnlotp3mKCpqMg0Xic0/640?wx_fmt=png&from=appmsg "")  
  
**现有防护措施**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/DYgfUBUgp8p2Z253zr513DrJJ3XUTQSjeBJ5Y4V3rZfwzAxX8wnE6TjIiaNrhhZoIl8XhG1ZEWYVjrVmibBBpK5EBJkXVcTDZgvO8lYqAxW5o/640?wx_fmt=png&from=appmsg "")  
  
  
  
由于React远程代码执行漏洞的高危特性与安全影响，我们系统性地开展各项应对工作，覆盖漏洞修复、监测防护、经验复盘与安全培训等多个方面。具体措施如下：  
  
**1、推进漏洞快速修复**  
  
在CVE-2025-55182漏洞披露后，立即启动高危漏洞排查及修复方案，安全、研发、运维等多个团队共同参与处置，保证应急响应的及时性、有效性和彻底性。全面盘点资产并梳理受影响的组件版本及相关依赖软件，第一时间向各项目组派发漏洞修复工单，督促项目组严格按照官方补丁升级至最新安全版本，尽快完成漏洞整改修复和安全风险收敛。  
  
**2、强化安全管控手段**  
  
完善安全监测体系，在流量监测设备上新增CVE-2025-55182漏洞的专项检测规则，基于漏洞特征实时感知和快速捕获典型攻击行为，重点监控恶意命令执行、异常请求构造、敏感模块调用等异常行为。全面加强防御措施，运用WAF、动态等防护设备的自动化防护规则，实现对漏洞扫描与试探攻击的快速拦截。  
  
**3、沉淀技术实战经验**  
  
针对此次漏洞开展攻击链深度研判，总结流量分析思路与应急处置方法，将相关经验补充至标准操作手册，为安全人员分析告警、处置威胁和溯源攻击提供操作规范。以攻促防，以案为鉴，掌握反序列化攻击、原型链污染、远程命令执行等攻击的底层原理和实战手法，提升未来同类高危漏洞的应急效率和处置质量。  
  
**4、开展常态化安全培训**  
  
面向一线安全人员分享CVE-2025-55182漏洞的相关资料，全面了解漏洞涉及的前后端开发知识，做到知其然，也知其所以然。通过案例讲解、漏洞复现与定期考试的方式，提升安全人员的理论水平和实战技能，推动安全意识从被动修复向主动防范转变。  
  
回顾Next.js React远程命令执行漏洞的攻击链，该漏洞是反序列化问题、原型链污染、恶意命令执行多重问题叠加的典型案例。前端框架在前后端边界模糊化的迭代演进中，序列化与反序列化环节仍是高风险攻击面。企业与开发者可以从升级最新框架版本、更新流量监控规则、增加专用防护规则、安排代码审计等方面切入，防范此类框架级高危漏洞带来的系统性安全风险。  
  
  
  
**END**  
  
  
作者|邢骏 唐志敏  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/DYgfUBUgp8oZ9pfQ8iaUficBicLiazaMIb1IrAKyK60Z6qvdUoTNeEoibbypLuMDuyhXbWlPjZqX13MxawUcwWmunVsAGf1AZMwgHdLicYZC8dHdY/640?wx_fmt=png&from=appmsg "")  
  
  
  
