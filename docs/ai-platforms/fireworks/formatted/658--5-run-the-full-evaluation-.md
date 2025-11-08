---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 5. RUN THE FULL EVALUATION ---

base_model_score = 0
large_base_model_score = 0
fine_tuned_model_score = 0

if dataset:
    print("\nStarting evaluation...")
    for item in tqdm(dataset, desc="Evaluating models"):
        system_prompt = item["messages"][0]["content"]
        user_prompt = item["messages"][1]["content"]
        ground_truth = item["ground_truth"]

        # Evaluate base model

        base_model_score += get_sql_and_evaluate(base_model_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)  # Be nice to the API

        # Evaluate large base model

        large_base_model_score += get_sql_and_evaluate(large_base_model_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)

        # Evaluate fine-tuned model

        fine_tuned_model_score += get_sql_and_evaluate(fine_tuned_model_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
