---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 6. Call Generative Model - Llama 405b

We will pass the final 3 concatenated chunks into an LLM to get our final answer.
```py
query = "What are 'skip-level' meetings?"

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "You are a helpful chatbot."},
        {
            "role": "user",
            "content": f"Answer the question: {query}. Use only information provided here: {reranked_chunks}",
        },
    ],
)

response.choices[0].message.content
```
If you want to learn more about how to best use open models refer to our [docs](/docs) here!


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
