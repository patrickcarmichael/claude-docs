---
title: "Langgraph: Define a tool"
description: "Define a tool section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Define a tool


Define a basic tool with the [@tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) decorator:

```python hl_lines="3"
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Call tools](./132-call-tools.md)

**Next:** [Run a tool →](./134-run-a-tool.md)
