---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Converting logprobs to probabilities

Let's take the first token from the previous example: `{ "New": -0.39648438 }`. The "New" token has a logprob of -0.39648438, but this isn't very helpful by itself. However, we can quickly convert it to a probability by taking the exponential of it.
```python
  import math


  def get_probability(logprob: float) -> float:
      return round(math.exp(logprob) * 100, 2)


  print(get_probability(-0.39648438))
  # 67.02%

```

This tells us that the model's confidence in starting with "New" was 67%. Let's now look at a practical example where this would be useful.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
