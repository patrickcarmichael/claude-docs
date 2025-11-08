---
title: "Crewai: Perfect for document processing"
description: "Perfect for document processing section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Perfect for document processing

document_processor = Agent(
    role="Document Analyst",
    goal="Extract insights from large research papers",
    backstory="Expert at analyzing extensive documentation",
    respect_context_window=True,  # Handle large documents gracefully
    max_iter=50,  # Allow more iterations for complex analysis
    verbose=True
)
```

#### Use `respect_context_window=False` when:

* **Precision is critical** and information loss is unacceptable
* **Legal or medical tasks** requiring complete context
* **Code review** where missing details could introduce bugs
* **Financial analysis** where accuracy is paramount

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Agent with strict context limits](./13-agent-with-strict-context-limits.md)

**Next:** [Perfect for precision tasks →](./15-perfect-for-precision-tasks.md)
