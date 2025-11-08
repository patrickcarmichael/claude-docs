---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Upload the merged weights to S3

```python
sess = sage.Session()
merged_weights = S3Uploader.upload(
    merged_weights_dir, s3_checkpoint_dir, sagemaker_session=sess
)
print("merged_weights", merged_weights)
```typescript
<a name="export" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
