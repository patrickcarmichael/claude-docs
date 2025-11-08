---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import SingleStoreSearchTool

tool = SingleStoreSearchTool(
    tables=["products"], 
    host="host", 
    user="user", 
    password="pass", 
    database="db",
)

agent = Agent(
    role="Analyst", 
    goal="Query SingleStore", 
    tools=[tool], 
    verbose=True,
)

task = Task(
    description="List 5 products", 
    expected_output="5 rows as JSON/text", 
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

**Previous:** [← Environment Variables](./859-environment-variables.md)

**Next:** [Snowflake Search Tool →](./861-snowflake-search-tool.md)
