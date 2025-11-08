---
title: "Langgraph: Setup"
description: "Setup section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Setup


```python
%pip install autogen langgraph
```

```python
import getpass
import os

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("OPENAI_API_KEY")
```
```output
OPENAI_API_KEY:  ········
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks](./180-how-to-integrate-langgraph-functional-api-with-aut.md)

**Next:** [Define AutoGen agent →](./182-define-autogen-agent.md)
