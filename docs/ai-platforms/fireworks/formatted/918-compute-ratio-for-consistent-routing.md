---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Compute ratio for consistent routing

ratio = hashed_user_id / MAX_HASH # Returns 0.0 to 1.0

if (ratio < fireworks_traffic_fraction):
    send_to_new_deployment(user=hashed_user_id)  # Pass user ID for caching

else:
    send_elsewhere()  # Route to old deployment or serverless

```
>   **⚠️ Warning**
>
> Avoid random sampling for traffic routing as it can negatively impact cache hit rates:
```python
  # Don't do this:

  if random() < fireworks_traffic_fraction:  # ❌ Reduces cache effectiveness

    send_to_new_deployment(user=hashed_user_id)
```
  Using consistent user-based routing ensures complete user sessions are maintained on the same deployment, optimizing prompt cache performance regardless of the traffic fraction.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
