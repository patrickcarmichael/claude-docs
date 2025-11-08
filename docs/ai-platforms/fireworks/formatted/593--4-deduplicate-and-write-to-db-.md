---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 4. Deduplicate and Write to DB ---

print("\n✨ Data generation complete. Aggregating, deduplicating, and saving to database...")

synthetic_data = all_synthetic_data
print("\n--- Deduplicating generated data ---")
for table_name, rows in synthetic_data.items():
    if not rows: continue
    initial_count = len(rows)
    df = pd.DataFrame(rows).drop_duplicates()
    final_count = len(df)
    synthetic_data[table_name] = df.to_dict('records')
    print(f" - Table '{table_name}': Removed {initial_count - final_count} duplicates ({initial_count} -> {final_count}).")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
