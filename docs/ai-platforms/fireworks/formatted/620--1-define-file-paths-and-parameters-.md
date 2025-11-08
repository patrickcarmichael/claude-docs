---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 1. Define File Paths and Parameters ---

llm = LLM(model="accounts/fireworks/models/qwen3-coder-480b-a35b-instruct", deployment_type="serverless", api_key=os.getenv("FIREWORKS_API_KEY"))
GROUND_TRUTH_FILE_PATH = "data/ground_truth_results.jsonl"
FINAL_TRAINING_DATA_PATH = "data/final_rft_sql_train_data.jsonl"
FINAL_TEST_DATA_PATH = "data/final_rft_sql_test_data.jsonl"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
