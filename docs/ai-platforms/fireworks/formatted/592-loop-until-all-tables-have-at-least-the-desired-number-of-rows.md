---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Loop until all tables have at least the desired number of rows

while not all(len(rows) >= TOTAL_ROW_COUNTS[name] for name, rows in all_synthetic_data.items()):
    call_count += 1
    print(f"\n📞 --- Generating data chunk #{call_count} ---")
    
    # --- Create a summary of existing data to guide the LLM ---

    existing_data_summary = ""
    if any(len(rows) > 0 for rows in all_synthetic_data.values()):
        summary_parts = ["\nYou have already generated the following data. Do NOT generate rows that are substantially similar to these examples. Create new, unique data.\n"]
        for table_name, rows in all_synthetic_data.items():
            if rows:
                summary_parts.append(f"\n--- Existing data in '{table_name}' table ---")
                sample_rows = rows[-100:] if len(rows) > 100 else rows  # sample the last 100 rows

                df = pd.DataFrame(sample_rows)
                if len(df.columns) > 10:
                    df = df.iloc[:, :10]
                markdown_summary = df.to_markdown(index=False, tablefmt="grid")
                if markdown_summary:
                    summary_parts.append(markdown_summary)
        existing_data_summary = "\n".join(summary_parts)


    # --- Construct the final prompt for this iteration ---

    final_prompt = (
        base_generation_prompt +
        existing_data_summary +
        f"\n\nNow, generate a NEW JSON object with a key for each table. The number of new rows for each table should be:\n" +
        json.dumps(chunk_row_counts, indent=2)
    )

    response = llm.chat.completions.create(
        messages=[{"role": "user", "content": final_prompt}],
        response_format={"type": "json_schema", "json_schema": {"name": "SyntheticDataset", "schema": SyntheticDataset.model_json_schema()}},
        temperature=0.7
    )

    choice = response.choices[0]
    response_content = choice.message.content

    if choice.finish_reason == "length":
        print(f"⚠️ WARNING: Chunk #{call_count} was truncated. Skipping.")
        continue
    if not response_content:
        print(f"⚠️ WARNING: Received empty content for chunk #{call_count}. Skipping.")
        continue

    try:
        chunk_data = json.loads(response_content)
        print(f"✅ Received and parsed chunk #{call_count}.")
        for table_name, rows in chunk_data.items():
            if table_name in all_synthetic_data and rows:
                all_synthetic_data[table_name].extend(rows)
        # Log progress

        for name, rows in all_synthetic_data.items():
             print(f"   - '{name}': {len(rows)} / {TOTAL_ROW_COUNTS[name]} rows")
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Failed to parse JSON for chunk #{call_count}. Reason: {e}. Skipping.")
    
    time.sleep(1)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
