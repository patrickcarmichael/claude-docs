---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Loop until we have enough queries

while len(all_generated_queries) < TOTAL_QUERIES_TO_GENERATE:
    print(f"\n📞 --- Generating batch #{len(all_generated_queries) // QUERIES_PER_API_CALL + 1} ---")

    # Create a summary of queries generated so far to prevent duplicates

    existing_queries_summary = ""
    if all_generated_queries:
        summary_parts = ["\nYou have already generated the following queries:\n"]
        for i, q in enumerate(all_generated_queries):
            summary_parts.append(f"{i+1}. {q}")
        existing_queries_summary = "\n".join(summary_parts)

    # Construct the final prompt for this iteration

    final_prompt = (
        base_query_generation_prompt +
        existing_queries_summary +
        f"\n\nNow, generate {QUERIES_PER_API_CALL} new, unique SQL queries, which cover different analytic scenarios and are not already in the list above. Return your response as a single JSON object adhering to the specified schema."
    )

    response = llm.chat.completions.create(
        messages=[{"role": "user", "content": final_prompt}],
        response_format={"type": "json_schema", "json_schema": {"name": "SqlQueryBatch", "schema": SqlQueryBatch.model_json_schema()}},
        temperature=0.8
    )

    response_content = response.choices[0].message.content
    if response_content:
        try:
            new_queries = json.loads(response_content).get("queries", [])
            all_generated_queries.extend(new_queries)
            print(f"   - Received {len(new_queries)} new queries. Total now: {len(all_generated_queries)} / {TOTAL_QUERIES_TO_GENERATE}")
        except json.JSONDecodeError as e:
            print(f"❌ ERROR: Failed to parse generated queries in this batch: {e}")
    
    time.sleep(1) # Be nice to the API

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
