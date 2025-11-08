---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[docs_agent],
    tasks=[create_doc_task]
)

crew.kickoff()
```

### Text Editing and Content Management

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new document](./1703-task-to-create-a-new-document.md)

**Next:** [Create an agent focused on text editing →](./1705-create-an-agent-focused-on-text-editing.md)
