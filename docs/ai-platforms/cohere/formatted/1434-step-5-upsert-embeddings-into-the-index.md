---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 5: Upsert embeddings into the index

```python PYTHON
batch_size = 128

for i in range(0, len(data_array), batch_size):
    i_end = min(i+batch_size, len(data_array))
    idx.upsert(vectors=to_upsert[i:i_end])

print(idx.describe_index_stats())
```
```txt title="Output"
{'dimension': 1024,
'index_fullness': 0.0,
'namespaces': {'': {'vector_count': 3664}},
'total_vector_count': 3664}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
