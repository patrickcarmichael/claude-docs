---
title: "Crewai: When using Claude as your LLM..."
description: "When using Claude as your LLM... section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# When using Claude as your LLM...

agent = Agent(
    role="Researcher",
    goal="Research topics",
    backstory="Expert researcher",
    llm=LLM(provider="anthropic", model="claude-3-sonnet")  # Using Claude
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Now all knowledge will be stored in your project directory](./166-now-all-knowledge-will-be-stored-in-your-project-d.md)

**Next:** [CrewAI will still use OpenAI embeddings by default for knowledge →](./168-crewai-will-still-use-openai-embeddings-by-default.md)
