---
title: "Crewai: More examples"
description: "More examples section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## More examples


### Basic initialization

```python Code theme={null}
from crewai_tools import MongoDBVectorSearchTool

tool = MongoDBVectorSearchTool(
    database_name="example_database",
    collection_name="example_collection",
    connection_string="<your_mongodb_connection_string>",
)
```

### Custom query configuration

```python Code theme={null}
from crewai_tools import MongoDBVectorSearchConfig, MongoDBVectorSearchTool

query_config = MongoDBVectorSearchConfig(limit=10, oversampling_factor=2)
tool = MongoDBVectorSearchTool(
    database_name="example_database",
    collection_name="example_collection",
    connection_string="<your_mongodb_connection_string>",
    query_config=query_config,
    vector_index_name="my_vector_index",
)

rag_agent = Agent(
    name="rag_agent",
    role="You are a helpful assistant that can answer questions with the help of the MongoDBVectorSearchTool.",
    goal="...",
    backstory="...",
    tools=[tool],
)
```

### Preloading the database and creating the index

```python Code theme={null}
import os
from crewai_tools import MongoDBVectorSearchTool

tool = MongoDBVectorSearchTool(
    database_name="example_database",
    collection_name="example_collection",
    connection_string="<your_mongodb_connection_string>",
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Common issues](./789-common-issues.md)

**Next:** [Load text content from a local folder and add to MongoDB →](./791-load-text-content-from-a-local-folder-and-add-to-m.md)
