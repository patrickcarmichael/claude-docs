---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Monitor training progress

while not job.is_completed:
    job.raise_if_bad_state()
    print(f"Training state: {job.state}")
    time.sleep(10)
    job = job.get()
    if job is None:
        raise Exception("Job was deleted while waiting for completion")

print(f"Training completed! New model: {job.output_model}")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
