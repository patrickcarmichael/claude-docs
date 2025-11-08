---
title: "Crewai: Create a task with more specific instructions"
description: "Create a task with more specific instructions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task with more specific instructions

advanced_scrape_task = Task(
    description="""
    Extract content from example.com with the following requirements:
    - Convert the content to plain text format
    - Enable JavaScript rendering
    - Use a US-based proxy
    - Handle any scraping failures gracefully
    """,
    expected_output="The extracted content from example.com",
    agent=web_scraper_agent,
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1362-run-the-task.md)

**Next:** [Error Handling →](./1364-error-handling.md)
