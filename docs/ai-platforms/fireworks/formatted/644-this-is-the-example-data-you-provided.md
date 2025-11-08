---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## This is the example data you provided.

DATASET_FILE_PATH = "data/final_rft_sql_train_data.jsonl"
ROW_INDEX_TO_TEST = 0  # 0 is the first row, 1 is the second row, etc.

EXAMPLE_DATA = None
try:
    with open(DATASET_FILE_PATH, 'r') as f:
        for i, line in enumerate(f):
            if i == ROW_INDEX_TO_TEST:
                EXAMPLE_DATA = json.loads(line)
                break
    
    if EXAMPLE_DATA is None:
        with open(DATASET_FILE_PATH, 'r') as f:
            line_count = sum(1 for line in f)
        raise IndexError(f"row index {ROW_INDEX_TO_TEST} is out of bounds for file with {line_count} rows.")

    print(f"Successfully loaded row {ROW_INDEX_TO_TEST} from '{DATASET_FILE_PATH}'.\n")
    print(EXAMPLE_DATA)
    print()

except Exception as e:
    print(f"Warning: Could not load from file. Reason: {e}")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
