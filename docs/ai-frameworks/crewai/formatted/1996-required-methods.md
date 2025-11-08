---
title: "Crewai: Required Methods"
description: "Required Methods section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Required Methods


### Constructor: `__init__()`

**Critical**: You must call `super().__init__(model, temperature)` with the required parameters:

```python  theme={null}
def __init__(self, model: str, api_key: str, temperature: Optional[float] = None):
    # REQUIRED: Call parent constructor with model and temperature
    super().__init__(model=model, temperature=temperature)
    
    # Your custom initialization
    self.api_key = api_key
```

### Abstract Method: `call()`

The `call()` method is the heart of your LLM implementation. It must:

* Accept messages (string or list of dicts with 'role' and 'content')
* Return a string response
* Handle tools and function calling if supported
* Raise appropriate exceptions for errors

### Optional Methods

```python  theme={null}
def supports_function_calling(self) -> bool:
    """Return True if your LLM supports function calling."""
    return True  # Default is True

def supports_stop_words(self) -> bool:
    """Return True if your LLM supports stop sequences."""
    return True  # Default is True

def get_context_window_size(self) -> int:
    """Return the context window size."""
    return 4096  # Default is 4096
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and execute tasks](./1995-create-and-execute-tasks.md)

**Next:** [Common Patterns →](./1997-common-patterns.md)
