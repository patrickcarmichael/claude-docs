---
title: "Crewai: Create and execute tasks"
description: "Create and execute tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and execute tasks

task = Task(
    description="Research the latest developments in AI",
    expected_output="A comprehensive summary",
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use with an agent](./1994-use-with-an-agent.md)

**Next:** [Required Methods →](./1996-required-methods.md)
