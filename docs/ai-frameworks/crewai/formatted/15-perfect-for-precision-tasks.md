---
title: "Crewai: Perfect for precision tasks"
description: "Perfect for precision tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Perfect for precision tasks

precision_agent = Agent(
    role="Code Security Auditor",
    goal="Identify security vulnerabilities in code",
    backstory="Security expert requiring complete code context",
    respect_context_window=False,  # Prefer failure over incomplete analysis
    max_retry_limit=1,  # Fail fast on context issues
    verbose=True
)
```

### Alternative Approaches for Large Data

When dealing with very large datasets, consider these strategies:

#### 1. Use RAG Tools

```python Code theme={null}
from crewai_tools import RagTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Perfect for document processing](./14-perfect-for-document-processing.md)

**Next:** [Create RAG tool for large document processing →](./16-create-rag-tool-for-large-document-processing.md)
