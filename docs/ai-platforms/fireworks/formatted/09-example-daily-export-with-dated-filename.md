---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example: Daily export with dated filename

firectl export billing-metrics \
  --start-time "$(date -v-1d '+%Y-%m-%d')" \
  --end-time "$(date '+%Y-%m-%d')" \
  --filename "billing_$(date '+%Y%m%d').csv"
```

<Tip>
  Run `firectl export billing-metrics --help` to see all available flags and options.
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
