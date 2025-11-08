---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 4. Save the Ground-Truth Data ---

with open(GROUND_TRUTH_FILE_PATH, 'w') as f:
    for entry in ground_truth_results:
        f.write(json.dumps(entry) + '\n')

print(f"\n✅ Successfully saved {len(ground_truth_results)} ground-truth results to `{GROUND_TRUTH_FILE_PATH}`.")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
