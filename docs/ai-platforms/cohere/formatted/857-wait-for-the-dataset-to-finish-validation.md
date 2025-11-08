---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## wait for the dataset to finish validation

print(co.wait(ds))
```

### Dataset Types

When a dataset is created, the `type` field *must* be specified in order to indicate the type of tasks this dataset is meant for.

The following table describes the types of datasets supported by the Dataset API:

#### Supported Dataset Types

| Dataset Type  | Description                           | Schema        | Rules                                      | Task Type | Status    | File Types Supported | Are Metadata Fields Supported? | Sample File                                                                                                                                                                                                                                                                                                 |
| ------------- | ------------------------------------- | ------------- | ------------------------------------------ | --------- | --------- | -------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `embed-input` | A file containing text to be embedded | `text:string` | None of the rows in the file can be empty. | Embed job | Supported | `csv` and `jsonl`    | Yes                            | [embed\_jobs\_sample\_data.jsonl](https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/data/embed_jobs_sample_data.jsonl) / [embed\_jobs\_sample\_data.csv](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/data/embed_jobs_sample_data.csv) |

### Downloading a dataset

Datasets can be fetched using its unique `id`. Note that the dataset `name` and `id` are different from each other; names can be duplicated, while `id`s cannot.

Here is an example code snippet showing how to fetch a dataset by its unique `id`.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
