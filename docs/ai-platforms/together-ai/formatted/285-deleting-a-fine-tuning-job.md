---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deleting a fine-tuning job

You can also delete your fine-tuning job. This action can not be undone. This will destroy all files produced by your job including intermediate and final checkpoints.
```python
  ## Run delete

  resp = client.fine_tuning.delete(ft_resp.id)
  print(resp)
```
```bash
  ## Using CLI

  together fine-tuning delete "your-job-id"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
