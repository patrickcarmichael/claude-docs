---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## ✅ Keep system prompt static, add time context to user message

system_prompt = """
You are a helpful AI assistant...
""" # This stays the same

user_message = f"""
Current time: {datetime.now().isoformat()}

User query: {user_query}
"""

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
