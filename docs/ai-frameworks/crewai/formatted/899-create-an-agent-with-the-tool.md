---
title: "Crewai: Create an agent with the tool"
description: "Create an agent with the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with the tool

rag_agent = Agent(
    name="rag_agent",
    role="You are a helpful assistant that can answer questions with the help of the WeaviateVectorSearchTool.",
    llm="gpt-4o-mini",
    tools=[weaviate_tool],
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./898-initialize-the-tool.md)

**Next:** [Conclusion →](./900-conclusion.md)
