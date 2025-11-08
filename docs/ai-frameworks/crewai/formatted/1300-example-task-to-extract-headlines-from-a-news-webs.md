---
title: "Crewai: Example task to extract headlines from a news website"
description: "Example task to extract headlines from a news website section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to extract headlines from a news website

scrape_task = Task(
    description="Extract the main headlines from the CNN homepage. Use the CSS selector '.headline' to target the headline elements.",
    expected_output="A list of the main headlines from CNN.",
    agent=web_scraper_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1299-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./1301-create-and-run-the-crew.md)
