---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(
    agents=[programmer_agent],
    tasks=[coding_task],
    verbose=True,
    process=Process.sequential,
)
result = crew.kickoff()
```

You can also enable code execution directly when creating an agent:

```python Code theme={null}
from crewai import Agent

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task to generate and execute code](./650-example-task-to-generate-and-execute-code.md)

**Next:** [Create an agent with code execution enabled →](./652-create-an-agent-with-code-execution-enabled.md)
