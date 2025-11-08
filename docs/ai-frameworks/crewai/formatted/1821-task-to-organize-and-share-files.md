---
title: "Crewai: Task to organize and share files"
description: "Task to organize and share files section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to organize and share files

organize_share_task = Task(
    description="Search for files containing 'presentation' in the name, create a folder called 'Presentations', move the found files to this folder, and create a view-only sharing link for the folder.",
    agent=file_organizer,
    expected_output="Files organized into 'Presentations' folder and sharing link created."
)

crew = Crew(
    agents=[file_organizer],
    tasks=[organize_share_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent for file organization and sharing](./1820-create-an-agent-for-file-organization-and-sharing.md)

**Next:** [Troubleshooting →](./1822-troubleshooting.md)
