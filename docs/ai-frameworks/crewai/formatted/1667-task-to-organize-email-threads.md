---
title: "Crewai: Task to organize email threads"
description: "Task to organize email threads section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to organize email threads

thread_task = Task(
    description="""
    1. Fetch all threads from the last month
    2. Apply appropriate labels to organize threads by project
    3. Archive or trash threads that are no longer relevant
    """,
    agent=thread_manager,
    expected_output="Email threads organized with appropriate labels and cleanup completed"
)

crew = Crew(
    agents=[thread_manager],
    tasks=[thread_task]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Gmail integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with Gmail thread management capabilities](./1666-create-agent-with-gmail-thread-management-capabili.md)

**Next:** [Google Calendar Integration →](./1668-google-calendar-integration.md)
