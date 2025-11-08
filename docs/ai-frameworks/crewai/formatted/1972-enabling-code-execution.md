---
title: "Crewai: Enabling Code Execution"
description: "Enabling Code Execution section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Enabling Code Execution


To enable code execution for an agent, set the `allow_code_execution` parameter to `True` when creating the agent.

Here's an example:

```python Code theme={null}
from crewai import Agent

coding_agent = Agent(
    role="Senior Python Developer",
    goal="Craft well-designed and thought-out code",
    backstory="You are a senior Python developer with extensive experience in software architecture and best practices.",
    allow_code_execution=True
)
```

<Note>
  Note that `allow_code_execution` parameter defaults to `False`.
</Note>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Introduction](./1971-introduction.md)

**Next:** [Important Considerations →](./1973-important-considerations.md)
