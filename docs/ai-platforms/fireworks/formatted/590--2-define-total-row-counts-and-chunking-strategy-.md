---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 2. Define Total Row Counts and Chunking Strategy ---

TOTAL_ROW_COUNTS = {name: TARGET_ROW_COUNT for name in table_names}
ROWS_PER_API_CALL = 2 # Ask for data in small, safe chunks

print("\n✅ Data Generation Plan:")
print(f" - Target rows per table: {list(TOTAL_ROW_COUNTS.values())[0]}")
print(f" - Will make API calls asking for {ROWS_PER_API_CALL} rows/call until target is met.")


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
