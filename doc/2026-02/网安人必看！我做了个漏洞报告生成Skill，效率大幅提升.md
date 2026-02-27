#  网安人必看！我做了个漏洞报告生成Skill，效率大幅提升  
原创 千里
                    千里  东方隐侠安全团队   2026-02-27 00:00  
  
各位少侠好，我是千里。  
  
最近鼓捣了一个新东西——安全报告编写助手，今天来给大家分享一下这段时间探索 AI Agent Skill 的阶段性成果。  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
背景：被报告支配的恐惧  
  
01  
  
相信各位做安全的少侠都有过这种经历：渗透测试结束后，面对几十个漏洞，要一个个写报告，改格式、算 CVSS 评分...一整套流程下来，光写报告的时间比挖洞还长。  
  
我之前也一直被这个问题困扰，尤其是给客户写正式报告的时候，不仅要描述清楚漏洞原理，还得注意行业合规要求。一份报告改来改去，半天就过去了。  
  
但实际上，漏洞报告只是安全工作中很小的一部分。我们更多的时间精力应该放在发现问题、解决问题上，而不是花在写报告这种"苦力活"上。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
漏洞报告的应用场景  
  
02  
  
场景一：渗透测试报告  
  
这是最常见的场景。作为乙方安全团队，我们在给甲方做渗透测试时，需要输出正式的安全评估报告。这份报告不仅要准确描述漏洞，还要符合甲方的格式要求、行业规范。金融行业要加监管合规分析，政府行业要加等级保护对应，医疗行业要加数据安全保护建议...一份报告改来改去，光格式调整就能耗费大半天。  
  
场景二：HW 期间的值守报告  
  
每年hw期间，各路人马齐上阵24小时值守。面对海量的告警，需要快速分析、验证、写出漏洞编号和利用方式。有时候一个高危漏洞出来，要在最短时间内输出简报，报送给防守方和指挥部。速度要快，格式要规范，内容要清晰。这种高强度输出非常考验报告能力。  
  
场景三：SRC 漏洞报告  
  
在厂商的SRC提交漏洞时，需要按照各厂商的格式要求来写报告。有的厂商要求详细到每个步骤，有的厂商只要概要。有的需要截图证明，有的需要复现步骤。不同厂商、不同漏洞类型，报告格式都不一样。熟悉各个厂商的报告格式，就是一个不小的学习成本。  
  
场景四：公司内部提单  
  
在大厂或者有安全团队的公司里，安全工程师需要向开发团队提漏洞单。一个好的漏洞单要包含：漏洞描述、影响范围、风险评级、修复建议。开发同学能不能看懂、愿不愿意修，很大程度上取决于你的单子写得好不好。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
怎么做的？  
  
03  
  
这两天没干别的，就研究怎么用 AI Agent 生成漏洞报告。  
  
核心思路很简单：你丢个漏洞编号或者扫描工具的报告给它，它能给你吐出一份像模像样的分析报告。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNjicPOvytCGiclp3QcqdvSnBybZBNw1u9Hc2Nj9FZmadtSoM0tGJQX0xAPcStyLNlQicb4hm12oAtD17gcdP7eNDOrvr0QLWfO5oY/640?wx_fmt=png&from=appmsg "")  
  
目前支持的功能：  
- 单个漏洞分析报告  
  
- 多个漏洞的总分结构报告  
  
- CVSS 3.1 自动评分  
  
- 金融、医疗、政府、制造业等行业模板  
  
- 修复建议自动生成  
  
- 各厂商SRC报告格式适配  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
这个 Skill 特别在哪？  
  
04  
  
很多少侠可能会担心：AI 会不会一本正经地胡说八道？  
  
这个我早就想到了！所以这个 Skill 不只是 AI 自己分析，还内置了大量漏洞查询资源：  
- CVE 官方数据库  
  
- 国内外漏洞库  
  
- 厂商安全公告  
  
- 修复方案库  
  
- 漏洞情报平台  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNhjC0vsjzYgfmx2kF3k17aF4RpZbHm6zk86gibicaYouWpSdhib7HbibAEwdeSBjFMSWrDoVnOofdRicml2YVF0drD3UafpKQge5mNo/640?wx_fmt=png&from=appmsg "")  
  
你只要告诉它漏洞编号，它会自动去查证这些信息，结合 AI 分析，生成更准确、更可靠的报告。这就是我说的"资源站点兜底"。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
用了效果怎么样？  
  
05  
  
说真的，比我预期的好用。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNhDktg9CQTq4GA5PpiaFxRC6n0mNuNnojv4YgjP7s8rwH7wkuELZegIiakzkpYYjOLOV24RJDyvKB2sG7UiboicxgS2JbtCl6xtWS8/640?wx_fmt=png&from=appmsg "")  
  
单个漏洞：丢个CVE编号进去，想要相关介绍，几秒钟出来一份完整的报告，CVSS评分、影响版本、修复建议都有。虽然有些地方要微调，但大体上能用了。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNhOszvmSGwI1RmWfn062icM187O0ibzAnvxoHbvdpqbr7dvc5SU5ia2UbELKbGE7OgcbfT7QGRYradQnDqceYIM7g4W6TMZtEicah4/640?wx_fmt=png&from=appmsg "")  
  
批量处理：上次测试扔了3个漏洞进去帮我生成了一份报告，包含风险评估、优先修复顺序、时间线建议。客户看完没再让我改。  
  
行业模板：金融行业模板会加上监管合规影响分析，政府行业模板会对应等级保护要求。（写报告多了的老铁都知道，就那么回事儿）  
  
SRC适配：测试了几个主流src的格式要求，也能自动生成符合厂商标准的报告。  
  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
有啥坑？  
  
06  
1. 模板适配：虽然带了多款模板，但其实真正场景下远不止如此，比如hw、客户等等都会有不同。  
  
1. 上下文限制：漏洞太多的话，可能会有遗漏。  
  
1. 保密问题：如果漏洞涉及敏感信息，建议还是自己手动写。  
  
![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg "")  
         
如何定制你的专属模板？  
  
07  
  
方法一：让 AI 帮你总结模板  
1. 找到你现有的一份漏洞报告  
  
1. 把报告内容发给 AI  
  
1. 让 AI 分析结构，总结成 Markdown 模板格式  
  
1. 把模板放到 Skill 的 templates 目录下  
  
1. 修改 SKILL.md 添加这个模板  
  
方法二：提交到 GitHub  
  
如果你有好的模板，可以提到 GitHub 的 Issue 里，我会定期整理合并。  
  
我把项目开源了：  
  
https://github.com/EastSword/dfyxskills  
lab/tree/main/安全报告编写助手  
  
有兴趣的少侠可以去看看。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNhyIBKwgicPiaNpZVrKRUmKNWRNdBpaYkbZDr7qdX3qnP0iawicdJlQSFeicsgHkrIbv1lDAaQk9NAXicXd5lm2LXh2ReuSjt3od3icxg/640?wx_fmt=png&from=appmsg "")  
  
  
后续我还会继续优化，也会探索更多 AI Agent Skill在安全工作中的应用场景。有好想法的少侠欢迎一起来交流。  
  
我相信，这不仅仅是一个技术创新思路，更是对安全业务重构的一小步。AI不是来替代我们的，而是来帮助我们的，它可以做那些重复、繁琐的工作，让我们有更多时间去思考、去创新、去解决更复杂的安全问题。  
  
就这样，溜了溜了。  
  
  
作者：千里，东方隐侠安全团队  
  
  
  
  
  
关注东方隐侠安全团队 一起打造网安江湖  
  
      
东方隐侠安全团队，一支专业的网络安全团队，将持续为您分享红蓝对抗、病毒研究、安全运营、应急响应、AI安全、区块链安全等网络安全知识，提供一流网络安全服务，敬请关注！  
  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/icqGYtiaRQqH7zgibKsqKmX3H4AatvwPeXFsrHGpp0RsxLJpzgd0cyiaPH2HDnfv4GMdxf0lkGjAibiaBtFcLmnm2ZkA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=31 "")  
  
  
  
  
公众号｜东方隐侠安全团队  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/JahlehOWN0zwKYScsRoXZueXUcrKWr3fU8EG1gz9ob0r0uX2VvSHsf48jUaAqAGpVPJ5xPL8z6oIbacx8VXpjlo2YMQiaETdfzW38RiaJ0lZ0/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NyLic1UAQsezMvBJazYSelmqIzdqHRrE2ettq5zpQbJicC9FW77KuKan2JoQDLwYd0hvU2IkKVDnwPsQIMichHX2ajuYf89ljz9Gj1Y2fZJ7Xw/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNiaUSlfYibiaSHuzavibjWUwfIUW5dLTtZLp7mMRBz8zxmibXBibKqPUHIc63hGnFcL8vQX6DiaGgSWhibam4mPQCibndGwjwtYYgWv7wYE/640?wx_fmt=png&from=appmsg "")  
  
春  
  
节  
  
快  
  
乐  
  
千里Trace私密群  
  
![](https://mmbiz.qpic.cn/mmbiz_png/JahlehOWN0zwKYScsRoXZueXUcrKWr3fU8EG1gz9ob0r0uX2VvSHsf48jUaAqAGpVPJ5xPL8z6oIbacx8VXpjlo2YMQiaETdfzW38RiaJ0lZ0/640?from=appmsg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NyLic1UAQsezMvBJazYSelmqIzdqHRrE2ettq5zpQbJicC9FW77KuKan2JoQDLwYd0hvU2IkKVDnwPsQIMichHX2ajuYf89ljz9Gj1Y2fZJ7Xw/640?from=appmsg "")  
  
  
  
  
