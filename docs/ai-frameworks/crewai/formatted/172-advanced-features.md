---
title: "Crewai: Advanced Features"
description: "Advanced Features section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced Features


### Query Rewriting

CrewAI implements an intelligent query rewriting mechanism to optimize knowledge retrieval. When an agent needs to search through knowledge sources, the raw task prompt is automatically transformed into a more effective search query.

#### How Query Rewriting Works

1. When an agent executes a task with knowledge sources available, the `_get_knowledge_search_query` method is triggered
2. The agent's LLM is used to transform the original task prompt into an optimized search query
3. This optimized query is then used to retrieve relevant information from knowledge sources

#### Benefits of Query Rewriting

<CardGroup cols={2}>
  <Card title="Improved Retrieval Accuracy" icon="bullseye-arrow">
    By focusing on key concepts and removing irrelevant content, query rewriting helps retrieve more relevant information.
  </Card>

  <Card title="Context Awareness" icon="brain">
    The rewritten queries are designed to be more specific and context-aware for vector database retrieval.
  </Card>
</CardGroup>

#### Example

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Option 3: Agent-level embedding customization](./171-option-3-agent-level-embedding-customization.md)

**Next:** [Original task prompt →](./173-original-task-prompt.md)
