---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(
    agents=[image_analyst],
    tasks=[task]
)

result = crew.kickoff()
```

### Advanced Usage with Context

You can provide additional context or specific questions about the image when creating tasks for multimodal agents. The task description can include specific aspects you want the agent to focus on:

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a task for image analysis](./2110-create-a-task-for-image-analysis.md)

**Next:** [Create a multimodal agent for detailed analysis →](./2112-create-a-multimodal-agent-for-detailed-analysis.md)
