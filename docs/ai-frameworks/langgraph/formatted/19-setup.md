---
title: "Langgraph: Setup"
description: "Setup section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Setup


Set your your environment:

```python
import getpass
import os

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("OPENAI_API_KEY")
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./18-prerequisites.md)

**Next:** [1. Define AutoGen agent →](./20-1-define-autogen-agent.md)
