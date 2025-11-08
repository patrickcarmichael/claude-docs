---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Examples

Export all billing metrics for an account:
```bash
firectl export billing-metrics
```

Export metrics for a specific date range and filename:
```bash
firectl export billing-metrics \
  --start-time "2025-01-01" \
  --end-time "2025-01-31" \
  --filename january_metrics.csv
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
