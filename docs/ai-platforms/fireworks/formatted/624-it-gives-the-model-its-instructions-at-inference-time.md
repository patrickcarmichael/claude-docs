---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## It gives the model its instructions at inference time.

rft_system_prompt = f"""
You are an expert SQL data analyst.
Your task is to write a single, valid DuckDB SQL query to answer the user's question, based on the provided database schema.
Write only the raw SQL query text and nothing else (i.e., no markdown formatting); your output should be a directly executable valid SQL query.
Make sure your queries do not return duplicate rows (i.e., GROUP BY all columns that are not aggregate functions).
Ensure the generated SQL is valid for DuckDB.

**Database Schema:**
{schema_for_prompt}
""".strip()

final_generated_data = []
print(f"Generating natural language questions and formatting for RFT for {len(query_result_pairs)} queries...")

for i, pair in enumerate(query_result_pairs):
    print(f" - Processing query {i+1}/{len(query_result_pairs)}...")
    query = pair['query']
    ground_truth = pair['result']
    nl_generation_prompt = nl_generation_prompt_template.format(schema_for_prompt=schema_for_prompt, query=query)
    
    response = llm.chat.completions.create(
        messages=[{"role": "user", "content": nl_generation_prompt}],
        temperature=0.5
    )
    
    nl_question = response.choices[0].message.content
    if nl_question:  # Only include the entry if the LLM generated a question

        # Assemble the final data structure

        rft_entry = {
            "messages": [
                {"role": "system", "content": rft_system_prompt},
                {"role": "user", "content": nl_question.strip()},
                {"role": "assistant", "content": query}
            ],
            "ground_truth": ground_truth  # The ground-truth result for the evaluator

        }
        final_generated_data.append(rft_entry)
    
    time.sleep(0.5) # Be nice to the API

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
