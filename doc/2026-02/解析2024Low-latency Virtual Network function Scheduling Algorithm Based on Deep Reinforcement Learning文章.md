#  解析2024:Low-latency Virtual Network function Scheduling Algorithm Based on Deep Reinforcement Learning文章  
原创 豆豆
                    豆豆  豆豆咨询   2026-02-02 06:33  
  
一、研究背景介绍  
  
     在传统静态网络架构中，主要存在两大问题。  
  
     其一，网络提供的服务（如防火墙、广域网加速器等）与被称为中间盒的硬件紧密耦合[1]。不同网络功能需要不同硬件支撑，导致网络功能僵化且维护困难，需要投入大量运营成本与资金支出[2][3]。  
  
    其二，静态网络模式无法满足新兴应用的差异化性能需求。  
  
    为解决这些问题，5G网络引入了网络功能虚拟化技术。网络功能虚拟化的核心作用在于实现专有设备中硬件与软件的分离，使软件能够脱离特定硬件独立运行。经过解耦的软件被抽象为独立的网络模块，即虚拟化网络功能（VNFs）[4]。这些虚拟化网络功能可根据需要动态部署于物理资源上，为网络节点提供相应的功能服务。因此，建立在可靠VNF架构基础上的网络系统，不仅能提升网络灵活性、满足服务质量要求、实现网络资源合理利用，还可替代专用硬件设备，从而有效降低运营商的运营成本与资本支出[5][6]。  
  
      
  
     在NFV架构中，若干VNF实例按特定顺序排列构成服务功能链，从而在网络基础设施上提供网络服务[7]。  
然而，在支持NFV的网络基础设施上配置SFC并非易事，尤其对于延迟敏感的SFC（如触觉互联网服务）而言，这类SFC既需要按特定顺序组合，又必须在严格的服务期限内完成[8]。为满足如此严苛的时序要求，服务提供商必须有效实施VNF部署与调度，并完成相关流量路由规划，这一挑战亦被称为NFV资源分配问题[2][9]。通常，NFV-RA问题可分解为三个主要子问题：（a）VNF组合，（b）VNF部署，（c）VNF调度。第一子问题涉及SFC的构建；第二子问题旨在将SFC中的VNF部署至支持NFV的节点，并将VNF间的虚拟链路映射到底层物理链路；第三子问题则专注于制定运行特定服务所需的SFC中VNF执行方案。  
  
      
  
    尽管NFV资源分配问题包含三项子课题，其中VNF的部署与调度始终是主要研究焦点[9]。关于VNF部署问题，学界已有诸多研究成果。例如，部分学者研究了可靠性感知的VNF部署问题，通过构建整数线性规划模型提出两种保护机制，并设计出基于动态规划的启发式算法[10]。Hyodo等人[11]将VNF部署问题建模为ILP模型，提出一种允许放宽VNF访问顺序与循环SFC配置约束的启发式算法，以实现部署成本与链路成本最小化。Alahmad与Agarwal[12]构建了两个混合整数线性规划模型，从成本与可用性维度解决VNF部署及类型选择问题，相比现有方案，该解决方案能在不违反服务可用性要求的前提下降低整体网络服务成本。冯等人[13]提出一种高级启发式算法，可将VNF迁移至其他可用节点，从而有效提升SFC的资源利用率与请求接收率。鉴于现有深度强化学习模型对不同网络拓扑的泛化能力不足，孙等人[14]将深度强化学习与神经网络相结合，显著增强了VNF部署问题中针对不同网络拓扑的泛化能力。Laaziz等人[15]设计了多目标整数线性模型，用以解决线性或非线性拓扑结构下的VNF部署问题。Rankothge等人[16]则提出两种算法，分别针对新服务请求中的VNF部署以及网络流量变化时的VNF位置调整问题提出解决方案。  
  
     关于VNF部署算法的研究已相当广泛，该问题在网络功能虚拟化领域具有关键意义。然而，  
VNF调度同样至关重要，学术界已通过多种问题模型与求解方法对此展开研究。例如，Riera等人[17]率先将VNF调度问题构建为作业车间调度问题并给出数学模型，但未提出多项式时间解法。考虑到算法复杂度，李与钱[18]基于数据包队列特性与SFC链属性提出一种数据包调度算法。陈与吴[19]设计了处理延迟模型，该模型能处理中间盒处理流中的通信延迟行为，随后提出两种相应的启发式调度算法。Mijumbi等人[20]针对虚拟机环境下的VNF部署与调度问题，提出了三种贪心算法及一种禁忌搜索算法。Assi等人[21]通过启发式算法提出一种高效节能的VNF部署与调度方法。李等人[22]则提出联合VNF部署与调度算法，采用两阶段在线算法解决该问题。需要指出的是，上述研究[19][20][21][22]在进行网络服务调度时，均未考虑网络路由与流量传输延迟——这些在实际环境中对延迟敏感的SFC而言是至关重要的影响因素。  
  
    由上述文献可知，  
现有关于VNF调度的研究大多侧重于优化调度顺序，而较少考虑VNF部署在不同节点的影响。由于不同节点CPU的处理与存储能力存在差异，VNF的处理时间亦会随之变化。此外，部分涉及部署的研究未考虑路由优化与传输延迟，导致实际场景中无法满足严格的服务时限要求。因此，  
本文提出基于深度强化学习的调度算法，旨在解决VNF部署与调度问题，确保时延敏感型网络服务在严格时限内完成，并最大限度减少未完成SFC的总数。本文主要贡献如下：（a）设定五条复合规则并训练D3QN模型，通过获取各规则的行动价值，依据价值评估选择不同规则来确定最高优先级的SFC。（b）为在尽可能满足SFC时序要求的同时降低传输延迟，采用启发式算法进行路由选择，在满足VNF功能需求的同时确定最优下一处理节点。（c）数值实验表明，D3QN模型性能优于复合规则，相较于传统DQN算法表现更为突出。  
  
    本文后续章节安排如下：第2节阐述问题描述，将核心问题分解为若干子问题，并探讨各子问题间的相互作用与影响。第3节明确定义问题，提出基于规则的深度强化学习调度模型，详细阐释VNF映射、调度及流量路由三大问题的解决方案。第4节展示数值实验结果。最后在第5节总结全文。  
## 二、问题描述与模型  
  
    The resource allocation of VNFs mainly consists of: (a) VNF  composition, (b) VNF placement, and (c) VNF scheduling.  Regarding VNF composition, a lot of existing literature have  studied it and proposed feasible solution [27][28]. this article will  not describe it further. In this section, we mainly focus on the joint  problem of VNF placement and scheduling for latency-sensitive  SFCs.  
  
    SFC is a chain of network functions composed of different  VNFs based on customer demands at the beginning of the network  service phase. These SFCs have a sequential and dependent  execution order (the next VNF can only start processing after the  previous one is completed). For example, there are one SFC with  the execution order: VNF11 → VNF12 → VNF13 → VNF14, in  which VNF12 only start to run after the execution of VNF11 is  completed.  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lWpCB8WzM55tHMStl61Yh0RQCXgaTUSC7yz70ILa8zhc7yrF5YKdkHD2Mp6Q05q4vYa76T9uulSVyicicAT0M8kg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lWpCB8WzM55tHMStl61Yh0RQCXgaTUSCu8Yp0CXRiaeOLJ1QBIAamfPhT9IT7tPkjy3hPh3ncicCa89hKwJQWqsg/640?wx_fmt=png&from=appmsg "")  
  
    The placement of VNFs is performed based on the completion  of the SFC components. Its main purpose is to find a node position  that meets the constraints of the VNF and prepares for the  subsequent scheduling phase. The VNF scheduling is performed  on the traffic of each SFC to enable more SFCs to be completed  within the specified deadline. Therefore, create a virtual network  to place the VNFs in the SFC and run them on the virtual machines  deployed on physical servers. This article considers issues such as  deploying the SFC along the chain on the network, guiding the  traffic between them while ensuring their order and required  bandwidth, and ultimately scheduling the VNFs for their traffic  according to the deadline. It is assumed that each VNF instance on  each virtual machine can be shared by multiple SFCs, but each  virtual machine can only handle the traffic of one SFC at a time as  described [20],[22]. In the remainder of this paper, the problem is  refined through examples, and the impact on scheduling is  discussed. Assuming an NFV infrastructure consists of four virtual  nodes Nthat support VNFs and five links L,The available  bandwidth of the links is 15 Mbps, as shown in Fig1.Given a set of  delay-sensitive SFCs, each composed of KVNFs, the virtual  network functions are represented by F={ f1, f2,…,fm} ,and  VNF  
l represents the function corresponding to the VNF,  where1≤ι≤m,For example, VNF1 means that the function of the  VNF is f1 , and Each VNFimust be mapped to a node Nthat has the  corresponding function.   
  
     
 流量的处理时间：  
Since each VNF may have different  processing capabilities in the network, its processing time is  represented as pt=w/ pv, where wis the size of the traffic and  pvis the processing capability of the VNF.   
  
      
流量的传输时间：Apart from the processing time of nodes, the time taken for traffic to be  transmitted through a link can also be represented as Dt=w/ b，brepresents the required link bandwidth.  
  
    According to the  above description, the SFC in this example can be represented by a  5-tuple, denoted as SFC={VNF,w,b, pt, D} VNFrepresents  the set of VNFs required for the SFC, wdenotes the size of traffic,  brepresents the required bandwidth for each virtual link , ptis  the processing time of the node, and Dis the deadline for the SFC,  Assuming that there are three SFCs in the  example, SFC={ SFC1 , SFC2 , SFC3 } SFC1 ={( VNF1 , VNF4 ), 24Mb,, 12Mbps, 2T, 10T}, SFC2 ={( VNF2, , VNF5 ), 12Mb, 12Mbps, 1T, 3T}, SFC3 ={( VNF2 , VNF4 ), 24Mb, 6Mbps, 2T, 8T}.  
  
       
    The three SFCs  arrive at the network atT=0 as shown in Fig2, and in the first  scenario where they are accepted in sequence, the situation is  shown in Fig3,They are all mapped to Node 1 at the same time and  processed sequentially in the order of SFC1 , SFC2 , and SFC3 ,at  timeT=0 toT=2 , Node 1 completed the processing of the  first VNFof SFC1 , and traffic began to be transmitted through  virtual link L1 for a duration of 2s. At T=4 ,Node 3 began  processing the next VNF, and finally completed SFC1 at T=6 ,  which is less than the deadline Dof SFC1 and meets the  transmission delay requirements. Next, we look at SFC2 .  WhenT=2 , Node 1 started processing the first VNFof SFC2 after  completing SFC1 , and completed it at T=3with a processing  time of 1s. It also began traffic transmission through virtual link  L1 , but since virtual link L1 was still transmitting traffic for SFC1 at  this time, the remaining bandwidth (15Mbps−12Mbp<12Mbps) of  the virtual link was not sufficient to meet the bandwidth demand,  so SFC2 had to wait, at T=4 after the transmission of SFC1 is  completed, SFC2 starts to transmit and reaches node 3 atT=5 .  However, since the processing of SFC1 is not yet completed at this  time, it has to wait again and complete atT=7 . But by this time,  it has exceeded the deadline of SFC2 and is therefore not accepted.  Finally, SFC3 starts processing atT=3and completes atT=5 .  At this time, the remaining bandwidth of virtual link L1 is 15Mbps,  which satisfies the bandwidth required for SFC3 to transmit. It  arrives at node 3 atT=9 and finally completes processing at  T=11 ,which is the same as SFC2 . However, the final  processing completion time exceeds the deadline of SFC3 and  cannot be accepted. It is obvious that in this situation, two of the  three SFCthat entered the network at the same time cannot satisfy  their latency requirements and are rejected. The sub-problem  impact of scheduling was proposed in [8], but the constraints and  solution methods are different from those in this paper. Inspired by  this, we describe several scenarios for scheduling the network,  ensuring that all SFCare completed before the deadline as much as possible. These scenarios are also problems that need to be jointly  addressed.  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lWpCB8WzM55tHMStl61Yh0RQCXgaTUSC43AFFqtpXg8VSw6jTox9GRwDVfWrFALGxTU9Tb43t1G0fQWdrsxOQg/640?wx_fmt=png&from=appmsg "")  
  
      
In the previous section, the completion times of SFC2 and  SFC3 were much greater than their deadlines, mainly due to the  processing order of SFCand insufficient virtual link bandwidth,  which resulted in excessive waiting and delayed SFCprocessing  time. To reduce the waiting time on nodes and links, the first VNF  of SFC3 is mapped to node 2 here, SFC1 and SFC3 are processed  simultaneously at T=0 as shown in Fig4. At T=2, SFC1 and  SFC3 have both completed processing. SFC1 continues to propagate  on the virtual link L1 , while SFC3 propagates on the virtual link L3 .  When T=7 , SFC1 reaches node 2 and begins processing,  completing at T=6. Similar to the previous section, SFC2 also  completes at T=7 , while SFC3 starts processing at T=7 and  completes atT=9 . Although SFC3 has still not met the expected  processing time, compared to the previous scenario, its completion time is much earlier.   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lWpCB8WzM55tHMStl61Yh0RQCXgaTUSChXcBXUsfFBJN8GfJUibFtrkyoqpichM5ApcHJFPI5lu4dFNW2Cp7nK5w/640?wx_fmt=png&from=appmsg "")  
  
  In sections A and B, SFC2 still failed to complete within the  deadline because SFC1 was always processed first, which caused  SFC2 , which is very sensitive to time delays, to wait for two time  units. This is not ideal. Therefore, in this section, we consider  scheduling to let SFC2 process traffic first, as shown in Fig5. At  T=0 , SFC2 and SFC3 start processing at nodes 1 and nodes 2,  respectively. At T=1, SFC2 completes processing, is transmitted  on virtual link L1 , and reaches node 3 at T=2 , completing  traffic processing at T=3. At this time, the delay requirement  is satisfied, and it can be accepted in the network. SFC1 and  SFC3 also complete atT=7 and T=9 , respectively.  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lWpCB8WzM55tHMStl61Yh0RQCXgaTUSCJZKpEKc5YBWibukjIVDQN6gfl1iaVxjudOibgOelu7AHwva335Mmiclncg/640?wx_fmt=png&from=appmsg "")  
  
    Although SFC1 and SFC2 met the delay requirement in the  previous sections, SFC3 still exceeded the deadline by one time unit.  This is mainly because SFC1 arrived at node 3 first and node 3 was  idle at that time, so it processed SFC1 before SFC3 arrived, causing  SFC3 to wait. In order to solve this problem, we choose a different  routing strategy, as shown in Fig6. As before, at  T=0 , SFC2 and SFC3 start processing at nodes 1 and nodes 2,  respectively. After SFC2 processing completes, SFC1 is processed,  and the first VNFis completed atT=3. Then, SFC1 traffic begins  to be transmitted on virtual links L2 and L3 instead of L1 , which  changes the transmission route. This allows SFC3 to arrive at node  3 first and start processing at T=6 , completing processing at T=8 ,thereby meeting the delay requirement. After  SFC3 processing completes, SFC1 starts processing and completes  atT=10, meeting the delay requirement as well. In this way, all  three SFCs are completed within the specified time and can be  accepted by the network.  From the above scenarios, it can be seen that VNF mapping,  processing order, and routing selection all have certain impacts on  their respective schedules and thus affect the network acceptance  rate. In the remainder of this paper, we will explore how to solve  these problems and combine them for VNF scheduling.   
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/lWpCB8WzM55tHMStl61Yh0RQCXgaTUSC3tJYFMUpgQARzqV5EbVE2IogMAoayo470IcytzllZ8Hqbq9MjJRDvw/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
  
