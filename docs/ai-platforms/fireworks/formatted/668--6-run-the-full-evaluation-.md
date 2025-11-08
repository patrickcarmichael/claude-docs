---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 6. RUN THE FULL EVALUATION ---

model_1_score = 0
model_2_score = 0
model_3_score = 0

if dataset:
    msg = "\nStarting evaluation..."
    print(msg)
    write_to_log(msg.strip())
    for item in tqdm(dataset, desc="Evaluating models"):
        system_prompt = item["messages"][0]["content"]
        user_prompt = item["messages"][1]["content"]
        ground_truth = item["ground_truth"]

        # Evaluate model 1

        model_1_score += get_sql_and_evaluate(model_1_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)  # Be nice to the API

        # Evaluate model 2

        model_2_score += get_sql_and_evaluate(model_2_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)

        # Evaluate model 3

        model_3_score += get_sql_and_evaluate(model_3_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
