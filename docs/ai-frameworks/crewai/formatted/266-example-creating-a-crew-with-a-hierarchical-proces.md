---
title: "Crewai: Example: Creating a crew with a hierarchical process"
description: "Example: Creating a crew with a hierarchical process section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example: Creating a crew with a hierarchical process

# Ensure to provide a manager_llm or manager_agent
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.hierarchical,
    manager_llm="gpt-4o"
    # or
    # manager_agent=my_manager_agent
)
```

**Note:** Ensure `my_agents` and `my_tasks` are defined prior to creating a `Crew` object, and for the hierarchical process, either `manager_llm` or `manager_agent` is also required.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example: Creating a crew with a sequential process](./265-example-creating-a-crew-with-a-sequential-process.md)

**Next:** [Sequential Process →](./267-sequential-process.md)
