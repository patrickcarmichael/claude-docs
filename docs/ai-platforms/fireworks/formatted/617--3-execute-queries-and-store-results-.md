---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 3. Execute Queries and Store Results ---

ground_truth_results = []
successful_executions = 0
failed_executions = 0
oversized_skipped = 0

print("Executing queries against the synthetic database...")
with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con:
    for query in queries_to_execute:
        try:
            result_df = con.sql(query).df()

            # Replace any NaN/NaT values with None, which serializes to JSON `null`

            result_df = result_df.astype(object).where(pd.notna(result_df), None)
            result_records = result_df.to_dict('records')

            # Skip examples that are "much too wide"

            if len(result_records) > MAX_RESULT_ROWS:
                oversized_skipped += 1
                continue
            # Size-based guard (in bytes)

            payload_bytes = len(json.dumps(result_records, ensure_ascii=False).encode("utf-8"))
            if payload_bytes > MAX_RESULT_BYTES:
                oversized_skipped += 1
                continue

            ground_truth_results.append({
                "query": query,
                "result": result_records
            })
            successful_executions += 1
        except Exception as e:
            print(f"⚠️  Skipping query due to execution error: {query}\n   Error: {e}\n")
            failed_executions += 1

print(f"\nExecution complete. Success: {successful_executions}, Skipped (oversized): {oversized_skipped}, Failed: {failed_executions}.")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
