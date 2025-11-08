---
title: "Crewai: Define your tasks"
description: "Define your tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define your tasks

research_task = Task(
  description='Gather relevant data...', 
  agent=researcher, 
  expected_output='Raw Data'
)
analysis_task = Task(
  description='Analyze the data...', 
  agent=analyst, 
  expected_output='Data Insights'
)
writing_task = Task(
  description='Compose the report...', 
  agent=writer, 
  expected_output='Final Report'
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define your agents](./2130-define-your-agents.md)

**Next:** [Form the crew with a sequential process →](./2132-form-the-crew-with-a-sequential-process.md)
