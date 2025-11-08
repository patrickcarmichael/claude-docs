---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 3. Setup Base Prompt and Generation Loop ---

base_query_generation_prompt = f"""
You are an expert SQL data analyst. Your task is to generate unique and diverse SQL queries based on the database schema provided.
The queries should be realistic and cover a range of complexities and SQL features (JOINS, GROUP BY, aggregates, etc.).
Ensure you break ties with ORDER BY clauses so that the same queries produce the same results when executed against the database.
Write only the raw SQL query text and nothing else (i.e., no markdown formatting); your output should be a directly executable valid SQL query.
Make sure your queries do not return duplicate rows (i.e., GROUP BY all columns that are not aggregate functions).
Ensure the generated SQL is valid for DuckDB.

**Database Schema:**
{schema_for_prompt}
""".strip()

all_generated_queries = []

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
