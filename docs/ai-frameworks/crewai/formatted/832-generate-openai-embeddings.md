---
title: "Crewai: Generate OpenAI embeddings"
description: "Generate OpenAI embeddings section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Generate OpenAI embeddings

def get_openai_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-large"
    )
    return response.data[0].embedding

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Extract text from PDF](./831-extract-text-from-pdf.md)

**Next:** [Store text and embeddings in Qdrant →](./833-store-text-and-embeddings-in-qdrant.md)
