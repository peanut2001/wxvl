#  效率封神！Claude Opus 4.6联合Mozilla，挖出Firefox 22个全新漏洞  
看雪学苑
                    看雪学苑  看雪学苑   2026-03-09 09:59  
  
近日，人工智能公司Anthropic宣布，在与Mozilla的安全合作中，其旗下Claude Opus 4.6大语言模型成功挖出Firefox浏览器22个全新安全漏洞，展现出远超传统检测方式的效率与精准度。  
  
  
据悉，这22个漏洞的严重程度差异分明：14个被判定为高危级别，7个为中危，仅1个属于低危。这些安全隐患已在本月底发布的Firefox 148版本中得到解决，而整个漏洞挖掘过程仅耗时两周，全程在2026年1月完成。  
  
  
**20分钟定位高危漏洞，占全年修复量近五分之一**  
  
  
  
  
Anthropic方面透露，Claude Opus 4.6找到的14个高危漏洞，几乎占到了Firefox浏览器2025年全年修复高危漏洞总数的五分之一。更令人惊叹的是，该模型仅用20分钟，就在浏览器JavaScript引擎中发现了一个释放后重用漏洞，随后研究人员在虚拟化环境中验证了该漏洞，排除了误报可能。  
  
  
此次合作中，Claude Opus 4.6累计扫描了近6000个C++文件，最终提交了112份独立漏洞报告，其中就包含上述高危和中危漏洞。Anthropic表示，大部分漏洞已在Firefox 148版本中修复，剩余漏洞将在后续版本中逐步完善。  
  
  
**AI挖漏洞易，写攻击程序难且成本高**  
  
  
  
  
为测试模型的安全能力上限，Anthropic还让Claude Opus 4.6尝试利用已发现的漏洞编写可实际运行的攻击程序。尽管团队进行了数百次测试，消耗约4000美元API费用，但该模型仅成功将两个漏洞转化为攻击程序。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K12GyjSa6icShKiboBfemMdQ8UEQ8rrftTHvXjvTM8sLiatkk7FYnyb2icDo21OGWNuCYveny93rjPvhRREibEMhiciaMbqfiaTQcORjHw/640?wx_fmt=png&from=appmsg "")  
  
这一结果也揭示了两个关键结论：识别漏洞的成本远低于编写攻击程序，且Claude Opus 4.6在发现漏洞方面的能力，显著优于利用漏洞的能力。不过Anthropic也强调，即便只有两例成功案例，AI能自动生成浏览器攻击程序这一事实，仍值得警惕——且这些攻击程序仅在剥离了沙箱等安全功能的测试环境中有效。  
  
  
值得一提的是，此次漏洞挖掘过程中，一个“任务验证器”发挥了关键作用。它能实时判断攻击程序是否有效，为模型提供反馈，帮助其反复迭代，直至生成成功的攻击程序。其中，Claude针对CVE-2026-2796漏洞（CVSS评分9.8）编写的攻击程序，就属于JavaScript WebAssembly组件中的即时编译错误漏洞。  
  
  
**AI辅助成安全新工具，Mozilla同步响应**  
  
  
  
  
此次漏洞披露，距离Anthropic推出Claude Code Security有限研究预览版仅过去数周，该工具可通过AI智能体修复漏洞。Anthropic表示，目前无法保证AI生成的所有补丁都能直接合并使用，但任务验证器能大幅提升补丁的可靠性，确保其在修复漏洞的同时，不影响程序正常功能。  
  
  
作为合作方，Mozilla同步宣布，这种AI辅助检测方式还发现了另外90个漏洞，且大部分已完成修复。这些漏洞包括传统模糊测试可发现的断言失败问题，以及模糊测试无法捕捉的各类逻辑错误。  
  
  
Mozilla表示，此次大量漏洞的发现，印证了严谨工程与新型分析工具结合的强大力量，也充分说明大规模AI辅助分析，已成为安全工程师手中极具价值的新工具。  
  
  
资讯来源：Anthropic官方公告及Mozilla协同声明  
  
  
﹀  
  
﹀  
  
﹀  
  
  
![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg "")  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球分享**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球点赞**  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg "")  
  
**球在看**  
  
