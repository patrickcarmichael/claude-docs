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

### Using PatronusLocalEvaluatorTool

The following example demonstrates how to use the `PatronusLocalEvaluatorTool`, which uses custom function evaluators:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import PatronusLocalEvaluatorTool
from patronus import Client, EvaluationResult
import random

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example task to generate code](./2248-example-task-to-generate-code.md)

**Next:** [Initialize the Patronus client →](./2250-initialize-the-patronus-client.md)
