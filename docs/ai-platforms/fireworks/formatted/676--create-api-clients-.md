---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- Create API Clients ---

openai_client = None
anthropic_client = None
try:
    openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    print("OpenAI and Anthropic clients created successfully.")
except Exception as e:
    print(f"FATAL: Could not create clients. Error: {e}")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
