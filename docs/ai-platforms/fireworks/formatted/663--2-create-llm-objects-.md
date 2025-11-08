---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 2. Create LLM Objects ---

model_1_llm = None
model_2_llm = None
model_3_llm = None
try:
    model_1_llm = LLM(model=MODEL_1_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    model_2_llm = LLM(model=MODEL_2_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    model_3_llm = LLM(model=MODEL_3_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    print("LLM objects for all three models created successfully.")
except Exception as e:
    print(f"FATAL: Could not create LLM objects. Error: {e}")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
