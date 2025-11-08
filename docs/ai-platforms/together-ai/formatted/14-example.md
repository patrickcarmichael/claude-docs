---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example

Below is a simple agent with access to web search.
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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
