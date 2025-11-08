---
title: "Crewai: Connect to CrewAI's knowledge ChromaDB"
description: "Connect to CrewAI's knowledge ChromaDB section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Connect to CrewAI's knowledge ChromaDB

knowledge_path = os.path.join(db_storage_path(), "knowledge")

if os.path.exists(knowledge_path):
    client = chromadb.PersistentClient(path=knowledge_path)
    collections = client.list_collections()
    
    print("Knowledge Collections:")
    for collection in collections:
        print(f"  - {collection.name}: {collection.count()} documents")
        
        # Sample a few documents to verify content
        if collection.count() > 0:
            sample = collection.peek(limit=2)
            print(f"    Sample content: {sample['documents'][0][:100]}...")
else:
    print("No knowledge storage found")
```

#### Check Knowledge Processing

```python  theme={null}
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Test agent knowledge retrieval](./180-test-agent-knowledge-retrieval.md)

**Next:** [Create a test knowledge source →](./182-create-a-test-knowledge-source.md)
