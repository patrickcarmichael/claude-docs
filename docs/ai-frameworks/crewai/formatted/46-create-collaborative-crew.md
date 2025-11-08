---
title: "Crewai: Create collaborative crew"
description: "Create collaborative crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create collaborative crew

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[article_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a task that encourages collaboration](./45-create-a-task-that-encourages-collaboration.md)

**Next:** [Collaboration Patterns →](./47-collaboration-patterns.md)
