---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Filter out entries where 'ground_truth' is an empty list

original_count = len(final_generated_data)
final_generated_data = [entry for entry in final_generated_data if entry.get("ground_truth")]
print(f"Filtered out {original_count - len(final_generated_data)} examples with empty ground truth.")

print(f"Now splitting the remaining {len(final_generated_data)} examples into train and test sets.")

random.seed(42)
random.shuffle(final_generated_data)

split_index = int(len(final_generated_data) * 0.8)
train_data = final_generated_data[:split_index]
test_data = final_generated_data[split_index:]

print(f"Train set size: {len(train_data)}")
print(f"Test set size: {len(test_data)}")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
