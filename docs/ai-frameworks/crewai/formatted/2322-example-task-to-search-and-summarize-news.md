---
title: "Crewai: Example task to search and summarize news"
description: "Example task to search and summarize news section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to search and summarize news

browse_task = Task(
    description="Summarize the top 3 trending AI News headlines",
    expected_output="A summary of the top 3 trending AI News headlines",
    agent=browser_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./2321-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./2323-create-and-run-the-crew.md)
