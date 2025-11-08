---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

browser_agent = Agent(
    role="Browser Agent",
    goal="Control web browsers using natural language",
    backstory="An expert browsing agent.",
    tools=[multion_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./2320-initialize-the-tool.md)

**Next:** [Example task to search and summarize news →](./2322-example-task-to-search-and-summarize-news.md)
