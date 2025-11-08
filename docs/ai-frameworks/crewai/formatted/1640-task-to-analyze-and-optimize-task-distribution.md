---
title: "Crewai: Task to analyze and optimize task distribution"
description: "Task to analyze and optimize task distribution section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to analyze and optimize task distribution

task_analysis = Task(
    description="""
    Search for all tasks assigned to team members in the last 30 days,
    analyze completion patterns, and create optimization recommendations
    """,
    agent=task_analyst,
    expected_output="Task analysis report with optimization recommendations"
)

crew = Crew(
    agents=[task_analyst],
    tasks=[task_analysis]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with ClickUp integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex task involving multiple ClickUp operations](./1639-complex-task-involving-multiple-clickup-operations.md)

**Next:** [GitHub Integration →](./1641-github-integration.md)
