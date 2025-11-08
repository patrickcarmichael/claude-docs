---
title: "Crewai: Establishing the crew with a hierarchical process and additional configurations"
description: "Establishing the crew with a hierarchical process and additional configurations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Establishing the crew with a hierarchical process and additional configurations

project_crew = Crew(
    tasks=[...],  # Tasks to be delegated and executed under the manager's supervision
    agents=[researcher, writer],
    manager_llm="gpt-4o",  # Specify which LLM the manager should use
    process=Process.hierarchical,  
    planning=True, 
)
```

### Using a Custom Manager Agent

Alternatively, you can create a custom manager agent with specific attributes tailored to your project's management needs. This gives you more control over the manager's behavior and capabilities.

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Agents are defined with attributes for backstory, cache, and verbose mode](./2039-agents-are-defined-with-attributes-for-backstory-c.md)

**Next:** [Define a custom manager agent →](./2041-define-a-custom-manager-agent.md)
