---
title: "Crewai: Example task to scrape content from a website"
description: "Example task to scrape content from a website section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to scrape content from a website

scrape_task = Task(
    description="Extract the main content from the homepage of example.com. Use the CSS selector 'main' to target the main content area.",
    expected_output="The main content from example.com's homepage.",
    agent=web_scraper_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1374-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./1376-create-and-run-the-crew.md)
