---
title: "Crewai: Create your task with the guardrail"
description: "Create your task with the guardrail section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create your task with the guardrail

task = Task(
    description="Write a summary about AI capabilities",
    expected_output="A factual summary based on the provided context",
    agent=my_agent,
    guardrail=guardrail  # Add the guardrail to validate output
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← With explicit reference context](./1455-with-explicit-reference-context.md)

**Next:** [Advanced Configuration →](./1457-advanced-configuration.md)
