---
title: "Crewai: ✅ Use context parameter for task dependencies"
description: "✅ Use context parameter for task dependencies section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# ✅ Use context parameter for task dependencies

writing_task = Task(
    description="Write article based on research",
    agent=writer,
    context=[research_task],  # Shares research results
    ...
)
```

### 4. **Clear Task Descriptions**

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← ✅ Disable for focused specialists (optional)](./57-disable-for-focused-specialists-optional.md)

**Next:** [✅ Specific, actionable descriptions →](./59-specific-actionable-descriptions.md)
