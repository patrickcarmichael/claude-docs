---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 4. GENERATE SQL QUERY USING THE LLM ---

print("="*20)
print("LLM QUERY GENERATION")
print("="*20)

model_generated_sql = ""
try:
    print(f"User prompt: {user_prompt}")
    print(f"Ground truth: {GROUND_TRUTH_ROWS}")
    print(f"Calling model '{LLM_MODEL}' to generate SQL query...")
    
    messages_for_llm = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    response = llm.chat.completions.create(
        model=LLM_MODEL,
        messages=messages_for_llm,
        temperature=0.0  # Set to 0 for deterministic output

    )
    
    model_generated_sql = response.choices[0].message.content.strip()
    print("\nModel Generated SQL Query:")
    print(model_generated_sql)
    
except Exception as e:
    print(f"\nAN ERROR OCCURRED during LLM call: {e}")


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
