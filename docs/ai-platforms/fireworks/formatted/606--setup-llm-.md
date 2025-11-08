---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- Setup LLM ---

load_dotenv()
llm = LLM(
    model="accounts/fireworks/models/qwen3-coder-480b-a35b-instruct",
    deployment_type="serverless",
    api_key=os.getenv("FIREWORKS_API_KEY"),
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
