---
title: "Crewai: Creating a Task with Tools"
description: "Creating a Task with Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Creating a Task with Tools


```python Code theme={null}
import os
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

research_agent = Agent(
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="""You're a researcher at a large company.
  You're responsible for analyzing data and providing insights
  to the business.""",
  verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Integrating Tools with Tasks](./312-integrating-tools-with-tasks.md)

**Next:** [to perform a semantic search for a specified query from a text's content across the internet →](./314-to-perform-a-semantic-search-for-a-specified-query.md)
