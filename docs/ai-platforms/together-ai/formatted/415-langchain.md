---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Langchain

*LangChain is a framework for developing context-aware, reasoning applications powered by language models.*

To install the LangChain x Together library, run:
```text
pip install --upgrade langchain-together
```

Here's sample code to get you started with Langchain + Together AI:
```python
from langchain_together import ChatTogether

chat = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf")

for m in chat.stream("Tell me fun things to do in NYC"):
    print(m.content, end="", flush=True)
```

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-langchain?_gl=1*exkmyi*_gcl_au*MTA3NDk3OTU0MS4xNzM3OTk4MjUw*_ga*MTg5NTkzNDM0LjE3MjgzMzM2MDQ.*_ga_BS43X21GZ2*MTc0NTQ1ODY4OC44MC4xLjE3NDU0NjY2ODYuMC4wLjA.*_ga_BBHKJ5V8S0*MTc0NTQ1ODY4OC42OS4xLjE3NDU0NjY2ODYuMC4wLjA.) for the RAG implementation details using Together and LangChain.

* [LangChain TogetherEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/together)
* [LangChain Together](https://python.langchain.com/docs/integrations/llms/together)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
