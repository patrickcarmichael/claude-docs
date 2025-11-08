---
title: "Crewai: Create an agent that uses the tool"
description: "Create an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent that uses the tool

agent = Agent(
    role="Research Assistant",
    goal="Find relevant information in documents",
    tools=[qdrant_tool]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with QdrantConfig](./825-initialize-the-tool-with-qdrantconfig.md)

**Next:** [The tool will automatically use OpenAI embeddings →](./827-the-tool-will-automatically-use-openai-embeddings.md)
