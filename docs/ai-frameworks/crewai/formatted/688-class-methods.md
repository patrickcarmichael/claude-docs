---
title: "Crewai: Class Methods"
description: "Class Methods section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Class Methods


The `LlamaIndexTool` provides two main class methods for creating instances:

### from\_tool

Creates a `LlamaIndexTool` from a LlamaIndex tool.

```python Code theme={null}
@classmethod
def from_tool(cls, tool: Any, **kwargs: Any) -> "LlamaIndexTool":
    # Implementation details
```

### from\_query\_engine

Creates a `LlamaIndexTool` from a LlamaIndex query engine.

```python Code theme={null}
@classmethod
def from_query_engine(
    cls,
    query_engine: Any,
    name: Optional[str] = None,
    description: Optional[str] = None,
    return_direct: bool = False,
    **kwargs: Any,
) -> "LlamaIndexTool":
    # Implementation details
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a LlamaIndexTool from the query engine](./687-create-a-llamaindextool-from-the-query-engine.md)

**Next:** [Parameters →](./689-parameters.md)
