---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import DatabricksQueryTool

tool = DatabricksQueryTool(
    default_catalog="main", 
    default_schema="default",
)

agent = Agent(
    role="Data Analyst",
    goal="Query Databricks",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="SELECT * FROM my_table LIMIT 10",
    expected_output="10 rows", 
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)
result = crew.kickoff()

print(result)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Environment Variables](./1074-environment-variables.md)

**Next:** [Parameters →](./1076-parameters.md)
