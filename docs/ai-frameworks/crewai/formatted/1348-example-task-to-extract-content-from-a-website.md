---
title: "Crewai: Example task to extract content from a website"
description: "Example task to extract content from a website section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to extract content from a website

scrape_task = Task(
    description="Extract the main content from the product page at https://web-scraping.dev/products and summarize the available products.",
    expected_output="A summary of the products available on the website.",
    agent=web_scraper_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1347-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./1349-create-and-run-the-crew.md)
