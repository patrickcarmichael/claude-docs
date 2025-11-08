---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 2. Load Ground-Truth Data ---

query_result_pairs = []
with jsonlines.open(GROUND_TRUTH_FILE_PATH) as reader:
    for obj in reader:
        query_result_pairs.append(obj)

print(f"Loaded {len(query_result_pairs)} query-result pairs.")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
