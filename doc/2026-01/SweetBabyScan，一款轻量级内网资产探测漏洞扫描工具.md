#  SweetBabyScan，一款轻量级内网资产探测漏洞扫描工具  
inbug-team
                    inbug-team  泷羽Sec   2026-01-20 23:55  
  
## 简介  
  
甜心宝贝是一款支持弱口令爆破的内网资产探测漏洞扫描工具，集成了Xray与Nuclei的Poc  
### 工具定位  
  
内网资产探测、通用漏洞扫描、弱口令爆破、端口转发、内网穿透、SOCK5  
- 主机[IP&域名]存活检测，支持PING/ICMP模式  
  
- 端口[IP&域名]服务扫描  
  
- 网站爬虫截图，CMS识别  
  
- Nuclei & Xray POC  
  
- 网卡识别、域控识别、SMBGhost、MS17017  
  
- 弱口令爆破：  
  
- 文件：FTP/SMB  
  
- 远程：SSH/RDP/SNMP  
  
- 数据库：Redis/MongoDB/MySQL/SQLServer/PgSQL/ES/Oracle/Memcached  
  
- TCP端口转发  
  
- 内网穿透  
  
- SOCK5穿透  
  
### 工具截图  
  
工具根据系统自动下载对应版本的Chromium  
  
![1](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASpA0QfOzQdcE2HLUfksGMxfXPLLt9M65yXEw5D6YsjBnzJ2iamkEEic8Q/640?wx_fmt=other&from=appmsg "")  
  
1  
  
![2](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASgOzxjGoZZjbAL8qj5rroV5fa4J2ia7WReLVgqGKCu6pKS74I0lhPRfQ/640?wx_fmt=other&from=appmsg "")  
  
2  
  
![3](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASsxauMhj1jzdibtTzssPUu7oicPDGhuniaJ17BtgJsxv09KwR4mHqNAEUA/640?wx_fmt=other&from=appmsg "")  
  
3  
  
![4](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASoRllCGaibec3AMW7w1SwGdHRZVNDWnZWbVwzTvbwT8qM2ILliaibiczr6A/640?wx_fmt=other&from=appmsg "")  
  
4  
  
![5](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGAS3zhm3pvKn3ZYehia9xmf0FY2VbSqicDCosMx2JqlwBibf8J1AZsCLtsjg/640?wx_fmt=other&from=appmsg "")  
  
5  
  
![13](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGAS5efpVA777K5SUsbEe1P8DuSrLZvzZy8Ozo65XJ9HZxaH2WiajKshlTQ/640?wx_fmt=other&from=appmsg "")  
  
13  
  
![14](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASCJSic595L48PX3QLa9KDpu5br8gqlicLxW2Dn8C7hwrDjLjrwVsVCYBA/640?wx_fmt=other&from=appmsg "")  
  
14  
  
![17](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASKV0OIDzxL0JO2tricoecpibicyk78UnpCibjByIeJP4JVOmyakuGjXcpng/640?wx_fmt=other&from=appmsg "")  
  
17  
  
调高探测与扫描并发  
```
./SbScan -h 192.168.0.0/16 -wsh 500 --wsp 500

```  
  
![6](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASvCI22ibaVyaM9WEI4yTonfEMXEt7r0BfnpO6NuGgJOGxm1BtS9kTOvQ/640?wx_fmt=other&from=appmsg "")  
  
6  
  
![7](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASuEeqgM8QojvbxXiby8yRcFYV2icKiay0Aufo1KtqjUN2XLeVLqiaeozaWQ/640?wx_fmt=other&from=appmsg "")  
  
7  
  
![8](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASnZHQ5sGJyfVW2FpOkvKTabEkr19cZKxzro2tT4h4egq8LJqBozfeZw/640?wx_fmt=other&from=appmsg "")  
  
8  
  
端口扫描可以写端口号、端口范围或者常用端口类型  
```
./SbScan -h 192.168.188.0/24 -p 80,22,81-89

```  
  
![9](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASujVkg505kGqYZYfCar1bLs2z7rcmicqFBEBg8EebArnicqxkhyd2HKOA/640?wx_fmt=other&from=appmsg "")  
  
9  
  
![10](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGAS43wj0rMKfdR0T6lJUFuGevn840cpA2icO3mCBZlnkPGkum1OK1ibxYbg/640?wx_fmt=other&from=appmsg "")  
  
10  
  
列出weblogic漏洞对应的poc  
```
./SbScan --lpn --fpn weblogic

```  
  
![15](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGASMZEUWyxEJpeGCwopRGVARqtKINYpWnicia3tsVvZ6URd82PyFUdpuomQ/640?wx_fmt=other&from=appmsg "")  
  
15  
  
列出thinkphp漏洞对应的poc  
  
![16](https://mmbiz.qpic.cn/mmbiz/5975bXHXfWHzTC1iaP61NgO3EfKlGBGAS9QtqvKLC4H2UmyCwibeO9PCSAib4Cmv7S8zrDFrK0Ab9lB0b3gIibyqoQ/640?wx_fmt=other&from=appmsg "")  
  
16  
### 一、编译  
- 递归克隆项目，获取最新poc  
  
```
git clone https://github.com/inbug-team/SweetBabyScan.git --recursive

```  
- 初始化module  
  
```
go mod tidy
go mod vendor

```  
- Windows  
  
```
set GOOS=windows
set GOARCH=amd64
go build -ldflags="-s -w" -trimpath -o SbScan.exe

set GOOS=windows
set GOARCH=386
go build -ldflags="-s -w" -trimpath -o SbScan.exe

```  
- Mac or Linux  
  
```
GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -trimpath -o SbScan
GOOS=darwin GOARCH=arm64 go build -ldflags="-s -w" -trimpath -o SbScan
GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -trimpath -o SbScan
GOOS=linux GOARCH=386 go build -ldflags="-s -w" -trimpath -o SbScan

```  
### 二、运行  
- 自动扫描  
  
```
./SbScan

```  
- 根据指定IP段扫描  
  
```
./SbScan -h=192.168.188.1/24

```  
- 根据指定IP+端口扫描  
  
```
./SbScan -h=192.168.188.1/24 -p=tiny
./SbScan -h=192.168.188.1/24,10.0.0.1/16 -p=22,80,443

```  
- 根据指定IP段混合域名扫描  
  
```
./SbScan -h=192.168.188.1/24,10.0.0.1/24,www.a.com,www.b.xyz,www.c.net

```  
- 修改并发提高性能  
  
```
./SbScan -wsh=2048 -wsp=1024 -h=192.168.188.1/24,10.0.0.1/16 -p=22,80,443

```  
- 跳过主机存活检测（nsh）、POC漏洞探测（nsp）、弱口令爆破（nsw）、高危漏洞探测（nsv）  
  
```
./SbScan -h=192.168.188.1/24 -p=22,80 --nsh --nsp --nsw --nsv

```  
- 指定IP文件、密码文件、账号文件、输出excel文件、指定爆破协议  
  
```
./SbScan -h=ip.txt -wp=pass.txt -wu=user.txt -oe=test.xlsx -ot=test.txt -ssw=redis,ssh,mysql

```  
- 弱口令生成器（覆盖模式iwp、追加模式iap）  
  
```
./SbScan -h=192.168.188.1/24 -iwp -pp=test,Test -pc=@ -ps=123

```  
- 端口转发  
  
```
./SbScan --pf -sh=192.168.188.1:8080 -lp=8080

```  
- 内网穿透公网服务器端启动，启动端口默认9188可自定义  
  
```
./SbScan --pm --pms -secret=自定义密码

```  
- 内网客户端端口映射，TCP端口转发  
  
```
./SbScan --pm --pmc -secret=自定义密码 -su=公网IP:9188 -pcm=8081-127.0.0.1:8080,8082-127.0.0.1:8080,8088-192.168.166.55:80

```  
```
127.0.0.1:8080 映射到 公网8081
127.0.0.1:8080 映射到 公网8082
192.168.166.55:80 映射到 公网8088

```  
- 内网Sock5穿透  
  
```
./SbScan --pm --pmc --pmcs -secret=自定义密码 -su=公网IP:9188

```  
### 三、参数  
- 查看参数帮助命令  
  
> 白小羽  
> ./SbScan --help  
  
```
Usage:
  ./SbScan [flags]

Flags:
   -il, -isLog                         显示日志 (default true)
   -is, -isScreen                      启用截图 (default true)
   -oe, -outputExcel string            指定保存excel文件路径[以.xlsx结尾]
   -ot, -outputTxt string              指定保存txt文件路径[以.txt结尾]
   -h, -host string                    检测网段/域名，或者txt文件[以.txt结尾，一行一组回车换行] (default "192.168.0.0/16,172.16.0.0/12,10.0.0.0/8")
   -p, -port string                    端口范围：tiny[精简]、web[WEB服务]、normal[常用]、database[数据库]、caffe[咖啡厅/酒店/机场]、iot[物联网]、all[全部]、自定义 (default "web")
   -pt, -protocol string               端口范围：tcp、udp、tcp+udp (default "tcp+udp")
   -hb, -hostBlack string              排除网段
   -msh, -methodScanHost string        验存方式：PING、ICMP (default "ICMP")
   -wsh, -workerScanHost int           存活并发 (default 250)
   -tsh, -timeOutScanHost int          存活超时 (default 3)
   -r, -rarity int                     优先级 (default 10)
   -wsp, -workerScanPort int           扫描并发 (default 250)
   -tspc, -timeOutScanPortConnect int  端口扫描连接超时 (default 6)
   -tsps, -timeOutScanPortSend int     端口扫描发包超时 (default 6)
   -tspr, -timeOutScanPortRead int     端口扫描读取超时 (default 6)
   -inpo, -isNULLProbeOnly             使用空探针，默认使用自适应探针
   -iuap, -isUseAllProbes              使用全量探针，默认使用自适应探针
   -wss, -workerScanSite int           爬虫并发 (default 16)
   -tss, -timeOutScanSite int          爬虫超时 (default 6)
   -ts, -timeOutScreen int             截图超时 (default 60)
   -lpn, -listPocNuclei                列举Poc Nuclei
   -lpx, -ListPocXray                  列举Poc Xray
   -fpn, -filterPocName string         筛选POC名称，多个关键字英文逗号隔开
   -fvl, -filterVulLevel string        筛选POC严重等级：critical[严重] > high[高危] > medium[中危] > low[低危] > info[信息]、unknown[未知]、all[全部]，多个关键字英文逗号隔开
   -tspn, -timeOutScanPocNuclei int    PocNuclei扫描超时 (default 6)
   -wsPoc, -workerScanPoc int          Poc并发 (default 100)
   -gsw, -groupScanWeak int            爆破分组 (default 20)
   -wsw, -workerScanWeak string        爆破并发，键值对形式，英文逗号分隔 (default "ssh:1,smb:1,rdp:1,snmp:1,sqlserver:4,mysql:4,mongodb:4,postgres:4,redis:6,ftp:1,clcsearch:4,oracle:4,memcached:4")
   -tsw, -timeOutScanWeak int          爆破超时 (default 6)
   -nsh, -noScanHost                   跳过主机存活检测
   -nsw, -noScanWeak                   跳过弱口令爆破
   -nsp, -noScanPoc                    跳过POC漏洞验证
   -nsv, -noScanVul                    跳过高危系统漏洞探测
   -ssw, -serviceScanWeak string       指定爆破协议：ssh,smb,rdp,snmp,sqlserver,mysql,mongodb,postgres,redis,ftp,clickhouse,elasticsearch,oracle,memcached，多个协议英文逗号分隔，默认全部
   -au, -aUser string                  追加弱口令账号字典[以.txt结尾]
   -ap, -aPass string                  追加弱口令密码字典[以.txt结尾]
   -wu, -wUser string                  覆盖弱口令账号字典[以.txt结尾]
   -wp, -wPass string                  覆盖弱口令密码字典[以.txt结尾]
   -iap, -isAPass                      追加弱口令生成器
   -iwp, -isWPass                      覆盖弱口令生成器
   -pp, -passwordPrefix string         密码前缀，多个英文逗号分隔
   -pc, -passwordCenter string         密码中位，多个英文逗号分隔
   -ps, -passwordSuffix string         密码后缀，多个英文逗号分隔
   -pf, -portForward                   开启端口转发
   -sh, -sourceHost string             目标转发主机
   -lp, -localPort int                 本机代理端口
   -pm, -portMap                       开启内网穿透
   -pmc, -portMapClient                开启内网穿透-客户端
   -pms, -portMapServer                开启内网穿透-服务端
   -pmcs, -portMapClientSock5          开启内网穿透-客户端Sock5
   -s, -secret string                  穿透密钥，自定义 (default "SBScan")
   -psl, -portServerListen int         穿透服务端监听端口 (default 9188)
   -sp, -sock5Port int                 Sock5监听端口 (default 9189)
   -sau, -sock5AuthUsername string     Sock5鉴权账号
   -sap, -sock5AuthPassword string     Sock5鉴权密码
   -su, -serverUri string              穿透服务端地址，公网IP:端口
   -pcm, -portClientMap string         穿透客户端映射字典，多个英文逗号隔开，格式：8080-127.0.0.1:8080,9000-192.168.188.1:9000

```  
## 往期推荐  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/5975bXHXfWHWSVf1v5QxtGDia3OGyyTS1mR5dPls0Z3iae00agQ79GcD4j2Z2aEUbQdrlHcSkCh4xq15nFevY9EQ/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x5RpVW0wcUxibFE5KCDG7T6nsshfEz5iamGD7X3SsCZP5bdrE0hADKC5uDVg8EwyEz375ibfQnoHtyBatbOjWbWCA/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/e9ibT0DffQxicdfZC5RfRfednVeicxJ3BGqRPds8hVqD9HUBLerF2ZkXUL3QZWcibqVs2icC4aeWWwQnJt1C6YRC4TQ/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/WGsaTdHhWOSt4yPVsFBldeLOgVm2QjzrMO3QfNGxMeV6GG637UorYaiaa8KtFlj0eS0usP1WWwkaUNJ8wDiaqZ1g/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/WGsaTdHhWOSt4yPVsFBldeLOgVm2QjzrMO3QfNGxMeV6GG637UorYaiaa8KtFlj0eS0usP1WWwkaUNJ8wDiaqZ1g/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/XcvyttTN862rWx054TJiaPrmfqTibGlQkskQrnDsRMamQBhlJkp8kdU2ia0n8T3uGcicjLvScj8iaTv6sicWgumQribHQ/640?wx_fmt=jpeg "")  
  
![](https://mmecoa.qpic.cn/mmecoa_png/WxxxgSJAp0KbtfuWCiaXgNKoT4yXVS1a9vlJlIH0aGHjCtUjVCFaxEibF4lwgD8xYUyibL0FibWmkibHzKfAzDYdqqw/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/e9ibT0DffQxicdfZC5RfRfednVeicxJ3BGqRPds8hVqD9HUBLerF2ZkXUL3QZWcibqVs2icC4aeWWwQnJt1C6YRC4TQ/640?wx_fmt=jpeg "")  
  
<<  滑动查看下一张图片  >>  
  
  
  
