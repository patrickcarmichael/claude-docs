---
title: "Crewai: Create custom storage with specific embedder"
description: "Create custom storage with specific embedder section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create custom storage with specific embedder

custom_storage = KnowledgeStorage(
    embedder={
        "provider": "ollama",
        "config": {"model": "mxbai-embed-large"}
    },
    collection_name="my_custom_knowledge"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← All knowledge will now be stored in ./my_project_storage/knowledge/](./162-all-knowledge-will-now-be-stored-in-my_project_sto.md)

**Next:** [Use with knowledge sources →](./164-use-with-knowledge-sources.md)
