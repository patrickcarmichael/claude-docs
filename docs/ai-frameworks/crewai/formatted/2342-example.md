---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.adapters.zapier_adapter import ZapierActionsAdapter

adapter = ZapierActionsAdapter(api_key="your_zapier_api_key")
tools = adapter.tools()

agent = Agent(
    role="Automator",
    goal="Execute Zapier actions",
    backstory="Automation specialist",
    tools=tools,
    verbose=True,
)

task = Task(
    description="Create a new Google Sheet and add a row using Zapier actions",
    expected_output="Confirmation with created resource IDs",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Environment Variables](./2341-environment-variables.md)

**Next:** [Notes & limits →](./2343-notes-limits.md)
