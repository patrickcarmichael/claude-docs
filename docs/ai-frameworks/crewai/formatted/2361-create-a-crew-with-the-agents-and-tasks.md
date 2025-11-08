---
title: "Crewai: Create a crew with the agents and tasks"
description: "Create a crew with the agents and tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a crew with the agents and tasks

crew = Crew(
    agents=[researcher, analyst, summarizer],
    tasks=[research_task, analysis_task, summary_task],
    process=Process.sequential,
    verbose=2
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create tasks](./2360-create-tasks.md)

**Next:** [Run the crew →](./2362-run-the-crew.md)
