---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 5: Monitor training

print(f"Job started: {job.id}")
while job.status in ["pending", "running"]:
    job = client.fine_tuning.retrieve(job.id)
    print(f"Status: {job.status}")
    time.sleep(30)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
