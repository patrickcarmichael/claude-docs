---
title: "Crewai: Complex contact management task"
description: "Complex contact management task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex contact management task

comprehensive_task = Task(
    description="""
    1. Retrieve contacts from all sources (personal, directory, other)
    2. Search for duplicate contacts and merge information
    3. Update outdated contact information
    4. Create missing contacts for important stakeholders
    5. Organize contacts into meaningful groups
    6. Generate a comprehensive contact report
    """,
    agent=contact_specialist,
    expected_output="Complete contact management performed with unified contact database and detailed report"
)

crew = Crew(
    agents=[contact_specialist],
    tasks=[comprehensive_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to organize contact groups](./1693-task-to-organize-contact-groups.md)

**Next:** [Troubleshooting →](./1695-troubleshooting.md)
