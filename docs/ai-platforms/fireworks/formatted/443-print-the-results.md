---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print the results

print(f"Score: {result.score}")
print("Metrics:")
for name, metric in result.metrics.items():
    print(f"  {name}: {metric.score}")
    print(f"    {metric.reason}")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
