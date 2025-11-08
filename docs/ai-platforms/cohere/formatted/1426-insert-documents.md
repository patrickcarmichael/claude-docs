---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Insert Documents

Let's insert our example wiki dataset. You need a production Cohere account to complete this step, otherwise the documentation ingest will time out due to the API request rate limits.
```python PYTHON
url = "https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/data/embed_jobs_sample_data.jsonl"
response = requests.get(url)

jsonl_data = response.content.decode('utf-8').splitlines()

documents = []
for line in jsonl_data:
    data_dict = json.loads(line)
    documents.append({
        "_index": "cohere-wiki-embeddings",
        "_source": data_dict,
        }
      )

helpers.bulk(client, documents)

print("Done indexing documents into `cohere-wiki-embeddings` index!")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
