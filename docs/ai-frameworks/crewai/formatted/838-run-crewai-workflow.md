---
title: "Crewai: Run CrewAI workflow"
description: "Run CrewAI workflow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run CrewAI workflow

crew = Crew(
    agents=[search_agent, answer_agent],
    tasks=[search_task, answer_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(
    inputs={"query": "What is the role of X in the document?"}
)
print(result)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define tasks](./837-define-tasks.md)

**Next:** [Tool Parameters →](./839-tool-parameters.md)
