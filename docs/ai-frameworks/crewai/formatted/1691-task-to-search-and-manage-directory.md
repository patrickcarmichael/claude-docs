---
title: "Crewai: Task to search and manage directory"
description: "Task to search and manage directory section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to search and manage directory

directory_task = Task(
    description="Search for team members in the company directory and create a team contact list",
    agent=directory_manager,
    expected_output="Team directory compiled with contact information"
)

crew = Crew(
    agents=[directory_manager],
    tasks=[directory_task]
)

crew.kickoff()
```

### Contact Creation and Updates

```python  theme={null}
from crewai import Agent, Task, Crew

contact_curator = Agent(
    role="Contact Curator",
    goal="Create and update contact information systematically",
    backstory="An AI assistant that maintains accurate and up-to-date contact information.",
    apps=['google_contacts']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1690-run-the-task.md)

**Next:** [Task to create and update contacts →](./1692-task-to-create-and-update-contacts.md)
