---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SerpApiGoogleSearchTool

tool = SerpApiGoogleSearchTool()

agent = Agent(
    role="Researcher",
    goal="Answer questions using Google search",
    backstory="Search specialist",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search for the latest CrewAI releases",
    expected_output="A concise list of relevant results with titles and links",
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

**Previous:** [← Environment Variables](./1119-environment-variables.md)

**Next:** [Notes →](./1121-notes.md)
