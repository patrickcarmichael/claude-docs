---
title: "Crewai: Memory and Learning"
description: "Memory and Learning section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Memory and Learning


Enable agents to remember past collaborations:

```python  theme={null}
agent = Agent(
    role="Content Lead",
    memory=True,  # Remembers past interactions
    allow_delegation=True,
    verbose=True
)
```

With memory enabled, agents learn from previous collaborations and improve their delegation decisions over time.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set specific collaboration guidelines in agent backstory](./66-set-specific-collaboration-guidelines-in-agent-bac.md)

**Next:** [Next Steps →](./68-next-steps.md)
