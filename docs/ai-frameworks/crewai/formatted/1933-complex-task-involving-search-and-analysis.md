---
title: "Crewai: Complex task involving search and analysis"
description: "Complex task involving search and analysis section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving search and analysis

analysis_task = Task(
    description="""
    1. Search for recent project-related messages across all channels
    2. Find users by email to identify team members
    3. Analyze communication patterns and response times
    4. Generate weekly team communication summary
    """,
    agent=analytics_agent,
    expected_output="Comprehensive communication analysis with team insights and recommendations"
)

crew = Crew(
    agents=[analytics_agent],
    tasks=[analysis_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with Slack search and user management capabilities](./1932-create-agent-with-slack-search-and-user-management.md)

**Next:** [Contact Support →](./1934-contact-support.md)
