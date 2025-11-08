---
title: "Crewai: Better: Focused state"
description: "Better: Focused state section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Better: Focused state

class FocusedState(BaseModel):
    user_id: str
    preferences: Dict[str, str]
    completion_status: Dict[str, bool]
```

### 2. Use Structured State for Complex Flows

As your flows grow in complexity, structured state becomes increasingly valuable:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Too broad](./502-too-broad.md)

**Next:** [Simple flow can use unstructured state →](./504-simple-flow-can-use-unstructured-state.md)
