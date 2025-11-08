---
title: "Crewai: Test agent knowledge retrieval"
description: "Test agent knowledge retrieval section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Test agent knowledge retrieval

if hasattr(agent, 'knowledge') and agent.knowledge:
    test_query = ["test query"]
    results = agent.knowledge.query(test_query)
    print(f"Agent knowledge results: {len(results)} documents found")
    
    # Test crew knowledge retrieval (if exists)
    if hasattr(crew, 'knowledge') and crew.knowledge:
        crew_results = crew.query_knowledge(test_query)
        print(f"Crew knowledge results: {len(crew_results)} documents found")
```

#### Inspect Knowledge Collections

```python  theme={null}
import chromadb
from crewai.utilities.paths import db_storage_path
import os

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Check storage structure](./179-check-storage-structure.md)

**Next:** [Connect to CrewAI's knowledge ChromaDB →](./181-connect-to-crewais-knowledge-chromadb.md)
