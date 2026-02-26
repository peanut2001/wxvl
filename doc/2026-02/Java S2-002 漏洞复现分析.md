#  Java S2-002 漏洞复现分析  
 蚁景网安   2026-02-26 08:31  
  
## 0x01 前言  
  
复现一下 S2-002 的洞  
## 0x02 S2-002  
### 漏洞简介  
  
Struts2-002  
 是一个 XSS  
 漏洞，该漏洞发生在 s:url  
 和 s:a  
 标签中，当标签的属性 includeParams=all  
 时，即可触发该漏洞。  
### 漏洞影响版本  
  
Struts 2.0.0 - Struts 2.1.8.1  
## 0x03 环境搭建  
- • 如果不想手动搭建的话，环境我已经配好了 https://github.com/Drun1baby/JavaSecurityLearning/tree/main/JavaSecurity/Struts2/S2-002AndS2-006  
  
因为 s2-002 的洞是一个 XSS，与处理的 Action 没有任何关系，所以这里我们只需要配置 .jsp  
 文件，以及 .xml  
 文件  
- • resources 文件夹下  
  
**struts.xml**  
```
<?xml version="1.0" encoding="UTF-8"?>  <!DOCTYPE struts PUBLIC          "-//Apache Software Foundation//DTD Struts Configuration 2.0//EN"          "http://struts.apache.org/dtds/struts-2.0.dtd"><struts>      <packagename="S2-002"extends="struts-default">          <actionname="login"class="com.drunkbaby.action.LoginAction"method="execute">              <resultname="success">welcome.jsp</result>              <resultname="error">index.jsp</result>          </action>      </package>  </struts>
```  
- • webapp 文件夹下  
  
**index.jsp**  
```
<%@ page language="java" contentType="text/html; charset=UTF-8"         pageEncoding="UTF-8"%>  <%@ taglib prefix="s" uri="/struts-tags" %>  <html>  <head>      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">      <title>S2-002</title>  </head>  <body>  <h2>S2-002 Demo</h2>  <s:url action="login" includeParams="all"></s:url>  <s:a href="%{url}">click</s:a>  </body>  </html>
```  
  
**welcome.jsp**  
```
<%@ page language="java" contentType="text/html; charset=UTF-8"           pageEncoding="UTF-8"%>  <%@ taglib prefix="s" uri="/struts-tags" %>    <html>  <head>    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">    <title>S2-002</title>  </head>  <body>  <p>Hello <s:property value="username"></s:property></p>  </body>  </html>
```  
  
接着在 WEB-INF 下，**web.xml**  
```
<!DOCTYPE web-app PUBLIC   "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"   "http://java.sun.com/dtd/web-app_2_3.dtd" >  <web-app>    <display-name>S2-002 Example</display-name>    <filter>      <filter-name>struts2</filter-name>      <filter-class>org.apache.struts2.dispatcher.FilterDispatcher</filter-class>    </filter>    <filter-mapping>      <filter-name>struts2</filter-name>      <url-pattern>/*</url-pattern>    </filter-mapping>    <welcome-file-list>      <welcome-file>index.jsp</welcome-file>    </welcome-file-list>  </web-app>
```  
  
项目结构如图，至此环境搭建完毕  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhcXGXiboqeoUUqjNxVJ9SibhMmNDpficFOVYjTmibJWBF104yXjZuUJV92Q/640?wx_fmt=png "null")  
## 0x04 漏洞复现与分析  
```
http://localhost:8080/?%22%3E%3Cscript%3Ealert(1)%3C/script%3E%3C%22
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxh9aEfoJR7J3TejKwAQKibic3pMtdw3q7c4Wxu7t0Q9XWJblbyojNTEWKg/640?wx_fmt=png "null")  
### 漏洞分析  
> 之前自己也没有分析过 XSS 相关的漏洞，在最后我会做一个小结来思考一下如何自己挖掘出这个漏洞  
  
  
我们先下一个断点在 org.apache.struts2.views.jsp.ComponentTagSupport#doStartTag()  
 方法处，开始调试  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhvupGia5Bt8vqcEJwEf4GRaon55AKNaXaodK2Ndo3tPKicnOApKzoibs1Q/640?wx_fmt=png "null")  
  
当在 JSP 文件中遇到 Struts2  
 标签 <s:  
 时，程序会先调用 doStartTag()  
 方法 ，并将标签中的属性设置到对应标签对象相应属性中。最后，在遇到 />  
 结束标签的时候调用 doEndTag()  
 方法。  
  
进入到了 index.jsp  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhiaVxwChkJZb43jt1vpFiaAsWm89znibPZ79qhn58xXelLM8ZHkzrTgodQ/640?wx_fmt=png "null")  
  
跟进 this.component.start()  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhKkqXxrbibQibicG5xHIiaericqog17yYzvVtrhdln2XSCpbBbHllAXMbviag/640?wx_fmt=png "null")  
  
在 index.jsp  
 中 includeParams=all  
，往下看代码知道 88 行，跟进 mergeRequestParameters()  
 方法  
  
在 includeParams=all  
 的情况下会调用 mergeRequestParameters()  
 将 Tomcat 处取来的参数，这里取到了我们输入的 payload，并且保存在 this.parameters  
 中  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhicusg0ANLKaXxZp6nBZ7moy8mnhM5b6kANibVp99otQGSjZNaBjpUdKw/640?wx_fmt=png "null")  
  
mergeRequestParameters()  
 方法运行完毕，往下是 includeGetParameters()  
 方法，也跟进去看一下；发现也是调用了 mergeRequestParameters()  
，同样是保存在了 this.parameters  
 中，不过这一次保存的是经过 url 编码的数据  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhmWibjNbEzlnjQud3mzzOQOPfjgeAxUGhcvt47XzNEibTA4eOtjNDcQ2A/640?wx_fmt=png "null")  
  
继续往下，程序还调用了 includeExtraParameters()  
 方法，跟进；这里的意思是如果有额外的参数，会被保存进这里，然后再保存到 this.paramters  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhglr0qjkEQXWicgQicM2ibBWIlbqz86bCeOoYemtibMF6WWyMicFQaeZI2NQ/640?wx_fmt=png "null")  
  
**其实到这里漏洞出发点就来了，第一次调用 mergeRequestParameters() 方法的时候那一段参数是未经过 URL 编码的，从而产生了 XSS**  
  
在执行完毕 doStartTag()  
 方法之后，会去到 doEndTag()  
 方法，我们跟进 this.component.end()  
，this.component  
 是 URL 类，所以也就是调用了 URL.end()  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhCDa8vb9GbB0Cfocx3mAkQicE5pBZCQj6WkCnuDR5sknhoClpCN0Cicqg/640?wx_fmt=png "null")  
  
往下走，第 146 行，判断目前调度器（Dispatcher）的实例是否支持这一 Struts2 组件的行为，并且判断这一个请求是否需要 Struts2 组件调用某 Action 来处理；如果不需要调用 Action 处理，则直接进入 buildUrl()  
 的代码逻辑，如果需要 Action 来处理，会先去选择/调用 Action，再进行后续操作。  
  
其实也就是 Struts2 运行的基本逻辑  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhJv2Vj4hjBBQ15YMD0u3YslIeqK8oYhtjUVMCIicxmudOzqD5HDECxKA/640?wx_fmt=png "null")  
  
此处因为我们定义了 action=login  
，所以进入到了 else 的代码逻辑，跟进 this.determineActionURL()  
 方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhUWFMGibkSI5x2fLvYibHuTS09icG7yy5nd4sETYibeNj4KEOD7dOELtMYg/640?wx_fmt=png "null")  
  
determineActionURL()  
 方法先定位到了对应的 action  
，再进行 buildUrl()  
 的操作，跟进 buildUrl()  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhDFMpTnibGXOPtVxcPk4EWy3XMFWAq3Gk4fnrxibQgRYL4JGHFkDM3skA/640?wx_fmt=png "null")  
  
再跟进  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhXZHtOqqPbOaFjArQNOy9HhBcm8yuZQicrhGcMWcicUiaWO2NQIrJlcRjg/640?wx_fmt=png "null")  
  
此时的 params 即将会被拿去拼接，造成触发 XSS 漏洞  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhVzLuzIACOgEhAHFiadt2BY71FxtsNbmY5jgzEVpr2g47OhtmeCyNyQQ/640?wx_fmt=png "null")  
  
具体拼接是在 115 行的 buildParametersString()  
 方法，跟进再跟进  
  
![](https://mmbiz.qpic.cn/mmbiz_png/3RhuVysG9LeXNDLW68MFWaUWkic6GuQxhergJV9xhzGers7icXukG2FbHzxDoXmh1HKFaQ1HHBUYriclQHic0Zjvyg/640?wx_fmt=png "null")  
> 至此，漏洞分析结束  
  
### 漏洞修复  
  
修改 **pom.xml**  
，将 Struts2 版本提升至 2.0.11（这是根据公告的，其实并没有真正解决漏洞）  
  
经过对 2.0.11.1 的代码阅读，在 UrlHelper  
 类 buildUrl()  
 方法里，第 136 行增加了如下修复代码:  
```
 // link是最终的生成的url        for(result = link.toString();         result.indexOf("<script>") > 0;         result = result.replaceAll("<script>", "script")) {        }
```  
  
太鸡肋，基本算不上修复。。。  
## 0x05 小结  
  
因为是 XSS 漏洞，成因基本都是未进行 URL 编码或某种转码，所以我们可以去看处理参数的过程进行漏洞挖掘。  
  
S2-002 还是比较简单的一个漏洞。  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1 "")  
  
学  
习  
网安实战课程  
，戳  
“阅读原文”  
  
