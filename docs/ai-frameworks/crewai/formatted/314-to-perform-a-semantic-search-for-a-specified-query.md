---
title: "Crewai: to perform a semantic search for a specified query from a text's content across the internet"
description: "to perform a semantic search for a specified query from a text's content across the internet section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# to perform a semantic search for a specified query from a text's content across the internet

search_tool = SerperDevTool()

task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
print(result)
```

This demonstrates how tasks with specific tools can override an agent's default set for tailored task execution.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Creating a Task with Tools](./313-creating-a-task-with-tools.md)

**Next:** [Referring to Other Tasks →](./315-referring-to-other-tasks.md)
