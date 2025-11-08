---
title: "Crewai: Create a task for the agent"
description: "Create a task for the agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task for the agent

scrape_task = Task(
    description="""
    Extract the following information from the news website at {website_url}:
    
    1. The headlines of all featured articles (CSS selector: '.headline')
    2. The publication dates of these articles (CSS selector: '.pub-date')
    3. The author names where available (CSS selector: '.author')
    
    Compile this information into a structured format with each article's details grouped together.
    """,
    expected_output="A structured list of articles with their headlines, publication dates, and authors.",
    agent=web_scraper_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./1382-define-an-agent-that-uses-the-tool.md)

**Next:** [Run the task →](./1384-run-the-task.md)
