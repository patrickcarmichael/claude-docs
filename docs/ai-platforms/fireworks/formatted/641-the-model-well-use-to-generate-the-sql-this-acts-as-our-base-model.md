---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The model we'll use to generate the SQL. This acts as our "base" model.

LLM_MODEL = "accounts/fireworks/models/llama-v3p1-8b-instruct"
llm = LLM(model=LLM_MODEL, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
