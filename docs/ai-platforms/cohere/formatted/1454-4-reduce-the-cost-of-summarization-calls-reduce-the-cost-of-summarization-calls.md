---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Reduce the cost of summarization calls \[#reduce-the-cost-of-summarization-calls]

Even though Command-R is an efficient, light-weight model, for some applications we may accept trading off some summarization quality for lower costs. To do this, we must reduce the amount of tokens sent to the model -- but how do we select the most relevant bits?

We have a whole notebook dedicated to methods for reducing context length. Here, we call our 'text-rank' method to select maximally central chunks in a graph based on the chunk-to-chunk similarties. For more detail, please refer [to this cookbook](https://colab.research.google.com/drive/1zxSAbruOWwWJHNsj3N56uxZtUeiS7Evd).
```python PYTHON
num_tokens = 8192
shortened = textrank(text, co, num_tokens, n_sentences_per_passage=30)

chunked = build_simple_chunks(shortened)
resp = co.chat(
  message=instructions,
  documents=[{"text": chunk} for chunk in chunked],
  model=co_model,
  temperature=0.3,
  return_prompt=True
)

num_tokens_in = co.tokenize(resp.prompt).length
num_tokens_out = resp.meta["billed_units"]["output_tokens"]
print(f"Generated summary with {num_tokens_in} tokens in, {num_tokens_out} tokens out")
print()
print("--- Summary with citations using text-rank + grounding in Command-R ---")
print()
print(resp.text)
```
The summary is looking convincing! In practice, the trade-off between cost-efficiency and performance should be considered carefully.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
