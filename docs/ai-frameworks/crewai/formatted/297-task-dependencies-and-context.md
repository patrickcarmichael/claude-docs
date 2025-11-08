---
title: "Crewai: Task Dependencies and Context"
description: "Task Dependencies and Context section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Task Dependencies and Context


Tasks can depend on the output of other tasks using the `context` attribute. For example:

```python Code theme={null}
research_task = Task(
    description="Research the latest developments in AI",
    expected_output="A list of recent AI developments",
    agent=researcher
)

analysis_task = Task(
    description="Analyze the research findings and identify key trends",
    expected_output="Analysis report of AI trends",
    agent=analyst,
    context=[research_task]  # This task will wait for research_task to complete
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task with markdown formatting enabled](./296-example-task-with-markdown-formatting-enabled.md)

**Next:** [Task Guardrails →](./298-task-guardrails.md)
