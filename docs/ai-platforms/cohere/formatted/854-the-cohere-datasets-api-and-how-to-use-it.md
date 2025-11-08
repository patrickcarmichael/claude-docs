---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The Cohere Datasets API (and How to Use It)

> Learn about the Dataset API, including its file size limits, data retention, creation, validation, metadata, and more, with provided code snippets.

The Cohere platform allows you to upload and manage datasets that can be used in  batch embedding with [Embedding Jobs](/docs/embed-jobs-api). Datasets can be managed [in the Dashboard](https://dashboard.cohere.com/datasets) or programmatically using the [Datasets API](/reference/create-dataset).

![](file:20ae1ef7-8eff-47f3-beb4-a26d09d8f8ee)

<br />

### File Size Limits

There are certain limits to the files you can upload, specifically:

* A Dataset can be as large as 1.5GB
* Organizations have up to 10GB of storage across all their users

### Retention

You should also be aware of how Cohere handles data retention. This is the most important context:

* Datasets get deleted 30 days after creation
* You can also manually delete a dataset in the Dashboard UI or [using the Datasets API](/reference/delete-dataset)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
