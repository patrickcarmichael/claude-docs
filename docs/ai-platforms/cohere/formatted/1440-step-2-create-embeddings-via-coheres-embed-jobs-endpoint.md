---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Create embeddings via Cohere's Embed Jobs endpoint

```python PYTHON
job = co.create_embed_job(
    dataset_id=ds.id,
    input_type='search_document' ,
    model='embed-english-v3.0',
    embeddings_types=['float'])

job.wait() # poll the server until the job is completed

```
```txt title="Output"
...
...
```
```python PYTHON
print(job)
```
```txt title="Output"
cohere.EmbedJob {
    job_id: 792bbc1a-561b-48c2-8a97-0c80c1914ea8
    status: complete
    created_at: 2024-01-13T02:53:31.879719Z
    input_dataset_id: sample-file-hca4x0
    output_urls: None
    model: embed-english-v3.0
    truncate: RIGHT
    percent_complete: 100
    output: cohere.Dataset {
    id: embeded-sample-file-drtjf9
    name: embeded-sample-file
    dataset_type: embed-result
    validation_status: validated
    created_at: 2024-01-13 02:53:33.569362
    updated_at: 2024-01-13 02:53:33.569362
    download_urls: ['']
    validation_error: None
    validation_warnings: []
}
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
