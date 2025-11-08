---
title: "Crewai: Advanced Usage"
description: "Advanced Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Advanced Usage


### Custom Retrieval Configuration

```python  theme={null}
kb_tool = BedrockKBRetrieverTool(
    knowledge_base_id="your-kb-id",
    retrieval_configuration={
        "vectorSearchConfiguration": {
            "numberOfResults": 10,
            "overrideSearchType": "HYBRID"
        }
    }
)

policy_expert = Agent(
    role='Policy Expert',
    goal='Analyze company policies in detail',
    backstory='I am an expert in corporate policy analysis with deep knowledge of regulatory requirements.',
    tools=[kb_tool]
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Response Format](./735-response-format.md)

**Next:** [Supported Data Sources →](./737-supported-data-sources.md)
