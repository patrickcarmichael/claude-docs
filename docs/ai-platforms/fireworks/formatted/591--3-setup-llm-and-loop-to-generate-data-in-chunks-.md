---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 3. Setup LLM and Loop to Generate Data in Chunks ---

SYNTHETIC_DB_PATH = "data/synthetic_openflights.db"
load_dotenv()
llm = LLM(model="accounts/fireworks/models/deepseek-v3", deployment_type="serverless", api_key=os.getenv("FIREWORKS_API_KEY"))

all_synthetic_data: Dict[str, List[Dict]] = {name: [] for name in table_names}
chunk_row_counts = {name: ROWS_PER_API_CALL for name in table_names}

base_generation_prompt = f"""
You are a highly intelligent AI data generator. Your task is to create a realistic, synthetic dataset based on the provided database schema.
The data you generate must be internally consistent. For example, an `airline_id` in a `routes` table must correspond to an existing `airline_id` in an `airlines` table within this same generated chunk.
This applies to any schema you might be working with, not just airline-related data.
You must generate a single JSON object that strictly adheres to the provided JSON schema.

The database schema is as follows:
{schema_for_prompt}
"""

call_count = 0

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
