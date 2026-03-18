#  工具分享 | Java反序列化漏洞Gadget Chain可视化图谱工具  
gb233
                    gb233  篝火信安   2026-03-18 02:51  
  
![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVtEXrmUGFwJGM692bZn7Pcdarkp12kTNZGeAqhbMdayhOjJy77s3kKGVcXSRbzWaRpXpqmXJowBqyGsNGxibic3Mgic5QVbaeGBg4/640?wx_fmt=png&from=appmsg "")  
  
0x00 项目介绍  
  
Gadget_Chain是一个交互式的Java反序列化漏洞Gadget Chain可视化工具，帮助安全研究人员直观理解从Source（入口）到Gadget（跳板）再到Sink（执行点）的完整调用链。  
  
0x01 核心功能  
- 交互式图谱展示：使用Vue Flow实现节点拖拽、缩放、点击查看详情  
  
- 双链对比模式：对比两条Gadget Chain的差异，Y型布局展示共用节点和独有节点  
  
- 代码高亮对比：使用Shiki实现Java代码语法高亮，支持差异行高亮  
  
- 步进播放：自动播放展示调用链执行过程  
  
- MiniMap导航：左下角缩略图快速定位  
  
0x02 支持的Gadget Chain  
  
说明: 本工具支持的Gadget Chain列表参考自 ysoserial 项目收集的Payload清单。以下列表中的Gadget Chain名称与ysoserial项目中的Payload名称一一对应，方便安全研究人员对照使用。  
  
Commons Collections (7个)  
- CommonsCollections1  
  
- CommonsCollections2  
  
- CommonsCollections3  
  
- CommonsCollections4  
  
- CommonsCollections5  
  
- CommonsCollections6  
  
- CommonsCollections7  
  
Spring Framework (2个)  
- Spring1  
  
- Spring2  
  
Hibernate (2个)  
- Hibernate1  
  
- Hibernate2  
  
JBoss (2个)  
- JBossInterceptors1  
  
- JavassistWeld1  
  
Mozilla Rhino (2个)  
- MozillaRhino1  
  
- MozillaRhino2  
  
MyFaces (2个)  
- MyFaces1  
  
- MyFaces2  
  
其他 (17个)  
- URLDNS  
  
- AspectJWeaver  
  
- BeanShell1  
  
- C3P0  
  
- Click1  
  
- Clojure  
  
- CommonsBeanutils1  
  
- FileUpload1  
  
- Groovy1  
  
- JSON1  
  
- JRMPClient  
  
- JRMPListener  
  
- Jython1  
  
- Rome  
  
- Vaadin1  
  
- Wicket1  
  
- JDK内置 (1个)  
  
- Jdk7u21  
  
总计: 34个Gadget Chain  
  
0x03 项目结构  
```
gadget-chain-visualizer/
├── src/
│   ├── components/        # Vue组件
│   │   ├── GadgetGraph.vue       # 图谱主组件
│   │   ├── CompareView.vue       # 对比模式组件
│   │   ├── GadgetNode.vue        # 节点组件
│   │   ├── CodePanel.vue         # 代码面板
│   │   └── PayloadSelector.vue   # Payload选择器
│   ├── data/             # Gadget数据
│   │   ├── gadgets/      # 各Chain定义
│   │   └── types.ts      # 类型定义
│   ├── App.vue           # 根组件
│   └── main.ts           # 入口
├── docs/                 # 文档
├── README.md
├── LICENSE
└── .gitignore
```  
  
0x04 快速开始  
```
#安装依赖
npm install
#开发模式
npm run dev
#构建
npm run build
#预览生产构建
npm run preview
```  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVubCvwL9sDZT0a7g4nZicyrZELrGZCcR6ZSnJSH9LdyaYhFPicdGsqLwlwvypcjGT6MhjFE5SB6ryh43xF7WRdfBm3nyeKBAvE3Q/640?wx_fmt=png&from=appmsg "")  
  
构建完成后，运行预览，显示如下信息即可访问。  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/prEia0ibIXVVu6nxWVTcKWrsFjrfS5gNiaUSVFaeoux7KiaCQlqex0tWtyWnjeAIpNf8UVfv70VJuicBSGiaxGoeW4ae3MT9Z2JYTibNXz9vFnKMX4/640?wx_fmt=png&from=appmsg "")  
  
  
0x05 使用说明  
  
1、单链模式  
- 从顶部下拉框选择Payload  
  
- 点击节点查看代码详情  
  
- 使用步进播放器自动播放调用链  
  
![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVviaibibzYOMoekYuybfODzY7Pql3kEfr7v4cbsiavooGZiaibEMD0JDAzhoZRwVpHibhPWZIFPY0rFKAJBshrl6gbuKPqe0oFtOp8ro4/640?wx_fmt=png&from=appmsg "")  
  
2、对比模式  
- 点击右上角"对比模式"按钮  
  
- 选择Chain A和Chain B  
  
- 查看Y型布局展示的共用节点和独有节点  
  
- 点击节点进行代码对比  
  
![](https://mmbiz.qpic.cn/mmbiz_png/prEia0ibIXVVvOfGSibJicoGnNkx4lbYFJ61UwqQ0P8XEeVLZmXhL0hvhxb4R9tZRMaeGYvukngTOJUWwXjSrRUVN00FARia8KPky1FCfiaTafRF0/640?wx_fmt=png&from=appmsg "")  
  
## 0x06 免责声明  
  
注意: 本工具仅供安全研究和教育目的使用，请勿用于非法用途。  
  
![](https://mmbiz.qpic.cn/mmbiz_gif/CQf7uHzmVb3icxXWABkpMvXDJ1aDF6RgkCFLMvzDgLEx7jjY4A1n7yTEc2AZmg5CFFoeHJLb3AiblNHRLVFBqlfw/640?wx_fmt=gif&from=appmsg "")  
  
```
```  
  
  
  
