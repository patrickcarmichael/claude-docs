---
title: "Crewai: Create an agent with the knowledge store"
description: "Create an agent with the knowledge store section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with the knowledge store

agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="You are a master at understanding people and their preferences.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source], # Enable knowledge by adding the sources here
)

result = crew.kickoff(inputs={"question": "What city does John live in and how old is he?"})
```

### Web Content Knowledge Example

<Note>
  You need to install `docling` for the following example to work: `uv add docling`
</Note>

```python Code theme={null}
from crewai import LLM, Agent, Crew, Process, Task
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an LLM with a temperature of 0 to ensure deterministic outputs](./133-create-an-llm-with-a-temperature-of-0-to-ensure-de.md)

**Next:** [Create a knowledge source from web content →](./135-create-a-knowledge-source-from-web-content.md)
