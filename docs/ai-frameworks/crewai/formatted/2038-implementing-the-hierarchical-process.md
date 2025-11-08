---
title: "Crewai: Implementing the Hierarchical Process"
description: "Implementing the Hierarchical Process section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementing the Hierarchical Process


To utilize the hierarchical process, it's essential to explicitly set the process attribute to `Process.hierarchical`, as the default behavior is `Process.sequential`.
Define a crew with a designated manager and establish a clear chain of command.

<Tip>
  Assign tools at the agent level to facilitate task delegation and execution by the designated agents under the manager's guidance.
  Tools can also be specified at the task level for precise control over tool availability during task execution.
</Tip>

<Tip>
  Configuring the `manager_llm` parameter is crucial for the hierarchical process.
  The system requires a manager LLM to be set up for proper function, ensuring tailored decision-making.
</Tip>

```python Code theme={null}
from crewai import Crew, Process, Agent

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Hierarchical Process Overview](./2037-hierarchical-process-overview.md)

**Next:** [Agents are defined with attributes for backstory, cache, and verbose mode →](./2039-agents-are-defined-with-attributes-for-backstory-c.md)
