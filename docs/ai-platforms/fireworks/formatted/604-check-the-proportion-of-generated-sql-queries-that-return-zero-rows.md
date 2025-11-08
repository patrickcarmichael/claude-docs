---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Check the proportion of generated SQL queries that return zero rows

import json
import duckdb

try:
    SYNTHETIC_DB_PATH
except NameError:
    SYNTHETIC_DB_PATH = "data/synthetic_openflights.db"

try:
    QUERIES_FILE_PATH
except NameError:
    QUERIES_FILE_PATH = "data/generated_queries.json"

with open(QUERIES_FILE_PATH, "r") as f:
    queries = json.load(f).get("queries", [])

total = len(queries)
zero_rows = 0
success = 0
failed = 0

with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con:
    for q in queries:
        try:
            cnt = con.sql(f"SELECT COUNT(*) AS c FROM ({q}) AS t").fetchone()[0]
            zero_rows += (cnt == 0)
            success += 1
        except Exception:
            failed += 1

print(f"Total queries: {total}")
print(f"Executed successfully: {success}")
print(f"Execution errors: {failed}")
print(f"Zero-row results: {zero_rows}")
if total > 0:
    print(f"Proportion zero-row (overall): {zero_rows/total:.3f}")
if success > 0:
    print(f"Proportion zero-row (successful only): {zero_rows/success:.3f}")
```

Total queries: 549
Executed successfully: 516
Execution errors: 33
Zero-row results: 211
Proportion zero-row (overall): 0.384
Proportion zero-row (successful only): 0.409

### 6. ♻️ Query-Aware Augmentation of the Synthetic Sandbox

To reduce empty results when executing our SQL queries, we augment the synthetic data to be "query-aware." We identify queries that return zero rows and generate minimal, natural-looking data that satisfies their conditions.

#### Why this matters

* **Higher coverage**: More queries produce non-empty results, improving label quality for RFT
* **Minimal changes**: Only adds the data needed to satisfy queries
* **Natural data**: Generated rows look realistic and maintain referential integrity

#### How it works

1. Execute all queries and identify those returning zero rows
2. Process zero-result queries in batches of 10, grouped by involved tables
3. Use the LLM to generate 1-2 new rows per table that satisfy the query conditions
4. Insert rows, check which queries were fixed, and repeat until ≤10% return zero results
5. Remove any duplicate rows

The process tracks which queries have been attempted to avoid redundant processing and can retry stubborn queries up to 2 times.

>   **Real World 🌍**: Run the cell below against your synthetic data and real queries. The code is domain-agnostic and will work with any SQL database schema.
```python
import os, json, re, time
import pandas as pd
import duckdb
from typing import List, Optional, Any, Dict, Type, Set
from pydantic import BaseModel, create_model
from fireworks import LLM
import datetime, decimal, uuid
from collections import defaultdict
from dotenv import load_dotenv

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
