---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 6: Deploy for inference (once completed)

if job.status == "succeeded":
    # Create dedicated endpoint

    endpoint = client.endpoints.create(
        model=job.fine_tuned_model, type="dedicated", hardware="A100-40GB"
    )
    print(f"Endpoint created: {endpoint.id}")
```

**Iterative Model Improvement Workflow**
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
