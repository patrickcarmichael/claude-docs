---
title: "Crewai: Task to organize documents"
description: "Task to organize documents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to organize documents

organize_task = Task(
    description="List all documents, check their properties, and identify any documents that might be duplicates or outdated for potential cleanup.",
    agent=document_organizer,
    expected_output="Analysis of document library with recommendations for organization."
)

crew = Crew(
    agents=[document_organizer],
    tasks=[organize_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent for document management](./1877-create-an-agent-for-document-management.md)

**Next:** [Troubleshooting →](./1879-troubleshooting.md)
