---
title: "Crewai: You can also see how the task description gets formatted"
description: "You can also see how the task description gets formatted section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# You can also see how the task description gets formatted

print("\n=== TASK CONTEXT ===")
print(f"Task Description: {task.description}")
print(f"Expected Output: {task.expected_output}")
```

### Overriding Default Instructions

You have several options to gain full control over the prompts:

#### Option 1: Custom Templates (Recommended)

```python  theme={null}
from crewai import Agent

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Print the complete system prompt that will be sent to the LLM](./361-print-the-complete-system-prompt-that-will-be-sent.md)

**Next:** [Define your own system template without default instructions →](./363-define-your-own-system-template-without-default-in.md)
