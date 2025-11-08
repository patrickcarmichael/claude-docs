---
title: "Crewai: Example task to query sales data"
description: "Example task to query sales data section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to query sales data

query_task = Task(
    description="Query the sales data for the last quarter and summarize the top 5 products by revenue.",
    expected_output="A summary of the top 5 products by revenue for the last quarter.",
    agent=data_analyst_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./869-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./871-create-and-run-the-crew.md)
