---
title: "Crewai: Example task to extract product information from an e-commerce site"
description: "Example task to extract product information from an e-commerce site section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to extract product information from an e-commerce site

scrape_task = Task(
    description="Extract product names, prices, and descriptions from the featured products section of example.com.",
    expected_output="A structured list of product information including names, prices, and descriptions.",
    agent=web_scraper_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1317-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./1319-create-and-run-the-crew.md)
