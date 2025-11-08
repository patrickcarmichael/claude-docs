---
title: "Crewai: Initialize LangDB before any CrewAI imports"
description: "Initialize LangDB before any CrewAI imports section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize LangDB before any CrewAI imports

init()

def create_llm(model):
    return LLM(
        model=model,
        api_key=os.environ.get("LANGDB_API_KEY"),
        base_url=os.environ.get("LANGDB_API_BASE_URL"),
        extra_headers={"x-project-id": os.environ.get("LANGDB_PROJECT_ID")}
    )

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Quick Start Example](./2172-quick-start-example.md)

**Next:** [Define your agent →](./2174-define-your-agent.md)
