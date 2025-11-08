---
title: "Crewai: Create a task for the agent to extract specific elements"
description: "Create a task for the agent to extract specific elements section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task for the agent to extract specific elements

extract_task = Task(
    description="""
    Extract all product titles from the featured products section on example.com.
    Use the CSS selector '.product-title' to target the title elements.
    """,
    expected_output="A list of product titles from the website",
    agent=web_scraper_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example of using the tool with an agent](./1305-example-of-using-the-tool-with-an-agent.md)

**Next:** [Run the task through a crew →](./1307-run-the-task-through-a-crew.md)
