---
title: "Crewai: Load text content from a local folder and add to MongoDB"
description: "Load text content from a local folder and add to MongoDB section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Load text content from a local folder and add to MongoDB

texts = []
for fname in os.listdir("knowledge"):
    path = os.path.join("knowledge", fname)
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            texts.append(f.read())

tool.add_texts(texts)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← More examples](./790-more-examples.md)

**Next:** [Create the Atlas Vector Search index (e.g., 3072 dims for text-embedding-3-large) →](./792-create-the-atlas-vector-search-index-eg-3072-dims-.md)
