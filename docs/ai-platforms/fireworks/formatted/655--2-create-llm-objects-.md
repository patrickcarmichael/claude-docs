---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 2. Create LLM Objects ---

base_model_llm = None
large_base_model_llm = None
fine_tuned_model_llm = None
try:
    base_model_llm = LLM(model=BASE_MODEL_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    large_base_model_llm = LLM(model=LARGE_BASE_MODEL_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    fine_tuned_model_llm = LLM(model=FINE_TUNED_MODEL_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    print("LLM objects for all three models created successfully.")
except Exception as e:
    print(f"FATAL: Could not create LLM objects. Error: {e}")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
