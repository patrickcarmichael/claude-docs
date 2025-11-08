---
title: "Crewai: Example with custom scraping parameters"
description: "Example with custom scraping parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example with custom scraping parameters

web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract information from websites with custom parameters",
    backstory="An expert in web scraping who can extract content from any website.",
    tools=[scrape_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and run the crew](./1349-create-and-run-the-crew.md)

**Next:** [The agent will use the tool with parameters like: →](./1351-the-agent-will-use-the-tool-with-parameters-like.md)
