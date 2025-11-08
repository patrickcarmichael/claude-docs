---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Connect to the "production" database we just created

with duckdb.connect(PROD_DB_PATH, read_only=True) as con:
    # The DESCRIBE command gives us the schema information for all tables

    schema_df = con.sql("DESCRIBE;").df()

print("✅ Schema successfully extracted from 'production' database:")
print(schema_df.to_markdown(index=False))

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
