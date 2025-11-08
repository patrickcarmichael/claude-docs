---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 5. Save the Final RFT-Ready Datasets ---

with jsonlines.open(FINAL_TRAINING_DATA_PATH, mode='w') as writer:
    writer.write_all(train_data)
print(f"\n✅ Successfully saved training dataset to `{FINAL_TRAINING_DATA_PATH}`.")

with jsonlines.open(FINAL_TEST_DATA_PATH, mode='w') as writer:
    writer.write_all(test_data)
print(f"✅ Successfully saved test dataset to `{FINAL_TEST_DATA_PATH}`.")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
