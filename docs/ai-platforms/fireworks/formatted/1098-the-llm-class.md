---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The `LLM()` class

Running a model on Fireworks is as simple as instantiating the `LLM` class and
calling a single function. Here's an example of how to instantiate the latest
[Llama 4 Maverick model](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic) using the Build SDK.
```python main.py {3} theme={null}
from fireworks import LLM

llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="serverless")

response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)
```
You can send various parameters to the `LLM()` constructor to take full advantage of all of Fireworks' customization options.
```python main.py {2-8} theme={null}
llm = LLM(
  model="qwen2p5-72b-instruct",
  id="my-deployment-id",
  deployment_type="on-demand",
  precision="FP8",
  accelerator_type="NVIDIA_H100_80GB",
  draft_model="qwen2p5-0p5b-instruct",
  draft_token_count=4,
  min_replica_count=1,
) 

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
