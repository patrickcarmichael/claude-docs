---
title: "Crewai: Get or create collection"
description: "Get or create collection section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Get or create collection

test_docs = client.collections.get("example_collections")
if not test_docs:
    test_docs = client.collections.create(
        name="example_collections",
        vectorizer_config=Configure.Vectorizer.text2vec_openai(model="nomic-embed-text"),
        generative_config=Configure.Generative.openai(model="gpt-4o"),
    )

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Connect to Weaviate](./893-connect-to-weaviate.md)

**Next:** [Load documents →](./895-load-documents.md)
