---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## AutoGen(AG2)

*AG2 (formerly AutoGen) is an open-source framework for building and orchestrating AI agents.*

Install `autogen`
```bash
pip install autogen
export TOGETHER_API_KEY=***
```

Build a coding agent
```python
import os
from pathlib import Path
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor

config_list = [
    {
        # Let's choose the Mixtral 8x7B model

        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        # Provide your Together.AI API key here or put it into the TOGETHER_API_KEY environment variable.

        "api_key": os.environ.get("TOGETHER_API_KEY"),
        # We specify the API Type as 'together' so it uses the Together.AI client class

        "api_type": "together",
        "stream": False,
    }
]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
