---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Configure dspy with a LLM from Together AI

lm = dspy.LM(
    "together_ai/togethercomputer/llama-2-70b-chat",
    api_key=os.environ.get("TOGETHER_API_KEY"),
    api_base="https://api.together.xyz/v1",
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
