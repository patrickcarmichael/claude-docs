---
title: "Langgraph: Setup"
description: "Setup section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Setup


First, let's install the required packages and set our API keys

```shell
pip install -U langgraph langchain-openai langmem
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

**Previous:** [← How to manage conversation history in a ReAct Agent](./173-how-to-manage-conversation-history-in-a-react-agen.md)

**Next:** [Keep the original message history unmodified →](./175-keep-the-original-message-history-unmodified.md)
