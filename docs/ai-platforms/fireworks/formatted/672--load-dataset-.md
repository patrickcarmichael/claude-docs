---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- Load Dataset ---

dataset = []
try:
    with open(DATASET_FILE_PATH, 'r') as f:
        dataset = [json.loads(line) for line in f]
    print(f"Loaded {len(dataset)} evaluation examples from '{DATASET_FILE_PATH}'.")
except Exception as e:
    print(f"FATAL: Could not load dataset. Error: {e}")
    dataset = []

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
