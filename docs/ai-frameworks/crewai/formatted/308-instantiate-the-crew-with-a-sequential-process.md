---
title: "Crewai: Instantiate the crew with a sequential process"
description: "Instantiate the crew with a sequential process section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Instantiate the crew with a sequential process

crew = Crew(
    agents=[blog_agent],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the task with output_json set to the Blog model](./307-define-the-task-with-output_json-set-to-the-blog-m.md)

**Next:** [Kickoff the crew to execute the task →](./309-kickoff-the-crew-to-execute-the-task.md)
