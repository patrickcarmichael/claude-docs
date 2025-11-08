---
title: "Langgraph: Tool customization"
description: "Tool customization section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Tool customization


For more control over tool behavior, use the `@tool` decorator.

### Parameter descriptions

Auto-generate descriptions from docstrings:

```python hl_lines="1 3"
from langchain_core.tools import tool

@tool("multiply_tool", parse_docstring=True)
def multiply(a: int, b: int) -> int:
    """Multiply two numbers.

    Args:
        a: First operand
        b: Second operand
    """
    return a * b
```

### Explicit input schema

Define schemas using `args_schema`:

```python hl_lines="9"
from pydantic import BaseModel, Field
from langchain_core.tools import tool

class MultiplyInputSchema(BaseModel):
    """Multiply two numbers"""
    a: int = Field(description="First operand")
    b: int = Field(description="Second operand")

@tool("multiply_tool", args_schema=MultiplyInputSchema)
def multiply(a: int, b: int) -> int:
    return a * b
```

### Tool name

Override the default tool name using the first argument or name property:

```python hl_lines="3"
from langchain_core.tools import tool

@tool("multiply_tool")
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use in a workflow](./136-use-in-a-workflow.md)

**Next:** [Context management →](./138-context-management.md)
