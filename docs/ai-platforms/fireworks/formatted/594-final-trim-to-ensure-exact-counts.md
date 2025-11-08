---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Final trim to ensure exact counts

for table_name, total_rows_needed in TOTAL_ROW_COUNTS.items():
    if table_name in synthetic_data:
        synthetic_data[table_name] = synthetic_data[table_name][:total_rows_needed]

with duckdb.connect(SYNTHETIC_DB_PATH) as con:
    for table_name, rows in synthetic_data.items():
        if rows:
            df = pd.DataFrame(rows)
            schema_cols = schema_df[schema_df['name'] == table_name].iloc[0]['column_names']
            for col in schema_cols:
                if col not in df.columns: df[col] = None
            df = df[schema_cols]
            con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
    
    print(f"\n✅ Synthetic training sandbox created at: {SYNTHETIC_DB_PATH}")
    print("Tables created:", con.sql("SHOW TABLES;").fetchall())
```

#### 4. ✅ Validate the Sandbox

Let's run a few queries against our new synthetic database to ensure the LLM did a good job generating plausible, interconnected data.

We expect to see non-empty, realistic-looking data that follows the schema constraints.
```python
import duckdb
from tabulate import tabulate

SYNTHETIC_DB_PATH = "data/synthetic_openflights.db"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
