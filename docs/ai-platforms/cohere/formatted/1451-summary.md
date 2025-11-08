---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## summary

"""

prompt = prompt_template.format(text=text)
resp = co.chat(
  message=prompt,
  model=co_model,
  temperature=0.3,
  return_prompt=True
)

num_tokens_in = co.tokenize(resp.prompt).length
num_tokens_out = resp.meta["billed_units"]["output_tokens"]
print(f"Generated summary with {num_tokens_in} tokens in, {num_tokens_out} tokens out")
print()
print("--- Out-of-the-box summary with Command-R ---")
print()
print(resp.text)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
