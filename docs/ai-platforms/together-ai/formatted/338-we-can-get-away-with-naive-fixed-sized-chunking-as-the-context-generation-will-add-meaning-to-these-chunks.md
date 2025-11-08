---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## We can get away with naive fixed sized chunking as the context generation will add meaning to these chunks


def create_chunks(document, chunk_size=300, overlap=50):
    return [
        document[i : i + chunk_size]
        for i in range(0, len(document), chunk_size - overlap)
    ]


chunks = create_chunks(pg_essay, chunk_size=250, overlap=30)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")
```

We get the following chunked content:
```
Chunk 1: September 2024At a YC event last week Brian Chesky gave a talk that everyone who was there will remember. Most founders I talked to afterward said it was the best they'd ever heard. Ron Conway, for the first time in his life, forgot to take notes. I'
Chunk 2: life, forgot to take notes. I'm not going to try to reproduce it here. Instead I want to talk about a question it raised.The theme of Brian's talk was that the conventional wisdom about how to run larger companies is mistaken. As Airbnb grew, well-me
...
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
