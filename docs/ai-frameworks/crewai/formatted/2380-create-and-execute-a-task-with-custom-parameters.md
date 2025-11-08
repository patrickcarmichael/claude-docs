---
title: "Crewai: Create and execute a task with custom parameters"
description: "Create and execute a task with custom parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and execute a task with custom parameters

research_task = Task(
    description="Conduct market research on AI tools market for 2024 in North America with detailed format",
    agent=research_agent,
    expected_output="Comprehensive market research report"
)

crew = Crew(
    agents=[research_agent],
    tasks=[research_task]
)

result = crew.kickoff()
```

### Multi-Stage Automation Workflow

```python {2, 4-35} theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import InvokeCrewAIAutomationTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with the tool](./2379-create-an-agent-with-the-tool.md)

**Next:** [Initialize different automation tools →](./2381-initialize-different-automation-tools.md)
