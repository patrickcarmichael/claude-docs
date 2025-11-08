---
title: "Crewai: Complete Working Example"
description: "Complete Working Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Complete Working Example


Here's a complete example showing how to:

1. Extract text from a PDF
2. Generate embeddings using OpenAI
3. Store in Qdrant
4. Create a CrewAI agentic RAG workflow for semantic search

```python  theme={null}
import os
import uuid
import pdfplumber
from openai import OpenAI
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import QdrantVectorSearchTool
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The tool will automatically use OpenAI embeddings](./827-the-tool-will-automatically-use-openai-embeddings.md)

**Next:** [Load environment variables →](./829-load-environment-variables.md)
