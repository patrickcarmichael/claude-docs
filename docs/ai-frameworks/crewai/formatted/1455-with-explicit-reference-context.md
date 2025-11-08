---
title: "Crewai: With explicit reference context"
description: "With explicit reference context section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# With explicit reference context

context_guardrail = HallucinationGuardrail(
    context="AI helps with various tasks including analysis and generation.",
    llm=LLM(model="gpt-4o-mini")
)
```

### Adding to Tasks

```python  theme={null}
from crewai import Task

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Basic usage - will use task's expected_output as context](./1454-basic-usage-will-use-tasks-expected_output-as-cont.md)

**Next:** [Create your task with the guardrail →](./1456-create-your-task-with-the-guardrail.md)
