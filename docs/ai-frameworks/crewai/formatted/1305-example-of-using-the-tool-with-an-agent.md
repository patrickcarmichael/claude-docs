---
title: "Crewai: Example of using the tool with an agent"
description: "Example of using the tool with an agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example of using the tool with an agent

web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific elements from websites",
    backstory="An expert in web scraping who can extract targeted content using CSS selectors.",
    tools=[scrape_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage](./1304-usage.md)

**Next:** [Create a task for the agent to extract specific elements →](./1306-create-a-task-for-the-agent-to-extract-specific-el.md)
