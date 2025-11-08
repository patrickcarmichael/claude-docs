---
title: "Crewai: Usage"
description: "Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Usage


To enable reasoning for an agent, simply set `reasoning=True` when creating the agent:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Data Analyst",
    goal="Analyze complex datasets and provide insights",
    backstory="You are an experienced data analyst with expertise in finding patterns in complex data.",
    reasoning=True,  # Enable reasoning
    max_reasoning_attempts=3  # Optional: Set a maximum number of reasoning attempts
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./272-overview.md)

**Next:** [How It Works →](./274-how-it-works.md)
