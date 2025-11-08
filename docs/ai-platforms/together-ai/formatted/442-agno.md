---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Agno

*Agno is an open-source library for creating multimodal agents.*

Install `agno`
```bash
pip install -U agno duckduckgo-search
```

Build a search and answer agent
```python
from agno.agent import Agent
from agno.models.together import Together
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)
agent.print_response("What's happening in New York?", stream=True)
```

Learn more in our [Agno Guide](https://docs.together.ai/docs/agno) including code a notebook.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
