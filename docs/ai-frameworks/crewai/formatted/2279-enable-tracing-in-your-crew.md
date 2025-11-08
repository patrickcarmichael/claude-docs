---
title: "Crewai: Enable tracing in your crew"
description: "Enable tracing in your crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Enable tracing in your crew

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    tracing=True,  # Enable built-in tracing
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create tasks for your agents](./2278-create-tasks-for-your-agents.md)

**Next:** [Execute your crew →](./2280-execute-your-crew.md)
