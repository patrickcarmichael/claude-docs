---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- Pre-evaluation Check ---

print("\n--- Pre-evaluation Check ---")
dataset_exists = 'dataset' in locals()
clients_exist = all([openai_client, anthropic_client])
print(f"1. 'dataset' variable exists: {dataset_exists}")
if dataset_exists:
    print(f"2. 'dataset' is not empty: {bool(dataset)}")
else:
    print("2. 'dataset' is not empty: N/A (Does not exist)")
print(f"3. OpenAI client created: {bool(openai_client)}")
print(f"4. Anthropic client created: {bool(anthropic_client)}")
print("--------------------------\n")

if dataset_exists and dataset and clients_exist:
    print("\nStarting evaluation for OpenAI and Anthropic models...")
    for item in tqdm(dataset, desc="Evaluating OpenAI/Anthropic"):
        system_prompt = item["messages"][0]["content"]
        user_prompt = item["messages"][1]["content"]
        ground_truth = item["ground_truth"]

        gpt_model_score += get_sql_and_evaluate_openai(openai_client, GPT_MODEL_ID, system_prompt, user_prompt, ground_truth)
        time.sleep(0.5)

        claude_model_score += get_sql_and_evaluate_anthropic(anthropic_client, CLAUDE_MODEL_ID, system_prompt, user_prompt, ground_truth)
        time.sleep(0.5)

    # --- 6. REPORT RESULTS for OpenAI and Anthropic ---

    total = len(dataset)
    gpt_accuracy = (gpt_model_score / total) * 100
    claude_accuracy = (claude_model_score / total) * 100

    print("\n" + "="*25)
    print("  EVALUATION COMPLETE")
    print("="*25)
    print(f"Total Examples: {total}\n")
    print("--- GPT MODEL (OpenAI) ---")
    print(f"Model ID: {GPT_MODEL_ID}")
    print(f"Correct: {gpt_model_score}/{total}")
    print(f"Accuracy: {gpt_accuracy:.2f}%\n")
    print("--- CLAUDE MODEL (Anthropic) ---")
    print(f"Model ID: {CLAUDE_MODEL_ID}")
    print(f"Correct: {claude_model_score}/{total}")
    print(f"Accuracy: {claude_accuracy:.2f}%\n")

else:
    print("\nEvaluation for OpenAI and Anthropic models skipped.")
    print("One of the pre-evaluation checks failed. Please check the output above.")
````
```text
    Loaded 92 evaluation examples from 'data/final_rft_sql_test_data.jsonl'.
    Manual logging configured. Log file is 'evaluation_manual_proprietary.log'.
    OpenAI and Anthropic clients created successfully.
    
    --- Pre-evaluation Check ---
    1. 'dataset' variable exists: True
    2. 'dataset' is not empty: True
    3. OpenAI client created: True
    4. Anthropic client created: True
    --------------------------
    
    
    Starting evaluation for OpenAI and Anthropic models...


    Evaluating OpenAI/Anthropic: 100%|██████████| 92/92 [08:06<00:00,  5.28s/it]

    
    =========================
      ADDITIONAL MODELS EVALUATION COMPLETE
    =========================
    Total Examples: 92
    
    --- GPT MODEL (OpenAI) ---
    Model ID: gpt-4o
    Correct: 22/92
    Accuracy: 23.91%
    
    --- CLAUDE MODEL (Anthropic) ---
    Model ID: claude-sonnet-4-20250514
    Correct: 27/92
    Accuracy: 29.35%
```
<div style={{ fontSize: '0.8em' }}>
  > Note that Claude Sonnet 4 and GPT-4o sometimes output SQL queries wrapped in markdown formatting like \`\`\`sql \<query\_here>\`\`\`, so we added a helper function to clean the output before executing the SQL query in those cases.
</div>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
