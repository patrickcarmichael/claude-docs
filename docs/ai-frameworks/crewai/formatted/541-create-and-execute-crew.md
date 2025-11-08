---
title: "Crewai: Create and execute crew"
description: "Create and execute crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and execute crew

research_crew = Crew(
    agents=[multi_source_agent],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True
)

result = research_crew.kickoff()
print(f"Research completed with {len(multi_source_agent.mcps)} MCP data sources")
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create comprehensive research task](./540-create-comprehensive-research-task.md)

**Next:** [Tool Naming and Organization →](./542-tool-naming-and-organization.md)
