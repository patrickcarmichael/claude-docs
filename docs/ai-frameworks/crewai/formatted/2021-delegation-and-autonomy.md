---
title: "Crewai: Delegation and Autonomy"
description: "Delegation and Autonomy section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Delegation and Autonomy


Controlling an agent's ability to delegate tasks or ask questions is vital for tailoring its autonomy and collaborative dynamics within the CrewAI framework. By default,
the `allow_delegation` attribute is now set to `False`, disabling agents to seek assistance or delegate tasks as needed. This default behavior can be changed to promote collaborative problem-solving and
efficiency within the CrewAI ecosystem. If needed, delegation can be enabled to suit specific operational requirements.

### Example: Disabling Delegation for an Agent

```python Code theme={null}
agent = Agent(
  role='Content Writer',
  goal='Write engaging content on market trends',
  backstory='A seasoned writer with expertise in market analysis.',
  allow_delegation=True # Enabling delegation
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the agent with advanced options](./2020-initialize-the-agent-with-advanced-options.md)

**Next:** [Conclusion →](./2022-conclusion.md)
