---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import MongoDBVectorSearchTool

tool = MongoDBVectorSearchTool(
    connection_string="mongodb+srv://...",
    database_name="mydb",
    collection_name="docs",
)

agent = Agent(
    role="RAG Agent",
    goal="Answer using MongoDB vector search",
    backstory="Knowledge retrieval specialist",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Find relevant content for 'indexing guidance'",
    expected_output="A concise answer citing the most relevant matches",
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create the Atlas Vector Search index (e.g., 3072 dims for text-embedding-3-large)](./792-create-the-atlas-vector-search-index-eg-3072-dims-.md)

**Next:** [MySQL RAG Search →](./794-mysql-rag-search.md)
