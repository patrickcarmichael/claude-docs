---
title: "Crewai: Form the crew and kick it off"
description: "Form the crew and kick it off section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Form the crew and kick it off

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=2
)

result = crew.kickoff()
print(result)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a task for the agent](./1174-create-a-task-for-the-agent.md)

**Next:** [Configuration Options →](./1176-configuration-options.md)
