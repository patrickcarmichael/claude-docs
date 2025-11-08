---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Final cleanup - remove exact duplicates

print("\n--- Final deduplication ---")
with duckdb.connect(SYNTHETIC_DB_PATH) as con:
    tables = con.sql("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_type = 'BASE TABLE' 
        AND table_schema = 'main'
    """).fetchall()
    
    for (table_name,) in tables:
        before = con.sql(f'SELECT COUNT(*) FROM "{table_name}"').fetchone()[0]
        con.execute(f'CREATE OR REPLACE TABLE "{table_name}" AS SELECT DISTINCT * FROM "{table_name}"')
        after = con.sql(f'SELECT COUNT(*) FROM "{table_name}"').fetchone()[0]
        if before != after:
            print(f"  {table_name}: removed {before - after} duplicate rows")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
