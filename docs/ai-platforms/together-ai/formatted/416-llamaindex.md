---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## LlamaIndex

*LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models (LLMs).*

Install `llama-index`
```bash
pip install llama-index
```

Here's sample code to get you started with Llama Index + Together AI:
```python
from llama_index.llms import OpenAILike

llm = OpenAILike(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    api_base="https://api.together.xyz/v1",
    api_key="TOGETHER_API_KEY",
    is_chat_model=True,
    is_function_calling_model=True,
    temperature=0.1,
)

response = llm.complete(
    "Write up to 500 words essay explaining Large Language Models"
)

print(response)
```

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-llamaindex?_gl=1*1t16mh2*_gcl_au*MTA3NDk3OTU0MS4xNzM3OTk4MjUw*_ga*MTg5NTkzNDM0LjE3MjgzMzM2MDQ.*_ga_BS43X21GZ2*MTc0NTQ1ODY4OC44MC4xLjE3NDU0NjY2ODYuMC4wLjA.*_ga_BBHKJ5V8S0*MTc0NTQ1ODY4OC42OS4xLjE3NDU0NjY2ODYuMC4wLjA.) for the RAG implementation details using Together and LlamaIndex.

* [LlamaIndex TogetherEmbeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/together.html)
* [LlamaIndex TogetherLLM](https://docs.llamaindex.ai/en/stable/examples/llm/together.html)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
