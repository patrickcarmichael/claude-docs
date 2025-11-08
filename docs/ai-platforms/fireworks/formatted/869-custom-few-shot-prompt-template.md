---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Custom few-shot prompt template

prompt = """Task: Classify the sentiment of the following text.

Text: I love this product!
Sentiment: Positive

Text: This is terrible.
Sentiment: Negative

Text: The weather is nice today.
Sentiment:"""

response = client.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    prompt=prompt,
    max_tokens=10,
    temperature=0
)

print(response.choices[0].text)  # Output: " Positive"

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
