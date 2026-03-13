#  DarkAngel：全自动漏洞扫描工具  
原创 子午猫
                        子午猫  网络侦查研究院   2026-03-12 23:38  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2bujwd3M0M1ICStsbhAHWtth8dQwoBBFoNDafDAzGbm1sCA8bqVWIjs40A8lu9rtuD4yeOOwDNadg/640?wx_fmt=png "")  
  
#   
  
DarkAngel 作为一款全自动的白色帽子漏洞扫描器，凭借其全面的功能和强大的性能，在网络安全领域崭露头角。它不仅能够对各类资产进行监控，还能快速准确地扫描出潜在漏洞，并生成详细报告，为网络安全防护提供了有力支持。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/mQFl6fQOc0o8R997icRBD2brU2dmSszT324sx1VaJtDy8zWLxM1yiatE6KYTB1hWhln5de3xEQdaeaLpWo7VUaSzTlUx5XqBo3MuU6ct9q0Ao/640?wx_fmt=png&from=appmsg "")  
## 0x00项目基本信息  
  
DarkAngel 的项目地址为 https://github.com/Bywalks/DarkAngel ，其下载地址同样为 github.com/Bywalks/DarkAngel 。该项目在 GitHub 上获得了一定数量的 stars ，并通过特定的 License 进行授权使用，同时还在 Twitter 上有相关推广。  
## 0x01功能亮点  
### 0x0101资产监控与管理  
1. **Hackerone 与 Bugcrowd 资产监控**  
：DarkAngel 能够实时监控 Hackerone 和 Bugcrowd 平台上的资产，及时发现新出现的目标，为安全扫描提供最新的对象。这使得安全人员能够紧跟这两个重要漏洞平台的动态，确保对相关资产的安全状况了如指掌。  
  
1. **自定义资产添加**  
：除了监控特定平台资产，用户还可以添加自定义资产。这一功能极大地拓展了扫描范围，满足了不同用户对特定目标进行安全检测的需求，无论是企业内部的特定系统，还是外部关注的特定网站，都能纳入扫描范畴。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0ovDQibdlgx2fpkkB2Zk0fg3ibgChSGia65ALcDY7uBc13buEmY7hLXsCia0RLRcmBibk2Nciaw8dLEIhNIXZx6Z1zE4nIJ7tvUsZNUw/640?wx_fmt=png&from=appmsg "")  
### 0x0102全面的扫描能力  
1. **子域名扫描**  
：通过强大的子域名扫描功能，DarkAngel 可以发现目标主域名下隐藏的众多子域名。许多安全漏洞往往隐藏在这些不易察觉的子域名中，该功能有助于全面排查潜在风险，扩大安全防护的覆盖范围。  
  
1. **网站爬虫**  
：利用网站爬虫技术，DarkAngel 能够深入目标网站内部，抓取网站的各种链接、页面结构和内容信息。这为后续的漏洞扫描提供了更全面的数据基础，确保不放过任何可能存在漏洞的角落。  
  
1. **网站指纹识别**  
：凭借先进的网站指纹识别技术，DarkAngel 可以准确判断目标网站所使用的技术框架、中间件、CMS 等信息。这些信息对于针对性地进行漏洞扫描至关重要，不同的技术架构可能存在特定类型的安全漏洞，准确识别有助于提高扫描效率和准确性。  
  
1. **弱点扫描**  
：DarkAngel 具备全面的弱点扫描能力，能够检测出多种常见的安全弱点，如 SQL 注入、XSS 跨站脚本攻击、文件包含漏洞等。通过对这些弱点的扫描，提前发现潜在的安全威胁，为及时修复漏洞提供依据。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/mQFl6fQOc0qYYfDYeiaeK4jDQJREBV3AQMiaZzBX2mdmeSGvyNfX8Dv7M4NGQcJWKmWmqFmE78zyKjKzgSd1Xpibcl7bP3nP3MzeFiap5VebFpQ/640?wx_fmt=png&from=appmsg "")  
### 0x0103漏洞处理与通知  
1. **漏洞 URL 自动截图**  
：一旦发现漏洞，DarkAngel 能够自动对漏洞所在的 URL 进行截图。这一功能为漏洞报告提供了直观的证据，方便安全人员和相关人员快速了解漏洞的实际情况，有助于后续的分析和处理。  
  
1. **自动生成漏洞报告**  
：该工具会自动生成 MarkDown 格式的漏洞报告，并存储在 /root/DarkAngel/vulscan/results/report 目录下。报告内容详细，包括漏洞的发现时间、漏洞类型、影响范围、详细描述以及修复建议等信息，为漏洞的修复和管理提供了清晰的指导。同时，它还支持自添加漏洞报告模板，用户可根据实际需求定制报告格式。  
  
1. **消息通知**  
：DarkAngel 支持多种消息通知方式，方便用户及时了解扫描结果。  
  
1. **电报通知**  
：用户可以先查看如何获取配置（TG 配置），获取参数后，在 /root/markup/view/logo.ini 中配置参数，以启用企业 TG 通知。这种方式能够及时向相关人员发送漏洞结果和扫描过程的通知，确保信息的快速传递。  
  
1. **企业微信通知**  
：参考企业微信开发接口文档获取参数后，在 /root/markup/view/page.ini 中配置参数，即可开启企业微信通知。企业微信在企业内部沟通中广泛使用，通过该方式通知扫描结果，方便团队成员之间的协作和信息共享。  
  
## 0x02安装流程  
  
DarkAngel 的项目整体架构为 ES + Kibana + scanner，因此安装过程需要分别处理这三个部分：  
### 0x0201ES 图像安装  
1. **拉取 ES 镜像**  
：执行 docker pull bywalkss/darkangel:es7.9.3  
 命令，从 Docker 镜像仓库中下载 ES 镜像。  
  
1. **部署 ES 镜像**  
：运行 docker run -e ES_JAVA_OPTS="-Xms1024m -Xms1024m" -e "discovery.type=single - node" -d -p 9200:9200 -p 9300:9300 --name elasticsearch elasticsearch:7.9.3  
 命令，启动 ES 容器。其中 -e ES_JAVA_OPTS="-Xms1024m -Xms1024m"  
 设置了 Java 堆内存大小，-e "discovery.type=single - node"  
 指定以单节点模式运行，-d  
 表示在后台运行，-p 9200:9200 -p 9300:9300  
 映射容器端口到主机端口，--name elasticsearch  
 为容器命名。  
  
1. **查看日志**  
：使用 docker logs -f elasticsearch  
 命令实时查看 ES 容器的运行日志，以便及时发现和解决可能出现的问题。  
  
1. **问题解决**  
：如果遇到问题，可执行 sysctl -w vm.max_map_count=262144  
 命令调整系统参数，然后重启 Docker，即 docker restart elasticsearch  
 ，确保 ES 正常运行。  
  
### 0x0202Kibana 图像安装  
1. **拉取 Kibana 镜像**  
：执行 docker pull bywalkss/darkangel:kibana7.9.3  
 命令下载 Kibana 镜像。  
  
1. **部署 Kibana 镜像**  
：运行 docker run --name kibana -e ELASTICSEARCH_URL = http://es - ip:9200 -p 5601:5601 -d docker.io/bywalkss/darkangel:kibana7.9.3  
 命令启动 Kibana 容器。这里需要将 es - ip  
 替换为实际的 ES 服务器 IP 地址，-e ELASTICSEARCH_URL  
 配置 Kibana 连接到 ES 服务器，--name kibana  
 为容器命名，-p 5601:5601  
 映射端口，-d  
 使其在后台运行。  
  
1. **查看日志**  
：通过 docker logs -f kibana  
 命令查看 Kibana 容器的日志。  
  
1. **问题解决**  
：若出现问题，同样执行 sysctl -w vm.max_map_count=262144  
 命令，并重启 Docker，即 docker start kibana  
 。  
  
### 0x0203扫描仪图像安装  
1. **拉取 Scanner 镜像**  
：执行 docker pull bywalkss/darkangel:v0.0.5  
 命令获取 Scanner 镜像。  
  
1. **部署 Scanner**  
：运行 docker run -it -d -v /root/DarkAngel:/root/DarkAngel --name darkangel bywalkss/darkangel:v0.0.5  
 命令启动 Scanner 容器。其中 -it  
 表示以交互模式运行，-d  
 后台运行，-v /root/DarkAngel:/root/DarkAngel  
 将主机的 /root/DarkAngel 目录挂载到容器内的相同目录，方便数据共享和操作，--name darkangel  
 为容器命名。  
  
1. **进入 Scanner Docker**  
：使用 docker exec -it docker_id /bin/bash  
 命令进入 Scanner 容器，这里 docker_id  
 为实际的容器 ID。  
  
1. **进入根目录并下载源代码**  
：进入容器后，执行 cd root  
 命令进入根目录，然后通过 git clone https://github.com/Bywalks/DarkAngel.git  
 命令下载 DarkAngel 项目的源代码。  
  
1. **添加执行权限**  
：为确保工具正常运行，执行 chmod 777 /root/DarkAngel/vulscan/tools/*  
 和 chmod 777 /root/DarkAngel/vulscan/tools/whatweb/*  
 命令，为相关工具添加执行权限。  
  
若在 docker 容器中挂载的目录没有权限，可采用以下两种解决方案：  
1. **运行容器时**  
：添加 --privileged=true  
 参数，赋予容器更高的权限。  
  
1. **主机运行命令**  
：执行 setenforce 0  
 命令，临时关闭 SELinux 安全机制。  
  
## 0x03使用指南  
  
DarkAngel 的使用通过命令行参数进行控制，以下是各个参数的详细说明及使用示例：  
### 0x0301资产相关操作  
1. **--add - new - domain**  
：添加来自 Hackerone 和 Bugcrowd 的新域名。使用示例：$ python3 darkangel.py --add - new - domain  
 ，此命令用于监听 Hackerone 和 Bugcrowd 平台上出现的新域名，为后续扫描做好准备。  
  
1. **--scan - domain - by - time SCAN_DOMAIN_BY_TIME SCAN_DOMAIN_BY_TIME**  
：以时间间隔为条件，对 ES 库中的 pdomain 进行漏洞扫描。该模块旨在批量扫描库中的 pdomain，缓解一次阻塞整个程序的问题。使用示例：$ python3 darkangel.py --scan - domain - by - time begin - time end - time  
 ，其中 begin - time  
 和 end - time  
 需替换为实际的时间范围。  
  
1. **--scan - new - domain**  
：监控 Hackerone 和 Bugcrowd 域名并进行扫描。首次使用时，会添加所有 Hackerone 和 Bugcrowd 域名。由于资产可能较多，扫描可能需要较长时间。使用示例：$ python3 darkangel.py --scan - new - domain  
 。  
  
1. **--add - domain - and - scan ADD_DOMAIN_AND_SCAN [ADD_DOMAIN_AND_SCAN ...] --offer - bounty {yes,no}**  
：自定义增加扫描域名并对这些域名进行漏洞扫描。文件名需为厂商名称，文件内容为需要扫描的域名。--offer - bounty  
 参数用于设置域名是否提供奖励。使用示例：$ python3 darkangel.py --add - domain - and - scan program - file - name1 program - file - name2 --offer - bounty yes  
 。扫描后，子域名结果将存储在 /root/DarkAngel/vulscan/results/urls 目录中的 bounty_temp_urls_output.txt 和 nobounty_temp_urls_output.txt 文档中。  
  
### 0x0302漏洞扫描相关操作  
1. **--nuclei - file - scan**  
：使用 Nucleus 扫描 20 个 URL 文件。使用示例：$ python3 darkangel.py --nuclei - file - scan  
 ，此命令可对指定的 URL 文件进行快速漏洞扫描，利用 Nucleus 的强大扫描能力检测潜在漏洞。  
  
1. **--nuclei - file - polling - scan**  
：使用 Nucleus 对 20 个 URL 文件进行轮询扫描。可将进程置于后台，进行轮询和扫描，并侦听 URL 列表中的新漏洞。使用示例：$ python3 darkangel.py --nuclei - file - polling - scan  
 ，这种方式适用于需要持续监控 URL 列表中是否出现新漏洞的场景。  
  
1. **--nuclei - file - scan - by - new - temp NUCLEI_FILE_SCAN_BY_NEW_TEMP**  
：监听 Nucleus 模板的更新，更新时扫描 URL 列表。当前核模板版本为 9.3.1 ，可执行命令监视 9.3.2 版本更新。使用示例：$ python3 darkangel.py --nuclei - file - scan - by - new - temp 9.3.2  
 ，通过及时跟踪模板更新，确保扫描能够检测到最新的漏洞类型。  
  
1. **--nuclei - file - scan - by - new - add - temp NUCLEI_FILE_SCAN_BY_NEW_ADD_TEMP**  
：监控单个核模板的更新，更新时使用此模板扫描 URL 列表。由于存在时间差，可能出现先提交模板但未及时添加到 Nucleus 就开始扫描的情况，但扫描后 ID 会自动增加，实现边监听边扫描。使用示例：$ python3 darkangel.py --nuclei - file - scan - by - new - add - temp 6296  
 ，这里 6296 为要监控的单个模板 ID。  
  
1. **--nuclei - file - scan - by - temp - name NUCLEI_FILE_SCAN_BY_TEMP_NAME**  
：使用单个模板扫描 URL 列表。使用示例：$ python3 darkangel.py --nuclei - file - scan - by - temp - name nuclei - template - name  
 ，其中 nuclei - template - name  
 需替换为实际的模板名称，可针对特定类型的漏洞进行精准扫描。  
  
## 0x04结果显示  
  
DarkAngel 的扫描结果通过多种方式展示，方便用户查看和管理：  
1. **前端显示**  
：在前端界面，用户可以直观地查看扫描制造商、扫描域名以及扫描结果等详细信息。这为用户提供了一个可视化的操作和监控平台，便于对整体扫描情况进行把控。  
  
1. **消息通知**  
：通过电报通知（TG 通知）和企业微信通知，用户能够及时收到漏洞结果和扫描过程的消息。无论是在办公室还是外出，都能随时了解扫描动态，及时采取相应措施应对发现的漏洞。  
  
  
  
  
**END**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/4kCmTUe2v2bujwd3M0M1ICStsbhAHWtt0VVqCfFLOVnpmeNJ3R59doWtI0AmqLn4Qkic8aAS06l0pATjcYx10zw/640?wx_fmt=png "")  
  
  
