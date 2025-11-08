---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Download and prepare the embeddings

```python PYTHON
embeddings_file_path = 'embed_jobs_output.csv'
output_dataset=co.get_dataset(job.output.id)
output_dataset.save(filepath=embeddings_file_path, format="csv")
```
```python PYTHON
embeddings=[]
texts=[]
for record in output_dataset:
  embeddings.append(record['embeddings']['float'])
  texts.append(record['text'])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
