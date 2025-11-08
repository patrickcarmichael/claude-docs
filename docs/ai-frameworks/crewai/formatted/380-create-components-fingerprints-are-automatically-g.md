---
title: "Crewai: Create components - fingerprints are automatically generated"
description: "Create components - fingerprints are automatically generated section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create components - fingerprints are automatically generated

agent = Agent(
    role="Data Scientist",
    goal="Analyze data",
    backstory="Expert in data analysis"
)

crew = Crew(
    agents=[agent],
    tasks=[]
)

task = Task(
    description="Analyze customer data",
    expected_output="Insights from data analysis",
    agent=agent
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Basic Usage](./379-basic-usage.md)

**Next:** [Access the fingerprints →](./381-access-the-fingerprints.md)
