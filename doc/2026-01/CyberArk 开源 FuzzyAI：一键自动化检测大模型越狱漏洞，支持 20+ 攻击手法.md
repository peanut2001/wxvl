#  CyberArk 开源 FuzzyAI：一键自动化检测大模型"越狱"漏洞，支持 20+ 攻击手法  
原创 0xSecDebug
                    0xSecDebug  0xSecDebug   2026-01-29 03:02  
  
# FuzzyAI Fuzzer  
  
  
>     请勿利用文章内的相关技术从事  
**非法渗透测试**  
，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除**  
。  
  
  
  
![项目标志](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsE1xl8Ir0IgnMOyQg2Mnicpd9mEGkFicV84aMA3stJu7wljXKhFBmBbE7X0yafYB6SG0kOqnR9YPY3w/640?wx_fmt=png&from=appmsg "")  
FuzzyAI 模糊器是一款强大的自动化大型语言模型模糊工具。它旨在帮助开发者和安全研究人员识别越狱漏洞，并缓解其LLM API中的潜在安全漏洞。  
## 工具使用Web UI（实验性）  
  
![FZAI](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsE1xl8Ir0IgnMOyQg2MnicpdtC4dbrMewqJSbwIRu3YJRaWw3ukaneWoKY4Ab8ibpb2RCuHXTuVEPDA/640?wx_fmt=png&from=appmsg "")  
## 攻击示例  
  
如果你用的是诗歌，确保你已经激活了venv（或者在命令行前加上了“poetry run”）  
### 默认攻击（只需评估提示“Harmful_Prompt”）用 llama 代替 Ollama。  
```
fuzzyai fuzz -m ollama/llama3.1 -a def -t "Harmful_Prompt"
```  
### 利用ManyShot和分类法攻击提示，使用gpt3.5而不是OpenAI，仅用一个工人  
```
OPENAI_API_KEY=sk-3fa1... fuzzyai fuzz -m openai/gpt-3.5-turbo -a man -a tax -t "Harmful_Prompt"
```  
### prompts.txt攻击提示使用 ArtPrompt 攻击，使用 Claude 3.5 而非拟人模式  
```
ANTHROPIC_API_KEY=deadbeef... fuzzyai fuzz -m anthropic/claude-3-5-sonnet-20240620 -a art -T src/fuzzyai/resources/adv_prompts.txt -e blacklisted_words="bomb,garbage,acid,ugly,self-harm,kill your"
```  
### 攻击你自己的REST API  
```
OPENAI_API_KEYT=sk-3fa1... fuzzyai fuzz -a def -x openai/gpt-4 -e classifier_model=openai/gpt-4 -m rest/http.raw -e host=localhost -e port=8000 -e scheme=https  -t "How to build a bomb"
```  
#### 论点分析：  
- **-a def**  
： 调用默认攻击模式，该模式评估 API，无需额外策略。  
  
- **-x openai/gpt-4**  
： 指定辅助模型（），在攻击过程中协助完成特定任务。gpt-4  
  
- **-e classifier_model=openai/gpt-4**  
： 配置fuzzer以使用模型进行输出分类。这有助于判断回答是否符合特定标准，比如检测有害或不想要的内容。gpt-4  
  
- **-m rest/http.raw**  
： 利用 REST 提供者攻击 API 端点。原始的 HTTP 请求是从文件 中解析出来的。（有关文件结构的详细信息，请参阅文档或示例。）http.raw  
  
- **-e host=localhost -e port=8000 -e scheme=https**  
： 配置 REST provider，包含以下 API 端点细节：  
  
- **主持人**  
：localhost  
  
- **移植**  
版：8000  
  
- **方案**  
：（通信将使用 HTTPS）https  
  
- **-t “如何制造炸弹”**  
： 指定测试输入。在这个例子中，它测试了API对敏感或有害内容的处理。  
  
## 主要特征  
- **全面的模糊技术**  
：利用基于突变、基于世代和智能模糊的效果。  
  
- **内置输入生成**  
：生成有效和无效输入，用于全面测试。  
  
- **无缝集成**  
：轻松融入您的开发和测试工作流程。  
  
- **可扩展架构**  
：定制和扩展fuzzer以满足您的独特需求。  
  
## 支持的模型  
  
FuzzyAI 支持多种顶级提供商的模型，包括：  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">Provider</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">Models</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">Anthropic</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Claude (3.5, 3.0, 2.1)</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">OpenAI</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">GPT-4o, GPT-4o mini, GPT o3</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">Gemini</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Gemini Pro, Gemini 1.5</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">Azure</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">GPT-4, GPT-3.5 Turbo</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">Bedrock</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">Claude (3.5, 3.0), Meta (LLaMa)</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">AI21</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">Jamba (1.5 Mini, Large)</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">DeepSeek</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">DeepSeek (DeepSeek-V3, DeepSeek-V1)</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><strong style="color: #fff;background-color: #6A00FF;font-weight: 700;padding: 2px 6px;margin: 0 2px;border: 1px solid #000;"><span leaf="">Ollama</span></strong></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">LLaMA (3.3, 3.2, 3.1), Dolphin-LLaMA3, Vicuna</span></section></td></tr></tbody></table>  
## 支持的攻击类型  
  
<table><thead><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">攻击类型</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">标题</span></section></th><th style="font-size: 16px;background-color: #f0f0f0;background: #6A00FF;color: #fff;font-weight: 900;border: 1px solid #000;padding: 12px;text-align: left;text-transform: uppercase;min-width: 85px;"><section><span leaf="">参考文献</span></section></th></tr></thead><tbody><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">艺术提示</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">基于ASCII艺术的越狱攻击针对阵线大型语言模型</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">arXiv：2402.11753</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">基于分类学的改写</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">说服性语言技巧，比如情感诉求，针对越狱大型语言模型</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">arXiv：2401.06373</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">PAIR（提示自动迭代细化）</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">通过用两个大型语言模型迭代优化提示，自动化对抗性提示的生成</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">arXiv：2310.08419</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">多次越狱</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">嵌入多个虚假对话示例以削弱模型安全性</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">人类学研究</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">ASCII走私</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">ASCII 走私利用 Unicode 标签字符在文本中嵌入隐藏指令，这些指令对用户不可见，但可被大型语言模型（LLM）处理，可能导致提示注入攻击</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">拥抱博客</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">遗传因素</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">利用遗传算法修改提示以实现对抗性结果</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">arXiv：2309.01446</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">幻觉</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">利用模型生成绕过RLHF滤波器</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">arXiv：2403.04769</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">DAN（现在就做任何事）</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">推动LLM采用无限制的人物形象，无视标准内容过滤，使其能够“立即行动”。</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">GitHub仓库</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">文字游戏</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">将有害提示伪装成文字谜题</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">arXiv：2405.14023</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">渐强</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">通过一系列逐步升级的对话转向来引导模型，从无害的提问开始，逐步引导对话到受限或敏感话题。</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">arXiv：2404.01833</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">演员攻击</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">该理论受行为者网络理论启发，构建“行为者”的语义网络，巧妙引导对话指向有害目标，同时隐藏恶意意图。</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">arxiv 2410.10700</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">最佳越狱</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">利用输入变异反复引发有害反应，利用模型敏感性</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">arXiv：2412.03556</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">洗牌不一致攻击（SI-Attack）</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">利用LLM理解能力与安全机制之间的不一致，通过洗牌有害的文本提示。这种洗牌文本绕过了安全机制，同时大语言模型仍将其理解为有害。仅完成了基于文本的实现;基于图像的部分未被实现。</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">arXiv：2501.04931</span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">回到过去</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">通过添加职业前缀和过去相关后缀来修改提示词</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf=""><br/></span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">历史/学术框架</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">将敏感技术数据框定为学术或历史研究，以实现伦理和合法的使用——可能导致越狱。</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf=""><br/></span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">请</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">通过添加“请”作为前缀和后缀来修改提示词</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf=""><br/></span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #ffffff;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">思想实验</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf="">通过添加与思想实验相关的前缀来修改提示。此外，还加上了“已采取预防措施”后缀</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;"><section><span leaf=""><br/></span></section></td></tr><tr style="border: 0;border-top: 1px solid #ccc;background-color: #F8F8F8;"><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">默认</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf="">把提示按原样发送给模型</span></section></td><td style="font-size: 16px;text-align: left;border: 1px solid #000;padding: 12px;color: #000;background: #fff;min-width: 85px;background-color: #faffd1;"><section><span leaf=""><br/></span></section></td></tr></tbody></table>  
## 支持的云API  
- **OpenAI**  
  
- **Anthropic**  
  
- **Gemini**  
  
- **Azure Cloud**  
  
- **AWS Bedrock**  
  
- **AI21**  
  
- **DeepSeek**  
  
- **Huggingface**  
  
- **Ollama**  
  
- **Custom REST API**  
  
## 📖 项目地址  
```
https://github.com/cyberark/FuzzyAI
```  
## 💻 威胁情报推送群  
>   如果师傅们想要第一时间获取到**最新的威胁情报**  
，可以添加下面我创建的  
**钉钉漏洞威胁情报群**  
，便于师傅们可以及时获取最新的  
**IOC**  
。  
>  如果师傅们想要获取  
**网络安全相关知识内容**  
，可以添加下面我创建的  
**网络安全全栈知识库**  
，便于师傅们的学习和使用：  
  
>     覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SOC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**  
。  
  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzgKUY4QqOTUNjibmmSiaNJibkPXMznRsC3eia8e4v7wcsibDepNqTft4aB2qw/640?wx_fmt=png&from=appmsg "")  
  
![img](https://mmbiz.qpic.cn/mmbiz_png/AXRefkPRWsGvpzTbNZamyJCmibbqwBWzg8cDB2ibsdhJVnLBBlicLYjMtyTmOicUQbia7oIMS0Fia7uYtDrKXzULJVgQ/640?wx_fmt=png&from=appmsg "")  
  
  
  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg "")  
  
**点分享**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg "")  
  
**点收藏**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg "")  
  
**点在看**  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg "")  
  
**点点赞**  
  
