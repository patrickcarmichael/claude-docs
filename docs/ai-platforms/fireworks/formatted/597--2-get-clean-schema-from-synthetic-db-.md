---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 2. Get Clean Schema From Synthetic DB ---

with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con:
    schema_df = con.sql("DESCRIBE;").df()
    schema_for_prompt = schema_df.to_markdown(index=False)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
