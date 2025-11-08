---
title: "Crewai: Form the crew with a sequential process"
description: "Form the crew with a sequential process section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Form the crew with a sequential process

report_crew = Crew(
  agents=[researcher, analyst, writer],
  tasks=[research_task, analysis_task, writing_task],
  process=Process.sequential
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define your tasks](./2131-define-your-tasks.md)

**Next:** [Execute the crew →](./2133-execute-the-crew.md)
