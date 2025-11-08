---
title: "Crewai: Create a task that instructs the agent to handle errors"
description: "Create a task that instructs the agent to handle errors section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task that instructs the agent to handle errors

error_handling_task = Task(
    description="""
    Extract content from a potentially problematic website and make sure to handle any 
    scraping failures gracefully by setting ignore_scrape_failures to True.
    """,
    expected_output="Either the extracted content or a graceful error message",
    agent=web_scraper_agent,
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Error Handling](./1364-error-handling.md)

**Next:** [Implementation Details →](./1366-implementation-details.md)
