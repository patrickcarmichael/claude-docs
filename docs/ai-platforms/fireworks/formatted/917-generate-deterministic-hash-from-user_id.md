---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate deterministic hash from user_id

hashed_user_id = int(hashlib.md5(user_id.encode()).hexdigest(), 16) # MD5 hash on user-id and convert to integer

MAX_HASH = 2**128 - 1  # MD5 hash maximum value

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
