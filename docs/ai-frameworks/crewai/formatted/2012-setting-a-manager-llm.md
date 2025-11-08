---
title: "Crewai: Setting a Manager LLM"
description: "Setting a Manager LLM section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setting a Manager LLM


If you're using the hierarchical process and don't want to set a custom manager agent, you can specify the language model for the manager:

```python Code theme={null}
from crewai import LLM

manager_llm = LLM(model="gpt-4o")

crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    process=Process.hierarchical,
    manager_llm=manager_llm
)
```

<Note>
  Either `manager_agent` or `manager_llm` must be set when using the hierarchical process.
</Note>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Benefits of a Custom Manager Agent](./2011-benefits-of-a-custom-manager-agent.md)

**Next:** [Customize Agents →](./2013-customize-agents.md)
