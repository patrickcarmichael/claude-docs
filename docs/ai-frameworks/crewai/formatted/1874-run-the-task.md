---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[word_agent],
    tasks=[create_doc_task]
)

crew.kickoff()
```

### Reading and Managing Documents

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new text document](./1873-task-to-create-a-new-text-document.md)

**Next:** [Create an agent focused on document operations →](./1875-create-an-agent-focused-on-document-operations.md)
