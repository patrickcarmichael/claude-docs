---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## A practical example for logprobs: Classification

In this example, we're building an email classifier and we want to know how confident the model is in its answer. We give the LLM 4 categories in the system prompt then pass in an example email.
```python
  from together import Together
  import json

  client = Together()

  completion = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "system",
              "content": "You are a helpful email categorizer. Given an email, please classify it as one of the following categories: 'work', 'personal', 'spam', or 'other'. ONLY respond with the category name.",
          },
          {
              "role": "user",
              "content": "I hope this message finds you well. I am writing to request a meeting next week to discuss the progress of Project X. We have reached several key milestones, and I believe it would be beneficial to review our current status and plan the next steps together.Could we schedule a time that works best for you? Please let me know your availability between Tuesday and Thursday next week. Also, lmk if you still wanna grab dinner on Friday!.",
          },
      ],
      logprobs=1,
  )

  print(completion.choices[0].logprobs.top_logprobs)
```

The output is the following:
```json
[{'work': -0.012512207}, {'<|eot_id|>': -0.005706787}]
```

This means that the model chose "work" as the answer, which is correct, and the logprob for work was `-0.012512207`. After taking the exponential of this, we get a probability of 98.7%. We're using a small and fast LLM here (llama 3.1 8B) which is great, but using logprobs, we can also tell when the model is unsure of its answer and see if we need to route it to a bigger LLM.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
