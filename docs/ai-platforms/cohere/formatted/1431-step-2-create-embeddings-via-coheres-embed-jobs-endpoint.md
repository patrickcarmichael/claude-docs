---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Create embeddings via Cohere's Embed Jobs endpoint

```python PYTHON
job = co.create_embed_job(dataset_id=ds.id,
                          input_type='search_document',
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
```bash title="Output"
cohere.EmbedJob {
    job_id: 6d691fbe-e026-436a-826a-16e70b293e51
    status: complete
    created_at: 2024-01-13T02:47:46.385016Z
    input_dataset_id: sample-file-2gwgxq
    output_urls: None
    model: embed-english-v3.0
    truncate: RIGHT
    percent_complete: 100
    output: cohere.Dataset {
      id: embeded-sample-file-mdse2h
      name: embeded-sample-file
      dataset_type: embed-result
      validation_status: validated
      created_at: 2024-01-13 02:47:47.850097
      updated_at: 2024-01-13 02:47:47.850097
      download_urls: ['']
      validation_error: None
      validation_warnings: []
  }
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
