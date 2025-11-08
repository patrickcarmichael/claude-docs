---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Analyze data from Snowflake database",
    backstory="An expert data analyst who can extract insights from enterprise data.",
    tools=[snowflake_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./868-initialize-the-tool.md)

**Next:** [Example task to query sales data →](./870-example-task-to-query-sales-data.md)
