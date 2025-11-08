---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 1: Upload a dataset

```python PYTHON
dataset_file_path = "data/embed_jobs_sample_data.jsonl" # Full path - https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/data/embed_jobs_sample_data.jsonl

ds=co.create_dataset(
	name='sample_file',
	# insert your file path here - you can upload it on the right - we accept .csv and jsonl files

	data=open(dataset_file_path, 'rb'),
	dataset_type="embed-input"
	)

print(ds.await_validation())
```
```txt title="Output"
uploading file, starting validation...
sample-file-2gwgxq was uploaded
...


cohere.Dataset {
    id: sample-file-2gwgxq
    name: sample_file
    dataset_type: embed-input
    validation_status: validated
    created_at: 2024-01-13 02:47:32.563080
    updated_at: 2024-01-13 02:47:32.563081
    download_urls: ['']
    validation_error: None
    validation_warnings: []
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
