#  0day速报：棋士AI代码审计又双叒叕发现新漏洞  
 鼎夏智能   2026-02-06 08:44  
  
**漏洞速览**  
  
漏洞类型:目录遍历任意文件删除，任意命令执行  
  
产品:foxcms  
  
版本:V1.2.60  
  
源码地址: https://gitee.com/qianfox/foxcms  
  
**概述**  
  
FoxCMS V1.2.60 近日被“棋士AI代码审计系统”捕获0day漏洞，涉及目录遍历删除任意文件与模板注入导致命令执行，可导致服务器被控制。  
  
“棋士”作为本次漏洞的发现者，通过AI驱动的深度代码分析，一次性定位了该系统中相关联的多个风险点，并精准解析其利用链，再次证明了其在自动化代码审计与0day挖掘方面的综合能力。  
  
**漏洞一：目录遍历任意文件删除**  
  
01  
  
**项目导入**  
  
将源码压缩包直接上传至“棋士”AI代码审计平台，系统自动解析并准备扫描。  
  
![](https://mmecoa.qpic.cn/mmecoa_png/yCicxXA8ruibnuvHa1LWCRITfRaKBeuOia4j7R6vibuo6UQtZibrDj3zzm5ibicQuibibpGFZ7ALFfTic6fgmQebtLJGeVEbJpEVTtEgJEx2ASjmfEstI/640?wx_fmt=png "")  
  
  
02  
  
**扫描检测**  
  
平台自动完成全量代码扫描，并智能标记出多处潜在风险点。  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/yCicxXA8ruibllwfzpNJH66JrbwI3Bk7j2XZuM15m9fvLa0ibTgTLGzZLNh9HWOu367UhWgCschiajwdANRNyD9dcSBuBnKA767LibyLfPUKOxyw/640?wx_fmt=png "")  
  
  
03  
  
**结果查看**  
  
扫描报告清晰列出两处高危代码位置，附带详细漏洞说明与风险评级，一目了然。  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/yCicxXA8ruibllS3IDliakBjibfJMY8jKbPGQhrpwNnnCz8fiaQy0ibg2IGzicTCAcl6OXeq6mm1EbQe7CndwFhQSibpZdMFgCCic3By02egBJvDia9kc/640?wx_fmt=png "")  
  
  
04  
  
**漏洞深度解析**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oziaey0zkUgmcr4jYoOPXNtves8oMbHJHd5SzSIricb7icTSVJUbLewOTnaEniaNtknmaiacVvqVLEJRNIHNocExrPQ/640?wx_fmt=png "")  
  
**AI 赋能漏洞机理分析**  
  
通过“棋士”内置的 AI 专家系统，即便对PHP审计经验较少的用户也能快速理解漏洞本质。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oziaey0zkUgmcr4jYoOPXNtves8oMbHJHd5SzSIricb7icTSVJUbLewOTnaEniaNtknmaiacVvqVLEJRNIHNocExrPQ/640?wx_fmt=png "")  
  
**攻击原理**  
  
- $id = $this->request->param("id"); 直接获取用户输入的 id 参数  
  
- $sqlPath = app()->getRootPath() . 'data' . $id; 将用户输入的 id 拼接到系统路径中  
  
- 攻击者可通过构造恶意参数（如 ../../../../etc/passwd）访问或覆盖系统任意文件  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oziaey0zkUgmcr4jYoOPXNtves8oMbHJHd5SzSIricb7icTSVJUbLewOTnaEniaNtknmaiacVvqVLEJRNIHNocExrPQ/640?wx_fmt=png "")  
  
**风险场景**  
  
- 删除服务器关键文件  
  
（如 id=../../../app/config）  
  
- 读取敏感文件（如 id=../../../../etc/passwd）  
  
- 覆盖代码文件植入后门  
  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/yCicxXA8ruibnRzZFm4kLC39wFZClAVuEhxBc7ichTYqfpJ1prVNcfibcDNGyoVvWMKiaClRKbDFuiasMyNiblPSZQPJuWv3HkqKz8Jb3DUVWMKMeI/640?wx_fmt=png "")  
  
  
05  
  
**实战验证与 PoC 辅助**  
  
棋士”不仅定位漏洞，还提供验证脚本（PoC）辅助测试。  
  
![](https://mmecoa.qpic.cn/mmecoa_png/yCicxXA8ruibm5y90mFvyrlOEFBlOXKKHeOW8vLnmr73UyiaBk0R9tPzu668xicr3GhMmVzVwJmDPlEQuNpWQEEWY9oo1GoGmPWQibfN2MjbDwEU/640?wx_fmt=png "")  
  
搭建漏洞环境，进行漏洞复现。  
  
http://192.168.106.4:8090/index.php/admin7525  
  
![](https://mmecoa.qpic.cn/mmecoa_png/yCicxXA8ruibmOtaId7Swrj3vjMoCv3V0GTuwJGHYic7Cm3zGWw3CC2v3ZWwz5KZgdZYic9laqziaoPTjFRJibxO0iazb5YJIYelMv6CgJmSfiaKlPk/640?wx_fmt=png "")  
  
即可实现服务器任意文件删除。  
  
06  
  
修复方案  
  
棋士 AI代码审计针对该漏洞提供了多层次修复方案：  
- 对用户输入的路径参数进行严格的验证和过滤，防止目录遍历攻击。  
  
- 使用basename( )等函数确保只操作指定目录下的文件。  
  
- 实现路径白名单机制，限制可访问的目录范围。  
  
- 对文件操作进行权限检查，确保用户只能操作其有权限的文件。  
  
  
  
**漏洞二：任意命令执行**  
  
01  
  
**漏洞定位**  
  
通过“棋士”扫描，快速定位到代码中的模板注入风险。  
  
![](https://mmecoa.qpic.cn/mmecoa_png/yCicxXA8ruibmWku2cAmCoR96RjicnOLjEEAYdNfByqDaTwoBYBchQVag6kZGcK8GWf1kyq1fiahAYJ5gJ91L8nsnUXhARGarlkZWV3p5peqQts/640?wx_fmt=png "")  
  
  
02  
  
**漏洞深度解析**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oziaey0zkUgmcr4jYoOPXNtves8oMbHJHd5SzSIricb7icTSVJUbLewOTnaEniaNtknmaiacVvqVLEJRNIHNocExrPQ/640?wx_fmt=png "")  
  
**漏洞分析**  
  
漏洞类型 : 模板注入导致的远程代码执行 (Template Injection to RCE)  
  
受影响函数 :tagDiyform   
(以及其他拼接 PHP 字符串的标签函数)  
  
Fox.php 中 tagDiyform 函数将用户输入的 tablename 直接拼接至PHP字符串，未转义单引号，导致代码注入。  
  
查看 Fox.php 第 384 行的代码：  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/yCicxXA8ruibmCHYicUDFV8RyaXRbzxIribcDXraIWHFE1cY8LWxcicFIhBfOkwRMSp3OZUvbIMnVb8pfS1ibo6h8eprlkKOUupD2XibBUtQdNs5mg/640?wx_fmt=png "")  
  
开发者试图构建一个 PHP 数组  
$param 。变量 $tablename 被包裹在单引号中。如果我们传入的 $tablename 包含单引号，就可以闭合前面的字符串，插入任意 PHP 代码。  
  
最终生成的 PHP 代码逻辑如下：  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/yCicxXA8ruiblmuH4k3am24yHLJ5RwuH019q78icjufT6uWAcCiaSL8uHCtBYZk9Mqx7NiaibdohUODsxjQQXBEBdy4N5IQt1CNicEl0fJWetbbpuY/640?wx_fmt=png "")  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oziaey0zkUgmcr4jYoOPXNtves8oMbHJHd5SzSIricb7icTSVJUbLewOTnaEniaNtknmaiacVvqVLEJRNIHNocExrPQ/640?wx_fmt=png "")  
  
**漏洞复现**  
  
通过后台模板编辑index.html插入exp;  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/yCicxXA8ruibmQymOuaSMbdSxXDwCzrjT3NyBvD4Uiaun49orNiaevLml1krY9kJ2LSthTibXsXt8sYcF4lwvOlQeDIknbYwSib5TlpIcb2ncticMc/640?wx_fmt=png "")  
  
访问前台首页确定命令已经成功执行；  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_png/yCicxXA8ruibn8JaiaqC7nib22gNxH4wkYOyrg7p16ft4R68VoKn64TicgWf1LgzYbWa1bYsf9nKOSiaicPkvbicVRWyII5kgdaibuoykST9sCqcjuHQ/640?wx_fmt=png "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oziaey0zkUgmcr4jYoOPXNtves8oMbHJHd5SzSIricb7icTSVJUbLewOTnaEniaNtknmaiacVvqVLEJRNIHNocExrPQ/640?wx_fmt=png "")  
  
**漏洞修复**  
  
必须在拼接字符串之前对所有用户输入的变量进行转义，确保单引号被转义为 \' 。  
  
总结  
  
棋士AI代码审计是一款集代码审计、AI 智能分析、PoC 辅助生成与修复建议于一体的综合安全工具。其能够显著提升漏洞发现、验证与修复的整体效率，是开发人员与安全工程师在实战中的得力助手。  
  
现在注册即可 **免费试用**  
 👇  
**https://aireview.dx-src.com**  
  
（复制链接至浏览器打开，立即体验智能审计）  
  
  
**关注我们**  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/yCicxXA8ruibnqR09y0jiaFCaUePkD5WGlKLId9kybPwbiaMzhompVwribhhX0jE59EuQ8SEnZwiastCGw93PJz7yibOA1nOLXXme79MGkc7CkviaWI/640?wx_fmt=jpeg "")  
  
  
![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/yCicxXA8ruibn5ckZzAQQ28Mbl9z4xHv1G5IA6eEsswID15uBULic4O4VYR51HFkhXcDCWbxDbQKmFnpZ41m8nJ00hMr4fyR6lbcpVLz3TK9gQ/640?wx_fmt=jpeg "")  
  
**关注公众号**  
  
获取更多  
  
AI办公资讯  
  
  
**添加客服微信**  
  
了解更多  
  
AI办公解决方案  
  
  
  
  
