---
title: "Crewai: Example of using the tool with an agent"
description: "Example of using the tool with an agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example of using the tool with an agent

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze sales data from Snowflake",
    backstory="An expert data analyst with experience in SQL and data visualization.",
    tools=[snowflake_tool],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage](./874-usage.md)

**Next:** [The agent will use the tool with parameters like: →](./876-the-agent-will-use-the-tool-with-parameters-like.md)
