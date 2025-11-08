---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Display summary of results

print("\nPercentage of questions won by each engine:")
for engine, count in winner_counts.items():
    percentage = (count / total_queries) * 100
    print(f"{engine}: {percentage:.2f}% ({count}/{total_queries})")
    

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
