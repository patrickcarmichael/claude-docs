---
title: "Crewai: Create a task for the agent to extract specific content"
description: "Create a task for the agent to extract specific content section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task for the agent to extract specific content

extract_task = Task(
    description="Extract the main heading and summary from example.com",
    expected_output="The main heading and summary from the website",
    agent=web_scraper_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example of using the tool with an agent](./1323-example-of-using-the-tool-with-an-agent.md)

**Next:** [Run the task →](./1325-run-the-task.md)
