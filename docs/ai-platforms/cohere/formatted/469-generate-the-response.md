---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the response

response = query_engine.query("What is Cohere's Embed model?")
print(response)
```

### Cohere Tool Use (Function Calling) with LlamaIndex

To use Cohere's tool use functionality with LlamaIndex, you can use the `FunctionTool` class to create a tool that uses Cohere's API.
```python PYTHON
from llama_index.llms.cohere import Cohere
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgent


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
