---
title: "Crewai: Task to create a presentation"
description: "Task to create a presentation section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a presentation

create_presentation_task = Task(
    description="Create a new presentation for the quarterly business review with key slides",
    agent=slides_agent,
    expected_output="Quarterly business review presentation created with structured content"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Google Slides capabilities](./1744-create-an-agent-with-google-slides-capabilities.md)

**Next:** [Run the task →](./1746-run-the-task.md)
