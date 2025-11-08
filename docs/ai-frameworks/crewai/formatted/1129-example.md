---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SerpApiGoogleShoppingTool

tool = SerpApiGoogleShoppingTool()

agent = Agent(
    role="Shopping Researcher",
    goal="Find relevant products",
    backstory="Expert in product search",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search Google Shopping for 'wireless noise-canceling headphones'",
    expected_output="Top relevant products with titles and links",
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

**Previous:** [← Environment Variables](./1128-environment-variables.md)

**Next:** [Notes →](./1130-notes.md)
