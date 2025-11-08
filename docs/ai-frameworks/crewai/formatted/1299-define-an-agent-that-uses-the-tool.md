---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific information from websites",
    backstory="An expert in web scraping who can extract targeted content from web pages.",
    tools=[scrape_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./1298-initialize-the-tool.md)

**Next:** [Example task to extract headlines from a news website →](./1300-example-task-to-extract-headlines-from-a-news-webs.md)
