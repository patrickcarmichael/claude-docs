---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import BrightDataSearchTool

tool = BrightDataSearchTool(
    query="CrewAI", 
    country="us",
)

agent = Agent(
    role="Web Researcher",
    goal="Search with Bright Data",
    backstory="Finds reliable results",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search for CrewAI and summarize top results",
    expected_output="Short summary with links",
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Troubleshooting](./1237-troubleshooting.md)

**Next:** [Browserbase Web Loader →](./1239-browserbase-web-loader.md)
