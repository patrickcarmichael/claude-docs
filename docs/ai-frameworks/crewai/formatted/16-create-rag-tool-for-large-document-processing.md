---
title: "Crewai: Create RAG tool for large document processing"
description: "Create RAG tool for large document processing section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create RAG tool for large document processing

rag_tool = RagTool()

rag_agent = Agent(
    role="Research Assistant",
    goal="Query large knowledge bases efficiently",
    backstory="Expert at using RAG tools for information retrieval",
    tools=[rag_tool],  # Use RAG instead of large context windows
    respect_context_window=True,
    verbose=True
)
```

#### 2. Use Knowledge Sources

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Perfect for precision tasks](./15-perfect-for-precision-tasks.md)

**Next:** [Use knowledge sources instead of large prompts →](./17-use-knowledge-sources-instead-of-large-prompts.md)
