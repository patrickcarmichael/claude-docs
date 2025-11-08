---
title: "Crewai: Create CrewAI agents"
description: "Create CrewAI agents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create CrewAI agents

search_agent = Agent(
    role="Senior Semantic Search Agent",
    goal="Find and analyze documents based on semantic search",
    backstory="""You are an expert research assistant who can find relevant
    information using semantic search in a Qdrant database.""",
    tools=[qdrant_tool],
    verbose=True
)

answer_agent = Agent(
    role="Senior Answer Assistant",
    goal="Generate answers to questions based on the context provided",
    backstory="""You are an expert answer assistant who can generate
    answers to questions based on the context provided.""",
    tools=[qdrant_tool],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize Qdrant search tool](./835-initialize-qdrant-search-tool.md)

**Next:** [Define tasks →](./837-define-tasks.md)
