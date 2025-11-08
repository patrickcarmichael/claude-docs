---
title: "Crewai: Create a crew with sequential processing"
description: "Create a crew with sequential processing section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a crew with sequential processing

crew = Crew(
    agents=[data_collector, data_analyst, report_generator],
    tasks=[collection_task, analysis_task, reporting_task],
    process=Process.sequential,
    verbose=2
)

result = crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create sequential tasks](./2383-create-sequential-tasks.md)

**Next:** [Use Cases →](./2385-use-cases.md)
