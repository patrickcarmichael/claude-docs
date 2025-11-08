---
title: "Crewai: Define your agent"
description: "Define your agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define your agent

researcher = Agent(
    role="Research Specialist",
    goal="Research topics thoroughly",
    backstory="Expert researcher with skills in finding information",
    llm=create_llm("openai/gpt-4o"), # Replace with the model you want to use
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize LangDB before any CrewAI imports](./2173-initialize-langdb-before-any-crewai-imports.md)

**Next:** [Create a task →](./2175-create-a-task.md)
