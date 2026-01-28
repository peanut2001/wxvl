#  1700 万美元闭源智能合约攻击事件：SwapNet 与 Aperture Finance 的任意调用漏洞  
原创 BlockSec
                    BlockSec  BlockSec   2026-01-28 10:01  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SGZPtVuJmqY6QhgPUa3C3MY8W5tGJm0By5TmwrQcJDa4m8887zjGIbA/640?wx_fmt=gif&from=appmsg "")  
  
2026 年 1 月 25 日，我们监测到一系列可疑交易，攻击目标为 SwapNet 与 Aperture Finance 在 Ethereum、Arbitrum、Base 及 BSC 上部署的受害合约，累计损失超过 1700 万美元。从整体来看，这两起事件的根因并不复杂，且已在我们最初发布的安全告警中指出 [1, 2]：  
**受害合约由于输入校验不足，暴露了任意调用（arbitrary-call）能力**  
，攻击者得以滥用既有的 token 授权，通过调用 transferFrom 转移资产。  
  
然而，这两组受害合约均为**闭源合约**  
，且在反汇编后会展开为包含大量分支与复杂控制流的数千行代码，这显著增加了技术分析的难度。此外，相关项目随后发布的事后复盘报告 [3, 4] 主要聚焦于应急处置与资产恢复，对底层技术细节的讨论较为有限。因此，仍有多个关键问题尚未得到充分解答，包括漏洞调用路径是如何被构造的，以及现有检查机制为何未能阻止攻击的发生。  
  
因此，本报告基于反汇编字节码（decompiled bytecode）与链上执行轨迹，对两起事件进行了更为深入的技术分析。尽管缺乏源码限制了可见性，但字节码层面的分析已足以还原核心漏洞逻辑，并揭示出若干在高层告警中并不直观的有趣观察与设计问题。  
  
本文将首先对 SwapNet 事件进行技术分析，随后再深入分析 Aperture Finance 事件。  
  
**SwapNet 事件**  
  
**背景介绍**  
  
SwapNet 是一个 DEX 聚合器，通过整合多个链上流动性来源（包括 AMM 与私有做市商），为用户寻找最优交易路径。此外，该协议还允许用户在交易时指定自定义的 router 或 pool，从而提供更高的灵活性。  
  
**根因分析**  
  
SwapNet 事件的根因在于：  
**对用户输入参数的校验不足，使攻击者能够以任意参数触发 transferFrom() 调用**  
。  
  
由此，所有已授权给受害合约的资产（如   
0x616000e384Ef1C2B52f5f3A88D57a3B64F23757e  
）都可能被转移至攻击者地址。  
  
根据反汇编结果，函数 0x87395540() 对关键输入参数缺乏必要校验。攻击者通过将原本预期为 router 或 pool 的地址，替换为 token 地址（例如 USDC），使合约错误地将该 token 视为合法执行目标，并据此执行了一次由攻击者控制 calldata 的低级调用（low-level call）。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7Sq3buBl4tELHaOa9nkJG3nMI9dGsnglpCzcbl1FG88iad3Kibd6Hccwgg/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7S0qtFw06cv4Vzw4y0SnW5zde6ia111dRT0s4TW6RYsNeAXoAYUINq4YA/640?wx_fmt=png&from=appmsg "")  
  
最终，受害合约在自身上下文中执行了 approvedAsset.transferFrom(victim, attacker, amount)，从而使攻击者能够转走所有已授权资产。  
  
**攻击流程**  
  
SwapNet 遭受了多次攻击。以下以 Base 链上的交易  
0xc15df1d131e98d24aa0f107a67e33e66cf2ea27903338cc437a3665b6404dd57  
 为例说明攻击流程。  
  
攻击者调用了受害合约的函数 0x87395540()并传入恶意构造的参数，这一调用包含两个主要步骤:  
1. 合约中的关键内部变量（如 v51）被设置为 USDC，从而绕过了原本的路由逻辑；  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SQsu8VgRvPBLsiaTJhy3hv0ib95f9vsryLDNuhoK0vR82suesGFoMaMPg/640?wx_fmt=png&from=appmsg "")  
1. 随后执行了一次由攻击者控制 calldata 的低级调用，触发 USDC.transferFrom()，并将所有已授权的 USDC 转走。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SG1pCMy032ibCROJHR1e6vzuog4y6kibu1skW6HvpicrwmokwqQhYvyzXg/640?wx_fmt=png&from=appmsg "")  
  
**损失概览、攻击交易与受害合约**  
  
SwapNet 事件在多条链上共造成约  
**1341 万美元**  
的损失。下表汇总了关键攻击交易及其对应的受害合约地址。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SjewlGDJQYP9n4CUK1G8jicadO5rOQVicSPwanJSDDPvPiaom0HO3d0low/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SZSCZfvYP5rytlfnuico8M5uMVbpTEcul43aaGMdcW9wyUZmrGHviaQyQ/640?wx_fmt=png&from=appmsg "")  
  
**Aperture Finance 事件**  
  
**背景介绍**  
  
Aperture Finance 是一个用于管理集中流动性头寸（如 Uniswap V3 LP）的 DeFi 协议。其闭源合约（如 0xD83d960deBEC397fB149b51F8F37DD3B5CFA8913）允许用户使用原生代币铸造并管理 Uniswap V3 头寸。  
  
**Uniswap V3 头寸铸造的正常流程**  
  
当用户通过 0x67b34120() 函数铸造 Uniswap V3 头寸时，合约的预期执行流程如下：  
1. 将原生代币进行封装（wrap）  
  
1. 通过内部函数 0x1d33() 执行代币交换  
  
1. 铸造 Uniswap V3 头寸  
  
问题出现在  
**第 2 步**  
：0x1d33() 会通过一次低级调用来执行定制化的 swap 操作，其中关键参数（如调用目标地址与 calldata）在实际执行中  
**高度依赖用户输入，且缺乏严格校验**  
，从而为非预期的外部调用创造了条件。后文将对此进行更详细的分析。  
  
**根因分析**  
  
由于受害合约的源代码并不公开，以下分析均基于反编译的字节码。 Aperture Finance 事件的根本原因可能在于缺乏适当的输入验证。具体来说，当用户通过函数 0x67b34120() 铸造 Uniswap V3 头寸时，内部函数 0x1d33() 中的low-level call在没有验证用户提供的 calldata 的情况下被调用。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7ShRaibDL6fAUzkg9Ecb3K39uupEicomiah3J8Pib8OY0CxN1v565aF39wlA/640?wx_fmt=png&from=appmsg "")  
  
下图显示了用于触发low-level call的 calldata。从图中可以看出, calldata是完全基于攻击者的inputs。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SOianmM0d9iaiaqoG8fxDbhaBnau1moYJjbstAFCRle2hQ60v3zy14aU0w/640?wx_fmt=png&from=appmsg "")  
  
通过利用这一漏洞，攻击者可以在铸造 Uniswap V3 头寸时构造恶意调用，如 approvedToken.transferFrom(victim, attacker, amount)。因此，这一漏洞允许攻击者转移所有approve给合约的代币和 Uniswap V3 头寸（即 NFT）。  
  
**攻击流程**  
  
针对 Aperture Finance 的攻击有多起。在这一部分，我们将以交易（  
0x8f28a7f604f1b3890c2275eec54cd7deb40935183a856074c0a06e4b5f72f25a  
）作为例子。  
  
1. 攻击者创建了合约   
0x5c92884dFE0795db5ee095E68414d6aaBf398130  
，用于发起攻击。  
  
1. 攻击合约使用恶意输入和 100 wei ETH（即 msg.value == 100）调用了函数 0x67b34120()。  
  
1. 原生 ETH 通过函数 WETH.deposit() 转换为 WETH。  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SLQPXI0hRDJa4talzwzbJXqRjic3evwOc2icNN5dGE07xKoY8xvrgSlfw/640?wx_fmt=png&from=appmsg "")  
  
b. 内部函数 0x1d33() 被调用以执行低级调用。在这一步中，调用了 WBTC.transferFrom(victim, attacker, amount)，在受害合约的上下文中，允许攻击者 siphon 已批准的代币。  
  
值得注意的是，在函数 0x1d33() 的末尾通过了余额检查。具体来说，函数 0x1d33() 将余额变化与攻击者指定的交换输出值（即 varg2.word2）进行比较, 这里使用 >=。因此，即使没有接收任何代币，该调用仍然可以成功执行。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SwIOMXShFslCIlb8PHE1pAOPQcneq8R6DD4RDib2eicDd6yoB8Hs2nmOw/640?wx_fmt=png&from=appmsg "")  
  
c. 最后，调用了函数 NonfungiblePositionManager.mint()，为攻击者铸造了一个 100 wei WETH 的头寸。  
  
**有趣的观察**  
  
通过对**正常交易**  
与  
**异常交易**  
的对比，我们发现：  
  
两类交易均将 token 授权给了相同的 spender（如 OKX DEX: TokenApprove）；  
  
但在 swap 阶段指定的 router 地址不同（ DexRouter 与 WBTC）。  
  
这表明合约可能仅对授权的 spender 进行了校验，而未对实际执行的 router / 调用目标进行验证，从而留下了可被任意调用利用的关键缺口。  
  
正常交易:  
   
  
https://app.blocksec.com/phalcon/explorer/tx/eth/0xc823b703c716fa9078e1d71714b734557bd540ddd1e41590dd73da7c5aba0200  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SHAI9bXAbQicSj2SDYngCdBUFIdXHLznvyUECHIhPwjjhWYiahcVStkhw/640?wx_fmt=png&from=appmsg "")  
  
异常交易:   
  
https://app.blocksec.com/phalcon/explorer/tx/eth/0x8f28a7f604f1b3890c2275eec54cd7deb40935183a856074c0a06e4b5f72f25a  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SL2GQSqFy8tLk7rnM12Ly9upUAwicXPrdBXNaAPEWmg9KWjqOq91ITnw/640?wx_fmt=png&from=appmsg "")  
  
**损失概览、攻击交易与受害合约**  
  
Aperture Finance 事件在多条链上造成了约  
**367 万美元**  
的损失。下表汇总了关键攻击交易及其对应的受害合约地址。  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7S45hXpicODJK5nkwlUUJx57IgVuP5MV3kFAibiaHNupXic7STQtR6XNgeug/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTJpuJJicRg9GAxFVebDcbW7SAutRTmX8GlSSRAeNDALZannw7Ghgia5Mglqfgk9flcOWdDb2PDIkbTQ/640?wx_fmt=png&from=appmsg "")  
  
**总结**  
  
尽管 SwapNet 与 Aperture Finance 分属不同协议、部署在不同链上，但两起事件的本质问题高度一致且并不复杂：  
**在持有用户 token 授权的合约中，允许用户控制低级调用，同时缺乏严格的输入校验。**  
这类设计在提供灵活性的同时，也显著放大了风险。尤其是在闭源合约中，一旦缺乏外部审计与社区审查，类似问题更容易被忽视，最终导致严重的资产损失。  
  
**参考文献**  
  
[1]   
  
https://x.com/Phalcon_xyz/status/2015614087443697738  
  
[2]   
  
https://x.com/Phalcon_xyz/status/2015624519898234997  
  
[3]   
  
https://meta.matcha.xyz/SwapNet-Incident-Post-Mortem  
  
[4]   
  
https://x.com/ApertureFinance/status/2015938720453820752  
  
[5] https://x.com/0xswapnet  
  
[6] https://x.com/ApertureFinance  
  
加密支付合规培训研修计划  
  
在   
BlockSec 加密支付合规培训研修计划 · 第一期  
 圆满结束后，我们开启了第二期培训的报名：[BlockSec 加密支付合规培训研修计划 · 第二期正式开启报名！](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491136&idx=1&sn=26271064f94f00073f89e2ffd95c4f6e&scene=21#wechat_redirect)  
  
  
面向支付机构、交易平台与合规负责人，提供系统的合规与反洗钱培训。课程由周亚金教授与多位合规专家联合授课，内容涵盖全球监管体系、链上风险识别、合规体系搭建与实战演练。  
  
📅 时间：2026 年 3 月 14–15 日  
  
📍 地点：杭州  
  
🎯 名额：限量30席  
  
扫描下方二维码了解详情并报名。  
  
![图片](https://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTK352WTicLZWzF1Md0zFZqr6ic4JJGDCMkcdA3By4rOaibYEGfn8icFE3qFWIicMLRsG3icaWeh5pzg2Q9A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "")  
  
  
  
  
  
     
   
关于Bloc  
kSec  
  
BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立。BlockSec 致力于提升 Web3 世界的安全性和易用性，提供一站式安全服务，包括智能合约/链/钱包安全审计服务、协议安全和数字货币合规(AML/CFT)平台 Phalcon Security / Phalcon Compliance / Phalcon Network、资金追踪调查平台 MetaSleuth 和区块链交易分析工具 Phalcon Explorer 等。  
  
目前，BlockSec 已服务全球逾 500 家客户，既涵盖 Web3 知名公司 Coinbase、Cobo、Uniswap、Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、Merlin、PancakeSwap 等，也包括了权威监管机构及咨询机构，如联合国、SFC、PwC、FTI Consulting 等。  
  
官网：https://blocksec.com/  
  
Twitter：https://twitter.com/BlockSecTeam  
  
推荐阅读  
👇  
  
[](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491136&idx=1&sn=26271064f94f00073f89e2ffd95c4f6e&scene=21#wechat_redirect)  
  
[](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491200&idx=1&sn=f0a133511ca63c3deb086c51654e4157&scene=21#wechat_redirect)  
  
[#BlockSec]()  
   
  
