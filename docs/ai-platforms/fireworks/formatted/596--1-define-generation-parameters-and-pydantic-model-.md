---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 1. Define Generation Parameters and Pydantic Model ---

llm = LLM(model="accounts/fireworks/models/qwen3-coder-480b-a35b-instruct", deployment_type="serverless", api_key=os.getenv("FIREWORKS_API_KEY"))  # Use Qwen3-coder for SQL queries

TOTAL_QUERIES_TO_GENERATE = 1000  # Note, some of these queries will likely be duplicates or invalid, reducing the final number used for fine-tuning

QUERIES_PER_API_CALL = 30

class SqlQueryBatch(BaseModel):
    queries: List[str] = Field(description=f"A list of exactly {QUERIES_PER_API_CALL} unique and diverse SQL queries.")

print(f"🎯 Goal: Generate {TOTAL_QUERIES_TO_GENERATE} unique queries in batches of {QUERIES_PER_API_CALL}.")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
