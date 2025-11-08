---
title: "Langgraph: Setup"
description: "Setup section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Setup


First, let's install the required packages and set our API keys

```shell
pip install -U langchain_anthropic langchain_openai langgraph
```

```python
import getpass
import os

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("ANTHROPIC_API_KEY")
_set_env("OPENAI_API_KEY")
```

!!! tip "Set up [LangSmith](https://smith.langchain.com) for LangGraph development"

    Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← How to add cross-thread persistence (functional API)](./146-how-to-add-cross-thread-persistence-functional-api.md)

**Next:** [Example: simple chatbot with long-term memory →](./148-example-simple-chatbot-with-long-term-memory.md)
