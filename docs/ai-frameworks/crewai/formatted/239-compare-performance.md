---
title: "Crewai: Compare performance"
description: "Compare performance section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Compare performance

openai_time = test_embedding_performance({
    "provider": "openai",
    "config": {"model": "text-embedding-3-small"}
})

ollama_time = test_embedding_performance({
    "provider": "ollama",
    "config": {"model": "mxbai-embed-large"}
})

print(f"OpenAI: {openai_time:.2f}s")
print(f"Ollama: {ollama_time:.2f}s")
```

### Entity Memory batching behavior

Entity Memory supports batching when saving multiple entities at once. When you pass a list of `EntityMemoryItem`, the system:

* Emits a single MemorySaveStartedEvent with `entity_count`
* Saves each entity internally, collecting any partial errors
* Emits MemorySaveCompletedEvent with aggregate metadata (saved count, errors)
* Raises a partial-save exception if some entities failed (includes counts)

This improves performance and observability when writing many entities in one operation.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Check if API keys are set](./238-check-if-api-keys-are-set.md)

**Next:** [2. External Memory →](./240-2-external-memory.md)
