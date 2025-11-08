---
title: "Crewai: Second run - state is automatically loaded"
description: "Second run - state is automatically loaded section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Second run - state is automatically loaded

flow2 = PersistentCounterFlow()
result2 = flow2.kickoff()
print(f"Second run result: {result2}")  # Will be higher due to persisted state
```

#### Method-Level Persistence

For more granular control, you can apply `@persist()` to specific methods:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from crewai.flow.persistence import persist

class SelectivePersistFlow(Flow):
    @start()
    def first_step(self):
        self.state["count"] = 1
        return "First step"

    @persist()  # Only persist after this method
    @listen(first_step)
    def important_step(self, prev_result):
        self.state["count"] += 1
        self.state["important_data"] = "This will be persisted"
        return "Important step completed"

    @listen(important_step)
    def final_step(self, prev_result):
        self.state["count"] += 1
        return f"Complete with count {self.state['count']}"
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← First run](./497-first-run.md)

**Next:** [Advanced State Patterns →](./499-advanced-state-patterns.md)
