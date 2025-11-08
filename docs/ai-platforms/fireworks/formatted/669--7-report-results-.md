---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 7. REPORT RESULTS ---

if dataset:
    total = len(dataset)
    model_1_accuracy = (model_1_score / total) * 100
    model_2_accuracy = (model_2_score / total) * 100
    model_3_accuracy = (model_3_score / total) * 100

    print("\n" + "="*25)
    print("  EVALUATION COMPLETE")
    print("="*25)
    print(f"Total Examples: {total}\n")
    
    print("--- MODEL 1 ---")
    print(f"Model ID: {MODEL_1_ID}")
    print(f"Correct: {model_1_score}/{total}")
    print(f"Accuracy: {model_1_accuracy:.2f}%\n")

    print("--- MODEL 2 ---")
    print(f"Model ID: {MODEL_2_ID}")
    print(f"Correct: {model_2_score}/{total}")
    print(f"Accuracy: {model_2_accuracy:.2f}%\n")

    print("--- MODEL 3 ---")
    print(f"Model ID: {MODEL_3_ID}")
    print(f"Correct: {model_3_score}/{total}")
    print(f"Accuracy: {model_3_accuracy:.2f}%\n")

    # Write final summary to log file

    write_to_log("="*25)
    write_to_log("  EVALUATION COMPLETE")
    write_to_log("="*25)
    write_to_log(f"Total Examples: {total}")
    write_to_log(f"--- MODEL 1 --- Model ID: {MODEL_1_ID} | Correct: {model_1_score}/{total} | Accuracy: {model_1_accuracy:.2f}%")
    write_to_log(f"--- MODEL 2 --- Model ID: {MODEL_2_ID} | Correct: {model_2_score}/{total} | Accuracy: {model_2_accuracy:.2f}%")
    write_to_log(f"--- MODEL 3 --- Model ID: {MODEL_3_ID} | Correct: {model_3_score}/{total} | Accuracy: {model_3_accuracy:.2f}%")

else:
    msg = "Evaluation skipped because the dataset or LLM objects could not be loaded"
    print(msg)
    write_to_log(f"WARNING: {msg}")
```
```text
    LLM objects for all three models created successfully.
    Loaded 92 evaluation examples from 'data/final_rft_sql_test_data.jsonl'.
    Manual logging configured. Log file is 'evaluation_manual_open.log'.
    
    Starting evaluation...


    Evaluating models: 100%|██████████| 92/92 [16:59<00:00, 11.08s/it]

    
    =========================
      EVALUATION COMPLETE
    =========================
    Total Examples: 92
    
    --- MODEL 1 ---
    Model ID: accounts/fireworks/models/qwen3-coder-480b-a35b-instruct
    Correct: 32/92
    Accuracy: 34.78%
    
    --- MODEL 2 ---
    Model ID: accounts/fireworks/models/kimi-k2-instruct
    Correct: 26/92
    Accuracy: 28.26%
    
    --- MODEL 3 ---
    Model ID: accounts/fireworks/models/deepseek-v3
    Correct: 25/92
    Accuracy: 27.17%
```

#### Testing proprietary models

````python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
