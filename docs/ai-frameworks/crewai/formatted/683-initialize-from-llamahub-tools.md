---
title: "Crewai: Initialize from LlamaHub Tools"
description: "Initialize from LlamaHub Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize from LlamaHub Tools

wolfram_spec = WolframAlphaToolSpec(app_id="your_app_id")
wolfram_tools = wolfram_spec.to_tool_list()
tools = [LlamaIndexTool.from_tool(t) for t in wolfram_tools]
```

### From a LlamaIndex Query Engine

```python Code theme={null}
from crewai_tools import LlamaIndexTool
from llama_index.core import VectorStoreIndex
from llama_index.core.readers import SimpleDirectoryReader

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./682-define-an-agent-that-uses-the-tool.md)

**Next:** [Load documents →](./684-load-documents.md)
