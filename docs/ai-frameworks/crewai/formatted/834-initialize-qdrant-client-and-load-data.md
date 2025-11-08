---
title: "Crewai: Initialize Qdrant client and load data"
description: "Initialize Qdrant client and load data section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize Qdrant client and load data

qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)
collection_name = "example_collection"
pdf_path = "path/to/your/document.pdf"
load_pdf_to_qdrant(pdf_path, qdrant, collection_name)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Store text and embeddings in Qdrant](./833-store-text-and-embeddings-in-qdrant.md)

**Next:** [Initialize Qdrant search tool →](./835-initialize-qdrant-search-tool.md)
