---
title: "Crewai: Asynchronous Tool Support"
description: "Asynchronous Tool Support section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Asynchronous Tool Support


CrewAI supports asynchronous tools, allowing you to implement tools that perform non-blocking operations like network requests, file I/O, or other async operations without blocking the main execution thread.

### Creating Async Tools

You can create async tools in two ways:

#### 1. Using the `tool` Decorator with Async Functions

```python Code theme={null}
from crewai.tools import tool

@tool("fetch_data_async")
async def fetch_data_async(query: str) -> str:
    """Asynchronously fetch data based on the query."""
    # Simulate async operation
    await asyncio.sleep(1)
    return f"Data retrieved for {query}"
```

#### 2. Implementing Async Methods in Custom Tool Classes

```python Code theme={null}
from crewai.tools import BaseTool

class AsyncCustomTool(BaseTool):
    name: str = "async_custom_tool"
    description: str = "An asynchronous custom tool"

    async def _run(self, query: str = "") -> str:
        """Asynchronously run the tool"""
        # Your async implementation here
        await asyncio.sleep(1)
        return f"Processed {query} asynchronously"
```

### Using Async Tools

Async tools work seamlessly in both standard Crew workflows and Flow-based workflows:

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Creating your own Tools](./344-creating-your-own-tools.md)

**Next:** [In standard Crew →](./346-in-standard-crew.md)
