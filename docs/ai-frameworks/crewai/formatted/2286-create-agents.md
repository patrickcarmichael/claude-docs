---
title: "Crewai: Create agents"
description: "Create agents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agents

researcher = Agent(
    role='Research Analyst',
    goal='Conduct detailed market research',
    backstory='Expert market analyst with attention to detail',
    llm=llm,
    verbose=True
)

writer = Agent(
    role='Content Writer', 
    goal='Create comprehensive reports',
    backstory='Experienced technical writer',
    llm=llm,
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Configure LLM with TrueFoundry](./2285-configure-llm-with-truefoundry.md)

**Next:** [Create tasks →](./2287-create-tasks.md)
