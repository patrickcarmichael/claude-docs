---
title: "Crewai: Use the custom manager in your crew"
description: "Use the custom manager in your crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Use the custom manager in your crew

project_crew = Crew(
    tasks=[...],
    agents=[researcher, writer],
    manager_agent=manager,  # Use your custom manager agent
    process=Process.hierarchical,
    planning=True,
)
```

<Tip>
  For more details on creating and customizing a manager agent, check out the [Custom Manager Agent documentation](https://docs.crewai.com/how-to/custom-manager-agent#custom-manager-agent).
</Tip>

### Workflow in Action

1. **Task Assignment**: The manager assigns tasks strategically, considering each agent's capabilities and available tools.
2. **Execution and Review**: Agents complete their tasks with the option for asynchronous execution and callback functions for streamlined workflows.
3. **Sequential Task Progression**: Despite being a hierarchical process, tasks follow a logical order for smooth progression, facilitated by the manager's oversight.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define a custom manager agent](./2041-define-a-custom-manager-agent.md)

**Next:** [Conclusion →](./2043-conclusion.md)
