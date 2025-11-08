---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(
    agents=[extractor_agent],
    tasks=[extract_task],
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

**Previous:** [← Define a task for the agent](./1157-define-a-task-for-the-agent.md)

**Next:** [Configuration Options →](./1159-configuration-options.md)
