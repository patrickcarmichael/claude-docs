---
title: "Langgraph: Custom tools"
description: "Custom tools section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Custom tools


You can define custom tools using the `@tool` decorator or plain Python functions. For example:

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

See the [tool calling guide](../how-tos/tool-calling.md) for more details.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prebuilt tools](./274-prebuilt-tools.md)

**Next:** [Tool execution →](./276-tool-execution.md)
