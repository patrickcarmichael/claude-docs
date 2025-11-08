---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task],
    verbose=True,
    process=Process.sequential,
)
result = crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a task for the agent](./657-create-a-task-for-the-agent.md)

**Next:** [Implementation Details →](./659-implementation-details.md)
