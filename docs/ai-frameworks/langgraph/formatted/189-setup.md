---
title: "Langgraph: Setup"
description: "Setup section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Setup


First, let's install the required packages and set our API keys

```shell
pip install --quiet -U langgraph langchain_openai numpy
```

```python
import getpass
import os

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("OPENAI_API_KEY")
```

<div class="admonition tip">
    <p class="admonition-title">Set up <a href="https://smith.langchain.com">LangSmith</a> for LangGraph development</p>
    <p style="padding-top: 5px;">
        Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started <a href="https://docs.smith.langchain.com">here</a>. 
    </p>
</div>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← How to handle large numbers of tools](./188-how-to-handle-large-numbers-of-tools.md)

**Next:** [Define the tools →](./190-define-the-tools.md)
