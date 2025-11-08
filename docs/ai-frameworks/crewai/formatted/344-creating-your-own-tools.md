---
title: "Crewai: Creating your own Tools"
description: "Creating your own Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Creating your own Tools


<Tip>
  Developers can craft `custom tools` tailored for their agent's needs or
  utilize pre-built options.
</Tip>

There are two main ways for one to create a CrewAI tool:

### Subclassing `BaseTool`

```python Code theme={null}
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class MyToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = "What this tool does. It's vital for effective utilization."
    args_schema: Type[BaseModel] = MyToolInput

    def _run(self, argument: str) -> str:
        # Your tool's logic here
        return "Tool's result"
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Available CrewAI Tools](./343-available-crewai-tools.md)

**Next:** [Asynchronous Tool Support →](./345-asynchronous-tool-support.md)
