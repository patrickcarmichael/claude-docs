---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract information from websites using Selenium",
    backstory="An expert web scraper who can extract content from dynamic websites.",
    tools=[selenium_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./1373-initialize-the-tool.md)

**Next:** [Example task to scrape content from a website →](./1375-example-task-to-scrape-content-from-a-website.md)
