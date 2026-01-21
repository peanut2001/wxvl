#  全是高危漏洞？CVSS 4.0 落地指南想帮安全团队挤挤漏洞的水分  
原创 玄月调查小组
                    玄月调查小组  玄月调查小组   2026-01-21 01:40  
  
对企业安全团队来说，最头疼的不是漏洞多，而是每个漏洞看起来都是**高危**  
。  
  
长期以来，大家习惯了直接套用厂商给出的**分数**  
。厂商说这个洞是 9.8 分，大家就判定为高危漏洞，得连夜打补丁。但这种做法其实和企业环境脱节：厂商并不知道你的服务器是在公网裸奔，还是在内网的防护之后？  
  
最近，CVSS的制定者FIRST发布的《CVSS 4.0 消费者实施指南》把这个问题摆到了台面上。  
  
这份指南就想教安全团队一件事：怎么给虚高的漏洞  
挤挤水分  
，让漏洞管理回归实战。  
## 别被厂商的“高分”漏洞带节奏  
  
厂商给出的分数往往反映的是“最坏情况下的理论严重性”。但在实际攻防中，这种分数的参考价值正在缩水。  
> 只有不到 5% 的 CVE 漏洞存在  
已知利用方式  
。  
  
  
如果一个 9.8 分的漏洞根本没有利用工具，而一个 7.0 分的漏洞正被黑客大规模扫描，优先处理哪一个？  
  
如果你直接拿CVSS分数来排优先级，结果就是资源错配——把精力花在了理论上很危险、但实际上根本打不进来的漏洞上。  
## CVSS 评分的生命周期  
  
指南明确指出：作为消费者，你的任务不是被动接受分数，而是**丰富**  
它。  
  
CVSS 4.0 的核心正在于引入了 威胁（Threat） 和 环境（Environmental） 指标。通过这两个维度的修正，原本高危漏洞的 9.8 分可能会断崖式下跌。  
  
1. **生产者（Producer）：**  
 发现漏洞，发布 Base Score（最坏情况）。  
  
1. **威胁情报（Enrich Threat）：**  
 消费者引入威胁情报，确认该漏洞是否真的有利用代码或正在被攻击。  
  
1. **环境上下文（Enrich Environment）：**  
 消费者根据自身IT架构（如是否在内网、是否有WAF）调整指标。  
  
1. **优先级（Prioritize）：**  
 根据最终计算出的分数进行修复。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnLedw8gibjL3wpDQ2GuRghrJfhTEqQSz4WLmF3QlJJZRZEL1Yk8icljIONnDS24Wb9zB4ibqh1dLfvQQ/640?wx_fmt=png&from=appmsg "")  
  
  
## 你买的防火墙和 IPS 总不是摆设  
  
在 CVSS 4.0 的逻辑里，如果你的资产放在防火墙后面，或者 IPS 已经更新了规则，你就完全有理由把分降下来。比如，攻击向量（AV）可能从“网络”受限至“本地”，攻击复杂度（AC）也会因为防御手段的存在而从“低”变成“高”。  
## 如何降低漏洞评分  
  
指南中给出了硬核的“降分”实操示例：  
### 修改攻击向量 (Modified Attack Vector, MAV)  
- **场景：**  
 厂商说这个漏洞是“网络攻击（AV:N）”。  
  
- **你的环境：**  
 你的设备在防火墙后面，或者只能通过 VPN 访问。  
  
- **操作：**  
 将指标改为 **“相邻网络（Adjacent）”**  
 甚至 **“本地（Local）”**  
。  
  
- **结果：**  
 攻击难度指数级上升，评分大幅下降。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnLedw8gibjL3wpDQ2GuRghrJFyjze3TPSEa2vVIPnfET3F6fqzSSHnY974bL5tgXicklC8uQKP64Gtw/640?wx_fmt=png&from=appmsg "")  
  
  
### 修改攻击复杂度 (Modified Attack Complexity, MAC)  
- **场景：**  
 漏洞很容易利用。  
  
- **你的环境：**  
 你部署了 IPS，并且已有针对该漏洞的拦截规则。  
  
- **操作：**  
 将攻击复杂度从“低”改为 **“高”**  
。  
  
- **结果：**  
 黑客想利用漏洞，得先绕过你的 IPS。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnLedw8gibjL3wpDQ2GuRghrJwQw9bMBSngBCfhHwUibmmDzia22wicWE8YfTdGzy1IH51z4ibofmXQfycQ/640?wx_fmt=png&from=appmsg "")  
  
  
## 进阶路线：CVSS 成熟度模型  
  
不同企业投入不同，指南还提出了一个 5 级的 **CVSS 成熟度模型**  
：  
- **Level 0 (无)：**  
 不使用 CVSS。  
  
- **Level 1 (基础)：**  
 仅使用供应商的基础分数。  
  
- 现状： 大多数企业的现状。  
  
- 代价： 容易产生“报警疲劳”，被大量误报淹没。  
  
- **Level 2 (威胁感知)：**  
 引入威胁情报 (Threat Intelligence)。  
  
- 做法： 看看 CISA KEV 或 ExploitDB。如果一个漏洞没有公开的利用代码（Exploit），那就先别急着修。  
  
- 数据： 根据当前情报源（如 FIRST/EPSS、Cyentia 和 CMU SEI）的数据，实际上只有不到 **6%**  
 的 CVE 拥有有效利用代码。仅此一步，就能过滤掉 90% 的“假高危”。  
  
- **Level 3 (环境感知)：**  
 结合 CMDB 和环境指标。  
  
- 做法： 自动化地根据环境信息，例如资产位置（如内网/外网）调整分数。这是高阶玩家的标志。  
  
## 最后：拒绝无效内卷，回归理性  
  
**CVSS 评分不是静态的数字，而是一个动态的框架**  
 。在数字化转型的洪流中，漏洞数量激增。如果继续死守“见洞就补”的旧策略，安全团队迟早会被累垮。  
  
安全团队应该通过了解自身的网络防御措施（环境指标）和外部黑客动态（威胁指标），来  
重写  
漏洞的评分，帮助企业从海量的高危漏洞风险中解脱出来，专注于那些真正能被利用且后果严重的漏洞。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnJgNxsHxmSeNIn3YDnErkLfWBPz7CFxD2Zs8s58xJ6XkjE6Zln5GU9qSgic9YDwF8L7nb0cZfb07UA/640?wx_fmt=png&from=appmsg "")  
## 参考资料  
  
Common Vulnerability Scoring System version 4.0 Consumer Implementation Guide  
：https://www.first.org/cvss/v4.0/implementation-guide  
  
