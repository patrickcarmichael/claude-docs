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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
