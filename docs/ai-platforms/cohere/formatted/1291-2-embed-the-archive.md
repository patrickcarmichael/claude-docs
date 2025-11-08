---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Embed the archive

The next step is to embed the text of the questions.

<img alt="embedding archive texts" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/semantic-search-embed-text-archive.png" />

To get a thousand embeddings of this length should take about fifteen seconds.
```python PYTHON
embeds = co.embed(texts=list(df['text']),
                  model=model_name,
                  input_type=input_type_embed).embeddings
```
```python PYTHON
embeds = np.array(embeds)
embeds.shape
```
```
(1000, 4096)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
