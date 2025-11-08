---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Prepare embeddings for upsert

```python PYTHON
output_dataset=co.get_dataset(job.output.id)
data_array = []
for record in output_dataset:
  data_array.append(record)

ids = [str(i) for i in range(len(data_array))]
meta = [{'text':str(data_array[i]['text'])} for i in range(len(data_array))]
embeds=[np.float32(data_array[i]['embeddings']['float']) for i in range(len(data_array))]

to_upsert = list(zip(ids, embeds, meta))
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
