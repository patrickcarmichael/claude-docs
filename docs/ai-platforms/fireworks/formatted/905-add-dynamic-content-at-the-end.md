---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Add dynamic content at the end

if user_context:
    user_message += f"User context: {user_context}\n\n"

if current_time_needed:
    user_message += f"Current time: {datetime.now().isoformat()}\n\n"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
