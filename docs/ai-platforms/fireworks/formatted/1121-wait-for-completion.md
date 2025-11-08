---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Wait for completion

while not job.is_completed:
    job.raise_if_bad_state()
    time.sleep(1)
    job = job.get()
    if job is None:
        raise Exception("Job was deleted while waiting for completion")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
