---
title: "Crewai: Create and run the crew"
description: "Create and run the crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and run the crew

crew = Crew(agents=[coding_agent], tasks=[generate_code_task])
result = crew.kickoff()
```

### Using PatronusPredefinedCriteriaEvalTool

The following example demonstrates how to use the `PatronusPredefinedCriteriaEvalTool`, which uses predefined evaluator and criteria:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import PatronusPredefinedCriteriaEvalTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task to generate and evaluate code](./2244-example-task-to-generate-and-evaluate-code.md)

**Next:** [Initialize the tool with predefined criteria →](./2246-initialize-the-tool-with-predefined-criteria.md)
