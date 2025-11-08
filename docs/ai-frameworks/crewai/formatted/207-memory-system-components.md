---
title: "Crewai: Memory System Components"
description: "Memory System Components section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Memory System Components


| Component             | Description                                                                                                                                                                                                                       |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Short-Term Memory** | Temporarily stores recent interactions and outcomes using `RAG`, enabling agents to recall and utilize information relevant to their current context during the current executions.                                               |
| **Long-Term Memory**  | Preserves valuable insights and learnings from past executions, allowing agents to build and refine their knowledge over time.                                                                                                    |
| **Entity Memory**     | Captures and organizes information about entities (people, places, concepts) encountered during tasks, facilitating deeper understanding and relationship mapping. Uses `RAG` for storing entity information.                     |
| **Contextual Memory** | Maintains the context of interactions by combining `ShortTermMemory`, `LongTermMemory`, `ExternalMemory` and `EntityMemory`, aiding in the coherence and relevance of agent responses over a sequence of tasks or a conversation. |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overview](./206-overview.md)

**Next:** [1. Basic Memory System (Recommended) →](./208-1-basic-memory-system-recommended.md)
