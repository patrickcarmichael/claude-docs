---
title: "Crewai: When using Claude as your LLM..."
description: "When using Claude as your LLM... section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# When using Claude as your LLM...

from crewai import Agent, LLM

agent = Agent(
    role="Analyst",
    goal="Analyze data",
    backstory="Expert analyst",
    llm=LLM(provider="anthropic", model="claude-3-sonnet")  # Using Claude
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Now all storage will be in your project directory](./217-now-all-storage-will-be-in-your-project-directory.md)

**Next:** [CrewAI will use OpenAI embeddings by default for consistency →](./219-crewai-will-use-openai-embeddings-by-default-for-c.md)
